# Issue 1360: Investigate long time graph_isom case

archive/issues_001360.json:
```json
{
    "body": "Assignee: mhansen\n\nThe full discussion is here.\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/4c615950a190e3f3\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1360\n\n",
    "created_at": "2007-12-02T04:21:06Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "Investigate long time graph_isom case",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1360",
    "user": "rlm"
}
```
Assignee: mhansen

The full discussion is here.

http://groups.google.com/group/sage-support/browse_thread/thread/4c615950a190e3f3


Issue created by migration from https://trac.sagemath.org/ticket/1360





---

archive/issue_comments_008710.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-02T04:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1360#issuecomment-8710",
    "user": "rlm"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008711.json:
```json
{
    "body": "Changing keywords from \"\" to \"graph isomorphism\".",
    "created_at": "2007-12-02T04:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1360#issuecomment-8711",
    "user": "rlm"
}
```

Changing keywords from "" to "graph isomorphism".



---

archive/issue_comments_008712.json:
```json
{
    "body": "Changing assignee from mhansen to rlm.",
    "created_at": "2007-12-02T04:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1360#issuecomment-8712",
    "user": "rlm"
}
```

Changing assignee from mhansen to rlm.



---

archive/issue_comments_008713.json:
```json
{
    "body": "Changing component from combinatorics to graph theory.",
    "created_at": "2007-12-17T15:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1360#issuecomment-8713",
    "user": "rlm"
}
```

Changing component from combinatorics to graph theory.



---

archive/issue_comments_008714.json:
```json
{
    "body": "Changing keywords from \"graph isomorphism\" to \"isomorphism, canonical labeling\".",
    "created_at": "2007-12-17T15:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1360#issuecomment-8714",
    "user": "rlm"
}
```

Changing keywords from "graph isomorphism" to "isomorphism, canonical labeling".



---

archive/issue_comments_008715.json:
```json
{
    "body": "After all of the patches that lead to the fix in #1961, this case no longer takes any real time. Once #1961 is merged, this ticket should also be closed!",
    "created_at": "2008-02-18T21:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1360#issuecomment-8715",
    "user": "rlm"
}
```

After all of the patches that lead to the fix in #1961, this case no longer takes any real time. Once #1961 is merged, this ticket should also be closed!



---

archive/issue_comments_008716.json:
```json
{
    "body": "In fact:\n\n```\nsage: time GAut = G.automorphism_group(partition=Pi)\nCPU times: user 0.10 s, sys: 0.04 s, total: 0.14 s\nWall time: 0.15\n```\n",
    "created_at": "2008-02-18T21:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1360#issuecomment-8716",
    "user": "rlm"
}
```

In fact:

```
sage: time GAut = G.automorphism_group(partition=Pi)
CPU times: user 0.10 s, sys: 0.04 s, total: 0.14 s
Wall time: 0.15
```




---

archive/issue_comments_008717.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-19T22:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1360#issuecomment-8717",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008718.json:
```json
{
    "body": "I ran the computation with #1961 applied and rlm confirms that the result is as expected:\n\n```\nsage: GAut = G.automorphism_group(partition=Pi)\nsage: GAut\nPermutation Group with generators [(1,6)(9,14)(18,28)(19,29)(34,44)(35,45)(50,60)(51,61)(66,76)(67,77), \n(6,7)(8,9)(28,30)(29,31)(32,34)(33,35)(60,62)(61,63)(64,66)(65,67), \n(5,8)(7,10)(26,32)(27,33)(30,36)(31,37)(58,64)(59,65)(62,68)(63,69), (4,5)(10,11)(24,26)(25,27)(36,38)(37,39)(56,58)(57,59)(68,70)(69,71), \n(3,4)(11,12)(22,24)(23,25)(38,40)(39,41)(54,56)(55,57)(70,72)(71,73),\n(2,3)(12,13)(20,22)(21,23)(40,42)(41,43)(52,54)(53,55)(72,74)(73,75)]\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-19T22:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1360#issuecomment-8718",
    "user": "mabshoff"
}
```

I ran the computation with #1961 applied and rlm confirms that the result is as expected:

```
sage: GAut = G.automorphism_group(partition=Pi)
sage: GAut
Permutation Group with generators [(1,6)(9,14)(18,28)(19,29)(34,44)(35,45)(50,60)(51,61)(66,76)(67,77), 
(6,7)(8,9)(28,30)(29,31)(32,34)(33,35)(60,62)(61,63)(64,66)(65,67), 
(5,8)(7,10)(26,32)(27,33)(30,36)(31,37)(58,64)(59,65)(62,68)(63,69), (4,5)(10,11)(24,26)(25,27)(36,38)(37,39)(56,58)(57,59)(68,70)(69,71), 
(3,4)(11,12)(22,24)(23,25)(38,40)(39,41)(54,56)(55,57)(70,72)(71,73),
(2,3)(12,13)(20,22)(21,23)(40,42)(41,43)(52,54)(53,55)(72,74)(73,75)]
```


Cheers,

Michael
