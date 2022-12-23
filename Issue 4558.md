# Issue 4558: please update to sympy-0.6.3.spkg

archive/issues_004558.json:
```json
{
    "body": "Assignee: burcin\n\nThe spkg is here:\n\nhttp://sage.math.washington.edu/home/ondrej/spkg/sympy-0.6.3.spkg\n\nand also apply the attached patch, that fixes one failing test in test_sympy.py.\n\nThe Sage tests are still running, I'll report if all pass.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4558\n\n",
    "created_at": "2008-11-20T00:21:33Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "please update to sympy-0.6.3.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4558",
    "user": "certik"
}
```
Assignee: burcin

The spkg is here:

http://sage.math.washington.edu/home/ondrej/spkg/sympy-0.6.3.spkg

and also apply the attached patch, that fixes one failing test in test_sympy.py.

The Sage tests are still running, I'll report if all pass.

Issue created by migration from https://trac.sagemath.org/ticket/4558





---

archive/issue_comments_034153.json:
```json
{
    "body": "Attachment\n\nOk, all tests pass:\n\nhttp://sage.math.washington.edu/home/ondrej/sympy-0.6.3-sage-tests.log",
    "created_at": "2008-11-20T01:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4558#issuecomment-34153",
    "user": "certik"
}
```

Attachment

Ok, all tests pass:

http://sage.math.washington.edu/home/ondrej/sympy-0.6.3-sage-tests.log



---

archive/issue_comments_034154.json:
```json
{
    "body": "Ondrej,\n\nin the future make sure to use the sympy.spkg from the tree, not the one you build last time since the one in tree contains various cleanups from the review. Next time you do not use the latest upstream the review on my end will be an automatic \"needs work\" since I am tired of forward porting fixes I have done over and over again.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T00:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4558#issuecomment-34154",
    "user": "mabshoff"
}
```

Ondrej,

in the future make sure to use the sympy.spkg from the tree, not the one you build last time since the one in tree contains various cleanups from the review. Next time you do not use the latest upstream the review on my end will be an automatic "needs work" since I am tired of forward porting fixes I have done over and over again.

Cheers,

Michael



---

archive/issue_comments_034155.json:
```json
{
    "body": "Positive review on the spkg and the patch - I have some cleanups in \n\n http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/alpha0/sympy-0.6.3.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T00:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4558#issuecomment-34155",
    "user": "mabshoff"
}
```

Positive review on the spkg and the patch - I have some cleanups in 

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/alpha0/sympy-0.6.3.p0.spkg

Cheers,

Michael



---

archive/issue_comments_034156.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-23T00:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4558#issuecomment-34156",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_comments_034157.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-23T00:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4558#issuecomment-34157",
    "user": "mabshoff"
}
```

Resolution: fixed
