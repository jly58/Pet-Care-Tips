import zmq

context = zmq.Context()

def request_tip(pet_type):
    """This function will send a request to the microservice and returns the tip"""
    socket = context.socket(zmq.REQ) # REQUEST
    socket.connect("tcp://localhost:58125") # Local host address
    socket.send_string(pet_type)     # Request is the pet type
    message = socket.recv()
    print(f"Your {pet_type} tip: {message}")

while True:
    """Asks the user for input of either dog or cat pet type."""
    user_input = input("""
    Please enter one of the following pet types to get a pet care tip:
                    Dog
                    Cat\n""").lower().strip()
    if user_input != "dog" and user_input != "cat": # Error handling
        print("Please enter a valid pet type")
    else: 
        request_tip(user_input)
        break