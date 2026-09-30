#Stack implementation using list

stack=[]

#Elements push onto stack(PUSH operation)
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after push elements:",stack)

#Elements pop from last(POP operation)
if stack:
    removed=stack.pop()
    print("Stack element popped:",removed)
    print("Stack after pop:",stack)
else:
    print("Stack is empty!")

#Access top element from stack(Peek element)
if stack:
    print("Top element:",stack[-1])
else:
    print("Stack is empty!")
