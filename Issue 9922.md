# Issue 9922: Minimum Feedback Arc/Edge set through constraint generation

archive/issues_009922.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  abmasse mvngu\n\nBecause of the friend who made me work on Feedback Arc Set and is already the cause of #9911, I implemented another LP formulation of this problem using constraint generation. The performances are....... IMPROVED `:-)`\n\nIf you have any question while reviewing this, please do not hesitate. As usual, I tried my best to make the code understandable `:-)`\n\nRequire #9911\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9923\n\n",
    "created_at": "2010-09-16T20:25:16Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Minimum Feedback Arc/Edge set through constraint generation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9922",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  abmasse mvngu

Because of the friend who made me work on Feedback Arc Set and is already the cause of #9911, I implemented another LP formulation of this problem using constraint generation. The performances are....... IMPROVED `:-)`

If you have any question while reviewing this, please do not hesitate. As usual, I tried my best to make the code understandable `:-)`

Require #9911

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9923





---

archive/issue_comments_098773.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-16T20:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98773",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098774.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-23T15:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98774",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098775.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-30T23:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98775",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098776.json:
```json
{
    "body": "Rebased on top of #9911 and its dependencies.\n\nNathann",
    "created_at": "2010-10-23T16:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98776",
    "user": "ncohen"
}
```

Rebased on top of #9911 and its dependencies.

Nathann



---

