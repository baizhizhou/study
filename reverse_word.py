
'''按单词反转字符串：保持每个单词内的字母顺序不变，只是将单词的顺序反转'''

'''def reverse_word(s):
    s1 = s.split()
    i = 0
    j = len(s1)-1
    while i<j:
        s1[i],s1[j] = s1[j],s1[i]
        i +=1
        j -=1
    print(' '.join(s1))


reverse_word('That is a boy wh')'''

'''给你一个包含 n 个整数的数组 nums，
判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。'''


def three_list(arr):
    n = len(arr)
    res = []
    if n <3 :  #如果数没有三个数
        return None
    arr.sort() # 从小到大排序
    if sum(arr[::3]) >0 or sum(arr[-3:])<0: #判断数组最小三个数是否大于0和最大三个数是否小于0
        return None
    for i in range(n-2):
        if arr[i] >0:  # 判断数组第一个数是否大于0
            return None
        if arr[i]+sum(arr[-2:])<0 or sum(arr[i:i+3])>0:
            continue
        if i>0 and arr[i] ==arr[i-1]:
            continue
        low = i+1
        high = n-1
        while low <high:
            count = arr[i] +arr[low]+arr[high]
            if count <0:
                low +=1
            elif count >0:
                high -=1
            else:
                mid = [arr[i],arr[low],arr[high]]
                if mid not in res:
                    res.append(mid)
                low +=1
                high -=1
    print(res)

three_list([1,-2,-1,0,3])

