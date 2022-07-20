
class Node:
    def __init__(self,y):
        self.info=y
        self.left=None
        self.right=None


class binarySearchtree:
    
    def buildTree(self,root,element):
        if root is None:
            root=Node(element)
            return root
            
        if root.info > element:
            root.left = self.buildTree(root.left,element)
        else:
            root.right = self.buildTree(root.right,element)
        return root
    
    def inorder(self,root):
        if root is None:
            return 0
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right) 

    def lca(self,root, v1, v2):
        if(v1>root.info and v2<root.info) or (v1<root.info and v2>root.info):
            return root
        elif v1>root.info and v2>root.info:
            self.lca(root.right,v1,v2)
        elif v1<root.info and v2<root.info:
            self.lca(root.left,v1,v2)  

    def inordertoList(self,root,l):

        if root is None:
            return 
        else:
            self.inordertoList(root.left,l)
            l.append(root.data)
            self.inordertoList(root.right,l)

    def ques2(self):
        self.inordertoList(root,l)

        i=0
        while(i<len(l)):
            print(l[i+1],end='\t')
            print(l[i],end='\t')
            i=i+2

    def search(self,root,key):
        value=0
        if root==None:
            return 0
        if key>root.data:
            value=self.search(root.right,key)
        elif key<root.data:
            value=self.search(root.left,key)
        else:
            value=1
        return value
    
    def delete(self,root,value):
        if value > root.data:
            root.right=self.delete(root.right,value)
        elif value < root.data:
            root.left=self.delete(root.left,value)
        else:
            if(root.left==None and root.right==None):
                return None
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                i=self.inordsuc(root.right)
                root.data=i.data
                self.delete(root.right,i.data)  
        return root

    def inordsuc(self,root):
        while root.left != None:
            root=root.left
        return root

    def noofnodes(self,root):
        if root is None:
            return 0
        else:
            l=self.noofnodes(root.left)
            r=self.noofnodes(root.right)
            return l+r+1

    def flatten(self,root):
        count = self.noofnodes(root)
        i=0

        s1=[]
        s2=[]

        root1,root2,curr1,curr2,head,temp=root,root,None,None,None,None
        while(i<((count//2)+1)):
            while(root1):
                s1.append(root1.data)
                root1=root1.left
            
            curr1=s1.top()
            s1.pop()
            root1=curr1.right
            
            while(root2):
                s2.append(root2.data)
                root2=root2.right
            
            curr2=s2.top()
            s2.pop()
            root2=curr2.left

            if curr1.data==curr2.data:
                temp.right=curr1
                temp=temp.right
                break

            if head is None:
                head=curr1
                temp=curr1

                temp.right=curr2
                temp=temp.right
            else:
                temp.right=curr1
                temp=temp.right

                temp.right=curr2
                temp=temp.right

    







           

def check(root,l,u):
    if root.data>=l and root.data<=u:
        return root.data
    else:
        return 0


values=[1,2,3,4,5,6]
b = binarySearchtree()
root=Node(0)
for i in range(len(values)):
    root=b.buildTree(root,values[i])















