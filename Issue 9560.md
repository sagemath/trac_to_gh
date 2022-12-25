# Issue 9560: Symbolic expressions don't do arithmetic with bools nicely

archive/issues_009560.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  cwitty @mstreng @kcrisman\n\nIt's convenient to assume that True and False are equivalent to 1 and 0 in Python, but this doesn't work as expected with symbolic expressions:\n\n\n```\nsage: SR(5) + True; SR(5) * True; SR(5) - True\n2\n1\n0\nsage: 5 + True; 5 * True; 5 - True\n6\n5\n4\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9560\n\n",
    "created_at": "2010-07-21T09:06:17Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "Symbolic expressions don't do arithmetic with bools nicely",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9560",
    "user": "https://github.com/fredrik-johansson"
}
```
Assignee: @burcin

CC:  cwitty @mstreng @kcrisman

It's convenient to assume that True and False are equivalent to 1 and 0 in Python, but this doesn't work as expected with symbolic expressions:


```
sage: SR(5) + True; SR(5) * True; SR(5) - True
2
1
0
sage: 5 + True; 5 * True; 5 - True
6
5
4
```


Issue created by migration from https://trac.sagemath.org/ticket/9560





---

archive/issue_comments_092002.json:
```json
{
    "body": "I understand that this is a Python convention, but I can't think of any situation where it would be useful. IMHO, adding a bool to an integer should be a type error. I'll raise the issue on sage-devel.",
    "created_at": "2010-07-24T21:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92002",
    "user": "https://github.com/burcin"
}
```

I understand that this is a Python convention, but I can't think of any situation where it would be useful. IMHO, adding a bool to an integer should be a type error. I'll raise the issue on sage-devel.



---

archive/issue_comments_092003.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-07-24T21:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92003",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_info.



---

archive/issue_events_023805.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2010-07-24T21:03:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "milestone": "sage-4.5.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9560#event-23805"
}
```



---

archive/issue_comments_092004.json:
```json
{
    "body": "See\n[http://groups.google.com/group/sage-devel/browse_thread/thread/2821c770f3c62efd](http://groups.google.com/group/sage-devel/browse_thread/thread/2821c770f3c62efd) and [http://groups.google.com/group/sage-devel/browse_thread/thread/43798faef815a86d](http://groups.google.com/group/sage-devel/browse_thread/thread/43798faef815a86d)",
    "created_at": "2010-07-25T08:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92004",
    "user": "https://github.com/mstreng"
}
```

See
[http://groups.google.com/group/sage-devel/browse_thread/thread/2821c770f3c62efd](http://groups.google.com/group/sage-devel/browse_thread/thread/2821c770f3c62efd) and [http://groups.google.com/group/sage-devel/browse_thread/thread/43798faef815a86d](http://groups.google.com/group/sage-devel/browse_thread/thread/43798faef815a86d)



---

archive/issue_comments_092005.json:
```json
{
    "body": "Attachment [trac_9560-symbolic_bool_arith.patch](tarball://root/attachments/some-uuid/ticket9560/trac_9560-symbolic_bool_arith.patch) by @burcin created at 2010-09-25 20:30:34",
    "created_at": "2010-09-25T20:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92005",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9560-symbolic_bool_arith.patch](tarball://root/attachments/some-uuid/ticket9560/trac_9560-symbolic_bool_arith.patch) by @burcin created at 2010-09-25 20:30:34



---

archive/issue_comments_092006.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-25T20:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92006",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_092007.json:
```json
{
    "body": "attachment:trac_9560-symbolic_bool_arith.patch *fixes* this problem...",
    "created_at": "2010-09-25T20:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92007",
    "user": "https://github.com/burcin"
}
```

attachment:trac_9560-symbolic_bool_arith.patch *fixes* this problem...



---

archive/issue_comments_092008.json:
```json
{
    "body": "This is a trivial patch. I don't understand why it hasn't been reviewed all this time. Fredrik, can you review this?",
    "created_at": "2011-05-30T21:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92008",
    "user": "https://github.com/burcin"
}
```

This is a trivial patch. I don't understand why it hasn't been reviewed all this time. Fredrik, can you review this?



---

archive/issue_comments_092009.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-08T18:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92009",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092010.json:
```json
{
    "body": "Probably it hasn't been reviewed for the same reason as people disagreed with it in the past - not really worth the effort :)\n\nMy favorites:\n\n```\nsage: e-True\ne - 1\nsage: pi+False\npi\n```\n\n\nAnyway, positive review.  It would have been nice to have an example with `False`, but that's not worth holding this up any further.",
    "created_at": "2011-06-08T18:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92010",
    "user": "https://github.com/kcrisman"
}
```

Probably it hasn't been reviewed for the same reason as people disagreed with it in the past - not really worth the effort :)

My favorites:

```
sage: e-True
e - 1
sage: pi+False
pi
```


Anyway, positive review.  It would have been nice to have an example with `False`, but that's not worth holding this up any further.



---

archive/issue_events_023806.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-06-14T21:08:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9560#event-23806"
}
```



---

archive/issue_comments_092011.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-14T21:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92011",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
