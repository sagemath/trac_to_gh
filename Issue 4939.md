# Issue 4939: massive performance regression to primes_first_n

archive/issues_004939.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is a doctest in arith.py:\n\n```\n    This is very fast, because we leave the output as a PARI object:\n        sage: v = primes_first_n(10^6, leave_pari=True)\n        sage: len(v)\n```\n\nIn fact, the above is now way way slower than doing leave_pari=False!  So the doctest is blatantly wrong multiple times.   It also says:\n\n```\n        leave_pari -- bool (default: False) if True the returned list\n                    is a PARI list; this is *vastly* (10 times!)\n```\n\n\nOn sage.math it is not very fast, and also uses 1.5GB RAM, which is a major problem for doctesting this on my build farm, where some machines have only 1GB RAM.  Also, I don't think it is reasonable to require 1.5GB RAM for standard doctests.\n\n```\nwstein@sage:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: time v = primes_first_n(10^6,leave_pari=True)\nCPU times: user 24.42 s, sys: 0.63 s, total: 25.05 s\nWall time: 25.05 s\nsage: get_memory_usage()\n1454.27734375\n```\n\n| Sage Version 3.2.2, Release Date: 2008-12-18                       |\n| Type notebook() for the GUI, and license() for information.        |\nFor comparison:\n\n```\nwstein@sage:~/sage/devel/sage/sage/rings$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: time v = primes_first_n(10^6, leave_pari=False)\nCPU times: user 0.42 s, sys: 0.19 s, total: 0.61 s\nWall time: 0.61 s\nsage: get_memory_usage()\n927.67578125\n```\n\n| Sage Version 3.2.2, Release Date: 2008-12-18                       |\n| Type notebook() for the GUI, and license() for information.        |\nThe documentation also says:\n{{\nHowever, PARI integers are much different than                                      \nSAGE integers.  If you use this option the lower                                   \nbound must be 2.         \n}}}\nwhich is patently false now.\n\nAn easy fix is to get rid entirely of the leave_pari=True option.  It was only ever there because it used to be really fast.  But now it is 50% better. \n\nThe problem is also in prime_range:\n\n```\nsage: time w = prime_range(10^6)                                                                                                                     \nCPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s\nWall time: 0.03 s\nsage: time w = prime_range(10^6,leave_pari=True)\nCPU times: user 0.95 s, sys: 0.02 s, total: 0.97 s\nWall time: 0.97 s\n```\n\n\nThe easiest solution is to simply delete all this \"leave_pari\" stuff.  It's totally useless, bad from an api point of view, and gains only a little speed.  Writing code against this api that uses the option would be particularly stupid, since in the feature we could easily have a native prime_range that is way faster than pari's, hence code that tries to be clever would be slower.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4939\n\n",
    "created_at": "2009-01-05T02:16:50Z",
    "labels": [
        "component: number theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "massive performance regression to primes_first_n",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4939",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This is a doctest in arith.py:

```
    This is very fast, because we leave the output as a PARI object:
        sage: v = primes_first_n(10^6, leave_pari=True)
        sage: len(v)
```

In fact, the above is now way way slower than doing leave_pari=False!  So the doctest is blatantly wrong multiple times.   It also says:

```
        leave_pari -- bool (default: False) if True the returned list
                    is a PARI list; this is *vastly* (10 times!)
```


On sage.math it is not very fast, and also uses 1.5GB RAM, which is a major problem for doctesting this on my build farm, where some machines have only 1GB RAM.  Also, I don't think it is reasonable to require 1.5GB RAM for standard doctests.

```
wstein@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: time v = primes_first_n(10^6,leave_pari=True)
CPU times: user 24.42 s, sys: 0.63 s, total: 25.05 s
Wall time: 25.05 s
sage: get_memory_usage()
1454.27734375
```

| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
For comparison:

```
wstein@sage:~/sage/devel/sage/sage/rings$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: time v = primes_first_n(10^6, leave_pari=False)
CPU times: user 0.42 s, sys: 0.19 s, total: 0.61 s
Wall time: 0.61 s
sage: get_memory_usage()
927.67578125
```

| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
The documentation also says:
{{
However, PARI integers are much different than                                      
SAGE integers.  If you use this option the lower                                   
bound must be 2.         
}}}
which is patently false now.

