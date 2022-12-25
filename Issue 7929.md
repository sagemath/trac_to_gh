# Issue 7929: Pickling fails for some residue fields

archive/issues_007929.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCatched with #7921:\n\n\n```\nsage: K.<a> = NumberField(x^3-17)\nsage: P = K.ideal(29).factor()[0][0]\nsage: k = K.residue_field(P) # indirect doctest\nsage: F = ZZ.residue_field(17)  # indirect doctest\nsage: loads(dumps(k))\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"sage_object.pyx\", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)\n  File \"ring.pyx\", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)\nTypeError: 'NoneType' object is unsubscriptable\n\nsage: loads(dumps(k.an_element()))\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"sage_object.pyx\", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)\n  File \"ring.pyx\", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)\nTypeError: 'NoneType' object is unsubscriptable\n\nsage: loads(dumps(F))\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"sage_object.pyx\", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)\n  File \"ring.pyx\", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)\nTypeError: 'NoneType' object is unsubscriptable\n\nsage: loads(dumps(F.an_element()))\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"sage_object.pyx\", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)\n  File \"ring.pyx\", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)\nTypeError: 'NoneType' object is unsubscriptable\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7929\n\n",
    "created_at": "2010-01-14T14:09:55Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Pickling fails for some residue fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7929",
    "user": "https://github.com/nthiery"
}
```
Assignee: @loefflerd

Catched with #7921:


```
sage: K.<a> = NumberField(x^3-17)
sage: P = K.ideal(29).factor()[0][0]
sage: k = K.residue_field(P) # indirect doctest
sage: F = ZZ.residue_field(17)  # indirect doctest
sage: loads(dumps(k))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "sage_object.pyx", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)
  File "ring.pyx", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)
TypeError: 'NoneType' object is unsubscriptable

sage: loads(dumps(k.an_element()))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "sage_object.pyx", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)
  File "ring.pyx", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)
TypeError: 'NoneType' object is unsubscriptable

sage: loads(dumps(F))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "sage_object.pyx", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)
  File "ring.pyx", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)
TypeError: 'NoneType' object is unsubscriptable

sage: loads(dumps(F.an_element()))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "sage_object.pyx", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)
  File "ring.pyx", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)
TypeError: 'NoneType' object is unsubscriptable
```


Issue created by migration from https://trac.sagemath.org/ticket/7929





---

archive/issue_comments_068913.json:
```json
{
    "body": "This works in 4.7.2.",
    "created_at": "2011-11-19T02:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7929#issuecomment-68913",
    "user": "https://github.com/roed314"
}
```

This works in 4.7.2.



---

archive/issue_comments_068914.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-19T04:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7929#issuecomment-68914",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068915.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-19T04:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7929#issuecomment-68915",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068916.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-11-26T13:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7929#issuecomment-68916",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_008145.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-11-26T13:07:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7929",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7929#event-8145"
}
```
