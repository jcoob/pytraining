# This program says hello and ask for name

print("Hello, user")
print("What is your name?")
userName = input()
print("It is good to meet you, " + userName)
print("The lenght of your name is")
print(len(userName))
print("What is your age? ")
userAge = input()
print("So, you will be " + str(int(userAge) + 1) + " in a year.")