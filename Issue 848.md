# Issue 848: Using strings for infinity

archive/issues_000848.json:
```json
{
    "body": "Assignee: was\n\nsage/gsl/integration.pyx uses the strings 'inf' and '-inf' rather than the infinity element for its bounds. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/848\n\n",
    "created_at": "2007-10-11T09:02:45Z",
    "labels": [
        "numerical",
        "minor",
        "bug"
    ],
    "title": "Using strings for infinity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/848",
    "user": "robertwb"
}
```
Assignee: was

sage/gsl/integration.pyx uses the strings 'inf' and '-inf' rather than the infinity element for its bounds. 


Issue created by migration from https://trac.sagemath.org/ticket/848





---

archive/issue_comments_005248.json:
```json
{
    "body": "Attachment\n\nSee the attached patch.",
    "created_at": "2008-04-13T03:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/848#issuecomment-5248",
    "user": "AlexGhitza"
}
```

Attachment

See the attached patch.



---

archive/issue_comments_005249.json:
```json
{
    "body": "Looks good to me.  All tests in gsl/ pass.",
    "created_at": "2008-04-14T22:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/848#issuecomment-5249",
    "user": "mhansen"
}
```

Looks good to me.  All tests in gsl/ pass.



---

archive/issue_comments_005250.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T23:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/848#issuecomment-5250",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005251.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-14T23:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/848#issuecomment-5251",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5
