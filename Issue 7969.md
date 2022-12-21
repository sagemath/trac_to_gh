# Issue 7969: escaped backslash at end of line in notebook

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2010-01-17 21:21:38

Assignee: was

The following input in the notebook produces the wrong output:


```
%python
2+2
print """\
a\\
n
c
"""
```


It should return


```
a\
n
c
```


but instead prints


```
a

c
```



---

Comment by wjp created at 2010-01-17 21:22:28

Changing assignee from was to timdumol.


---

Attachment

Prevents end-of-line backslashse from being replaced in sage and python systems.


---

Comment by timdumol created at 2010-01-19 09:01:10

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-19 11:54:49

Fixes the example above and a few others I've tried.  SageNB doctests pass.


---

Comment by mpatel created at 2010-01-19 11:54:49

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-25 00:51:22

Resolution: fixed
