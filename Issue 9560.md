# Issue 9560: Symbolic expressions don't do arithmetic with bools nicely

archive/issues_009560.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  cwitty mstreng kcrisman\n\nIt's convenient to assume that True and False are equivalent to 1 and 0 in Python, but this doesn't work as expected with symbolic expressions:\n\n\n```\nsage: SR(5) + True; SR(5) * True; SR(5) - True\n2\n1\n0\nsage: 5 + True; 5 * True; 5 - True\n6\n5\n4\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9560\n\n",
    "created_at": "2010-07-21T09:06:17Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "Symbolic expressions don't do arithmetic with bools nicely",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9560",
    "user": "fredrik.johansson"
}
```
Assignee: burcin

CC:  cwitty mstreng kcrisman

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

archive/issue_comments_092156.json:
```json
{
    "body": "I understand that this is a Python convention, but I can't think of any situation where it would be useful. IMHO, adding a bool to an integer should be a type error. I'll raise the issue on sage-devel.",
    "created_at": "2010-07-24T21:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92156",
    "user": "burcin"
}
```

I understand that this is a Python convention, but I can't think of any situation where it would be useful. IMHO, adding a bool to an integer should be a type error. I'll raise the issue on sage-devel.



---

archive/issue_comments_092157.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-07-24T21:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92157",
    "user": "burcin"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_092158.json:
```json
{
    "body": "See\n[http://groups.google.com/group/sage-devel/browse_thread/thread/2821c770f3c62efd](http://groups.google.com/group/sage-devel/browse_thread/thread/2821c770f3c62efd) and [http://groups.google.com/group/sage-devel/browse_thread/thread/43798faef815a86d](http://groups.google.com/group/sage-devel/browse_thread/thread/43798faef815a86d)",
    "created_at": "2010-07-25T08:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92158",
    "user": "mstreng"
}
```

See
[http://groups.google.com/group/sage-devel/browse_thread/thread/2821c770f3c62efd](http://groups.google.com/group/sage-devel/browse_thread/thread/2821c770f3c62efd) and [http://groups.google.com/group/sage-devel/browse_thread/thread/43798faef815a86d](http://groups.google.com/group/sage-devel/browse_thread/thread/43798faef815a86d)



---

archive/issue_comments_092159.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-25T20:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92159",
    "user": "burcin"
}
```

Attachment



---

archive/issue_comments_092160.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-25T20:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92160",
    "user": "burcin"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_092161.json:
```json
{
    "body": "attachment:trac_9560-symbolic_bool_arith.patch *fixes* this problem...",
    "created_at": "2010-09-25T20:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92161",
    "user": "burcin"
}
```

attachment:trac_9560-symbolic_bool_arith.patch *fixes* this problem...



---

archive/issue_comments_092162.json:
```json
{
    "body": "This is a trivial patch. I don't understand why it hasn't been reviewed all this time. Fredrik, can you review this?",
    "created_at": "2011-05-30T21:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92162",
    "user": "burcin"
}
```

This is a trivial patch. I don't understand why it hasn't been reviewed all this time. Fredrik, can you review this?



---

archive/issue_comments_092163.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-08T18:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92163",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092164.json:
```json
{
    "body": "Probably it hasn't been reviewed for the same reason as people disagreed with it in the past - not really worth the effort :)\n\nMy favorites:\n\n```\nsage: e-True\ne - 1\nsage: pi+False\npi\n```\n\n\nAnyway, positive review.  It would have been nice to have an example with `False`, but that's not worth holding this up any further.",
    "created_at": "2011-06-08T18:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92164",
    "user": "kcrisman"
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

archive/issue_comments_092165.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-14T21:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9560#issuecomment-92165",
    "user": "jdemeyer"
}
```

Resolution: fixed
