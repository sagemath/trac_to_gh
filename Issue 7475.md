# Issue 7475: bug pickling ZZ.residue_field's

archive/issues_007475.json:
```json
{
    "body": "Assignee: tbd\n\n```\nsage: K = ZZ.residue_field(2)\nsage: dumps(K)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/flat.local/44250/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/s/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.dumps (sage/structure/sage_object.c:7951)()\n\n/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12800)()\n\nTypeError: 'NoneType' object is unsubscriptable\nsage: K = ZZ.residue_field(3)\nsage: dumps(K)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/flat.local/44250/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/s/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.dumps (sage/structure/sage_object.c:7951)()\n\n/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12800)()\n\nTypeError: 'NoneType' object is unsubscriptable\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7475\n\n",
    "created_at": "2009-11-16T17:41:54Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "bug pickling ZZ.residue_field's",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7475",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

```
sage: K = ZZ.residue_field(2)
sage: dumps(K)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/flat.local/44250/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/s/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.dumps (sage/structure/sage_object.c:7951)()

/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12800)()

TypeError: 'NoneType' object is unsubscriptable
sage: K = ZZ.residue_field(3)
sage: dumps(K)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/flat.local/44250/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/s/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.dumps (sage/structure/sage_object.c:7951)()

/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12800)()

TypeError: 'NoneType' object is unsubscriptable
```

Issue created by migration from https://trac.sagemath.org/ticket/7475





---

archive/issue_comments_062882.json:
```json
{
    "body": "Changing component from misc to pickling.",
    "created_at": "2009-11-16T17:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7475#issuecomment-62882",
    "user": "https://github.com/williamstein"
}
```

Changing component from misc to pickling.



---

archive/issue_comments_062883.json:
```json
{
    "body": "Changing assignee from tbd to @williamstein.",
    "created_at": "2009-11-16T17:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7475#issuecomment-62883",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from tbd to @williamstein.



---

archive/issue_comments_062884.json:
```json
{
    "body": "Attachment [pickle.sobj](tarball://root/attachments/some-uuid/ticket7475/pickle.sobj) by @itaibn created at 2012-02-26 04:47:34\n\nThe pickle in a different system",
    "created_at": "2012-02-26T04:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7475#issuecomment-62884",
    "user": "https://github.com/itaibn"
}
```

Attachment [pickle.sobj](tarball://root/attachments/some-uuid/ticket7475/pickle.sobj) by @itaibn created at 2012-02-26 04:47:34

The pickle in a different system



---

archive/issue_comments_062885.json:
```json
{
    "body": "I tested this and the bug doesn't appear in my system. I attached the pickle and the result of `pickle_explain` on the pickle.",
    "created_at": "2012-02-26T04:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7475#issuecomment-62885",
    "user": "https://github.com/itaibn"
}
```

I tested this and the bug doesn't appear in my system. I attached the pickle and the result of `pickle_explain` on the pickle.



---

archive/issue_comments_062886.json:
```json
{
    "body": "An explanation of the pickle",
    "created_at": "2012-02-26T04:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7475#issuecomment-62886",
    "user": "https://github.com/itaibn"
}
```

An explanation of the pickle



---

archive/issue_events_017717.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7475#event-17717"
}
```



---

archive/issue_comments_062887.json:
```json
{
    "body": "Attachment [pickle-explanation](tarball://root/attachments/some-uuid/ticket7475/pickle-explanation) by @jdemeyer created at 2013-08-13 15:35:53",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7475#issuecomment-62887",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [pickle-explanation](tarball://root/attachments/some-uuid/ticket7475/pickle-explanation) by @jdemeyer created at 2013-08-13 15:35:53



---

archive/issue_events_017718.json:
```json
{
    "actor": "https://github.com/itaibn",
    "created_at": "2013-09-03T10:19:54Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7475#event-17718"
}
```



---

archive/issue_events_017719.json:
```json
{
    "actor": "https://github.com/itaibn",
    "created_at": "2013-09-03T10:19:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7475#event-17719"
}
```



---

archive/issue_comments_062888.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-09-03T10:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7475#issuecomment-62888",
    "user": "https://github.com/itaibn"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062889.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-03T07:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7475#issuecomment-62889",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062890.json:
```json
{
    "body": "Looks good.",
    "created_at": "2014-02-03T07:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7475#issuecomment-62890",
    "user": "https://github.com/jdemeyer"
}
```

Looks good.



---

archive/issue_events_017720.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-02-03T07:26:11Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7475#event-17720"
}
```



---

archive/issue_events_017721.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-02-03T07:26:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7475#event-17721"
}
```



---

archive/issue_events_017722.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-02-03T22:59:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7475#event-17722"
}
```



---

archive/issue_comments_062891.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-03T22:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7475#issuecomment-62891",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
