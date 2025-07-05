import random

#Creating a list of characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



#Function that passes through user inputs
def generate_password(user_letters, user_symbols, user_numbers):
    
    password = "" #creating an empty variable 
    
    #For loop to loop through and pick randomly from the letters, symbols, and numbers list user the user number input. 
    for _ in range(user_letters):
        password += random.choice(letters)
        
    for _ in range(user_symbols):
        password += random.choice(symbols)
        
    for _ in range(user_numbers):
        password += random.choice(numbers)
        
    return password
        

def main():
    
    print("Hi buddy, lets make these hackers struggle with getting through us!")

    user_letters = int(input("How many letters(Alphabets) do you want included in your password?\n"))
    user_symbols = int(input("How many symbols do you want included in your password?\n"))
    user_numbers = int(input("How many numbers do you want included in your password?\n"))

    password = generate_password(user_letters, user_symbols, user_numbers)
    
    print(password)
    
#calling the main function 
if __name__ == "__main__":
    main()