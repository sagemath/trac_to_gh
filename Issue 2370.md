# Issue 2370: unable to coerce bool types to Sage integers

Issue created by migration from https://trac.sagemath.org/ticket/2370

Original creator: TimothyClemans

Original creation time: 2008-03-02 20:13:20

Assignee: somebody

sage: ZZ(True)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/tclemans/<ipython console> in <module>()

/home/tclemans/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: unable to coerce element to an integer
sage: ZZ(False)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/tclemans/<ipython console> in <module>()

/home/tclemans/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: unable to coerce element to an integer

--------------------------------------------
Able to coerce bool types to Python integers
--------------------------------------------

sage: int(True)
1
sage: int(False)
0


---

Comment by dfdeshom created at 2008-03-03 16:04:37

Changing assignee from somebody to dfdeshom.


---

Comment by dfdeshom created at 2008-03-03 16:04:37

Added a small patch that check for bool types


---

Comment by mabshoff created at 2008-03-05 06:10:23

The patch looks correct, but integer.pyx could certainly use some doctests. So somebody should at least add Timothy's trivial test case to the docstrings.

Cheers,

Michael


---

Attachment

Replying to [comment:2 mabshoff]:
> The patch looks correct, but integer.pyx could certainly use some doctests.  

Done.


---

Comment by mabshoff created at 2008-03-05 06:27:36

Merged in Sage 2.10.3.rc2


---

Comment by mabshoff created at 2008-03-05 06:27:36

Resolution: fixed
