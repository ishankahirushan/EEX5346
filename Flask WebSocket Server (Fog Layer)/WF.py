# WF.py
import requests
import threading
import asyncio
import websockets
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_Temperature_level = None
Setmode = "Manual"
threshold = 30  # Temperature threshold
clients = set()  # Track connected WebSocket clients


# --------------------------------------------
# Flask HTTP Routes
# --------------------------------------------
@app.route('/')
def index():
    return "Welcome to the Flask and WebSocket server!"


@app.route('/status')
def status():
    return jsonify({"status": "Server is running", "connections": len(clients)})


@app.route('/control', methods=['PUT'])
async def control_fan():
    if request.is_json:
        command = request.json.get("command")
        await send_command(command)
        return jsonify({"message": "Command sent", "data": command}), 200
    else:
        return jsonify({"error": "Invalid JSON data"}), 400


# --------------------------------------------
# Function to forward data to Django
# --------------------------------------------
def send_to_server(NodeId, h_level, c_level, f_level):
    data = {
        "NodeId": NodeId,
        "h_level": h_level,
        "c_level": c_level,
        "f_level": f_level,
    }
    response = requests.post("http://<Django Cloud IP>:8000/api/fan", json=data)
    print(f"Response from Django server:", response.status_code, response.reason)


# --------------------------------------------
# WebSocket Handler
# --------------------------------------------
async def websocket_handler(websocket):
    print("Client connected")
    global latest_Temperature_level, Setmode

    clients.add(websocket)
    try:
        async for message in websocket:
            # Message format: NodeId,humidity,temperature,fan_level
            NodeId, h_level, c_level, f_level = message.split(",")
            c_level = int(float(c_level))
            f_level = int(float(f_level))

            print(f"Received from client: {message}")

            # Send to Django only if temperature changed
            if c_level != latest_Temperature_level:
                latest_Temperature_level = c_level
                send_to_server(NodeId, h_level, c_level, f_level)

            # You can add AUTO mode logic here
            print(f'SetMode:', Setmode)

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        clients.remove(websocket)


# --------------------------------------------
# Send commands to connected WebSocket clients
# --------------------------------------------
async def send_command(command):
    global Setmode
    if clients:
        try:
            for client in clients:
                await client.send(command)
                print(f"Sent command {command} to client")
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected")
    else:
        print("No clients connected")


# --------------------------------------------
# Start WebSocket Server
# --------------------------------------------
async def start_websocket_server():
    async with websockets.serve(websocket_handler, "0.0.0.0", 8765):
        print("WebSocket server running on ws://0.0.0.0:8765")
        await asyncio.Future()  # Keep server running


# --------------------------------------------
# Start Flask in separate thread
# --------------------------------------------
def start_flask():
    app.run(host='0.0.0.0', port=5000)


# --------------------------------------------
# Main Entry
# --------------------------------------------
if __name__ == "__main__":
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()

    # Start WebSocket server in main thread
    asyncio.run(start_websocket_server())
