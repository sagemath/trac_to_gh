# Issue 7569: random_vertex and random_edge functions

archive/issues_007569.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  abmasse\n\nIn many algorithms we want to find a random vertex or a random edge in a graph. It is also very often required to find, given a vertex, one edge adjacent to it ( for example in depth first or breadth first search ).\n\nThis should be possible easily, and most importantly efficiently ( if possible, directly written in C ) as DFS and BFS are very slow when written in python ( same problem with Floyd Warshall for all_pairs_shortest_path and networkX's distance function )\n\nIssue created by migration from https://trac.sagemath.org/ticket/7569\n\n",
    "created_at": "2009-12-01T10:15:12Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "random_vertex and random_edge functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7569",
    "user": "ncohen"
}
```
Assignee: rlm

CC:  abmasse

In many algorithms we want to find a random vertex or a random edge in a graph. It is also very often required to find, given a vertex, one edge adjacent to it ( for example in depth first or breadth first search ).

This should be possible easily, and most importantly efficiently ( if possible, directly written in C ) as DFS and BFS are very slow when written in python ( same problem with Floyd Warshall for all_pairs_shortest_path and networkX's distance function )

Issue created by migration from https://trac.sagemath.org/ticket/7569





---

archive/issue_comments_064388.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T10:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64388",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064389.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-23T10:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64389",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064390.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-23T10:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64390",
    "user": "ncohen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_064391.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-23T10:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64391",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064392.json:
```json
{
    "body": "All patches must include doctests, especially new functions.",
    "created_at": "2010-03-02T03:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64392",
    "user": "rlm"
}
```

All patches must include doctests, especially new functions.



---

archive/issue_comments_064393.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-02T03:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64393",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064394.json:
```json
{
    "body": "I agree, but I did not know how to comment a random generator.... How would you do that ? ;-)\n\nNathann",
    "created_at": "2010-03-02T08:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64394",
    "user": "ncohen"
}
```

I agree, but I did not know how to comment a random generator.... How would you do that ? ;-)

Nathann



---

archive/issue_comments_064395.json:
```json
{
    "body": "Replying to [comment:6 ncohen]:\n> I agree, but I did not know how to comment a random generator.... How would you do that ? ;-)\n> \n> Nathann\n\nThere are several ways, e.g.\n\n```\nsage: v = G.random_vertex()\nsage: v in G\nsage: G.has_vertex(v)\nTrue\n```\n\netc.\nYou can also do\n\n```\nsage: G.random_edge(labels=False)\n(...,...)\nsage: G.random_edge(labels=True)\n(...,...,...)\n```\n",
    "created_at": "2010-03-04T17:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64395",
    "user": "rlm"
}
```

Replying to [comment:6 ncohen]:
> I agree, but I did not know how to comment a random generator.... How would you do that ? ;-)
> 
> Nathann

There are several ways, e.g.

```
sage: v = G.random_vertex()
sage: v in G
sage: G.has_vertex(v)
True
```

etc.
You can also do

```
sage: G.random_edge(labels=False)
(...,...)
sage: G.random_edge(labels=True)
(...,...,...)
```




---

archive/issue_comments_064396.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-04T17:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64396",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064397.json:
```json
{
    "body": "Got it !\n\nHere is the new version :-)\n\nNathann",
    "created_at": "2010-03-04T17:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64397",
    "user": "ncohen"
}
```

Got it !

Here is the new version :-)

Nathann



---

archive/issue_comments_064398.json:
```json
{
    "body": "Hello, Nathann !\nI guess this patch won't be hard to review. I have a question, though. Why do you have the `**kwds` parameter ? It seems to me that there shouldn't be any parameter at all. Or if you want to keep the same parameters as for the `vertex_iterator` and `edge_iterator` functions, wouldn't it be better to use the same names (`vertices` for `vertex_iterator` for instance) ?\nWhat do you think ? If you still prefer to keep the `**kwds` argument, then I think it would be better to indicate at least that these are passed to the `vertex_iterator` and `edge_iterator` functions.",
    "created_at": "2010-03-21T21:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64398",
    "user": "abmasse"
}
```

Hello, Nathann !
I guess this patch won't be hard to review. I have a question, though. Why do you have the `**kwds` parameter ? It seems to me that there shouldn't be any parameter at all. Or if you want to keep the same parameters as for the `vertex_iterator` and `edge_iterator` functions, wouldn't it be better to use the same names (`vertices` for `vertex_iterator` for instance) ?
What do you think ? If you still prefer to keep the `**kwds` argument, then I think it would be better to indicate at least that these are passed to the `vertex_iterator` and `edge_iterator` functions.



---

archive/issue_comments_064399.json:
```json
{
    "body": "Hello !! \n\nI added this parameter because I can not stand the fact that Graph.edges() returns triples instead of pairs, so I constantly use the labels = False argument :-)\n\nPatch updated !\n\nNathann",
    "created_at": "2010-03-22T09:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64399",
    "user": "ncohen"
}
```

Hello !! 

I added this parameter because I can not stand the fact that Graph.edges() returns triples instead of pairs, so I constantly use the labels = False argument :-)

Patch updated !

Nathann



---

archive/issue_comments_064400.json:
```json
{
    "body": "Attachment [trac_7569.patch](tarball://root/attachments/some-uuid/ticket7569/trac_7569.patch) by ncohen created at 2010-03-22 09:51:55",
    "created_at": "2010-03-22T09:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64400",
    "user": "ncohen"
}
```

Attachment [trac_7569.patch](tarball://root/attachments/some-uuid/ticket7569/trac_7569.patch) by ncohen created at 2010-03-22 09:51:55



---

archive/issue_comments_064401.json:
```json
{
    "body": "Review patch with formatting of code and doc -- apply on top of Nathann's patch",
    "created_at": "2010-03-22T16:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64401",
    "user": "abmasse"
}
```

Review patch with formatting of code and doc -- apply on top of Nathann's patch



---

archive/issue_comments_064402.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-22T16:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64402",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064403.json:
```json
{
    "body": "Attachment [trac_7569_review-abm.patch](tarball://root/attachments/some-uuid/ticket7569/trac_7569_review-abm.patch) by abmasse created at 2010-03-22 16:34:27\n\nI've tested this patch on sage 4.3.4. All tests passed, and the documentation generated with the `browse_sage_doc` function looks ok (we really need to include those graph files in the tree for the reference manual). I made a few changes, only consisting of formatting of code and documentation.\n\nPositive review.",
    "created_at": "2010-03-22T16:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64403",
    "user": "abmasse"
}
```

Attachment [trac_7569_review-abm.patch](tarball://root/attachments/some-uuid/ticket7569/trac_7569_review-abm.patch) by abmasse created at 2010-03-22 16:34:27

I've tested this patch on sage 4.3.4. All tests passed, and the documentation generated with the `browse_sage_doc` function looks ok (we really need to include those graph files in the tree for the reference manual). I made a few changes, only consisting of formatting of code and documentation.

Positive review.



---

archive/issue_comments_064404.json:
```json
{
    "body": "Thank you very much again :-)\n\nNathann",
    "created_at": "2010-03-22T16:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64404",
    "user": "ncohen"
}
```

Thank you very much again :-)

Nathann



---

archive/issue_comments_064405.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n- trac_7569.patch\n- trac_7569_review-abm.patch",
    "created_at": "2010-04-15T05:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64405",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0:

- trac_7569.patch
- trac_7569_review-abm.patch



---

archive/issue_comments_064406.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64406",
    "user": "jhpalmieri"
}
```

Resolution: fixed
