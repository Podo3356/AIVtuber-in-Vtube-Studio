from flask import Flask, render_template, request, jsonify
from vtube_studio import VtubeStudioController
from ai_engine import AIVTuberEngine
from character_config import CharacterConfig

app = Flask(__name__)

# AI 엔진 및 Vtube Studio 컨트롤러 초기화
ai_engine = AIVTuberEngine()
vtube_controller = VtubeStudioController()

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    character_prompt = request.json.get('character_prompt')
    character_config = CharacterConfig(character_prompt)
    character_settings = character_config.generate_character_settings()

    if user_input:
        ai_response = ai_engine.generate_response(user_input)
    else:
        ai_response = ai_engine.generate_response()

    return jsonify({"response": ai_response})

@app.route('/control_avatar', methods=['POST'])
def control_avatar():
    action = request.json.get('action')
    vtube_controller.send_action(action)
    return jsonify({"status": f"Action '{action}' has been sent to Vtube Studio"})

if __name__ == '__main__':
    app.run(debug=True)
