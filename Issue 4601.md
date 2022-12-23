# Issue 4601: [with patch; needs review] optional magma interface -- fix all broken optional doctests by introducing _magma_init_(self, magma) signature

archive/issues_004601.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4601\n\n",
    "created_at": "2008-11-24T03:37:26Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] optional magma interface -- fix all broken optional doctests by introducing _magma_init_(self, magma) signature",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4601",
    "user": "was"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/4601





---

archive/issue_comments_034493.json:
```json
{
    "body": "Attachment\n\nthis patch should be applied to sage-3.2.1.alpha0.  it should fix *all* optional doctest failures related to the magma interface!  Note that there is a problem with -only_optional=magma (#4600) so doctesting with that will still show a few false errors.",
    "created_at": "2008-11-24T03:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34493",
    "user": "was"
}
```

Attachment

this patch should be applied to sage-3.2.1.alpha0.  it should fix *all* optional doctest failures related to the magma interface!  Note that there is a problem with -only_optional=magma (#4600) so doctesting with that will still show a few false errors.



---

archive/issue_comments_034494.json:
```json
{
    "body": "There is one slight problem here with the doctests:\n\n```\nsage -t -long devel/sage/sage/interfaces/magma.py           \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/interfaces/magma.py\", line 1559:\n    sage: magma(S.gen_names()[1])\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_52[3]>\", line 1, in <module>\n        magma(S.gen_names()[Integer(1)])###line 1559:\n    sage: magma(S.gen_names()[1])\n    NameError: name 'S' is not defined\n**********************************************************************\n```\n\nBut that is obviously easy to fix :)\n\nI have read the patch and while it wouldn't hurt that mhansen for example would take another look everything looks peachy :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T21:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34494",
    "user": "mabshoff"
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

archive/issue_comments_034495.json:
```json
{
    "body": "Sorry, I forgot a # optional - magma.  I assume you're going to fix that... or are you requesting I do it?",
    "created_at": "2008-11-24T22:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34495",
    "user": "was"
}
```

Sorry, I forgot a # optional - magma.  I assume you're going to fix that... or are you requesting I do it?



---

archive/issue_comments_034496.json:
```json
{
    "body": "I am fixing it and I will also put a dummy Magma executable in $PATH before the real one to make sure no missing \"#optional\" slips by :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T22:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34496",
    "user": "mabshoff"
}
```

I am fixing it and I will also put a dummy Magma executable in $PATH before the real one to make sure no missing "#optional" slips by :)

Cheers,

Michael



---

archive/issue_comments_034497.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1 - I will put a reviewers patch for the doctest issue in a second for completeness sake.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T23:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34497",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha1 - I will put a reviewers patch for the doctest issue in a second for completeness sake.

Cheers,

Michael



---

archive/issue_comments_034498.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-24T23:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4601#issuecomment-34498",
    "user": "mabshoff"
}
```

Resolution: fixed
