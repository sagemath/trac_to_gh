# Issue 8284: IntervalGraph generator and a bug in is_chordal

archive/issues_008284.json:
```json
{
    "body": "Assignee: rlm\n\nHello !!!\n\nThis very small patch creates an independent generator for IntervalGraph, which is then called by the old RandomIntervalGraph function... The function is_chordal is fixed, as it was not exploring the whole graph when it was not connected.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8284\n\n",
    "created_at": "2010-02-16T18:11:03Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "IntervalGraph generator and a bug in is_chordal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8284",
    "user": "ncohen"
}
```
Assignee: rlm

Hello !!!

This very small patch creates an independent generator for IntervalGraph, which is then called by the old RandomIntervalGraph function... The function is_chordal is fixed, as it was not exploring the whole graph when it was not connected.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8284





---

archive/issue_comments_073344.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-16T18:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73344",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073345.json:
```json
{
    "body": "Changing assignee from rlm to ncohen.",
    "created_at": "2010-02-16T18:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73345",
    "user": "ncohen"
}
```

Changing assignee from rlm to ncohen.



---

archive/issue_comments_073346.json:
```json
{
    "body": "oh yes, and the lex_bfs method now admits an optional initial vertex ! :-)",
    "created_at": "2010-02-16T18:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73346",
    "user": "ncohen"
}
```

oh yes, and the lex_bfs method now admits an optional initial vertex ! :-)



---

archive/issue_comments_073347.json:
```json
{
    "body": "Can you please provide a doctest which shows a simple example of creating an `IntervalGraph` from intervals?",
    "created_at": "2010-03-02T04:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73347",
    "user": "rlm"
}
```

Can you please provide a doctest which shows a simple example of creating an `IntervalGraph` from intervals?



---

archive/issue_comments_073348.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-02T04:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73348",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073349.json:
```json
{
    "body": "Done ! :-)",
    "created_at": "2010-03-02T09:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73349",
    "user": "ncohen"
}
```

Done ! :-)



---

archive/issue_comments_073350.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-02T09:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73350",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073351.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-06T21:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73351",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073352.json:
```json
{
    "body": "Please add the following doctests:\n\n1. An example of `is_chordal` for a non-connected graph.\n\n2. Examples of the usage of each option to `lex_BFS`.\n\nAfter this is done, I'll be happy with the patch. All tests pass.",
    "created_at": "2010-03-06T21:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73352",
    "user": "rlm"
}
```

Please add the following doctests:

1. An example of `is_chordal` for a non-connected graph.

2. Examples of the usage of each option to `lex_BFS`.

After this is done, I'll be happy with the patch. All tests pass.



---

archive/issue_comments_073353.json:
```json
{
    "body": "I forgot to mention, please also look over the attached patch. I believe this is a cleaner coding of the same thing.",
    "created_at": "2010-03-06T21:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73353",
    "user": "rlm"
}
```

I forgot to mention, please also look over the attached patch. I believe this is a cleaner coding of the same thing.



---

archive/issue_comments_073354.json:
```json
{
    "body": "The ``max`` instruction fails with this modification, as the --possibly last-- vertex in the list may have been removed before, thus max is trying to find the maximum of an empty list ...\n\nI'll bring the other modifications as soon as possible... Thank you for your help ! :-)\n\nNathann",
    "created_at": "2010-03-07T13:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73354",
    "user": "ncohen"
}
```

The ``max`` instruction fails with this modification, as the --possibly last-- vertex in the list may have been removed before, thus max is trying to find the maximum of an empty list ...

I'll bring the other modifications as soon as possible... Thank you for your help ! :-)

Nathann



---

archive/issue_comments_073355.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-08T12:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73355",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073356.json:
```json
{
    "body": "Here it is ! :-)",
    "created_at": "2010-03-08T12:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73356",
    "user": "ncohen"
}
```

Here it is ! :-)



---

