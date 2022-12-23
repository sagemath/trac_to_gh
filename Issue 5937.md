# Issue 5937: graph theory -- showing the result of a database query with_picture=True is totally broken

archive/issues_005937.json:
```json
{
    "body": "Assignee: rlm\n\nHere is *yet another* example of non-tested code being totally broken.  Try this in the notebook.\n\n\n```\nQ = GraphQuery(display_cols=['graph6','num_vertices','degree_sequence'],\n   num_edges=['<=',5],min_degree=1)\n\nQ.show(with_picture=True)\n```\n\n\nthis silently outputs absolutely nothing. \n\nThe doctests don't test this -- they only test that this fails (with a message) on the command line. \n\nShorterm fix: completely remove this option from the documentation and code.\n\nLonterm fix: actually track down and fix the bug -- this would be nice, since I know the output looks good (I've seen Emily demo it).\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5937\n\n",
    "created_at": "2009-04-29T16:05:22Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "graph theory -- showing the result of a database query with_picture=True is totally broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5937",
    "user": "was"
}
```
Assignee: rlm

Here is *yet another* example of non-tested code being totally broken.  Try this in the notebook.


```
Q = GraphQuery(display_cols=['graph6','num_vertices','degree_sequence'],
   num_edges=['<=',5],min_degree=1)

Q.show(with_picture=True)
```


this silently outputs absolutely nothing. 

The doctests don't test this -- they only test that this fails (with a message) on the command line. 

Shorterm fix: completely remove this option from the documentation and code.

Lonterm fix: actually track down and fix the bug -- this would be nice, since I know the output looks good (I've seen Emily demo it).



Issue created by migration from https://trac.sagemath.org/ticket/5937





---

archive/issue_comments_046937.json:
```json
{
    "body": "I am unable to duplicate this bug.  I'm using a clean branch of 4.0alpha0.  Can someone else give this a try?",
    "created_at": "2009-05-21T21:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5937#issuecomment-46937",
    "user": "ekirkman"
}
```

I am unable to duplicate this bug.  I'm using a clean branch of 4.0alpha0.  Can someone else give this a try?



---

archive/issue_comments_046938.json:
```json
{
    "body": "I have the same result. Everything looks fine for me.\n\nWilliam -- Could you try reproducing this? If you can, can we get what machine/version it is on?",
    "created_at": "2009-05-21T22:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5937#issuecomment-46938",
    "user": "rlm"
}
```

I have the same result. Everything looks fine for me.

William -- Could you try reproducing this? If you can, can we get what machine/version it is on?



---

archive/issue_comments_046939.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-07-13T21:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5937#issuecomment-46939",
    "user": "rlm"
}
```

Resolution: invalid



---

archive/issue_comments_046940.json:
```json
{
    "body": "This has been open for 8 weeks with zero comment, so I'm assuming this is no longer valid.",
    "created_at": "2009-07-13T21:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5937#issuecomment-46940",
    "user": "rlm"
}
```

This has been open for 8 weeks with zero comment, so I'm assuming this is no longer valid.
