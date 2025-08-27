//ESP32.ino
#include "DHT.h"
#include <WiFi.h>
#include <WebSocketsClient.h>

#define DHTPIN 14
#define ledPin 4
#define DHTTYPE DHT11

const char *NodeID = "node1"; // ID of the sensor node

// Wi-Fi credentials
const char* ssid = "SSID";         // Replace with your Wi-Fi SSID
const char* password = "PASSWORD"; // Replace with your Wi-Fi password

// WebSocket server info
const char* websocket_server = "<Flask Server IP>"; // IP of Flask + WebSocket PC
const int websocket_port = 8765;

WebSocketsClient webSocket;
DHT dht(DHTPIN, DHTTYPE);

// WebSocket event handler
void webSocketEvent(WStype_t type, uint8_t *payload, size_t length) {
    String command = String((char *) payload);
    switch(type) {
        case WStype_CONNECTED:
            Serial.println("Connected to WebSocket server");
            break;
        case WStype_DISCONNECTED:
            Serial.println("Disconnected from WebSocket server");
            break;
        case WStype_TEXT:
            Serial.print("Command received: ");
            Serial.println(command);
            // Control LED based on received command
            if (command == "ON") {
                digitalWrite(ledPin, HIGH);
            } else if (command == "OFF") {
                digitalWrite(ledPin, LOW);
            }
            break;
        case WStype_ERROR:
            Serial.println("Error in WebSocket connection");
            break;
        default:
            break;
    }
}

void setup() {
    Serial.begin(115200);
    dht.begin();
    pinMode(ledPin, OUTPUT);

    // Connect to Wi-Fi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.print("Connecting to Wi-Fi...");
    }
    Serial.print("Connected to Wi-Fi. IP: ");
    Serial.println(WiFi.localIP());

    // Initialize WebSocket
    webSocket.begin(websocket_server, websocket_port, "/");
    webSocket.onEvent(webSocketEvent);
}

void loop() {
    webSocket.loop();

    // Send periodic sensor data every 5 seconds
    static unsigned long lastTime = 0;
    unsigned long now = millis();
    if (now - lastTime > 5000) {
        lastTime = now;

        float h = dht.readHumidity();
        float t = dht.readTemperature();
        float f = dht.readTemperature(true);

        // Check if reading failed
        if (isnan(h) || isnan(t) || isnan(f)) {
            Serial.println(F("Failed to read from DHT sensor!"));
            return;
        }

        // Construct data string
        String data = String(NodeID) + "," + String(h) + "," + String(t) + "," + String(f);
        webSocket.sendTXT(data);

        // Print data to serial monitor
        Serial.print("Humidity: ");
        Serial.print(h);
        Serial.print("%  Temperature: ");
        Serial.print(t);
        Serial.print("°C, ");
        Serial.print(f);
        Serial.println("°F");
    }
}
