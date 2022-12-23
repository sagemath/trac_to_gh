# Issue 6952: follow-up to #6774: fix warnings and stylistic niceties

archive/issues_006952.json:
```json
{
    "body": "Assignee: tba\n\nCC:  ncohen jason\n\nThis is a follow-up to ticket #6774.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6952\n\n",
    "created_at": "2009-09-17T23:02:29Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "follow-up to #6774: fix warnings and stylistic niceties",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6952",
    "user": "mvngu"
}
```
Assignee: tba

CC:  ncohen jason

This is a follow-up to ticket #6774.

Issue created by migration from https://trac.sagemath.org/ticket/6952





---

archive/issue_comments_057491.json:
```json
{
    "body": "There's a warning when building the tutorial with the two patches at #6774:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/doc/en/tutorial/tour_graphtheory.rst:91: (WARNING/2) Title underline too short.\n\nCompute maximum matchings\n^^^^^^^^^^^^^^^^^^^\n```\n\nThere are also some stylistic errors that I'll take care of.",
    "created_at": "2009-09-17T23:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57491",
    "user": "mvngu"
}
```

There's a warning when building the tutorial with the two patches at #6774:

```
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/doc/en/tutorial/tour_graphtheory.rst:91: (WARNING/2) Title underline too short.

Compute maximum matchings
^^^^^^^^^^^^^^^^^^^
```

There are also some stylistic errors that I'll take care of.



---

archive/issue_comments_057492.json:
```json
{
    "body": "Attachment\n\ndepends on #6774",
    "created_at": "2009-09-17T23:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57492",
    "user": "mvngu"
}
```

Attachment

depends on #6774



---

archive/issue_comments_057493.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-09-17T23:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57493",
    "user": "mvngu"
}
```

Changing priority from major to minor.



---

archive/issue_comments_057494.json:
```json
{
    "body": "Thanks! I learned a few things about writing in ReST from your patch.  I won't make those mistakes again (like enumerated lists).\n\nThis applied and looks fine.\n\nI assume you merged the necessary patches to make the functions in these examples work.  They did not work for me with a copy of 4.1.1.alpha1.  So doctests really ought to be run on this file just to make sure that the examples are correct.",
    "created_at": "2009-09-19T02:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57494",
    "user": "jason"
}
```

Thanks! I learned a few things about writing in ReST from your patch.  I won't make those mistakes again (like enumerated lists).

This applied and looks fine.

I assume you merged the necessary patches to make the functions in these examples work.  They did not work for me with a copy of 4.1.1.alpha1.  So doctests really ought to be run on this file just to make sure that the examples are correct.



---

archive/issue_comments_057495.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-19T19:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57495",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057496.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> I assume you merged the necessary patches to make the functions in these examples work. \nYes, I tried that.\n\n\n\n\n> So doctests really ought to be run on this file just to make sure that the examples are correct.\nWith other dependencies and this patch, all doctests in the tutorial pass.",
    "created_at": "2009-09-19T19:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57496",
    "user": "mvngu"
}
```

Replying to [comment:3 jason]:
> I assume you merged the necessary patches to make the functions in these examples work. 
Yes, I tried that.




> So doctests really ought to be run on this file just to make sure that the examples are correct.
With other dependencies and this patch, all doctests in the tutorial pass.
