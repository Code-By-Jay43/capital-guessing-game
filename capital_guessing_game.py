score = 0  # Initialize score variable

print("What is the capital of France?")

x = input().lower()

if x == "paris":
    score+=1
    print("Good job, you got it correct! Your score is:", score)

else:
    print("You didn't get it correct. The correct answer was Paris. Your score is:", score)


print("What is the capital of India?")

y = input().lower()

if y == "new delhi":
    score+=1
    print("Good job, you got it correct! Your score is:", score)

else:
    print("You didn't get it correct. The correct answer was New Delhi. Your score is:", score)
    
print("What is the capital of Australia?")

z = input().lower()


if z == "canberra":
    score+=1
    print("Good job, you got it correct! Your final score is:", score, "out of 3")

else:
    print("You didn't get it correct. The correct answer was Canberra. Your final score is:", score, "out of 3")