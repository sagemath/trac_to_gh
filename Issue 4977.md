# Issue 4977: vector(RR vector) doesn't create a new vector

archive/issues_004977.json:
```json
{
    "body": "Assignee: was\n\n\n```\nHi,\n\nIs there a reason why, in sage 3.2.2, the following works :\n\nsage: vector(vector((1, 6)))\n(1, 6)\n\nbut the following doesn't :\n\nsage: vector(vector((1, 6.8)))\nTraceback (most recent call last):\n...\nTypeError: _vector_() takes exactly one argument (0 given)\n\n???\n\nThank you,\n\nS\u00e9bastien Labb\u00e9\nUQAM\n\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4977\n\n",
    "created_at": "2009-01-14T21:44:34Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "vector(RR vector) doesn't create a new vector",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4977",
    "user": "jason"
}
```
Assignee: was


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

archive/issue_comments_037948.json:
```json
{
    "body": "I want also to mention that the same problem was occuring when using the Symbolic Ring :\n\n```\nsage: vector(vector(SR, (1, sqrt(2)) ) )\n```\n",
    "created_at": "2009-01-15T15:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4977#issuecomment-37948",
    "user": "slabbe"
}
```

I want also to mention that the same problem was occuring when using the Symbolic Ring :

```
sage: vector(vector(SR, (1, sqrt(2)) ) )
```




---

archive/issue_comments_037949.json:
```json
{
    "body": "Attachment [4977.patch](tarball://root/attachments/some-uuid/ticket4977/4977.patch) by ncalexan created at 2009-01-21 22:46:24",
    "created_at": "2009-01-21T22:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4977#issuecomment-37949",
    "user": "ncalexan"
}
```

Attachment [4977.patch](tarball://root/attachments/some-uuid/ticket4977/4977.patch) by ncalexan created at 2009-01-21 22:46:24



---

archive/issue_comments_037950.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-01-22T00:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4977#issuecomment-37950",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_037951.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4977#issuecomment-37951",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037952.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4977#issuecomment-37952",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1
