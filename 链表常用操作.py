from collections import deque
#创建链表
linkedlist=deque()
#添加元素
# O(1)
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
print(linkedlist)
# O(N)
linkedlist.insert(2,99)
print(linkedlist)

#访问某个元素

