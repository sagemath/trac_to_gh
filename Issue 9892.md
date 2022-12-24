# Issue 9892: Make PARI *not* catch signals

archive/issues_009892.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @nexttime @robertwb\n\nIn Sage, there is no reason for the PARI library to catch signals (by default, it catches SIGBUS, SIGFPE, SIGINT, SIGBREAK, SIGPIPE, SIGSEGV).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9893\n\n",
    "created_at": "2010-09-10T21:59:30Z",
    "labels": [
        "c_lib",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Make PARI *not* catch signals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9892",
    "user": "@jdemeyer"
}
```
Assignee: tba

CC:  @nexttime @robertwb

In Sage, there is no reason for the PARI library to catch signals (by default, it catches SIGBUS, SIGFPE, SIGINT, SIGBREAK, SIGPIPE, SIGSEGV).

Issue created by migration from https://trac.sagemath.org/ticket/9893





---

archive/issue_comments_098050.json:
```json
{
    "body": "Changing component from c_lib to interfaces.",
    "created_at": "2010-09-12T08:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98050",
    "user": "@jdemeyer"
}
```

Changing component from c_lib to interfaces.



---

archive/issue_comments_098051.json:
```json
{
    "body": "Changing assignee from tba to @williamstein.",
    "created_at": "2010-09-12T08:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98051",
    "user": "@jdemeyer"
}
```

Changing assignee from tba to @williamstein.



---

archive/issue_comments_098052.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-12T09:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98052",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098053.json:
```json
{
    "body": "This seems to influence #10018, so both #9893 and #10018 should probably be handled together.",
    "created_at": "2010-09-26T17:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98053",
    "user": "@jdemeyer"
}
```

This seems to influence #10018, so both #9893 and #10018 should probably be handled together.



---

archive/issue_comments_098054.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-26T17:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98054",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098055.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-27T09:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98055",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098056.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-29T07:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98056",
    "user": "@loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098057.json:
```json
{
    "body": "Positive review of the proposal to close as duplicate.",
    "created_at": "2010-09-29T07:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98057",
    "user": "@loefflerd"
}
```

Positive review of the proposal to close as duplicate.



---

archive/issue_comments_098058.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-10-03T09:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98058",
    "user": "@qed777"
}
```

Resolution: duplicate



---

archive/issue_comments_098059.json:
```json
{
    "body": "I'm closing this now.  Feel free to reopen it, if #10018 ultimately does not subsume this.",
    "created_at": "2010-10-03T09:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98059",
    "user": "@qed777"
}
```

I'm closing this now.  Feel free to reopen it, if #10018 ultimately does not subsume this.



---

archive/issue_comments_098060.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-10-17T08:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98060",
    "user": "@jdemeyer"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_098061.json:
```json
{
    "body": "Reopening this to collect the minimal changes required in PARI to make #9678 work.  This patch here will then become a prerequisite for #9678.",
    "created_at": "2010-10-17T08:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98061",
    "user": "@jdemeyer"
}
```

Reopening this to collect the minimal changes required in PARI to make #9678 work.  This patch here will then become a prerequisite for #9678.



---

