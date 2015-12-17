#3 ways to string format

name = raw_input("What is your name?: ")
age = raw_input("How old are you?: ")
user = raw_input("What is your username?: ")

# Concatenation
print "Your name is " + name + ", you are " + age + " years old, and your username is " + user

#String formatting with %, old way will be removed
print "Your name is %s, you are %s years old, and your username is %s" % (name, age, user)

#String formatting using {}, .format converts ints to str automatically. 
#Numbers in brackets can change order
print "Your name is {2}, you are {0} years old, and your username is {1}" .format(name, age, user)