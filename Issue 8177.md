# Issue 8177: element_wrapper.py: Sage 4.3.2.alpha1 segfault on Mac OS X 10.6.2

archive/issues_008177.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nthiery mvngu @hivert\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/7754a347b837fad6) and also [reported here](http://groups.google.com/group/sage-devel/browse_thread/thread/7c920d26ddad3345):\n\n```\n> built fine on mac 10.6.2 but one failure for sage -testall :\n\n> The following tests failed:\n\n>        sage -t  \"devel/sage/sage/structure/element_wrapper.py\" # Segfault\n\nI get the same result on bsd.math (Mac OS X 10.6.2). Doing a verbose\nlong doctest, I get:\n\nTrying:\n    Integer(1) < l11###line 213:_sage_    >>> 1 < l11\nExpecting:\n    False\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------ \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8177\n\n",
    "created_at": "2010-02-03T18:45:01Z",
    "labels": [
        "component: doctest",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "element_wrapper.py: Sage 4.3.2.alpha1 segfault on Mac OS X 10.6.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

CC:  @nthiery mvngu @hivert

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/7754a347b837fad6) and also [reported here](http://groups.google.com/group/sage-devel/browse_thread/thread/7c920d26ddad3345):

```
> built fine on mac 10.6.2 but one failure for sage -testall :

> The following tests failed:

>        sage -t  "devel/sage/sage/structure/element_wrapper.py" # Segfault

I get the same result on bsd.math (Mac OS X 10.6.2). Doing a verbose
long doctest, I get:

Trying:
    Integer(1) < l11###line 213:_sage_    >>> 1 < l11
Expecting:
    False

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------ 
```


Issue created by migration from https://trac.sagemath.org/ticket/8177





---

archive/issue_comments_071921.json:
```json
{
    "body": "Here is a complete self-contained session that illustrates the problem:\n\n```\nwstein@bsd:~/build/sage-4.3.2.rc0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: class MyElement(ElementWrapper): __lt__ = ElementWrapper._lt_by_value\n....:\nsage: a = MyElement(1, parent = ZZ)\nsage: 1 < a\n| Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |\n| Type notebook() for the GUI, and license() for information.        |\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\nwstein@bsd:~/build/sage-4.3.2.rc0$\n```\n",
    "created_at": "2010-02-04T12:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71921",
    "user": "https://github.com/williamstein"
}
```

Here is a complete self-contained session that illustrates the problem:

```
wstein@bsd:~/build/sage-4.3.2.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: class MyElement(ElementWrapper): __lt__ = ElementWrapper._lt_by_value
....:
sage: a = MyElement(1, parent = ZZ)
sage: 1 < a
| Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

wstein@bsd:~/build/sage-4.3.2.rc0$
```




---

archive/issue_comments_071922.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-02-04T12:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71922",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_071923.json:
```json
{
    "body": "Oh, and here is the traceback:\n\n```\nsage: 1 < a                                                                 \n\nProgram received signal EXC_BAD_ACCESS, Could not access memory.\nReason: KERN_INVALID_ADDRESS at address: 0x0000000000000000\n0x000000010164f04d in __gmpz_cmp ()\n(gdb) bt\n#0  0x000000010164f04d in __gmpz_cmp ()\n#1  0x0000000103ab178d in __pyx_f_4sage_5rings_7integer_7Integer__cmp_c_impl (__pyx_v_left=0x1097f81b0, __pyx_v_right=0x10caade10) at sage/rings/integer.c:7334\n#2  0x0000000102317afc in __pyx_f_4sage_9structure_7element_7Element__richcmp_c_impl (__pyx_v_left=0x1097f81b0, __pyx_v_right=0x10caade10, __pyx_v_op=0) at sage/structure/element.c:7177\n#3  0x0000000102349553 in __pyx_f_4sage_9structure_7element_7Element__richcmp (__pyx_v_left=0x1097f81b0, __pyx_v_right=0x10caade10, __pyx_v_op=0) at sage/structure/element.c:6917\n#4  0x0000000103aae77b in __pyx_pf_4sage_5rings_7integer_7Integer___richcmp__ (__pyx_v_left=<value temporarily unavailable, due to optimizations>, __pyx_v_right=<value temporarily unavailable, due to optimizations>, __pyx_v_op=<value temporarily unavailable, due to optimizations>) at sage/rings/integer.c:7293\n#5  0x000000010004e15c in try_rich_compare ()\n#6  0x000000010004faff in PyObject_RichCompare ()\n#7  0x00000001000af100 in PyEval_EvalFrameEx ()\n#8  0x00000001000b3e70 in PyEval_EvalCodeEx ()\n...\n```\n",
    "created_at": "2010-02-04T12:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71923",
    "user": "https://github.com/williamstein"
}
```

Oh, and here is the traceback:

```
sage: 1 < a                                                                 

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_INVALID_ADDRESS at address: 0x0000000000000000
0x000000010164f04d in __gmpz_cmp ()
(gdb) bt
#0  0x000000010164f04d in __gmpz_cmp ()
#1  0x0000000103ab178d in __pyx_f_4sage_5rings_7integer_7Integer__cmp_c_impl (__pyx_v_left=0x1097f81b0, __pyx_v_right=0x10caade10) at sage/rings/integer.c:7334
#2  0x0000000102317afc in __pyx_f_4sage_9structure_7element_7Element__richcmp_c_impl (__pyx_v_left=0x1097f81b0, __pyx_v_right=0x10caade10, __pyx_v_op=0) at sage/structure/element.c:7177
#3  0x0000000102349553 in __pyx_f_4sage_9structure_7element_7Element__richcmp (__pyx_v_left=0x1097f81b0, __pyx_v_right=0x10caade10, __pyx_v_op=0) at sage/structure/element.c:6917
#4  0x0000000103aae77b in __pyx_pf_4sage_5rings_7integer_7Integer___richcmp__ (__pyx_v_left=<value temporarily unavailable, due to optimizations>, __pyx_v_right=<value temporarily unavailable, due to optimizations>, __pyx_v_op=<value temporarily unavailable, due to optimizations>) at sage/rings/integer.c:7293
#5  0x000000010004e15c in try_rich_compare ()
#6  0x000000010004faff in PyObject_RichCompare ()
#7  0x00000001000af100 in PyEval_EvalFrameEx ()
#8  0x00000001000b3e70 in PyEval_EvalCodeEx ()
...
```




---

archive/issue_comments_071924.json:
```json
{
    "body": "As mentioned in one of the sage-devel threads linked above, the issue here is that `ZZ` assumes that if it's the parent of some `x`, then `x` is of type `sage.rings.integer.Integer`. (Similar assumptions are made all over.) It turns out that this popping up only on OSX was a weird artifact of compiler details/how memory is initialized/the alignment of the planets, as explained in the sage-devel thread.\n\nI'm waiting for Nicolas to weigh in on what he thinks should happen with the `ElementWrapper` code -- he's probably the most appropriate person to spin a patch. (Nicolas, I'm adding you in the cc.)",
    "created_at": "2010-02-05T17:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71924",
    "user": "https://github.com/craigcitro"
}
```

As mentioned in one of the sage-devel threads linked above, the issue here is that `ZZ` assumes that if it's the parent of some `x`, then `x` is of type `sage.rings.integer.Integer`. (Similar assumptions are made all over.) It turns out that this popping up only on OSX was a weird artifact of compiler details/how memory is initialized/the alignment of the planets, as explained in the sage-devel thread.

I'm waiting for Nicolas to weigh in on what he thinks should happen with the `ElementWrapper` code -- he's probably the most appropriate person to spin a patch. (Nicolas, I'm adding you in the cc.)



---

archive/issue_comments_071925.json:
```json
{
    "body": "Attachment [trac_8177-element_wrapper_segfault-fh.patch](tarball://root/attachments/some-uuid/ticket8177/trac_8177-element_wrapper_segfault-fh.patch) by @hivert created at 2010-02-06 09:20:37",
    "created_at": "2010-02-06T09:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71925",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8177-element_wrapper_segfault-fh.patch](tarball://root/attachments/some-uuid/ticket8177/trac_8177-element_wrapper_segfault-fh.patch) by @hivert created at 2010-02-06 09:20:37



---

archive/issue_comments_071926.json:
```json
{
    "body": "Hi there !\n\nI uploaded a patch where a replaced `ZZ` as a parent to `Sets().example(\"facade\")` which is much closer to a meaningfull parent. It should hide the segfault problem which is actually a problem in Integer. However, I don't have access to a Max OS machine so please tell me if it doesn't work.\n\nCheers,\n\nFlorent",
    "created_at": "2010-02-06T09:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71926",
    "user": "https://github.com/hivert"
}
```

Hi there !

I uploaded a patch where a replaced `ZZ` as a parent to `Sets().example("facade")` which is much closer to a meaningfull parent. It should hide the segfault problem which is actually a problem in Integer. However, I don't have access to a Max OS machine so please tell me if it doesn't work.

Cheers,

Florent



---

archive/issue_comments_071927.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-06T09:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71927",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071928.json:
```json
{
    "body": "Replying to [comment:1 was]:\n> Here is a complete self-contained session that illustrates the problem:\n> {{{\n> wstein`@`bsd:~/build/sage-4.3.2.rc0$ ./sage\n> ----------------------------------------------------------------------\n> | Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |\n> | Type notebook() for the GUI, and license() for information.        |\n> ----------------------------------------------------------------------\n> **********************************************************************\n> *                                                                    *\n> * Warning: this is a prerelease version, and it may be unstable.     *\n> *                                                                    *\n> **********************************************************************\n> sage: class MyElement(ElementWrapper): __lt__ = ElementWrapper._lt_by_value\n> ....:\n> sage: a = MyElement(1, parent = ZZ)\n> sage: 1 < a\n\nJust for the record, could someone post the result of this more self contained example?\n\n```\n   sage: class F(Element):\n    ....:     pass\n    ....:\n    sage: x = F(ZZ)\n    sage: 1 < x\n    False\n```\n",
    "created_at": "2010-02-06T10:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71928",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:1 was]:
> Here is a complete self-contained session that illustrates the problem:
> {{{
> wstein`@`bsd:~/build/sage-4.3.2.rc0$ ./sage
> ----------------------------------------------------------------------
> | Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> **********************************************************************
> *                                                                    *
> * Warning: this is a prerelease version, and it may be unstable.     *
> *                                                                    *
> **********************************************************************
> sage: class MyElement(ElementWrapper): __lt__ = ElementWrapper._lt_by_value
> ....:
> sage: a = MyElement(1, parent = ZZ)
> sage: 1 < a

Just for the record, could someone post the result of this more self contained example?

```
   sage: class F(Element):
    ....:     pass
    ....:
    sage: x = F(ZZ)
    sage: 1 < x
    False
```




---

archive/issue_comments_071929.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-06T12:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71929",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071930.json:
```json
{
    "body": "I have worked further on Florent's patch, and made a separate ticket for it: #8200.\nI have removed the blocker priority on this, and set it on #8200. I leave this ticket open, since the issue is still there. I let the experts decide whether this should be a won't fix or not.",
    "created_at": "2010-02-06T12:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71930",
    "user": "https://github.com/nthiery"
}
```

I have worked further on Florent's patch, and made a separate ticket for it: #8200.
I have removed the blocker priority on this, and set it on #8200. I leave this ticket open, since the issue is still there. I let the experts decide whether this should be a won't fix or not.



---

archive/issue_comments_071931.json:
```json
{
    "body": "For me, this patch fixed the segfault but still failed:\n\n\n```\njeeves:sage-4.3.2.rc0 wdj$ ./sage -t  \"devel/sage/sage/structure/element_wrapper.py\" # Segfault\nsage -t  \"devel/sage/sage/structure/element_wrapper.py\"     \n**********************************************************************\nFile \"/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage/sage/structure/element_wrapper.py\", line 213:\n    sage: 1 < l11\nExpected:\n    False\nGot:\n    True\n**********************************************************************\n1 items had failures:\n   1 of  14 in __main__.example_8\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/wdj/.sage//tmp/.doctest_element_wrapper.py\n         [2.3 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/structure/element_wrapper.py\"\n```\n\nThis is on sage-4.3.2.rc0 and mac 10.6.2.",
    "created_at": "2010-02-06T12:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71931",
    "user": "https://github.com/wdjoyner"
}
```

For me, this patch fixed the segfault but still failed:


```
jeeves:sage-4.3.2.rc0 wdj$ ./sage -t  "devel/sage/sage/structure/element_wrapper.py" # Segfault
sage -t  "devel/sage/sage/structure/element_wrapper.py"     
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage/sage/structure/element_wrapper.py", line 213:
    sage: 1 < l11
Expected:
    False
Got:
    True
**********************************************************************
1 items had failures:
   1 of  14 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/wdj/.sage//tmp/.doctest_element_wrapper.py
         [2.3 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/structure/element_wrapper.py"
```

This is on sage-4.3.2.rc0 and mac 10.6.2.



---

archive/issue_comments_071932.json:
```json
{
    "body": "Replying to [comment:7 wdj]:\n> For me, this patch fixed the segfault but still failed:\n\nCould you please try with the patch on #8200? It should be fixed in principle. Thanks!",
    "created_at": "2010-02-06T13:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71932",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:7 wdj]:
> For me, this patch fixed the segfault but still failed:

Could you please try with the patch on #8200? It should be fixed in principle. Thanks!



---

archive/issue_comments_071933.json:
```json
{
    "body": "Replying to [comment:8 nthiery]:\n> Replying to [comment:7 wdj]:\n> > For me, this patch fixed the segfault but still failed:\n> \n> Could you please try with the patch on #8200? It should be fixed in principle. Thanks!\n\nI'm running sage -testall on #8200 now (the above single doctest passes though).\n\nDoes this new ticket mean you want Minh to make this as wontfix/invalid/duplicate and close it?",
    "created_at": "2010-02-06T13:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71933",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:8 nthiery]:
> Replying to [comment:7 wdj]:
> > For me, this patch fixed the segfault but still failed:
> 
> Could you please try with the patch on #8200? It should be fixed in principle. Thanks!

I'm running sage -testall on #8200 now (the above single doctest passes though).

Does this new ticket mean you want Minh to make this as wontfix/invalid/duplicate and close it?



---

archive/issue_comments_071934.json:
```json
{
    "body": "Replying to [comment:9 wdj]:\n> Does this new ticket mean you want Minh to make this as wontfix/invalid/duplicate and close it?\n\nNo, it means that, with #8200, I have done my part at fixing my improper usage of ZZ. But the issue that such an improper usage can cause a segfault is still there, and I leave to the experts the decision of whether to fix it now, leave it to later, or resolve it as wontfix.\n\nI personally vote -1 for making it a wontfix.",
    "created_at": "2010-02-06T13:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71934",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:9 wdj]:
> Does this new ticket mean you want Minh to make this as wontfix/invalid/duplicate and close it?

No, it means that, with #8200, I have done my part at fixing my improper usage of ZZ. But the issue that such an improper usage can cause a segfault is still there, and I leave to the experts the decision of whether to fix it now, leave it to later, or resolve it as wontfix.

I personally vote -1 for making it a wontfix.



---

archive/issue_comments_071935.json:
```json
{
    "body": "> No, it means that, with #8200, I have done my part at fixing my improper usage of ZZ. But the issue that such an improper usage can cause a segfault is still there, and I leave to the experts the decision of whether to fix it now, leave it to later, or resolve it as wontfix.\n> \n> I personally vote -1 for making it a wontfix.\n\nI strongly second Nicolas -1. \n\nMoreover, if the segfault is not removed the invariant \n\n```\n    x.parent() == ZZ <==> x.class == Integer\n```\n\nmust be clearly stated with a _big warning_ in the doc. My opinion is that the segfault must be left only if there is a very large performance penalty fixing it.\nBy the way is this invariant an equivalence ? As far as I understood the segfault only came because we where breaking the `==>` part. \n\nCheers,\n\nFlorent\n\nBy the way, I've removed myself as author since I won't be hacking in integers (my work in integrated in #8200).",
    "created_at": "2010-02-07T10:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71935",
    "user": "https://github.com/hivert"
}
```

> No, it means that, with #8200, I have done my part at fixing my improper usage of ZZ. But the issue that such an improper usage can cause a segfault is still there, and I leave to the experts the decision of whether to fix it now, leave it to later, or resolve it as wontfix.
> 
> I personally vote -1 for making it a wontfix.

I strongly second Nicolas -1. 

Moreover, if the segfault is not removed the invariant 

```
    x.parent() == ZZ <==> x.class == Integer
```

must be clearly stated with a _big warning_ in the doc. My opinion is that the segfault must be left only if there is a very large performance penalty fixing it.
By the way is this invariant an equivalence ? As far as I understood the segfault only came because we where breaking the `==>` part. 

Cheers,

Florent

By the way, I've removed myself as author since I won't be hacking in integers (my work in integrated in #8200).



---

archive/issue_comments_071936.json:
```json
{
    "body": "Changing component from doctest to documentation.",
    "created_at": "2013-03-28T23:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71936",
    "user": "https://github.com/roed314"
}
```

Changing component from doctest to documentation.



---

archive/issue_events_008380.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-22T15:19:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8177#event-8380"
}
```



---

archive/issue_comments_071937.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-22T15:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71937",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_071938.json:
```json
{
    "body": "I think we can mark this as invalid as of 5.10:\n\n\n```\nsage: class MyElement(ElementWrapper): __lt__ = ElementWrapper._lt_by_value\nsage: a = MyElement(ZZ, 1)\nsage: 1 < a\nFalse\nsage: a < 1\nFalse\n```\n",
    "created_at": "2013-07-22T15:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71938",
    "user": "https://github.com/mwhansen"
}
```

I think we can mark this as invalid as of 5.10:


```
sage: class MyElement(ElementWrapper): __lt__ = ElementWrapper._lt_by_value
sage: a = MyElement(ZZ, 1)
sage: 1 < a
False
sage: a < 1
False
```




---

archive/issue_comments_071939.json:
```json
{
    "body": "I looked at the code of Integer._rich_cmp, and indeed it now tests that the right hand side is indeed in the Integer class which fixes the issue.\n\nIn an ideal world, we would have added a regression test, but oh well, let's move on.",
    "created_at": "2013-07-24T10:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8177#issuecomment-71939",
    "user": "https://github.com/nthiery"
}
```

I looked at the code of Integer._rich_cmp, and indeed it now tests that the right hand side is indeed in the Integer class which fixes the issue.

In an ideal world, we would have added a regression test, but oh well, let's move on.
