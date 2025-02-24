import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)  # REQ = Request socket
socket.connect("tcp://localhost:5555")  # Connect to the microservice

# Example test data
ratings_data = {"ratings": [8, 9, 7, 10, 6, 8, 7, 9]}
socket.send_json(ratings_data)  # Send request

response = socket.recv_json()  # Receive response
print("Average Rating:", response.get("average", "Error"))

#Example invalid test data
# ratings_data = {"ratings": ["bad_data", 5, 7]}  # Invalid input
# socket.send_json(ratings_data)  # Send request
# response = socket.recv_json()  # Receive response
# print(response)
