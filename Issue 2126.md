# Issue 2126: [with patch, with positive review] small fixes to eisenstein_series_qexp()

archive/issues_002126.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe attached patch fixes a small typo and adds a small clarification to the docstring (specifying which normalization of the Eisenstein series is returned).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2126\n\n",
    "closed_at": "2008-02-17T21:28:03Z",
    "created_at": "2008-02-09T09:41:48Z",
    "labels": [
        "component: modular forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, with positive review] small fixes to eisenstein_series_qexp()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2126",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

The attached patch fixes a small typo and adds a small clarification to the docstring (specifying which normalization of the Eisenstein series is returned).


Issue created by migration from https://trac.sagemath.org/ticket/2126





---

archive/issue_comments_013911.json:
```json
{
    "body": "The last line should probably read\n\n```\nraise ValueError, \"-(2*k)/B_k (=%s) must be invertible in the %r\"%(a0inv, K) \n```\n\nrather than\n\n```\nraise ValueError, \"-(2*k)/B_k (=%s) must be invertible in the %s\"%(a0inv, K._repr_()) \n```\n\nOther than that, I approve.",
    "created_at": "2008-02-14T06:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2126#issuecomment-13911",
    "user": "https://github.com/robertwb"
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

archive/issue_comments_013912.json:
```json
{
    "body": "Attachment [2126-eisenstein_series_qexp.patch](tarball://root/attachments/some-uuid/ticket2126/2126-eisenstein_series_qexp.patch) by @aghitza created at 2008-02-17 00:17:59\n\nI've incorporated Robert's suggested change and resubmitted the patch.",
    "created_at": "2008-02-17T00:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2126#issuecomment-13912",
    "user": "https://github.com/aghitza"
}
```

Attachment [2126-eisenstein_series_qexp.patch](tarball://root/attachments/some-uuid/ticket2126/2126-eisenstein_series_qexp.patch) by @aghitza created at 2008-02-17 00:17:59

I've incorporated Robert's suggested change and resubmitted the patch.



---

archive/issue_comments_013913.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T21:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2126#issuecomment-13913",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005095.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-17T21:28:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2126",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2126#event-5095"
}
```



---

archive/issue_comments_013914.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T21:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2126#issuecomment-13914",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
