# Queues

## What is a queue data structure?

A queue is a data structure that works under the premise of **FIFO** (First-in First-out). The best way to understand it is by think about a waiting line, where basically the first one in the line, in the **front**, will be attended first. Then one by one in that order, so if a new person incorporates in the line he will be located in the **back** of the line until those in front of him are attended and it's his turn.

![my queue illustration](/queue%20data%20structure1.png)

## The purpose of a queue

This data structure and it's behavior is relevant for many situations where a **FIFO** approach is necessary to handling processes, tasks, etc. The concept of a queue provides an specific order, therefore, it's desired for multiple circumstances, like in the example above of a waiting line or whenever you want to tackle first what arrives first.

## Working with queues in Python

Now let's dive in to see how queues are used in Python. We are going to use a Python list to understand hos this data structure works. There're other Python libraries that provide queues, but we are going to model it with a list.

Following the illustration above let's create a waiting line and add new people on the line. This process of adding new items in a list is called **enqueue**. It will normally have a O(1) performance.

```
# Create the list for people in the line
people_in_line = []

def enqueue(person):
    # Add to the back of the list
    people_in_line.append(person)

# Test:
print("Add 6 new people in line:")
for person in range(0, 6):
    enqueue(person)
    print(people_in_line)
```
**Output:**
```
Add 6 new people in line:
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
```
Now let's continue with the process of **dequeue**, which means to remove the person in the front. Also, there's an example on how to handle an *error* if dequeue is called and there's no more people in the line. Dequeue will normally have a O(n) performance.

```
def dequeue():
    # If the list is empty and there's
    # a dequeue
    if len(people_in_line) == 0:
        return print("No more people in line")
    
    # Remove the first on the front of
    # the list
    else:
        people_in_line.pop(0)

# Test:
print("Remove the 6 people as they are attended and a non-existent extra to trigger the error handling:")
for person in range(0, 7):
    print(people_in_line)
    dequeue()
```
**Output:**
```
Remove the 6 people as they are attended and a non existent extra to trigger the error handling:
[0, 1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[3, 4, 5]
[4, 5]
[5]
[]
No more people in line
```


## Example: Bogota's Transmilenio bus transit system daily losses report

In Bogotá there is a bus transportation system called Transmilenio, this system allows many of the inhabitants of Bogotá, the capital of Colombia, to travel throughout the city.
Users pay to charge their tickets using an electronic card that registers and allows them to enter the system through the turnstiles. however, there's a huge problem, lots of people enter the system without paying for their tickets (see image below) which generates losses for the enterprise. With the power of a queue data structure, we can create a program that allows us to know how many losses Transmilenio has each day.

