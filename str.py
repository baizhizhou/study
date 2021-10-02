
class Soution:
    def str(self):
        string = 'qwsf'

        s1 = string.capitalize()  # 把字符串的第一个字符大写
        print(s1)

        s2 = string.count('s', 0, len(string))  # 返回 s 在 string 里面出现的次数，0, len(string)指定则返回指定范围内
        print(s2)

        s3 = string.endswith('f', 0, len(string)) # 检查字符串是否以 f结束，如果是，返回 True,否则返回 False.
        print(s3)

        s4 = string.find('q', 0, len(string))  # 检测 q 是否包含在 string 中，如果是返回开始的索引值，否则返回-1
        print(s4)

        s5= string.index('s', 0, len(string))   # 跟find()方法一样，只不过如果s不在 string中会报一个异常.
        print(s5)
        
        s6 = string.isalnum()  # 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
        print(s6)

        s7= string.isalpha()  # string 至少有一个字符并且所有字符都是字母则返回
        print(s7)

        s8 = string.isdecimal()  #  只包含十进制数字则返回
        print(s8)

        s9 = string.isdigit()   # string 只包含数字则返回

        s10 = string.lower()  # string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写

        s11 = string.isnumeric() #   string 中只包含数字字符

        s12 = string.isspace()  # string 中只包含空格

        s13 = string.join(item) # 以 string 作为分隔符，将item 中所有的元素(的字符串表示)合并为一个新的字符串

        s14 = string.lower() #  所有大写字符为小写

        s15 = string.lstrip()  # 截掉string左边的空格
        max(str)  # 返回字符串str中最大的字母。
        min(str)  # 返回字符串str中最小的字母。

        s16 = string.replace(str1, str2, string.count(str1))  # str1 替换成 str2,则替换不超过 duos 次.


        s17 = string.split("s", string.count('s'))  # str 为分隔符切片  分成多少个个子字符串

        s18 = string.strip([obj])  # 在 string 上执行 lstrip()和 rstrip()

        s19 =  string.swapcase()  #  翻转 string 中的大小写

        s20 = string.title()  #  所有单词都是以大写开始，其余字母均为小写

        s21 = string.upper()  # 小写字母为大写


Soution().str()