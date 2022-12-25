# Issue 3938: coercion framework converts built-in types to Sage types when it should not

archive/issues_003938.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  cwitty\n\nThis came up while reviewing #2898, which adds a conversion from float to ZZ (for integral values).  After applying that patch, you get:\n\n```\nsage: 1.0r/8\n1/8\n```\n\nThat's because of this code in coerce.pyx, which does a conversion rather than a coercion:\n\n```\n        elif PY_IS_NUMERIC(x):\n            try:\n                x = yp(x)\n                if PY_TYPE_CHECK(yp, type): return x,y\n```\n\nI tried to fix this, but every time I fixed something it broke something else.  I'm going to attach my latest non-working patch, which may or may not be a useful place to start.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3938\n\n",
    "created_at": "2008-08-23T21:02:17Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "coercion framework converts built-in types to Sage types when it should not",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3938",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @robertwb

CC:  cwitty

This came up while reviewing #2898, which adds a conversion from float to ZZ (for integral values).  After applying that patch, you get:

```
sage: 1.0r/8
1/8
```

That's because of this code in coerce.pyx, which does a conversion rather than a coercion:

```
        elif PY_IS_NUMERIC(x):
            try:
                x = yp(x)
                if PY_TYPE_CHECK(yp, type): return x,y
```

I tried to fix this, but every time I fixed something it broke something else.  I'm going to attach my latest non-working patch, which may or may not be a useful place to start.

Issue created by migration from https://trac.sagemath.org/ticket/3938





---

