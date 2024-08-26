'''编程实现∶X星的坦克战车很奇怪，它必须交替地穿越正能量辐射区和负能量辐射区才能保持正常运转，否则将报废。   某坦克需要从A区到B区去（A，B区本身是安全区，没有正能量或负能量特征），怎样走才能路径最短？
已知的地图是一个方阵，上面用字母标出了A，B区，其它区都标了正号或负号分别表示正负能量辐射区。
例如：
A + - + -
- + - - +
- + + + -
+ - + - +
B + - + -
坦克车只能水平或垂直方向上移动到相邻的区。
输入描述∶
输入第一行是一个整数n，表示方阵的大小， 4<=n<100；
接下来是n行，每行有n个数据，可能是A，B，+，-中的某一个，中间用空格分开。   A，B都只出现一次。
样例输出∶
要求输出一个整数，表示坦克从A区到B区的最少移动步数。
如果没有方案，则输出-1
示例一
输入：
5
A + - + -
- + - - +
- + + + -
+ - + - +
B + - + -
输出：
10
示例二
输入：
5
A + - + B
- + + + +
+ + + - +
+ + + + -
+ - + - +
输出：
4
示例三
输入：
4
A - + -
+ + + +
- + - +
B + - -
输出：
3'''
#1.输入
n = int(input())#接下来是n行
maze = [] #地图
for i in range(n):
    lines = input().split(' ')
    maze.append(lines)
# 2.创建是否访问过的列表
visit = []
for i in range(len(maze)):
    visit.append([0] * len(maze[0]))#0为未访问，1为访问过
#开始广度优先算法
def bfs(start,end):
    visit[start[0]][start[1]] = 1#将起始位置标记为已访问
    path = [[start,0]]#创建一个队列,记录路径  #[坐标,步数]#坐标:[x,x]
    while len(path) != 0:#循环至列表为空
        pathnow = path.pop(0)#将当前信息出队列
        posnow = pathnow[0]#当前坐标
        stepnow = pathnow[1]#当前步数
        if posnow == end:#到达终点返回步数
            return stepnow
        #上下左右查找
        move_0 = [-1,1,0,0]
        move_1 = [0,0,-1,+1]
        for i in range(4):
            x = posnow[0]+move_0[i]
            y = posnow[1]+move_1[i]
            #同时满足:
            #未访问的节点
            #该节点在二维列表内
            #该节点与原节点不同（+与-不同）
            if 0<=x<n and 0<=y<len(maze[0]):
                if visit[x][y] == 0:
                    if maze[x][y]!=maze[posnow[0]][posnow[1]]:
                        visit[posnow[0]][posnow[1]] = 1  # 当前位置标记为已访问
                        path.append([[x, y], stepnow + 1])#将下一个坐标与步数加入队列
    return -1

def findstart():#寻找到开始位置(A)
    for i in range(n):
        for j in range(len(maze[0])):
            if maze[i][j] == 'A':
                return [i,j]
def findend():#寻找到结束位置(B)
    for i in range(n):
        for j in range(len(maze[0])):
            if maze[i][j] == 'B':
                return [i,j]
start = findstart()
end = findend()
print(bfs(start,end))
