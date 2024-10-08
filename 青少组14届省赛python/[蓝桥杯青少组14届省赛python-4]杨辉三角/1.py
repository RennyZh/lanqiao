'''【题目描述】杨辉三角就是一个用数排列起来的三角形，杨辉三角规则如下：
1）每行第一个数和最后一个数都为1，其它每个数等于它左上方和右上方的两数之和；
2）第n行有n个数。
注意：“列”指的是斜列。
                1
             1    1
          1    2    1
        1   3     3   1
     1    4    6    4    1
   1   5    10    10  5   1
       ...     ...     ...
小青对杨辉三角的特点和规律研究得很明白，现要考察你对杨辉三角的熟悉程度，首先告知你这是一个N行的杨辉三角，然后又告知了两个数值X和Y（X表示第几行，Y表示第几列），让你根据杨辉三角的特点和观察到的规律解决以下两个问题。
1）第X行第Y列对应的数是多少；
2）求出N行的杨辉三角中第Y列中所有数的和。
例如：N=5，X=5，Y=3。对于5行的杨辉三角，第5行第3列对应的数为6；第3列中所有数的和为10（10 = 6 + 3 + 1）。
【输入描述】
第一行输入一个正整数N（2≤N≤30），表示杨辉三角的行数
第二行输入两个正整数X和Y（1≤Y≤X≤N），分别表示第X行和第Y列，正整数之间以一个英文逗号隔开
【输出描述】
输出两个整数，分别表示N行的杨辉三角中第X行Y列对应的数，及第Y列上所有数的和，两个整数之间以一个英文逗号隔开
示例一
输入：
5
5,3
输出：
6,10
示例二
输入：
6
5,2
输出：
4,15
示例三
输入：
2
2,1
输出：
1,2'''
N = int(input())
XYls = input().split(',')
X = int(XYls[0])
Y = int(XYls[1])
PTls =[[1],
    [1,1]]
for i in range(2,N):
    nls = [1]#每一行的数
    for z in range(1, i):
        nls.append(PTls[i - 1][z - 1] + PTls[i - 1][z])#左上角的数加上方的数
    nls.append(1)
    PTls.append(nls)
#第Y列上所有数的和
sumY=0
for i in range(Y-1,N):
    sumY += PTls[i][Y-1]

print(str(PTls[X-1][Y-1])+','+str(sumY))