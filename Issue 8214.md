# Issue 8214: add better error message when symbolic expressions are called

archive/issues_008214.json:
```json
{
    "body": "Assignee: @burcin\n\nFrom sage-devel:\n\n\n```\nOn Sun, 7 Feb 2010 10:36:29 -0800 (PST)\nGustav Delius <gustav.delius@gmail.com> wrote:\n\n> I wonder whether it would be possible to give a better error message\n> when a user leaves out the multiplication operator in something like\n> x(x+1). Perhaps somthing like: \"Warning: you may have forgotten a\n> multiplication operator.\"\n> \n> Currently one gets the error message: \"DeprecationWarning:\n> Substitution using function-call syntax and unnamed arguments is\n> deprecated and will be removed from a future release of Sage; you can\n> use named arguments instead, like EXPR(x=...,y=...)\". This error\n> message is meaningful only to people who know the history of sage and\n> know that there used to be a confusing shorthand notation that allowed\n> something like x=a^2 to be interpreted as x(a)=a^2. I am glad that was\n> deprecated, but I think that the deprecation warning should be\n> preceeded by the warning about the possibility of a missing *.\n```\n\n\nHere is the thread:\n\nhttp://groups.google.com/group/sage-devel/t/de97f91d548cc0ec\n\nIncidentally, it's almost a year since this was deprecated, #5413. Maybe we can remove the deprecation message for good. :)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8214\n\n",
    "created_at": "2010-02-08T13:36:24Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "add better error message when symbolic expressions are called",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8214",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

From sage-devel:


```
On Sun, 7 Feb 2010 10:36:29 -0800 (PST)
Gustav Delius <gustav.delius@gmail.com> wrote:

> I wonder whether it would be possible to give a better error message
> when a user leaves out the multiplication operator in something like
> x(x+1). Perhaps somthing like: "Warning: you may have forgotten a
> multiplication operator."
> 
> Currently one gets the error message: "DeprecationWarning:
> Substitution using function-call syntax and unnamed arguments is
> deprecated and will be removed from a future release of Sage; you can
> use named arguments instead, like EXPR(x=...,y=...)". This error
> message is meaningful only to people who know the history of sage and
> know that there used to be a confusing shorthand notation that allowed
> something like x=a^2 to be interpreted as x(a)=a^2. I am glad that was
> deprecated, but I think that the deprecation warning should be
> preceeded by the warning about the possibility of a missing *.
```


Here is the thread:

http://groups.google.com/group/sage-devel/t/de97f91d548cc0ec

Incidentally, it's almost a year since this was deprecated, #5413. Maybe we can remove the deprecation message for good. :)

Issue created by migration from https://trac.sagemath.org/ticket/8214





---

archive/issue_comments_072313.json:
```json
{
    "body": "Burcin, I agree with your observation that the shortcut notation has now been deprecated for a long time. However the shortcut notation has not actually been disabled yet. Perhaps the warning should stay until that has happened.",
    "created_at": "2010-02-08T15:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8214#issuecomment-72313",
    "user": "https://trac.sagemath.org/admin/accounts/users/delius"
}
```

Burcin, I agree with your observation that the shortcut notation has now been deprecated for a long time. However the shortcut notation has not actually been disabled yet. Perhaps the warning should stay until that has happened.



---

archive/issue_comments_072314.json:
```json
{
    "body": "As to what the new message should be:\n\n```\nMaybe, but that message is not so helpful.  I guarantee you that you don't need to know the history of Sage to do\n\nsage: f=x^2\nsage: f(2)\n\nand expect 4.  You just need to attend an insufficiently pedantic algebra or calculus lecture :)\n```\n",
    "created_at": "2010-05-27T14:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8214#issuecomment-72314",
    "user": "https://github.com/kcrisman"
}
```

As to what the new message should be:

```
Maybe, but that message is not so helpful.  I guarantee you that you don't need to know the history of Sage to do

sage: f=x^2
sage: f(2)

and expect 4.  You just need to attend an insufficiently pedantic algebra or calculus lecture :)
```




---

archive/issue_comments_072315.json:
```json
{
    "body": "But definitely add some **serious** documentation in several spots people might look for why this is \"wrong\".  If it is ;-)\n\nSee also [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/5f2705b2b8d21593/b11079d8299a03b5), where the BDFL suggests it really is time to let it go.",
    "created_at": "2011-11-07T22:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8214#issuecomment-72315",
    "user": "https://github.com/kcrisman"
}
```

But definitely add some **serious** documentation in several spots people might look for why this is "wrong".  If it is ;-)

See also [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/5f2705b2b8d21593/b11079d8299a03b5), where the BDFL suggests it really is time to let it go.



---

archive/issue_comments_072316.json:
```json
{
    "body": "duplicate of #14270",
    "created_at": "2015-02-01T09:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8214#issuecomment-72316",
    "user": "https://github.com/rwst"
}
```

duplicate of #14270



---

archive/issue_comments_072317.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-02-01T09:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8214#issuecomment-72317",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072318.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-02-01T10:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8214#issuecomment-72318",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008416.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-02-08T15:28:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8214",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8214#event-8416"
}
```



---

archive/issue_comments_072319.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2015-02-08T15:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8214#issuecomment-72319",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
