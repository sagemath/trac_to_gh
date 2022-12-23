# Issue 451: flintqs Solaris build fixes

Issue created by migration from https://trac.sagemath.org/ticket/451

Original creator: mabshoff

Original creation time: 2007-08-19 07:55:51

Assignee: mabshoff

flintqs-20070505 uses linux-ism for types. In lanzos.h add

#ifdef __sun
#define u_int32_t unsigned int
#define u_int64_t unsigned long long
#endif 


---

Comment by mabshoff created at 2007-08-22 19:38:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-04 11:51:45

This has been fixed upstream by Bill some time before Sage 2.8.3

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-04 11:51:45

Resolution: fixed
