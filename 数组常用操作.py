#数组中的元素都是相同类型的

#创建数组
a=[]

#添加元素
#尾部添加 时间复杂度O(1)
a.append(1)
a.append(2)
a.append(3)
print(a)

#指定位置添加 时间复杂度O(N)
a.insert(2,99)
print(a)

#访问元素：用索引访问
temp=a[2]

print(temp)

#更新元素
a[2]=88
print(a)

#删除元素
#O(N)
a.remove(88)
print(a)
a.pop(1)
print(a)

#O(1)
a.pop()
print(a)

#获取数组长度
a=[4,5,6]
size=len(a)
print(size)

#遍历数组
#O(N)
for i in a:
    print(i)
for index,element in enumerate(a):
    print("Index at ",index,"is:",element)
for i in range(0,len(a)):
    print("i:",i,"element:",a[i])

#查找某个元素
#O(N)
#返回索引位置

index=a.index(6)
print(index)


#数组排序
a=[3,1,2]
a.sort()
print(a)
a.sort(reverse=True)
print(a)