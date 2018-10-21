'''
	名称：Python基础|十个编程的小tips
	链接：https://mp.weixin.qq.com/s?__biz=MzUzOTkyMDU5Mg==&mid=2247483999&idx=1&sn=5edc8d3224cbd0a8dc5cba6171a685c0&chksm=fac053e0cdb7daf67f373e7561ec272521d70078738fb4b64b6deb70bb026279665926abed4f&mpshare=1&scene=22&srcid=1021rVPMwHq4NFske39SBudx#rd

'''
####################
# 1. 列表推导式
####################
print("\n-----------1. 列表推导式-----------\n")
bag = [1, 2, 3, 4, 5]  
for i in range(len(bag)):  
    bag[i] = bag[i] * 2


# 但是有更好的方法：
print("--new--")
bag = [elem * 2 for elem in bag]
print(f"bag:{bag}")
del bag


####################
# 2. 遍历列表
####################
print("\n-----------2. 遍历列表-----------\n")
bag = [1, 2, 3, 4, 5]  
for i in range(len(bag)):  
    print(bag[i])
del bag

# 取而代之的应该是这样：
print("--new--")
bag = [1, 2, 3, 4, 5]  
for i in bag:  
    print(i)
del bag

# 如果x是一个列表，你可以对它的元素进行迭代。
# 多数情况下你不需要各元素的索引，但如果你非要这样做，
# 那就用enumerate函数。它像下边的样子：
print("--new--")
bag = [1, 2, 3, 4, 5]  
for index, element in enumerate(bag):  
    print(index, element)
del bag


####################
# 3. 元素互换
####################
print("\n-----------3. 元素互换-----------\n")
a = 5 
b = 10
# 交换 a 和 b
tmp = a  
a = b  
b = tmp
print(f"a:{a};b:{b}")
del a,b,tmp

# 但Python提供了一个更自然更好的方法！
print("--new--")
a = 5  
b = 10  
# 交换a 和 b
a, b = b, a
print(f"a:{a};b:{b}")
del a,b


####################
# 4. 初始化列表
####################
print("\n-----------4. 初始化列表-----------\n")
# 假如你要一个是10个整数0的列表，你可能首先想到：
bag = []  
for _ in range(10):  
    bag.append(0)
print(f"bag:{bag}")
del bag

# 换个方式吧：
print("--new--")
bag = [0] * 10
print(f"bag:{bag}")
del bag

# 注意：如果你列表包含了列表，这样做会产生浅拷贝。
# 举个例子：
bag_of_bags = [[0]] * 5 # [[0], [0], [0], [0], [0]]
print(f"bag_of_bags:{bag_of_bags}")  
bag_of_bags[0][0] = 1 # [[1], [1], [1], [1], [1]]
print(f"bag_of_bags:{bag_of_bags}")
del bag_of_bags
# Oops！所有的列表都改变了，而我们只是想要改变第一个列表。

# 改一改啦：
print("--new--")
bag_of_bags = [[0] for _ in range(5)] 
print(f"bag_of_bags:{bag_of_bags}")  
# [[0], [0], [0], [0], [0]]
bag_of_bags[0][0] = 1  
print(f"bag_of_bags:{bag_of_bags}") 
# [[1], [0], [0], [0], [0]]
del bag_of_bags


####################
# 5. 构造字符串
####################
print("\n-----------5. 构造字符串-----------\n")
# 你会经常需要打印字符串。要是有很多变量，避免下面这样：
name = "Raymond"  
age = 22  
born_in = "Oakland, CA"  
string = "Hello my name is " + name + "and I'm " + str(age) + " years old. I was born in " + born_in + "."  
print(string)
del name,age,born_in,string

# 改一改啦：
print("--new--")
# 额，这看起来多乱呀？你可以用个漂亮简洁的方法来代替，.format。
name = "Raymond"  
age = 22  
born_in = "Oakland, CA"  
string = "Hello my name is {0} and I'm {1} years old. I was born in {2}.".format(name, age, born_in) 
print(string)
del name,age,born_in,string


####################
# 6. 返回tuples（元组）
####################
print("\n-----------6. 返回tuples（元组）-----------\n")
# Python允许你在一个函数中返回多个元素，这让生活更简单。
# 但是在解包元组的时候出出线这样的常见错误：
def binary():  
    return 0, 1

result = binary()  
zero = result[0]  
one = result[1]
del zero,one

print("--new--")
# 这是没必要的，你完全可以换成这样：
def binary():  
    return 0, 1

zero, one = binary()
print(f"zero:{zero};one:{one}")
del zero,one

# 要是你需要所有的元素被返回，用个下划线_：
zero, _ = binary()
print(f"zero:{zero};one:{_}")
del zero,_


####################
# 7. 访问Dicts（字典）
####################
print("\n-----------7. 访问Dicts（字典）-----------\n")
# 你也会经常给dicts中写入key，value（键，值）。
# 如果你试图访问一个不存在的于dict的key，
# 可能会为了避免KeyError错误，你会倾向于这样做：
countr = {}  
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]  
for i in bag:  
    if i in countr:
        countr[i] += 1
    else:
        countr[i] = 1

for i in range(10):  
    if i in countr:
        print("Count of {}: {}".format(i, countr[i]))
    else:
        print("Count of {}: {}".format(i, 0))
del countr,bag


print("--new--")
# 但是，用get()是个更好的办法。
print("\n####################\n")
countr = {}  
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]  
for i in bag:  
	# countr.get(i, 0) i 表示第几个key，0表示初始值
    countr[i] = countr.get(i, 0) + 1

for i in range(10):  
    print("Count of {}: {}".format(i, countr.get(i, 0)))
del countr,bag

# 当然你也可以用setdefault来代替。
# 这还用一个更简单却多费点开销的办法：
print("\n####################\n")
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]  
countr = dict([(num, bag.count(num)) for num in bag])

for i in range(10):  
    print("Count of {}: {}".format(i, countr.get(i, 0)))

print("\n####################\n")
# 你也可以用dict推导式。
countr = {num: bag.count(num) for num in bag}
for i in range(10):  
    print("Count of {}: {}".format(i, countr.get(i, 0)))

# 这两种方法开销大是因为它们在每次count被调用时都会对列表遍历。
del countr,bag


####################
# 8 使用库
####################
print("\n-----------8. 使用库-----------\n")
# 现有的库只需导入你就可以做你真正想做的了。

# 还是说前面的例子，我们建一个函数来数一个数字在列表中出现的次数。
# 那么，已经有一个库就可以做这样的事情。
from collections import Counter  
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]  
countr = Counter(bag)

for i in range(10):  
    print("Count of {}: {}".format(i, countr[i]))
'''
	一些用库的理由：
		代码是正确而且经过测试的。
		它们的算法可能会是最优的，这样就跑的更快。
		抽象化：它们指向明确而且文档友好，你可以专注于那些还没有被实现的。
		最后，它都已经在那儿了，你不用再造轮子了。
'''
del countr,bag

####################
# 9. 在列表中切片/步进
####################
print("\n-----------9. 在列表中切片/步进-----------\n")
# 你可以指定start的点和stop点，就像这样list[start:stop:step]。
# 我们取出列表中的前5个元素：
bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
for elem in bag[:5]:  
    print(f"elem:{elem}")
# 这就是切片，我们指定stop点是5，再停止前就会从列表中取出5个元素。
# 要是最后5个元素怎么做？
print("\n####################\n")
bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
for elem in bag[-5:]:  
    print(f"elem:{elem}")

# 没看明白吗？-5意味着从列表的结尾取出5个元素。
# 如果你想对列表中元素间隔操作，你可能会这样做：
print("\n####################\n")
bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
for index, elem in enumerate(bag):  
    if index % 2 == 0:        
        print(f"elem:{elem}")

# 但是你应该这样来做：
print("\n####################\n")
bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
print("--new--")
for elem in bag[::2]:  
    print(f"elem:{elem}")
# 或者用 ranges
print("--new--")
bag = list(range(0,10,2))  
print(f"bag:{bag}")


####################
# 10. tab键还是空格键
####################
print("\n-----------10. tab键还是空格键-----------\n")
'''
	长时间来看，将tab和空格混在一起会带来很多不必要的麻烦，
	你会看到IndentationError: unexpected indent。
	不管你选择tab键还是空格键，你应该在你的文件和项目中一直保持使用。

	一个使用空格而不是tab的原因是，tab不是在所有编辑器中都一样的。
	视呢所用的编辑器，tab可能会被当作2到8个空格。

	你也可以在写代码时用空格来定义tab。
	这样你可以自己选择用几个空格来当做tab。
	大多数Python用户是用4个空格。
'''
