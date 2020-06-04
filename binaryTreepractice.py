#非线性数据结构--树
#树的列表实现
def Binarytree(r):
    return [r,[],[]]
def insertLeft(root,newbranch):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[newbranch,t,[]])
    else:
        root.insert(1,[newbranch,[],[]])
    return root
def insertRight(root,newbranch):
    t=root.pop(2)
    if len(t)>1:
        root,insert(2,[newbranch,[],t])
    else:
        root.insert(2,[newbranch,[],[]])
    return root
def getrootvalue(root):
    return root[0]
def setrootvalue(root,newvalue):
    root[0]=newvalue
def getleftchild(root):
    return root[1]
def getrightchild(root):
    return root[2]


#树的链表实现
class BinaryTree():
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftchild=None
        self.rightchild=None
    def insertLeft(self,newnode):
        if self.leftchild==None:
            self.leftchild=BinaryTree(newnode)
        else:
            t=BinaryTree(newnode)
            t.leftchild=self.leftchild
            self.leftchild=t
    def insertRight(self,newnode):
        if self.rightchild==None:
            self.rightchild=BinaryTree(newnode)
        else:
            t=BinaryTree(newnode)
            t.rightchild=self.rightchild
            self.rightchild=t
    def getleftchild(self):
        return self.leftchild
    def getrightchild(self):
        return self.rightchild
    def setRootVla(self,obj):
        self.key=obj
    def getRootVla(self):
        return self.key
    def preorder(self):#前序遍历
        print(self.key)
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.oreorder()



#树的应用：表达式解析
def bulidParseTree(fpexp):
    fplist=[i for i in fpexp]
    pstack=Stack()
    etree=BinaryTree('')
    pstack.push(etree)
    currenttree=etree
    for i in fplist:
        if i =="(":
            currenttree.insertLeft('')
            pstack.push(currenttree)
            currenttree=currenttree.getleftchild()
        elif i not in ['+','-','*','/',')']:
            currenttree.setRootVla(int(i))
            parent=pstack.pop()
            currenttree=parent
        elif i in ['+','-','*','/']:
            currenttree.setRootVla(i)
            currenttree.insertRight('')
            pstack.push(currenttree)
            currenttree=currenttree.getrightchild()
        elif i==')':
            currenttree=pstack.pop()
        else:
            raise ValueError
    return etree

class Stack:
    def __init__(self):
        self.items=[]
    def Isempty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

