# Issue 4957: inconsistent integer hashing

archive/issues_004957.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: z = 18446462603027742720\nsage: hash(z)\n66912258\nsage: hash(int(z))\n-131071\nsage: hash(long(z))\n-131071\n```\n\n\nThis causes problems with looking up values in hashtables...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4957\n\n",
    "created_at": "2009-01-09T02:26:00Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "title": "inconsistent integer hashing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4957",
    "user": "robertwb"
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

archive/issue_comments_037677.json:
```json
{
    "body": "This was **ugly**. It turns out that we were shifting an `int` to the right by 45 bits on a 32 bit machine, which one might think would result in zero, but in fact shifts to the right by `(45%32) = 13` bits.\n\nThe attached patch fixes this, and adds some doctests.",
    "created_at": "2009-01-23T12:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37677",
    "user": "craigcitro"
}
```

This was **ugly**. It turns out that we were shifting an `int` to the right by 45 bits on a 32 bit machine, which one might think would result in zero, but in fact shifts to the right by `(45%32) = 13` bits.

The attached patch fixes this, and adds some doctests.



---

archive/issue_comments_037678.json:
```json
{
    "body": "Changing assignee from somebody to craigcitro.",
    "created_at": "2009-01-23T12:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37678",
    "user": "craigcitro"
}
```

Changing assignee from somebody to craigcitro.



---

archive/issue_comments_037679.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T12:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37679",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037680.json:
```json
{
    "body": "Excellent. I haven't been able to break it, and the code (and comment) look good.",
    "created_at": "2009-01-23T13:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37680",
    "user": "robertwb"
}
```

Excellent. I haven't been able to break it, and the code (and comment) look good.



---

archive/issue_comments_037681.json:
```json
{
    "body": "This is broken on 64 bit linux:\n\n```\nsage -t -long \"devel/sage/sage/rings/integer.pyx\"           \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx\", line 2085:\n    sage: n = -920390823904823094890238490238484; n.__hash__()\nExpected:\n    6874330978542788722   \nGot:\n    6917515397235318898\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx\", line 2101:\n    sage: hash(n)\nExpected:\n    -9223372036854767616      \nGot:\n    8192\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx\", line 2104:\n    sage: hash(n) == hash(int(n))\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n",
    "created_at": "2009-01-24T14:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37681",
    "user": "mabshoff"
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

archive/issue_comments_037682.json:
```json
{
    "body": "Darn :(. The first two may be OK (we need to see what hash(int(n)) is, but the second one is a problem.",
    "created_at": "2009-01-24T21:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37682",
    "user": "robertwb"
}
```

Darn :(. The first two may be OK (we need to see what hash(int(n)) is, but the second one is a problem.



---

archive/issue_comments_037683.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-24T23:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37683",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_037684.json:
```json
{
    "body": "Ok, I fixed it. It turns out it was some sloppy C coding on my part: I really wanted `sizeof(mp_limb_t)` instead of `sizeof(int)`.",
    "created_at": "2009-01-24T23:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37684",
    "user": "craigcitro"
}
```

Ok, I fixed it. It turns out it was some sloppy C coding on my part: I really wanted `sizeof(mp_limb_t)` instead of `sizeof(int)`.



---

archive/issue_comments_037685.json:
```json
{
    "body": "I bet this is the right fix, could you re-run the tests on a 64 bit machine?",
    "created_at": "2009-01-24T23:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37685",
    "user": "robertwb"
}
```

I bet this is the right fix, could you re-run the tests on a 64 bit machine?



---

archive/issue_comments_037686.json:
```json
{
    "body": "That does the trick on sage.math",
    "created_at": "2009-01-24T23:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37686",
    "user": "robertwb"
}
```

That does the trick on sage.math



---

archive/issue_comments_037687.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T21:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37687",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_037688.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T21:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4957#issuecomment-37688",
    "user": "mabshoff"
}
```

Resolution: fixed
