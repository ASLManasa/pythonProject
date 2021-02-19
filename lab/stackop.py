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
    return stack[0]


stack = createStack()

push(stack, input())
push(stack, input())
push(stack, input())

print("Is Stack Empty ? " + isEmpty(stack))
print("The size of the Stack is " + size(stack))
print("The top element is " + top(stack))
print(pop(stack) + " popped from Stack")
