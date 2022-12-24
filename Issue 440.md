# Issue 440: Integer.__index__() currently goes via a python long

archive/issues_000440.json:
```json
{
    "body": "Assignee: somebody\n\nCurrently `Integer.__index__()` goes via a python long. In most cases the result should be just a python int, and it should be much faster to go directly there.\n\nProbably the best way to implement this is to first call `mpz_size(x.value)` to check the size in words; if the size is one, then construct a python int directly; otherwise go to a long.\n\nEven better might be to write another version of `mpz_get_pylong` which can produce a python int when that's feasible, or a long if it's not.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/440\n\n",
    "created_at": "2007-08-18T18:25:28Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "Integer.__index__() currently goes via a python long",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/440",
    "user": "dmharvey"
}
```
Assignee: somebody

Currently `Integer.__index__()` goes via a python long. In most cases the result should be just a python int, and it should be much faster to go directly there.

Probably the best way to implement this is to first call `mpz_size(x.value)` to check the size in words; if the size is one, then construct a python int directly; otherwise go to a long.

Even better might be to write another version of `mpz_get_pylong` which can produce a python int when that's feasible, or a long if it's not.


Issue created by migration from https://trac.sagemath.org/ticket/440





---

archive/issue_comments_002202.json:
```json
{
    "body": "oops I forgot to mention the above comment is for sage 2.8",
    "created_at": "2007-08-18T18:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/440#issuecomment-2202",
    "user": "dmharvey"
}
```

oops I forgot to mention the above comment is for sage 2.8



---

archive/issue_comments_002203.json:
```json
{
    "body": "Here's a profile, on sage.math, sage 2.8.1:\n\n\n```\nsage: L = [None] * 10\nsage: index = Integer(5)\nsage: timeit x = L[index]\n1000000 loops, best of 3: 690 ns per loop\nsage: timeit x = L[index]\n1000000 loops, best of 3: 691 ns per loop\n```\n\n\nLet's see if we can do better than that...",
    "created_at": "2007-08-18T19:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/440#issuecomment-2203",
    "user": "dmharvey"
}
```

Here's a profile, on sage.math, sage 2.8.1:


```
sage: L = [None] * 10
sage: index = Integer(5)
sage: timeit x = L[index]
1000000 loops, best of 3: 690 ns per loop
sage: timeit x = L[index]
1000000 loops, best of 3: 691 ns per loop
```


Let's see if we can do better than that...



---

archive/issue_comments_002204.json:
```json
{
    "body": "I'm about to attach a patch for this, here is the new profile:\n\n\n```\nsage: L = [None] * 10\nsage: index = Integer(5)\nsage: timeit x = L[index]\n1000000 loops, best of 3: 331 ns per loop\n```\n",
    "created_at": "2007-08-18T20:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/440#issuecomment-2204",
    "user": "dmharvey"
}
```

I'm about to attach a patch for this, here is the new profile:


```
sage: L = [None] * 10
sage: index = Integer(5)
sage: timeit x = L[index]
1000000 loops, best of 3: 331 ns per loop
```




---

archive/issue_comments_002205.json:
```json
{
    "body": "Attachment [trac-440.hg](tarball://root/attachments/some-uuid/ticket440/trac-440.hg) by dmharvey created at 2007-08-18 20:18:09\n\nadds new mpz_get_pyintlong function, change some calls in Integer class to use this function",
    "created_at": "2007-08-18T20:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/440#issuecomment-2205",
    "user": "dmharvey"
}
```

Attachment [trac-440.hg](tarball://root/attachments/some-uuid/ticket440/trac-440.hg) by dmharvey created at 2007-08-18 20:18:09

adds new mpz_get_pyintlong function, change some calls in Integer class to use this function



---

archive/issue_comments_002206.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T20:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/440#issuecomment-2206",
    "user": "was"
}
```

Resolution: fixed
