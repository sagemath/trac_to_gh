# Issue 4957: inconsistent integer hashing

archive/issues_004957.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: z = 18446462603027742720\nsage: hash(z)\n66912258\nsage: hash(int(z))\n-131071\nsage: hash(long(z))\n-131071\n```\n\n\nThis causes problems with looking up values in hashtables...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4957\n\n",
    "created_at": "2009-01-09T02:26:00Z",
    "labels": [
        "component: basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "inconsistent integer hashing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4957",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody


```
sage: z = 18446462603027742720
sage: hash(z)
66912258
sage: hash(int(z))
-131071
sage: hash(long(z))
-131071
```


This causes problems with looking up values in hashtables...

Issue created by migration from https://trac.sagemath.org/ticket/4957





---

archive/issue_comments_037605.json:
```json
{
    "body": "This was **ugly**. It turns out that we were shifting an `int` to the right by 45 bits on a 32 bit machine, which one might think would result in zero, but in fact shifts to the right by `(45%32) = 13` bits.\n\nThe attached patch fixes this, and adds some doctests.",
    "created_at": "2009-01-23T12:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37605",
    "user": "https://github.com/craigcitro"
}
```

This was **ugly**. It turns out that we were shifting an `int` to the right by 45 bits on a 32 bit machine, which one might think would result in zero, but in fact shifts to the right by `(45%32) = 13` bits.

The attached patch fixes this, and adds some doctests.



---

archive/issue_comments_037606.json:
```json
{
    "body": "Changing assignee from somebody to @craigcitro.",
    "created_at": "2009-01-23T12:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37606",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from somebody to @craigcitro.



---

archive/issue_comments_037607.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T12:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37607",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037608.json:
```json
{
    "body": "Excellent. I haven't been able to break it, and the code (and comment) look good.",
    "created_at": "2009-01-23T13:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37608",
    "user": "https://github.com/robertwb"
}
```

Excellent. I haven't been able to break it, and the code (and comment) look good.



---

archive/issue_comments_037609.json:
```json
{
    "body": "This is broken on 64 bit linux:\n\n```\nsage -t -long \"devel/sage/sage/rings/integer.pyx\"           \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx\", line 2085:\n    sage: n = -920390823904823094890238490238484; n.__hash__()\nExpected:\n    6874330978542788722   \nGot:\n    6917515397235318898\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx\", line 2101:\n    sage: hash(n)\nExpected:\n    -9223372036854767616      \nGot:\n    8192\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx\", line 2104:\n    sage: hash(n) == hash(int(n))\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n",
    "created_at": "2009-01-24T14:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is broken on 64 bit linux:

```
sage -t -long "devel/sage/sage/rings/integer.pyx"           
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx", line 2085:
    sage: n = -920390823904823094890238490238484; n.__hash__()
Expected:
    6874330978542788722   
Got:
    6917515397235318898
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx", line 2101:
    sage: hash(n)
Expected:
    -9223372036854767616      
Got:
    8192
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx", line 2104:
    sage: hash(n) == hash(int(n))
Expected:
    True
Got:
    False
**********************************************************************
```




---

archive/issue_comments_037610.json:
```json
{
    "body": "Darn :(. The first two may be OK (we need to see what hash(int(n)) is, but the second one is a problem.",
    "created_at": "2009-01-24T21:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37610",
    "user": "https://github.com/robertwb"
}
```

Darn :(. The first two may be OK (we need to see what hash(int(n)) is, but the second one is a problem.



---

archive/issue_comments_037611.json:
```json
{
    "body": "Attachment [trac-4957.patch](tarball://root/attachments/some-uuid/ticket4957/trac-4957.patch) by @craigcitro created at 2009-01-24 23:24:15",
    "created_at": "2009-01-24T23:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37611",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4957.patch](tarball://root/attachments/some-uuid/ticket4957/trac-4957.patch) by @craigcitro created at 2009-01-24 23:24:15



---

archive/issue_comments_037612.json:
```json
{
    "body": "Ok, I fixed it. It turns out it was some sloppy C coding on my part: I really wanted `sizeof(mp_limb_t)` instead of `sizeof(int)`.",
    "created_at": "2009-01-24T23:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37612",
    "user": "https://github.com/craigcitro"
}
```

Ok, I fixed it. It turns out it was some sloppy C coding on my part: I really wanted `sizeof(mp_limb_t)` instead of `sizeof(int)`.



---

archive/issue_comments_037613.json:
```json
{
    "body": "I bet this is the right fix, could you re-run the tests on a 64 bit machine?",
    "created_at": "2009-01-24T23:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37613",
    "user": "https://github.com/robertwb"
}
```

I bet this is the right fix, could you re-run the tests on a 64 bit machine?



---

archive/issue_comments_037614.json:
```json
{
    "body": "That does the trick on sage.math",
    "created_at": "2009-01-24T23:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37614",
    "user": "https://github.com/robertwb"
}
```

That does the trick on sage.math



---

archive/issue_comments_037615.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T21:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37615",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_events_005198.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-25T21:01:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4957#event-5198"
}
```



---

archive/issue_comments_037616.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T21:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37616",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