An easy fix is to get rid entirely of the leave_pari=True option.  It was only ever there because it used to be really fast.  But now it is 50% better. 

The problem is also in prime_range:

```
sage: time w = prime_range(10^6)                                                                                                                     
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03 s
sage: time w = prime_range(10^6,leave_pari=True)
CPU times: user 0.95 s, sys: 0.02 s, total: 0.97 s
Wall time: 0.97 s
```


The easiest solution is to simply delete all this "leave_pari" stuff.  It's totally useless, bad from an api point of view, and gains only a little speed.  Writing code against this api that uses the option would be particularly stupid, since in the feature we could easily have a native prime_range that is way faster than pari's, hence code that tries to be clever would be slower.

Issue created by migration from https://trac.sagemath.org/ticket/4939





---

archive/issue_comments_037416.json:
```json
{
    "body": "Attachment [trac_4939.patch](tarball://root/attachments/some-uuid/ticket4939/trac_4939.patch) by @williamstein created at 2009-01-05 02:24:05",
    "created_at": "2009-01-05T02:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4939#issuecomment-37416",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4939.patch](tarball://root/attachments/some-uuid/ticket4939/trac_4939.patch) by @williamstein created at 2009-01-05 02:24:05



---

archive/issue_comments_037417.json:
```json
{
    "body": "Yep, looks good.",
    "created_at": "2009-01-05T04:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4939#issuecomment-37417",
    "user": "https://github.com/craigcitro"
}
```

Yep, looks good.



---

archive/issue_comments_037418.json:
```json
{
    "body": "Here's what is taking the time when leave_pari=True:\n\n```\nsage: time p=pari.prime_list(10^6)\nCPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s\nWall time: 0.09 s\nsage: len(p)\n1000000\nsage: time c=p[0:]\nCPU times: user 45.05 s, sys: 0.54 s, total: 45.59 s\nWall time: 46.20 s\nsage: time c=p\nCPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s\nWall time: 0.07 s\n```\n\nIf you were to change the line \n\n```\n   if leave_pari:\n        return v[m:]\n```\n\nto\n\n```\n   if leave_pari:\n        if m==0: \n              return v\n        return v[m:]\n```\n \nthen it would have been faster.  But as William said, this option seems not to be worth keeping anyway.",
    "created_at": "2009-01-05T09:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4939#issuecomment-37418",
    "user": "https://github.com/JohnCremona"
}
```

Here's what is taking the time when leave_pari=True:

```
sage: time p=pari.prime_list(10^6)
CPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s
Wall time: 0.09 s
sage: len(p)
1000000
sage: time c=p[0:]
CPU times: user 45.05 s, sys: 0.54 s, total: 45.59 s
Wall time: 46.20 s
sage: time c=p
CPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s
Wall time: 0.07 s
```

If you were to change the line 

```
   if leave_pari:
        return v[m:]
```

to

```
   if leave_pari:
        if m==0: 
              return v
        return v[m:]
```
 
then it would have been faster.  But as William said, this option seems not to be worth keeping anyway.



---

archive/issue_comments_037419.json:
```json
{
    "body": "I have opened #4941 to address the massive performance issue with pari list slicing.",
    "created_at": "2009-01-05T17:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4939#issuecomment-37419",
    "user": "https://github.com/williamstein"
}
```

I have opened #4941 to address the massive performance issue with pari list slicing.



---

archive/issue_comments_037420.json:
```json
{
    "body": "Merged in Sage 3.2.3.post-final\n\nCheers,\n\nMichael",
    "created_at": "2009-01-06T01:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4939#issuecomment-37420",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.post-final

Cheers,

Michael



---

archive/issue_comments_037421.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-06T01:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4939#issuecomment-37421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005182.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-06T01:53:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4939",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4939#event-5182"
}
```
