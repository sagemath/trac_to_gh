# Issue 2530: interact bug -- drop down menu default doesn't show default value

archive/issues_002530.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n@interact\ndef _(f = (33,[1..100])):\n    pass\n```\n\n\nThe drop down should be set to 33 but isn't. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2530\n\n",
    "created_at": "2008-03-15T06:28:46Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "interact bug -- drop down menu default doesn't show default value",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2530",
    "user": "was"
}
```
Assignee: boothby


```
@interact
def _(f = (33,[1..100])):
    pass
```


The drop down should be set to 33 but isn't. 


Issue created by migration from https://trac.sagemath.org/ticket/2530





---

archive/issue_comments_017254.json:
```json
{
    "body": "Attachment [sage-2530.patch](tarball://root/attachments/some-uuid/ticket2530/sage-2530.patch) by was created at 2008-03-15 07:45:11\n\nThe attached patch fixes some minor issues with selectors with interact:\n\n1. the default for a drop-down menu is now correct,\n\n2. buttons with strings are no longer have quotes,\n\n3. the default value for selectors is the actual value rather than the index into the list of values, which is much much more natural.",
    "created_at": "2008-03-15T07:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2530#issuecomment-17254",
    "user": "was"
}
```

Attachment [sage-2530.patch](tarball://root/attachments/some-uuid/ticket2530/sage-2530.patch) by was created at 2008-03-15 07:45:11

The attached patch fixes some minor issues with selectors with interact:

1. the default for a drop-down menu is now correct,

2. buttons with strings are no longer have quotes,

3. the default value for selectors is the actual value rather than the index into the list of values, which is much much more natural.



---

archive/issue_comments_017255.json:
```json
{
    "body": "I tested this, and it looks good to me.",
    "created_at": "2008-03-16T00:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2530#issuecomment-17255",
    "user": "TimothyClemans"
}
```

I tested this, and it looks good to me.



---

archive/issue_comments_017256.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T00:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2530#issuecomment-17256",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017257.json:
```json
{
    "body": "Merged in Sage 2.10.4.rc0",
    "created_at": "2008-03-16T00:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2530#issuecomment-17257",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.rc0



---

archive/issue_comments_017258.json:
```json
{
    "body": "Replying to [comment:2 TimothyClemans]:\n> I tested this, and it looks good to me.\n\nTimothy,\n\nfor the record: Please doctest patches you review and clearly indicate what you doctested, i.e. all of Sage, some subdirectory and so on. Applying this patch causes a doctest failure, see #2538.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T02:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2530#issuecomment-17258",
    "user": "mabshoff"
}
```

Replying to [comment:2 TimothyClemans]:
> I tested this, and it looks good to me.

Timothy,

for the record: Please doctest patches you review and clearly indicate what you doctested, i.e. all of Sage, some subdirectory and so on. Applying this patch causes a doctest failure, see #2538.

Cheers,

Michael