archive/issue_comments_098062.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-10-17T08:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98062",
    "user": "@jdemeyer"
}
```

Changing priority from minor to major.



---

archive/issue_comments_098063.json:
```json
{
    "body": "Changing keywords from \"\" to \"pari signals\".",
    "created_at": "2010-10-17T08:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98063",
    "user": "@jdemeyer"
}
```

Changing keywords from "" to "pari signals".



---

archive/issue_comments_098064.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-19T20:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98064",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098065.json:
```json
{
    "body": "All long doctests pass on a 32-bit PPC OS X 10.4 and on a 64-bit Intel Linux.  This patch was first included in #10018, then in #9678 and now I have separated it again in order to make #9678 not too much of a patch bomb.  The current version of the patch is pretty much the same as the old version of 5 weeks ago.  The patch makes sense by itself, but of course it is partially motivated by #9678.  Remark also that currently all tests in `sage/libs/pari` pass with #9678, #10061 and #10030 applied.",
    "created_at": "2010-10-19T20:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98065",
    "user": "@jdemeyer"
}
```

All long doctests pass on a 32-bit PPC OS X 10.4 and on a 64-bit Intel Linux.  This patch was first included in #10018, then in #9678 and now I have separated it again in order to make #9678 not too much of a patch bomb.  The current version of the patch is pretty much the same as the old version of 5 weeks ago.  The patch makes sense by itself, but of course it is partially motivated by #9678.  Remark also that currently all tests in `sage/libs/pari` pass with #9678, #10061 and #10030 applied.



---

archive/issue_comments_098066.json:
```json
{
    "body": "In general I'm a fan of using try...finally to handle sig_on/sig_off where there are many exits to a function, especially if exceptions are involved. (It can also alleviate the use of temporary variables to return something, but that's a matter of taste.)\n\nSpeed is important for new_gen_from_mpz_t, which is why we don't set up signals for \"small\" values. This behavior should be preserved.",
    "created_at": "2010-10-22T05:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98066",
    "user": "@robertwb"
}
```

In general I'm a fan of using try...finally to handle sig_on/sig_off where there are many exits to a function, especially if exceptions are involved. (It can also alleviate the use of temporary variables to return something, but that's a matter of taste.)

Speed is important for new_gen_from_mpz_t, which is why we don't set up signals for "small" values. This behavior should be preserved.



---

archive/issue_comments_098067.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-22T05:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98067",
    "user": "@robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098068.json:
```json
{
    "body": "Attachment [9893_pari_init.patch](tarball://root/attachments/some-uuid/ticket9893/9893_pari_init.patch) by @jdemeyer created at 2010-10-22 11:59:56",
    "created_at": "2010-10-22T11:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98068",
    "user": "@jdemeyer"
}
```

Attachment [9893_pari_init.patch](tarball://root/attachments/some-uuid/ticket9893/9893_pari_init.patch) by @jdemeyer created at 2010-10-22 11:59:56



---

archive/issue_comments_098069.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-22T13:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98069",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098070.json:
```json
{
    "body": "New patch still needs review....",
    "created_at": "2010-10-26T12:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98070",
    "user": "@jdemeyer"
}
```

New patch still needs review....



---

archive/issue_comments_098071.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-05T03:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98071",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098072.json:
```json
{
    "body": "Looks good to me, though I haven't had time to run all tests yet.",
    "created_at": "2010-11-05T03:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98072",
    "user": "@robertwb"
}
```

Looks good to me, though I haven't had time to run all tests yet.



---

archive/issue_comments_098073.json:
```json
{
    "body": "Replying to [comment:15 robertwb]:\n> Looks good to me\nThanks!",
    "created_at": "2010-11-05T08:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98073",
    "user": "@jdemeyer"
}
```

Replying to [comment:15 robertwb]:
> Looks good to me
Thanks!



---

archive/issue_comments_098074.json:
```json
{
    "body": "Resolution changed from duplicate to fixed",
    "created_at": "2010-11-10T22:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98074",
    "user": "@jdemeyer"
}
```

Resolution changed from duplicate to fixed



---

archive/issue_comments_098075.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-11-12T13:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98075",
    "user": "@jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_098076.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-11-12T13:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98076",
    "user": "@jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_098077.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-12T13:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98077",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098078.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-12T13:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98078",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098079.json:
```json
{
    "body": "I decided not to merge this in sage-4.6.1.alpha1 because I thought it might be the cause for #9163 (it turns out that's not the case).",
    "created_at": "2010-11-13T10:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98079",
    "user": "@jdemeyer"
}
```

I decided not to merge this in sage-4.6.1.alpha1 because I thought it might be the cause for #9163 (it turns out that's not the case).



---

archive/issue_comments_098080.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-15T23:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9892#issuecomment-98080",
    "user": "@jdemeyer"
}
```

Resolution: fixed
