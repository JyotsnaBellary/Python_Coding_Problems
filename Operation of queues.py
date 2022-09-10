queue = [20,-9,-3,2,1]
print("queue originally:", queue)
queue.append(15)
queue.append(100)
print("stack after push operation:", queue)
queue.pop(0)
print("stack after pop operation:", queue)
print("value obtained after peek operation:", queue[len(queue)-1])
