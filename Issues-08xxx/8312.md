# Issue 8312: speed up random_matrix creation

archive/issues_008312.json:
```json
{
    "body": "Assignee: jkantor\n\n`random_matrix` is really slow. This ticket seeks to improve it's performance, probably by using cython, a better vectorized routine, Numpy's `random` function or something else. Notice, that besides Numpy, also Matlab and others are much faster.\n\nTimings of Numpy's `random` with `random_matrix` on an Atom N270 netbook running Sage 4.3.2\n\n```\nsage: import numpy \nsage: matrix(numpy.random.normal(size=(1000,1000))) \n1000 x 1000 dense matrix over Real Double Field\nsage: a = random_matrix(RDF, 1000, 1000)\nsage: import numpy \nsage: %time _ = random_matrix(RDF, 1000, 1000)\nCPU times: user 17.51 s, sys: 0.10 s, total: 17.61 s\nWall time: 18.43 s\nsage: %time _ = matrix(numpy.random.normal(size=(1000,1000))) \nCPU times: user 0.40 s, sys: 0.04 s, total: 0.44 s\nWall time: 0.45 s\n```\n\nRelated to that: a `random_element` in `MatrixSpace` 1000x1000 is also faster (but still slower than Numpy)\n\n```\nsage: v = MatrixSpace(RDF,1000,1000)\nsage: %time _ = v.random_element()\nCPU times: user 3.45 s, sys: 0.01 s, total: 3.46 s\nWall time: 3.46 s\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8312\n\n",
    "created_at": "2010-02-20T13:54:06Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "speed up random_matrix creation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8312",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: jkantor

`random_matrix` is really slow. This ticket seeks to improve it's performance, probably by using cython, a better vectorized routine, Numpy's `random` function or something else. Notice, that besides Numpy, also Matlab and others are much faster.

Timings of Numpy's `random` with `random_matrix` on an Atom N270 netbook running Sage 4.3.2

```
sage: import numpy 
sage: matrix(numpy.random.normal(size=(1000,1000))) 
1000 x 1000 dense matrix over Real Double Field
sage: a = random_matrix(RDF, 1000, 1000)
sage: import numpy 
sage: %time _ = random_matrix(RDF, 1000, 1000)
CPU times: user 17.51 s, sys: 0.10 s, total: 17.61 s
Wall time: 18.43 s
sage: %time _ = matrix(numpy.random.normal(size=(1000,1000))) 
CPU times: user 0.40 s, sys: 0.04 s, total: 0.44 s
Wall time: 0.45 s
```

Related to that: a `random_element` in `MatrixSpace` 1000x1000 is also faster (but still slower than Numpy)

```
sage: v = MatrixSpace(RDF,1000,1000)
sage: %time _ = v.random_element()
CPU times: user 3.45 s, sys: 0.01 s, total: 3.46 s
Wall time: 3.46 s
```

Issue created by migration from https://trac.sagemath.org/ticket/8312





---

archive/issue_events_019881.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8312",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8312#event-19881"
}
```



---

archive/issue_events_019882.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8312",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8312#event-19882"
}
```



---

archive/issue_events_019883.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8312",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8312#event-19883"
}
```



---

archive/issue_events_019884.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8312",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8312#event-19884"
}
```



---

archive/issue_events_019885.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8312",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8312#event-19885"
}
```



---

archive/issue_events_019886.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8312",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8312#event-19886"
}
```



---

archive/issue_events_019887.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8312",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8312#event-19887"
}
```
