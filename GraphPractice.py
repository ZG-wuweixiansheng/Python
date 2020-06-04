#ADT graph的实现有两种方式：邻接矩阵；邻接列表
#创建顶点类
class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
        self.distance=0
        self.color='white'
        self.pred=None
        self.discovery=0#记录开始探索时间
        self.finish=0#记录结束探索时间
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    def __str__(self):
        return str(self.id)+'connectedTo:'+str([i for i in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWight(self,nbr):
        return self.connectedTo[nbr]
    def getDistance(self):
        return self.distance
    def setDistance(self,dis):
        self.distance=dis
    def getColor(self):
        return self.color
    def setColor(self,clo):
        self.color=clo
    def getPred(self):
        return self.pred
    def setPred(self,pre):
        self.pred=pre
    def setDiscovery(self,dis):
        self.discovery=dis
    def setFinish(self,fin):
        self.finish=fin


# 创建Graph类
class Graph:
    def __init__(self):
        self.vertlist={}
        self.numvertices=0
    def addVertex(self,key):
        self.numvertices+=1
        newVertex=Vertex(key)
        self.vertlist[key]=newVertex
        return newVertex
    def getVertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertlist
    def addEdge(self,f,t,cost):
        if f not in self.vertlist:
            nv=self.addVertex(f)
        if t not in self.vertlist:
            nv=self.addVertex(t)
        self.vertlist[f].addNerghbor(self.vertlist[t],cost)
    def getVertices(self):
        return self.vertlist.keys()
    def __iter__(self):
        return iter(self.vertlist.values())


#图的应用--词梯问题
def bulidGraph(wordfile):
    d={}
    g=Graph()
    wfile=open(wordfile,'r')# 读取文件中的单词
    for line in wfile:#创建词桶，每个词桶中的单词只有一个字母不同
        word=line[:-1]
        for i in range(len(word)):
            bucket=word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket]=[word]
#     给同一个桶的单词添加顶点和边
    for bucket in d.keys()
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g
# 利用广度优先搜索Breadth First Search算法对单词关系图进行搜索
def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue=Queue()#创建顶点队列
    vertQueue.enqueue(start)
    while (vertQueue.size()>0):
        currentVert=vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor=='white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
class Queue:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
# 通过回溯函数确定最短词梯
def traverse(y):
    x=y
    while x.getPred:
        print(x.getId())
        x=x.getPred
    print(x.getId())

# 图的应用--骑士周游问题
# 创建合法走棋位置函数
def genLegalMoves(x,v,bdsize):
    newmoves=[]
    moveoffsets=[(-1,-2),(-1,2),(-2,-1),(-2,1),(1,2),(1,-2),(2,-1),(2,-2)]
    for i in moveoffsets:
        newx=x+i[0]
        newy=y+i[1]
        if legalCoord(newx,bdsize) and legalCoord(newy,bdsize):
            newmoves.append((newx,newy))
    return newmoves
def legalCoord(x,bdsize):
    if x>=0 and x<=bdsize:
        return True
    else:
        return False
# 构建走棋关系图
def knightGraph(bdsize):
    ktGraph=Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeId=postToNodeId(row,col,bdsize)
            newpoints=genLegalMoves(row,col,bdsize)
            for e in newpoints:
                nid=postToNodeId(e[0],e[1],bdsize)
                ktGraph.addEdge(nodeId,nid)
    return ktGraph
def postToNodeId(row,col,bdsize):
    return row*bdsize+col
# 深度优先搜索（Depth First Search）算法解决骑士周游问题
def knightTour(n,path,u,limit): #n:层次；path：路径，类似栈；u：当前顶点；limit：搜索总深度
    u.setColor('gray')
    path.append(u)
    if n<limit:
        nbrlist=list(u.getConnections())
        i=0
        done=False
        while i<len(nbrlist) and not done:
            if nbrlist[i].getColor()=='white':
                knightTour(n+1,path,nbrlist[i],limit)
            i+=1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done=True
    return done
# 骑士周游问题算法改进：Warnsdorff算法
# 将u的合法移动目标棋盘格进行排序：具有最少合法移动目标的格子优先搜索
def orderByAvail(n)
    reslist=[]
    for v in n.getConections():
        i=0
        for c in v.getConnections():
            if c.getColor=='white':
                i+=1
        reslist.append((i,v))
    reslist.sort(key=lambda x: x[0])
    return [y[1] for y in reslist]

# 通用的深度优先搜索算法
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()#保证子类进行初始化时还可以继承父类的属性
        self.time=0
    def dfs(self):
        for avertex in self:
            avertex.setColor('white')
            avertex.setPred(-1)
        for avertex in self:
            if avertex.getColor()=='white':
                avertex.dfsvisit(avertex)
    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time+=1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor()=='white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time+=1
        startVertex.setFinish(self.time)
# 拓扑排序 Topologicl Sort
# 从工作流程图到工作次序的排序
# 其算法在于根据通用深度优先搜索中每个顶点的结束时间进行从大到小的排序












