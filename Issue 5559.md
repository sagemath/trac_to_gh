# Issue 5559: roots issue on fedora core 32-bit

Issue created by migration from https://trac.sagemath.org/ticket/5559

Original creator: was

Original creation time: 2009-03-18 14:26:39

Assignee: mabshoff

CC:  cwitty


```
>> x86-Linux-fc (cicero)
>>
>> The following tests failed:
>>
>>        sage -t  "devel/sage/sage/rings/polynomial/complex_roots.py"
>
> Could you send the output of this test failing?

sage -t  "devel/sage/sage/rings/polynomial/complex_roots.py"
**********************************************************************
File "/home/mariah/sage/sage-3.4-x86-Linux-fc/devel/sage/sage/rings/polynomial/c
omplex_roots.py", line 271:
   sage: complex_roots(x^2 + 27*x + 181)
Expected:
   [(-14.61803398874990?..., 1), (-12.3819660112501...? + 0.?e-27*I, 1)]
Got:
   [(-12.3819660112501?, 1), (-14.61803398874990? + 0.?e-27*I, 1)]
**********************************************************************
1 items had failures:
```



---

Comment by mabshoff created at 2009-04-01 02:00:05

This is "only" a problem with gcc 4.3.3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 18:32:41

This is a 3.4.1 blocker if there ever was one :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 21:26:21

After chatting to cwitty about this problem a couple weeks ago: we can just use another polynomial since the specific choice is irrelevant. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 01:06:51

Resolution: duplicate


---

Comment by mabshoff created at 2009-04-18 01:06:51

This is a dupe of #5378.

Cheers,

Michael
