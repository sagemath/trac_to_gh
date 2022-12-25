# Issue 3510: sage charpoly slower than Mma's for small integer (dim <=10) matrices

archive/issues_003510.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @haraldschilly\n\nThis timing difference ought to be fixed...\n\n```\nsage: mathematica(\"time[expr_, reps_] := Timing[Do[ClearSystemCache[]; expr;, >\nNull\nsage: mathematica(\"time[expr_, reps_] := Timing[Do[ClearSystemCache[]; expr;, {reps}]][[1]]/reps\")                                                              \nNull\nsage: mathematica(\"SetAttributes[time, HoldFirst]\")                                                                                              \nNull\nsage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(50)]                  \nsage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(25)]\nsage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(1,25)]\nsage: b=[mathematica(i) for i in a]                                                                                                                             \nsage: mma_timings=[mathematica(\"time[CharacteristicPolynomial[%s,t],20]\"%(m._name)) for m in b]                                                                 \nsage: sage_timings=[timeit(\"a[i].charpoly(); a[i]._clear_cache()\") for i in xrange(len(a))]                                                                     \n125 loops, best of 3: 989 \u00b5s per loop\n125 loops, best of 3: 2.83 ms per loop\n25 loops, best of 3: 3.37 ms per loop\n25 loops, best of 3: 3.99 ms per loop\n25 loops, best of 3: 4.18 ms per loop\n25 loops, best of 3: 4.18 ms per loop\n25 loops, best of 3: 5.73 ms per loop\n25 loops, best of 3: 6.66 ms per loop\n25 loops, best of 3: 8.36 ms per loop\n25 loops, best of 3: 8.57 ms per loop\n25 loops, best of 3: 9.41 ms per loop\n25 loops, best of 3: 11.6 ms per loop\n25 loops, best of 3: 13.3 ms per loop\n25 loops, best of 3: 13.3 ms per loop\n25 loops, best of 3: 16.2 ms per loop\n5 loops, best of 3: 17.9 ms per loop\n5 loops, best of 3: 21.1 ms per loop\n5 loops, best of 3: 24.6 ms per loop\n5 loops, best of 3: 24.7 ms per loop\n5 loops, best of 3: 28.4 ms per loop\n5 loops, best of 3: 30.4 ms per loop\n5 loops, best of 3: 33.2 ms per loop\n5 loops, best of 3: 36.2 ms per loop\n5 loops, best of 3: 36.6 ms per loop\nsage: mma_timings \n\n[0.0004000500000010843,\n 0.00019999999999930075,\n 0.0004000000000011883,\n 0.000600049999999279,\n 0.0008000499999993819,\n 0.0012001000000004176,\n 0.0016001000000006246,\n 0.0026001499999989217,\n 0.004000250000001096,\n 0.005000299999999682,\n 0.007600499999999302,\n 0.009800600000001224,\n 0.014000900000001421,\n 0.01760109999999937,\n 0.021401350000000537,\n 0.02840180000000124,\n 0.03700230000000092,\n 0.046602900000000586,\n 0.058003650000001405,\n 0.07060440000000084,\n 0.08600534999999886,\n 0.10280644999999965,\n 0.12460779999999874,\n 0.14660915000000047]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3510\n\n",
    "created_at": "2008-06-25T14:02:28Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "sage charpoly slower than Mma's for small integer (dim <=10) matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3510",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @haraldschilly

This timing difference ought to be fixed...

```
sage: mathematica("time[expr_, reps_] := Timing[Do[ClearSystemCache[]; expr;, >
Null
sage: mathematica("time[expr_, reps_] := Timing[Do[ClearSystemCache[]; expr;, {reps}]][[1]]/reps")                                                              
Null
sage: mathematica("SetAttributes[time, HoldFirst]")                                                                                              
Null
sage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(50)]                  
sage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(25)]
sage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(1,25)]
sage: b=[mathematica(i) for i in a]                                                                                                                             
sage: mma_timings=[mathematica("time[CharacteristicPolynomial[%s,t],20]"%(m._name)) for m in b]                                                                 
sage: sage_timings=[timeit("a[i].charpoly(); a[i]._clear_cache()") for i in xrange(len(a))]                                                                     
125 loops, best of 3: 989 µs per loop
125 loops, best of 3: 2.83 ms per loop
25 loops, best of 3: 3.37 ms per loop
25 loops, best of 3: 3.99 ms per loop
25 loops, best of 3: 4.18 ms per loop
25 loops, best of 3: 4.18 ms per loop
25 loops, best of 3: 5.73 ms per loop
25 loops, best of 3: 6.66 ms per loop
25 loops, best of 3: 8.36 ms per loop
25 loops, best of 3: 8.57 ms per loop
25 loops, best of 3: 9.41 ms per loop
25 loops, best of 3: 11.6 ms per loop
25 loops, best of 3: 13.3 ms per loop
25 loops, best of 3: 13.3 ms per loop
25 loops, best of 3: 16.2 ms per loop
5 loops, best of 3: 17.9 ms per loop
5 loops, best of 3: 21.1 ms per loop
5 loops, best of 3: 24.6 ms per loop
5 loops, best of 3: 24.7 ms per loop
5 loops, best of 3: 28.4 ms per loop
5 loops, best of 3: 30.4 ms per loop
5 loops, best of 3: 33.2 ms per loop
5 loops, best of 3: 36.2 ms per loop
5 loops, best of 3: 36.6 ms per loop
sage: mma_timings 

