from flask import Flask, render_template_string, request, jsonify
import webbrowser

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JSON Validator - github.com/or1z</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        body {
            min-height: 100vh;
            background: rgb(0, 0, 0);
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            position: relative;
            overflow: hidden;
        }
        .scene {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            perspective: 1000px;
        }
        .grid {
            position: absolute;
            width: 200%;
            height: 200%;
            top: -50%;
            left: -50%;
            background-image: linear-gradient(90deg, rgba(223, 223, 223, 0.1) 1px, transparent 1px), 
                              linear-gradient(rgba(223, 223, 223, 0.1) 1px, transparent 1px);
            background-size: 40px 40px;
            transform: rotateX(60deg);
            animation: grid 20s linear infinite;
        }
        @keyframes grid {
            0% { transform: rotateX(60deg) translateY(0); }
            100% { transform: rotateX(60deg) translateY(40px); }
        }
        .container {
            max-width: 600px;
            width: 90%;
            padding: 20px;
            position: relative;
            z-index: 2;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
        }
        textarea {
            width: 100%;
            height: 300px;
            margin-bottom: 15px;
            border: none;
            border-radius: 8px;
            padding: 15px;
            font-size: 16px;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            resize: none;
            outline: none;
        }
        button {
            margin: 10px;
            padding: 12px 25px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.2s;
        }
        button:active {
            transform: scale(0.95);
        }
        .validate-btn {
            background-color: #28a745;
            color: white;
        }
        .validate-btn:hover {
            background-color: #218838;
        }
        .clear-btn {
            background-color: #dc3545;
            color: white;
        }
        .clear-btn:hover {
            background-color: #c82333;
        }
        .message {
            margin-top: 15px;
            font-size: 18px;
            color: white;
        }
    </style>
</head>
<body>
    <div class="scene">
        <div class="grid"></div>
    </div>
    <div class="container">
        <textarea id="jsonInput" placeholder="Enter your JSON here..."></textarea>
        <br>
        <button class="validate-btn" onclick="validateJSON()">Validate</button>
        <button class="clear-btn" onclick="clearBox()">Clear Box</button>
        <div id="message" class="message"></div>
    </div>
    <script>
        function validateJSON() {
            const jsonInput = document.getElementById('jsonInput').value.trim();
            const messageDiv = document.getElementById('message');
            if (!jsonInput) {
                messageDiv.textContent = "Enter JSON in the box before trying to validate.";
                messageDiv.style.color = "orange";
                return;
            }
            fetch('/validate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ json: jsonInput })
            })
            .then(response => response.json())
            .then(data => {
                messageDiv.textContent = data.message;
                messageDiv.style.color = data.valid ? 'green' : 'red';
            });
        }

        function clearBox() {
            document.getElementById('jsonInput').value = '';
            const messageDiv = document.getElementById('message');
            messageDiv.textContent = '';
        }
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(html_template)


@app.route("/validate", methods=["POST"])
def validate():
    try:
        data = request.get_json()
        json_string = data.get("json", "")
        if not json_string.strip():
            return jsonify(
                {
                    "valid": False,
                    "message": "Enter JSON in the box before trying to validate.",
                }
            )
        import json

        json.loads(json_string)
        return jsonify({"valid": True, "message": "JSON is valid!"})
    except (json.JSONDecodeError, TypeError):
        return jsonify({"valid": False, "message": "JSON is not valid!"})


if __name__ == "__main__":
    port = 5000
    webbrowser.open(f"http://127.0.0.1:{port}")
    app.run(debug=False, port=port)
