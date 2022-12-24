# Issue 6069: Blank notebook page when loading URL for published sheet that is AWOL

archive/issues_006069.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  acleone robert.marik\n\nIf someone attempts to access a URL for a published worksheet that no longer exists (perhaps because the URL changed when the worksheet went through a published to unpublished to published cycle), or the URL was mistyped, they get a blank page titled \"Error | Sage Notebook\", with no hint on what to do to resolve the problem.\n\nIf they are trying to access a published worksheet that cannot be found, it is probably useful to redirect to the page with the list of published worksheets, perhaps after showing an error message like \"There is no worksheet currently available at this URL. You will be redirected to the <a href='URL of published worksheets index'>index of published worksheets</a> in 15 seconds.\"\n\nThis may be related to ticket 5988:\n\nhttp://trac.sagemath.org/sage_trac/ticket/5988\n\nIssue created by migration from https://trac.sagemath.org/ticket/6069\n\n",
    "created_at": "2009-05-18T13:16:06Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Blank notebook page when loading URL for published sheet that is AWOL",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6069",
    "user": "khorton"
}
```
Assignee: somebody

CC:  acleone robert.marik

If someone attempts to access a URL for a published worksheet that no longer exists (perhaps because the URL changed when the worksheet went through a published to unpublished to published cycle), or the URL was mistyped, they get a blank page titled "Error | Sage Notebook", with no hint on what to do to resolve the problem.

If they are trying to access a published worksheet that cannot be found, it is probably useful to redirect to the page with the list of published worksheets, perhaps after showing an error message like "There is no worksheet currently available at this URL. You will be redirected to the <a href='URL of published worksheets index'>index of published worksheets</a> in 15 seconds."

This may be related to ticket 5988:

http://trac.sagemath.org/sage_trac/ticket/5988

Issue created by migration from https://trac.sagemath.org/ticket/6069





---

archive/issue_comments_048294.json:
```json
{
    "body": "Attachment [trac_6069-missing-published-worksheet.patch](tarball://root/attachments/some-uuid/ticket6069/trac_6069-missing-published-worksheet.patch) by timdumol created at 2010-01-18 19:53:09\n\nThis says that \"There is no published worksheet with name '%s'\" instead.",
    "created_at": "2010-01-18T19:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48294",
    "user": "timdumol"
}
```

Attachment [trac_6069-missing-published-worksheet.patch](tarball://root/attachments/some-uuid/ticket6069/trac_6069-missing-published-worksheet.patch) by timdumol created at 2010-01-18 19:53:09

This says that "There is no published worksheet with name '%s'" instead.



---

archive/issue_comments_048295.json:
```json
{
    "body": "I think the previous message \"The user 'pub' has no worksheet '%s'\" was a bit confusing, but it does work. Feel free to ignore the patch and close this.",
    "created_at": "2010-01-18T19:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48295",
    "user": "timdumol"
}
```

I think the previous message "The user 'pub' has no worksheet '%s'" was a bit confusing, but it does work. Feel free to ignore the patch and close this.



---

archive/issue_comments_048296.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T19:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48296",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_048297.json:
```json
{
    "body": "Redirect to `pub/` after delay.  Apply only this patch.  sagenb repo.",
    "created_at": "2010-01-20T03:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48297",
    "user": "mpatel"
}
```

Redirect to `pub/` after delay.  Apply only this patch.  sagenb repo.



---

archive/issue_comments_048298.json:
```json
{
    "body": "Attachment [trac_6069-missing_pub_ws.2.patch](tarball://root/attachments/some-uuid/ticket6069/trac_6069-missing_pub_ws.2.patch) by mpatel created at 2010-01-20 03:15:34\n\nV2 is an attempt to set up redirection.  It should also ensure for `guest` users that the error page does not include the full top bar (Settings, Log, etc.).\n\nFeel free to make changes.",
    "created_at": "2010-01-20T03:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48298",
    "user": "mpatel"
}
```

Attachment [trac_6069-missing_pub_ws.2.patch](tarball://root/attachments/some-uuid/ticket6069/trac_6069-missing_pub_ws.2.patch) by mpatel created at 2010-01-20 03:15:34

V2 is an attempt to set up redirection.  It should also ensure for `guest` users that the error page does not include the full top bar (Settings, Log, etc.).

Feel free to make changes.



---

archive/issue_comments_048299.json:
```json
{
    "body": "V2 applies cleanly to #8051 + #7784 + #5712.",
    "created_at": "2010-01-25T04:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48299",
    "user": "mpatel"
}
```

V2 applies cleanly to #8051 + #7784 + #5712.



---

archive/issue_comments_048300.json:
```json
{
    "body": "Better titles for non-Error pages.  Apply only this patch.",
    "created_at": "2010-02-14T01:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48300",
    "user": "mpatel"
}
```

Better titles for non-Error pages.  Apply only this patch.



---

archive/issue_comments_048301.json:
```json
{
    "body": "Attachment [trac_6069-missing_pub_ws.3.patch](tarball://root/attachments/some-uuid/ticket6069/trac_6069-missing_pub_ws.3.patch) by mpatel created at 2010-02-14 01:31:08\n\nV3 should\n\n* Fix #8234.\n* Use a title more appropriate than `Error` for certain non-Error pages (see the patch).\n* Make \"Sign Out\" redirect to \"/\" when `require_login=False`.  This is better than returning a page whose header refers to a user named \"None\" and has a broken \"Home\" link!",
    "created_at": "2010-02-14T01:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48301",
    "user": "mpatel"
}
```

Attachment [trac_6069-missing_pub_ws.3.patch](tarball://root/attachments/some-uuid/ticket6069/trac_6069-missing_pub_ws.3.patch) by mpatel created at 2010-02-14 01:31:08

V3 should

* Fix #8234.
* Use a title more appropriate than `Error` for certain non-Error pages (see the patch).
* Make "Sign Out" redirect to "/" when `require_login=False`.  This is better than returning a page whose header refers to a user named "None" and has a broken "Home" link!



---

archive/issue_comments_048302.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-02-14T01:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48302",
    "user": "mpatel"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_048303.json:
```json
{
    "body": "Patel's changes look great. Anyone mind signing off mine?",
    "created_at": "2010-03-12T01:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48303",
    "user": "timdumol"
}
```

Patel's changes look great. Anyone mind signing off mine?



---

archive/issue_comments_048304.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-12T18:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48304",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_048305.json:
```json
{
    "body": "(I'm not changing any notebook code in Sage 4.4.)",
    "created_at": "2010-04-23T04:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48305",
    "user": "jhpalmieri"
}
```

(I'm not changing any notebook code in Sage 4.4.)



---

archive/issue_comments_048306.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-04T04:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6069#issuecomment-48306",
    "user": "timdumol"
}
```

Resolution: fixed
