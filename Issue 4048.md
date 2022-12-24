# Issue 4048: missing minpoly for GF(p)

archive/issues_004048.json:
```json
{
    "body": "Assignee: was\n\nNick Alexander reports in https://groups.google.com/group/sage-devel/browse_thread/thread/e5538e40d2b89002\n\n```\nsage: GF(241^2, 'a')(1).minpoly() \nx + 240 \nsage: GF(241, 'a')(1).minpoly() \n--------------------------------------------------------------------------- \nAttributeError                            Traceback (most recent call   \nlast) \n... \nAttributeError: 'sage.rings.integer_mod.IntegerMod_int' object has no   \nattribute 'minpoly' \n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4048\n\n",
    "created_at": "2008-09-03T17:43:18Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "missing minpoly for GF(p)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4048",
    "user": "mabshoff"
}
```
Assignee: was

Nick Alexander reports in https://groups.google.com/group/sage-devel/browse_thread/thread/e5538e40d2b89002

```
sage: GF(241^2, 'a')(1).minpoly() 
x + 240 
sage: GF(241, 'a')(1).minpoly() 
--------------------------------------------------------------------------- 
AttributeError                            Traceback (most recent call   
last) 
... 
AttributeError: 'sage.rings.integer_mod.IntegerMod_int' object has no   
attribute 'minpoly' 
```




Issue created by migration from https://trac.sagemath.org/ticket/4048





---

archive/issue_comments_029190.json:
```json
{
    "body": "Attachment [trac_4048.patch](tarball://root/attachments/some-uuid/ticket4048/trac_4048.patch) by AlexGhitza created at 2009-01-22 01:21:29",
    "created_at": "2009-01-22T01:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4048#issuecomment-29190",
    "user": "AlexGhitza"
}
```

Attachment [trac_4048.patch](tarball://root/attachments/some-uuid/ticket4048/trac_4048.patch) by AlexGhitza created at 2009-01-22 01:21:29



---

archive/issue_comments_029191.json:
```json
{
    "body": "See the attached patch.",
    "created_at": "2009-01-22T01:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4048#issuecomment-29191",
    "user": "AlexGhitza"
}
```

See the attached patch.



---

archive/issue_comments_029192.json:
```json
{
    "body": "works for me",
    "created_at": "2009-01-23T10:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4048#issuecomment-29192",
    "user": "boothby"
}
```

works for me



---

archive/issue_comments_029193.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T17:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4048#issuecomment-29193",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_029194.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T17:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4048#issuecomment-29194",
    "user": "mabshoff"
}
```

Resolution: fixed
