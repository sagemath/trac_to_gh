# Issue 8324: Reconcile sage.misc.sageinspect and sagenb.misc.sageinspect

archive/issues_008324.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jhpalmieri\n\nThe module `sage.misc.sageinspect` is missing several recent changes to `sagenb.misc.sageinspect`.\n\nNote: SageNB has its own `sageinspect` so that it can stand alone.\n\nRelated: #2064.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8324\n\n",
    "created_at": "2010-02-22T03:50:36Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Reconcile sage.misc.sageinspect and sagenb.misc.sageinspect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8324",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @jhpalmieri

The module `sage.misc.sageinspect` is missing several recent changes to `sagenb.misc.sageinspect`.

Note: SageNB has its own `sageinspect` so that it can stand alone.

Related: #2064.

Issue created by migration from https://trac.sagemath.org/ticket/8324





---

archive/issue_comments_073751.json:
```json
{
    "body": "sagenb repo.",
    "created_at": "2010-02-22T03:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73751",
    "user": "https://github.com/qed777"
}
```

sagenb repo.



---

archive/issue_comments_073752.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-22T04:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73752",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073753.json:
```json
{
    "body": "Attachment [trac_8324-sagenb_sageinspect.patch](tarball://root/attachments/some-uuid/ticket8324/trac_8324-sagenb_sageinspect.patch) by @qed777 created at 2010-02-22 04:06:09",
    "created_at": "2010-02-22T04:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73753",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8324-sagenb_sageinspect.patch](tarball://root/attachments/some-uuid/ticket8324/trac_8324-sagenb_sageinspect.patch) by @qed777 created at 2010-02-22 04:06:09



---

archive/issue_events_019930.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-22T04:06:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "milestone": "sage-4.3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8324#event-19930"
}
```



---

archive/issue_comments_073754.json:
```json
{
    "body": "I guess outside (non-Sage) projects delete some doctests?",
    "created_at": "2010-02-22T04:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73754",
    "user": "https://github.com/qed777"
}
```

I guess outside (non-Sage) projects delete some doctests?



---

archive/issue_comments_073755.json:
```json
{
    "body": "I suppose this \"depends\" on #8244: it adds a bit to sagenb.misc.sageinspect.py from the patch there.  Overall, it looks fine: just the obvious changes.  Is there a good way to run doctests on all of sagenb?  The new sageinspect passes doctests with Sage installed, and I think it should without the rest of the Sage library, but I haven't checked it.\n\n> I guess outside (non-Sage) projects delete some doctests?\n\n\nI'm not sure what this refers to.",
    "created_at": "2010-02-24T22:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73755",
    "user": "https://github.com/jhpalmieri"
}
```

I suppose this "depends" on #8244: it adds a bit to sagenb.misc.sageinspect.py from the patch there.  Overall, it looks fine: just the obvious changes.  Is there a good way to run doctests on all of sagenb?  The new sageinspect passes doctests with Sage installed, and I think it should without the rest of the Sage library, but I haven't checked it.

> I guess outside (non-Sage) projects delete some doctests?


I'm not sure what this refers to.



---

archive/issue_comments_073756.json:
```json
{
    "body": "You can run `make test` or `make ptest` in the root of the sagenb repository or run `sage -t -sagenb`, say, but these assume Sage is installed.\n\nI'm not aware of an easy way to doctest the standalone notebook.  We only recently got the tests to run with Sage (cf. #7650).\n\nSeveral notebook doctests and some `import`s not wrapped in `try-except` clauses refer to Sage modules.  It seems that most of the Sage-dependent doctests in `sagenb.misc.sageinspect` test Cython introspection, but right now, the notebook doesn't include Cython modules.  I don't know if outside projects depend on these Cython-related features.",
    "created_at": "2010-02-25T05:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73756",
    "user": "https://github.com/qed777"
}
```

You can run `make test` or `make ptest` in the root of the sagenb repository or run `sage -t -sagenb`, say, but these assume Sage is installed.

I'm not aware of an easy way to doctest the standalone notebook.  We only recently got the tests to run with Sage (cf. #7650).

Several notebook doctests and some `import`s not wrapped in `try-except` clauses refer to Sage modules.  It seems that most of the Sage-dependent doctests in `sagenb.misc.sageinspect` test Cython introspection, but right now, the notebook doesn't include Cython modules.  I don't know if outside projects depend on these Cython-related features.



---

archive/issue_comments_073757.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-25T05:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73757",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073758.json:
```json
{
    "body": "Is this ticket meant to have the milestone \"Sage 4.3.4\"? In any case, it could only be closed once the relevant patch is merged in the SageNB repository, which is managed by the upstream SageNB team.",
    "created_at": "2010-03-03T03:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73758",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Is this ticket meant to have the milestone "Sage 4.3.4"? In any case, it could only be closed once the relevant patch is merged in the SageNB repository, which is managed by the upstream SageNB team.



---

archive/issue_comments_073759.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-03T22:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73759",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_073760.json:
```json
{
    "body": "Here's a new patch; apply on top of the old one.  This changes one line to fix the doctest failure in 4.3.4.alpha0: `sage_getsourcelines(matrix,True)[1])` used to return 33, and now it returns 34.",
    "created_at": "2010-03-03T22:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73760",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a new patch; apply on top of the old one.  This changes one line to fix the doctest failure in 4.3.4.alpha0: `sage_getsourcelines(matrix,True)[1])` used to return 33, and now it returns 34.



---

archive/issue_comments_073761.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-03T22:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73761",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073762.json:
```json
{
    "body": "(This new patch is supposed to fix one of the bugs listed at #8430.  Only the \"new\" patch needs reviewing.)",
    "created_at": "2010-03-03T22:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73762",
    "user": "https://github.com/jhpalmieri"
}
```

(This new patch is supposed to fix one of the bugs listed at #8430.  Only the "new" patch needs reviewing.)



---

archive/issue_events_019931.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-03-03T22:07:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "milestone": "sage-4.3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8324#event-19931"
}
```



---

archive/issue_events_019932.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-03-03T22:07:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "milestone": "sage-4.3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8324#event-19932"
}
```



---

archive/issue_comments_073763.json:
```json
{
    "body": "Attachment [trac_8324-new.patch](tarball://root/attachments/some-uuid/ticket8324/trac_8324-new.patch) by @jhpalmieri created at 2010-03-03 22:08:03\n\napply on top of other patch",
    "created_at": "2010-03-03T22:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73763",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8324-new.patch](tarball://root/attachments/some-uuid/ticket8324/trac_8324-new.patch) by @jhpalmieri created at 2010-03-03 22:08:03

apply on top of other patch



---

archive/issue_comments_073764.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-04T07:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73764",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073765.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-04T22:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73765",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019933.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-03-04T22:51:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8324#event-19933"
}
```
