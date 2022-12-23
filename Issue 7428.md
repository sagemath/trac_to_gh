# Issue 7428: worksheets listed on published list only after they are republished, but not after initial publication

archive/issues_007428.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was\n\nWhen I try to publish a worksheet, it does not initially show up in the list of published worksheets.  To reproduce, on sagenb.org:\n\n1. Create a new worksheet\n2. Click the Publish tab\n3. Click \"Yes\"\n4. Click the \"Published\" link at the very top right to look at the list of published worksheets.\n\nThe worksheet you just published should be up at the top of this list, but it's not.  This is the bug.\n5. Navigate back to your worksheet\n6. Click the publish tab again\n7. Click \"Re-publish worksheet\"\n8. Again click \"Published\" to go to the list of published worksheets\n\nNow your worksheet is listed at the top of this list.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7428\n\n",
    "created_at": "2009-11-11T07:31:12Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "worksheets listed on published list only after they are republished, but not after initial publication",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7428",
    "user": "jason"
}
```
Assignee: boothby

CC:  was

When I try to publish a worksheet, it does not initially show up in the list of published worksheets.  To reproduce, on sagenb.org:

1. Create a new worksheet
2. Click the Publish tab
3. Click "Yes"
4. Click the "Published" link at the very top right to look at the list of published worksheets.

The worksheet you just published should be up at the top of this list, but it's not.  This is the bug.
5. Navigate back to your worksheet
6. Click the publish tab again
7. Click "Re-publish worksheet"
8. Again click "Published" to go to the list of published worksheets

Now your worksheet is listed at the top of this list.

Issue created by migration from https://trac.sagemath.org/ticket/7428





---

archive/issue_comments_062507.json:
```json
{
    "body": "The problem appears to be the \"Last Edited\" field.",
    "created_at": "2009-11-12T04:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7428#issuecomment-62507",
    "user": "mpatel"
}
```

The problem appears to be the "Last Edited" field.



---

archive/issue_comments_062508.json:
```json
{
    "body": "Attachment\n\nUpdate \"Last Edited\" field for newly published worksheets.  Apply to sagenb repo.",
    "created_at": "2009-11-12T09:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7428#issuecomment-62508",
    "user": "mpatel"
}
```

Attachment

Update "Last Edited" field for newly published worksheets.  Apply to sagenb repo.



---

archive/issue_comments_062509.json:
```json
{
    "body": "Attachment\n\nAdded Selenium test.  Apply only this patch to sagenb repo.",
    "created_at": "2009-11-12T14:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7428#issuecomment-62509",
    "user": "mpatel"
}
```

Attachment

Added Selenium test.  Apply only this patch to sagenb repo.



---

archive/issue_comments_062510.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-12T14:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7428#issuecomment-62510",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062511.json:
```json
{
    "body": "Feel free to bump the milestone back to 4.3.",
    "created_at": "2009-11-12T14:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7428#issuecomment-62511",
    "user": "mpatel"
}
```

Feel free to bump the milestone back to 4.3.



---

archive/issue_comments_062512.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-13T19:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7428#issuecomment-62512",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062513.json:
```json
{
    "body": "Patch and test work. Positive review.",
    "created_at": "2009-11-13T19:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7428#issuecomment-62513",
    "user": "timdumol"
}
```

Patch and test work. Positive review.



---

archive/issue_comments_062514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-08T05:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7428#issuecomment-62514",
    "user": "was"
}
```

Resolution: fixed
