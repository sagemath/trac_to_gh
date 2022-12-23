# Issue 6872: #6596 follow-up: typo in docstring

archive/issues_006872.json:
```json
{
    "body": "Assignee: tba\n\nCC:  malb\n\nThis is a follow-up to #6596 to fix a typo introduced in a docstring.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6872\n\n",
    "created_at": "2009-09-03T05:28:35Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "title": "#6596 follow-up: typo in docstring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6872",
    "user": "mvngu"
}
```
Assignee: tba

CC:  malb

This is a follow-up to #6596 to fix a typo introduced in a docstring.

Issue created by migration from https://trac.sagemath.org/ticket/6872





---

archive/issue_comments_056740.json:
```json
{
    "body": "depends on #6596",
    "created_at": "2009-09-03T05:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6872#issuecomment-56740",
    "user": "mvngu"
}
```

depends on #6596



---

archive/issue_comments_056741.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-03T05:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6872#issuecomment-56741",
    "user": "mvngu"
}
```

Attachment



---

archive/issue_comments_056742.json:
```json
{
    "body": "I don't understand the reason for the change (because I didn't look at the produced HTML) but it is definitely fine.",
    "created_at": "2009-09-03T08:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6872#issuecomment-56742",
    "user": "malb"
}
```

I don't understand the reason for the change (because I didn't look at the produced HTML) but it is definitely fine.



---

archive/issue_comments_056743.json:
```json
{
    "body": "Attachment\n\nwithout the patch",
    "created_at": "2009-09-03T09:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6872#issuecomment-56743",
    "user": "mvngu"
}
```

Attachment

without the patch



---

archive/issue_comments_056744.json:
```json
{
    "body": "The module `sage/libs/singular/groebner_strategy.pyx` is currently not in the reference manual. After adding it to the reference manual and (re)building it, you get something like that shown in the screenshot `trac_6872-without-patch.png`. Notice the redundant colon \":\" after \"ALGORITHM\". Now supposing you leave \"ALGORITHM::\" alone and move \"Uses Singular via libSINGULAR\" to a new line. Building the reference manual would result in a warning:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/libs/singular/groebner_strategy.so:docstring of sage.libs.singular.groebner_strategy.GroebnerStrategy:8: (WARNING/2) Literal block expected; none found.\n```\n\nBut removing the redundant colon and the documentation builder is now happy. Hence the patch `trac_6872-fix-typo.patch`.",
    "created_at": "2009-09-03T09:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6872#issuecomment-56744",
    "user": "mvngu"
}
```

The module `sage/libs/singular/groebner_strategy.pyx` is currently not in the reference manual. After adding it to the reference manual and (re)building it, you get something like that shown in the screenshot `trac_6872-without-patch.png`. Notice the redundant colon ":" after "ALGORITHM". Now supposing you leave "ALGORITHM::" alone and move "Uses Singular via libSINGULAR" to a new line. Building the reference manual would result in a warning:

```
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/libs/singular/groebner_strategy.so:docstring of sage.libs.singular.groebner_strategy.GroebnerStrategy:8: (WARNING/2) Literal block expected; none found.
```

But removing the redundant colon and the documentation builder is now happy. Hence the patch `trac_6872-fix-typo.patch`.



---

archive/issue_comments_056745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-03T09:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6872#issuecomment-56745",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056746.json:
```json
{
    "body": "Thanks, very well explained!",
    "created_at": "2009-09-03T11:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6872#issuecomment-56746",
    "user": "malb"
}
```

Thanks, very well explained!
