# Trees

## What is a Tree?

A tree follows the same principle as the linked lists, meaning that nodes are connected with pointers. There are various types of trees, but we will focus on **binary search trees (BST)** because many functions with this data structure can achieve a **log(n)** performance. A BST has a set of rules established that we need to understand. First, of all let's look at the structure of a tree. Like any tree you can find in real life, there's a root, one root can have branches or subtrees, and branches or subtrees have leaves. In a binary tree there are some basic assumptions:
1. There's only one root, the origin of the tree which can have two child nodes.
2. Each node after the root can be considered a parent if it has 1 or 2 child nodes and also a child if it has a parent node connected above.
3. A node that has no child is called a leave because it's the end of the tree.
4. Each parent node with a node to the left and to the right can be considered a subtree because it has by itself all that's required to be a small tree within the big tree.

![my tree illustration 1](/my_trees_diagram.png)

## The purpose of a Tree

The fact that a parent node can only have two child nodes provides order and purpose to the binary search tree data structure. In China, the government implemented for many years a 1 child policy, meaning that a family could only have 1 child. According to them, the purpose was to control the birth rate and population growth. Whether if that was the best strategy or not, we don't know, but we can recognize that it provided order to their population structure. In a binary tree, the rule is that a parent can only have two child nodes, this *allows us to perform a unique placement strategy to store the data efficiently in a tree.*

The strategy is simple, if the new number is smaller than the parent's number, the new number should be positioned and connected as the left child node, and the bigger number than the parent as the right node child. Of course, if the node that is being compared has already two child nodes connected, it won't replace it in the selected spot, rather it will continue repeating the comparison process with the following node until a fresh spot is found for it to become the newest child node and the latest leaf of the tree.

Using the previous illustration, let's imagine we want to add number 25 to the tree.  First, we compare it with the root number (18), we know that 25 > 18, so we move to the right, and because there's already a node there we can't put it there, instead we proceed to compare it with the node number, in this case (23), we know 25 > 23, therefore, we move to the right again looking for a spot, but because is already taken by (28) we compare it instead. 25 < 28, so in this case we move to the left because it's less than 28 and because (28) is a leaf it means that to the left there's space, so our number it's placed in that node, therefore (28) is now a parent and not a leaf, and (25) becomes a new leaf.

![my set illustration](/my_trees_diagram2.png)

You get the idea now, simply put, you check if there's space, if it's empty place it there. Always move based on whether it was less (left) or greater (right ) than the node number and keep repeating the process.

## Working with binary search trees in Python

In Python we will create a BST using **recursion** which is basically calling a function within a function as many times needed until it breaks based on a *base case* previously established. There are models to make sure the BST is balanced, which means it always keeps a similar **height** (*height refers to the number of nodes between the root and the leaves*) in both sides. But we will focus on using a BST and won't care about height perfection to learn the data structure.

To create a BST in Python we will create a class for the BST and a class inside the BST class called Node. The **init** will create an empty root, and each node will have their given spot, a left link, and a right links: 

```
class BST:

    class Node:

        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None
```
To insert data in the BST we create two functions:

```
    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Notice that we start at the root

    def _insert(self, data, node):

        # If it's less than the node number:
        if data < node.data:
            # Go to the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        # If it's greater than the node number:
        elif data > node.data:
            # Go to the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
```
**NOTE:** It's important to notice that if the number is already in the tree it won't do anything, this way we avoid duplicates.

To check if data is contained in the tree:

```
    def __contains__(self, data):

        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):

        if data < node.data:
            # Go to the left side.
            if node.left is None:
                # It's not contained in the BST
                return False
            else:
                # Need to keep looking.  Call _contains
                # recursively on the left sub-tree.
                return self._contains(data, node.left)
        elif data > node.data:
            # Go to the right side.
            if node.right is None:
                # It's not contained in the BST
                return False
            else:
                # Need to keep looking.  Call _contains
                # recursively on the right sub-tree.
                return self._contains(data, node.right)
        else:
            # It's contained in the BST
            return True
```

To move through data in order, from smallest to largest, we use **transverse_forward** by calling the **__iter__** function:

