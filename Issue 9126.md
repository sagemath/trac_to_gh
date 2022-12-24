# Issue 9126: Symbolic arguments() method

archive/issues_009126.json:
```json
{
    "body": "Assignee: @burcin\n\nRight now, the following works:\n\n```\nsage: a=(x+y)\nsage: a.arguments()\n(x, y)\n```\n\nHowever, we deprecated the following a long time ago:\n\n```\nsage: a(1,2)\n/Users/grout/sage/local/lib/python2.6/site-packages/IPython/iplib.py:2073:\nDeprecationWarning: Substitution using function-call syntax and unnamed\narguments is deprecated and will be removed from a future release of\nSage; you can use named arguments instead, like EXPR(x=..., y=...)\n   exec code_obj in self.user_global_ns, self.user_ns\n3\n```\n\nI propose that a.arguments() should return a deprecation warning:\n\n```\nsage: a.arguments()\n/Users/grout/sage/local/lib/python2.6/site-packages/IPython/iplib.py:2073:\nDeprecationWarning: (Since Sage version 4.4.2) symbolic expressions do\nnot have default callable arguments.  Please use the variables() method\n   exec code_obj in self.user_global_ns, self.user_ns\n(x, y)\n```\n\nThis will impact other things as well, since apparently things have been\nusing .arguments() when they should have been using .variables().  I can\npost a patch for this.  Here, I'm just calling for comment, especially\nfrom those that think this will mess everything up in some way.\n\nNote that callable functions will still have sensible return values:\n\n```\nsage: f(x,y)=x+y\nsage: f.arguments()\n(x, y) \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9126\n\n",
    "created_at": "2010-06-03T05:11:07Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Symbolic arguments() method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9126",
    "user": "@jasongrout"
}
```
Assignee: @burcin

Right now, the following works:

```
sage: a=(x+y)
sage: a.arguments()
(x, y)
```

However, we deprecated the following a long time ago:

```
sage: a(1,2)
/Users/grout/sage/local/lib/python2.6/site-packages/IPython/iplib.py:2073:
DeprecationWarning: Substitution using function-call syntax and unnamed
arguments is deprecated and will be removed from a future release of
Sage; you can use named arguments instead, like EXPR(x=..., y=...)
   exec code_obj in self.user_global_ns, self.user_ns
3
```

I propose that a.arguments() should return a deprecation warning:

```
sage: a.arguments()
/Users/grout/sage/local/lib/python2.6/site-packages/IPython/iplib.py:2073:
DeprecationWarning: (Since Sage version 4.4.2) symbolic expressions do
not have default callable arguments.  Please use the variables() method
   exec code_obj in self.user_global_ns, self.user_ns
(x, y)
```

This will impact other things as well, since apparently things have been
using .arguments() when they should have been using .variables().  I can
post a patch for this.  Here, I'm just calling for comment, especially
from those that think this will mess everything up in some way.

Note that callable functions will still have sensible return values:

```
sage: f(x,y)=x+y
sage: f.arguments()
(x, y) 
```


Issue created by migration from https://trac.sagemath.org/ticket/9126





---

archive/issue_comments_084905.json:
```json
{
    "body": "Attachment [trac-9126-arguments.patch](tarball://root/attachments/some-uuid/ticket9126/trac-9126-arguments.patch) by @jasongrout created at 2010-06-03 05:12:31",
    "created_at": "2010-06-03T05:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84905",
    "user": "@jasongrout"
}
```

Attachment [trac-9126-arguments.patch](tarball://root/attachments/some-uuid/ticket9126/trac-9126-arguments.patch) by @jasongrout created at 2010-06-03 05:12:31



---

archive/issue_comments_084906.json:
```json
{
    "body": "I've attached a rough patch which needs work to finish fixing the ramifications of this change.",
    "created_at": "2010-06-03T05:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84906",
    "user": "@jasongrout"
}
```

I've attached a rough patch which needs work to finish fixing the ramifications of this change.



---

archive/issue_comments_084907.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-03T05:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84907",
    "user": "@jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_084908.json:
```json
{
    "body": "dup of #32227, can close",
    "created_at": "2021-09-06T05:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84908",
    "user": "@mkoeppe"
}
```

dup of #32227, can close



---

archive/issue_comments_084909.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-09-06T05:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84909",
    "user": "@mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084910.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-11-20T21:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84910",
    "user": "@orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084911.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-11-20T23:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84911",
    "user": "@mkoeppe"
}
```

Resolution: invalid