archive/issue_comments_028160.json:
```json
{
    "body": "Attachment [trac3938-coercion-converts-native.patch](tarball://root/attachments/some-uuid/ticket3938/trac3938-coercion-converts-native.patch) by @robertwb created at 2008-08-24 08:43:53\n\nI've been playing around with this a bit, simplified your patch some, but one consequence is that \n\n```\nsage: parent(RealField(100)(1.5) + float(1.5)) # good?\n<type 'float'>\nsage: RealField(100)(2^4000) == float('inf')   # bad?\nTrue\n```\n\nThoughts?",
    "created_at": "2008-08-24T08:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28160",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac3938-coercion-converts-native.patch](tarball://root/attachments/some-uuid/ticket3938/trac3938-coercion-converts-native.patch) by @robertwb created at 2008-08-24 08:43:53

I've been playing around with this a bit, simplified your patch some, but one consequence is that 

```
sage: parent(RealField(100)(1.5) + float(1.5)) # good?
<type 'float'>
sage: RealField(100)(2^4000) == float('inf')   # bad?
True
```

Thoughts?



---

archive/issue_comments_028161.json:
```json
{
    "body": "Both of these changes make float act more like RDF.  I've sometimes wished that comparison operators would coerce to more-precise types instead of less-precise, but that would be a huge change across big parts of Sage; unless such a policy change is made, I think that both consequences are actually good.",
    "created_at": "2008-08-24T22:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28161",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Both of these changes make float act more like RDF.  I've sometimes wished that comparison operators would coerce to more-precise types instead of less-precise, but that would be a huge change across big parts of Sage; unless such a policy change is made, I think that both consequences are actually good.



---

archive/issue_comments_028162.json:
```json
{
    "body": "Attachment [3938-type-coercion-2.patch](tarball://root/attachments/some-uuid/ticket3938/3938-type-coercion-2.patch) by @robertwb created at 2008-08-27 16:13:58",
    "created_at": "2008-08-27T16:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28162",
    "user": "https://github.com/robertwb"
}
```

Attachment [3938-type-coercion-2.patch](tarball://root/attachments/some-uuid/ticket3938/3938-type-coercion-2.patch) by @robertwb created at 2008-08-27 16:13:58



---

archive/issue_comments_028163.json:
```json
{
    "body": "Attachment [3938-type-coercion-3.patch](tarball://root/attachments/some-uuid/ticket3938/3938-type-coercion-3.patch) by @robertwb created at 2008-08-27 16:15:59\n\nI feel your pain...what a nasty patch to try and write! Well, I finally feel like I've got a correct, working solution. Apply all three patches.",
    "created_at": "2008-08-27T16:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28163",
    "user": "https://github.com/robertwb"
}
```

Attachment [3938-type-coercion-3.patch](tarball://root/attachments/some-uuid/ticket3938/3938-type-coercion-3.patch) by @robertwb created at 2008-08-27 16:15:59

I feel your pain...what a nasty patch to try and write! Well, I finally feel like I've got a correct, working solution. Apply all three patches.



---

archive/issue_comments_028164.json:
```json
{
    "body": "Carl,\n\nany chance you could review those three patches?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T23:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Carl,

any chance you could review those three patches?

Cheers,

Michael



---

archive/issue_comments_028165.json:
```json
{
    "body": "I get\n\n```\nsage: parent(RealField(10)(1) * float(1))\nReal Field with 10 bits of precision\n```\n\nwith the patches applied against 3.1.2.alpha4.",
    "created_at": "2008-09-06T23:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28165",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

I get

```
sage: parent(RealField(10)(1) * float(1))
Real Field with 10 bits of precision
```

with the patches applied against 3.1.2.alpha4.



---

archive/issue_comments_028166.json:
```json
{
    "body": "Is this not the desired behavior?",
    "created_at": "2008-09-08T16:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28166",
    "user": "https://github.com/robertwb"
}
```

Is this not the desired behavior?



---

archive/issue_comments_028167.json:
```json
{
    "body": "I thought the goal was to convert to the type with most precision.  It seems I was mistaken and this is trying to convert to the type with less precision.  \n\nIn that case it works and passes a good chunk of the test suite.  (I can't test the rest because of the interfaces/lisp.py failure)\n\nIt also passes its own tests and the code looks good.",
    "created_at": "2008-09-08T17:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28167",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

I thought the goal was to convert to the type with most precision.  It seems I was mistaken and this is trying to convert to the type with less precision.  

In that case it works and passes a good chunk of the test suite.  (I can't test the rest because of the interfaces/lisp.py failure)

It also passes its own tests and the code looks good.



---

archive/issue_comments_028168.json:
```json
{
    "body": "This patch causes a Heisenbug:\n\n```\n\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0$ ./sage -t -long devel/sage/sage/modular/modsym/ambient.py\nsage -t -long devel/sage/sage/modular/modsym/ambient.py     \n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n         [4.6 s]\nexit code: 768\n```\nIt does not happen without \"-long\" and when running \"-long -verbose\" it also seems to pass. I guess it is time to valgrind :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T01:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes a Heisenbug:

```

mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0$ ./sage -t -long devel/sage/sage/modular/modsym/ambient.py
sage -t -long devel/sage/sage/modular/modsym/ambient.py     

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [4.6 s]
exit code: 768
```
It does not happen without "-long" and when running "-long -verbose" it also seems to pass. I guess it is time to valgrind :)

Cheers,

Michael



---

archive/issue_comments_028169.json:
```json
{
    "body": "I didn't find the Heisenbug that Michael mentioned.  I rebased the patches against 3.2.3.",
    "created_at": "2009-01-23T02:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28169",
    "user": "https://github.com/roed314"
}
```

I didn't find the Heisenbug that Michael mentioned.  I rebased the patches against 3.2.3.



---

archive/issue_comments_028170.json:
```json
{
    "body": "Thanks for rebasing this. Since you're not the one who originally wrote it, do you want to give it a review?",
    "created_at": "2009-01-23T22:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28170",
    "user": "https://github.com/robertwb"
}
```

Thanks for rebasing this. Since you're not the one who originally wrote it, do you want to give it a review?



---

archive/issue_comments_028171.json:
```json
{
    "body": "Attachment [3938.patch](tarball://root/attachments/some-uuid/ticket3938/3938.patch) by @roed314 created at 2009-01-24 07:49:26\n\nMerged the three patches, added a few fixes to precision.",
    "created_at": "2009-01-24T07:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28171",
    "user": "https://github.com/roed314"
}
```

Attachment [3938.patch](tarball://root/attachments/some-uuid/ticket3938/3938.patch) by @roed314 created at 2009-01-24 07:49:26

Merged the three patches, added a few fixes to precision.



---

archive/issue_comments_028172.json:
```json
{
    "body": "Patch looks good. Thankfully, David folded everything into one patch. \n\nI have two minor issues, and after these are fixed, I'm happy to give this a positive review. \n\n* There are two long blocks (an `EXAMPLES` and a `TESTS`) that are not indented correctly. \n\n* There are three functions that are moved and one that is new which need doctests. (The moved functions don't necessarily have to have them added, but since it's three functions, it seems worth just adding doctests.)\n\nOnce these are done, I'm happy to give this a positive review.",
    "created_at": "2009-01-24T08:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28172",
    "user": "https://github.com/craigcitro"
}
```

Patch looks good. Thankfully, David folded everything into one patch. 

I have two minor issues, and after these are fixed, I'm happy to give this a positive review. 

* There are two long blocks (an `EXAMPLES` and a `TESTS`) that are not indented correctly. 

* There are three functions that are moved and one that is new which need doctests. (The moved functions don't necessarily have to have them added, but since it's three functions, it seems worth just adding doctests.)

Once these are done, I'm happy to give this a positive review.



---

archive/issue_comments_028173.json:
```json
{
    "body": "OK, I'll go ahead and add those doctests.",
    "created_at": "2009-01-24T08:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28173",
    "user": "https://github.com/robertwb"
}
```

OK, I'll go ahead and add those doctests.



---

archive/issue_comments_028174.json:
```json
{
    "body": "Attachment [3938-type-coercion-final.patch](tarball://root/attachments/some-uuid/ticket3938/3938-type-coercion-final.patch) by @robertwb created at 2009-01-24 10:46:21\n\napply only this patch",
    "created_at": "2009-01-24T10:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28174",
    "user": "https://github.com/robertwb"
}
```

Attachment [3938-type-coercion-final.patch](tarball://root/attachments/some-uuid/ticket3938/3938-type-coercion-final.patch) by @robertwb created at 2009-01-24 10:46:21

apply only this patch



---

archive/issue_comments_028175.json:
```json
{
    "body": "OK, I added the doctests and fixed the indentation.",
    "created_at": "2009-01-24T10:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28175",
    "user": "https://github.com/robertwb"
}
```

OK, I added the doctests and fixed the indentation.



---

archive/issue_comments_028176.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-01-24T11:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28176",
    "user": "https://github.com/craigcitro"
}
```

Looks good.



---

archive/issue_comments_028177.json:
```json
{
    "body": "One fix:\n\n```\n    TypeError: no cannonical coercion from Real Field with 53 bits of precision to Real Field with 100 bits of precision\n```\nneeds to become\n\n```\n    TypeError: no canonical coercion from Real Field with 53 bits of precision to Real Field with 100 bits of precision\n```\n\nI am fixing that in the patch I am applying.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T15:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One fix:

```
    TypeError: no cannonical coercion from Real Field with 53 bits of precision to Real Field with 100 bits of precision
```
needs to become

```
    TypeError: no canonical coercion from Real Field with 53 bits of precision to Real Field with 100 bits of precision
```

I am fixing that in the patch I am applying.

Cheers,

Michael



---

archive/issue_events_009042.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T15:22:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3938#event-9042"
}
```



---

archive/issue_events_009043.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T15:22:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3938#event-9043"
}
```



---

archive/issue_comments_028178.json:
```json
{
    "body": "Merged 3938-type-coercion-final.patch with spelling fix in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T15:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28178",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 3938-type-coercion-final.patch with spelling fix in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_028179.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T15:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3938#issuecomment-28179",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
