# Issue 848: Using strings for infinity

archive/issues_000848.json:
```json
{
    "body": "Assignee: @williamstein\n\nsage/gsl/integration.pyx uses the strings 'inf' and '-inf' rather than the infinity element for its bounds. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/848\n\n",
    "created_at": "2007-10-11T09:02:45Z",
    "labels": [
        "component: numerical",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Using strings for infinity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/848",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

sage/gsl/integration.pyx uses the strings 'inf' and '-inf' rather than the infinity element for its bounds. 


Issue created by migration from https://trac.sagemath.org/ticket/848





---

archive/issue_comments_005232.json:
```json
{
    "body": "Attachment [848-gsl_infinity.patch](tarball://root/attachments/some-uuid/ticket848/848-gsl_infinity.patch) by @aghitza created at 2008-04-13 03:38:44\n\nSee the attached patch.",
    "created_at": "2008-04-13T03:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/848#issuecomment-5232",
    "user": "https://github.com/aghitza"
}
```

Attachment [848-gsl_infinity.patch](tarball://root/attachments/some-uuid/ticket848/848-gsl_infinity.patch) by @aghitza created at 2008-04-13 03:38:44

See the attached patch.



---

archive/issue_comments_005233.json:
```json
{
    "body": "Looks good to me.  All tests in gsl/ pass.",
    "created_at": "2008-04-14T22:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/848#issuecomment-5233",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  All tests in gsl/ pass.



---

archive/issue_comments_005234.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T23:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/848#issuecomment-5234",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005235.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-14T23:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/848#issuecomment-5235",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha5
