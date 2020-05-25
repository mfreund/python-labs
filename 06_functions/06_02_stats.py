'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list):
  maximum = max(list)
  print(f"The max is {maximum}")
  minimum = min(list)
  print(f"The min is {minimum}")
  avg = sum(list)/len(list)
  print(f"The average is {avg}")
  total = sum(list)
  print(f"The sum is {total}")

# call the function below here
stats(example_list)
