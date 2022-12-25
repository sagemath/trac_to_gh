# Issue 8408: Update sqlite to 3.6.22 (the latest version)

archive/issues_008408.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nOne doctest that fails on Solaris #8400 is solved by updating the version of sqlite to the latest upstream release, which is http://www.sqlite.org/sqlite-amalgamation-3.6.22.tar.gz\n\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8408\n\n",
    "created_at": "2010-03-01T13:33:20Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Update sqlite to 3.6.22 (the latest version)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8408",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

One doctest that fails on Solaris #8400 is solved by updating the version of sqlite to the latest upstream release, which is http://www.sqlite.org/sqlite-amalgamation-3.6.22.tar.gz






Issue created by migration from https://trac.sagemath.org/ticket/8408





---

archive/issue_comments_075209.json:
```json
{
    "body": "Actually, this solves **ALL** the doctest failures on Solaris, so assuming nobody manages to break anything, Sage 4.3.4 should work on Solaris with all doctests passing! \n\nThe new package can be found at http://boxen.math.washington.edu/home/kirkby/Solaris-fixes/sqlite-3.6.22/sqlite-3.6.22.spkg\n\nDave",
    "created_at": "2010-03-01T14:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8408#issuecomment-75209",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Actually, this solves **ALL** the doctest failures on Solaris, so assuming nobody manages to break anything, Sage 4.3.4 should work on Solaris with all doctests passing! 

The new package can be found at http://boxen.math.washington.edu/home/kirkby/Solaris-fixes/sqlite-3.6.22/sqlite-3.6.22.spkg

Dave



---

archive/issue_comments_075210.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-01T14:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8408#issuecomment-75210",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075211.json:
```json
{
    "body": "Attachment [sqlite-update-allows-all-Solaris-doctests-to-pass.patch](tarball://root/attachments/some-uuid/ticket8408/sqlite-update-allows-all-Solaris-doctests-to-pass.patch) by drkirkby created at 2010-03-01 14:25:00",
    "created_at": "2010-03-01T14:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8408#issuecomment-75211",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [sqlite-update-allows-all-Solaris-doctests-to-pass.patch](tarball://root/attachments/some-uuid/ticket8408/sqlite-update-allows-all-Solaris-doctests-to-pass.patch) by drkirkby created at 2010-03-01 14:25:00



---

archive/issue_comments_075212.json:
```json
{
    "body": "Do we know what changed from 3.6.19 to 3.6.22 that might have fixed the segmentation faults?",
    "created_at": "2010-03-03T08:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8408#issuecomment-75212",
    "user": "https://github.com/qed777"
}
```

Do we know what changed from 3.6.19 to 3.6.22 that might have fixed the segmentation faults?



---

archive/issue_comments_075213.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-03T08:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8408#issuecomment-75213",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075214.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T08:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8408#issuecomment-75214",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_075215.json:
```json
{
    "body": "**Notes to the release manager**\n\nSorry, I should have written on the ticket, but #8397, #8398, #8399 #8400 and #8401 can all be closed now this is fixed. \n\nDave",
    "created_at": "2010-03-06T21:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8408#issuecomment-75215",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

**Notes to the release manager**

Sorry, I should have written on the ticket, but #8397, #8398, #8399 #8400 and #8401 can all be closed now this is fixed. 

Dave
