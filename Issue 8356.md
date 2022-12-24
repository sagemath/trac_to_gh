# Issue 8356: python is configured with an unreconised option

archive/issues_008356.json:
```json
{
    "body": "Assignee: tbd\n\nWhen python is configured, it is showing the following warning:\n\n\n```\nconfigure: WARNING: unrecognized options: --without-libpng\n```\n\n\nIt would be good if when people update packages, they actually check things like the options. R recently had --without-iconv, despite that was no longer an option. \n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8356\n\n",
    "created_at": "2010-02-25T03:58:59Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "python is configured with an unreconised option",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8356",
    "user": "drkirkby"
}
```
Assignee: tbd

When python is configured, it is showing the following warning:


```
configure: WARNING: unrecognized options: --without-libpng
```


It would be good if when people update packages, they actually check things like the options. R recently had --without-iconv, despite that was no longer an option. 





Issue created by migration from https://trac.sagemath.org/ticket/8356





---

archive/issue_comments_074647.json:
```json
{
    "body": "If the issues at #7867 can be solved by some updates to python, which may be the case, then I'll fix this as part of the fixes for #7867. Otherwise, it will have to wait for someone else to do it. \n\nI'm dropping the priority of this, as the warning is harmless.",
    "created_at": "2010-02-25T04:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8356#issuecomment-74647",
    "user": "drkirkby"
}
```

If the issues at #7867 can be solved by some updates to python, which may be the case, then I'll fix this as part of the fixes for #7867. Otherwise, it will have to wait for someone else to do it. 

I'm dropping the priority of this, as the warning is harmless.



---

archive/issue_comments_074648.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-02-25T04:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8356#issuecomment-74648",
    "user": "drkirkby"
}
```

Changing priority from major to minor.



---

archive/issue_comments_074649.json:
```json
{
    "body": "Fixed by #8440.",
    "created_at": "2010-03-07T01:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8356#issuecomment-74649",
    "user": "mhansen"
}
```

Fixed by #8440.



---

archive/issue_comments_074650.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-07T01:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8356#issuecomment-74650",
    "user": "mhansen"
}
```

Resolution: fixed
