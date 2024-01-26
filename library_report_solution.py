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

        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

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
print("TEST 1: Record of citizens that visited the library today (from largest to smallest ID):")
print("--------------------------------------------------")
for user in reversed(library_users):
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