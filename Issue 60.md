# Issue 60: notebook cuts output of latex view

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2006-09-14 15:15:34

Assignee: somebody

Keywords: notebook, latex

This may be related to ticket #38.

Enter

f = maxima("%e<sup>(k*x)+sin(b*x)+x</sup>3")

g = f.diff("x")

view(f)

view(g)

into a cell and hit "shift-enter". Only the latexed
display of g is shown.


---

Comment by boothby created at 2006-09-14 18:48:28

Currently, view() calls typeset() if EMBEDDED_MODE is True.  typeset() merely returns a string -- so if you want to see both f and g, 


```
    f = maxima("%e(k*x)+sin(b*x)+x3")
    g = f.diff("x")
    print view(f)
    print view(g)
```


Perhaps view() should print?


---

Comment by boothby created at 2006-09-14 18:48:28

Changing type from defect to enhancement.


---

Comment by boothby created at 2006-09-14 18:48:28

Changing priority from major to trivial.


---

Comment by was created at 2006-09-15 18:10:02

I definitely consider this a bug.


---

Comment by was created at 2006-10-15 17:49:21

Fixed.  Changed start of view function in sage/misc/latex.py to the following:

```
    if EMBEDDED_MODE:
        print typeset(objects)
        return 
```



---

Comment by was created at 2006-10-15 17:49:21

Resolution: fixed
