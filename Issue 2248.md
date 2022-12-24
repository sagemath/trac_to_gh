# Issue 2248: [with patch, needs trivial review] sage-2.10.2.alpha2: multi_polynomial.pyx doctest failure

archive/issues_002248.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nsage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx\n**********************************************************************\nFile \"multi_polynomial.pyx\", line 256:\n    sage: R(S.0)\nExpected:\n    BROKEN -- FIX ME\nGot:\n    p\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2248\n\n",
    "created_at": "2008-02-21T19:01:42Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "[with patch, needs trivial review] sage-2.10.2.alpha2: multi_polynomial.pyx doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2248",
    "user": "mabshoff"
}
```
Assignee: failure


```
sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx
**********************************************************************
File "multi_polynomial.pyx", line 256:
    sage: R(S.0)
Expected:
    BROKEN -- FIX ME
Got:
    p
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/2248





---

archive/issue_comments_014900.json:
```json
{
    "body": "fixed the failure as suggested by William",
    "created_at": "2008-02-21T19:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2248#issuecomment-14900",
    "user": "mabshoff"
}
```

fixed the failure as suggested by William



---

archive/issue_comments_014901.json:
```json
{
    "body": "Attachment [trac_2248.patch](tarball://root/attachments/some-uuid/ticket2248/trac_2248.patch) by was created at 2008-02-21 19:21:23",
    "created_at": "2008-02-21T19:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2248#issuecomment-14901",
    "user": "was"
}
```

Attachment [trac_2248.patch](tarball://root/attachments/some-uuid/ticket2248/trac_2248.patch) by was created at 2008-02-21 19:21:23



---

archive/issue_comments_014902.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-21T19:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2248#issuecomment-14902",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.rc0



---

archive/issue_comments_014903.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T19:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2248#issuecomment-14903",
    "user": "mabshoff"
}
```

Resolution: fixed
