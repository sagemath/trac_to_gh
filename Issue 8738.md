# Issue 8738: @interact matrix input control ignores label

archive/issues_008738.json:
```json
{
    "body": "Assignee: jason, was\n\nTry this interact:\n\n```\n@interact\ndef f(M = (\"matrix \", random_matrix(QQ,3,4)), n=(\"an int\", 5)):\n    print \"The echelon form of the above matrix is:\"\n    print M.echelon_form()\n```\n\n\nThe first input control should be labeled \"matrix\", but it isn't.  Whoever added the matrix control for `@`interact, somehow did it in a way that breaks control labels. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8738\n\n",
    "created_at": "2010-04-21T17:05:43Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "@interact matrix input control ignores label",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8738",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was

Try this interact:

```
@interact
def f(M = ("matrix ", random_matrix(QQ,3,4)), n=("an int", 5)):
    print "The echelon form of the above matrix is:"
    print M.echelon_form()
```


The first input control should be labeled "matrix", but it isn't.  Whoever added the matrix control for `@`interact, somehow did it in a way that breaks control labels. 

Issue created by migration from https://trac.sagemath.org/ticket/8738





---

archive/issue_comments_079793.json:
```json
{
    "body": "I added the matrix control.  I had no idea that you could pass a tuple of (\"label\", control), so it's likely that it broke from ignorance.  Thanks for pointing out this feature!",
    "created_at": "2010-04-21T19:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8738#issuecomment-79793",
    "user": "https://github.com/jasongrout"
}
```

I added the matrix control.  I had no idea that you could pass a tuple of ("label", control), so it's likely that it broke from ignorance.  Thanks for pointing out this feature!



---

archive/issue_comments_079794.json:
```json
{
    "body": "I don't have a development copy of sagenb right now (it'd be nice of the local/lib/python2.6/site-packages/sagenb.../sagenb/notebook directory contained the mercurial repository so we could easily just change things and make a patch, without having to go get the spkg, extract it, install it with the develop option, etc.)\n\nHowever, to fix this, just change line 3750 of interact.py from:\n\n```\n        C = input_grid(default.nrows(), default.ncols(), default=default.list(), to_value=default.parent())\n\n```\n\n\n\nto\n\n\n```\n        C = input_grid(default.nrows(), default.ncols(), default=default.list(), to_value=default.parent(), label=label)\n\n```\n\n\nI have a comment about the design feature.  I notice from the code that this sets a default value *sometimes* (depending on the control):\n\n\n```\n@interact\ndef f(n=(2,[1,2,3,4,5])):\n    print n\n```\n\n\nHowever, this does *not set the default, because the first spot is overloaded to mean \"label\" and \"default value\", and \"label\" takes precedence:\n\n\n```\n@interact\ndef f(n=(\"b\",[\"a\",\"b\",\"c\"])):\n    print n\n```\n\n\nI think this interplay and double-meaning of the first argument confuses things too much.",
    "created_at": "2010-04-21T19:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8738#issuecomment-79794",
    "user": "https://github.com/jasongrout"
}
```

I don't have a development copy of sagenb right now (it'd be nice of the local/lib/python2.6/site-packages/sagenb.../sagenb/notebook directory contained the mercurial repository so we could easily just change things and make a patch, without having to go get the spkg, extract it, install it with the develop option, etc.)

However, to fix this, just change line 3750 of interact.py from:

```
        C = input_grid(default.nrows(), default.ncols(), default=default.list(), to_value=default.parent())

```



to


```
        C = input_grid(default.nrows(), default.ncols(), default=default.list(), to_value=default.parent(), label=label)

```


I have a comment about the design feature.  I notice from the code that this sets a default value *sometimes* (depending on the control):


```
@interact
def f(n=(2,[1,2,3,4,5])):
    print n
```


However, this does *not set the default, because the first spot is overloaded to mean "label" and "default value", and "label" takes precedence:


```
@interact
def f(n=("b",["a","b","c"])):
    print n
```


I think this interplay and double-meaning of the first argument confuses things too much.



---

archive/issue_events_021220.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21220"
}
```



---

archive/issue_events_021221.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21221"
}
```



---

archive/issue_events_021222.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21222"
}
```



---

archive/issue_events_021223.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21223"
}
```



---

archive/issue_events_021224.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21224"
}
```



---

archive/issue_events_021225.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21225"
}
```



---

archive/issue_events_021226.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21226"
}
```



---

archive/issue_comments_079795.json:
```json
{
    "body": "This is fixed by that very code in upstream https://github.com/sagemath/sagenb/pull/299 - we don't take care of the ambiguity, though!  I wonder what Sage cell and SMC do with that?",
    "created_at": "2014-12-10T21:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8738#issuecomment-79795",
    "user": "https://github.com/kcrisman"
}
```

This is fixed by that very code in upstream https://github.com/sagemath/sagenb/pull/299 - we don't take care of the ambiguity, though!  I wonder what Sage cell and SMC do with that?



---

archive/issue_comments_079796.json:
```json
{
    "body": "This would then be fixed in #10057, as this was merged.",
    "created_at": "2014-12-18T02:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8738#issuecomment-79796",
    "user": "https://github.com/kcrisman"
}
```

This would then be fixed in #10057, as this was merged.



---

archive/issue_events_021227.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2014-12-18T02:54:34Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21227"
}
```



---

archive/issue_events_021228.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2014-12-18T02:54:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21228"
}
```



---

archive/issue_comments_079797.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-18T02:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8738#issuecomment-79797",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079798.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-24T09:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8738#issuecomment-79798",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021229.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-12-24T09:48:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21229"
}
```



---

archive/issue_events_021230.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-12-24T09:48:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21230"
}
```



---

archive/issue_comments_079799.json:
```json
{
    "body": "Fixed by #10057.",
    "created_at": "2014-12-24T09:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8738#issuecomment-79799",
    "user": "https://github.com/jdemeyer"
}
```

Fixed by #10057.



---

archive/issue_comments_079800.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-01-13T01:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8738#issuecomment-79800",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_021231.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-01-13T01:22:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8738",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8738#event-21231"
}
```
