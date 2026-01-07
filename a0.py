# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Olivia Kong
# oykong@uci.edu
# 92692989

num = int(input())

if num == 1:
    print ("+-+")
    print ("| |")
    print ("+-+")
else:
    print ("+-+")
    print ("| |")
    print ("+-+-+")
    
    for i in range (1, num):
        space_count = "  " * i
        if i != num - 1:
            print (f"{space_count}| |")
            print (f"{space_count}+-+-+")
        elif i == num - 1:
            print (f"{space_count}| |")
            print (f"{space_count}+-+")
