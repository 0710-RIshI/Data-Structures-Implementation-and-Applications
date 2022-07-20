
class Node:
    def __init__(self,y):
        self.data=y
        self.left=None
        self.right=None


    
class binarytree:
    def __init__(self):
        self.x=-1
    def buildTree(self,values):
        self.x=self.x+1
        if(values[self.x]==-1):
            return None
        
        new = Node(values[self.x])
        new.left = self.buildTree(values)
        new.right = self.buildTree(values)
    
        return new

    def preorder(self,root):
        if(root is None):
            print("-1")
        else:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)


    def inorder(self,root):
        if(root is None):
            return
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
        
    def postorder(self,root):
        if root is None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
Sign in
Operating System Tutorial
/
Process Synchronization in OS
￼
Log Into get certified and check your progress
MODULE  1
Basics of OS
MODULE  2
Memory Management in OS
MODULE  3
How does PC boot?
MODULE  4
Process Creation And System Calls
MODULE  5
Interrupts in OS
MODULE  6
CPU Scheduling in OS
MODULE  7
Synchronization in OS
Producer Consumer Problem in OS
Process Synchronization in OS
What is Process Synchronization in OS?
How Process Synchronization in OS Works?
Race Condition
What is the Critical Section Problem?
Requirements of Synchronization
Solutions To The Critical Section Problem
Conclusion
￼
Challenge
Mutex in OS
Disk Management in OS
Dining Philosophers Problem in OS
Priority Scheduling Algorithm
Deadlock Avoidance in OS
Multi-processor Scheduling
MODULE  8
Deadlocks and Threads in OS
MODULE  9
Disk Management in OS
MODULE  10
Glossary for Operating Systems
￼
CERTIFICATE
Get certified
￼
Process Synchronization in OS
Learn about process synchronization in OS.

B
Bhupender Yadav
2 Mar 2022-9 mins read
￼
Challenge Inside! : Find out where you stand! Try quiz, solve problems & win rewards!
Go to Challenge
Process Synchronization in OS
Overview
Processes Synchronization or Synchronization is the way by which processes that share the same memory space are managed in an operating system. It helps maintain the consistency of data by using variables or hardware so that only one process can make changes to the shared memory at a time. There are various solutions for the same such as semaphores, mutex locks, synchronization hardware, etc.

Scope of the Article
This article discusses Process Synchronization in Operating systems.
This also article discusses the solutions to synchronization, including Semaphores, Mutex, Synchronization Hardware, and Peterson's solution.
What is Process Synchronization in OS?
An operating system is a software that manages all applications on a device and basically helps in the smooth functioning of our computer. Because of this reason, the operating system has to perform many tasks, and sometimes simultaneously. This isn't usually a problem unless these simultaneously occurring processes use a common resource.

For example, consider a bank that stores the account balance of each customer in the same database. Now suppose you initially have x rupees in your account. Now, you take out some amount of money from your bank account, and at the same time, someone tries to look at the amount of money stored in your account. As you are taking out some money from your account, after the transaction, the total balance left will be lower than x. But, the transaction takes time, and hence the person reads x as your account balance which leads to inconsistent data. If in some way, we could make sure that only one process occurs at a time, we could ensure consistent data.

￼

In the above image, if Process1 and Process2 happen at the same time, user 2 will get the wrong account balance as Y because of Process1 being transacted when the balance is X.

Inconsistency of data can occur when various processes share a common resource in a system which is why there is a need for process synchronization in the operating system.

How Process Synchronization in OS Works?
Let us take a look at why exactly we need Process Synchronization. For example, If a process1 is trying to read the data present in a memory location while another process2 is trying to change the data present at the same location, there is a high chance that the data read by the process1 will be incorrect.

￼

Let us look at different elements/sections of a program:

Entry Section: The entry Section decides the entry of a process.
Critical Section: Critical section allows and makes sure that only one process is modifying the shared data.
Exit Section: The entry of other processes in the shared data after the execution of one process is handled by the Exit section.
Remainder Section: The remaining part of the code which is not categorized as above is contained in the Remainder section.
Race Condition
- Javatpointhttps://www.javatpoint.com › os-readers-writers-problem
The readers-writers problem is a 
        while(Flag[i] && Turn == i);
        
        { Critical Section };
        
        Flag[i] = False;
        // another process can go to Critical Section
        Turn = j;
        
            Remainder Section
            
    }  while ( True);


                j=j-1
                continue
    def ques2(self):
        self.inordertoList(root,l)def topological(AList):
    indegree = {i:0 for i in range(10)}
    path = {i:0 for i in range(10)}
    for i in AList:
        for j in AList[i]:
            indegree[j] += 1i