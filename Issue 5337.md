# Issue 5337: update French to tutorial to reflect the fact that "I in CC" works in tour_rings.rst

archive/issues_005337.json:
```json
{
    "body": "Assignee: tba\n\nOld French version:\n\n```\nIl y a une subtilit\u00e9 dans la d\u00e9finition des nombres complexes. Comme\nmentionn\u00e9 ci-dessus, le symbole  ``i`` repr\u00e9sente une racine carr\u00e9e de\n:math:`-1`, mais il s'agit d'une racine carr\u00e9e *formelle* de\n:math:`-1`, qui n'appartient pas aux nombres complexes. L'appel ``CC(i)``\nrenvoie la racine carr\u00e9e complexe de :math:`-1`.\n```\n\nNew English version:\n\n```\nThere is one subtlety in defining complex numbers: as mentioned\nabove, the symbol ``i`` represents a square root of :math:`-1`, but it is a\n*formal* square root of :math:`-1`.  Calling\n``CC(i)`` returns the complex square root of :math:`-1`.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5337\n\n",
    "created_at": "2009-02-22T18:08:19Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "update French to tutorial to reflect the fact that \"I in CC\" works in tour_rings.rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5337",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tba

Old French version:

```
Il y a une subtilité dans la définition des nombres complexes. Comme
mentionné ci-dessus, le symbole  ``i`` représente une racine carrée de
:math:`-1`, mais il s'agit d'une racine carrée *formelle* de
:math:`-1`, qui n'appartient pas aux nombres complexes. L'appel ``CC(i)``
renvoie la racine carrée complexe de :math:`-1`.
```

New English version:

```
There is one subtlety in defining complex numbers: as mentioned
above, the symbol ``i`` represents a square root of :math:`-1`, but it is a
*formal* square root of :math:`-1`.  Calling
``CC(i)`` returns the complex square root of :math:`-1`.
```


Issue created by migration from https://trac.sagemath.org/ticket/5337





---

archive/issue_comments_041032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-05T20:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5337#issuecomment-41032",
    "user": "https://github.com/mezzarobba"
}
```

Resolution: fixed



---

archive/issue_events_012443.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2009-03-05T20:09:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5337#event-12443"
}
```



---

archive/issue_comments_041033.json:
```json
{
    "body": "Hi Marc,\n\nI was wondering where this was fixed?  In general, we don't close tickets until the appropriate changes have been merged into the main tree.\n\n--Mike",
    "created_at": "2009-03-05T20:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5337#issuecomment-41033",
    "user": "https://github.com/mwhansen"
}
```

Hi Marc,

I was wondering where this was fixed?  In general, we don't close tickets until the appropriate changes have been merged into the main tree.

--Mike



---

archive/issue_comments_041034.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-03-05T20:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5337#issuecomment-41034",
    "user": "https://github.com/mwhansen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_041035.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-03-05T20:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5337#issuecomment-41035",
    "user": "https://github.com/mwhansen"
}
```

Changing status from closed to reopened.



---

archive/issue_events_012444.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-03-05T20:13:20Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5337#event-12444"
}
```



---

archive/issue_comments_041036.json:
```json
{
    "body": "Hi,\n\nReplying to [comment:2 mhansen]:\n> In general, we don't close tickets until the appropriate\n> changes have been merged into the main tree.\n\n\nActually I sent you an email asking precisely this question when I closed this ticket--but it seems you saw my action on the ticket first. Sorry for my mistake; I have just reopened #4318 too.\n\n-- Marc",
    "created_at": "2009-03-07T12:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5337#issuecomment-41036",
    "user": "https://github.com/mezzarobba"
}
```

Hi,

Replying to [comment:2 mhansen]:
> In general, we don't close tickets until the appropriate
> changes have been merged into the main tree.


Actually I sent you an email asking precisely this question when I closed this ticket--but it seems you saw my action on the ticket first. Sorry for my mistake; I have just reopened #4318 too.

-- Marc



---

archive/issue_comments_041037.json:
```json
{
    "body": "This should be fixed by the patch attached to #5850.",
    "created_at": "2009-04-27T21:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5337#issuecomment-41037",
    "user": "https://github.com/mezzarobba"
}
```

This should be fixed by the patch attached to #5850.



---

archive/issue_comments_041038.json:
```json
{
    "body": "Replying to [comment:4 mmezzarobba]:\n> This should be fixed by the patch attached to #5850.\n\n\nAnd now #5850 has been closed, so I think this ticket should be closed too.",
    "created_at": "2009-06-24T19:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5337#issuecomment-41038",
    "user": "https://github.com/mezzarobba"
}
```

Replying to [comment:4 mmezzarobba]:
> This should be fixed by the patch attached to #5850.


And now #5850 has been closed, so I think this ticket should be closed too.



---

archive/issue_events_012445.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-09T07:59:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5337#event-12445"
}
```



---

archive/issue_comments_041039.json:
```json
{
    "body": "Fixed via #5850.",
    "created_at": "2009-09-09T07:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5337#issuecomment-41039",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Fixed via #5850.



---

archive/issue_comments_041040.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-09T07:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5337#issuecomment-41040",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_012446.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-09T07:59:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5337",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5337#event-12446"
}
```
