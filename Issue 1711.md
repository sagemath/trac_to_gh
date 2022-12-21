# Issue 1711: SIGSEGV in PolyBoRi

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-07 13:30:53

Assignee: burcin

Keywords: sigsegv

How to reproduce:


```
sage: P.<a,b,c> = BooleanPolynomialRing(3,order='degrevlex')
sage: list(a.set())
```


Backtrace:


```
#0  0x00002b62d02c9277 in std::deque<polybori::CCuddNavigator, std::allocator<polybori::CCuddNavigator> >::operator= (this=0x3073ba8, __x=`@`0x7fffedfa4268) at /usr/include/c++/4.2/bits/stl_algobase.h:283
#1  0x00002b62d02ab7f8 in __pyx_pf_4sage_5rings_10polynomial_5pbori_8BooleSet___iter__ (__pyx_v_self=0x30d08d0) at /home/malb/SAGE/local/include/polybori/CTermStack.h:196
#2  0x000000000041914f in PyObject_GetIter (o=0x30d08d0) at Objects/abstract.c:2350
#3  0x00000000004382a5 in listextend (self=0x30d95f0, b=0x7fffedfa4268) at Objects/listobject.c:776
#4  0x0000000000438837 in list_init (self=0x30d95f0, args=<value optimized out>, kw=<value optimized out>) at Objects/listobject.c:2372
#5  0x000000000045cbd1 in type_call (type=0x721d60, args=0x30d0ed0, kwds=0x0) at Objects/typeobject.c:436
#6  0x0000000000417bb3 in PyObject_Call (func=0xffffffffffffffc0, arg=0x7fffedfa4268, kw=0x3218e00) at Objects/abstract.c:1860
...
```



---

Comment by mabshoff created at 2008-01-19 20:13:04

This is still a problem in Sage 2.10.


---

Comment by burcin created at 2008-01-20 10:15:54

Changing status from new to assigned.


---

Comment by burcin created at 2008-01-20 10:15:54

I'll look at this in more detail as part of an effort to make the iterators for the polybori wrapper look more uniform. 

For now, I cannot figure out why this specific iterator fails, and the others don't.


---

Attachment

workaround the crash by using BooleanPolynomial iterators


---

Comment by burcin created at 2008-03-07 10:13:39

attachment:1711_BooleSet_iterator_workaround.patch does not really fix the issue, but at least prevents the segfault.

I think the patch should be applied before 2.10.3, and this ticket still kept open so we remember the problem.


---

Comment by mhansen created at 2008-03-07 10:47:39

Works for me in rc2.


---

Comment by mabshoff created at 2008-03-07 15:01:22

Resolution: fixed


---

Comment by mabshoff created at 2008-03-07 15:01:22

Merged in Sage 2.10.3.rc3
