# Issue 5404: deprecate numerical_sqrt

archive/issues_005404.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  jason\n\nNow we have sqrt(a, prec=1000). Also, it doesn't even do what it says. \n\n\n```\nsage: numerical_sqrt(3)\nsqrt(3)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5404\n\n",
    "created_at": "2009-02-28T21:55:42Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "deprecate numerical_sqrt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5404",
    "user": "robertwb"
}
```
Assignee: burcin

CC:  jason

Now we have sqrt(a, prec=1000). Also, it doesn't even do what it says. 


```
sage: numerical_sqrt(3)
sqrt(3)
```


Issue created by migration from https://trac.sagemath.org/ticket/5404





---

archive/issue_comments_041756.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-02-28T22:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5404#issuecomment-41756",
    "user": "robertwb"
}
```

Changing priority from major to minor.



---

archive/issue_comments_041757.json:
```json
{
    "body": "Attachment [5404-numerical_sqrt.patch](tarball://root/attachments/some-uuid/ticket5404/5404-numerical_sqrt.patch) by robertwb created at 2009-02-28 22:02:51\n\nNot used anywhere in the Sage source.",
    "created_at": "2009-02-28T22:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5404#issuecomment-41757",
    "user": "robertwb"
}
```

Attachment [5404-numerical_sqrt.patch](tarball://root/attachments/some-uuid/ticket5404/5404-numerical_sqrt.patch) by robertwb created at 2009-02-28 22:02:51

Not used anywhere in the Sage source.



---

archive/issue_comments_041758.json:
```json
{
    "body": "It would be good to mention the deprecation in the docstring of the function as well.\n\nWe could also change the doctests, which test the wrong function now anyway, to demonstrate using sqrt with the prec parameter.",
    "created_at": "2009-03-01T15:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5404#issuecomment-41758",
    "user": "burcin"
}
```

It would be good to mention the deprecation in the docstring of the function as well.

We could also change the doctests, which test the wrong function now anyway, to demonstrate using sqrt with the prec parameter.



---

archive/issue_comments_041759.json:
```json
{
    "body": "The deprecation message doesn't make sense to me:\n\n```\nsage: sqrt(10.1, prec=5)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: sqrt() got an unexpected keyword argument 'prec'\n```\n\nI think the issue here is that in real_mpfr.pyx, the sqrt method doesn't accept a 'prec' argument. If I do `search_def('sqrt')`, I see lots of sqrt methods without a prec argument.  Perhaps the sqrt function in calculus/calculus.py should check for a `TypeError` in addition to an `AttributeError`?  In any case, we can't give a deprecation message which suggests using code which doesn't work.\n\nWe also need some doctests in the sqrt function in calculus/calculus.py using all of the advertised arguments.",
    "created_at": "2009-05-10T22:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5404#issuecomment-41759",
    "user": "jhpalmieri"
}
```

The deprecation message doesn't make sense to me:

```
sage: sqrt(10.1, prec=5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: sqrt() got an unexpected keyword argument 'prec'
```

I think the issue here is that in real_mpfr.pyx, the sqrt method doesn't accept a 'prec' argument. If I do `search_def('sqrt')`, I see lots of sqrt methods without a prec argument.  Perhaps the sqrt function in calculus/calculus.py should check for a `TypeError` in addition to an `AttributeError`?  In any case, we can't give a deprecation message which suggests using code which doesn't work.

We also need some doctests in the sqrt function in calculus/calculus.py using all of the advertised arguments.



---

archive/issue_comments_041760.json:
```json
{
    "body": "See #6171 for a possible fix to the 'prec' issue.  Maybe with this fix, the patch here is okay?",
    "created_at": "2009-05-31T21:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5404#issuecomment-41760",
    "user": "jhpalmieri"
}
```

See #6171 for a possible fix to the 'prec' issue.  Maybe with this fix, the patch here is okay?



---

archive/issue_comments_041761.json:
```json
{
    "body": "Okay, I think with #6171, my main complaint is taken care of.  Here's a new patch; the only difference is the docstring.  The code gets a positive review from me, so if you're happy with my docstring, give the ticket a positive review.\n\nThis depends on #6171, not to apply and to pass doctests, but in the sense that the deprecation message is inaccurate without #6171.",
    "created_at": "2009-05-31T23:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5404#issuecomment-41761",
    "user": "jhpalmieri"
}
```

Okay, I think with #6171, my main complaint is taken care of.  Here's a new patch; the only difference is the docstring.  The code gets a positive review from me, so if you're happy with my docstring, give the ticket a positive review.

This depends on #6171, not to apply and to pass doctests, but in the sense that the deprecation message is inaccurate without #6171.



---

archive/issue_comments_041762.json:
```json
{
    "body": "Attachment [numerical_sqrt.patch](tarball://root/attachments/some-uuid/ticket5404/numerical_sqrt.patch) by jhpalmieri created at 2009-05-31 23:40:07\n\napply only this patch",
    "created_at": "2009-05-31T23:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5404#issuecomment-41762",
    "user": "jhpalmieri"
}
```

Attachment [numerical_sqrt.patch](tarball://root/attachments/some-uuid/ticket5404/numerical_sqrt.patch) by jhpalmieri created at 2009-05-31 23:40:07

apply only this patch



---

archive/issue_comments_041763.json:
```json
{
    "body": "Looks good to me.\n\nMerged numerical_sqrt.patch in 4.0.1.rc1.",
    "created_at": "2009-06-04T19:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5404#issuecomment-41763",
    "user": "mhansen"
}
```

Looks good to me.

Merged numerical_sqrt.patch in 4.0.1.rc1.



---

archive/issue_comments_041764.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T19:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5404#issuecomment-41764",
    "user": "mhansen"
}
```

Resolution: fixed
