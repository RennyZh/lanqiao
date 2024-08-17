'''编程实现∶
有一块农田被划分为 N*M 块，农作物和杂草分布生长在农田中，其中农作物使用大写字母“R”表示，杂草使用大写字母“X”表示。请计算出农田中有几块独立的农作物区域（独立的农作物区域指该区域上下左右都被杂草围住，且 N*M以外的区域都是杂草）。
例如：N=4， M=4，4*4 的农田中农作物和杂草分布如下：
RRRX
RXRX
XXXR
RXXX
这块农田中有3块独立的农作物区域。
输入描述∶
第一行输入两个整数N和M (1≤N≤100, 1≤M≤100），N表示农田的行数，M 表示农田的列数，且两个正整数之间以一个逗号隔开；
接下来的N行每行包括M 个字符（字符只能为R或X），R 表示农作物，X 表示杂草，字符之间以一个逗号隔开
输出描述∶输出一个整数，表示N*M 的农田中有几块独立的衣作物区域
示例一
输入：
4,4
R,R,R,X
R,X,R,X
X,X,X,R
R,X,X,X
输出：
3
示例二
输入：
4,4
R,R,R,R
X,X,X,X
R,X,X,X
X,X,X,X
输出：
2
示例三
输入：
2,2
X,X
X,X
输出：
0
示例四
输入：
3,3
R,X,R
R,X,R
R,X,R
输出：
2'''
#输入
NMlst = input().split(',')
N = int(NMlst[0])#矩阵方格的行
M = int(NMlst[1])#矩阵方格的列
farmland = []#农田
for i in range(N):
    farm = input().split(',')
    farmland.append(farm)

def dfs(x,y):
    # 防止上下左右搜索超出边界或者遇到为X的区块
    if not 0<=x<N or not 0<=y<N or farmland[x][y] == 'X':
        return None
    farmland[x][y] = 'X'#已被搜索过，标记为X
    # 上下左右搜索
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
# 有多少块
c = 0
for i in range(N):
    for j in range(M):
        if farmland[i][j] == 'R':#当找到为R的块时开始深搜
            dfs(i,j)#将同一岛屿的全部标为R
            c+=1
print(c)