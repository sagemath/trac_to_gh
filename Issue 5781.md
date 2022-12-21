# Issue 5781: [with patch, need review] The empty standard tableau exists ! :-)

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-04-13 22:03:38

Assignee: hivert

CC:  sage-combinat

Keywords: tableau

Before my patch:

```
sage: [] in StandardTableaux()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/averell/.sage/temp/tomahawk/19026/_home_averell__sage_init_sage_0.py in <module>()

/usr/local/sage/sage/local/lib/python2.5/site-packages/sage/combinat/tableau.pyc in __contains__(self, x)
   1740             fillings += row
   1741         fillings.sort()
-> 1742         if fillings != range(1, max(fillings)+1):
   1743             return False
   1744

ValueError: max() arg is an empty sequence
```


Now:

```
sage: [] in StandardTableaux()
True
```


Florent, the specialist of the empty objects !!!



---

Attachment


---

Comment by hivert created at 2009-04-13 22:33:15

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-13 23:22:23

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 23:22:23

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
