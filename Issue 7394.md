# Issue 7394: sqrt(e) causes segfaults

Issue created by migration from Trac.

Original creator: edrex

Original creation time: 2009-11-05 07:07:06

Assignee: AlexGhitza

CC:  jason

multiplying/dividing sqrt(e) with anything other than 1 causes a segfault, for example:


```
2*sqrt(e)
```


tested with source compile i686 and sagenb.org


---

Comment by mhansen created at 2009-11-05 14:58:15

Pynac gets into an infinite recursion with these lines:


```
#141 0x00007ff794d21de6 in GiNaC::ex::construct_from_basic (other=`@`0x7fff450abfe6) at ex.cpp:312
#142 0x00007ff794dc7405 in GiNaC::mul::eval (this=0x57772f0, level=<value optimized out>) at ex.h:267
```



---

Comment by AlexGhitza created at 2009-11-15 13:12:10

Changing component from algebra to symbolics.


---

Comment by AlexGhitza created at 2009-11-15 13:12:10

Changing assignee from AlexGhitza to burcin.


---

Comment by burcin created at 2009-11-22 18:02:37

This is a duplicate of #7264. The patch attached to that ticket contains this example as a doctest as well.


---

Comment by burcin created at 2009-11-22 18:02:37

Resolution: duplicate
