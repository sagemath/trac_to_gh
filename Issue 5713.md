# Issue 5713: multigraph plotting bug

Issue created by migration from https://trac.sagemath.org/ticket/5713

Original creator: was

Original creation time: 2009-04-08 16:07:40

Assignee: ekirkman

CC:  rlm


```
I just tried to plot a multigraph with setting positions of vertices,

G=Graph({'a':['a','b','b','b','e'],'b':['c','d','e'],'c':
['c','d','d','d'],'d':['e']})

G.show(pos={'a':[0,1],'b':[1,1],'c':[2,0],'d':[1,0],'e':[0,0]})

and got an error

 File "/home/alec/sage/local/lib/python2.5/site-packages/sage/graphs/
graph_plot.py", line 459, in set_edges
   odd_y = M[1] + d
NameError: global name 'd' is not defined

Without pos both show and plot work OK.

Alec Mihailovs
```



---

Comment by mabshoff created at 2009-04-09 18:44:29

Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-04-10 01:03:01

Ok, given the scope of this patch I am capable of understanding what is going on and I am giving this patch a positive review. Even all doctests pass :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-10 01:03:18

Resolution: fixed


---

Comment by mabshoff created at 2009-04-10 01:03:18

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
