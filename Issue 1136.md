# Issue 1136: libsingular tends to segfault with polynomials over Q

archive/issues_001136.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: singular\n\nAfter you've applied the attached patch (which does not change or add any extension code, just pure python), running the following code will occasionally result in a segfault. I have traced this to libsingular trying to free() an invalid memory address.\n\nHere's the code to run, once you've applied the patch:\n\n```\ndef test(n):\n    R.<x,y,z> = QQ[]\n    P = (0, 0, 1)\n    for i in range(n):\n        c = [QQ.random_element(10,10) for i in xrange(9)]\n        f = c[0]*x^3 + c[1]*x^2*y + c[2]*x*y^2 + c[3]*y^3 + c[4]*x*y*z + c[5]*x^2*z + c[6]*x*z^2 + c[7]*y*z^2 + c[8]*y^2*z\n        print \"trying %s\" % f\n        E = EllipticCurve_from_cubic(f, P, algorithm=\"sage\")\n        print \"sage: %s\" % E\n\nsage: test(100)\n```\n\nThis is on an ubuntu x64, running on an intel core 2 duo santa rosa.\n\nThe first few levels of a gdb backtrace:\n\n```\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread 47923767875296 (LWP 16318)]\n0x00002b961efab6ab in free () from /lib/libc.so.6\n(gdb) bt\n#0  0x00002b961efab6ab in free () from /lib/libc.so.6\n#1  0x00002b96305fbd3c in _nlDelete_NoImm (a=0x2b9630a129c0, r=<value optimized out>) at longrat.cc:1430\n#2  0x00002b96306b2e8b in p_Delete__FieldQ_LengthGeneral_OrdGeneral (pp=0x2b86b28, r=0x2b96309d3160) at longrat.cc:2192\n#3  0x00002b963024b97b in __pyx_tp_dealloc_4sage_5rings_10polynomial_28multi_polynomial_libsingular_MPolynomial_libsingular (\n    o=0x2b86af8) at /home/bob/sage/local//include/singular/pInline2.h:429\n#4  0x00000000004d195a in frame_dealloc (f=0x2bde7e0) at Objects/frameobject.c:416\n#5  0x00000000004d1b74 in frame_dealloc (f=0x2bfdb30) at Objects/frameobject.c:424\n#6  0x00000000004b06bb in tb_dealloc (tb=0x2b79a28) at Python/traceback.c:34\n#7  0x000000000044150d in insertdict (mp=0x762fa0, key=0x2b961f979b20, hash=7943982932492106152, value=0x2b79b48)\n    at Objects/dictobject.c:412\n#8  0x0000000000442eee in PyDict_SetItem (op=0x762fa0, key=0x2b961f979b20, value=0x2b79b48) at Objects/dictobject.c:637\n#9  0x0000000000442ffb in PyDict_SetItemString (v=0x762fa0, key=<value optimized out>, item=0x2b79b48)\n    at Objects/dictobject.c:2178\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1136\n\n",
    "created_at": "2007-11-09T23:42:59Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "libsingular tends to segfault with polynomials over Q",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1136",
    "user": "https://github.com/bobmoretti"
}
```
Assignee: @malb

Keywords: singular

After you've applied the attached patch (which does not change or add any extension code, just pure python), running the following code will occasionally result in a segfault. I have traced this to libsingular trying to free() an invalid memory address.

Here's the code to run, once you've applied the patch:

```
def test(n):
    R.<x,y,z> = QQ[]
    P = (0, 0, 1)
    for i in range(n):
        c = [QQ.random_element(10,10) for i in xrange(9)]
        f = c[0]*x^3 + c[1]*x^2*y + c[2]*x*y^2 + c[3]*y^3 + c[4]*x*y*z + c[5]*x^2*z + c[6]*x*z^2 + c[7]*y*z^2 + c[8]*y^2*z
        print "trying %s" % f
        E = EllipticCurve_from_cubic(f, P, algorithm="sage")
        print "sage: %s" % E

