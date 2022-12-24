# Issue 6560: docstring formatting issue from ticket #6332

archive/issues_006560.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  fwclarke\n\nThe patch `trac_6332.patch` at #6332 contains docstrings that aren't formatted properly:\n\n```\n164\t        -  ``var'' - the name used for the generator of the number fields (default 'a').\n203\t        -  ``var'' - the name used for the generator of the number fields (default 'a').\n246\t        -  ``var'' - the name used for the generator of the number fields (default 'a').\n```\n\nThese results in 3 warnings when building the HTML version of the reference manual.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6560\n\n",
    "created_at": "2009-07-19T16:37:27Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "docstring formatting issue from ticket #6332",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6560",
    "user": "mvngu"
}
```
Assignee: tbd

CC:  fwclarke

The patch `trac_6332.patch` at #6332 contains docstrings that aren't formatted properly:

```
164	        -  ``var'' - the name used for the generator of the number fields (default 'a').
203	        -  ``var'' - the name used for the generator of the number fields (default 'a').
246	        -  ``var'' - the name used for the generator of the number fields (default 'a').
```

These results in 3 warnings when building the HTML version of the reference manual.

Issue created by migration from https://trac.sagemath.org/ticket/6560





---

archive/issue_comments_053511.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-07-21T10:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6560#issuecomment-53511",
    "user": "mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_053512.json:
```json
{
    "body": "This is a duplicate of #6577.",
    "created_at": "2009-07-21T10:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6560#issuecomment-53512",
    "user": "mvngu"
}
```

This is a duplicate of #6577.
