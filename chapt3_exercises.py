# 1 Rewrite your pay computation (from Chapt2) to give the employees 1.5 times the hourly rate for hours worked above 40 hours.

# pay computation from Chapt2
# rate = input('Rate: ')
# hours = input('Hours: ')
# pay = round(float(rate) * float(hours))
# print('Pay:', pay)

# hours = input('Hours: ')
# h_number = float(hours)
# rate = input('Rate: ')
# r_number = float(rate)
# # pay = float(hours) * (float(rate) * 1.5)

# if h_number > 40:
#     print('Pay: ', round((h_number * 1.5) * r_number))
# else:
#     print('Pay: ', round(h_number * r_number))

# ----------------------------------------------------------------

# 2 Rewrite your pay program using 'try' and 'except' so that your program handles non-numeric input gracefully by printing a message and exiting the program.

# Examples
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: fort
# Error, please enter a numeric input

# hours try and except
# inp_hours = input('Hours: ')
# try:
#     num_hours = float(inp_hours)
# except:
#     print('please enter a number')
#     del inp_hours
#     inp_hours = input()
#     num_hours = float(inp_hours)

# # rate try and except
# inp_rate = input('Rate: ')
# try:
#     num_rate = float(inp_rate)
# except:
#     print('please enter a number')
#     del inp_rate
#     inp_rate = input()
#     num_rate = float(inp_rate)

# if num_hours > 40:
#     print('Pay: ', round((num_hours * 1.5) * num_rate))
# else:
#     print('Pay: ', round(num_hours * num_rate))

# ----------------------------------------------------------------

# 3 Write a program to prompt a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

# >= 0.9  A
# >= 0.8  B
# >= 0.7  C
# >= 0.6  D
# <  0.6  F

# Enter score: 0.95
# A

# Enter score: perfect
# Bad score

# Enter score: 10.0
# Bad score

# Enter score: 0.75
# C

# Enter score: 0.5
# F

# Run the program repeatedly as shown above to test the various different values for input.

score = input('Input a score between 0.0 and 1.0: ')
num_score = float(score)

if num_score < 0.0 or num_score > 10:
    print('Bad score')
elif num_score >= 0.9:
    print('A')
elif num_score >= 0.8:
    print('B')
elif num_score >= 0.7:
    print('C')
elif num_score >= 0.6:
    print('D')
elif num_score < 0.6:
    print('F')
