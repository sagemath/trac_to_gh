# Issue 1712: SIGSEGV in PolyBoRi's cmp

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-07 13:40:35

Assignee: burcin

CC:  robertwb

Keywords: sigsegv

How to reproduce:


```
sage: sage: P.<a,b,c> = BooleanPolynomialRing(3,order='degrevlex')
sage: sage: R.<a,b,c> = BooleanPolynomialRing(3,order='degrevlex')
sage: sage: P("a") == R("a")
```


Backtrace:


```
#0  0x00002b208e6ef457 in ?? () from /lib/libc.so.6
#1  0x00002b208e6f12a0 in malloc () from /lib/libc.so.6
#2  0x00002b208ffcb1ed in operator new () from /usr/lib/libstdc++.so.6
#3  0x00002b20a166397c in std::_Deque_base<polybori::CCuddNavigator, std::allocator<polybori::CCuddNavigator> >::_M_create_nodes () from /home/malb/SAGE/local/lib/libpolybori.so
#4  0x00002b20a1663a68 in std::_Deque_base<polybori::CCuddNavigator, std::allocator<polybori::CCuddNavigator> >::_M_initialize_map () from /home/malb/SAGE/local/lib/libpolybori.so
#5  0x00002b20a168644b in polybori::CDegTermStack<polybori::CCuddNavigator, polybori::invalid_tag, polybori::invalid_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> >::findTerm ()
   from /home/malb/SAGE/local/lib/libpolybori.so
#6  0x00002b20a1687270 in polybori::CDegTermStack<polybori::CCuddNavigator, polybori::invalid_tag, polybori::invalid_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> >::increment ()
   from /home/malb/SAGE/local/lib/libpolybori.so
#7  0x00002b20a166bb88 in polybori::dd_print_terms<polybori::COrderedIter<polybori::CCuddNavigator, polybori::BooleExponent>, polybori::variable_name<polybori::OrderedManagerBase<polybori::CCuddInterface>, int, char const*>, polybori::CStringLiteral<3u>, polybori::CStringLiteral<4u>, polybori::integral_constant<unsigned int, 1u, unsigned int>, std::ostream> ()
   from /home/malb/SAGE/local/lib/libpolybori.so
#8  0x00002b20a1662ea1 in polybori::BoolePolynomial::print ()
   from /home/malb/SAGE/local/lib/libpolybori.so
#9  0x00002b20a13811eb in _to_PyString<polybori::BoolePolynomial> (x=0x2b208dc4b7a0)
    at /home/malb/SAGE/local//include/csage/ccobject.h:87
#10 0x00002b20a1373b14 in __pyx_pf_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial__repr_ (
    __pyx_v_self=0x2b208dc4b780, unused=<value optimized out>)
    at sage/rings/polynomial/pbori.cpp:10639
#11 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)
    at Objects/abstract.c:1860
#12 0x00000000004801d2 in PyEval_CallObjectWithKeywords (func=0x30d1cf8, arg=0x2b208dbda050,
    kw=0x0) at Python/ceval.c:3433
#13 0x00002b209293dc8d in __pyx_pf_4sage_9structure_11sage_object_10SageObject___repr__ (
    __pyx_v_self=0x2b208dc4b780) at sage/structure/sage_object.c:723
#14 0x0000000000446042 in _PyObject_Str (v=0x2b208e9d49c0) at Objects/object.c:406
#15 0x00000000004460eb in PyObject_Str (v=0x2b208e9d49c0) at Objects/object.c:426
#16 0x0000000000450f9d in string_new (type=0x726580, args=<value optimized out>,
    kwds=<value optimized out>) at Objects/stringobject.c:3892
#17 0x000000000045cb23 in type_call (type=0x2b208e9d49c0, args=0x33f0e50, kwds=0x0)
    at Objects/typeobject.c:422
#18 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)
    at Objects/abstract.c:1860
#19 0x00000000004801d2 in PyEval_CallObjectWithKeywords (func=0x726580, arg=0x33f0e50, kw=0x0)
    at Python/ceval.c:3433
#20 0x000000000047dd3e in builtin_map (self=<value optimized out>, args=<value optimized out>)
    at Python/bltinmodule.c:948
#21 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)
    at Objects/abstract.c:1860
#22 0x00000000004801d2 in PyEval_CallObjectWithKeywords (func=0x2b208dbe6e18, arg=0x1cd2ef0,
    kw=0x0) at Python/ceval.c:3433
#23 0x00002b20a1358535 in __pyx_f_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing__cmp_c_impl (__pyx_v_left=0x2f12d50, __pyx_v_right=0x2f12b50) at sage/rings/polynomial/pbori.cpp:7016
#24 0x00002b2094a9de21 in __pyx_f_4sage_9structure_6parent_6Parent__richcmp (
    __pyx_v_left=0x2f12d50, __pyx_v_right=0x2f12b50, __pyx_v_op=2) at sage/structure/parent.c:5349
#25 0x00002b20a1351725 in __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___richcmp__ (__pyx_v_left=0x2b208e9d49c0, __pyx_v_right=0x200, __pyx_v_op=-1902293984)
    at sage/rings/polynomial/pbori.cpp:6941
---Type <return> to continue, or q <return> to quit---
#26 0x0000000000446cb8 in PyObject_RichCompare (v=0x2f12d50, w=0x2f12b50, op=2)
    at Objects/object.c:905
#27 0x00002b2094aa474b in __pyx_f_4sage_9structure_6parent_6Parent__coerce_c (
    __pyx_v_self=0x2f12b50, __pyx_v_x=0x30f6780) at sage/structure/parent.c:3624
#28 0x00002b20a136e6da in __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___call__ (__pyx_v_self=0x2f12b50, __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)
    at sage/rings/polynomial/pbori.cpp:5652
#29 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)
    at Objects/abstract.c:1860
#30 0x00000000004801d2 in PyEval_CallObjectWithKeywords (func=0x2f12b50, arg=0x33f0e10, kw=0x0)
    at Python/ceval.c:3433
#31 0x00002b2094aa49a7 in __pyx_f_4sage_9structure_6parent_6Parent__coerce_c (
    __pyx_v_self=0x2f12b50, __pyx_v_x=0x30f6780) at sage/structure/parent.c:3639
#32 0x00002b20a136e6da in __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___call__ (__pyx_v_self=0x2f12b50, __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)
    at sage/rings/polynomial/pbori.cpp:5652
#33 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)
    at Objects/abstract.c:1860
#34 0x00000000004801d2 in PyEval_CallObjectWithKeywords (func=0x2f12b50, arg=0x33f0dd0, kw=0x0)
    at Python/ceval.c:3433
#35 0x00002b2094aa49a7 in __pyx_f_4sage_9structure_6parent_6Parent__coerce_c (
    __pyx_v_self=0x2f12b50, __pyx_v_x=0x30f6780) at sage/structure/parent.c:3639
#36 0x00002b20a136e6da in __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___call__ (__pyx_v_self=0x2f12b50, __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)
    at sage/rings/polynomial/pbori.cpp:5652
#37 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)
    at Objects/abstract.c:1860
```



