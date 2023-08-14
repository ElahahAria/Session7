print('welcome to sort check code: ')
def sort(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

print ("enter your number list to check them ;)'")
arr = input("enter your list:")
arr = [int(x) for x in arr.split(",")]

if sort(arr):
    print("list is sorted.")
else:
    print("list is not sorted.")
print('welcome to my sort app: ')
def tartib(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

print ("make your int list:'")
arr = input("enter your list:")
arr = [int(x) for x in arr.split(",")]

if tartib(arr):
    print("tartib rayat shode!!!.")
else:
    print("tartib rayat nashode!!!.")