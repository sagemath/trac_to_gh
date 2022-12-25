# Issue 7740: Spped up MixedIntegerLinearProgram

archive/issues_007740.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @rlmill\n\nFrom Robert Miller :\n\n\n```\nsage: from sage.graphs.graph_coloring import vertex_coloring\nsage: g = graphs.CirculantGraph(120, [2,3,5,7])\nsage: vertex_coloring(g)\n```\n\n\nIt takes longer to set up the constraint than to solve the problem, on my laptop. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7740\n\n",
    "created_at": "2009-12-19T08:43:58Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Spped up MixedIntegerLinearProgram",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7740",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jkantor

CC:  @rlmill

From Robert Miller :


```
sage: from sage.graphs.graph_coloring import vertex_coloring
sage: g = graphs.CirculantGraph(120, [2,3,5,7])
sage: vertex_coloring(g)
```


It takes longer to set up the constraint than to solve the problem, on my laptop. 

Issue created by migration from https://trac.sagemath.org/ticket/7740





---

archive/issue_comments_066396.json:
```json
{
    "body": "Well, this time is spent as expected on the add_constraint function, which may spend time over considerations coming from symbolic computations, though I did not achieve to know where... When I am profiling your example I see :\n\n```\n\n25448/21366    0.529    0.000    0.695    0.000 complex_interval_field.py:257(__call__)\n     8642    0.427    0.000    1.136    0.000 complex_interval_field.py:330(random_element)\n     8642    0.106    0.000    0.117    0.000 complex_interval_field.py:325(gen)\n```\n\n\nThese functions are the ones responsible for the time spent defining the LP, but I could not find which line of add_constraint is calling them... If you have any idea, please tell me and I'll give it a look :-)",
    "created_at": "2009-12-20T17:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66396",
    "user": "https://github.com/nathanncohen"
}
```

Well, this time is spent as expected on the add_constraint function, which may spend time over considerations coming from symbolic computations, though I did not achieve to know where... When I am profiling your example I see :

```

25448/21366    0.529    0.000    0.695    0.000 complex_interval_field.py:257(__call__)
     8642    0.427    0.000    1.136    0.000 complex_interval_field.py:330(random_element)
     8642    0.106    0.000    0.117    0.000 complex_interval_field.py:325(gen)
```


These functions are the ones responsible for the time spent defining the LP, but I could not find which line of add_constraint is calling them... If you have any idea, please tell me and I'll give it a look :-)



---

archive/issue_comments_066397.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-12-20T17:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66397",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_066398.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-26T12:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66398",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_066399.json:
```json
{
    "body": "This patch adds to the file numerical.mip a class LinearFunction which avoid using the much more general symbolic expressions from Sage ( as we only need to define linear functions ). \n\nBefore :\n\n\n```\nsage: from sage.graphs.graph_coloring import vertex_coloring\nsage: g = graphs.CirculantGraph(120, [2,3,5,7])\nsage: timeit(\"vertex_coloring(g)\")\n5 loops, best of 3: 3.94 s per loop\n```\n\n\nAfter :\n\n\n```\nsage: from sage.graphs.graph_coloring import vertex_coloring\nsage: g = graphs.CirculantGraph(120, [2,3,5,7])\nsage: timeit(\"vertex_coloring(g)\")\n5 loops, best of 3: 2.18 s per loop\n```\n\n\nThe next way to speed up this class would be, methinks, to cythonize it. I tried it this time but got stuck by the fact that the solving functions ( solveCoin, solveGlpk ) are not directly included in Sage and installed by the packages... The best way would really be to move these sources into Sage. It would also solve solve the problem of having to update both packages and numerical.mip t the same time .. :-/\n\nNathann",
    "created_at": "2009-12-26T12:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66399",
    "user": "https://github.com/nathanncohen"
}
```

This patch adds to the file numerical.mip a class LinearFunction which avoid using the much more general symbolic expressions from Sage ( as we only need to define linear functions ). 

Before :


```
sage: from sage.graphs.graph_coloring import vertex_coloring
sage: g = graphs.CirculantGraph(120, [2,3,5,7])
sage: timeit("vertex_coloring(g)")
5 loops, best of 3: 3.94 s per loop
```


After :


```
sage: from sage.graphs.graph_coloring import vertex_coloring
sage: g = graphs.CirculantGraph(120, [2,3,5,7])
sage: timeit("vertex_coloring(g)")
5 loops, best of 3: 2.18 s per loop
```


The next way to speed up this class would be, methinks, to cythonize it. I tried it this time but got stuck by the fact that the solving functions ( solveCoin, solveGlpk ) are not directly included in Sage and installed by the packages... The best way would really be to move these sources into Sage. It would also solve solve the problem of having to update both packages and numerical.mip t the same time .. :-/

Nathann



---

archive/issue_comments_066400.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-28T08:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66400",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066401.json:
```json
{
    "body": "Before :\n\n```\nsage: g = graphs.WorldMap()\nsage: %timeit g.edge_connectivity()\n10 loops, best of 3: 1.29 s per loop\n```\n\n\nAfter :\n\n```\nsage: g = graphs.WorldMap()\nsage: %timeit g.edge_connectivity()\n10 loops, best of 3: 231 ms per loop\n```\n\n\nBut as mentionned earlier, we will have to find other ways to improve this class ! :-)\n\nNathann",
    "created_at": "2009-12-28T11:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66401",
    "user": "https://github.com/nathanncohen"
}
```

Before :

```
sage: g = graphs.WorldMap()
sage: %timeit g.edge_connectivity()
10 loops, best of 3: 1.29 s per loop
```


After :

```
sage: g = graphs.WorldMap()
sage: %timeit g.edge_connectivity()
10 loops, best of 3: 231 ms per loop
```


But as mentionned earlier, we will have to find other ways to improve this class ! :-)

Nathann



---

archive/issue_comments_066402.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-28T11:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66402",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066403.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-06T16:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66403",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066404.json:
```json
{
    "body": "Looks good to me! Aside from this typo:\n\"An elementary algebra algebra\"",
    "created_at": "2010-01-06T16:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66404",
    "user": "https://github.com/rlmill"
}
```

Looks good to me! Aside from this typo:
"An elementary algebra algebra"



---

archive/issue_comments_066405.json:
```json
{
    "body": "Attachment [trac_7740.patch](tarball://root/attachments/some-uuid/ticket7740/trac_7740.patch) by @nathanncohen created at 2010-01-09 08:16:31",
    "created_at": "2010-01-09T08:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66405",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7740.patch](tarball://root/attachments/some-uuid/ticket7740/trac_7740.patch) by @nathanncohen created at 2010-01-09 08:16:31



---

archive/issue_comments_066406.json:
```json
{
    "body": "Here it is ! :-)",
    "created_at": "2010-01-09T08:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66406",
    "user": "https://github.com/nathanncohen"
}
```

Here it is ! :-)