![Colados en Transmilenio](https://www.infobae.com/new-resizer/kSINzcMynd8MEQyu9w-9aT2IOTk=/768x432/filters:format(webp):quality(85)/cloudfront-us-east-1.images.arcpublishing.com/infobae/7YRSYANJX5F6XPXHHQ6NCWNIBY.jpg)

Image published in: [Infobae News](https://www.infobae.com/america/colombia/2022/03/06/colados-y-trafico-de-pasajes-los-problemas-que-buscara-enfrentar-transmilenio/)

We know that the turnstiles count the number of people entering the bus system and also the number of people leaving the bus system, usually, when the people that aren't paying to enter the system leave, they do it like everyone else, by going through the exit turnstiles. With this, we can create a program that helps us know how many people are not paying and we can estimate money losses at the end of each day.

Again, there's a Python library with a class called deque that you can use to get this data structure, but we are going to use a Python list instead and create functions for our queue.

**We need to create:**
* A function to enqueue users paying to enter through the turnstile
* A function to dequeue users leaving through the exit turnstile *(This function also needs to handle the error of dequeue when the list is empty to keep track of the non-payers)*
* A function to count how many users are currently in the bus system
* A function to estimate losses based on a ticket price and the total number of non-payers exiting through the exit turnstile

**Function** | **Inputs**      | **Outputs**
-------------|-----------------|--------------
enqueue_user | user_no         | Append user to the bus_users list
dequeue_user | none            | Pop the index 0 of the bus_users list. Also, if the list is empty append a 1 to the no_pay_users list to keep track of non-payers
size         | list            | Length of the list (It has a O(1) performance.)
estimated_losses| ticket-price | A message displaying computed losses

Here is the implementation for these 4 functions:

```
# List to capture current bus users in the
# system and non-payers
bus_users = []
no_pay_users = []

def enqueue_user(user_no):
    """
    Adds a new user to the back of the queue.
    Parameter:
        user_no: a number to represent an entry
        in the turnstile.
    """
    # Add to the back of the list
    bus_users.append(user_no)

def dequeue_user():
    """
    Removes the user in the back of the queue.
    """
    # If the list is empty and there's
    # a dequeue add 1 to the no payers
    if len(bus_users) == 0:
        no_pay_users.append(1)
    
    # Remove the first on the front of
    # the list
    else:
        bus_users.pop(0)

def size(list):
    """
    Computes the size of the list.
    parameter:
        list: python list
    """
    # Get the length of the non-payers
    # list
    length = len(list)
    return length

def estimated_losses(ticket_price):
    """
    Computes the estimated losses in COP
    (Colombian Pesos).
    parameter:
        ticket_price: float number
    """
    size_no_payers = size(no_pay_users)
    losses = '{:,}'.format(size_no_payers * ticket_price)
    message = print(f"Today there are aproximately ${losses} COP in losses")
    return message
```
To test these functions in a simulated day of activities at Transmilenio we have the following testing code calling the 4 functions:

```
# TESTING:

# 50,000 users enter the system through the turnstiles
print("1. 50000 users enter the transmilenio during the day")
for user in range(0, 50000):
    enqueue_user(user)

# Verify the number of current users in the system
print()
print("Number of people currently inside the bus system:")
print(size(bus_users)) # 50000

# 50,100 users exit the system through
# the turnstiles
print()
print("2. 50100 users exit the system through the turnstiles")
for user in range(0, 50100):
    dequeue_user()

# Verify the number of current users in the system
print()
print("Number of people currently inside the bus system:")
print(size(bus_users)) # 0

# Check the number of no payers that exited through
# the turnstiles
print()
print("3. Number of people that exit but didn't pay to enter:")
print(size(no_pay_users)) # 100

# Compute the estimated losses at a ticket price of
# 3000 COP
print()
print("4. Estimated losses at a ticket price of 3000 COP:")
estimated_losses(3000) # $300,000 COP
```
**Output:**
```
1. 50000 users enter the transmilenio during the day

Number of people currently inside the bus system:
50000

2. 50100 users exit the system through the turnstiles

Number of people currently inside the bus system:
0

3. Number of people that exit but didn't pay to enter:
100

4. Estimated losses at a ticket price of 3000 COP:
Today there are approximately $300,000 COP in losses
```

## Problem to Solve: Wait time while in the queue for a roller coaster at an Amusement Park

There's a popular roller coaster in the local amusement park. You decided to go there. To join the line you have to provide your phone number at the beginning of the line. The amusement park's AI provides text message updates about the length of the line and an estimated of how many minutes you will have to wait in order to be your turn at the roller coaster.

You will have to create the code for the following 4 functions in order for it to work properly:

**Function** | **Inputs**      | **Outputs**
-------------|-----------------|--------------
enqueue_user | user_no         | Add a new user in the line
dequeue_user | none            | Remove users that leave the line
size         | list            | Length of the list aka. quantity of people in the line
join_rollercoaster| none       | Removes 40 users which is the max number of users that can take a ride in the roller coaster

The output of the program if it's working well should be the following:

**Output:**
```
Roller coaster line
There are 290 people waiting on the line.

You joined the line!

You have to wait 14 minutes until it's
your turn to enter the roller coaster.

2 rides have already passed, which means there
are 211 people waiting, including you.
You have to wait 10 minutes for your turn.

5 rides have already passed, there are 11
people waiting in front of you. Therefore,
It's your turn!

You should be the last person in the line:
[280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 'You']

*Testing when there's a dequeue but the line is empty:
No people in the line
```
Below is the [Unsolved Program](/wait_time_unsolved.py) that is missing the code for the 4 functions mentioned above. At the end there are some lines of code to test if your functions are working properly.

```
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
```

Here's the [Solution](/wait_time_solution.py) for this program using the queue data structure.

[Back to Welcome Page](/README.md)