```
    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
```
To move through data in the *opposite direction*, from largest to smallest, we should simply use the same **transverse_forward** code and the **__iter__** function, but instead of going from node.left to node.right, we flip them. And of course, we change the names to a more proper naming like **transverse_backward** and **__reversed__**.

Let's see how this work with the following test based on the illustrations above:

```
# TESTING:

# Create a new Tree:
tree = BST()

# Insert numbers:
tree.insert(18)
tree.insert(11)
tree.insert(23)
tree.insert(9)
tree.insert(13)
tree.insert(7)
tree.insert(10)
tree.insert(28)
tree.insert(25)
tree.insert(25) # DUPLICATE
tree.insert(25) # DUPLICATE

print("Transverse forward:")
for x in iter(tree):
    print(x)
print()
print("Transverse backward:")
for x in reversed(tree):
    print(x)
print()
print("Verify if a number is contained in the tree:")
print(10 in tree) # True
print(7 in tree) # True
print(23 in tree) # True
print(35 in tree) # False
print(5 in tree) # False
```

**Output:**
```
Transverse forward:
7
9
10
11
13
18
23
25
28

Transverse backward:
28
25
23
18
13
11
10
9
7

Verify if a number is contained in the tree:
True
True
True
False
False
```
Based on the results from this test we can be confident that the BST is working properly because when it transverses forward or backward the results are sorted accordingly. Additionally, the duplicates were handled without problem, and when checking if a number was in the tree we got the expected answers.

## Example: Users visiting our website

