'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
user_num = int(input("Please enter a number between 0 and 1,000,000,000: "))
loop_num = 0

while loop_num != user_num:
    loop_num += 1
print(loop_num)
# less nesting

# while True:
#     if loop_num == user_num:
#         break
#     loop_num += 1
# print(loop_num)
