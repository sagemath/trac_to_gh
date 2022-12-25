# Issue 1712: [with patch, positive review] logic error in coercion

archive/issues_001712.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @robertwb\n\nKeywords: sigsegv\n\nHow to reproduce:\n\n```\nsage: P.<a,b,c> = BooleanPolynomialRing(3,order='degrevlex')\nsage: R.<a,b,c> = BooleanPolynomialRing(3,order='degrevlex')\nsage: P(\"a\") == R(\"a\")\n```\n\nBacktrace:\n\n```\n#0  0x00002b208e6ef457 in ?? () from /lib/libc.so.6\n#1  0x00002b208e6f12a0 in malloc () from /lib/libc.so.6\n#2  0x00002b208ffcb1ed in operator new () from /usr/lib/libstdc++.so.6\n#3  0x00002b20a166397c in std::_Deque_base<polybori::CCuddNavigator, std::allocator<polybori::CCuddNavigator> >::_M_create_nodes () from /home/malb/SAGE/local/lib/libpolybori.so\n#4  0x00002b20a1663a68 in std::_Deque_base<polybori::CCuddNavigator, std::allocator<polybori::CCuddNavigator> >::_M_initialize_map () from /home/malb/SAGE/local/lib/libpolybori.so\n#5  0x00002b20a168644b in polybori::CDegTermStack<polybori::CCuddNavigator, polybori::invalid_tag, polybori::invalid_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> >::findTerm ()\n   from /home/malb/SAGE/local/lib/libpolybori.so\n#6  0x00002b20a1687270 in polybori::CDegTermStack<polybori::CCuddNavigator, polybori::invalid_tag, polybori::invalid_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> >::increment ()\n   from /home/malb/SAGE/local/lib/libpolybori.so\n#7  0x00002b20a166bb88 in polybori::dd_print_terms<polybori::COrderedIter<polybori::CCuddNavigator, polybori::BooleExponent>, polybori::variable_name<polybori::OrderedManagerBase<polybori::CCuddInterface>, int, char const*>, polybori::CStringLiteral<3u>, polybori::CStringLiteral<4u>, polybori::integral_constant<unsigned int, 1u, unsigned int>, std::ostream> ()\n   from /home/malb/SAGE/local/lib/libpolybori.so\n#8  0x00002b20a1662ea1 in polybori::BoolePolynomial::print ()\n   from /home/malb/SAGE/local/lib/libpolybori.so\n#9  0x00002b20a13811eb in _to_PyString<polybori::BoolePolynomial> (x=0x2b208dc4b7a0)\n    at /home/malb/SAGE/local//include/csage/ccobject.h:87\n#10 0x00002b20a1373b14 in __pyx_pf_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial__repr_ (\n    __pyx_v_self=0x2b208dc4b780, unused=<value optimized out>)\n    at sage/rings/polynomial/pbori.cpp:10639\n#11 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)\n    at Objects/abstract.c:1860\n#12 0x00000000004801d2 in PyEval_CallObjectWithKeywords (func=0x30d1cf8, arg=0x2b208dbda050,\n    kw=0x0) at Python/ceval.c:3433\n#13 0x00002b209293dc8d in __pyx_pf_4sage_9structure_11sage_object_10SageObject___repr__ (\n    __pyx_v_self=0x2b208dc4b780) at sage/structure/sage_object.c:723\n#14 0x0000000000446042 in _PyObject_Str (v=0x2b208e9d49c0) at Objects/object.c:406\n#15 0x00000000004460eb in PyObject_Str (v=0x2b208e9d49c0) at Objects/object.c:426\n#16 0x0000000000450f9d in string_new (type=0x726580, args=<value optimized out>,\n    kwds=<value optimized out>) at Objects/stringobject.c:3892\n#17 0x000000000045cb23 in type_call (type=0x2b208e9d49c0, args=0x33f0e50, kwds=0x0)\n    at Objects/typeobject.c:422\n#18 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)\n    at Objects/abstract.c:1860\n#19 0x00000000004801d2 in PyEval_CallObjectWithKeywords (func=0x726580, arg=0x33f0e50, kw=0x0)\n    at Python/ceval.c:3433\n#20 0x000000000047dd3e in builtin_map (self=<value optimized out>, args=<value optimized out>)\n    at Python/bltinmodule.c:948\n#21 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)\n    at Objects/abstract.c:1860\n#22 0x00000000004801d2 in PyEval_CallObjectWithKeywords (func=0x2b208dbe6e18, arg=0x1cd2ef0,\n    kw=0x0) at Python/ceval.c:3433\n#23 0x00002b20a1358535 in __pyx_f_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing__cmp_c_impl (__pyx_v_left=0x2f12d50, __pyx_v_right=0x2f12b50) at sage/rings/polynomial/pbori.cpp:7016\n#24 0x00002b2094a9de21 in __pyx_f_4sage_9structure_6parent_6Parent__richcmp (\n    __pyx_v_left=0x2f12d50, __pyx_v_right=0x2f12b50, __pyx_v_op=2) at sage/structure/parent.c:5349\n#25 0x00002b20a1351725 in __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___richcmp__ (__pyx_v_left=0x2b208e9d49c0, __pyx_v_right=0x200, __pyx_v_op=-1902293984)\n    at sage/rings/polynomial/pbori.cpp:6941\n---Type <return> to continue, or q <return> to quit---\n#26 0x0000000000446cb8 in PyObject_RichCompare (v=0x2f12d50, w=0x2f12b50, op=2)\n    at Objects/object.c:905\n#27 0x00002b2094aa474b in __pyx_f_4sage_9structure_6parent_6Parent__coerce_c (\n    __pyx_v_self=0x2f12b50, __pyx_v_x=0x30f6780) at sage/structure/parent.c:3624\n#28 0x00002b20a136e6da in __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___call__ (__pyx_v_self=0x2f12b50, __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)\n    at sage/rings/polynomial/pbori.cpp:5652\n#29 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)\n    at Objects/abstract.c:1860\n#30 0x00000000004801d2 in PyEval_CallObjectWithKeywords (func=0x2f12b50, arg=0x33f0e10, kw=0x0)\n    at Python/ceval.c:3433\n#31 0x00002b2094aa49a7 in __pyx_f_4sage_9structure_6parent_6Parent__coerce_c (\n    __pyx_v_self=0x2f12b50, __pyx_v_x=0x30f6780) at sage/structure/parent.c:3639\n#32 0x00002b20a136e6da in __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___call__ (__pyx_v_self=0x2f12b50, __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)\n    at sage/rings/polynomial/pbori.cpp:5652\n#33 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)\n    at Objects/abstract.c:1860\n#34 0x00000000004801d2 in PyEval_CallObjectWithKeywords (func=0x2f12b50, arg=0x33f0dd0, kw=0x0)\n    at Python/ceval.c:3433\n#35 0x00002b2094aa49a7 in __pyx_f_4sage_9structure_6parent_6Parent__coerce_c (\n    __pyx_v_self=0x2f12b50, __pyx_v_x=0x30f6780) at sage/structure/parent.c:3639\n#36 0x00002b20a136e6da in __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___call__ (__pyx_v_self=0x2f12b50, __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)\n    at sage/rings/polynomial/pbori.cpp:5652\n#37 0x0000000000417bb3 in PyObject_Call (func=0x2b208e9d49c0, arg=0x200, kw=0x2b208e9d4c20)\n    at Objects/abstract.c:1860\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1712\n\n",
    "closed_at": "2008-01-11T19:25:12Z",
    "created_at": "2008-01-07T13:40:35Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch, positive review] logic error in coercion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1712",
    "user": "https://github.com/malb"
}
```
Assignee: @burcin

