# Issue 1055: Don't factor discriminant for quadratic number fields

archive/issues_001055.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe current implementation of quadratic number fields calculates the discriminant on initialization, which can be expensive and is unnecessary. \n\nElements are represented as a+b sqrt(D) / denom. I don't believe that we require D to be the discriminant, but this needs to be verified before a change is made. For efficiency reasons, it might be worth doing trial division to reduce squares of small prime powers from D, as smaller D yields faster arithmetic. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1055\n\n",
    "created_at": "2007-11-01T20:27:44Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "Don't factor discriminant for quadratic number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1055",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

The current implementation of quadratic number fields calculates the discriminant on initialization, which can be expensive and is unnecessary. 

Elements are represented as a+b sqrt(D) / denom. I don't believe that we require D to be the discriminant, but this needs to be verified before a change is made. For efficiency reasons, it might be worth doing trial division to reduce squares of small prime powers from D, as smaller D yields faster arithmetic. 


Issue created by migration from https://trac.sagemath.org/ticket/1055





---

archive/issue_comments_006395.json:
```json
{
    "body": "easy to fix?",
    "created_at": "2007-11-03T15:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1055#issuecomment-6395",
    "user": "https://github.com/williamstein"
}
```

easy to fix?



---

archive/issue_comments_006396.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-11-03T17:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1055#issuecomment-6396",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_006397.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-03T22:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1055#issuecomment-6397",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006398.json:
```json
{
    "body": "Attachment [1055-quad-nf.diff](tarball://root/attachments/some-uuid/ticket1055/1055-quad-nf.diff) by @robertwb created at 2007-11-03 22:17:38",
    "created_at": "2007-11-03T22:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1055#issuecomment-6398",
    "user": "https://github.com/robertwb"
}
```

Attachment [1055-quad-nf.diff](tarball://root/attachments/some-uuid/ticket1055/1055-quad-nf.diff) by @robertwb created at 2007-11-03 22:17:38



---

archive/issue_comments_006399.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T21:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1055#issuecomment-6399",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.12.rc0



---

archive/issue_comments_006400.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T21:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1055#issuecomment-6400",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
