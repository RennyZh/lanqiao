'''编程实现：
有N个正整数，现对N （3≤N）个正整数进行不同方式的排列，每次排列后都会按照以下规则进行一次计算，聪明的小蓝发现，排列方式不同，最后计算出的结果也不相同。
计算规则：
第一次：第一个数乘以第二个数乘以第三个数，结果记录为 M(1)；
第二次：第二个数乘以第三个数乘以第四个数，结果记录为 M(2)；
第三次：第三个数乘以第四个数乘以第五个数，结果记录为 M(3)；
...
第N-2次：第N-2个数乘以第N-1 个数乘以第N 个数，结果记录为 M(N-2)。
最后计算M(1)+M(2)+M(3)....M(N-2)的数值。
请找出一种排列方式使这个数值最大。

例如：N=4，4个正整数分别为1，2，3，4，那么排列方式就会有24种；
其中排列方式为1，3，4，2时，按照规则计算2次：1*3*4=12，3*4*2=24；乘积相加：12+24=36。这种排序方式是所有乘积相加的数值最大，为 36。
输入描述：输入N个正整数 （3≤N），正整数之间以一个英文逗号隔开
输出描述：输出按照规则计算后的最大数值
示例一
输入：
1,2,3,4
输出：
36
示例二
输入：
2,3,4
输出：
24
示例三
输入：
1,2,3
输出：
6'''
#第1种方法
#输入
Nli = input().split(',')
for i in range(len(Nli)):
    Nli[i] = int(Nli[i])
Nli.sort(reverse=True)
c = 0
#1，3，4，2中可以找到规律:
#先把最大的数添加进列表
#再把剩余大的数插到列表首位
#再把剩余大的数添加放进列表
a = []
for i in range(len(Nli)):
    if i % 2==0:
        a.append(Nli[i])
    else:
        a.insert(0,Nli[i])
for i in range(0,len(a)-2):
    c+=(a[i]*a[i+1]*a[i+2])
print(c)


#第2种方法
import itertools # 迭代器，python内置模块
a = input().split(',')
for i in range(len(a)):
    a[i] = int(a[i])
n = len(a)
ans = 0
permutations = itertools.permutations(a) # 生成a的排列
for b in permutations:
    s = 0
    for i in range(n - 2):
        s += b[i] * b[i + 1] * b[i + 2]
        ans = max(ans, s)#比较哪一个比较大
print(ans)
