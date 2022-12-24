# Issue 4273: Failure on Jordan form transformation matrices

archive/issues_004273.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason\n\nKeywords: jordan form, matrix\n\nGetting the change of basis matrix for Jordan forms fails if there are multiple blocks with the same eigenvalue, e.g.:\n\n```\nm = matrix(QQ,[[0,1,0], [0,0,0], [0,0,0]])\nm.jordan_form(base_ring=QQ, transformation=True) \n```\n\ngives \n\n```\nValueError: cannot compute the basis of the Jordan block of size 2 with eigenvalue 0\n```\n\nThis was reported on sage-support by Rob Beezer, subject line is: \"Transformation to Jordan form for tame 6x6 integer matrix\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/4273\n\n",
    "created_at": "2008-10-13T11:59:45Z",
    "labels": [
        "linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Failure on Jordan form transformation matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4273",
    "user": "mhampton"
}
```
Assignee: was

CC:  jason

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

archive/issue_comments_031195.json:
```json
{
    "body": "Changing assignee from was to mhampton.",
    "created_at": "2008-10-15T03:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31195",
    "user": "mhampton"
}
```

Changing assignee from was to mhampton.



---

archive/issue_comments_031196.json:
```json
{
    "body": "Attachment [trac-4273-jordan_form.patch](tarball://root/attachments/some-uuid/ticket4273/trac-4273-jordan_form.patch) by jason created at 2008-11-18 04:31:34",
    "created_at": "2008-11-18T04:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31196",
    "user": "jason"
}
```

Attachment [trac-4273-jordan_form.patch](tarball://root/attachments/some-uuid/ticket4273/trac-4273-jordan_form.patch) by jason created at 2008-11-18 04:31:34



---

archive/issue_comments_031197.json:
```json
{
    "body": "Tests pass in matrix2.pyx.",
    "created_at": "2008-11-18T04:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31197",
    "user": "jason"
}
```

Tests pass in matrix2.pyx.



---

archive/issue_comments_031198.json:
```json
{
    "body": "Changing assignee from mhampton to jason.",
    "created_at": "2008-11-18T04:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31198",
    "user": "jason"
}
```

Changing assignee from mhampton to jason.



---

archive/issue_comments_031199.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-18T04:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31199",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031200.json:
```json
{
    "body": "Seems to work very well.  I tested it on some tough random cases of size 12x12 to 30x30 and it seems correct, and reasonably fast.  Nice work.",
    "created_at": "2008-11-18T15:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31200",
    "user": "mhampton"
}
```

Seems to work very well.  I tested it on some tough random cases of size 12x12 to 30x30 and it seems correct, and reasonably fast.  Nice work.



---

archive/issue_comments_031201.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T08:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31201",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031202.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T08:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4273#issuecomment-31202",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha0