archive/issue_comments_098777.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-11-04T11:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98777",
    "user": "mvngu"
}
```

Attachment



---

archive/issue_comments_098778.json:
```json
{
    "body": "Nathann,\n\nCan you say more about the difference between the two patches? Why should we merge the slower patch? I'm a bit confused over this....",
    "created_at": "2011-01-12T03:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98778",
    "user": "rlm"
}
```

Nathann,

Can you say more about the difference between the two patches? Why should we merge the slower patch? I'm a bit confused over this....



---

archive/issue_comments_098779.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-12T03:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98779",
    "user": "gbe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098780.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-01-12T09:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98780",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_098781.json:
```json
{
    "body": "Hello Robert !!!\n\n> Can you say more about the difference between the two patches? Why should we merge the slower patch? I'm a bit confused over this....\n\nOf course ! I should have been way more explicit when I replaced the former patch by the new one `^^;`\n\nThis patch is about finding a smallest (cardinality) subset of vertices (or edges, but let's just talk about vertices) in a digraph whose removal makes it acyclic. It is solved by a LP in a following way : \ngive me the set of vertices you have now, and I will tell you if you did not forget any circuit. If you forgot a circuit, I give it to you (the LP), and you compute again a *smallest set of vertices such that each circuit your know is cut by at least a vertex*.\n\nThe LP solver does not know the whole graph. Is just knows a small list of circuits. With this information, it computes a possible set of vertices, and cycles are added if the given set is not sufficient.\n\nSo, there are three parts in this method : the first one is a loop doing what I said just above : getting the current solution, checking whether is it acyclic, adding a constraint (the cycle) if it is not. The second one is the LP itself, of course (knowing a list of circuits, find the set -- the hard part), and a routine checking whether the digraph without the vertices returned by the solver is acyclic.\n\nIn the first patch, everything was written in Cython. I was worried it wouldn't be as clear as Python, plus it was again defining a function somewhere, this function being called dy digraph.py, and most importantly, I thought it would be easier/faster to review this way `^^;`. Besides, I was redefining a function checking whether the graph is acyclic in a funny way : optimised for my use, while the standard one present in Sage was still using NetworkX. In #10432, the method checking whether the digraph is acyclic has been rewritten in Cython, so even though my version was a tad more optimised for my use, it is still way faster than using NetworkX.\n\nWith the new patch, the loop (is this set good?) is in Python, the LP is still solved by C libraries, and the routine checking the solution is in Cython (not so bad) because of #10432. My tricks avoided to make a copy of the graph at each loop, which is clearly nice, but I wondered whether this was reason enough to keep a looong copy of the routine optimised for my needs, and Cython code instead of Python when it is not really needed (this part is not really bad. The only problem is the graph copy).\n\nConsidering this version is already infinitely better than what we already have, I thought it would not be so bad to waste a few milliseconds, when the size of the problems we solve now would have made any computer crash out of memory previously.\n\n(patch updated, still being debated) `:-)`\n\nNathann",
    "created_at": "2011-01-12T09:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98781",
    "user": "ncohen"
}
```

Hello Robert !!!

> Can you say more about the difference between the two patches? Why should we merge the slower patch? I'm a bit confused over this....

Of course ! I should have been way more explicit when I replaced the former patch by the new one `^^;`

This patch is about finding a smallest (cardinality) subset of vertices (or edges, but let's just talk about vertices) in a digraph whose removal makes it acyclic. It is solved by a LP in a following way : 
give me the set of vertices you have now, and I will tell you if you did not forget any circuit. If you forgot a circuit, I give it to you (the LP), and you compute again a *smallest set of vertices such that each circuit your know is cut by at least a vertex*.

The LP solver does not know the whole graph. Is just knows a small list of circuits. With this information, it computes a possible set of vertices, and cycles are added if the given set is not sufficient.

So, there are three parts in this method : the first one is a loop doing what I said just above : getting the current solution, checking whether is it acyclic, adding a constraint (the cycle) if it is not. The second one is the LP itself, of course (knowing a list of circuits, find the set -- the hard part), and a routine checking whether the digraph without the vertices returned by the solver is acyclic.

In the first patch, everything was written in Cython. I was worried it wouldn't be as clear as Python, plus it was again defining a function somewhere, this function being called dy digraph.py, and most importantly, I thought it would be easier/faster to review this way `^^;`. Besides, I was redefining a function checking whether the graph is acyclic in a funny way : optimised for my use, while the standard one present in Sage was still using NetworkX. In #10432, the method checking whether the digraph is acyclic has been rewritten in Cython, so even though my version was a tad more optimised for my use, it is still way faster than using NetworkX.

With the new patch, the loop (is this set good?) is in Python, the LP is still solved by C libraries, and the routine checking the solution is in Cython (not so bad) because of #10432. My tricks avoided to make a copy of the graph at each loop, which is clearly nice, but I wondered whether this was reason enough to keep a looong copy of the routine optimised for my needs, and Cython code instead of Python when it is not really needed (this part is not really bad. The only problem is the graph copy).

Considering this version is already infinitely better than what we already have, I thought it would not be so bad to waste a few milliseconds, when the size of the problems we solve now would have made any computer crash out of memory previously.

(patch updated, still being debated) `:-)`

Nathann



---

archive/issue_comments_098782.json:
```json
{
    "body": "Attachment\n\nThanks for explaining Nathann, that greatly clarifies things.",
    "created_at": "2011-01-12T20:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98782",
    "user": "gbe"
}
```

Attachment

Thanks for explaining Nathann, that greatly clarifies things.



---

archive/issue_comments_098783.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-12T21:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98783",
    "user": "ncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_098784.json:
```json
{
    "body": "Ran tests with the following applied:\n\n```\nrlmill@geom:/scratch/rlmill/sage-4.6.1.rc0/devel/sage-main$ hg qap\ntrac_9911.patch\n9911_fix.patch\ntrac_10435.patch\ntrac_10432.patch\ntrac_9923-python.patch\n```\n\n\nLooks good!",
    "created_at": "2011-01-16T04:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98784",
    "user": "rlm"
}
```

Ran tests with the following applied:

```
rlmill@geom:/scratch/rlmill/sage-4.6.1.rc0/devel/sage-main$ hg qap
trac_9911.patch
9911_fix.patch
trac_10435.patch
trac_10432.patch
trac_9923-python.patch
```


Looks good!



---

archive/issue_comments_098785.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-16T04:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98785",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098786.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-26T22:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9922#issuecomment-98786",
    "user": "jdemeyer"
}
```

Resolution: fixed
