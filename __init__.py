print("Hello World! How are you doing?")
print("I am a program being written by Jamal Rodgers")
print("He is beginning to learn Python and this is his first program." + "\nFirst we're going to collect a little data on you"
      + "\n")


#this is my first comment in python


name=input("What is your name? ")
Name=name.capitalize()
#for input requiring numbers you need to specify the type

age=int(input("What is your age? "))
Age= str(age)
print("Hello " + Name + ", we will put your name as well as your age, " + Age + " in our records!")
print("Now let's continue " + Name + "!")
isemployer: str = input(" Are you a potential employer? ")
isEmployer=isemployer.capitalize()
links = ["hyperlink1","hyperlink2","hyperlink3"]
if isEmployer == "Yes":
    print("Thank you so much for taking the time to look at some of my work!")
    print("Here's some more work that I've done!")
    for x in links:
        print(x)
elif isEmployer == "No":
    print("Thank you so much for taking the time to look at some of my work!")

else:
    print("Thank you for your time! It seems as if your input isn't acceptable presently so please input something else. currently I cant process numbers or special characters, and im looking for yes or no answers.")

print()





