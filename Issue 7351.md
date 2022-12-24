# Issue 7351: optimize import of singular.py

archive/issues_007351.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb\n\n\n```\nI'm using sage -startuptime.\n\nThe singular interface also looks like a *major* culprit:\n\n              sage.interfaces.singular: 0.329 (sage.rings.ideal)\n               sage.structure.sequence: 0.000 (sage.interfaces.singular)\n\nLooking, I see that a *horrendously* time consuming function called \n\"generate_docstring_dictionary()\" is called whenever the file sage/interfaces/singular.py is imported.  This is completely pointless, and shouldn't happen until somebody actually tries to use the singular interface.  A few lines of code would immediately reduce the startup time of Sage by nearly a half second there. \n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7351\n\n",
    "created_at": "2009-10-29T22:56:33Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "optimize import of singular.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7351",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @robertwb


```
I'm using sage -startuptime.

The singular interface also looks like a *major* culprit:

              sage.interfaces.singular: 0.329 (sage.rings.ideal)
               sage.structure.sequence: 0.000 (sage.interfaces.singular)

Looking, I see that a *horrendously* time consuming function called 
"generate_docstring_dictionary()" is called whenever the file sage/interfaces/singular.py is imported.  This is completely pointless, and shouldn't happen until somebody actually tries to use the singular interface.  A few lines of code would immediately reduce the startup time of Sage by nearly a half second there. 

```


Issue created by migration from https://trac.sagemath.org/ticket/7351





---

archive/issue_comments_061582.json:
```json
{
    "body": "Attachment [singular_startup_time.patch](tarball://root/attachments/some-uuid/ticket7351/singular_startup_time.patch) by @malb created at 2009-11-18 13:01:41\n\nthis fixes the issue for me",
    "created_at": "2009-11-18T13:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7351#issuecomment-61582",
    "user": "@malb"
}
```

Attachment [singular_startup_time.patch](tarball://root/attachments/some-uuid/ticket7351/singular_startup_time.patch) by @malb created at 2009-11-18 13:01:41

this fixes the issue for me



---

archive/issue_comments_061583.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-18T13:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7351#issuecomment-61583",
    "user": "@malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061584.json:
```json
{
    "body": "Nice. Thanks!",
    "created_at": "2009-11-20T03:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7351#issuecomment-61584",
    "user": "@robertwb"
}
```

Nice. Thanks!



---

archive/issue_comments_061585.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-20T03:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7351#issuecomment-61585",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061586.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7351#issuecomment-61586",
    "user": "@mwhansen"
}
```

Resolution: fixed
