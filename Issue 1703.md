# Issue 1703: memleak in Singular: one mpz is leaked in longrat.cc triggered by linear_code.py

archive/issues_001703.json:
```json
{
    "body": "Assignee: mabshoff\n\nHi, while valgrinding `linear_code.py` I came across the following:\n\n```\n==32468== 5,296 bytes in 662 blocks are definitely lost in loss record 7,790 of 8,072\n==32468==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==32468==    by 0x6160C87: __gmpz_init (in /tmp/Work-mabshoff/release-cycle/sage-2.10.alpha0/local/lib/libgmp.so.3.4.1)\n==32468==    by 0x128B87AF: nlNormalize(snumber*&) (longrat.cc:1147)\n==32468==    by 0x128DBE70: p_Normalize(spolyrec*, sip_sring*) (polys.cc:800)\n==32468==    by 0x12CB3DB0: __pyx_f_4sage_4libs_8singular_8singular_10Conversion_new_MP (singular.cpp:4552)\n==32468==    by 0x12641F8F: __pyx_f_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular__mul_\nc_impl(__pyx_obj_4sage_5rings_10polynomial_28multi_polynomial_libsingular_MPolynomial_libsingular*, __pyx_obj_4sage_9structu\nre_7element_RingElement*) (multi_polynomial_libsingular.cpp:13961)\n==32468==    by 0x9793833: __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (element.c:18414)\n==32468==    by 0x41580C: binary_op1 (abstract.c:398)\n==32468==    by 0x418F47: PyNumber_Multiply (abstract.c:669)\n==32468==    by 0x47F5BC: PyEval_EvalFrameEx (ceval.c:1072)\n==32468==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==32468==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n```\nI tracked this down in `longrat.cc` and am currently testing an updated singular.spkg which should fix this. In case this does I will also send it to the Singular team.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1703\n\n",
    "created_at": "2008-01-06T22:19:11Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "memleak in Singular: one mpz is leaked in longrat.cc triggered by linear_code.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1703",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Hi, while valgrinding `linear_code.py` I came across the following:

```
==32468== 5,296 bytes in 662 blocks are definitely lost in loss record 7,790 of 8,072
==32468==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==32468==    by 0x6160C87: __gmpz_init (in /tmp/Work-mabshoff/release-cycle/sage-2.10.alpha0/local/lib/libgmp.so.3.4.1)
==32468==    by 0x128B87AF: nlNormalize(snumber*&) (longrat.cc:1147)
==32468==    by 0x128DBE70: p_Normalize(spolyrec*, sip_sring*) (polys.cc:800)
==32468==    by 0x12CB3DB0: __pyx_f_4sage_4libs_8singular_8singular_10Conversion_new_MP (singular.cpp:4552)
==32468==    by 0x12641F8F: __pyx_f_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular__mul_
c_impl(__pyx_obj_4sage_5rings_10polynomial_28multi_polynomial_libsingular_MPolynomial_libsingular*, __pyx_obj_4sage_9structu
re_7element_RingElement*) (multi_polynomial_libsingular.cpp:13961)
==32468==    by 0x9793833: __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (element.c:18414)
==32468==    by 0x41580C: binary_op1 (abstract.c:398)
==32468==    by 0x418F47: PyNumber_Multiply (abstract.c:669)
==32468==    by 0x47F5BC: PyEval_EvalFrameEx (ceval.c:1072)
==32468==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==32468==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
```
I tracked this down in `longrat.cc` and am currently testing an updated singular.spkg which should fix this. In case this does I will also send it to the Singular team.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1703





---

archive/issue_comments_010760.json:
```json
{
    "body": "Attachment [Sage-2.9.3-fix-singular-memleak-in-longrat.cc.patch](tarball://root/attachments/some-uuid/ticket1703/Sage-2.9.3-fix-singular-memleak-in-longrat.cc.patch) by mabshoff created at 2008-01-06 22:25:17\n\nThis patch isn't against the latest spkg, but I will post an updated spkg with this patch shortly",
    "created_at": "2008-01-06T22:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1703#issuecomment-10760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.9.3-fix-singular-memleak-in-longrat.cc.patch](tarball://root/attachments/some-uuid/ticket1703/Sage-2.9.3-fix-singular-memleak-in-longrat.cc.patch) by mabshoff created at 2008-01-06 22:25:17

This patch isn't against the latest spkg, but I will post an updated spkg with this patch shortly



---

archive/issue_comments_010761.json:
```json
{
    "body": "`sage -testall` passes. Some statistics:\nBefore the patch:\n\n```\n==32468== LEAK SUMMARY:\n==32468==    definitely lost: 5,816 bytes in 727 blocks.\n==32468==      possibly lost: 386,415 bytes in 1,043 blocks.\n==32468==    still reachable: 30,608,788 bytes in 187,141 blocks.\n==32468==         suppressed: 0 bytes in 0 blocks.\n```\nAfter the patch:\n\n```\n==11915== LEAK SUMMARY:\n==11915==    definitely lost: 16 bytes in 2 blocks.\n==11915==      possibly lost: 386,991 bytes in 1,044 blocks.\n==11915==    still reachable: 30,608,164 bytes in 187,136 blocks.\n==11915==         suppressed: 0 bytes in 0 blocks.\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-01-06T23:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1703#issuecomment-10761",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

`sage -testall` passes. Some statistics:
Before the patch:

```
==32468== LEAK SUMMARY:
==32468==    definitely lost: 5,816 bytes in 727 blocks.
==32468==      possibly lost: 386,415 bytes in 1,043 blocks.
==32468==    still reachable: 30,608,788 bytes in 187,141 blocks.
==32468==         suppressed: 0 bytes in 0 blocks.
```
After the patch:

```
==11915== LEAK SUMMARY:
==11915==    definitely lost: 16 bytes in 2 blocks.
==11915==      possibly lost: 386,991 bytes in 1,044 blocks.
==11915==    still reachable: 30,608,164 bytes in 187,136 blocks.
==11915==         suppressed: 0 bytes in 0 blocks.
```

Cheers,

Michael



---

archive/issue_comments_010762.json:
```json
{
    "body": "The actual line change is:\n\n```\n--- longrat.cc.orig     2007-12-02 07:05:25.000000000 -0800\n+++ longrat.cc  2008-01-07 03:17:40.000000000 -0800\n@@ -1171,6 +1171,7 @@\n#endif\n               omFreeBin((ADDRESS)x, rnumber_bin);\n               x=INT_TO_SR(ui);\n+              mpz_clear(&gcd);\n               return;\n             }\n           }\n```\nwhich looks good to me.",
    "created_at": "2008-01-07T11:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1703#issuecomment-10762",
    "user": "https://github.com/malb"
}
```

The actual line change is:

```
--- longrat.cc.orig     2007-12-02 07:05:25.000000000 -0800
+++ longrat.cc  2008-01-07 03:17:40.000000000 -0800
@@ -1171,6 +1171,7 @@
#endif
               omFreeBin((ADDRESS)x, rnumber_bin);
               x=INT_TO_SR(ui);
