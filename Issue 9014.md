# Issue 9014: Implement a repr_prod

archive/issues_009014.json:
```json
{
    "body": "Assignee: @jasongrout\n\nCC:  @nthiery\n\nKeywords: repr product\n\nAs for linear combinaison, implement a method in misc 'repr_prod' to represent products. \n\n```\ndef repr_prodcomb(symbols, coeffs, is_latex=False):\n    r\"\"\"\n    Compute a string representation of a product combination of some\n    formal symbols\n    \"\"\"\n    bla bla bla\n\nsage: repr_prodcomb(['a','b','c'], [1,-2,-3])\n'a * b^-2 * c^-3'\nsage: repr_prodcomb([],[])\n'1'\n```\n\nThere is already a such function in sage/rings/polynomial/polynomial_element_generic.py\n\nWith categories will come FreeGroups(Gens), FreeMonoid(Gens), Free... Such futurs features motivate the need of this function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9014\n\n",
    "created_at": "2010-05-22T09:29:33Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Implement a repr_prod",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9014",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```
Assignee: @jasongrout

CC:  @nthiery

Keywords: repr product

As for linear combinaison, implement a method in misc 'repr_prod' to represent products. 

```
def repr_prodcomb(symbols, coeffs, is_latex=False):
    r"""
    Compute a string representation of a product combination of some
    formal symbols
    """
    bla bla bla

sage: repr_prodcomb(['a','b','c'], [1,-2,-3])
'a * b^-2 * c^-3'
sage: repr_prodcomb([],[])
'1'
```

There is already a such function in sage/rings/polynomial/polynomial_element_generic.py

With categories will come FreeGroups(Gens), FreeMonoid(Gens), Free... Such futurs features motivate the need of this function.

Issue created by migration from https://trac.sagemath.org/ticket/9014





---

archive/issue_comments_083246.json:
```json
{
    "body": "Feel free to sugest a better name (still sorry for my english...) and a better description.",
    "created_at": "2010-05-22T09:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9014#issuecomment-83246",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Feel free to sugest a better name (still sorry for my english...) and a better description.



---

archive/issue_events_022053.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9014",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9014#event-22053"
}
```



---

archive/issue_events_022054.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9014",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9014#event-22054"
}
```



---

archive/issue_events_022055.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9014",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9014#event-22055"
}
```



---

archive/issue_events_022056.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9014",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9014#event-22056"
}
```



---

archive/issue_events_022057.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9014",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9014#event-22057"
}
```



---

archive/issue_events_022058.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9014",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9014#event-22058"
}
```



---

archive/issue_events_022059.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9014",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9014#event-22059"
}
```
