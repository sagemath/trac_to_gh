# Issue 9892: Make PARI *not* catch signals

archive/issues_009892.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @nexttime @robertwb\n\nIn Sage, there is no reason for the PARI library to catch signals (by default, it catches SIGBUS, SIGFPE, SIGINT, SIGBREAK, SIGPIPE, SIGSEGV).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9893\n\n",
    "created_at": "2010-09-10T21:59:30Z",
    "labels": [
        "component: c_lib",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Make PARI *not* catch signals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9892",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: tba

CC:  @nexttime @robertwb

In Sage, there is no reason for the PARI library to catch signals (by default, it catches SIGBUS, SIGFPE, SIGINT, SIGBREAK, SIGPIPE, SIGSEGV).

Issue created by migration from https://trac.sagemath.org/ticket/9893





---

archive/issue_comments_097888.json:
```json
{
    "body": "Changing component from c_lib to interfaces.",
    "created_at": "2010-09-12T08:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97888",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from c_lib to interfaces.



---

archive/issue_comments_097889.json:
```json
{
    "body": "Changing assignee from tba to @williamstein.",
    "created_at": "2010-09-12T08:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97889",
    "user": "https://github.com/jdemeyer"
}
```

Changing assignee from tba to @williamstein.



---

archive/issue_comments_097890.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-12T09:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97890",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097891.json:
```json
{
    "body": "This seems to influence #10018, so both #9893 and #10018 should probably be handled together.",
    "created_at": "2010-09-26T17:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97891",
    "user": "https://github.com/jdemeyer"
}
```

This seems to influence #10018, so both #9893 and #10018 should probably be handled together.



---

archive/issue_comments_097892.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-26T17:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97892",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_097893.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-27T09:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97893",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097894.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-29T07:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97894",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097895.json:
```json
{
    "body": "Positive review of the proposal to close as duplicate.",
    "created_at": "2010-09-29T07:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97895",
    "user": "https://github.com/loefflerd"
}
```

Positive review of the proposal to close as duplicate.



---

archive/issue_events_010017.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-03T09:37:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9892#event-10017"
}
```



---

archive/issue_comments_097896.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-10-03T09:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97896",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate



---

archive/issue_comments_097897.json:
```json
{
    "body": "I'm closing this now.  Feel free to reopen it, if #10018 ultimately does not subsume this.",
    "created_at": "2010-10-03T09:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97897",
    "user": "https://github.com/qed777"
}
```

I'm closing this now.  Feel free to reopen it, if #10018 ultimately does not subsume this.



---

archive/issue_comments_097898.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-10-17T08:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97898",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_010018.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-10-17T08:39:22Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9892#event-10018"
}
```



---

archive/issue_comments_097899.json:
```json
{
    "body": "Reopening this to collect the minimal changes required in PARI to make #9678 work.  This patch here will then become a prerequisite for #9678.",
    "created_at": "2010-10-17T08:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97899",
    "user": "https://github.com/jdemeyer"
}
```

Reopening this to collect the minimal changes required in PARI to make #9678 work.  This patch here will then become a prerequisite for #9678.



---

archive/issue_comments_097900.json:
```json
{
    "body": "Changing keywords from \"\" to \"pari signals\".",
    "created_at": "2010-10-17T08:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97900",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "" to "pari signals".



---

archive/issue_comments_097901.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-19T20:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97901",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097902.json:
```json
{
    "body": "All long doctests pass on a 32-bit PPC OS X 10.4 and on a 64-bit Intel Linux.  This patch was first included in #10018, then in #9678 and now I have separated it again in order to make #9678 not too much of a patch bomb.  The current version of the patch is pretty much the same as the old version of 5 weeks ago.  The patch makes sense by itself, but of course it is partially motivated by #9678.  Remark also that currently all tests in `sage/libs/pari` pass with #9678, #10061 and #10030 applied.",
    "created_at": "2010-10-19T20:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97902",
    "user": "https://github.com/jdemeyer"
}
```

All long doctests pass on a 32-bit PPC OS X 10.4 and on a 64-bit Intel Linux.  This patch was first included in #10018, then in #9678 and now I have separated it again in order to make #9678 not too much of a patch bomb.  The current version of the patch is pretty much the same as the old version of 5 weeks ago.  The patch makes sense by itself, but of course it is partially motivated by #9678.  Remark also that currently all tests in `sage/libs/pari` pass with #9678, #10061 and #10030 applied.



---

archive/issue_comments_097903.json:
```json
{
    "body": "In general I'm a fan of using try...finally to handle sig_on/sig_off where there are many exits to a function, especially if exceptions are involved. (It can also alleviate the use of temporary variables to return something, but that's a matter of taste.)\n\nSpeed is important for new_gen_from_mpz_t, which is why we don't set up signals for \"small\" values. This behavior should be preserved.",
    "created_at": "2010-10-22T05:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97903",
    "user": "https://github.com/robertwb"
}
```

In general I'm a fan of using try...finally to handle sig_on/sig_off where there are many exits to a function, especially if exceptions are involved. (It can also alleviate the use of temporary variables to return something, but that's a matter of taste.)

Speed is important for new_gen_from_mpz_t, which is why we don't set up signals for "small" values. This behavior should be preserved.



---

archive/issue_comments_097904.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-22T05:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97904",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_097905.json:
```json
{
    "body": "Attachment [9893_pari_init.patch](tarball://root/attachments/some-uuid/ticket9893/9893_pari_init.patch) by @jdemeyer created at 2010-10-22 11:59:56",
    "created_at": "2010-10-22T11:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97905",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9893_pari_init.patch](tarball://root/attachments/some-uuid/ticket9893/9893_pari_init.patch) by @jdemeyer created at 2010-10-22 11:59:56



---

archive/issue_comments_097906.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-22T13:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97906",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097907.json:
```json
{
    "body": "New patch still needs review....",
    "created_at": "2010-10-26T12:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97907",
    "user": "https://github.com/jdemeyer"
}
```

New patch still needs review....



---

archive/issue_comments_097908.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-05T03:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97908",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097909.json:
```json
{
    "body": "Looks good to me, though I haven't had time to run all tests yet.",
    "created_at": "2010-11-05T03:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97909",
    "user": "https://github.com/robertwb"
}
```

Looks good to me, though I haven't had time to run all tests yet.



---

archive/issue_comments_097910.json:
```json
{
    "body": "Replying to [comment:15 robertwb]:\n> Looks good to me\nThanks!",
    "created_at": "2010-11-05T08:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97910",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:15 robertwb]:
> Looks good to me
Thanks!



---

archive/issue_events_010019.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-10T22:20:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9892#event-10019"
}
```



---

archive/issue_comments_097911.json:
```json
{
    "body": "Resolution changed from duplicate to fixed",
    "created_at": "2010-11-10T22:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97911",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from duplicate to fixed



---

archive/issue_comments_097912.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-11-12T13:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97912",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_097913.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-11-12T13:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97913",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_010020.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-12T13:24:49Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9892#event-10020"
}
```



---

archive/issue_comments_097914.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-12T13:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97914",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097915.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-12T13:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97915",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097916.json:
```json
{
    "body": "I decided not to merge this in sage-4.6.1.alpha1 because I thought it might be the cause for #9163 (it turns out that's not the case).",
    "created_at": "2010-11-13T10:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97916",
    "user": "https://github.com/jdemeyer"
}
```

I decided not to merge this in sage-4.6.1.alpha1 because I thought it might be the cause for #9163 (it turns out that's not the case).



---

archive/issue_comments_097917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-15T23:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-97917",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_010021.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-15T23:26:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9892#event-10021"
}
```
