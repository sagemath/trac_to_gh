# Issue 4017: Sage 3.1.2.alpha1 - PPC OSX: numerical noise in sage/stats/hmm/chmm.pyx

archive/issues_004017.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  devel/sage/sage/stats/hmm/chmm.pyx                \n**********************************************************************\nFile \"/Users/sagedevel/Desktop/sage-3.1.2.alpha1/tmp/chmm.py\", line 579:\n    sage: m.log_likelihood([ ([1,0,1,1], 10),  ([1,0,1,20], 0.1)  ])\nExpected:\n    -72.225116741468781\nGot:\n    -72.225116741468767\n**********************************************************************\nFile \"/Users/sagedevel/Desktop/sage-3.1.2.alpha1/tmp/chmm.py\", line 701:\n    sage: m\nExpected:\n    Gaussian Hidden Markov Model with 2 States\n    Transition matrix:\n    [1.0 0.0]\n    [0.0 1.0]\n    Emission parameters:\n    [(1.946539535984342, 0.70508296299241024), (2.0208156913293394, 0.70680033099099593)]\n    Initial probabilities: [0.28024729110782109, 0.71975270889217891]\nGot:\n    Gaussian Hidden Markov Model with 2 States\n    Transition matrix:\n    [1.0 0.0]\n    [0.0 1.0]\n    Emission parameters:\n    [(1.9465395359843427, 0.70508296299241024), (2.0208156913293389, 0.70680033099099593)]\n    Initial probabilities: [0.28024729110782093, 0.71975270889217924]\n**********************************************************************\nFile \"/Users/sagedevel/Desktop/sage-3.1.2.alpha1/tmp/chmm.py\", line 713:\n    sage: m\nExpected:\n    Gaussian Hidden Markov Model with 2 States\n    Transition matrix:\n    [1.0 0.0]\n    [0.0 1.0]\n    Emission parameters:\n    [(1.5851786151779879, 0.57264580740105153), (1.5945035666064733, 0.57928632238916189)]\n    Initial probabilities: [0.38546857052811945, 0.61453142947188055]\nGot:\n    Gaussian Hidden Markov Model with 2 States\n    Transition matrix:\n    [1.0 0.0]\n    [0.0 1.0]\n    Emission parameters:\n    [(1.5851786151779883, 0.57264580740105153), (1.5945035666064731, 0.57928632238916189)]\n    Initial probabilities: [0.38546857052811928, 0.61453142947188077]\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4017\n\n",
    "created_at": "2008-08-31T08:22:58Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Sage 3.1.2.alpha1 - PPC OSX: numerical noise in sage/stats/hmm/chmm.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4017",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
sage -t  devel/sage/sage/stats/hmm/chmm.pyx                
**********************************************************************
File "/Users/sagedevel/Desktop/sage-3.1.2.alpha1/tmp/chmm.py", line 579:
    sage: m.log_likelihood([ ([1,0,1,1], 10),  ([1,0,1,20], 0.1)  ])
Expected:
    -72.225116741468781
Got:
    -72.225116741468767
**********************************************************************
File "/Users/sagedevel/Desktop/sage-3.1.2.alpha1/tmp/chmm.py", line 701:
    sage: m
Expected:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [1.0 0.0]
    [0.0 1.0]
    Emission parameters:
    [(1.946539535984342, 0.70508296299241024), (2.0208156913293394, 0.70680033099099593)]
    Initial probabilities: [0.28024729110782109, 0.71975270889217891]
Got:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [1.0 0.0]
    [0.0 1.0]
    Emission parameters:
    [(1.9465395359843427, 0.70508296299241024), (2.0208156913293389, 0.70680033099099593)]
    Initial probabilities: [0.28024729110782093, 0.71975270889217924]
**********************************************************************
File "/Users/sagedevel/Desktop/sage-3.1.2.alpha1/tmp/chmm.py", line 713:
    sage: m
Expected:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [1.0 0.0]
    [0.0 1.0]
    Emission parameters:
    [(1.5851786151779879, 0.57264580740105153), (1.5945035666064733, 0.57928632238916189)]
    Initial probabilities: [0.38546857052811945, 0.61453142947188055]
Got:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [1.0 0.0]
    [0.0 1.0]
    Emission parameters:
    [(1.5851786151779883, 0.57264580740105153), (1.5945035666064731, 0.57928632238916189)]
    Initial probabilities: [0.38546857052811928, 0.61453142947188077]
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4017





---

archive/issue_comments_028917.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-31T08:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4017#issuecomment-28917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028918.json:
```json
{
    "body": "Attachment [trac_4017.patch](tarball://root/attachments/some-uuid/ticket4017/trac_4017.patch) by mabshoff created at 2008-08-31 08:43:19",
    "created_at": "2008-08-31T08:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4017#issuecomment-28918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4017.patch](tarball://root/attachments/some-uuid/ticket4017/trac_4017.patch) by mabshoff created at 2008-08-31 08:43:19



---

archive/issue_comments_028919.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-08-31T22:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4017#issuecomment-28919",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_004247.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-01T02:19:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4017",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4017#event-4247"
}
```



---

archive/issue_comments_028920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T02:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4017#issuecomment-28920",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028921.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T02:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4017#issuecomment-28921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha4
