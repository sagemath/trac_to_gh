# Issue 7704: bug in sparse matrix det

archive/issues_007704.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  spancratz\n\n\n```\nsage: matrix(ZZ,4,sparse=True).det()\n...\nTypeError: charpoly() takes at most 1 positional argument (2 given)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7704\n\n",
    "created_at": "2009-12-16T08:13:27Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "bug in sparse matrix det",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7704",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  spancratz


```
sage: matrix(ZZ,4,sparse=True).det()
...
TypeError: charpoly() takes at most 1 positional argument (2 given)
```


Issue created by migration from https://trac.sagemath.org/ticket/7704





---

archive/issue_comments_065999.json:
```json
{
    "body": "Attachment [trac_7704.patch](tarball://root/attachments/some-uuid/ticket7704/trac_7704.patch) by @williamstein created at 2009-12-16 08:34:24",
    "created_at": "2009-12-16T08:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7704#issuecomment-65999",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7704.patch](tarball://root/attachments/some-uuid/ticket7704/trac_7704.patch) by @williamstein created at 2009-12-16 08:34:24



---

archive/issue_comments_066000.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-16T08:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7704#issuecomment-66000",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066001.json:
```json
{
    "body": "Very minor cosmetic change to the method",
    "created_at": "2009-12-19T01:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7704#issuecomment-66001",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Very minor cosmetic change to the method



---

archive/issue_comments_066002.json:
```json
{
    "body": "Attachment [trac_7704b.patch](tarball://root/attachments/some-uuid/ticket7704/trac_7704b.patch) by spancratz created at 2009-12-19 01:13:59\n\nThe patch looks fine, and ``make test`` on my installation of SAGE 4.2.1 returns only one unrelated error, which I include for completeness:\n\n\n```\nsage -t  \"devel/sage/sage/plot/plot3d/tachyon.py\"\n```\n\n\n\n```\nFile \"/scratch/pancratz/sage-4.2.1/devel/sage/sage/plot/plot3d/tachyon.py\", line 297:\n    sage: os.system('rm ' + tempname)\nExpected:\n    0\nGot:\n    256\n```\n\n\nI have attached an additional patch which removes one unused local variable.\n\nSebastian",
    "created_at": "2009-12-19T01:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7704#issuecomment-66002",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_7704b.patch](tarball://root/attachments/some-uuid/ticket7704/trac_7704b.patch) by spancratz created at 2009-12-19 01:13:59

The patch looks fine, and ``make test`` on my installation of SAGE 4.2.1 returns only one unrelated error, which I include for completeness:


```
sage -t  "devel/sage/sage/plot/plot3d/tachyon.py"
```



```
File "/scratch/pancratz/sage-4.2.1/devel/sage/sage/plot/plot3d/tachyon.py", line 297:
    sage: os.system('rm ' + tempname)
Expected:
    0
Got:
    256
```


I have attached an additional patch which removes one unused local variable.

Sebastian



---

archive/issue_comments_066003.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-29T08:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7704#issuecomment-66003",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007921.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-01-03T21:32:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7704",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7704#event-7921"
}
```



---

archive/issue_comments_066004.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7704#issuecomment-66004",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
