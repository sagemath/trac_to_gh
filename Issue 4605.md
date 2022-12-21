# Issue 4605: Update Cython to 0.10.2 (latest stable upstream)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-24 20:49:40

Assignee: robertwb

Cython 0.10.2 fixes a important bug that resolves an issue so that #4206 can be merged.

Cheers,

Michael


---

Comment by robertwb created at 2008-11-25 22:31:55

See http://sage.math.washington.edu/home/robertwb/cython/cython-0.10.2.spkg


---

Comment by mabshoff created at 2008-11-25 22:38:22

Thanks Robert,

I am doing a full -ba followed by a full test run. The spkg itself looks good, the only thing we should add in the long term is a version change history in SPKG.txt. For now I don't care too much about that.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-25 23:17:25

I get the following failure:

```
python2.5 `which cython` --embed-positions --incref-local-binop -I/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main -o sage/rings/real_rqdf.cpp sage/rings/real_rqdf.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
cdef extern from "qd/qd_real.h":

    ctypedef struct qd "qd_real":
        # Members
        double *x
        qd _pi
          ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:21:11: Struct cannot contain itself as a member.

Error converting Pyrex file to C:
------------------------------------------------------------
...

    ctypedef struct qd "qd_real":
        # Members
        double *x
        qd _pi
        qd _log2
          ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:22:11: Struct cannot contain itself as a member.

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ctypedef struct qd "qd_real":
        # Members
        double *x
        qd _pi
        qd _log2
        qd _nan
          ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:23:11: Struct cannot contain itself as a member.
Error converting Pyrex file to C:
------------------------------------------------------------
...
    ctypedef struct qd "qd_real":
        # Members
        double *x
        qd _pi
        qd _log2
        qd _nan
          ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:23:11: Struct cannot contain itself as a member.

Error converting Pyrex file to C:
------------------------------------------------------------
...
        # Members
        double *x
        qd _pi
        qd _log2
        qd _nan
        qd _e
          ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:24:11: Struct cannot contain itself as a member.

Error converting Pyrex file to C:


Error running command, exited with status 256.
sage: There was an error installing modified sage library code.  

```


Cheers,

Michael


---

Comment by mabshoff created at 2008-11-25 23:25:46

I am actually surprised that the issue pops up with a stable release :p

Cheers,

Michael


---

Comment by robertwb created at 2008-11-25 23:53:09

This was to catch a gcc compiler error. Surely that typedef is wrong...


---

Comment by mabshoff created at 2008-11-26 00:04:25

Replying to [comment:5 robertwb]:
> This was to catch a gcc compiler error. Surely that typedef is wrong...

Wasn't this the "recursive" definition issue the other day on the Cython-dev list?

Cheers,

Michael


---

Comment by robertwb created at 2008-11-26 00:06:28

Yes. A struct can contain a pointer to itself (which was the error on cython-devel), but it can't actually contain itself. Before gcc would choke on such a definition.


---

Comment by robertwb created at 2008-11-26 00:32:44

Oh, it's a C++ class pretending to be a struct. 

I had thought it was safe because it moved a gcc compile error into a Cython compile error, but of course extern declarations don't actually get produced and may (as in this case) be fake structs. I'll fix this. 

A new spkg is up, though as before my own sage -ba is still in progress.


---

Comment by mabshoff created at 2008-11-26 01:16:12

Replying to [comment:8 robertwb]:
> Oh, it's a C++ class pretending to be a struct. 
> 
> I had thought it was safe because it moved a gcc compile error into a Cython compile error, but of course extern declarations don't actually get produced and may (as in this case) be fake structs. I'll fix this. 

Cool.

> A new spkg is up, though as before my own sage -ba is still in progress. 

Using eight CPUs I got passed the Cython phase, so things should be loooking good. If the tests pass this will turn into a positive revivew.

Cheers,

Michael


---

Comment by robertwb created at 2008-11-26 01:44:43

Thanks. Sage -ba just succeeded on my machine too.


---

Comment by mabshoff created at 2008-11-26 01:46:30

Positive review, but I am running doctests to be 100% certain. Thanks for the quick fix.

Cheers,

Michael


---

Comment by robertwb created at 2008-11-26 01:51:34

Thanks for the quick review and bug catch :).


---

Comment by mabshoff created at 2008-11-26 07:14:43

Resolution: fixed


---

Comment by mabshoff created at 2008-11-26 07:14:43

Merged in Sage 3.2.1.alpha1


---

Comment by jason created at 2008-11-26 16:49:13

Thanks for getting this in!
