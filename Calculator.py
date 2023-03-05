# Initial Thinking By eval 

'''We have not implimented that because it is 
very prone to errors and is not good with respect to security 
'''

# def Calculator(expression):
#     result = eval(expression)
#     return result


# expression = input("Enter a Number :-")
# Calculator(expression)


# Another Approach 

def isdigit_accumalator()




special_characters = list("!@#$%^&*()-+?_=,<>/")
result = [] 
expression = input()
storage_list = list(expression)

for i in storage_list:
    if i.isdigit():
        isdigit_accumalator()
    elif any(storage_list[0] and storage_list[-1]) == special_characters :
        raise ValueError
    