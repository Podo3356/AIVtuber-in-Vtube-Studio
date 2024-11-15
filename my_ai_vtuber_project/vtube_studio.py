import websocket
import json

class VtubeStudioController:
    def __init__(self, host='localhost', port=8001):
        self.ws_url = f"ws://{host}:{port}"
        self.ws = websocket.WebSocket()
        self.connect()

    def connect(self):
        self.ws.connect(self.ws_url)
        print("Vtube Studio에 연결되었습니다.")

    def send_action(self, action):
        data = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "action",
            "messageType": "HotkeyTrigger",
            "data": {"hotkeyID": action}
        }
        self.ws.send(json.dumps(data))
    
    def set_emotion(self, emotion):
        print(f"Emotion set to: {emotion}")
