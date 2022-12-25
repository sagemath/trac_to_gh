# Issue 5173: Sage 3.3.a5: doctest failure in sage/rings/polynomial/polynomial_element.pyx due to print order of roots

archive/issues_005173.json:
```json
{
    "body": "Assignee: mabshoff\n\nObserved on cleo and iras:\n\n```\nsage -t -long \"devel/sage/sage/rings/polynomial/polynomial_element.pyx\"\n**********************************************************************\nFile \"/home/mabshoff/build-3.3.alpha5/sage-3.3.alpha5-cleo/devel/sage/sage/rings/polynomial/polynomial_element.pyx\", line 3418:\n    sage: p.roots(ring=ComplexIntervalField(200))\nExpected:\n    [(1.167303978261418684256045899854842180720560371525489039140082?, 1), \n(-0.76488443360058472602982318770854173032899665194736756700778? - \n0.35247154603172624931794709140258105439420648082424733283770?*I, 1), \n(-0.76488443360058472602982318770854173032899665194736756700778? + \n0.35247154603172624931794709140258105439420648082424733283770?*I, 1), \n(0.18123244446987538390180023778112063996871646618462304743774? - \n1.08395410131771066843034449298076657427364024315511565430114?*I, 1), \n(0.18123244446987538390180023778112063996871646618462304743774? + \n1.08395410131771066843034449298076657427364024315511565430114?*I, 1)]\nGot:\n    [(1.167303978261418684256045899854842180720560371525489039140082?, 1), \n(0.18123244446987538390180023778112063996871646618462304743774? - \n1.08395410131771066843034449298076657427364024315511565430114?*I, 1), \n(-0.76488443360058472602982318770854173032899665194736756700778? - \n0.35247154603172624931794709140258105439420648082424733283770?*I, 1), \n(-0.76488443360058472602982318770854173032899665194736756700778? + \n0.35247154603172624931794709140258105439420648082424733283770?*I, 1), \n(0.18123244446987538390180023778112063996871646618462304743774? + \n1.08395410131771066843034449298076657427364024315511565430114?*I, 1)]\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5173\n\n",
    "created_at": "2009-02-04T14:12:13Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Sage 3.3.a5: doctest failure in sage/rings/polynomial/polynomial_element.pyx due to print order of roots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5173",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Observed on cleo and iras:

```
sage -t -long "devel/sage/sage/rings/polynomial/polynomial_element.pyx"
**********************************************************************
File "/home/mabshoff/build-3.3.alpha5/sage-3.3.alpha5-cleo/devel/sage/sage/rings/polynomial/polynomial_element.pyx", line 3418:
    sage: p.roots(ring=ComplexIntervalField(200))
Expected:
    [(1.167303978261418684256045899854842180720560371525489039140082?, 1), 
(-0.76488443360058472602982318770854173032899665194736756700778? - 
0.35247154603172624931794709140258105439420648082424733283770?*I, 1), 
(-0.76488443360058472602982318770854173032899665194736756700778? + 
0.35247154603172624931794709140258105439420648082424733283770?*I, 1), 
(0.18123244446987538390180023778112063996871646618462304743774? - 
1.08395410131771066843034449298076657427364024315511565430114?*I, 1), 
(0.18123244446987538390180023778112063996871646618462304743774? + 
1.08395410131771066843034449298076657427364024315511565430114?*I, 1)]
Got:
    [(1.167303978261418684256045899854842180720560371525489039140082?, 1), 
(0.18123244446987538390180023778112063996871646618462304743774? - 
1.08395410131771066843034449298076657427364024315511565430114?*I, 1), 
(-0.76488443360058472602982318770854173032899665194736756700778? - 
0.35247154603172624931794709140258105439420648082424733283770?*I, 1), 
(-0.76488443360058472602982318770854173032899665194736756700778? + 
0.35247154603172624931794709140258105439420648082424733283770?*I, 1), 
(0.18123244446987538390180023778112063996871646618462304743774? + 
1.08395410131771066843034449298076657427364024315511565430114?*I, 1)]
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/5173





---

archive/issue_comments_039554.json:
```json
{
    "body": "Attachment [trac5173-cmp-complex-converts.patch](tarball://root/attachments/some-uuid/ticket5173/trac5173-cmp-complex-converts.patch) by cwitty created at 2009-02-05 04:17:20\n\nThe code didn't do the right thing at all with ComplexIntervalField(200), because it was trying to compare incomparable values, so it fell back to comparing the types.  Fixed in the attached patch by adding an explicit conversion to the appropriate type.",
    "created_at": "2009-02-05T04:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5173#issuecomment-39554",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac5173-cmp-complex-converts.patch](tarball://root/attachments/some-uuid/ticket5173/trac5173-cmp-complex-converts.patch) by cwitty created at 2009-02-05 04:17:20

The code didn't do the right thing at all with ComplexIntervalField(200), because it was trying to compare incomparable values, so it fell back to comparing the types.  Fixed in the attached patch by adding an explicit conversion to the appropriate type.



---

archive/issue_comments_039555.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T10:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5173#issuecomment-39555",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_039556.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T10:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5173#issuecomment-39556",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_events_005423.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-05T10:49:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5173",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5173#event-5423"
}
```



---

archive/issue_comments_039557.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T10:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5173#issuecomment-39557",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
