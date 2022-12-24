# Issue 8231: Place cursor in new input cell in notebook

archive/issues_008231.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jhpalmieri @williamstein @robert-marik\n\nSince the upgrade to sage 4.3.2, when one creates a new input cell in the notebook, the cursor is not automatically placed in the new input cell. It is fair to assume that a user that creates a new input cell wants to type in it straight away, so time would be saved if the cursor was put there automatically, as was the case in previous versions of the notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8231\n\n",
    "created_at": "2010-02-10T15:27:31Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Place cursor in new input cell in notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8231",
    "user": "schymans"
}
```
Assignee: @williamstein

CC:  @jhpalmieri @williamstein @robert-marik

Since the upgrade to sage 4.3.2, when one creates a new input cell in the notebook, the cursor is not automatically placed in the new input cell. It is fair to assume that a user that creates a new input cell wants to type in it straight away, so time would be saved if the cursor was put there automatically, as was the case in previous versions of the notebook.

Issue created by migration from https://trac.sagemath.org/ticket/8231





---

archive/issue_comments_072708.json:
```json
{
    "body": "In fact, there are a *bunch* of situations where suddenly no cell has focus.  I say that there should be *no possible way* to ever make it so that no cell has focus, except maybe something involving `@`interact.",
    "created_at": "2010-02-13T00:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8231#issuecomment-72708",
    "user": "@williamstein"
}
```

In fact, there are a *bunch* of situations where suddenly no cell has focus.  I say that there should be *no possible way* to ever make it so that no cell has focus, except maybe something involving `@`interact.



---

archive/issue_comments_072709.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-02-14T01:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8231#issuecomment-72709",
    "user": "@qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_072710.json:
```json
{
    "body": "Revert and fix #4450.  sagenb repo.",
    "created_at": "2010-02-14T01:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8231#issuecomment-72710",
    "user": "@qed777"
}
```

Revert and fix #4450.  sagenb repo.



---

archive/issue_comments_072711.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-14T02:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8231#issuecomment-72711",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072712.json:
```json
{
    "body": "Attachment [trac_8231-cursor_AWOL.patch](tarball://root/attachments/some-uuid/ticket8231/trac_8231-cursor_AWOL.patch) by @qed777 created at 2010-02-14 02:01:48\n\nThe patch should restore the earlier behavior and fix the cursor-wraps-around-the-last-compute-cell problem.  If not, let me know.",
    "created_at": "2010-02-14T02:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8231#issuecomment-72712",
    "user": "@qed777"
}
```

Attachment [trac_8231-cursor_AWOL.patch](tarball://root/attachments/some-uuid/ticket8231/trac_8231-cursor_AWOL.patch) by @qed777 created at 2010-02-14 02:01:48

The patch should restore the earlier behavior and fix the cursor-wraps-around-the-last-compute-cell problem.  If not, let me know.



---

archive/issue_comments_072713.json:
```json
{
    "body": "This works for me, but I don't know javascript, and this is also an important issue, so other people should take a good look, too.",
    "created_at": "2010-02-17T04:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8231#issuecomment-72713",
    "user": "@jhpalmieri"
}
```

This works for me, but I don't know javascript, and this is also an important issue, so other people should take a good look, too.



---

archive/issue_comments_072714.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-21T19:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8231#issuecomment-72714",
    "user": "@williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072715.json:
```json
{
    "body": "Positive review.",
    "created_at": "2010-02-21T19:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8231#issuecomment-72715",
    "user": "@williamstein"
}
```

Positive review.



---

archive/issue_comments_072716.json:
```json
{
    "body": "Merged [sagenb-0.7.5.1.spkg](http://sage.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.7.5.1.spkg) in standard spkg repository.",
    "created_at": "2010-02-22T03:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8231#issuecomment-72716",
    "user": "mvngu"
}
```

Merged [sagenb-0.7.5.1.spkg](http://sage.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.7.5.1.spkg) in standard spkg repository.



---

archive/issue_comments_072717.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-22T03:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8231#issuecomment-72717",
    "user": "mvngu"
}
```

Resolution: fixed
