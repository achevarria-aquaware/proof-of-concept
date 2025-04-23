from flask import Flask, jsonify
# from os import path

app = Flask(__name__)

# def text_to_dict(text: str) -> dict:
#   """Convert key=value pairs in a string to a dictionary"""
#   result = {}
#   for line in text.split('\n'):
#       # Skip empty lines
#       if not line.strip():
#           continue
        # Split into key/value pair
#       key, value = line.split('=', 1)  # Split on first '=' only
#       result[key.strip()] = value.strip()
#   return result

@app.route('/data', methods=['GET'])
def get_data():
    sample_data = {
        "message": "Welcome to the Flask API!",
        "status": "success",
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"}
        ]
    }
    return jsonify(sample_data)

#@app.route('/secrets', methods=['GET'])
#def get_secrets():
#   result = {}

#   with open(path.join('/var', 'secrets', 'database-secrets.txt')) as f:
#       result = text_to_dict(f.read())
#       print(result)
#   return jsonify(result)

if __name__ == '__main__':
#   print("")

#   resultado = {}

#   with open(path.join('/var', 'secrets', 'database-secrets.txt')) as f:
#       resultado = text_to_dict(f.read())
#       print(resultado)

#   print("")
#   print("")
    app.run(host='0.0.0.0', port=5000)
