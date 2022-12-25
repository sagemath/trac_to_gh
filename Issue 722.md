# Issue 722: GF(100) gives weird error message

archive/issues_000722.json:
```json
{
    "body": "Assignee: somebody\n\n```\nsage: GF(100)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/dmharvey/<ipython console> in <module>()\n\n/home/was/s/local/lib/python2.5/site-packages/sage/rings/finite_field.py in FiniteField(order, name, modulus, names, elem_cache, check_irreducible, *args, **kwds)\n    184                 raise ValueError, \"finite field modulus must be irreducible but it is not\"\n    185         if name is None:\n--> 186             raise TypeError, \"you must specify the generator name\"\n    187         if order < 2**16:  \n    188             # DO *NOT* use for prime subfield, since that would lead to\n\n<type 'exceptions.TypeError'>: you must specify the generator name\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/722\n\n",
    "created_at": "2007-09-20T23:01:00Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5.1",
    "title": "GF(100) gives weird error message",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/722",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

```
sage: GF(100)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/dmharvey/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/rings/finite_field.py in FiniteField(order, name, modulus, names, elem_cache, check_irreducible, *args, **kwds)
    184                 raise ValueError, "finite field modulus must be irreducible but it is not"
    185         if name is None:
--> 186             raise TypeError, "you must specify the generator name"
    187         if order < 2**16:  
    188             # DO *NOT* use for prime subfield, since that would lead to

<type 'exceptions.TypeError'>: you must specify the generator name
```


Issue created by migration from https://trac.sagemath.org/ticket/722





---

archive/issue_events_001957.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-23T10:33:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/722",
    "milestone": "sage-2.8.5.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/722#event-1957"
}
```



---

archive/issue_comments_004193.json:
```json
{
    "body": "This happens because of the order of the checks in GF.  See below:\n\n```\nsage: GF(13)\nFinite Field of size 13\n\nsage: GF(2^5)\nTraceback (most recent call last):\n...\nTypeError: you must specify the generator name\n\nsage: GF(2^5, 'a')\nFinite Field in a of size 2^5\nsage: GF(12)\nTraceback (most recent call last):\n...\nTypeError: you must specify the generator name\n\nsage: GF(12, 'a')\nTraceback (most recent call last):\n...\nArithmeticError: q must be a prime power\n\n\n```\n\nI guess it's a matter of deciding which of the two errors should come up first.",
    "created_at": "2007-09-23T19:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/722#issuecomment-4193",
    "user": "https://github.com/mwhansen"
}
```

This happens because of the order of the checks in GF.  See below:

```
sage: GF(13)
Finite Field of size 13

sage: GF(2^5)
Traceback (most recent call last):
...
TypeError: you must specify the generator name

sage: GF(2^5, 'a')
Finite Field in a of size 2^5
sage: GF(12)
Traceback (most recent call last):
...
TypeError: you must specify the generator name

sage: GF(12, 'a')
Traceback (most recent call last):
...
ArithmeticError: q must be a prime power


```

I guess it's a matter of deciding which of the two errors should come up first.



---

archive/issue_comments_004194.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-09-23T21:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/722#issuecomment-4194",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to minor.



---

archive/issue_comments_004195.json:
```json
{
    "body": "Attachment [6516.patch](tarball://root/attachments/some-uuid/ticket722/6516.patch) by @williamstein created at 2007-09-25 06:33:35",
    "created_at": "2007-09-25T06:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/722#issuecomment-4195",
    "user": "https://github.com/williamstein"
}
```

Attachment [6516.patch](tarball://root/attachments/some-uuid/ticket722/6516.patch) by @williamstein created at 2007-09-25 06:33:35



---

archive/issue_comments_004196.json:
```json
{
    "body": "fixed.",
    "created_at": "2007-09-25T06:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/722#issuecomment-4196",
    "user": "https://github.com/williamstein"
}
```

fixed.



---

archive/issue_events_001958.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-25T06:33:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/722",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/722#event-1958"
}
```



---

archive/issue_comments_004197.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-25T06:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/722#issuecomment-4197",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
