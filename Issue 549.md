# Issue 549: print statement doesn't leave blank line in notebook

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-09-01 02:18:33

Assignee: boothby

In the notebook, the following code:


```
print "abc"
print
print "def"
```


displays


```
abc
def
```


instead of


```
abc

def
```




---

Comment by mabshoff created at 2007-09-05 16:59:21

This might be Bug Day 2 material, otherwise we will retag it for 2.9.x.

Cheers,

Michael


---

Comment by boothby created at 2007-09-06 18:25:56

Fixed by patch:

[http://128.208.160.195/home/boothby/notebook549.hg](http://128.208.160.195/home/boothby/notebook549.hg)


---

Comment by was created at 2007-09-06 19:03:45

This is fixed -- but it caused #601.


---

Comment by was created at 2007-09-06 19:03:45

Resolution: fixed
