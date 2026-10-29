from flask import Flask, request, jsonify

app = Flask(__name__)


# Function to calculate the sum of numbers
def calculate_sum(numbers):
    return sum(numbers)


# GET endpoint
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name')

    if name:
        return jsonify({
            "message": f"Hello, {name}!"
        })

    return jsonify({
        "message": "Hello, World!"
    })


# POST endpoint
@app.route('/sum', methods=['POST'])
def add_numbers():
    data = request.get_json()

    # Check if JSON was sent
    if not data:
        return jsonify({
            "error": "JSON payload is required"
        }), 400

    # Check for numbers field
    if "numbers" not in data:
        return jsonify({
            "error": "Missing 'numbers' field"
        }), 400

    numbers = data["numbers"]

    # Ensure numbers is a list
    if not isinstance(numbers, list):
        return jsonify({
            "error": "'numbers' must be a list"
        }), 400

    # Ensure all values are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        return jsonify({
            "error": "All values must be numeric"
        }), 400

    total = calculate_sum(numbers)

    return jsonify({
        "sum": total
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)