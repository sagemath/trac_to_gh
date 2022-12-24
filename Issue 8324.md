# Issue 8324: Reconcile sage.misc.sageinspect and sagenb.misc.sageinspect

archive/issues_008324.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jhpalmieri\n\nThe module `sage.misc.sageinspect` is missing several recent changes to `sagenb.misc.sageinspect`.\n\nNote: SageNB has its own `sageinspect` so that it can stand alone.\n\nRelated: #2064.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8324\n\n",
    "created_at": "2010-02-22T03:50:36Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Reconcile sage.misc.sageinspect and sagenb.misc.sageinspect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8324",
    "user": "@qed777"
}
```
Assignee: @williamstein

CC:  @jhpalmieri

The module `sage.misc.sageinspect` is missing several recent changes to `sagenb.misc.sageinspect`.

Note: SageNB has its own `sageinspect` so that it can stand alone.

Related: #2064.

Issue created by migration from https://trac.sagemath.org/ticket/8324





---

archive/issue_comments_073875.json:
```json
{
    "body": "sagenb repo.",
    "created_at": "2010-02-22T03:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73875",
    "user": "@qed777"
}
```

sagenb repo.



---

archive/issue_comments_073876.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-22T04:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73876",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073877.json:
```json
{
    "body": "Attachment [trac_8324-sagenb_sageinspect.patch](tarball://root/attachments/some-uuid/ticket8324/trac_8324-sagenb_sageinspect.patch) by @qed777 created at 2010-02-22 04:06:09",
    "created_at": "2010-02-22T04:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73877",
    "user": "@qed777"
}
```

Attachment [trac_8324-sagenb_sageinspect.patch](tarball://root/attachments/some-uuid/ticket8324/trac_8324-sagenb_sageinspect.patch) by @qed777 created at 2010-02-22 04:06:09



---

archive/issue_comments_073878.json:
```json
{
    "body": "I guess outside (non-Sage) projects delete some doctests?",
    "created_at": "2010-02-22T04:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73878",
    "user": "@qed777"
}
```

I guess outside (non-Sage) projects delete some doctests?



---

archive/issue_comments_073879.json:
```json
{
    "body": "I suppose this \"depends\" on #8244: it adds a bit to sagenb.misc.sageinspect.py from the patch there.  Overall, it looks fine: just the obvious changes.  Is there a good way to run doctests on all of sagenb?  The new sageinspect passes doctests with Sage installed, and I think it should without the rest of the Sage library, but I haven't checked it.\n\n> I guess outside (non-Sage) projects delete some doctests?\n\nI'm not sure what this refers to.",
    "created_at": "2010-02-24T22:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73879",
    "user": "@jhpalmieri"
}
```

I suppose this "depends" on #8244: it adds a bit to sagenb.misc.sageinspect.py from the patch there.  Overall, it looks fine: just the obvious changes.  Is there a good way to run doctests on all of sagenb?  The new sageinspect passes doctests with Sage installed, and I think it should without the rest of the Sage library, but I haven't checked it.

> I guess outside (non-Sage) projects delete some doctests?

I'm not sure what this refers to.



---

archive/issue_comments_073880.json:
```json
{
    "body": "You can run `make test` or `make ptest` in the root of the sagenb repository or run `sage -t -sagenb`, say, but these assume Sage is installed.\n\nI'm not aware of an easy way to doctest the standalone notebook.  We only recently got the tests to run with Sage (cf. #7650).\n\nSeveral notebook doctests and some `import`s not wrapped in `try-except` clauses refer to Sage modules.  It seems that most of the Sage-dependent doctests in `sagenb.misc.sageinspect` test Cython introspection, but right now, the notebook doesn't include Cython modules.  I don't know if outside projects depend on these Cython-related features.",
    "created_at": "2010-02-25T05:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73880",
    "user": "@qed777"
}
```

You can run `make test` or `make ptest` in the root of the sagenb repository or run `sage -t -sagenb`, say, but these assume Sage is installed.

I'm not aware of an easy way to doctest the standalone notebook.  We only recently got the tests to run with Sage (cf. #7650).

Several notebook doctests and some `import`s not wrapped in `try-except` clauses refer to Sage modules.  It seems that most of the Sage-dependent doctests in `sagenb.misc.sageinspect` test Cython introspection, but right now, the notebook doesn't include Cython modules.  I don't know if outside projects depend on these Cython-related features.



---

archive/issue_comments_073881.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-25T05:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73881",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073882.json:
```json
{
    "body": "Is this ticket meant to have the milestone \"Sage 4.3.4\"? In any case, it could only be closed once the relevant patch is merged in the SageNB repository, which is managed by the upstream SageNB team.",
    "created_at": "2010-03-03T03:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73882",
    "user": "mvngu"
}
```

Is this ticket meant to have the milestone "Sage 4.3.4"? In any case, it could only be closed once the relevant patch is merged in the SageNB repository, which is managed by the upstream SageNB team.



---

archive/issue_comments_073883.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-03T22:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73883",
    "user": "@jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_073884.json:
```json
{
    "body": "Here's a new patch; apply on top of the old one.  This changes one line to fix the doctest failure in 4.3.4.alpha0: `sage_getsourcelines(matrix,True)[1])` used to return 33, and now it returns 34.",
    "created_at": "2010-03-03T22:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73884",
    "user": "@jhpalmieri"
}
```

Here's a new patch; apply on top of the old one.  This changes one line to fix the doctest failure in 4.3.4.alpha0: `sage_getsourcelines(matrix,True)[1])` used to return 33, and now it returns 34.



---

archive/issue_comments_073885.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-03T22:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73885",
    "user": "@jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073886.json:
```json
{
    "body": "(This new patch is supposed to fix one of the bugs listed at #8430.  Only the \"new\" patch needs reviewing.)",
    "created_at": "2010-03-03T22:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73886",
    "user": "@jhpalmieri"
}
```

(This new patch is supposed to fix one of the bugs listed at #8430.  Only the "new" patch needs reviewing.)



---

archive/issue_comments_073887.json:
```json
{
    "body": "Attachment [trac_8324-new.patch](tarball://root/attachments/some-uuid/ticket8324/trac_8324-new.patch) by @jhpalmieri created at 2010-03-03 22:08:03\n\napply on top of other patch",
    "created_at": "2010-03-03T22:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73887",
    "user": "@jhpalmieri"
}
```

Attachment [trac_8324-new.patch](tarball://root/attachments/some-uuid/ticket8324/trac_8324-new.patch) by @jhpalmieri created at 2010-03-03 22:08:03

apply on top of other patch



---

archive/issue_comments_073888.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-04T07:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73888",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073889.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-04T22:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8324#issuecomment-73889",
    "user": "@qed777"
}
```

Resolution: fixed
