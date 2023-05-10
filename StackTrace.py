# https://www.educative.io/answers/what-is-stack-trace-in-python

# note from github contributor
# this code is intentionally buggy, can you understand it?


def printName(name, age):
    print("Hi, ", name)
    print("Are you", ag, " years old ?")


printName("Marry", 20)

# ----
# below is the stacktrace. i.e. when you run the code you get this in the terminal


# Hi,  Marry
# Traceback (most recent call last):
#   File "/root/code/Interview-Cheatsheet/StackTrace.py", line 12, in <module>
#     printName("Marry", 20)
#   File "/root/code/Interview-Cheatsheet/StackTrace.py", line 9, in printName
#     print("Are you", ag, " years old ?")
# NameError: name 'ag' is not defined. Did you mean: 'age'?


# ----
# stacktrace diagnosis
# 1) In line 5 of main.py the function printName(...) is called
# 2) In line 3 of main.py the variable ag is referenced before it is defined
