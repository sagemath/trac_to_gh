# Issue 4247: plotting -- bug in text and pdf export

archive/issues_004247.json:
```json
{
    "body": "Assignee: was\n\nThis works:\n\n```\nsage: text(\"sage\", (0,0), rgbcolor=(0r,0r,0r)).save(SAGE_TMP + 'a.pdf')\n```\n\nbut this doesn't (big confusing traceback):\n\n```\nsage: text(\"sage\", (0,0), rgbcolor=(0,0,0)).save(SAGE_TMP + 'a.pdf')\n```\n\n\nThe fix will be to make sure text (or whatever) normalizes the rgb input\nparams to all be of type float. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4247\n\n",
    "created_at": "2008-10-06T21:25:32Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "plotting -- bug in text and pdf export",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4247",
    "user": "was"
}
```
Assignee: was

This works:

```
sage: text("sage", (0,0), rgbcolor=(0r,0r,0r)).save(SAGE_TMP + 'a.pdf')
```

but this doesn't (big confusing traceback):

```
sage: text("sage", (0,0), rgbcolor=(0,0,0)).save(SAGE_TMP + 'a.pdf')
```


The fix will be to make sure text (or whatever) normalizes the rgb input
params to all be of type float. 

Issue created by migration from https://trac.sagemath.org/ticket/4247





---

archive/issue_comments_030879.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-06T21:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4247#issuecomment-30879",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_030880.json:
```json
{
    "body": "Attachment\n\nApply only trac_4247.patch -- it is rebased against the latest plot.py.  Otherwise, it looks good to me.",
    "created_at": "2008-10-06T21:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4247#issuecomment-30880",
    "user": "mhansen"
}
```

Attachment

Apply only trac_4247.patch -- it is rebased against the latest plot.py.  Otherwise, it looks good to me.



---

archive/issue_comments_030881.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-07T23:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4247#issuecomment-30881",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030882.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha3",
    "created_at": "2008-10-07T23:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4247#issuecomment-30882",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha3
