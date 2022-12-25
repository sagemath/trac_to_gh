# Issue 7569: random_vertex and random_edge functions

archive/issues_007569.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  abmasse\n\nIn many algorithms we want to find a random vertex or a random edge in a graph. It is also very often required to find, given a vertex, one edge adjacent to it ( for example in depth first or breadth first search ).\n\nThis should be possible easily, and most importantly efficiently ( if possible, directly written in C ) as DFS and BFS are very slow when written in python ( same problem with Floyd Warshall for all_pairs_shortest_path and networkX's distance function )\n\nIssue created by migration from https://trac.sagemath.org/ticket/7569\n\n",
    "created_at": "2009-12-01T10:15:12Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "random_vertex and random_edge functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7569",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

CC:  abmasse

In many algorithms we want to find a random vertex or a random edge in a graph. It is also very often required to find, given a vertex, one edge adjacent to it ( for example in depth first or breadth first search ).

This should be possible easily, and most importantly efficiently ( if possible, directly written in C ) as DFS and BFS are very slow when written in python ( same problem with Floyd Warshall for all_pairs_shortest_path and networkX's distance function )

Issue created by migration from https://trac.sagemath.org/ticket/7569





---

archive/issue_comments_064272.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T10:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64272",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064273.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-23T10:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64273",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064274.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-23T10:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64274",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_064275.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-23T10:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64275",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064276.json:
```json
{
    "body": "All patches must include doctests, especially new functions.",
    "created_at": "2010-03-02T03:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64276",
    "user": "https://github.com/rlmill"
}
```

All patches must include doctests, especially new functions.



---

archive/issue_comments_064277.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-02T03:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64277",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064278.json:
```json
{
    "body": "I agree, but I did not know how to comment a random generator.... How would you do that ? ;-)\n\nNathann",
    "created_at": "2010-03-02T08:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64278",
    "user": "https://github.com/nathanncohen"
}
```

I agree, but I did not know how to comment a random generator.... How would you do that ? ;-)

Nathann



---

archive/issue_comments_064279.json:
```json
{
    "body": "Replying to [comment:6 ncohen]:\n> I agree, but I did not know how to comment a random generator.... How would you do that ? ;-)\n> \n> Nathann\n\nThere are several ways, e.g.\n\n```\nsage: v = G.random_vertex()\nsage: v in G\nsage: G.has_vertex(v)\nTrue\n```\n\netc.\nYou can also do\n\n```\nsage: G.random_edge(labels=False)\n(...,...)\nsage: G.random_edge(labels=True)\n(...,...,...)\n```\n",
    "created_at": "2010-03-04T17:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64279",
    "user": "https://github.com/rlmill"
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

archive/issue_comments_064280.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-04T17:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64280",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064281.json:
```json
{
    "body": "Got it !\n\nHere is the new version :-)\n\nNathann",
    "created_at": "2010-03-04T17:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64281",
    "user": "https://github.com/nathanncohen"
}
```

Got it !

Here is the new version :-)

Nathann



---

archive/issue_comments_064282.json:
```json
{
    "body": "Hello, Nathann !\nI guess this patch won't be hard to review. I have a question, though. Why do you have the `**kwds` parameter ? It seems to me that there shouldn't be any parameter at all. Or if you want to keep the same parameters as for the `vertex_iterator` and `edge_iterator` functions, wouldn't it be better to use the same names (`vertices` for `vertex_iterator` for instance) ?\nWhat do you think ? If you still prefer to keep the `**kwds` argument, then I think it would be better to indicate at least that these are passed to the `vertex_iterator` and `edge_iterator` functions.",
    "created_at": "2010-03-21T21:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64282",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Hello, Nathann !
I guess this patch won't be hard to review. I have a question, though. Why do you have the `**kwds` parameter ? It seems to me that there shouldn't be any parameter at all. Or if you want to keep the same parameters as for the `vertex_iterator` and `edge_iterator` functions, wouldn't it be better to use the same names (`vertices` for `vertex_iterator` for instance) ?
What do you think ? If you still prefer to keep the `**kwds` argument, then I think it would be better to indicate at least that these are passed to the `vertex_iterator` and `edge_iterator` functions.



---

archive/issue_comments_064283.json:
```json
{
    "body": "Hello !! \n\nI added this parameter because I can not stand the fact that Graph.edges() returns triples instead of pairs, so I constantly use the labels = False argument :-)\n\nPatch updated !\n\nNathann",
    "created_at": "2010-03-22T09:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64283",
    "user": "https://github.com/nathanncohen"
}
```

Hello !! 

I added this parameter because I can not stand the fact that Graph.edges() returns triples instead of pairs, so I constantly use the labels = False argument :-)

Patch updated !

Nathann



---

archive/issue_comments_064284.json:
```json
{
    "body": "Attachment [trac_7569.patch](tarball://root/attachments/some-uuid/ticket7569/trac_7569.patch) by @nathanncohen created at 2010-03-22 09:51:55",
    "created_at": "2010-03-22T09:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64284",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7569.patch](tarball://root/attachments/some-uuid/ticket7569/trac_7569.patch) by @nathanncohen created at 2010-03-22 09:51:55



---

archive/issue_comments_064285.json:
```json
{
    "body": "Review patch with formatting of code and doc -- apply on top of Nathann's patch",
    "created_at": "2010-03-22T16:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64285",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Review patch with formatting of code and doc -- apply on top of Nathann's patch



---

archive/issue_comments_064286.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-22T16:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64286",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064287.json:
```json
{
    "body": "Attachment [trac_7569_review-abm.patch](tarball://root/attachments/some-uuid/ticket7569/trac_7569_review-abm.patch) by abmasse created at 2010-03-22 16:34:27\n\nI've tested this patch on sage 4.3.4. All tests passed, and the documentation generated with the `browse_sage_doc` function looks ok (we really need to include those graph files in the tree for the reference manual). I made a few changes, only consisting of formatting of code and documentation.\n\nPositive review.",
    "created_at": "2010-03-22T16:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64287",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Attachment [trac_7569_review-abm.patch](tarball://root/attachments/some-uuid/ticket7569/trac_7569_review-abm.patch) by abmasse created at 2010-03-22 16:34:27

I've tested this patch on sage 4.3.4. All tests passed, and the documentation generated with the `browse_sage_doc` function looks ok (we really need to include those graph files in the tree for the reference manual). I made a few changes, only consisting of formatting of code and documentation.

Positive review.



---

archive/issue_comments_064288.json:
```json
{
    "body": "Thank you very much again :-)\n\nNathann",
    "created_at": "2010-03-22T16:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64288",
    "user": "https://github.com/nathanncohen"
}
```

Thank you very much again :-)

Nathann



---

archive/issue_comments_064289.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n- trac_7569.patch\n- trac_7569_review-abm.patch",
    "created_at": "2010-04-15T05:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64289",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0:

- trac_7569.patch
- trac_7569_review-abm.patch



---

archive/issue_comments_064290.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7569#issuecomment-64290",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
