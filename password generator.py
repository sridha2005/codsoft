import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("----Password Generator----")
    try:
        length = int(input("enter desired password length:"))
    except ValueError:
        print("please enter a valid number")
        return
    password = generate_password(length)
    if password:
        print("\nGenerated Password:", password)
if __name__ == "__main__" :
   main()
        
