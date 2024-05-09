import time
import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP) 
socket.bind("tcp://*:58125") 

cat_tips = ["Provide fresh water at all time for your cat. A flowing water fountain can entice your cat to drink more water.",
                "While cats rarely need baths, frequent brushing can help reduce the amount of shedding.",
                "Make sure your cat is microchipped or has an ID tag in case they become lost."
                "Keep at least one litter box per floor in a multi-level home or one litter box per cat you own.",
                "Do not use ammonia or citrus oils to clean a litter box.",
                "Provide your cat with a stable scratching post that is at least three feet tall.",
                "Play and bond with your cat everyday. Cat toys are a good way to keep your pet's body and mind active.",
                "Keep the litter box clean by scooping once a day and making a complete change at least once a week. Cats like to use clean restrooms!",
                "Cardboard boxes can be reused as cat beds.",
                "Automatic feeders are a good purchase to make to maintain a scheduled feeding routine and prevent overfeeding."
                ]
dog_tips = ["Limit human food for dogs. Feed your dog high quality dog food according to their life stage and weight.",
            "Teaching your dog new tricks and playing games like hide-and-seek can help sharpen your their brain.",
            "Bathe your dog no more than once a month.",
            "Find an appropriate flea treatment for your dog with your vet especially during the warmer months. Flea combs can also be very helpful in locating fleas.",
            "Brushing your dog's teeth at least 3 times a week can help prevent dental diseases.",
            "Walking your dog everyday helps eliminate boredom and provide mental stimulation.",
            "Consider microchipping your dog which can help shelters and veterinary offices find you in case your dog is lost",
            "If your dog gobbles up their food too fast, use a puzzle feeder to slow down their eating pace.",
            "Provide a comfortable spot in your house for your dog with its bed, blanket, and toys.",
            "Make sure to clean your dog's bedding, toy, and dishes regularly to remove bacteria and allergens."
            ]
tip = ""

while True:
    #  awaiting request from the client
    message = socket.recv_string()
    print(f"Received this request from the client: {message}")
    
    if message == "cat":
        # gets a random tip from the cat tips list 
        index = random.randint(0, len(cat_tips)-1)
        tip = cat_tips[index]
    if message == "dog":
        # gets a random tip from the dog tips list 
        index = random.randint(0, len(dog_tips)-1)
        tip = dog_tips[index]

    print(f"Sending the following tip to the client: {tip} ")
    time.sleep(1)

    # send a reply back to the client
    socket.send_string(tip)