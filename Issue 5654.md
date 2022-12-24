# Issue 5654: [with patch, needs review] Boundary/interior points of vertices were computed wrong.

archive/issues_005654.json:
```json
{
    "body": "Assignee: mhampton\n\nThis is wrong:\n\n```\nsage: ReflexivePolytope(2,0).faces(dim=0)[0].nboundary_points()\n1\n```\n\nbecause vertices do not have boundary points. \n\nThe patch fixes the function that caused this error.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5654\n\n",
    "created_at": "2009-04-01T02:00:01Z",
    "labels": [
        "geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] Boundary/interior points of vertices were computed wrong.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5654",
    "user": "novoselt"
}
```
Assignee: mhampton

This is wrong:

```
sage: ReflexivePolytope(2,0).faces(dim=0)[0].nboundary_points()
1
```

because vertices do not have boundary points. 

The patch fixes the function that caused this error.

Issue created by migration from https://trac.sagemath.org/ticket/5654





---

archive/issue_comments_044221.json:
```json
{
    "body": "Attachment [11804.patch](tarball://root/attachments/some-uuid/ticket5654/11804.patch) by mhampton created at 2009-04-13 19:21:40\n\nThis passes doctests, and is a simple change that makes sense to me.",
    "created_at": "2009-04-13T19:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5654#issuecomment-44221",
    "user": "mhampton"
}
```

Attachment [11804.patch](tarball://root/attachments/some-uuid/ticket5654/11804.patch) by mhampton created at 2009-04-13 19:21:40

This passes doctests, and is a simple change that makes sense to me.



---

archive/issue_comments_044222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-15T00:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5654#issuecomment-44222",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044223.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T00:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5654#issuecomment-44223",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
