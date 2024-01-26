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
    if phone_number in active_phones:
        print("Calling...")
    elif phone_number in inactive_phones:
        print("The phone number is incorrect or inactive for several months.")
    else:
        print("The phone number you are calling doesn't exists.")
        question = int(input("Would you like to purchase that phone number? (1 for Yes / 2 for No): "))
        if question == 1:
            # After purchase adding phone number to active set.
            active_phones.add(phone_number)
            print(f"Phone number: {phone_number} purchased!")
        elif question == 2:
            print("Call ended.")

def call(phone_number):
    """
    Makes a call to the given number.
    Parameter:
        phone_number = long integer
    """
    check_phone(phone_number)

# FUNCTIONS FOR INTERNAL WORKERS:

def remove_phone(phone_number):
    """
    Checks membership of phone number and removes it
    from active phones and adds it to inactive phones.
    Parameter:
        phone_number = long integer
    """
    if phone_number in active_phones:
        inactive_phones.add(phone_number)
        active_phones.remove(phone_number)
    elif phone_number in inactive_phones:
        print(f"Phone number: {phone_number} is already inactive.")
    else:
        print(f"Phone number: {phone_number} not found.")

def activate_phone(phone_number):
    """
    Checks membership of phone number and removes it
    from inactive phones and adds it to active phones.
    Parameter:
        phone_number = long integer
    """
    if phone_number in inactive_phones:
        active_phones.add(phone_number)
        inactive_phones.remove(phone_number)
        print(f"Phone number: {phone_number} has been activated.")

# TESTING:

active_list = [3456781, 3667878, 3214545,
                3689000, 3332122, 3546765]

inactive_list = [3556681]

# Add random numbers to both active and inactive sets:
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