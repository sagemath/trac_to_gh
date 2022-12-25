# Issue 5663: Infinite loop in multiplication of 0 (parent Symbolic Ring) and 1.0000000000000000 (parent Real Field with 60 bits of precision)!

archive/issues_005663.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  @robertwb\n\nKeywords: coercion symbolic ring real field\n\n```\nsage: SR(0) * RealField(60)(1)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1027, 0))\n\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/home/ncalexan/.sage/temp/sage.math.washington.edu/19397/_home_ncalexan__sage_init_sage_0.py in <module>()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/element.so in sage.stru\\\ncture.element.RingElement.__mul__ (sage/structure/element.c:10558)()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.struc\\\nture.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6543)()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.struc\\\nture.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:11646)()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.struc\\\nture.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12920)()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.struc\\\nture.parent.Parent.get_action (sage/structure/parent.c:11816)()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\\\ntructure.parent_old.Parent._get_action_ (sage/structure/parent_old.c:8141)()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\\\ntructure.parent_old.Parent.get_action_c (sage/structure/parent_old.c:2998)()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\\\ntructure.parent_old.Parent.get_action_impl (sage/structure/parent_old.c:3333)()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\\\ntructure.parent_old.Parent.get_action_c_impl (sage/structure/parent_old.c:4193)()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\\\ntructure.parent_old._register_pair (sage/structure/parent_old.c:9303)()\n\nNotImplementedError: Infinite loop in multiplication of\n                                       0 (parent Symbolic Ring) and 1.0000000000000000 (parent Real Field with 60 bits of precision)!\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5663\n\n",
    "closed_at": "2009-06-05T03:07:28Z",
    "created_at": "2009-04-02T03:20:32Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Infinite loop in multiplication of 0 (parent Symbolic Ring) and 1.0000000000000000 (parent Real Field with 60 bits of precision)!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5663",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @robertwb

CC:  @robertwb

Keywords: coercion symbolic ring real field

```
sage: SR(0) * RealField(60)(1)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1027, 0))

---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/19397/_home_ncalexan__sage_init_sage_0.py in <module>()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/element.so in sage.stru\
cture.element.RingElement.__mul__ (sage/structure/element.c:10558)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.struc\
ture.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6543)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.struc\
ture.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:11646)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.struc\
ture.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12920)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.struc\
ture.parent.Parent.get_action (sage/structure/parent.c:11816)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\
tructure.parent_old.Parent._get_action_ (sage/structure/parent_old.c:8141)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\
tructure.parent_old.Parent.get_action_c (sage/structure/parent_old.c:2998)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\
tructure.parent_old.Parent.get_action_impl (sage/structure/parent_old.c:3333)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\
tructure.parent_old.Parent.get_action_c_impl (sage/structure/parent_old.c:4193)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\
tructure.parent_old._register_pair (sage/structure/parent_old.c:9303)()

NotImplementedError: Infinite loop in multiplication of
                                       0 (parent Symbolic Ring) and 1.0000000000000000 (parent Real Field with 60 bits of precision)!
```

Issue created by migration from https://trac.sagemath.org/ticket/5663





---

archive/issue_events_013313.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-05T03:07:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5663",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5663#event-13313"
}
```



---

archive/issue_events_013314.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-05T03:07:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5663",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5663#event-13314"
}
```



---

archive/issue_comments_044206.json:
```json
{
    "body": "This is taken care of with the switch to the new symbolics:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: SR(0) * RealField(60)(1)\n0\n```",
    "created_at": "2009-06-05T03:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5663#issuecomment-44206",
    "user": "https://github.com/mwhansen"
}
```

This is taken care of with the switch to the new symbolics:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: SR(0) * RealField(60)(1)
0
```



---

archive/issue_comments_044207.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-05T03:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5663#issuecomment-44207",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid
