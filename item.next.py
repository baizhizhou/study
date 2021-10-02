


# 链表
class Node:
    # 节点类
    def __init__(self,item):
        self.item = item # 保存值域
        self.next = None  # 设置指针域，开始不知道指向谁，就直接指向空
# 创建单链表
class Solution:
    def __init__(self):
        self.header = None # 定义头节点， 如果head为None，实际上意味着这是一个空的链表

    def is_empty(self): #判断是否为空
        if self.header ==None: # 如果head为None，实际上意味着这是一个空的链表
            return True
        else:
            return False

    def length(self): # 返回长度
        cur = self.header  # cur 为游标，用来移动
        num = 0        # 用来记录数量
        while cur != None:
            num += 1
            cur = cur.next
        return num

    def travel(self): # 遍历整个链表
        cur = self.header
        while  cur != None:
            print(cur.item)
            cur  = cur.next

    def add(self,item):   # 头部添加元素，
        node =Node(item) # 建立一个新节点
        node.next = self.header
        self.header = node # 原有链表为空链表


    def append(self,item): # 尾部添加元素
        node = Node(item)
        if self.is_empty():
            self.header = node
        else:
            cur = self.header
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item): # 指定位置添加元素
        # params:pos 从0开始
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.header  # header所指的对象，不是headers本身
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 当循环结束后，pre指向pos-1节点
            node.next= pre.next
            pre.next =node

    def remove(self,item): # 删除节点
        cur = self.header
        pre = None
        while cur != None:
            if cur.item == item:
                # 判断此节点是否是头节点
                if cur ==self.header:
                    self.header = cur.next
                else:
                    pre.next = cur.next
                    break
            else:
                pre = cur
                cur = cur.next





    def search(self,item): # 查找节点是否存在
        cur =  self.header # 指向第一个数
        while cur != None:
            if cur.item == item: # cur.item 指链表元素 =？ 目标元素
                return True
            else:
                cur =cur.next
        return False


s = Solution() # 初始化
s.append(1)
# s.append(2)
print(s.is_empty())
print(s.length())
print('---')

# s.insert(1,9)
s.travel()
print(s.search(7))
print('----')
s.remove(1)
s.travel()
