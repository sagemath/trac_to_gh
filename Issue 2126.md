# Issue 2126: [with patch, needs review] small fixes to eisenstein_series_qexp()

archive/issues_002126.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThe attached patch fixes a small typo and adds a small clarification to the docstring (specifying which normalization of the Eisenstein series is returned).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2126\n\n",
    "created_at": "2008-02-09T09:41:48Z",
    "labels": [
        "modular forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, needs review] small fixes to eisenstein_series_qexp()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2126",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

The attached patch fixes a small typo and adds a small clarification to the docstring (specifying which normalization of the Eisenstein series is returned).


Issue created by migration from https://trac.sagemath.org/ticket/2126





---

archive/issue_comments_013942.json:
```json
{
    "body": "The last line should probably read\n\n\n```\nraise ValueError, \"-(2*k)/B_k (=%s) must be invertible in the %r\"%(a0inv, K) \n```\n\n\nrather than\n\n\n```\nraise ValueError, \"-(2*k)/B_k (=%s) must be invertible in the %s\"%(a0inv, K._repr_()) \n```\n\n\nOther than that, I approve.",
    "created_at": "2008-02-14T06:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2126#issuecomment-13942",
    "user": "robertwb"
}
```

The last line should probably read


```
raise ValueError, "-(2*k)/B_k (=%s) must be invertible in the %r"%(a0inv, K) 
```


rather than


```
raise ValueError, "-(2*k)/B_k (=%s) must be invertible in the %s"%(a0inv, K._repr_()) 
```


Other than that, I approve.



---

archive/issue_comments_013943.json:
```json
{
    "body": "Attachment [2126-eisenstein_series_qexp.patch](tarball://root/attachments/some-uuid/ticket2126/2126-eisenstein_series_qexp.patch) by AlexGhitza created at 2008-02-17 00:17:59\n\nI've incorporated Robert's suggested change and resubmitted the patch.",
    "created_at": "2008-02-17T00:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2126#issuecomment-13943",
    "user": "AlexGhitza"
}
```

Attachment [2126-eisenstein_series_qexp.patch](tarball://root/attachments/some-uuid/ticket2126/2126-eisenstein_series_qexp.patch) by AlexGhitza created at 2008-02-17 00:17:59

I've incorporated Robert's suggested change and resubmitted the patch.



---

archive/issue_comments_013944.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T21:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2126#issuecomment-13944",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013945.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T21:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2126#issuecomment-13945",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
