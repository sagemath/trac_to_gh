# Issue 5444: elipses + float = boom

archive/issues_005444.json:
```json
{
    "body": "Assignee: robertwb\n\n\n```\n   sage: [(1.0)..(2.0)]\n   [1.00000000000000, 2.00000000000000]\n   sage: [1.0..2.0]\n    line 4\n    (ellipsis_range(_sage_const_1p0 ,Ellipsis,_sage_const_2 RealNumber('.0')))\n                                                                     ^\nSyntaxError: invalid syntax\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5444\n\n",
    "created_at": "2009-03-05T19:58:26Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "elipses + float = boom",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5444",
    "user": "boothby"
}
```
Assignee: robertwb


```
   sage: [(1.0)..(2.0)]
   [1.00000000000000, 2.00000000000000]
   sage: [1.0..2.0]
    line 4
    (ellipsis_range(_sage_const_1p0 ,Ellipsis,_sage_const_2 RealNumber('.0')))
                                                                     ^
SyntaxError: invalid syntax
```


Issue created by migration from https://trac.sagemath.org/ticket/5444





---

archive/issue_comments_042093.json:
```json
{
    "body": "This has been resolved, probably while cleaning up the preparser code. \n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.4.2, Release Date: 2009-05-05                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: [1.0..2.0]\n [1.00000000000000, 2.00000000000000]\n\n```\n",
    "created_at": "2009-05-18T21:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5444#issuecomment-42093",
    "user": "robertwb"
}
```

This has been resolved, probably while cleaning up the preparser code. 


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.4.2, Release Date: 2009-05-05                       |
| Type notebook() for the GUI, and license() for information.        |
sage: [1.0..2.0]
 [1.00000000000000, 2.00000000000000]

```




---

archive/issue_comments_042094.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2009-05-18T21:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5444#issuecomment-42094",
    "user": "robertwb"
}
```

Resolution: worksforme



---

archive/issue_comments_042095.json:
```json
{
    "body": "Has a doctest been added? Otherwise this ticket should be reopened.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T22:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5444#issuecomment-42095",
    "user": "mabshoff"
}
```

Has a doctest been added? Otherwise this ticket should be reopened.

Cheers,

Michael



---

archive/issue_comments_042096.json:
```json
{
    "body": "Resolution changed from worksforme to ",
    "created_at": "2009-05-19T04:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5444#issuecomment-42096",
    "user": "mabshoff"
}
```

Resolution changed from worksforme to 



---

archive/issue_comments_042097.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-05-19T04:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5444#issuecomment-42097",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_042098.json:
```json
{
    "body": "Reopening until someone either points to a doctests or post a doctest patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T04:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5444#issuecomment-42098",
    "user": "mabshoff"
}
```

Reopening until someone either points to a doctests or post a doctest patch.

Cheers,

Michael



---

archive/issue_comments_042099.json:
```json
{
    "body": "Attachment [trac_5444.patch](tarball://root/attachments/some-uuid/ticket5444/trac_5444.patch) by mhansen created at 2009-06-05 01:28:54",
    "created_at": "2009-06-05T01:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5444#issuecomment-42099",
    "user": "mhansen"
}
```

Attachment [trac_5444.patch](tarball://root/attachments/some-uuid/ticket5444/trac_5444.patch) by mhansen created at 2009-06-05 01:28:54



---

archive/issue_comments_042100.json:
```json
{
    "body": "Doctest looks fine to me.",
    "created_at": "2009-06-05T03:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5444#issuecomment-42100",
    "user": "robertwb"
}
```

Doctest looks fine to me.



---

archive/issue_comments_042101.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5444#issuecomment-42101",
    "user": "ncalexan"
}
```

Resolution: fixed
