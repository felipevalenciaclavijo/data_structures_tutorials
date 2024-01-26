# Sets

## What is a Set?

When the order in a list is irrelevant that's when you can take advantage of a set data structure. A set cares for uniqueness but ignores the order, meaning that there couldn't be duplicate data within a list but they can be located anywhere in the list, contrary to what other data structures would allow.

## The purpose of a Set

As mentioned early, when we don't care about the order of the data we can boost performance, even when handling massive amounts of data to have a fast way of adding, removing, and finding data, that's when the set becomes your best friend. In fact, to add, remove, and find data in a set you will always achieve an **O(1)** performance which is literally the best you can get.

The characteristic of not allowing duplicates, it's key for finding membership within a list. There are thousands of circumstances where duplicates are errors, so handling duplicates properly with a set is a great way to tackle that.

Take for example email accounts. As you might already know, emails are unique IDs for users. Order is irrelevant, but uniqueness is key to having a functional system with thousands of emails.

![my set illustration](/my_set_diagram.png)

## Working with sets in Python

To create a set in Python we use the **set()**: 

```
emails = set()
```
To add data in the set we use the **.add**:

```
emails.add("daniel.hans1@gmail.com")
```
To remove we use the **.remove**:

```
emails.remove("daniel.hans1@gmail.com")
```

To check membership within a set we do the following:

```
value = "daniel.hans1@gmail.com"

if email in emails:
    print("Found it! :)")
else:
    print("Not found :(")
```
To get how many emails you have we simply use the length:

```
quantity_emails = len(emails)
```
Let's see it more clearly with the following example:

```
emails = set()

# Add:
emails.add("daniel.hans1@gmail.com")
emails.add("raul.serna23@gmail.com")
emails.add("mike.thomas45@gmail.com")
emails.add("james.szendre12@gmail.com")
emails.add("val.foster094@gmail.com")
# trying to add a duplicate email:
emails.add("val.foster094@gmail.com")

print(emails)

# Remove:
emails.remove("raul.serna23@gmail.com")
emails.remove("james.szendre12@gmail.com")

print()
print(emails)
print()
# Check membership:
email_test = ["mike.thomas45@gmail.com", "james.szendre12@gmail.com"]

for email in email_test:
    if email in emails:
        print(f"{email} found! :)")
    else:
        print(f"{email} not found :(")

# Quantity of emails:
print()
quantity_emails = len(emails)
print(quantity_emails)
```

**Output:**
```
{'val.foster094@gmail.com', 'mike.thomas45@gmail.com', 'raul.serna23@gmail.com', 'james.szendre12@gmail.com', 'daniel.hans1@gmail.com'}

{'val.foster094@gmail.com', 'mike.thomas45@gmail.com', 'daniel.hans1@gmail.com'}

mike.thomas45@gmail.com found! :)
james.szendre12@gmail.com Not found :(

3
```
**NOTE:** It's important to recognize that I tried to add a duplicate email, yet it wasn't duplicated within the set when printed.

## Example: Names Registered in the National Civil Registry

![Registraduria Logo](https://www.registraduria.gov.co/sites/-Sistema-Integral-de-Capacitacion-Electoral-/assets/img/logo-registraduria-siglo.svg)

Image published in: [Registraduria](www.registraduria.gov.co)

The National Civil Registry (Registraduría Nacional del Estado Civil) it's a government entity dedicated to recording all Colombians, they keep records of people at birth with relevant data and they are given unique IDs. They used this data for research purposes as well. The National Civil Registry keeps a huge list of unique names too, we are going to simulate the record-keeping of unique names in Colombia.

**We need to create a program that can:**
* Add new names
* Verify if a name already exists
* Count the total of unique names

**Function** | **Inputs**      | **Outputs**
-------------|-----------------|--------------
new_name | name         | Add a new name to the names set
verify_existence | name           | Checks for membership  within the names set, if it's not in the set call the new_name function
total_unique_names         | none            | Length of the names set

Here is the implementation for these 3 functions:

```
# Create a set for the names:
names = set()

def new_name(name):
    """
    Adds a new name to the set
    Parameter:
        name: string
    """
    names.add(name)
    print(f"{name} added!")

def verify_existence(name):
    """
    Verifies if the name already
    exists in the set
    Parameter:
        name: string
    """
    if name in names:
        print(f"{name} already exists.")
    else:
        print(f"{name} is new. We have added it to the set.")
        new_name(name)
    
def total_unique_names():
    """
    Counts the number of unique names
    """
    quantity = len(names)
    return quantity

# TESTING:

names_list = ["Juan", "Felipe", "Carlos",
            "Daniel", "Raul", "Pedro",
            "Miguel", "Laura", "Helena",
            "Jasmine", "Yazmin", "Jasmin"]

# Add names to the set:
for name in names_list:
    new_name(name)

print()
print("Names in set:")
print(names)
print()
print(f"There are {total_unique_names()} total unique names in Colombia's records")

print()
print("Verify the existence of certain names:")
print("*If a name doesn't exist it is added to the set.")
print()
verify_existence("Helena")
verify_existence("Raul")
verify_existence("Jasmine")
verify_existence("Jacob")
print()
print(names)
print()
print(f"There are {total_unique_names()} total unique names in Colombia's records")

```
**Output:**
```
Juan added!
Felipe added!
Carlos added!
Daniel added!
Raul added!
Pedro added!
Miguel added!
Laura added!
Helena added!
Jasmine added!
Yazmin added!
Jasmin added!

Names in set:
{'Pedro', 'Daniel', 'Yazmin', 'Helena', 'Juan', 'Raul', 'Carlos', 'Miguel', 'Jasmine', 'Jasmin', 'Laura', 'Felipe'}

There are 12 total unique names in Colombia's records

Verify the existence of certain names:
*If a name doesn't exist it is added to the set.

Helena already exists.
Raul already exists.
Jasmine already exists.
Jacob is new. We have added it to the set.
Jacob added!

{'Pedro', 'Daniel', 'Yazmin', 'Jacob', 'Helena', 'Juan', 'Raul', 'Carlos', 'Miguel', 'Jasmine', 'Jasmin', 'Laura', 'Felipe'}

There are 13 total unique names in Colombia's records
```

## Problem to Solve: Phone Company

A Phone Company wants to implement a program to keep track of active phone numbers and inactive phone numbers while allowing **external users** to make calls or at least know if the number they are calling is inactive or doesn't exists yet, if it doesn't exist the user can purchase it.

On the other hand, **internal users** need to remove phone numbers that have been inactive for several months or reactivate phone numbers that were inactive.

You will have to create the code for the following 4 functions in order for it to work properly:

**Function** | **Inputs**      | **Outputs**
-------------|-----------------|--------------
call | phone_number         | Calls the check_phone function
check_phone | phone_number           | Checks membership of phone number to make a call, know the status of that phone number, or purchase it if available.
remove_phone         | phone_number            | Removes the phone number from active numbers and adds it to inactive numbers
activate_phone         | phone_number            | Removes the phone number from inactive numbers and adds it to active numbers

**Instructions:**
* The **check_phone** function checks if the phone number is in the **active_phones** set, if it is there, it should print: *"Calling..."*
* The **check_phone** function checks if the phone number is in the **inactive_phones** set, if it is there, it should print: *"The phone number is incorrect or inactive for several months."*
* If none of the two previous statements is true, then **check_phone** function should print: *"The phone number you are calling doesn't exists."* and request the user for input: *"Would you like to purchase that phone number? (1 for Yes / 2 for No): "*. Depending on the answer, if it's 1 it should print: *"Phone number: {**display phone_number here**} purchased!"*. If the answer is 2: *"Call ended."*
* The **call** function should be fairly simple, you just have to call the **check_phone**.
* The **remove_phone** function should basically allow you to remove the phone number from the **active_phones** set and add it to the **inactive_phones** set. Remember to verify membership, so when a worker tries to remove a phone number that has already been removed, it prints the following message: *"Phone number: {**display phone_number here**} is already inactive."* Additionally, if a worker tries to remove a phone number that doesn't exists in any of the two sets, put the following message: *"Phone number: {**display phone_number here**} not found."*
* Lastly, the **activate_phone** function does the opposite to the **remove_phone** function. When succesfully acomplished make sure to print the following message: *"Phone number: {**display phone_number here**} has been activated."*

If you followed the instructions correctly and applied sets in Python properly, your result should be as follow (Keep in mind that your printed sets could have a different order due to the nature of a set, but make sure the data in them is the same for each situation).

**Output:**
```
John calls an active phone number.
Calling...

John calls an inactive phone number.
The phone number is incorrect or inactive for several months.

John calls a phone number that hasn't been used before.
The phone number you are calling doesn't exists.
Would you like to purchase that phone number? (1 for Yes / 2 for No): 1
Phone number: 3006688 purchased!

Andrea is a worker at the Phone Company.
She has been asked to remove several phone         
numbers that haven't been used for several months. 
Active phones should only be: 3456781, 3689000,    
and 3006688 if purchased in the last step:
{3006688, 3689000, 3456781}

Removed active phones should be listed in inactive phones now:
{3667878, 3556681, 3546765, 3214545, 3332122}

A customer contacted Andrea and requested to
reactivate his inactive phone number:
Phone number: 3332122 has been activated.
Active phones should only be: 3456781, 3689000,
and 3006688 if purchased in the last step plus
the one reactivated 3332122:
{3006688, 3332122, 3689000, 3456781}

Reactivated phone number shouldn't be in inactive phones now:
{3667878, 3556681, 3546765, 3214545}
```
Below is the [Unsolved Program](/phone_company_unsolved.py) that is missing the code for the 4 functions mentioned above. At the end are the lines of code to test if your functions are working properly (make sure to compare it with the output given above).

```
# Create sets for active phone numbers and inactive ones:
active_phones = set()
inactive_phones = set()

# FUNCTIONS FOR END USER:

def check_phone(phone_number):
    """
    Checks membership of phone number to make a call,
    Know the status of that phone number, or purchase it
    if available.
    Parameter:
        phone_number = long integer
    """
    # YOUR CODE GOES HERE:
    pass


def call(phone_number):
    """
    Makes a call to the given number.
    Parameter:
        phone_number = long integer
    """
    # YOUR CODE GOES HERE:
    pass

# FUNCTIONS FOR INTERNAL WORKERS:

def remove_phone(phone_number):
    """
    Checks membership of phone number and removes it
    from active phones and adds it to inactive phones.
    Parameter:
        phone_number = long integer
    """
    # YOUR CODE GOES HERE:
    pass

def activate_phone(phone_number):
    """
    Checks membership of phone number and removes it
    from inactive phones and adds it to active phones.
    Parameter:
        phone_number = long integer
    """
    # YOUR CODE GOES HERE:
    pass

# TESTING-----------------------------------------

active_list = [3456781, 3667878, 3214545,
                3689000, 3332122, 3546765]

inactive_list = [3556681]

# Add numbers to both active and inactive sets:
for number in active_list:
    active_phones.add(number)

for number in inactive_list:
    inactive_phones.add(number)

print("John calls an active phone number.")
call(3689000) # Calling...

print()
print("John calls an inactive phone number.")
call(3556681) # The phone number is incorrect
              # or inactive for several months.

print()
print("John calls a phone number that hasn't been used before.")
call(3006688) # Depending on the response it can show:
              # Phone number: 3006688 purchased! or
              # Call ended.

print()
print("Andrea is a worker at the Phone Company.")
print("She has been asked to remove several phone\
    \nnumbers that haven't been used for several months.")
remove_phone(3667878)
remove_phone(3214545)
remove_phone(3546765)
remove_phone(3332122)
print("Active phones should only be: 3456781, 3689000,\
    \nand 3006688 if purchased in the last step:")
print(active_phones)
print()
print("Removed active phones should be listed in inactive phones now:")
print(inactive_phones)
print()
print("A customer contacted Andrea and requested to\
    \nreactivate his inactive phone number:")
activate_phone(3332122)
print("Active phones should only be: 3456781, 3689000,\
    \nand 3006688 if purchased in the last step plus\
    \nthe one reactivated 3332122:")
print(active_phones)
print()
print("Reactivated phone number shouldn't be in inactive phones now:")
print(inactive_phones)
```

Here's the [Solution](/phone_company_solution.py) for this program using the set data structure.

[Back to Welcome Page](/README.md)