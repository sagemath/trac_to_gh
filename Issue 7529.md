# Issue 7529: Maximum Average Degree of a graph

archive/issues_007529.json:
```json
{
    "body": "Assignee: rlm\n\nThe maximum average degree of a graph is the maximum, over all subgraphs H of a graph G, of average_degree(H).\n\nThis can be computed in polynomial time ( though I do not know of any practical way to do it ) and could be used, for example, as a certificate for negative answers in #7528.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7529\n\n",
    "created_at": "2009-11-25T09:57:52Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Maximum Average Degree of a graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7529",
    "user": "ncohen"
}
```
Assignee: rlm

The maximum average degree of a graph is the maximum, over all subgraphs H of a graph G, of average_degree(H).

This can be computed in polynomial time ( though I do not know of any practical way to do it ) and could be used, for example, as a certificate for negative answers in #7528.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7529





---

archive/issue_comments_063818.json:
```json
{
    "body": "After some thinking, is was easy to write it through Linear Programming :-)\n\nI also wrote a pretty elementary average_degree function, that I had been missing for some time !\n\nNathann",
    "created_at": "2010-01-28T11:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7529#issuecomment-63818",
    "user": "ncohen"
}
```

After some thinking, is was easy to write it through Linear Programming :-)

I also wrote a pretty elementary average_degree function, that I had been missing for some time !

Nathann



---

archive/issue_comments_063819.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T11:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7529#issuecomment-63819",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063820.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-28T11:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7529#issuecomment-63820",
    "user": "ncohen"
}
```

Attachment



---

archive/issue_comments_063821.json:
```json
{
    "body": "For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/\n\nNathann",
    "created_at": "2010-04-08T21:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7529#issuecomment-63821",
    "user": "ncohen"
}
```

For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/

Nathann



---

archive/issue_comments_063822.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-12T12:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7529#issuecomment-63822",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063823.json:
```json
{
    "body": "This installs fine on 4.4.2.a0, passes sage -testall both before and after installing glpk (except for unrelated failures).\n\nAlso, the docs look good and I tested it on other examples and it works as claimed:\n\n\n```\nsage: g = graphs.RandomGNP(20,.3) \nsage: h = graphs.RandomGNP(20,.2) \nsage: j = g+h\nsage: j.density()\n49/390\nsage: h.density()\n3/19\nsage: g.density()\n34/95\nsage: RR(g.density())\n0.357894736842105\nsage: RR(h.density())\n0.157894736842105\nsage: j.maximum_average_degree()\n34/5\nsage: h.average_degree()\n3\nsage: g.average_degree()\n34/5\n```\n",
    "created_at": "2010-05-12T12:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7529#issuecomment-63823",
    "user": "wdj"
}
```

This installs fine on 4.4.2.a0, passes sage -testall both before and after installing glpk (except for unrelated failures).

Also, the docs look good and I tested it on other examples and it works as claimed:


```
sage: g = graphs.RandomGNP(20,.3) 
sage: h = graphs.RandomGNP(20,.2) 
sage: j = g+h
sage: j.density()
49/390
sage: h.density()
3/19
sage: g.density()
34/95
sage: RR(g.density())
0.357894736842105
sage: RR(h.density())
0.157894736842105
sage: j.maximum_average_degree()
34/5
sage: h.average_degree()
3
sage: g.average_degree()
34/5
```




---

archive/issue_comments_063824.json:
```json
{
    "body": "Thaaaaaaank you so much !!! The other LP tickets are just applications of the following thing : if a graph has maximum average degree strictly less than 2 ( so 2-epsilon in the code, or 1-epsilon as it is sometimes divided) then it is acyclic -> a forest !!\n\nSo this ticket really is they key to all others ! When I found how to solve this one I knew how to write the others, so there shouldn't be any surprise in them :-)\n\nThank you again !!\n\nNathann",
    "created_at": "2010-05-12T14:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7529#issuecomment-63824",
    "user": "ncohen"
}
```

Thaaaaaaank you so much !!! The other LP tickets are just applications of the following thing : if a graph has maximum average degree strictly less than 2 ( so 2-epsilon in the code, or 1-epsilon as it is sometimes divided) then it is acyclic -> a forest !!

So this ticket really is they key to all others ! When I found how to solve this one I knew how to write the others, so there shouldn't be any surprise in them :-)

Thank you again !!

Nathann



---

archive/issue_comments_063825.json:
```json
{
    "body": "[print pictures](http://like-search.info/)",
    "created_at": "2010-05-26T08:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7529#issuecomment-63825",
    "user": "bascorp2"
}
```

[print pictures](http://like-search.info/)



---

archive/issue_comments_063826.json:
```json
{
    "body": "Replying to [comment:6 bascorp2]:\n> [print pictures](http://like-search.info/)\n\nThis looks like spam but I didn't try the link.",
    "created_at": "2010-05-26T10:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7529#issuecomment-63826",
    "user": "wdj"
}
```

Replying to [comment:6 bascorp2]:
> [print pictures](http://like-search.info/)

This looks like spam but I didn't try the link.



---

archive/issue_comments_063827.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7529#issuecomment-63827",
    "user": "mhansen"
}
```

Resolution: fixed
