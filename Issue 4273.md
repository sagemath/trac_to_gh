# Issue 4273: Failure on Jordan form transformation matrices

archive/issues_004273.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout\n\nKeywords: jordan form, matrix\n\nGetting the change of basis matrix for Jordan forms fails if there are multiple blocks with the same eigenvalue, e.g.:\n\n```\nm = matrix(QQ,[[0,1,0], [0,0,0], [0,0,0]])\nm.jordan_form(base_ring=QQ, transformation=True) \n```\n\ngives \n\n```\nValueError: cannot compute the basis of the Jordan block of size 2 with eigenvalue 0\n```\n\nThis was reported on sage-support by Rob Beezer, subject line is: \"Transformation to Jordan form for tame 6x6 integer matrix\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/4273\n\n",
    "created_at": "2008-10-13T11:59:45Z",
    "labels": [
        "component: linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Failure on Jordan form transformation matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4273",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: @williamstein

CC:  @jasongrout

Keywords: jordan form, matrix

Getting the change of basis matrix for Jordan forms fails if there are multiple blocks with the same eigenvalue, e.g.:

```
m = matrix(QQ,[[0,1,0], [0,0,0], [0,0,0]])
m.jordan_form(base_ring=QQ, transformation=True) 
```

gives 

```
ValueError: cannot compute the basis of the Jordan block of size 2 with eigenvalue 0
```

This was reported on sage-support by Rob Beezer, subject line is: "Transformation to Jordan form for tame 6x6 integer matrix".

Issue created by migration from https://trac.sagemath.org/ticket/4273





---

archive/issue_comments_031133.json:
```json
{
    "body": "Changing assignee from @williamstein to mhampton.",
    "created_at": "2008-10-15T03:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31133",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from @williamstein to mhampton.



---

archive/issue_comments_031134.json:
```json
{
    "body": "Attachment [trac-4273-jordan_form.patch](tarball://root/attachments/some-uuid/ticket4273/trac-4273-jordan_form.patch) by @jasongrout created at 2008-11-18 04:31:34",
    "created_at": "2008-11-18T04:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31134",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-4273-jordan_form.patch](tarball://root/attachments/some-uuid/ticket4273/trac-4273-jordan_form.patch) by @jasongrout created at 2008-11-18 04:31:34



---

archive/issue_comments_031135.json:
```json
{
    "body": "Tests pass in matrix2.pyx.",
    "created_at": "2008-11-18T04:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31135",
    "user": "https://github.com/jasongrout"
}
```

Tests pass in matrix2.pyx.



---

archive/issue_comments_031136.json:
```json
{
    "body": "Changing assignee from mhampton to @jasongrout.",
    "created_at": "2008-11-18T04:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31136",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from mhampton to @jasongrout.



---

archive/issue_comments_031137.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-18T04:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31137",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031138.json:
```json
{
    "body": "Seems to work very well.  I tested it on some tough random cases of size 12x12 to 30x30 and it seems correct, and reasonably fast.  Nice work.",
    "created_at": "2008-11-18T15:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31138",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Seems to work very well.  I tested it on some tough random cases of size 12x12 to 30x30 and it seems correct, and reasonably fast.  Nice work.



---

archive/issue_comments_031139.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T08:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31139",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031140.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T08:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31140",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0