[0.0004000500000010843,
 0.00019999999999930075,
 0.0004000000000011883,
 0.000600049999999279,
 0.0008000499999993819,
 0.0012001000000004176,
 0.0016001000000006246,
 0.0026001499999989217,
 0.004000250000001096,
 0.005000299999999682,
 0.007600499999999302,
 0.009800600000001224,
 0.014000900000001421,
 0.01760109999999937,
 0.021401350000000537,
 0.02840180000000124,
 0.03700230000000092,
 0.046602900000000586,
 0.058003650000001405,
 0.07060440000000084,
 0.08600534999999886,
 0.10280644999999965,
 0.12460779999999874,
 0.14660915000000047]
```


Issue created by migration from https://trac.sagemath.org/ticket/3510





---

archive/issue_comments_024683.json:
```json
{
    "body": "Wait...something seems wrong with my comparison...",
    "created_at": "2008-06-25T14:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3510#issuecomment-24683",
    "user": "https://github.com/jasongrout"
}
```

Wait...something seems wrong with my comparison...



---

archive/issue_comments_024684.json:
```json
{
    "body": "Nope; Mma beats up through 10 vertices, it seems.  We're fine after that, though.",
    "created_at": "2008-06-25T14:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3510#issuecomment-24684",
    "user": "https://github.com/jasongrout"
}
```

Nope; Mma beats up through 10 vertices, it seems.  We're fine after that, though.



---

archive/issue_comments_024685.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-06-25T14:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3510#issuecomment-24685",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to minor.



---

archive/issue_events_008002.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3510#event-8002"
}
```



---

archive/issue_events_008003.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3510#event-8003"
}
```



---

archive/issue_events_008004.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3510#event-8004"
}
```



---

archive/issue_events_008005.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3510#event-8005"
}
```



---

archive/issue_events_008006.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3510#event-8006"
}
```



---

archive/issue_events_008007.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3510#event-8007"
}
```



---

archive/issue_events_008008.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3510#event-8008"
}
```



---

archive/issue_comments_024686.json:
```json
{
    "body": "I don't have access to Mathematica for comparison, but I just tried this in Sage and the timings seem to be much better than before. Can someone do a direct comparison to see if this ticket is still valid?\n\n```\nsage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(1,25)]\nsage: sage_timings=[timeit(\"a[i].charpoly(); a[i]._clear_cache()\") for i in xrange(len(a))]                                                                     \n625 loops, best of 3: 721 \u00b5s per loop\n625 loops, best of 3: 732 \u00b5s per loop\n625 loops, best of 3: 798 \u00b5s per loop\n625 loops, best of 3: 847 \u00b5s per loop\n625 loops, best of 3: 909 \u00b5s per loop\n625 loops, best of 3: 982 \u00b5s per loop\n625 loops, best of 3: 1.1 ms per loop\n625 loops, best of 3: 1.15 ms per loop\n625 loops, best of 3: 1.32 ms per loop\n625 loops, best of 3: 1.44 ms per loop\n625 loops, best of 3: 1.57 ms per loop\n125 loops, best of 3: 1.72 ms per loop\n125 loops, best of 3: 1.99 ms per loop\n125 loops, best of 3: 2.07 ms per loop\n125 loops, best of 3: 2.38 ms per loop\n125 loops, best of 3: 2.56 ms per loop\n125 loops, best of 3: 2.95 ms per loop\n125 loops, best of 3: 3.06 ms per loop\n125 loops, best of 3: 3.48 ms per loop\n125 loops, best of 3: 3.77 ms per loop\n125 loops, best of 3: 4.27 ms per loop\n125 loops, best of 3: 4.65 ms per loop\n125 loops, best of 3: 5.05 ms per loop\n125 loops, best of 3: 5.39 ms per loop\n```",
    "created_at": "2017-09-23T02:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3510#issuecomment-24686",
    "user": "https://github.com/kedlaya"
}
```

I don't have access to Mathematica for comparison, but I just tried this in Sage and the timings seem to be much better than before. Can someone do a direct comparison to see if this ticket is still valid?

```
sage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(1,25)]
sage: sage_timings=[timeit("a[i].charpoly(); a[i]._clear_cache()") for i in xrange(len(a))]                                                                     
625 loops, best of 3: 721 µs per loop
625 loops, best of 3: 732 µs per loop
625 loops, best of 3: 798 µs per loop
625 loops, best of 3: 847 µs per loop
625 loops, best of 3: 909 µs per loop
625 loops, best of 3: 982 µs per loop
625 loops, best of 3: 1.1 ms per loop
625 loops, best of 3: 1.15 ms per loop
625 loops, best of 3: 1.32 ms per loop
625 loops, best of 3: 1.44 ms per loop
625 loops, best of 3: 1.57 ms per loop
125 loops, best of 3: 1.72 ms per loop
125 loops, best of 3: 1.99 ms per loop
125 loops, best of 3: 2.07 ms per loop
125 loops, best of 3: 2.38 ms per loop
125 loops, best of 3: 2.56 ms per loop
125 loops, best of 3: 2.95 ms per loop
125 loops, best of 3: 3.06 ms per loop
125 loops, best of 3: 3.48 ms per loop
125 loops, best of 3: 3.77 ms per loop
125 loops, best of 3: 4.27 ms per loop
125 loops, best of 3: 4.65 ms per loop
125 loops, best of 3: 5.05 ms per loop
125 loops, best of 3: 5.39 ms per loop
```
