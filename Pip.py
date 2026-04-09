
import random 
number = random.randint(1, 100)

print("Welcome to the guessing game ")
print("You have 10 chances to get it right")
Max_attempts = 10
count = 0  

while True:
    a = int(input("Enter a number between 1 and 100: "))
    if a == number:
        print("Good job you guessed correctly")
        break 

    elif a > number :
        print("Too high"
              "\n guess again ") 
        count += 1 

    elif a < number :
        print("Too low "
              "\n guess again") 
        count += 1 
    if count == Max_attempts and a != number :
        print("Game over"
            "\n You have used up all your chances")
        break
    print(count)
    
        
       

           