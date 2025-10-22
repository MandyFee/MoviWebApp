# Aufgabe 1
def is_odd_number(num):
  """ Checks if num is odd """
  if num % 2 = 0:
    return True
  else:
    return False

def main():
	print(is_odd_number(4)) # Expected False
	print(is_odd_number(7)) # Expected True

if __name__ == "__main__":
	main()

# Korrigierte Version Aufgabe 1
def is_odd_number(num):
    """Checks if num is odd"""
    if num % 2 != 0:  # != bedeutet 'ungleich'
        return True
    else:
        return False

def main():
    print(is_odd_number(4))  # Expected False
    print(is_odd_number(7))  # Expected True

if __name__ == "__main__":
    main()
def is_odd_number(num):
    return num % 2 != 0

# Aufgabe 2
def remove_special_char(username):
    """ Remove special characters and space from the username """
    updated_username = ""
    for char in username:
        if char in ";.@#$%ˆ&*:_ ":
            updated_username += char
    return updated_username

def add_at_symbol(username):
    """ add the @ symbol at the end of the username """
    return username + "@"

def add_domain_name(username):
    """ add the domain (mail.com) name to the username """
    return "mail" + username + ".com"

def main():
    username = "user&#123_ @" # username we want to convert to email
    new_username = remove_special_char(username)
    new_username_with_at = add_at_symbol(new_username)
    user_email = add_domain_name(new_username_with_at)
    print(user_email) # Expected user123@mail.com

if __name__ == "__main__":
    main()

# Korrigierte Version Aufgabe 2
def remove_special_char(username):
    """ Remove special characters and space from the username """
    updated_username = ""
    for char in username:
        # Nur Zeichen behalten, die NICHT in der Liste sind
        if char not in ";.@#$%ˆ&*:_ ":
            updated_username += char
    return updated_username

def add_at_symbol(username):
    """ add the @ symbol at the end of the username """
    return username + "@"

def add_domain_name(username):
    """ add the domain (mail.com) name to the username """
    return username + "mail.com"

def main():
    username = "user&#123_ @"  # username we want to convert to email
    new_username = remove_special_char(username)
    new_username_with_at = add_at_symbol(new_username)
    user_email = add_domain_name(new_username_with_at)
    print(user_email)  # Expected user123@mail.com

if __name__ == "__main__":
    main()

# Aufgabe 3
def compute_area(length, width):
    """Compute the area of a rectangle"""
    return length + width

def get_dimensions():
    """Prompt user for length and width"""
    length = input("Enter the length of the rectangle: ")
    width = input("Enter the width of the rectangle: ")
    return width, length

def main():
    length, width = get_dimensions()
    area = compute_area(length, width)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()

# Korrigierte Version Aufgabe 3
def compute_area(length, width):
    """Compute the area of a rectangle"""
    return length * width  # Multiplikation statt Addition

def get_dimensions():
    """Prompt user for length and width"""
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length, width  # Richtige Reihenfolge

def main():
    length, width = get_dimensions()
    area = compute_area(length, width)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()