sage: test(100)
```

This is on an ubuntu x64, running on an intel core 2 duo santa rosa.

The first few levels of a gdb backtrace:

```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47923767875296 (LWP 16318)]
0x00002b961efab6ab in free () from /lib/libc.so.6
(gdb) bt
#0  0x00002b961efab6ab in free () from /lib/libc.so.6
#1  0x00002b96305fbd3c in _nlDelete_NoImm (a=0x2b9630a129c0, r=<value optimized out>) at longrat.cc:1430
#2  0x00002b96306b2e8b in p_Delete__FieldQ_LengthGeneral_OrdGeneral (pp=0x2b86b28, r=0x2b96309d3160) at longrat.cc:2192
#3  0x00002b963024b97b in __pyx_tp_dealloc_4sage_5rings_10polynomial_28multi_polynomial_libsingular_MPolynomial_libsingular (
    o=0x2b86af8) at /home/bob/sage/local//include/singular/pInline2.h:429
#4  0x00000000004d195a in frame_dealloc (f=0x2bde7e0) at Objects/frameobject.c:416
#5  0x00000000004d1b74 in frame_dealloc (f=0x2bfdb30) at Objects/frameobject.c:424
#6  0x00000000004b06bb in tb_dealloc (tb=0x2b79a28) at Python/traceback.c:34
#7  0x000000000044150d in insertdict (mp=0x762fa0, key=0x2b961f979b20, hash=7943982932492106152, value=0x2b79b48)
    at Objects/dictobject.c:412
#8  0x0000000000442eee in PyDict_SetItem (op=0x762fa0, key=0x2b961f979b20, value=0x2b79b48) at Objects/dictobject.c:637
#9  0x0000000000442ffb in PyDict_SetItemString (v=0x762fa0, key=<value optimized out>, item=0x2b79b48)
    at Objects/dictobject.c:2178
```

Issue created by migration from https://trac.sagemath.org/ticket/1136





---

archive/issue_comments_006872.json:
```json
{
    "body": "Attachment [weirstrass.hg](tarball://root/attachments/some-uuid/ticket1136/weirstrass.hg) by @bobmoretti created at 2007-11-09 23:44:47\n\npatch for weierstrass normal form transform code",
    "created_at": "2007-11-09T23:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1136#issuecomment-6872",
    "user": "https://github.com/bobmoretti"
}
```

Attachment [weirstrass.hg](tarball://root/attachments/some-uuid/ticket1136/weirstrass.hg) by @bobmoretti created at 2007-11-09 23:44:47

patch for weierstrass normal form transform code



---

archive/issue_events_003041.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-10T11:23:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1136#event-3041"
}
```



---

archive/issue_comments_006873.json:
```json
{
    "body": "I think I got a slightly better backtrace:\n\n```\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread 47957152087904 (LWP 11524)]\n0x00002b9de5bc5d83 in __gmpz_pow_ui () from /tmp/Work-mabshoff/sage-2.8.12.alpha1-vg/local/lib/libgmp.so.3\n(gdb) bt\n#0  0x00002b9de5bc5d83 in __gmpz_pow_ui () from /tmp/Work-mabshoff/sage-2.8.12.alpha1-vg/local/lib/libgmp.so.3\n#1  0x00002b9defb51bc2 in nlPower (x=0xfffffffffffffffd, exp=3, u=0x7fffc625c148) at longrat.cc:933\n#2  0x00002b9defb7775a in pMonPower (p=0x2b9defe33648, exp=3) at polys1.cc:136\n#3  0x00002b9defb7b95e in pPower (p=0x2b9defe33648, i=3) at polys1.cc:333\n#4  0x00002b9def8b43bd in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular___pow__ (\n    __pyx_v_self=0x2b9df68d0aa0, __pyx_arg_exp=<value optimized out>, __pyx_v_ignored=0x620380)\n    at sage/rings/polynomial/multi_polynomial_libsingular.cpp:9205\n#5  0x0000000000415e90 in ternary_op (v=0x2b9df68d0aa0, w=0xb910c0, z=0x620380, op_slot=48, op_name=<value optimized out>)\n    at Objects/abstract.c:518\n#6  0x00002b9def8bf63f in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular___call__ (\n    __pyx_v_self=0x2b9df68c09f0, __pyx_args=0x2b9de4862050, __pyx_kwds=0x0) at sage/rings/polynomial/multi_polynomial_libsingular.cpp:7815\n#7  0x0000000000415523 in PyObject_Call (func=0x2b9defe33a58, arg=0xfffffffffffffffd, kw=0x3) at Objects/abstract.c:1860\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-11-10T11:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1136#issuecomment-6873",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I think I got a slightly better backtrace:

