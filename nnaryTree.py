class Node:
    def __init__(self,data):
        self.data=data
        self.child=[]

def newNode(key):
    temp = Node(key)
    return temp

class nnary:
    def __init__(self):
        self.maxi=0
    def findmaxsum(self,root,sum):

        if len(root.child)==0:
            self.maxi=max(self.maxi,sum)
            
        else:

            for i in range(len(root.child)):
                self.findmaxsum(root.child[i],sum + root.child[i].data)
        
        return self.maxi

root = newNode(1)
(root.child).append(newNode(2))
(root.child).append(newNode(3))
(root.child[0].child).append(newNode(4))
(root.child[1].child).append(newNode(6))
(root.child[0].child).append(newNode(5))
(root.child[1]).child.append(newNode(7))
(root.child[1].child).append(newNode(8))

n = nnary()
print(n.findmaxsum(root,root.data))