---

archive/issue_comments_066407.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-09T08:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66407",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T11:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66408",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_066409.json:
```json
{
    "body": "positive review",
    "created_at": "2010-01-13T11:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66409",
    "user": "https://github.com/rlmill"
}
```

positive review



---

archive/issue_events_007952.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-01-13T11:39:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7740#event-7952"
}
```



---

archive/issue_comments_066410.json:
```json
{
    "body": "Thank you again !!! I was longing for this one :-)\n\nNathann",
    "created_at": "2010-01-13T11:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66410",
    "user": "https://github.com/nathanncohen"
}
```

Thank you again !!! I was longing for this one :-)

Nathann



---

archive/issue_comments_066411.json:
```json
{
    "body": "Hi Nathan,\n\nSorry to pop up late into the discussion. What was the rationale for not using CombinatorialFreeModule(whatever_ring, ZZ)?\n\nFor the record, I very much hope that FreeModule(ring, infinity, sparse = True) will be available sometime soon. That will be a faster alternative.",
    "created_at": "2010-01-14T14:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66411",
    "user": "https://github.com/nthiery"
}
```

Hi Nathan,

Sorry to pop up late into the discussion. What was the rationale for not using CombinatorialFreeModule(whatever_ring, ZZ)?

For the record, I very much hope that FreeModule(ring, infinity, sparse = True) will be available sometime soon. That will be a faster alternative.



---

archive/issue_comments_066412.json:
```json
{
    "body": "Hello !\n\nAt first I used InfinitePolynomialRing, then plain \"vars\", then I just wondered why it was still very slow and just wondered what it would give if I were to write the symbolics myself to understand... As it was easy enough, I wrote something to try it on my computer, and ended up writing a patch to send the code. \n\nThis way, it stores the informations in a format that is optimal for what I need ( no powers --only linear functions--, sparse from the beginning, ... ). Since, I have also noticed that having my own symbolics would let me define expressions like double inequalities :\n\n0 < a + b < 9\n\nWhich I had been missing for a long time.. :-)\nThe main problem I have is that in many cases, the symbolics take most of the time spent on the computation of a matching (or other LP problems), which is quite disturbing ;-)\n\nNathann",
    "created_at": "2010-01-14T14:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7740#issuecomment-66412",
    "user": "https://github.com/nathanncohen"
}
```

Hello !

At first I used InfinitePolynomialRing, then plain "vars", then I just wondered why it was still very slow and just wondered what it would give if I were to write the symbolics myself to understand... As it was easy enough, I wrote something to try it on my computer, and ended up writing a patch to send the code. 

This way, it stores the informations in a format that is optimal for what I need ( no powers --only linear functions--, sparse from the beginning, ... ). Since, I have also noticed that having my own symbolics would let me define expressions like double inequalities :

0 < a + b < 9

Which I had been missing for a long time.. :-)
The main problem I have is that in many cases, the symbolics take most of the time spent on the computation of a matching (or other LP problems), which is quite disturbing ;-)

Nathann