archive/issue_comments_073357.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-05-20T20:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73357",
    "user": "ncohen"
}
```

Changing priority from major to critical.



---

archive/issue_comments_073358.json:
```json
{
    "body": "Patch updated ! And based on the brand new 4.4.4.alpha0. Apply only this one !\n\nNathann",
    "created_at": "2010-06-08T12:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73358",
    "user": "ncohen"
}
```

Patch updated ! And based on the brand new 4.4.4.alpha0. Apply only this one !

Nathann



---

archive/issue_comments_073359.json:
```json
{
    "body": "Attachment\n\nLooks good.",
    "created_at": "2010-06-08T17:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73359",
    "user": "rlm"
}
```

Attachment

Looks good.



---

archive/issue_comments_073360.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-08T17:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73360",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073361.json:
```json
{
    "body": "This new graphs.IntervalGraph and the repaired graphs.RandomInterval work as advertised. Nicely done Nathann. \n\nHowever, I think graphs.Interval should allow repeated intervals, e.g., \ng = graphs.IntervalGraph( [(0,2), (0,2), (1,5), (3,7)] )\nshould create a graph with four vertices (not three as the method currently does).",
    "created_at": "2010-06-13T22:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73361",
    "user": "edward.scheinerman"
}
```

This new graphs.IntervalGraph and the repaired graphs.RandomInterval work as advertised. Nicely done Nathann. 

However, I think graphs.Interval should allow repeated intervals, e.g., 
g = graphs.IntervalGraph( [(0,2), (0,2), (1,5), (3,7)] )
should create a graph with four vertices (not three as the method currently does).



---

archive/issue_comments_073362.json:
```json
{
    "body": "you are right !!! I think the best way would be to create a RealInterval class in sage.sets, this way each vertex would be an immutable (hashable) object, and the graph could have two vertices representing the same interval.. I had the same problem when writing the recognition algorithm (#7563) : twin vertices were representing the same intervals, and the final graph was not isomorphic to the first as some vertices had disappeared..\n\nI used a small trick to make it work, but this is definitely not a good answer :-)\n\nNathann",
    "created_at": "2010-06-14T06:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73362",
    "user": "ncohen"
}
```

you are right !!! I think the best way would be to create a RealInterval class in sage.sets, this way each vertex would be an immutable (hashable) object, and the graph could have two vertices representing the same interval.. I had the same problem when writing the recognition algorithm (#7563) : twin vertices were representing the same intervals, and the final graph was not isomorphic to the first as some vertices had disappeared..

I used a small trick to make it work, but this is definitely not a good answer :-)

Nathann



---

archive/issue_comments_073363.json:
```json
{
    "body": "You might be able to get away with just creating a class that doesn't have a defined hash function, so that the default (the memory address) is used.  The problem with using a tuple is that the two hash values below are the same:\n\n\n```\nsage: a=(1,2)\nsage: b=(1,2)\nsage: hash(a)\n3713081631934410656\nsage: hash(b)\n3713081631934410656\n```\n\n\nWe can use a feature of user-defined classes, though:\n\n\"User-defined classes have __cmp__()  and __hash__()  methods by default; with them, all objects compare unequal (except with themselves) and x.__hash__()  returns id(x).\"\n\nThis means we can get vertices which contain objects which normally would be considered equal in a dictionary to be stored as two different things in a dictionary:\n\n\n```\nsage: class Vertex(object):\n....:     def __init__(self, value):\n....:         self.__value=value\n....:         \nsage: a=Vertex((1,2))\nsage: b=Vertex((1,2))\nsage: a is b\nFalse\nsage: hash(a)\n4528980944\nsage: hash(b)\n4528980816\nsage: Graph({a: [b]})\nGraph on 2 vertices\n```\n\n\nDoes that address the problem?  It introduces a problem, in that now you can't do:\n\n`g[Vertex((1,2))]`\n\nto get the neighbors, since, of course, the element you are creating is not the same as any of the vertices of the graph.  Also, you have to use v.__value to get the interval (or better, make some accessors for the attribute (and if you want, try to disallow changing it).",
    "created_at": "2010-06-14T15:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73363",
    "user": "jason"
}
```

You might be able to get away with just creating a class that doesn't have a defined hash function, so that the default (the memory address) is used.  The problem with using a tuple is that the two hash values below are the same:


```
sage: a=(1,2)
sage: b=(1,2)
sage: hash(a)
3713081631934410656
sage: hash(b)
3713081631934410656
```


We can use a feature of user-defined classes, though:

"User-defined classes have __cmp__()  and __hash__()  methods by default; with them, all objects compare unequal (except with themselves) and x.__hash__()  returns id(x)."

This means we can get vertices which contain objects which normally would be considered equal in a dictionary to be stored as two different things in a dictionary:


```
sage: class Vertex(object):
....:     def __init__(self, value):
....:         self.__value=value
....:         
sage: a=Vertex((1,2))
sage: b=Vertex((1,2))
sage: a is b
False
sage: hash(a)
4528980944
sage: hash(b)
4528980816
sage: Graph({a: [b]})
Graph on 2 vertices
```


Does that address the problem?  It introduces a problem, in that now you can't do:

`g[Vertex((1,2))]`

to get the neighbors, since, of course, the element you are creating is not the same as any of the vertices of the graph.  Also, you have to use v.__value to get the interval (or better, make some accessors for the attribute (and if you want, try to disallow changing it).



---

archive/issue_comments_073364.json:
```json
{
    "body": "Hmmmm.. Anyway creating a RealInterval class wouldn't be a solution as we would like RealInterval(1,2) == RealInterval(1,2) to be True, which can not hold if we want the vertices to be different in the Graph  :-/\n\nIn the end, perhaps the best idea is the one Ed mentionned in one of his emails : just labels the vertices with (id,(a.b)), and forget about unnecessary abstraction, which wouldn't add anything in this case...\n\nBut then the user creating an interval graph by giving a list of pairs (a,b) would not be able to guess the name of its vertices, as they would depend on the id given by IntervalGraph. Of course we can make it number them according to the order given by the list, but I don't like it very much either :-/\n\nAny idea ? :-/\n\nNathann",
    "created_at": "2010-06-14T15:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73364",
    "user": "ncohen"
}
```

Hmmmm.. Anyway creating a RealInterval class wouldn't be a solution as we would like RealInterval(1,2) == RealInterval(1,2) to be True, which can not hold if we want the vertices to be different in the Graph  :-/

In the end, perhaps the best idea is the one Ed mentionned in one of his emails : just labels the vertices with (id,(a.b)), and forget about unnecessary abstraction, which wouldn't add anything in this case...

But then the user creating an interval graph by giving a list of pairs (a,b) would not be able to guess the name of its vertices, as they would depend on the id given by IntervalGraph. Of course we can make it number them according to the order given by the list, but I don't like it very much either :-/

Any idea ? :-/

Nathann



---

archive/issue_comments_073365.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8284#issuecomment-73365",
    "user": "rlm"
}
```

Resolution: fixed
