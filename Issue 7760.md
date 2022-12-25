# Issue 7760: sage -merge fails silently when applying patches with rejects

archive/issues_007760.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @craigcitro\n\nWe need to make sure the hg qpush command is failing with the proper exit code and handle it appropriately.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7760\n\n",
    "created_at": "2009-12-24T11:03:04Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "sage -merge fails silently when applying patches with rejects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7760",
    "user": "https://github.com/mwhansen"
}
```
Assignee: GeorgSWeber

CC:  @craigcitro

We need to make sure the hg qpush command is failing with the proper exit code and handle it appropriately.

Issue created by migration from https://trac.sagemath.org/ticket/7760





---

archive/issue_comments_066703.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T17:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7760#issuecomment-66703",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066704.json:
```json
{
    "body": "Attachment [trac_7760.patch](tarball://root/attachments/some-uuid/ticket7760/trac_7760.patch) by @mwhansen created at 2010-01-16 17:46:05",
    "created_at": "2010-01-16T17:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7760#issuecomment-66704",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7760.patch](tarball://root/attachments/some-uuid/ticket7760/trac_7760.patch) by @mwhansen created at 2010-01-16 17:46:05



---

archive/issue_comments_066705.json:
```json
{
    "body": "This is clearly the right fix for the problem Mike ran into, and I'm giving it a positive review. \n\nI'm happy to see this merged, but it brings up a question: why aren't we checking the exit code from mercurial? A quick check of the code reveals the issue: we use `os.popen3` inside the hg interface, which we can't easily use to get the return code. (Or, at least, I don't know how to do it.) Maybe we should file an enhancement ticket to rewrite those lines to use `subprocess.Popen`, and correctly give back the return code?",
    "created_at": "2010-01-17T23:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7760#issuecomment-66705",
    "user": "https://github.com/craigcitro"
}
```

This is clearly the right fix for the problem Mike ran into, and I'm giving it a positive review. 

I'm happy to see this merged, but it brings up a question: why aren't we checking the exit code from mercurial? A quick check of the code reveals the issue: we use `os.popen3` inside the hg interface, which we can't easily use to get the return code. (Or, at least, I don't know how to do it.) Maybe we should file an enhancement ticket to rewrite those lines to use `subprocess.Popen`, and correctly give back the return code?



---

archive/issue_comments_066706.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T23:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7760#issuecomment-66706",
    "user": "https://github.com/craigcitro"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066707.json:
```json
{
    "body": "Yep, I think that sounds good.  I don't know how to get it from os.popen3.",
    "created_at": "2010-01-17T23:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7760#issuecomment-66707",
    "user": "https://github.com/mwhansen"
}
```

Yep, I think that sounds good.  I don't know how to get it from os.popen3.



---

archive/issue_comments_066708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T00:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7760#issuecomment-66708",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_018564.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-19T00:42:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7760",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7760#event-18564"
}
```
