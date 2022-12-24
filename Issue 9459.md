# Issue 9459: Implement a generic radical() function

archive/issues_009459.json:
```json
{
    "body": "Assignee: was\n\nCC:  mhansen\n\nRight now, there is a function radical() as member of IntegerRing_class.  But there is no generic radical() function:\n\n```\nsage: radical(100)\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/usr/local/src/sage-4.4.4/devel/sage-test/<ipython console> in <module>()\n\nNameError: name 'radical' is not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9459\n\n",
    "created_at": "2010-07-08T21:43:40Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Implement a generic radical() function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9459",
    "user": "jdemeyer"
}
```
Assignee: was

CC:  mhansen

Right now, there is a function radical() as member of IntegerRing_class.  But there is no generic radical() function:

```
sage: radical(100)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/usr/local/src/sage-4.4.4/devel/sage-test/<ipython console> in <module>()

NameError: name 'radical' is not defined
```


Issue created by migration from https://trac.sagemath.org/ticket/9459





---

archive/issue_comments_090679.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-10T14:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9459#issuecomment-90679",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090680.json:
```json
{
    "body": "The attached patch adds a radical() function, functions Factorization.radical() and Factorization.radical_value().  It also fixes a bug in the radical of a polynomial where the content was not accounted for.\n\nIt also changes the output of radical(), in a way which I think makes more sense: radical(0) now gives an error instead of returning 1 and the radical of a negative number is positive (instead of negative).\n\nIn order for all doctests to succeed, you need to apply also the patches for #9450.",
    "created_at": "2010-07-10T14:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9459#issuecomment-90680",
    "user": "jdemeyer"
}
```

The attached patch adds a radical() function, functions Factorization.radical() and Factorization.radical_value().  It also fixes a bug in the radical of a polynomial where the content was not accounted for.

It also changes the output of radical(), in a way which I think makes more sense: radical(0) now gives an error instead of returning 1 and the radical of a negative number is positive (instead of negative).

In order for all doctests to succeed, you need to apply also the patches for #9450.



---

archive/issue_comments_090681.json:
```json
{
    "body": "For what it's worth, groups and algebras have radicals too, so it might be worth putting a `#TODO` in the main definition that one might want `radical(G,type='nilpotent')` to work here if that ever is implemented/wrapped nicely (e.g. see [here](http://www.gap-system.org/Manuals/doc/htm/ref/CHAP037.htm#SSEC012.9)), so that future developers do not break the possibility of that syntax.",
    "created_at": "2010-08-06T19:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9459#issuecomment-90681",
    "user": "kcrisman"
}
```

For what it's worth, groups and algebras have radicals too, so it might be worth putting a `#TODO` in the main definition that one might want `radical(G,type='nilpotent')` to work here if that ever is implemented/wrapped nicely (e.g. see [here](http://www.gap-system.org/Manuals/doc/htm/ref/CHAP037.htm#SSEC012.9)), so that future developers do not break the possibility of that syntax.



---

archive/issue_comments_090682.json:
```json
{
    "body": "Applies well to 4.6.1.alpha1 and all tests pass.",
    "created_at": "2010-11-21T16:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9459#issuecomment-90682",
    "user": "cremona"
}
```

Applies well to 4.6.1.alpha1 and all tests pass.



---

archive/issue_comments_090683.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-21T16:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9459#issuecomment-90683",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090684.json:
```json
{
    "body": "Thanks, this is something I did in Leiden and totally forgot about.",
    "created_at": "2010-11-21T17:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9459#issuecomment-90684",
    "user": "jdemeyer"
}
```

Thanks, this is something I did in Leiden and totally forgot about.



---

archive/issue_comments_090685.json:
```json
{
    "body": "Replying to [comment:5 jdemeyer]:\n> Thanks, this is something I did in Leiden and totally forgot about.\n\nI cannot see a reason not to include it, despite the comment from kcrisman.",
    "created_at": "2010-11-21T17:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9459#issuecomment-90685",
    "user": "cremona"
}
```

Replying to [comment:5 jdemeyer]:
> Thanks, this is something I did in Leiden and totally forgot about.

I cannot see a reason not to include it, despite the comment from kcrisman.



---

archive/issue_comments_090686.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9459#issuecomment-90686",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_090687.json:
```json
{
    "body": "Attachment [9459.patch](tarball://root/attachments/some-uuid/ticket9459/9459.patch) by jdemeyer created at 2011-01-12 06:32:30",
    "created_at": "2011-01-12T06:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9459#issuecomment-90687",
    "user": "jdemeyer"
}
```

Attachment [9459.patch](tarball://root/attachments/some-uuid/ticket9459/9459.patch) by jdemeyer created at 2011-01-12 06:32:30
