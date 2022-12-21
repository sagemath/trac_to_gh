# Issue 2857: numerical_approx for matrices

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2008-04-08 17:54:48

Assignee: was

I'm running into problems with coercing to complexes or reals in
matrices:

 sage: d = matrix([[3, 0],[0,sqrt(2)]])
 sage: b = matrix([[1, -1], [2, 2]])
 sage: e = b * d * b.inverse(); e

 [    1/sqrt(2) + 3/2 3/4 - 1/(2*sqrt(2))]
 [        3 - sqrt(2)     1/sqrt(2) + 3/2]

and when I try to run n() on the matrix e, I get:

 sage: e.n()  # or n(e)
 [snip]
 <type 'exceptions.TypeError'>: unable to coerce to a [ComplexNumber](ComplexNumber)



If you take a look at the source code for n(), you'll see that the first thing that it does is to try calling numerical_approx(prec) on the object, and then tries coercing to real or complex fields.  So the solution is to write a method numerical_approx(prec) in the matrix base class that tries to numerically approximate the entries and make a new matrix out of them.


---

Attachment


---

Comment by dfdeshom created at 2008-04-13 19:14:40

Patch attached. The functionality was already there (in `change_ring()` and this wrapper around it works fairly well.


---

Attachment

Looks good to me.

Apply 2857.2.patch after #1763


---

Comment by mabshoff created at 2008-04-15 00:28:51

Resolution: fixed


---

Comment by mabshoff created at 2008-04-15 00:28:51

Merged in Sage 3.0.alpha5
