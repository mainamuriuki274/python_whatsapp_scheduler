# has all functions that relate to validation of numbers
# import module
import numbers


# function to validate number supplied by user
def check_phone_number(phonenumber):
    if phonenumber == "done":
        return phonenumber
    else:
        is_valid = False
        try:
            if any(not phonenumber.isalnum() for p in phonenumber):
                raise ValueError
            else:
                phonenumber = int(phonenumber)
        except ValueError as e:
            is_valid = False
        else:
            if isinstance(phonenumber, numbers.Number):
                if 8 < len(str(phonenumber)) < 16:
                    is_valid = True
        return is_valid


# Check options of when to send message
def check_options(choice):
    valid_choice = False
    if choice == "1" or choice == "2":
        valid_choice = True
    return valid_choice
