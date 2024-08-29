from flask import Flask, jsonify, request
from datetime import datetime, timedelta

# Initialize the Flask application
app = Flask(__name__)

# Simulate a queue with customer details
queue = []

# Define your routes here
@app.route('/join_queue', methods=['POST'])
def join_queue():
    customer = request.json
    customer['join_time'] = datetime.now()
    queue.append(customer)
    return jsonify({"message": "You have joined the queue", "position": len(queue)})

@app.route('/queue_status', methods=['GET'])
def queue_status():
    if not queue:
        return jsonify({"message": "Queue is empty"})
    
    current_time = datetime.now()
    status = []
    for i, customer in enumerate(queue):
        wait_time = (current_time - customer['join_time']).seconds // 60
        status.append({"position": i+1, "customer_name": customer['name'], "wait_time": wait_time})
    
    return jsonify(status)

@app.route('/notify_customer', methods=['GET'])
def notify_customer():
    if len(queue) > 0:
        customer = queue.pop(0)  # Serve the next customer
        return jsonify({"message": f"Notifying {customer['name']} to approach the counter"})
    return jsonify({"message": "No customers in queue"})

@app.route('/dashboard', methods=['GET'])
def dashboard():
    current_time = datetime.now()
    status = []
    for i, customer in enumerate(queue):
        wait_time = (current_time - customer['join_time']).seconds // 60
        status.append({"position": i+1, "customer_name": customer['name'], "wait_time": wait_time})
    
    return jsonify({"queue_length": len(queue), "status": status})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
