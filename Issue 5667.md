# Issue 5667: matrix modified when operation should be rolled back

archive/issues_005667.json:
```json
{
    "body": "Assignee: @williamstein\n\nCheck this out:\n\n\n```\nsage: b\n\n[ 1  1  0 -1  1  0]\n[ 0  2  0 -5  3  1]\n[ 0  0  1  2 -1  0]\nsage: b[1] = b[1]/2\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/grout/.sage/temp/good/14543/_home_grout__sage_init_sage_0.py in <module>()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:6325)()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix._coerce_element (sage/matrix/matrix0.c:6667)()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/rings/rational.so in sage.rings.rational.Q_to_Z._call_ (sage/rings/rational.c:16008)()\n\nTypeError: no conversion of this rational to integer\nsage: b\n\n[ 1  1  0 -1  1  0]\n[ 0  1  0 -5  3  1]\n[ 0  0  1  2 -1  0]\nsage: b.base_ring()\nInteger Ring\n```\n\n\nThe matrix `b` was modified, but should not have been modified since the operation had an error.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5667\n\n",
    "created_at": "2009-04-02T19:42:42Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "matrix modified when operation should be rolled back",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5667",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Check this out:


```
sage: b

[ 1  1  0 -1  1  0]
[ 0  2  0 -5  3  1]
[ 0  0  1  2 -1  0]
sage: b[1] = b[1]/2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/good/14543/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:6325)()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix._coerce_element (sage/matrix/matrix0.c:6667)()

/home/grout/sage/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)()

/home/grout/sage/local/lib/python2.5/site-packages/sage/rings/rational.so in sage.rings.rational.Q_to_Z._call_ (sage/rings/rational.c:16008)()

TypeError: no conversion of this rational to integer
sage: b

[ 1  1  0 -1  1  0]
[ 0  1  0 -5  3  1]
[ 0  0  1  2 -1  0]
sage: b.base_ring()
Integer Ring
```


The matrix `b` was modified, but should not have been modified since the operation had an error.

Issue created by migration from https://trac.sagemath.org/ticket/5667





---

archive/issue_events_013323.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5667",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5667#event-13323"
}
```



---

archive/issue_events_013324.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5667",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5667#event-13324"
}
```



---

archive/issue_events_013325.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5667",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5667#event-13325"
}
```



---

archive/issue_events_013326.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5667",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5667#event-13326"
}
```



---

archive/issue_events_013327.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5667",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5667#event-13327"
}
```



---

archive/issue_events_013328.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5667",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5667#event-13328"
}
```



---

archive/issue_events_013329.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5667",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5667#event-13329"
}
```