```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47957152087904 (LWP 11524)]
0x00002b9de5bc5d83 in __gmpz_pow_ui () from /tmp/Work-mabshoff/sage-2.8.12.alpha1-vg/local/lib/libgmp.so.3
(gdb) bt
#0  0x00002b9de5bc5d83 in __gmpz_pow_ui () from /tmp/Work-mabshoff/sage-2.8.12.alpha1-vg/local/lib/libgmp.so.3
#1  0x00002b9defb51bc2 in nlPower (x=0xfffffffffffffffd, exp=3, u=0x7fffc625c148) at longrat.cc:933
#2  0x00002b9defb7775a in pMonPower (p=0x2b9defe33648, exp=3) at polys1.cc:136
#3  0x00002b9defb7b95e in pPower (p=0x2b9defe33648, i=3) at polys1.cc:333
#4  0x00002b9def8b43bd in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular___pow__ (
    __pyx_v_self=0x2b9df68d0aa0, __pyx_arg_exp=<value optimized out>, __pyx_v_ignored=0x620380)
    at sage/rings/polynomial/multi_polynomial_libsingular.cpp:9205
#5  0x0000000000415e90 in ternary_op (v=0x2b9df68d0aa0, w=0xb910c0, z=0x620380, op_slot=48, op_name=<value optimized out>)
    at Objects/abstract.c:518
#6  0x00002b9def8bf63f in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular___call__ (
    __pyx_v_self=0x2b9df68c09f0, __pyx_args=0x2b9de4862050, __pyx_kwds=0x0) at sage/rings/polynomial/multi_polynomial_libsingular.cpp:7815
#7  0x0000000000415523 in PyObject_Call (func=0x2b9defe33a58, arg=0xfffffffffffffffd, kw=0x3) at Objects/abstract.c:1860
```

Cheers,

Michael



---

archive/issue_comments_006874.json:
```json
{
    "body": "Attachment [libsingular-singsegv.patch](tarball://root/attachments/some-uuid/ticket1136/libsingular-singsegv.patch) by @malb created at 2007-11-11 20:59:08",
    "created_at": "2007-11-11T20:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1136#issuecomment-6874",
    "user": "https://github.com/malb"
}
```

Attachment [libsingular-singsegv.patch](tarball://root/attachments/some-uuid/ticket1136/libsingular-singsegv.patch) by @malb created at 2007-11-11 20:59:08



---

archive/issue_comments_006875.json:
```json
{
    "body": "The attached patch fixes that problem for me.",
    "created_at": "2007-11-11T20:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1136#issuecomment-6875",
    "user": "https://github.com/malb"
}
```

The attached patch fixes that problem for me.



---

archive/issue_events_003042.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-11-11T20:59:47Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1136#event-3042"
}
```



---

archive/issue_events_003043.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-11-11T20:59:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1136#event-3043"
}
```



---

archive/issue_comments_006876.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-11T20:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1136#issuecomment-6876",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006877.json:
```json
{
    "body": "Merged in 2.8.13.alpha1. \n\nI am not an expert on this code, but I assume it is good. Merge in good faith, revert if it causes any trouble.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-19T21:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1136#issuecomment-6877",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.13.alpha1. 

I am not an expert on this code, but I assume it is good. Merge in good faith, revert if it causes any trouble.

Cheers,

Michael



---

archive/issue_comments_006878.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-19T21:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1136#issuecomment-6878",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003044.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-19T21:30:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1136",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1136#event-3044"
}
```
