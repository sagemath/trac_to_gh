# Issue 4683: memory leak when performing the calculation CDF(I)^2

archive/issues_004683.json:
```json
{
    "body": "Assignee: somebody\n\nUsing sage 3.2 (compiled from sources) on a 32-bit Core Duo machine running Debian Etch,\nwhen performing\n\n```\ngeorg@HILBERT:~/Daten/Sync/Phd/Code/sde$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2, Release Date: 2008-11-20                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: v = [CDF(i)^2 for n in range(50000)]\n```\n\nmemory consumption increases about 70Mb which each command (at least on my machine),\nthis does not happen if one writes\n\n```\nsage: v = [CDF(i^2.) for n in range(50000)]\n```\n\n, however, results are the same,\n\nGeorg\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4683\n\n",
    "created_at": "2008-12-03T01:12:51Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "memory leak when performing the calculation CDF(I)^2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4683",
    "user": "ggrafendorfer"
}
```
Assignee: somebody

Using sage 3.2 (compiled from sources) on a 32-bit Core Duo machine running Debian Etch,
when performing

```
georg@HILBERT:~/Daten/Sync/Phd/Code/sde$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2, Release Date: 2008-11-20                         |
| Type notebook() for the GUI, and license() for information.        |
sage: v = [CDF(i)^2 for n in range(50000)]
sage: v = [CDF(i)^2 for n in range(50000)]
sage: v = [CDF(i)^2 for n in range(50000)]
```

memory consumption increases about 70Mb which each command (at least on my machine),
this does not happen if one writes

```
sage: v = [CDF(i^2.) for n in range(50000)]
```

, however, results are the same,

Georg


Issue created by migration from https://trac.sagemath.org/ticket/4683





---

archive/issue_comments_035300.json:
```json
{
    "body": "Hi Georg,\n\nthis looks like a dupe of #4639.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T01:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4683#issuecomment-35300",
    "user": "mabshoff"
}
```

Hi Georg,

this looks like a dupe of #4639.

Cheers,

Michael



---

archive/issue_comments_035301.json:
```json
{
    "body": "A yes, probably, I'm sorry, did not look ...\nGeorg",
    "created_at": "2008-12-03T01:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4683#issuecomment-35301",
    "user": "ggrafendorfer"
}
```

A yes, probably, I'm sorry, did not look ...
Georg



---

archive/issue_comments_035302.json:
```json
{
    "body": "#4639 fixes the vast majority of the problem here, but:\n\n```\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n421.88671875\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n422.140625\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n422.15234375\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n422.40625\n```\n\nSo still some small leak to go. I will poke around post 3.2.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T04:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4683#issuecomment-35302",
    "user": "mabshoff"
}
```

#4639 fixes the vast majority of the problem here, but:

```
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
421.88671875
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
422.140625
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
422.15234375
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
422.40625
```

So still some small leak to go. I will poke around post 3.2.2.

Cheers,

Michael



---

archive/issue_comments_035303.json:
```json
{
    "body": "Hmmm:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n134.1328125\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n136.578125\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n136.7734375\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n136.7734375\nsage: get_memory_usage()\n136.7734375\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n136.7734375\n```\n",
    "created_at": "2009-06-03T07:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4683#issuecomment-35303",
    "user": "AlexGhitza"
}
```

Hmmm:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
134.1328125
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
136.578125
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
136.7734375
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
136.7734375
sage: get_memory_usage()
136.7734375
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
136.7734375
```




---

archive/issue_comments_035304.json:
```json
{
    "body": "I don't see any growth in memory usage anymore either. I guess we can safely close it.",
    "created_at": "2010-01-17T23:19:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4683#issuecomment-35304",
    "user": "wjp"
}
```

I don't see any growth in memory usage anymore either. I guess we can safely close it.



---

archive/issue_comments_035305.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-17T23:19:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4683#issuecomment-35305",
    "user": "wjp"
}
```

Resolution: fixed
