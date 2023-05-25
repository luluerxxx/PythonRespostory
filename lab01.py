import sys
import re

# 词频统计
def gettext():
    file = open('C:\\test1\\The Masque of The Red Death - Edgar Allan Poe.txt', errors='ignore').read()
    # 单词全部小写
    file = file.lower()
    # 匹配the,a这个单词
    pattern1 = re.compile(r' the ')
    pattern2 = re.compile(r' a ')
    # 从file里找出the,a，是一个数组
    arr1 = pattern1.findall(file)
    arr2 = pattern2.findall(file)
    # 用空字符串替代the,a
    file = file.replace(arr1[0], "")
    file = file.replace(arr2[0], "")
    return file

file = gettext()
# 将一个字符串分裂成多个字符串组成的列表
words = file.split()
counts = {}
# 遍历words数组，计数++
for word in words:
    counts[word] = counts.get(word, 0) + 1
# 转换为列表
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
# 创建一个写的文件
file2 = open('xxx.txt', 'w')
for i in range(26):
    word, count = items[i]
    print(word, count)
    file2.write(word+" ")
    file2.write(str(count)+" ")
