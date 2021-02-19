print("****IMPLEMENTATION OF STACK***")


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return str((len(stack) == 0))


def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")


def pop(stack):
    if (len(stack) == 0):
        return ("Nothing")
    return stack.pop()


def size(stack):
    return str(len(stack))


def top(stack):
    if (len(stack) == 0):
        return ("Nothing")
    return stack[len(stack) - 1]


stack = createStack()
while True:
    print("push<value>")
    print("pop")
    print("top")
    print("size")
    print("isempty")
    print("quit")
    do = input("What would you like to do?").split()
    operation = do[0].strip().lower()
    if operation == "push":
        push(stack, do[1])
    elif operation == "pop":
        print(pop(stack), " is popped from stack")
    elif operation == "top":
        print("The top element is: ", top(stack))
    elif operation == "size":
        print("The size of the stack is: ", size(stack))
    elif operation == "isempty":
        print("Stack is empty or not: ", isEmpty(stack))
    elif operation == "quit":
        break
