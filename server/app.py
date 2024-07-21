from flask import Flask, render_template, request, jsonify
import hmac
import hashlib
from urllib.parse import unquote

bot_token = ""


app = Flask(__name__, template_folder="template")

def validate_init_data(init_data: str, bot_token: str):
    params = {k: unquote(v) for k, v in (item.split('=') for item in init_data.split('&'))}
    
    received_hash = params.pop('hash', None)
    
    data_check_string = '\n'.join([f'{k}={params[k]}' for k in sorted(params.keys())])
    
    secret_key = hmac.new("WebAppData".encode(), bot_token.encode(), hashlib.sha256).digest()
    
    hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    
    return hmac.compare_digest(hmac_hash, received_hash)


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/data", methods=["POST"])
def data():
    data = request.get_json()
    if data and 'value' in data:
        init_data = data['value']
        is_valid = validate_init_data(init_data, bot_token)
        print(f"Received init_data: {init_data}")
        print(f"Validation result: {is_valid}")
        return jsonify(isvalid=is_valid)
    return jsonify(isvalid=False)

if __name__ == "__main__":
    app.run(debug=True)

#emboy