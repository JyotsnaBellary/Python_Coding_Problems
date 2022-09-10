stack = [20,-9,-3,2,1]
print("stack originally:", stack)
stack.append(15)
stack.append(100)
print("stack after push operation:", stack)
stack.pop()
print("stack after pop operation:", stack)
print("value obtained after peek operation:", stack[len(stack)-1])
