# Issue 5836: Make show() immediately show an image in the notebook

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-04-20 18:30:27

Assignee: was

CC:  was

The patch makes the cell containing:

```
show(plot(x^2, (x, -2,2)))
print "hi"
```

display the plot before printing "hi".  This makes it much easier to construct nice-looking output.

William should get author credit on this one as well as me, since he showed how it could be done in a demo.


---

Comment by jason created at 2009-04-20 18:31:19

Well, unless William wants to review it.

In a sense, I reviewed his demo; I suppose he could review the actual patch.

A note about the patch: sage.misc.misc was imported twice in plot.py.  I changed one of those imports to import the html function.


---

Comment by was created at 2009-04-20 18:38:50

Despite rumors to the contrary, there are several hundred doctests in the notebook directory, and your new code breaks two in cell.py, so post a patch that fixes those doctest breaks:


```
sage -t  devel/sage/sage/server/notebook/cell.py
**********************************************************************
File "/Users/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/server/notebook/cell.py", line 1751:
    sage: W.check_comp(wait=9999)
Expected:
    ('d', Cell 0; in=plot(sin(x),0,5), out=
    <BLANKLINE>
    )
Got:
    ('d', Cell 0; in=plot(sin(x),0,5), out=
    <html><font color='black'><img src='cell://sage0.png'></font></html>
    <BLANKLINE>
    )
**********************************************************************
File "/Users/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/server/notebook/cell.py", line 1777:
    sage: W.check_comp(wait=9999)
Expected:
    ('d', Cell 0; in=plot(sin(x),0,5), out=
    <BLANKLINE>
    )
Got:
    ('d', Cell 0; in=plot(sin(x),0,5), out=
    <html><font color='black'><img src='cell://sage0.png'></font></html>
    <BLANKLINE>
    )
**********************************************************************
2 items had failures:
   1 of  10 in __main__.example_80

```



---

Attachment

Patch redone to correct the doctests.


---

Comment by mabshoff created at 2009-04-24 07:19:27

Resolution: fixed


---

Comment by mabshoff created at 2009-04-24 07:19:27

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael
