# Issue 825: extending % to more sage types

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2007-10-04 18:42:03

Assignee: mhampton

Keywords: remainder

Currently the following gives an error:
10.23 % 2
The % should be extended to handle more types.


---

Comment by mhampton created at 2007-10-04 18:42:24

Changing status from new to assigned.


---

Comment by robertwb created at 2007-10-05 02:02:17

And probably be placed into the coercion model as well (though this will be easier once cdef overrideable is in place).


---

Comment by zimmerma created at 2007-11-16 23:24:39

The remainder of floating-point numbers can be given a sense: see the C99 remainder function, and
the corresponding mpfr_remainder in MPFR.


---

Comment by AlexGhitza created at 2009-01-23 07:07:57

Changing type from defect to enhancement.


---

Comment by zimmerma created at 2009-02-01 21:25:46

#5132 is a duplicate of that ticket.


---

Comment by mabshoff created at 2009-02-02 07:28:25

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 07:28:25

Fixed via #5132 in Sage 3.3.alpha4.

Cheers,

Michael
