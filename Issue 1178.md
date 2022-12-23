# Issue 1178: flint in 2.8.12 fails on Solaris 10: u_int16_t undefined

Issue created by migration from https://trac.sagemath.org/ticket/1178

Original creator: mabshoff

Original creation time: 2007-11-15 15:51:45

Assignee: Bill Hart

Hello,

the problem was reported by Klas Heggemann. See

http://groups.google.com/group/sage-devel/t/b35f8758cd98fad6

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 20:50:11

FLINT 1.0 works on Solaris 9 when I define

```
typedef unsigned int            uint32_t;
typedef unsigned long long      u_int64_t;
```

in `stdint.h`

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-28 05:46:13

This has been fixed a while ago. So close it.


---

Comment by mabshoff created at 2008-01-28 05:46:13

Resolution: fixed
