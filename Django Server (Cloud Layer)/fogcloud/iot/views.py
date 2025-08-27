from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json, requests
from .models import SensorData

# Flask server URL
FLASK_URL = "http://<Flask Server IP>:5000/control"

# --------------------------
# API to receive sensor data from Flask
# --------------------------
@csrf_exempt
def fan_data(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        node_id = data.get("NodeId")
        humidity = float(data.get("h_level"))
        temperature = float(data.get("c_level"))
        fan_level = float(data.get("f_level"))

        # Save in database
        SensorData.objects.create(
            node_id=node_id,
            humidity=humidity,
            temperature=temperature,
            fan_level=fan_level,
        )

        # Threshold logic – auto mode
        if humidity > 80 or temperature > 40:
            try:
                requests.put(FLASK_URL, json={"command": "AUTO"})
            except Exception as e:
                print("Error sending AUTO to Flask:", e)
            return JsonResponse({"status": "auto triggered"}, status=200)

        return JsonResponse({"status": "data stored"}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)

# --------------------------
# HTML Control Page – ON/OFF/AUTO buttons
# --------------------------
@csrf_exempt
def control_page(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        command = data.get("command")

        # Forward command to Flask
        try:
            r = requests.put(FLASK_URL, json={"command": command})
            return JsonResponse({"message": f"Sent {command} to Flask"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    # GET request → render HTML page
    return render(request, "iot/control.html")
