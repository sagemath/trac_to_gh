# Issue 4601: [with patch; needs review] optional magma interface -- fix all broken optional doctests by introducing _magma_init_(self, magma) signature

archive/issues_004601.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4601\n\n",
    "created_at": "2008-11-24T03:37:26Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch; needs review] optional magma interface -- fix all broken optional doctests by introducing _magma_init_(self, magma) signature",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4601",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/4601





---

archive/issue_comments_034426.json:
```json
{
    "body": "Attachment [sage-4601.patch](tarball://root/attachments/some-uuid/ticket4601/sage-4601.patch) by @williamstein created at 2008-11-24 03:39:44\n\nthis patch should be applied to sage-3.2.1.alpha0.  it should fix *all* optional doctest failures related to the magma interface!  Note that there is a problem with -only_optional=magma (#4600) so doctesting with that will still show a few false errors.",
    "created_at": "2008-11-24T03:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34426",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4601.patch](tarball://root/attachments/some-uuid/ticket4601/sage-4601.patch) by @williamstein created at 2008-11-24 03:39:44

this patch should be applied to sage-3.2.1.alpha0.  it should fix *all* optional doctest failures related to the magma interface!  Note that there is a problem with -only_optional=magma (#4600) so doctesting with that will still show a few false errors.



---

archive/issue_comments_034427.json:
```json
{
    "body": "There is one slight problem here with the doctests:\n\n```\nsage -t -long devel/sage/sage/interfaces/magma.py           \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/interfaces/magma.py\", line 1559:\n    sage: magma(S.gen_names()[1])\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_52[3]>\", line 1, in <module>\n        magma(S.gen_names()[Integer(1)])###line 1559:\n    sage: magma(S.gen_names()[1])\n    NameError: name 'S' is not defined\n**********************************************************************\n```\n\nBut that is obviously easy to fix :)\n\nI have read the patch and while it wouldn't hurt that mhansen for example would take another look everything looks peachy :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T21:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34427",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is one slight problem here with the doctests:

```
sage -t -long devel/sage/sage/interfaces/magma.py           
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/interfaces/magma.py", line 1559:
    sage: magma(S.gen_names()[1])
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[3]>", line 1, in <module>
        magma(S.gen_names()[Integer(1)])###line 1559:
    sage: magma(S.gen_names()[1])
    NameError: name 'S' is not defined
**********************************************************************
```

But that is obviously easy to fix :)

I have read the patch and while it wouldn't hurt that mhansen for example would take another look everything looks peachy :)

Cheers,

Michael



---

archive/issue_comments_034428.json:
```json
{
    "body": "Sorry, I forgot a # optional - magma.  I assume you're going to fix that... or are you requesting I do it?",
    "created_at": "2008-11-24T22:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34428",
    "user": "https://github.com/williamstein"
}
```

Sorry, I forgot a # optional - magma.  I assume you're going to fix that... or are you requesting I do it?



---

archive/issue_comments_034429.json:
```json
{
    "body": "I am fixing it and I will also put a dummy Magma executable in $PATH before the real one to make sure no missing \"#optional\" slips by :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T22:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34429",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am fixing it and I will also put a dummy Magma executable in $PATH before the real one to make sure no missing "#optional" slips by :)

Cheers,

Michael



---

archive/issue_events_004850.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-24T23:38:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4601#event-4850"
}
```



---

archive/issue_comments_034430.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1 - I will put a reviewers patch for the doctest issue in a second for completeness sake.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T23:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34430",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha1 - I will put a reviewers patch for the doctest issue in a second for completeness sake.

Cheers,

Michael



---

archive/issue_comments_034431.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-24T23:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34431",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