+              mpz_clear(&gcd);
               return;
             }
           }
```
which looks good to me.



---

archive/issue_comments_010763.json:
```json
{
    "body": "Attachment [Singular-3-0-4-2-fix-longrat.cc-mpz-leak.patch](tarball://root/attachments/some-uuid/ticket1703/Singular-3-0-4-2-fix-longrat.cc-mpz-leak.patch) by mabshoff created at 2008-01-07 11:53:21\n\nThis is the actual patch against the Singular codebase",
    "created_at": "2008-01-07T11:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1703#issuecomment-10763",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Singular-3-0-4-2-fix-longrat.cc-mpz-leak.patch](tarball://root/attachments/some-uuid/ticket1703/Singular-3-0-4-2-fix-longrat.cc-mpz-leak.patch) by mabshoff created at 2008-01-07 11:53:21

This is the actual patch against the Singular codebase



---

archive/issue_comments_010764.json:
```json
{
    "body": "Malb gave this a positive review. I patched the singular.p2.spkg and produced\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha0/singular-3-0-4-1-20071209.p3.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-07T16:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1703#issuecomment-10764",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Malb gave this a positive review. I patched the singular.p2.spkg and produced

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha0/singular-3-0-4-1-20071209.p3.spkg

Cheers,

Michael



---

archive/issue_comments_010765.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-07T16:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1703#issuecomment-10765",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004159.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-07T16:38:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1703",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1703#event-4159"
}
```



---

archive/issue_comments_010766.json:
```json
{
    "body": "The patch has been merged in upstream Singular, so that we can probably remove this workaround from our spkg the next time we update to the current Singular release.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-09T16:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1703#issuecomment-10766",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch has been merged in upstream Singular, so that we can probably remove this workaround from our spkg the next time we update to the current Singular release.

Cheers,

Michael
