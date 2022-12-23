# Issue 3250: Parent does not have a cdef class default hash

Issue created by migration from https://trac.sagemath.org/ticket/3250

Original creator: gfurnish

Original creation time: 2008-05-18 02:33:23

Assignee: rlm

CC:  robertwb

Parent does has a default hash for python classes, but not for cython classes.  This leads to very subtle bugs where converting a python class to a cython class can result in coercion failing mysteriously.  Either coercion should be more descriptive with its error messages resulting from lack of a hash function or Parent should get a default cdef hash function.


---

Comment by gfurnish created at 2008-05-18 02:33:32

Changing assignee from rlm to robertwb.


---

Comment by gfurnish created at 2008-05-18 02:33:32

Changing component from coding theory to coercion.


---

Comment by robertwb created at 2008-06-12 23:44:57

Hashing/comparison is being addressed in the new coercion model.


---

Comment by mabshoff created at 2008-12-10 13:47:08

Hi Robert,

I assume this has been addressed by now? If so please close this ticket as fixed.

Cheers,

Michael


---

Comment by robertwb created at 2008-12-11 07:42:19

We didn't do as many changes to the comparison/hashing model as we had intended starting out, mainly because it just got to be too much on top of everything else... 

However, short of a specific example, this ticket is rather vague, and I have never run into this.


---

Comment by jdemeyer created at 2018-03-08 10:05:34

Resolution: invalid
