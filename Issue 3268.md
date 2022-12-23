# Issue 3268: Fix GAP interface

archive/issues_003268.json:
```json
{
    "body": "Assignee: was\n\nI might be wrong, but it looks like output isn't getting printed:\n\n\n```\n# From a pure GAP session:\nGAP4, Version: 4.4.10 of 02-Oct-2007, i686-apple-darwin9.2.2-gcc\ngap> g := Group((1,3,2),(2,4,3));\nGroup([ (1,3,2), (2,4,3) ])\ngap> Stabilizer(g,4);\nGroup([ (1,3,2) ])\ngap> \n\n# From a Sage session:\nsage: %gap\n\n  --> Switching to Gap <-- \n\n''\ngap: g := Group((1,3,2),(2,4,3));\n\ngap: Stabilizer(g,4);\n\ngap: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3268\n\n",
    "created_at": "2008-05-21T16:43:12Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "Fix GAP interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3268",
    "user": "rlm"
}
```
Assignee: was

I might be wrong, but it looks like output isn't getting printed:


```
# From a pure GAP session:
GAP4, Version: 4.4.10 of 02-Oct-2007, i686-apple-darwin9.2.2-gcc
gap> g := Group((1,3,2),(2,4,3));
Group([ (1,3,2), (2,4,3) ])
gap> Stabilizer(g,4);
Group([ (1,3,2) ])
gap> 

# From a Sage session:
sage: %gap

  --> Switching to Gap <-- 

''
gap: g := Group((1,3,2),(2,4,3));

gap: Stabilizer(g,4);

gap: 
```


Issue created by migration from https://trac.sagemath.org/ticket/3268





---

archive/issue_comments_022623.json:
```json
{
    "body": "This isn't just for Stabilizer(), since the group isn't printing either...",
    "created_at": "2008-05-25T06:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3268#issuecomment-22623",
    "user": "rlm"
}
```

This isn't just for Stabilizer(), since the group isn't printing either...



---

archive/issue_comments_022624.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-23T09:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3268#issuecomment-22624",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_022625.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2009-01-23T09:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3268#issuecomment-22625",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_022626.json:
```json
{
    "body": "Note that there is no good way to test this as you can't access the processed line as it's completely internal to the function.",
    "created_at": "2009-01-23T09:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3268#issuecomment-22626",
    "user": "mhansen"
}
```

Note that there is no good way to test this as you can't access the processed line as it's completely internal to the function.



---

archive/issue_comments_022627.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T09:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3268#issuecomment-22627",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022628.json:
```json
{
    "body": "Nice catch.",
    "created_at": "2009-01-23T22:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3268#issuecomment-22628",
    "user": "robertwb"
}
```

Nice catch.



---

archive/issue_comments_022629.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T23:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3268#issuecomment-22629",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022630.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T23:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3268#issuecomment-22630",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael
