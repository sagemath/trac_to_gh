# Issue 5690: Update MPIR to 1.0.0.rc7 (latest upstream)

Issue created by migration from https://trac.sagemath.org/ticket/5690

Original creator: mabshoff

Original creation time: 2009-04-06 02:34:20

Assignee: mabshoff

Spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc1/gmp-mpir-1.0.rc7.spkg

Cheers,

Michael


---

Comment by was created at 2009-04-06 02:44:45

Put in quotes: `"$SAGE_LOCAL"`

```
    rm -f $SAGE_LOCAL/include/mpir*.h $SAGE_LOCAL/include/gmp*.h
    rm -f $SAGE_LOCAL/lib/libmpir* $SAGE_LOCAL/lib/libgmp*
```



---

Comment by mabshoff created at 2009-04-06 02:48:36

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-06 02:50:58

Resolution: fixed


---

Comment by mabshoff created at 2009-04-06 02:50:58

Merged in Sage 3.4.1.rc1.

Cheers,

Michael