![Usuarios](https://images.pexels.com/photos/8088451/pexels-photo-8088451.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)

Image from: [Pexels](https://www.pexels.com/license/)

To login in our website users have to enter their IDs. When users created their accounts they selected their gender. The IDs and the respective genders are stored in a dictionary.

Using a BST that is created every new day our website keeps track of users visiting the website with which we can also compute the total number of users visiting by gender. 

**We need to create a program that can:**
* Insert user IDs in the daily users BST
* Tranverse the data in the BST to report visits
* Track IDs visits with gender totals

**Function** | **Inputs**      | **Outputs**
-------------|-----------------|--------------
insert | data         | Call the _insert function to insert a new ID for the day to the daily_users BST
_insert | data, node           | Compares the ID with the node and recursively keep doing it to find a spot on the right or left node depending on the ID number
iter         | none            | Calls the _transverse_forward to sort the IDs
_transverse_forward       | none            | Moves from the left nodes to the right ones to sort them

Here is the implementation for these 4 functions:

```
# Create a BST class with a Node class in it:
class BST:

    class Node:

        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Notice that we start at the root

    def _insert(self, data, node):

        # If it's less than the node number:
        if data < node.data:
            # Go to the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        # If it's greater than the node number:
        elif data > node.data:
            # Go to the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

# Database of users' genders:
users_gender = {
    # User_ID: Gender
    10: "female",
    9: "male",
    8: "male",
    7: "male",
    6: "female",
    5: "male",
    4: "male",
    3: "female",
    2: "male",
    1: "female"
    }

# Create a new BST for daily users in the website:
daily_users = BST()

# Users that visit the website during the day:
daily_users.insert(5)
daily_users.insert(8)
daily_users.insert(3)
daily_users.insert(1)
daily_users.insert(2)

# Print a sorted list of users with their respective gender:
print("Record of users in website today with gender info:")
print("--------------------------------------------------")
for x in daily_users:
    print(f"{x} is a {users_gender[x]}")

# Track totals by gender:
total_males = 0
total_females = 0

# Using BST daily_users count totals by gender:
for x in daily_users:
    gender = users_gender[x]
    if gender == "male":
        total_males += 1
    else:
        total_females += 1

print()
print(f"Today there were {total_males} males and {total_females} females on the website.")
```
**Output:**
```
Record of users in website today with gender info:
--------------------------------------------------
1 is a female
2 is a male
3 is a female
5 is a male
8 is a male

Today there were 3 males and 2 females on the website.
```

## Problem to Solve: Report of Colombian Citizens visiting a Public Library

![Colombian Library](https://bogota.gov.co/sites/default/files/2022-03/elecciones-2022.jpg)

Image from: [Alcaldía de Bogotá](https://bogota.gov.co/mi-ciudad/cultura-recreacion-y-deporte/horario-de-las-bibliotecas-publicas-de-bogota-en-la-jornada-electoral)

In Colombia, every citizen is given a unique ID called "Cedula". The National Civil Registry is the entity in charge of keeping citizens' data. They keep the age of each citizen in a database.

Public libraries ask citizens to provide their "Cedula" ID when they enter a public library facility. With this, they can keep a record of how many people are using the public libraries and other relevant data.

You have been requested to implement a program using BST to record daily library users. You also have access to the citizens' ages database (This is a dictionary provided in the problem).

You will have to complete the code for the following 3 functions for it to work properly:

**Function** | **Inputs**      | **Outputs**
-------------|-----------------|--------------
_insert | data, node           | Compares the ID with the node and recursively keep doing it to find a spot on the right or left node depending on the ID number
_contains        | data, none            | Checks if an ID is in the tree by comparing the ID with the node and recursively keep doing it to find it. HINT: Use the _insert function as a guide.
_traverse_backward       | node            | Moves from the right nodes to the left ones to sort them from largest to smallest

**NOTE: Read carefully the unsolved code and follow the instructions to make sure your program works well.**

If you followed the instructions correctly and applied BST in Python properly, your result should be as follow.

**Output:**
```
TEST 1: Record of citizens that visited the library today (from largest to smallest ID):
--------------------------------------------------
1846591742 entered the library and is 27 years old.
1789534645 entered the library and is 45 years old.
1739971801 entered the library and is 76 years old.
1708499062 entered the library and is 28 years old.
1635128800 entered the library and is 98 years old.
1530586023 entered the library and is 43 years old.
1499444343 entered the library and is 44 years old.
1497737130 entered the library and is 82 years old.
1470318933 entered the library and is 75 years old.
1420275031 entered the library and is 60 years old.
1375446835 entered the library and is 59 years old.
1331901175 entered the library and is 92 years old.
1216696512 entered the library and is 34 years old.
1170741186 entered the library and is 59 years old.
1152897392 entered the library and is 62 years old.
1097602870 entered the library and is 78 years old.

TEST 2: Today's Stats:
--------------
The youngest person that visited today was 27 years old.
The oldest person that visited today was 98 years old.
The average age for today was 60.125 years old.

TEST 3: Checking visits by certain individuals:
---------------------------------------
1170741186 visited the library today.
1470318933 visited the library today.
1327939204 didn't visit the library today.
```
Below is the [Unsolved Program](/library_report_unsolved.py) that is missing the code for the 3 functions mentioned above. At the end are the lines of code to test if your functions are working properly (make sure to compare it with the output given above).

```
# Create a BST class with a Node class in it:
class BST:

    class Node:

        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Notice that we start at the root

    def _insert(self, data, node):

        pass
        # YOUR CODE GOES HERE
        # Hint: Use the "Users visiting our website" example provided
        # in the trees explanation to complete this function

    def __contains__(self, data):

        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):

        pass
        # YOUR CODE GOES HERE
        # HINT: To accomplish this function use _insert function as
        # a guide, but instead of inserting and ID in an empty node
        # return TRUE or FALSE.

    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)


    def __reversed__(self):

        yield from self._traverse_backward(self.root)  # Start at the root
        
    def _traverse_backward(self, node):

        pass
        # IMPORTANT NOTE: To make this work you have to change the TEST 1 code.
        # instructions on how to change the code once you finished writing this
        # function can be found below on TEST 1.  

# Database of Colombian Citizens:
col_citizens = {
    # Unique Colombian ID: Age
    1781538447: 18,
    1584474331: 78,
    1599428801: 50,
    1231252029: 43,
    1305917988: 54,
    1216572601: 49,
    1388308518: 48,
    1881484406: 31,
    1819174402: 71,
    1189089461: 58,
    1490081850: 86,
    1971012416: 35,
    1041627731: 38,
    1954384239: 46,
    1108670997: 98,
    1372176048: 39,
    1037905645: 31,
    1956884640: 60,
    1581459929: 36,
    1138723812: 18,
    1441610424: 18,
    1057778277: 83,
    1370193257: 97,
    1938821046: 81,
    1609735155: 24,
    1742092223: 94,
    1115184708: 47,
    1208327210: 66,
    1294506756: 34,
    1267370377: 31,
    1048031958: 21,
    1723103594: 85,
    1030683693: 35,
    1500073044: 88,
    1184010692: 43,
    1016651133: 27,
    1327939204: 93,
    1303986969: 59,
    1622547477: 62,
    1828167644: 26,
    1930811188: 65,
    1994348582: 75,
    1972648090: 28,
    1556152475: 70,
    1862802242: 39,
    1552046222: 83,
    1389883599: 19,
    1513976094: 18,
    1706564785: 49,
    1004182569: 34,
    1962513812: 75,
    1636370608: 46,
    1588707290: 81,
    1620441506: 63,
    1216553928: 39,
    1169586650: 19,
    1635609901: 81,
    1349117965: 61,
    1323066948: 35,
    1793001327: 48,
    1245738760: 71,
    1222333775: 92,
    1185690598: 28,
    1566250206: 27,
    1384300223: 61,
    1296875960: 42,
    1962384926: 86,
    1073496482: 47,
    1247677375: 95,
    1065258604: 47,
    1732611967: 93,
    1145238372: 93,
    1067943368: 92,
    1171022880: 34,
    1959636843: 41,
    1578095851: 66,
    1531846987: 23,
    1692954538: 19,
    1117365355: 41,
    1344306208: 82,
    1274018031: 24,
    1224811489: 68,
    1352109699: 66,
    1885197329: 87,
    1170741186: 59,
    1470318933: 75,
    1331901175: 92,
    1216696512: 34,
    1708499062: 28,
    1097602870: 78,
    1499444343: 44,
    1739971801: 76,
    1530586023: 43,
    1152897392: 62,
    1789534645: 45,
    1846591742: 27,
    1375446835: 59,
    1420275031: 60,
    1497737130: 82,
    1635128800: 98,
}

# Create a new BST for library_users of the day:
library_users = BST()

# IDs of people that visited the library:
today_users = [1170741186, 1470318933, 1331901175, 1216696512,
            1708499062, 1097602870, 1499444343, 1739971801,
            1530586023, 1152897392, 1789534645, 1846591742,
            1375446835, 1420275031, 1497737130, 1635128800]

# inserting the IDs of the people that visited the library today:
for user in today_users:
    library_users.insert(user)

# Print a list of users with their respective gender:
print("TEST 1: Record of citizens that visited the library today:")
print("--------------------------------------------------")
# _______________________________________________________________________________________________
# IMPORTANT: change the following line to: "for user in reversed(library_users):" to use the
# reversed function instead
for user in (library_users): # Change this to  be "for user in reversed(library_users):"
    print(f"{user} entered the library and is {col_citizens[user]} years old.")

# Using BST library_users to get some stats (min age, max age, and average age):
user_count = 0
sum_ages = 0
old_age = 0
young_age = 100
for user in library_users:
    user_count += 1
    age = col_citizens[user]
    sum_ages += age
    if age >= old_age:
        old_age = age
    if age <= young_age:
        young_age = age

average = sum_ages / user_count
max_age = old_age
min_age = young_age

print()
print("TEST 2: Today's Stats:")
print("--------------")
print(f"The youngest person that visited today was {min_age} years old.")
print(f"The oldest person that visited today was {max_age} years old.")
print(f"The average age for today was {average} years old.")

# Check visits of certain people by using the contain function in the BST:
print()
print("TEST 3: Checking visits by certain individuals:")
print("---------------------------------------")

check_users = [1170741186, 1470318933, 1327939204]

for user in check_users:
    checking = user in library_users
    if checking == True:
        print(f"{user} visited the library today.")
    else:
        print(f"{user} didn't visit the library today.")
```

Here's the [Solution](/library_report_solution.py) for this program using the tree data structure.

[Back to Welcome Page](/README.md)