CC:  @robertwb

Keywords: sigsegv

How to reproduce:

```
sage: P.<a,b,c> = BooleanPolynomialRing(3,order='degrevlex')
sage: R.<a,b,c> = BooleanPolynomialRing(3,order='degrevlex')
sage: P("a") == R("a")
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

Issue created by migration from https://trac.sagemath.org/ticket/1712





---

archive/issue_comments_010825.json:
```json
{
    "body": "fix logic error in coercion",
    "created_at": "2008-01-11T10:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1712#issuecomment-10825",
    "user": "https://github.com/burcin"
}
```

fix logic error in coercion



---

archive/issue_comments_010826.json:
```json
{
    "body": "Changing component from commutative algebra to coercion.",
    "created_at": "2008-01-11T10:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1712#issuecomment-10826",
    "user": "https://github.com/burcin"
}
```

Changing component from commutative algebra to coercion.



---

archive/issue_comments_010827.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-11T10:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1712#issuecomment-10827",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010828.json:
```json
{
    "body": "Attachment [trac_1712.patch](tarball://root/attachments/some-uuid/ticket1712/trac_1712.patch) by @burcin created at 2008-01-11 10:41:11\n\nAs of 2.9.10.alpha0, `BooleanPolynomialRing` doesn't support coercion from strings. Approximating the test case with\n\n```\nP(a) == R(a)\n```\n\ngives a similar error. The real culprit is here:\n\n```\nP(a)\n```\n\nWhen trying to coerce an element from a ring that compares equal to self, the coercion model goes into an infinite recursion, because of the following lines  in `sage/structure/parent.pyx` (starting from line 349)\n\n```\ncdef _coerce_c(self, x):          # DO NOT OVERRIDE THIS (call it)\n    try:\n        P = x.parent()   # todo -- optimize\n        if P is self:\n            return x\n        elif P == self:      # canonically isomorphic parents in same category.\n            return self(x)   \n\n```\n\nIf `x` has a \"canonically isomorphic parent\", then the coerce function of `self` should handle the conversion, which is called by the code that follows the segment above. Calling `self(x)` leads to `self.__call__` trying `self._coerce_c`, which results in the infinite recursion.\n\nattachment:trac_1712.patch removes the offending lines, fixing the error. All tests pass after the patch.",
    "created_at": "2008-01-11T10:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1712#issuecomment-10828",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_1712.patch](tarball://root/attachments/some-uuid/ticket1712/trac_1712.patch) by @burcin created at 2008-01-11 10:41:11

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

archive/issue_comments_010829.json:
```json
{
    "body": "Attachment [coercion_test.patch](tarball://root/attachments/some-uuid/ticket1712/coercion_test.patch) by @burcin created at 2008-01-11 10:48:26\n\nadd testcase to BooleanPolynomialRing._coerce_c_impl to catch this error",
    "created_at": "2008-01-11T10:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1712#issuecomment-10829",
    "user": "https://github.com/burcin"
}
```

Attachment [coercion_test.patch](tarball://root/attachments/some-uuid/ticket1712/coercion_test.patch) by @burcin created at 2008-01-11 10:48:26

add testcase to BooleanPolynomialRing._coerce_c_impl to catch this error



---

archive/issue_comments_010830.json:
```json
{
    "body": "OK, I see the problem and the solution is good. Will keep this in mind for the coercion re-write.",
    "created_at": "2008-01-11T18:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1712#issuecomment-10830",
    "user": "https://github.com/robertwb"
}
```

OK, I see the problem and the solution is good. Will keep this in mind for the coercion re-write.



---

archive/issue_events_004174.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-11T19:25:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1712",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1712#event-4174"
}
```



---

archive/issue_comments_010831.json:
```json
{
    "body": "I merged both patches in Sage 2.10.alpha2",
    "created_at": "2008-01-11T19:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1712#issuecomment-10831",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I merged both patches in Sage 2.10.alpha2



---

archive/issue_comments_010832.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-11T19:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1712#issuecomment-10832",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
