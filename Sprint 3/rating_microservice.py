import zmq


def calculate_average(ratings):
    if not ratings or not all(isinstance(r, (int, float)) for r in ratings):
        return {"error": "Invalid input: ratings must be a list of numbers"}
    
    avg_rating = sum(ratings) / len(ratings)
    return {"average": int(round(avg_rating))}  # Return as an integer

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # REP = Reply socket
    socket.bind("tcp://*:5555")  # Listening on port 5555
    
    print("Rating Microservice is running...")

    while True:
        message = socket.recv_json()
        response = calculate_average(message.get("ratings", []))
        socket.send_json(response)

if __name__ == "__main__":
    main()
