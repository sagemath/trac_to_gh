# Issue 1776: symbolic function preparser bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-14 14:14:50

Assignee: was


```
sage: preparse('f(x) = x')
'_=var("x");f=symbolic_expression(x).function(x)'
sage: preparse('f(x) =+x')
'f(x) =+x'
sage: preparse('f(x) =-x')
'f(x) =-x'
```


This was found by Jason Grout, with input by Jaap Spies and John Cremona.


---

Comment by was created at 2008-01-14 14:20:08

Changing status from new to assigned.


---

Comment by was created at 2008-01-14 14:36:25

slightly better fix (there is only one post-equals symbol, namely =).  This also fixes typos and mistakes in some of the docs.


---

Attachment


```
Works for me!

----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.alpha2, Release Date: 2008-01-11                 |
| Type notebook() for the GUI, and license() for information.        |

sage: f(x)=-x

sage: f(2)
 -2


Jaap

```



---

Comment by mabshoff created at 2008-01-14 16:49:18

Resolution: fixed


---

Comment by mabshoff created at 2008-01-14 16:49:18

Merged in Sage 2.10.alpha3.
