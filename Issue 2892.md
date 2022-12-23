# Issue 2892: notebook -- traceback shrinking/expanding in the notebook is broken in an obscure case

Issue created by migration from https://trac.sagemath.org/ticket/2892

Original creator: was

Original creation time: 2008-04-12 03:17:30

Assignee: boothby

I discovered this but when teaching my class.  It's best explained
with a screen shot. 

http://sage.math.washington.edu/home/was/patches/traceback_shrinking.png


---

Comment by was created at 2008-04-12 03:55:18

This patch:
  * fixes the stated bug.  To observe this try this input: 

```
try:
    1/0
finally:
    print "<html><b>hello</b></html>"
```

Note that the output has html properly formated at the top, etc.

  * also fixes a bug when the traceback output is too long.  To 
verify this, try this input and wait a few seconds.  NOte that a link
appears as it should:

```
def f(n):
    f(n)

f(5)
```


  * I'm sorry but providing doctests for this is just too hard at present, given that we don't have a good notebook testing framework just yet.  These bugs are pretty high priority imho.


---

Attachment


---

Comment by boothby created at 2008-04-12 07:27:11

works for me


---

Comment by mabshoff created at 2008-04-12 11:27:35

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-12 11:27:35

Resolution: fixed
