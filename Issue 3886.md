# Issue 3886: Plotting of digraphs is broken

Issue created by migration from https://trac.sagemath.org/ticket/3886

Original creator: saliola

Original creation time: 2008-08-18 03:53:19

Assignee: rlm

Keywords: digraphs, graphs, graphics

See the attached images for the results of these commands (images produced by sagenb.org).


```
DiGraph({0:[1]}).show()
```



```
DiGraph({0:[1], 1:[2]}).show()
```



---

Attachment

First example.


---

Comment by saliola created at 2008-08-18 03:54:13

Second example


---

Attachment

Franco,

This is caused by/related to #3877 and #3880.


---

Comment by jason created at 2008-08-18 20:47:02

rlm: are you saying that fixing #3877 and #3880 should fix the problem?


---

Comment by rlm created at 2008-08-19 01:22:11

Fixed by the patch at #3880.


---

Comment by mabshoff created at 2008-08-19 01:50:21

Resolution: fixed


---

Comment by mabshoff created at 2008-08-19 01:50:21

Fixed by merging #3880.

Cheers,

Michael
