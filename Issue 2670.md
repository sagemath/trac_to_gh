# Issue 2670: matrix cmp expr should return a matrix with True/False entries from mapping the test to the entries

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-25 22:27:36

Assignee: mabshoff

See the numpy where() command or the matlab find() command:

http://www.scipy.org/NumPy_for_Matlab_Users

so:


```
sage: m=matrix([[1,2,],[3,4]])
sage: m>2
*returns matrix([[False,True],[True,True]])
```




---

Comment by jason created at 2008-03-25 22:28:09

uh, the return above should be `matrix([[False, False], [True, True]])`, of course!


---

Comment by dfdeshom created at 2008-03-26 18:28:02

Changing assignee from mabshoff to was.


---

Comment by dfdeshom created at 2008-03-26 18:28:02

Do we want to mess with python's semantics for `__cmp__` here? I would rather not take that route and instead define a custom operator (like (`.>`)) to indicate element-wise comparison. 

Actually, there has been a thread related to element-wise operations on matrices in sage whichc could be part of a larger ticket.


---

Comment by dfdeshom created at 2008-03-26 18:28:02

Changing component from Cygwin to linear algebra.


---

Comment by jason created at 2008-03-31 19:14:15

Changing the original proposal, how about adding a find() method of a matrix that takes a boolean test and applies the boolean function to the entries of the matrix.

So in the above example,


```
sage: m=matrix([[1,2,],[3,4]])
sage: m.find(lambda x:x>2)
*returns matrix([[False,False],[True,True]])
```



---

Attachment

A patch is up. Turns out you cannot create a matrix with True and False entries, so I returned one with entries in GF(2).


---

Comment by mhansen created at 2008-04-04 21:39:34

Looks good to me.


---

Comment by mabshoff created at 2008-04-04 21:56:41

Resolution: fixed


---

Comment by mabshoff created at 2008-04-04 21:56:41

Merged in Sage 3.0.alpha1
