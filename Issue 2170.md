# Issue 2170: sage's integer.pyx digits function sucks in the base 10 case

archive/issues_002170.json:
```json
{
    "body": "Assignee: somebody\n\nThe digits function should be rewritten to have a special\ncase in the base 10 case, since as illustrated below\nit is currently **WAY** slower than just doing str(...) on \nthe input number!\n\n\n```\nsage: a = 3^100000\nsage: time w = a.digits(base=10)\nCPU times: user 1.00 s, sys: 0.01 s, total: 1.01 s\nWall time: 1.01\nsage: time v = list(reversed(str(a)))\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.02\nsage: v[:10]\n['1', '0', '0', '0', '0', '0', '2', '2', '5', '5']\nsage: w[:10]\n[1, 0, 0, 0, 0, 0, 2, 2, 5, 5]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2170\n\n",
    "created_at": "2008-02-15T07:59:32Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "sage's integer.pyx digits function sucks in the base 10 case",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2170",
    "user": "was"
}
```
Assignee: somebody

The digits function should be rewritten to have a special
case in the base 10 case, since as illustrated below
it is currently **WAY** slower than just doing str(...) on 
the input number!


```
sage: a = 3^100000
sage: time w = a.digits(base=10)
CPU times: user 1.00 s, sys: 0.01 s, total: 1.01 s
Wall time: 1.01
sage: time v = list(reversed(str(a)))
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02
sage: v[:10]
['1', '0', '0', '0', '0', '0', '2', '2', '5', '5']
sage: w[:10]
[1, 0, 0, 0, 0, 0, 2, 2, 5, 5]
```



Issue created by migration from https://trac.sagemath.org/ticket/2170





---

archive/issue_comments_014236.json:
```json
{
    "body": "Together with Laurent Imbert, we propose the attached patch. This solves the case where\nthe base is >= 10.\n\n```\nsage: a = 3^100000\nsage: time w = a.digits(base=10)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.01\n```\n",
    "created_at": "2008-02-15T13:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14236",
    "user": "zimmerma"
}
```

Together with Laurent Imbert, we propose the attached patch. This solves the case where
the base is >= 10.

```
sage: a = 3^100000
sage: time w = a.digits(base=10)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.01
```




---

archive/issue_comments_014237.json:
```json
{
    "body": "Attachment [8312.patch](tarball://root/attachments/some-uuid/ticket2170/8312.patch) by zimmerma created at 2008-02-15 13:56:15",
    "created_at": "2008-02-15T13:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14237",
    "user": "zimmerma"
}
```

Attachment [8312.patch](tarball://root/attachments/some-uuid/ticket2170/8312.patch) by zimmerma created at 2008-02-15 13:56:15



---

archive/issue_comments_014238.json:
```json
{
    "body": "REVIEW: The patch needs to be changed to only use the mpz string trick when the base is  small enough to work with GMP.   Right now we have:\n\nBefore patch:\n\n```\nsage: a = 9939082340\nsage: a.digits(512)\n[100, 302, 26, 74]\n```\n\n\nAfter patch:\n\n```\nsage: a = 9939082340\nsage: a.digits(10)\n['0', '4', '3', '2', '8', '0', '9', '3', '9', '9']\nsage: a.digits(32)\n['4', '3', 'n', 'k', '6', '8', '9']\nsage: a.digits(62)\n['g', 'L', 'N', 'd', 'q', 'A']\nsage: a.digits(63)\n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n",
    "created_at": "2008-02-15T16:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14238",
    "user": "was"
}
```

REVIEW: The patch needs to be changed to only use the mpz string trick when the base is  small enough to work with GMP.   Right now we have:

Before patch:

```
sage: a = 9939082340
sage: a.digits(512)
[100, 302, 26, 74]
```


After patch:

```
sage: a = 9939082340
sage: a.digits(10)
['0', '4', '3', '2', '8', '0', '9', '3', '9', '9']
sage: a.digits(32)
['4', '3', 'n', 'k', '6', '8', '9']
sage: a.digits(62)
['g', 'L', 'N', 'd', 'q', 'A']
sage: a.digits(63)
------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```




---

archive/issue_comments_014239.json:
```json
{
    "body": "\n```\nl = <object> PyString_FromString(str_out) \n```\n\n\ncould simply read \n\n\n```\nl = str_out\n```\n\n\nand Cython will do the string conversion for you. This looks like it was copied from `Integer.str()` and should be changed there as well. \n\nIt certainly needs to be fixed to handle the base > 62 case, and this patch changes the semantics of the function as well, so I don't think it should be applied as is.",
    "created_at": "2008-02-19T19:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14239",
    "user": "robertwb"
}
```


```
l = <object> PyString_FromString(str_out) 
```


could simply read 


```
l = str_out
```


and Cython will do the string conversion for you. This looks like it was copied from `Integer.str()` and should be changed there as well. 

It certainly needs to be fixed to handle the base > 62 case, and this patch changes the semantics of the function as well, so I don't think it should be applied as is.



---

archive/issue_comments_014240.json:
```json
{
    "body": "Attachment [8312.2.patch](tarball://root/attachments/some-uuid/ticket2170/8312.2.patch) by zimmerma created at 2008-02-25 14:18:47\n\nAttached is a revised patch, fixing the issues reported by the reviewers (whom we thank):\n\n```\nsage: a = 9939082340\nsage: a.digits(512)\n[100, 302, 26, 74]\nsage: a.digits(10)\n[0, 4, 3, 2, 8, 0, 9, 3, 9, 9]\nsage: a = 3^100000\nsage: time w = a.digits(base=10)\nCPU times: user 0.12 s, sys: 0.00 s, total: 0.12 s\nWall time: 0.11\nsage: w[:10]\n[1, 0, 0, 0, 0, 0, 2, 2, 5, 5]\n```\n\nWe also made the change suggested by Robert (in Integer.str() too).\nThe new digits() function is faster for 10 <= base <= 62, but not as fast as in the 1st (wrong)\npatch; the bottleneck seems to be the map(make_integer, l) call.",
    "created_at": "2008-02-25T14:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14240",
    "user": "zimmerma"
}
```

Attachment [8312.2.patch](tarball://root/attachments/some-uuid/ticket2170/8312.2.patch) by zimmerma created at 2008-02-25 14:18:47

Attached is a revised patch, fixing the issues reported by the reviewers (whom we thank):

```
sage: a = 9939082340
sage: a.digits(512)
[100, 302, 26, 74]
sage: a.digits(10)
[0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
sage: a = 3^100000
sage: time w = a.digits(base=10)
CPU times: user 0.12 s, sys: 0.00 s, total: 0.12 s
Wall time: 0.11
sage: w[:10]
[1, 0, 0, 0, 0, 0, 2, 2, 5, 5]
```

We also made the change suggested by Robert (in Integer.str() too).
The new digits() function is faster for 10 <= base <= 62, but not as fast as in the 1st (wrong)
patch; the bottleneck seems to be the map(make_integer, l) call.



---

archive/issue_comments_014241.json:
```json
{
    "body": "> Attached is a revised patch,\n\nThis patch seems to be identical to the original patch.",
    "created_at": "2008-02-25T14:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14241",
    "user": "was"
}
```

> Attached is a revised patch,

This patch seems to be identical to the original patch.



---

archive/issue_comments_014242.json:
```json
{
    "body": "Attachment [8683.patch](tarball://root/attachments/some-uuid/ticket2170/8683.patch) by zimmerma created at 2008-02-25 16:32:56\n\n> This patch seems to be identical to the original patch.\n\nSorry for that. The new one (8683.patch) should be the correct one.",
    "created_at": "2008-02-25T16:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14242",
    "user": "zimmerma"
}
```

Attachment [8683.patch](tarball://root/attachments/some-uuid/ticket2170/8683.patch) by zimmerma created at 2008-02-25 16:32:56

> This patch seems to be identical to the original patch.

Sorry for that. The new one (8683.patch) should be the correct one.



---

archive/issue_comments_014243.json:
```json
{
    "body": "I applied 8312.patch and 8683.patch (in that order) to a vanilla 2.10.2.  I may be losing my mind, but it sure appears to me that the patched version is actually *slower* than 2.10.2.  I would also point out that there is no point in declaring 'l' as a 'cdef object' -- that's the cython default.    I also think that \" = PyList_New(0)\" allocates a python list that is never used (just overwritten later).\n\nAs to the original bug, it seems quite intrinsic to me that digits would be slower than str.  The digits method needs to create individual python objects for each and every digit, str does not.  There's a frikkin lot of memory allocation going on there.  With that in mind, I'm not at all convinced that the bug is even fixable at all.",
    "created_at": "2008-03-01T18:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14243",
    "user": "jbmohler"
}
```

I applied 8312.patch and 8683.patch (in that order) to a vanilla 2.10.2.  I may be losing my mind, but it sure appears to me that the patched version is actually *slower* than 2.10.2.  I would also point out that there is no point in declaring 'l' as a 'cdef object' -- that's the cython default.    I also think that " = PyList_New(0)" allocates a python list that is never used (just overwritten later).

As to the original bug, it seems quite intrinsic to me that digits would be slower than str.  The digits method needs to create individual python objects for each and every digit, str does not.  There's a frikkin lot of memory allocation going on there.  With that in mind, I'm not at all convinced that the bug is even fixable at all.



---

archive/issue_comments_014244.json:
```json
{
    "body": "Oh, I see, upon more reflection.  I see that my idea of \"big\" wasn't quite big enough.  Once, we have a really big number, this patch becomes effective.\n\nHere's what I observe for moderate numbers:\n\n```\n# vanilla 2.10.2\nsage: a = 28356982659^15\nsage: %timeit w = a.digits(base=10)\n10000 loops, best of 3: 67 \u00c2\u00b5s per loop\n```\n\n\n\n```\n# Patched version\nsage: a = 28356982659^15\nsage: %timeit w = a.digits(base=10)\n10000 loops, best of 3: 136 \u00c2\u00b5s per loop\n```\n\n\nI do see that my memory allocation comment is entirely incorrect though.  I'm still a bit disturbed though.  Why should we suddenly get slower at 63?  Can't we extract gmp's algorithm for larger bases?  Part of the reason for my questions is that I want to use the digits method for mpoly factoring and it has some issues with large bases.\n\nModulo my comments above about the variable 'l', I think this is a good patch for the moment and should be included.  I do think there is a better answer in the long-term for larger bases though.",
    "created_at": "2008-03-01T19:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14244",
    "user": "jbmohler"
}
```

Oh, I see, upon more reflection.  I see that my idea of "big" wasn't quite big enough.  Once, we have a really big number, this patch becomes effective.

Here's what I observe for moderate numbers:

```
# vanilla 2.10.2
sage: a = 28356982659^15
sage: %timeit w = a.digits(base=10)
10000 loops, best of 3: 67 Âµs per loop
```



```
# Patched version
sage: a = 28356982659^15
sage: %timeit w = a.digits(base=10)
10000 loops, best of 3: 136 Âµs per loop
```


I do see that my memory allocation comment is entirely incorrect though.  I'm still a bit disturbed though.  Why should we suddenly get slower at 63?  Can't we extract gmp's algorithm for larger bases?  Part of the reason for my questions is that I want to use the digits method for mpoly factoring and it has some issues with large bases.

Modulo my comments above about the variable 'l', I think this is a good patch for the moment and should be included.  I do think there is a better answer in the long-term for larger bases though.



---

archive/issue_comments_014245.json:
```json
{
    "body": "Well, I guess I should've waited to post the first two after I thought about this a bit more.  :)\n\nI now have some serious reservations about this patch:\n\n1)  It actually makes small cases slower.  (See above)\n\n2)  It doesn't handle negatives correctly (what is correct?) -- we need a doc-test to clarify intent here.\n\n\n```\nsage: n=-20385\nsage: n.digits(100)  # this is what used to occur with negatives\n[-85, -3, -2]\nsage: n.digits(10)  # the last zero comes from '-' in the string?\n[5, 8, 3, 0, 2, 0]\n```\n\n\n3)  The version that runs with a non-None digits parameter is still slow.\n\n4)  A big base (bigger than 62) is still slow.\n\n5)  I now have cold feet about the 'PyMem_Free'.  Shouldn't it be 'free' since presumably gmp allocated with 'malloc'?  Or, did we hack gmp?  Or, doesn't it matter?\n\nNow, this raises some questions in my mind.  What should happen with negatives when digits are specified?",
    "created_at": "2008-03-02T03:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14245",
    "user": "jbmohler"
}
```

Well, I guess I should've waited to post the first two after I thought about this a bit more.  :)

I now have some serious reservations about this patch:

1)  It actually makes small cases slower.  (See above)

2)  It doesn't handle negatives correctly (what is correct?) -- we need a doc-test to clarify intent here.


```
sage: n=-20385
sage: n.digits(100)  # this is what used to occur with negatives
[-85, -3, -2]
sage: n.digits(10)  # the last zero comes from '-' in the string?
[5, 8, 3, 0, 2, 0]
```


3)  The version that runs with a non-None digits parameter is still slow.

4)  A big base (bigger than 62) is still slow.

5)  I now have cold feet about the 'PyMem_Free'.  Shouldn't it be 'free' since presumably gmp allocated with 'malloc'?  Or, did we hack gmp?  Or, doesn't it matter?

Now, this raises some questions in my mind.  What should happen with negatives when digits are specified?



---

archive/issue_comments_014246.json:
```json
{
    "body": "With apologies to zimmerma and Laurent Imbert for stealing their thunder, I attached a patch to #2362 which fixes that bug and this bug.",
    "created_at": "2008-03-02T05:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14246",
    "user": "jbmohler"
}
```

With apologies to zimmerma and Laurent Imbert for stealing their thunder, I attached a patch to #2362 which fixes that bug and this bug.



---

archive/issue_comments_014247.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-03T19:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14247",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014248.json:
```json
{
    "body": "As Joel pointed out in IRC this ticket can be closed as fixed since his patches at #2363 [that have been merged] fix the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T19:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2170#issuecomment-14248",
    "user": "mabshoff"
}
```

As Joel pointed out in IRC this ticket can be closed as fixed since his patches at #2363 [that have been merged] fix the issue.

Cheers,

Michael
