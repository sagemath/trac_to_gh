# Issue 7365: Petersen's 2-factor theorem

archive/issues_007365.json:
```json
{
    "body": "Assignee: rlm\n\nImplement a function corresponding to Petersen's theorem on 2-factors.\n\nThis theorem says that any 2r-regular graphs can be decomposed in 2-factors. If the graph is not regular and is of maximum degree Delta, then it can be decomposed as an union of Delta/2 disjoints (<=2)-factors.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7365\n\n",
    "created_at": "2009-10-31T20:53:35Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Petersen's 2-factor theorem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7365",
    "user": "ncohen"
}
```
Assignee: rlm

Implement a function corresponding to Petersen's theorem on 2-factors.

This theorem says that any 2r-regular graphs can be decomposed in 2-factors. If the graph is not regular and is of maximum degree Delta, then it can be decomposed as an union of Delta/2 disjoints (<=2)-factors.

Issue created by migration from https://trac.sagemath.org/ticket/7365





---

archive/issue_comments_061722.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-18T18:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61722",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061723.json:
```json
{
    "body": "If you're introducing a new module in sage.graphs, the header of the file should be much more descriptive of what the module is for, etc... Take a look at some of the other files for examples.\n\nI'm (personally) very curious about what else you plan on including in `graph_decompositions`...\n\nThe patch applies cleanly, and the code looks good. Once again, I'd like to see a little more examples in the documentation.",
    "created_at": "2009-12-15T17:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61723",
    "user": "rlm"
}
```

If you're introducing a new module in sage.graphs, the header of the file should be much more descriptive of what the module is for, etc... Take a look at some of the other files for examples.

I'm (personally) very curious about what else you plan on including in `graph_decompositions`...

The patch applies cleanly, and the code looks good. Once again, I'd like to see a little more examples in the documentation.



---

archive/issue_comments_061724.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T17:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61724",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061725.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-18T08:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61725",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061726.json:
```json
{
    "body": "Hello !!!\n\nAs mentionned, I moved this function toward graph.py, and will patiently wait for the splitting of graph.py to begin creating new files.. :-)\n\n(please do not forget to install GLPK or CBC before testing it because of #7734)\n\nNathann",
    "created_at": "2009-12-18T08:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61726",
    "user": "ncohen"
}
```

Hello !!!

As mentionned, I moved this function toward graph.py, and will patiently wait for the splitting of graph.py to begin creating new files.. :-)

(please do not forget to install GLPK or CBC before testing it because of #7734)

Nathann



---

archive/issue_comments_061727.json:
```json
{
    "body": "Attachment\n\nI tried to find another example, but could not find any interesting/funny one (the theorem and its proof by themselves are enough to make me laugh :-) ). If you can think of a good one, just tell me and I'll add it :-)\n\nNathann",
    "created_at": "2009-12-18T08:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61727",
    "user": "ncohen"
}
```

Attachment

I tried to find another example, but could not find any interesting/funny one (the theorem and its proof by themselves are enough to make me laugh :-) ). If you can think of a good one, just tell me and I'll add it :-)

Nathann



---

archive/issue_comments_061728.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-18T19:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61728",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_061729.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-18T19:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61729",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061730.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-18T19:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61730",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_061731.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T22:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61731",
    "user": "mhansen"
}
```

Resolution: fixed