---

Comment by burcin created at 2008-01-11 10:30:33

fix logic error in coercion


---

Comment by burcin created at 2008-01-11 10:41:11

Changing component from commutative algebra to coercion.


---

Comment by burcin created at 2008-01-11 10:41:11

Changing status from new to assigned.


---

Attachment

As of 2.9.10.alpha0, `BooleanPolynomialRing` doesn't support coercion from strings. Approximating the test case with


```
P(a) == R(a)
```


gives a similar error. The real culprit is here:


```
P(a)
```


When trying to coerce an element from a ring that compares equal to self, the coercion model goes into an infinite recursion, because of the following lines  in `sage/structure/parent.pyx` (starting from line 349)


```
cdef _coerce_c(self, x):          # DO NOT OVERRIDE THIS (call it)
    try:
        P = x.parent()   # todo -- optimize
        if P is self:
            return x
        elif P == self:      # canonically isomorphic parents in same category.
            return self(x)   

```


If `x` has a "canonically isomorphic parent", then the coerce function of `self` should handle the conversion, which is called by the code that follows the segment above. Calling `self(x)` leads to `self.__call__` trying `self._coerce_c`, which results in the infinite recursion.

attachment:trac_1712.patch removes the offending lines, fixing the error. All tests pass after the patch.


---

Attachment

add testcase to BooleanPolynomialRing._coerce_c_impl to catch this error


---

Comment by robertwb created at 2008-01-11 18:01:58

OK, I see the problem and the solution is good. Will keep this in mind for the coercion re-write.


---

Comment by mabshoff created at 2008-01-11 19:25:12

I merged both patches in Sage 2.10.alpha2


---

Comment by mabshoff created at 2008-01-11 19:25:12

Resolution: fixed
