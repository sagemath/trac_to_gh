# Issue 7358: Strong orientations of 2-connected graphs

archive/issues_007358.json:
```json
{
    "body": "Assignee: rlm\n\nA special case of #7303 ( which is much easier and efficient to implement ) is to find a strongly connected orientation of the edges of a bridgeless connected graph.\n\nThis can be done using the short algorithm given in :\nSchriver Combinatorial optimization\nVolume B \npage 1037\n\nIssue created by migration from https://trac.sagemath.org/ticket/7358\n\n",
    "created_at": "2009-10-31T08:44:40Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Strong orientations of 2-connected graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7358",
    "user": "ncohen"
}
```
Assignee: rlm

A special case of #7303 ( which is much easier and efficient to implement ) is to find a strongly connected orientation of the edges of a bridgeless connected graph.

This can be done using the short algorithm given in :
Schriver Combinatorial optimization
Volume B 
page 1037

Issue created by migration from https://trac.sagemath.org/ticket/7358





---

archive/issue_comments_061664.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-01T19:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7358#issuecomment-61664",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061665.json:
```json
{
    "body": "Here it is !!!",
    "created_at": "2009-11-01T19:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7358#issuecomment-61665",
    "user": "ncohen"
}
```

Here it is !!!



---

archive/issue_comments_061666.json:
```json
{
    "body": "1. You need to describe what a strongly connected orientation is in your docstrings.\n\n2. You also need to clearly describe the output, i.e. what type of object is it...\n\n3. The function shouldn't assume but rather check whether the necessary conditions are met, and print a helpful error message if they aren't. If you're concerned about speed, then you can make use of a `check=False` option.\n\nOther than these minor issues, the patch applies and passes tests, and looks good.",
    "created_at": "2009-12-15T17:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7358#issuecomment-61666",
    "user": "rlm"
}
```

1. You need to describe what a strongly connected orientation is in your docstrings.

2. You also need to clearly describe the output, i.e. what type of object is it...

3. The function shouldn't assume but rather check whether the necessary conditions are met, and print a helpful error message if they aren't. If you're concerned about speed, then you can make use of a `check=False` option.

Other than these minor issues, the patch applies and passes tests, and looks good.



---

archive/issue_comments_061667.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T17:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7358#issuecomment-61667",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061668.json:
```json
{
    "body": "I added a definition of both \"orientation\" and \"strong\", plsu a reference to the wikipedia page, and described the output. This function is actually useful in both situations ( when the graph is not 2-connected, or when it is ), so I removed \"of a 2-connected graph\" in the first sentence of the docstring : it is explicitely written later that if the graph is not 2-connected, the result will be \"as best as can be hoped for\" in this situation ( and I assure you this part of the function is useful by itself :-) )",
    "created_at": "2009-12-16T01:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7358#issuecomment-61668",
    "user": "ncohen"
}
```

I added a definition of both "orientation" and "strong", plsu a reference to the wikipedia page, and described the output. This function is actually useful in both situations ( when the graph is not 2-connected, or when it is ), so I removed "of a 2-connected graph" in the first sentence of the docstring : it is explicitely written later that if the graph is not 2-connected, the result will be "as best as can be hoped for" in this situation ( and I assure you this part of the function is useful by itself :-) )



---

archive/issue_comments_061669.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-16T01:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7358#issuecomment-61669",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061670.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-16T03:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7358#issuecomment-61670",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_061671.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T03:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7358#issuecomment-61671",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061672.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T21:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7358#issuecomment-61672",
    "user": "mhansen"
}
```

Resolution: fixed
