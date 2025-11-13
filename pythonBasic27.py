#While loop in Python
#While loops are used to repeatedly execute a block of code as long as a given condition is
#true. The syntax for a while loop in Python is straightforward.
#Example 1: Basic while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment count by 1
#Example 2: Using else with while loop
num = 0
while num < 3:
    print("Number is:", num)
    num += 1
else:
    print("While loop has ended")
#Example 3: Using break and continue in while loop
i = 0
while i < 5:
    if i == 3:
        break  # Exit the loop when i is 3
    print("i is:", i)
    i += 1
j = 0
while j < 5:
    j += 1
    if j == 3:
        continue  # Skip the iteration when j is 3
    print("j is:", j)
#Example 4: Using pass in while loop
k = 0
while k < 5:
    if k == 3:
        pass  # Do nothing when k is 3
    print("k is:", k)
    k += 1
# Output the value of k from 0 to 4
#Example 5: Infinite loop (commented out to prevent actual infinite execution)
# while True:
#     print("This is an infinite loop")
# Output a message repeatedly
# To stop the infinite loop, you would typically use a break statement or an external interrupt.
# Example 6: While loop with a list
myList = [1, 2, 3, 4, 5]
index = 0
while index < len(myList):
    print("List element:", myList[index])
    index += 1
# Output each element in the list using a while loop
# Example 7: While loop with user input (commented out to prevent waiting for input)
# user_input = ""
# while user_input.lower() != "exit":
#     user_input = input("Enter something (type 'exit' to quit): ")
#     print("You entered:", user_input)
# Output user input until 'exit' is entered