import operator
def evaluate(parsetree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftc=parsetree.getleftchild()
    rightc=parsetree.getrightchild()
    if leftc and rightc:
        fn=opers[parsetree.getRootVla()]
        return fn(evaluate(leftc),evaluate(rightc))
    else:
        return parsetree.getRootVla()
parsetree1=bulidParseTree('(3*(4+5))')
#print(evaluate(parsetree1))

#中序遍历递归生成全括号中缀表达式
def printexp(tree):
    sVal=''
    if tree.getleftchild()==None and tree.getrightchild()==None:
        return str(tree.getRootVla())
    sVal='('+printexp(tree.getleftchild())
    sVal=sVal+str(tree.getRootVla())
    sVal=sVal+printexp(tree.getrightchild())+')'
    return sVal
expression=bulidParseTree('(3*(4+5))')
#print(evaluate(expression))
#print(printexp(expression))


#无嵌套列表的二叉堆实现优先队列
class BinHeap:
    def __init__(self):
        self.heapList=[0]
        self.currentsize=0
    def perup(self,i):
        stop=False
        while i//2>0 and not stop:
            if self.heapList[i]<self.heapList[i//2]:
                temp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=temp
            else:
                stop=True
            i//=2
    def insert(self,key):
        self.heapList.append(key)
        self.currentsize+=1
        self.perup(self.currentsize)
    def perdown(self,i):
        stop=False
        while i*2<=self.currentsize and not stop:
            mc=self.minchild(i)
            if self.heapList[mc]<self.heapList[i]:
                temp=self.heapList[i]
                self.heapList[i]=self.heapList[mc]
                self.heapList[mc]=temp
            else:
                stop=True
            i=mc
    def minchild(self,i):
        if 2*i+1>self.currentsize:
            return 2*i
        else:
            if self.heapList[2*i]<self.heapList[2*i+1]:
                return 2*i
            else:
                return 2*i+1
    def delMin(self):
        retval=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentsize]
        self.currentsize-=1
        self.heapList.pop()
        self.perdown(1)
        return retval


#二叉搜索树
class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size+=1
    def _put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasleftchild():
                self._put(key,val,currentNode.leftchild)
            else:
                currentNode.leftchild=TreeNode(key,val,parent=currentNode)
               # self.updateBanlance(currentNode.leftchild)#更新平衡因子，优化二叉搜索树为AVL树
        else:
            if currentNode.hasrightchild():
                self._put(key,val,currentNode.rightchild)
            else:
                currentNode.rightchild=TreeNode(key,val,parent=currentNode)
                #self.updateBanlance(currentNode.rightchild)#更新平衡因子，优化二叉搜索树为AVL树
    # def updateBanlance(self,node):#定义更新平衡因子的方法，优化二叉搜索树为AVL树
    #    if node.banlancefactor>1 or node.banlancefactor<-1:
    #        self.rebanlance(node)
    #        return
    #    if node.parent!=None:
    #        if node.isleftchild():
    #            node.parent.banlancefactor+=1
    #        elif node.isrightchild():
    #            node.parent.banlancefactor-=1
    #         if node.parent.banlancefactor!=0:
    #             self.updateBanlance(node.parent)
    

    def __setitem__(self, k, v):
        self.put(k,v)
    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key==key:
            return currentNode
        elif key<currentNode.key:
            self._get(key,currentNode.leftchild)
        else:
            self._get(key,currentNode.rightchild)
    def __getitem__(self,key):#特殊方法，实现mytree[0]的取值方式
        return self.get(key)
    def __contain__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
    def delete(self,key):
        if self.size>1:
            nodeToremove=self._get(key,self.root)
            if nodeToremove:
                self.remove(nodeToremove)
                self.size-=1
            else:
                raise KeyError('Error,key not in tree')
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size-=1
        else:
            raise KeyError('Error,key not in tree')
    def __delete__(self,key):
        self.delete(key)
    def remove(self,currentNode):#remove函数分为三种情况：被删除的节点没有子节点、有一个子节点、有两个子节点
        if currentNode.isleaf():#被删除的节点没有子节点
            if currentNode==currentNode.parent.leftchild:
                currentNode.parent.leftchild=None
            else:
                currentNode.parent.rightchild=None
        elif currentNode.hasbothchildren():#被删除的节点有两个子节点
            succ=currentNode.findsuccessor()#找到被删除节点右子树下的最小节点,函数为TreeNode类的内部函数
            succ.spliceout()#去掉被删除节点右子树下的最小节点，函数为TreeNode类的内部函数
            currentNode.key=succ.key#用右子树下最小节点的值替代当前节点
            currentNode.payload=succ.payload
        else:#被删除的节点有一个子节点
            if currentNode.hasleftchilid():#被删除的节点为左子节点
                if currentNode.isleftchild():#当前节点本身是左子节点
                    currentNode.leftchild.parent=currentNode.parent
                    currentNode.parent.leftchild=currentNode.leftchild
                elif currentNode.isrightchild():#当前节点本身是右子节点
                    currentNode.leftchild.parent=currentNode.parent
                    currentNode.parent.rightchild=currentNode.leftchild
                else:#当前节点本身是根节点
                    currentNode.replacenodedata(currentNode.leftchild.key,
                                                currentNode.leftchild.payload,
                                                currentNode.leftchild.leftchild,
                                                currentNode.leftchild.rightchild)
            else:#被删除的节点为右子节点
                if currentNode.isleftchild():#当前节点本身为左子节点
                    currentNode.rightchild.parent=currentNode.parent
                    currentNode.parent.leftchild=currentNode.rightchild
                elif currentNode.isrightchild():#当前节点本身为右子节点
                    currentNode.rightchild.parent=currentNode.parent
                    currentNode.parent.rightchild=currentNode.rightchild
                else:#当前节点本身为根节点
                    currentNode.replacenodedata(currentNode.rightchild.key,
                                                currentNode.rightchild.payload,
                                                currentNode.rightchild.leftchild,
                                                currentNode.rightchild.rightchild)

#创建一个节点类
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key=key
        self.payload=val
        self.leftchild=left
        self.rightchild=right
        self.parent=parent
    def hasleftchild(self):
        return self.leftchild
    def hasrightchild(self):
        return self.rightchild
    def isleftchild(self):
        return self.parent and self.parent.leftchild==self
    def isrightchild(self):
        return self.parent and self.parent.rightchild==self
    def isroot(self):
        return not self.parent
    def isleaf(self):
        return not (self.leftchild and self.rightchild)
    def hasanychild(self):
        return self.leftchild or self.rightchild
    def hasbothchildren(self):
        return self.leftchild and self.rightchild
    def replacenodedata(self,key,value,lc,rc):
        self.key=key
        self.payload=value
        self.leftchild=lc
        self.rightchild=rc
        if self.hasleftchild():
            self.leftchild.parent=self
        if self.hasrightchild():
            self.rightchild.parent=self
    def findsuccessor(self):#寻找后继节点的函数
        succ=None
        if self.hasrightchild():
            succ=self.rightchild.findmin()
        return succ
    def findmin(self):
        current=self
        while current.hasleftchild():
            current=current.leftchild
        return current
    def spliceout(self):#摘掉节点
        if self.isleaf():
            if self.isleftchild():
                self.parent.leftchild=None
            else:
                self.parent.rightchild=None
        elif self.hasanychild():
            if self.hasleftchild():
                if self.isleftchild():
                    self.parent.leftchild=self.leftchild
                else:
                    self.parent.rightchild=self.leftchild
                self.leftchild.parent=self.parent
            else:
                if self.isleftchild():
                    self.parent.leftchild=self.rightchild
                else:
                    self.parent.rightchild=self.rightchild
                self.rightchild.parent=self.parent








