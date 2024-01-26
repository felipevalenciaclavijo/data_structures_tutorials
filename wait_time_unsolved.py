import math

# List to keep track of the number of people in line:
people_in_line = []

def enqueue_user(user_no):
    """
    Adds a new user to the back of the queue.
    Parameter:
        user_no: a number to represent an entry
        in the turnstile.
    """
    # Add to the back of the list

    # YOUR CODE GOES HERE:
    pass

def dequeue_user():
    """
    Removes the user in the back of the queue.
    """
    # If the list is empty and there's
    # a dequeue print a message saying:
    # "No people in the line"
    # Else dequeue the user.

    # YOUR CODE GOES HERE:
    pass

def size(list):
    """
    Computes the size of the list.
    parameter:
        list: python list
    return length
    """
    # Get the length of the list

    # YOUR CODE GOES HERE:

    # Remove the return 0 once
    # you implemented your code
    return 0

def join_rollercoaster():
    """
    People leave the line because they
    enter the roller coaster. The capacity
    of the roller coaster is 40 people a ride
    """
    # 40 people enter the roller coaster
    # and leave the line

    # YOUR CODE GOES HERE:
    # HINT: use the dequeue_user function
    pass

def wait_time(list):
    """
    Computes the estimated time the user has to
    wait until it's his turn to join the ride
    parameter:
        list: python list
    """
    number_people = size(list)
    capacity = 40
    time_per_ride = 2 # 2 minutes

    # If the number of people is equal or less
    # than 40 it means it's your turn
    if number_people == 0:
        return "???"
    elif number_people <= 40:
        return f"It's your turn!"
    # Compute the wait time
    else:
        wait = math.floor((number_people / capacity)) * time_per_ride
        return wait

# -------TESTING---------

print("Roller coaster line")
print("There are 290 people waiting on the line.")
for person in range(0, 290):
    enqueue_user(person)
print()
print("You joined the line!")
enqueue_user("You")

time = wait_time(people_in_line)

print()
print(f"You have to wait {time} minutes until it's")
print("your turn to enter the roller coaster.")
print()
# 2 rides have passed
join_rollercoaster()
join_rollercoaster()
current_size = size(people_in_line)
time = wait_time(people_in_line)
print(f"2 rides have already passed, which means there")
print(f"are {current_size} people waiting, including you.")
print(f"You have to wait {time} minutes for your turn.")

# 5 rides have passed
join_rollercoaster()
join_rollercoaster()
join_rollercoaster()
join_rollercoaster()
join_rollercoaster()
current_size = size(people_in_line)
print()
print(f"5 rides have already passed, there are {current_size}")
print(f"people waiting in front of you. Therefore,")
print(wait_time(people_in_line)) # It's your turn!
print()
print("You should be the last person in the line:")
print(people_in_line)
print()
print("*Testing when there's a dequeue but the line is empty:")
for person in range(0, 12):
    dequeue_user() # No people in the line