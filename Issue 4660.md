# Issue 4660: mark  inline fortran and inline cython examples optional

Issue created by migration from https://trac.sagemath.org/ticket/4660

Original creator: was

Original creation time: 2008-11-30 07:54:45

Assignee: mabshoff

Since gcc and fortran compilers are both optional to run sage, mark doctests that use them 

```
  # optional -- gcc
```

and

```
  # optional -- fortran
```



---

Attachment


---

Comment by mabshoff created at 2008-11-30 08:24:01

Merged in Sage 3.2.1.rc1


---

Comment by mabshoff created at 2008-11-30 08:24:01

Resolution: fixed


---

Comment by mabshoff created at 2008-11-30 08:26:08

Oops, forgot the positive review.

Cheers,

Michael
