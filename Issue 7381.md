# Issue 7381: Coercion of HyperellipticCurve over pAdicField to an extension

Issue created by migration from Trac.

Original creator: jen

Original creation time: 2009-11-03 17:54:12

Assignee: roed

CC:  jen


```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x^3-10*x+9)
sage: K = Qp(3,5)
sage: J.<a> = K.extension(x^30-3)
sage: HK = H.change_ring(K)
sage: HJ = HK.change_ring(J)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (8, 0))

[snip]

ValueError: variable names must be alphanumeric, but one is '(1 + O(3^5))*x' which is not.
```



---

Comment by mhansen created at 2009-11-04 07:27:30

Changing status from new to needs_review.


---

Attachment


---

Comment by mhansen created at 2009-12-07 08:51:41

If you look at the error, you'll see that it is expecting an
alphanumeric variable name, but got '(1 + O(3^5))*x' instead.  This
is because it is using the .gen() method and that's how the
generator prints out.  The patch changes it so that it uses the
variable_name() method instead which doesn't have the (1 + O(3^5))
part.


---

Comment by ncohen created at 2009-12-07 09:07:53

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-12-07 09:07:53

Applies fine, passes the tests.. It took me 10 times the amount of time somebody knowing this class would have needed, but it is ok :-)

Nathann


---

Comment by mhansen created at 2009-12-07 23:23:53

Resolution: fixed
