print("Welcome to my computer Quiz")

playing=input("Do you want to play? ")

if playing.lower()!="yes":
    quit()

print("Okay! let's play :")
score=0

answer=input("Which animal is known as the 'Ship of Desert?' ")
if answer.lower()=="camel":
    print("Correct!")
    score=score+1
else:
    print("Incorrect!!")
    
answer=input("Name the National Heritage Animal of India? ")
if answer=="elephant":
    print("Correct!")
    score=score+1
else:
    print("Incorrect!!")
    
answer=input("Who is the first citizen of India? ")
if answer.lower()=="the president of india":
    print("Correct!")
    score=score+1
else:
    print("Incorrect!!")
    
answer=input("Name the planet nearest to the earth? ")
if answer.lower()=="mercury":
    print("Correct!")
    score=score+1
else:
    print("Incorrect!!")
    
answer=input("Name the longest river on earth? ")
if answer=="nile":
    print("Correct!")
    score=score+1
else:
    print("Incorrect!!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5)*100) + "%")