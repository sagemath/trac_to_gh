# Issue 3797: [with patch, needs review] several improvements to graph generation

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-08-09 22:25:31

Assignee: rlm

CC:  ekirkman

This patch:

1. Fixes a bug in sparse6 strings for n=0.
2. Implements generation of graphs with loops.
3. Implements generation of graphs with specified degree sequence.

The last two have been verified to some extent using Sloane's tables. It's all in the documentation.


---

Attachment


---

Comment by rlm created at 2008-08-10 03:19:12

Depends on #3789.


---

Attachment


---

Comment by ncalexan created at 2008-08-10 06:04:53

From the submission:


```
This patch:

   1. Fixes a bug in sparse6 strings for n=0.
```


I think this bugfix looks good.


```
   2. Implements generation of graphs with loops.
```


This looks good -- I can't guarantee that it works, but it looks fine.


```
   3. Implements generation of graphs with specified degree sequence.
```


It's not clear what degree sequence means.  I can derive it from the code, but maybe change

```
 	241	        deg_seq -- a sequence of degrees for the graph to have. If specified, 
 	242	            augment, property and size are all ignored. 
```

to something like

```
 	241	        deg_seq -- a sequence of non-negative integers.  The degrees of the vertices of the generated graph will be the specified integers, in some order.  If specified, 
 	242	            augment, property and size are all ignored. 
```


Is that even clearer?


---

Attachment

Looks good!


---

Comment by mabshoff created at 2008-08-10 06:53:45

Merged all three patches in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-10 06:53:45

Resolution: fixed
