# Issue 3068: empty matrices: smith_form() throws a RuntimeError

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-04-30 15:25:30

Assignee: was


```
sage: m = matrix([])
sage: m.smith_form()
<type 'exceptions.RuntimeError'>:
```



---

Comment by dfdeshom created at 2008-08-27 18:21:39

This seems to be gone as of 3.1.1. Could someone close this?

```
sage: m = matrix([])
sage: m.smith_form()
 ([], [], [])
```



---

Comment by davidloeffler created at 2008-12-08 18:03:59

In 3.2.2.alpha0 this works fine as long as the matrix has 0 rows and 0 columns, but for 0 rows and a nonzero number of columns (or vice versa) we still get the error. This arises from the fact that Pari doesn't have the notion of a matrix with 0 rows and 1 column, so the matrix gets "truncated" (!) before being passed to Pari.

I will fix this as part of #4681.


---

Comment by davidloeffler created at 2008-12-08 18:03:59

Resolution: fixed


---

Comment by mabshoff created at 2008-12-08 18:08:51

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-12-08 18:08:51

Hi David,

usually the release manager does the closing of a ticket once the fix has been merged. Until then it stays open.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-08 18:08:51

Changing status from closed to reopened.


---

Comment by davidloeffler created at 2008-12-08 18:18:38

I'm sorry for overstepping my authority. Anyway, the fix is now up at #4681.


---

Comment by mabshoff created at 2008-12-08 18:19:47

Replying to [comment:4 davidloeffler]:
> I'm sorry for overstepping my authority. Anyway, the fix is now up at #4681.

Don't worry about it because it is one of those unwritten rules :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-10 11:27:53

Resolution: fixed


---

Comment by mabshoff created at 2008-12-10 11:27:53

Fixed in Sage 3.2.2.alpha1 via #4681.

Cheers,

Michael
