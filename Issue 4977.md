# Issue 4977: vector(RR vector) doesn't create a new vector

archive/issues_004977.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nHi,\n\nIs there a reason why, in sage 3.2.2, the following works :\n\nsage: vector(vector((1, 6)))\n(1, 6)\n\nbut the following doesn't :\n\nsage: vector(vector((1, 6.8)))\nTraceback (most recent call last):\n...\nTypeError: _vector_() takes exactly one argument (0 given)\n\n???\n\nThank you,\n\nS\u00e9bastien Labb\u00e9\nUQAM\n\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4977\n\n",
    "created_at": "2009-01-14T21:44:34Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "vector(RR vector) doesn't create a new vector",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4977",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein


```
Hi,

Is there a reason why, in sage 3.2.2, the following works :

sage: vector(vector((1, 6)))
(1, 6)

but the following doesn't :

sage: vector(vector((1, 6.8)))
Traceback (most recent call last):
...
TypeError: _vector_() takes exactly one argument (0 given)

???

Thank you,

Sébastien Labbé
UQAM


```



Issue created by migration from https://trac.sagemath.org/ticket/4977





---

archive/issue_comments_037876.json:
```json
{
    "body": "I want also to mention that the same problem was occuring when using the Symbolic Ring :\n\n```\nsage: vector(vector(SR, (1, sqrt(2)) ) )\n```\n",
    "created_at": "2009-01-15T15:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4977#issuecomment-37876",
    "user": "https://github.com/seblabbe"
}
```

I want also to mention that the same problem was occuring when using the Symbolic Ring :

```
sage: vector(vector(SR, (1, sqrt(2)) ) )
```




---

archive/issue_comments_037877.json:
```json
{
    "body": "Attachment [4977.patch](tarball://root/attachments/some-uuid/ticket4977/4977.patch) by @ncalexan created at 2009-01-21 22:46:24",
    "created_at": "2009-01-21T22:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4977#issuecomment-37877",
    "user": "https://github.com/ncalexan"
}
```

Attachment [4977.patch](tarball://root/attachments/some-uuid/ticket4977/4977.patch) by @ncalexan created at 2009-01-21 22:46:24



---

archive/issue_comments_037878.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-01-22T00:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4977#issuecomment-37878",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_comments_037879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4977#issuecomment-37879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037880.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4977#issuecomment-37880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_events_005221.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T08:03:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4977#event-5221"
}
```
