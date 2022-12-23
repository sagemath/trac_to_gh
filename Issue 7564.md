# Issue 7564: graph theory: examples on degree sequences

archive/issues_007564.json:
```json
{
    "body": "Assignee: rlm\n\nThe degree sequence of a graph is a basic property that is studied in an introductory course on graph theory. There should be examples explaining how to compute the degree sequence of a given graph.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7564\n\n",
    "created_at": "2009-11-30T20:07:28Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "title": "graph theory: examples on degree sequences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7564",
    "user": "mvngu"
}
```
Assignee: rlm

The degree sequence of a graph is a basic property that is studied in an introductory course on graph theory. There should be examples explaining how to compute the degree sequence of a given graph.

Issue created by migration from https://trac.sagemath.org/ticket/7564





---

archive/issue_comments_064361.json:
```json
{
    "body": "The patch `trac_7564-degree-sequences.patch` adds two examples to the method `GenericGraph.degree()`, showcasing how to obtain the degree sequence of a graph using that method.",
    "created_at": "2009-11-30T21:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64361",
    "user": "mvngu"
}
```

The patch `trac_7564-degree-sequences.patch` adds two examples to the method `GenericGraph.degree()`, showcasing how to obtain the degree sequence of a graph using that method.



---

archive/issue_comments_064362.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-30T21:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64362",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064363.json:
```json
{
    "body": "I will ask for more, if it isn't too much trouble.  Could there be a small wrapper to (the better one) called degree_sequence as well?  I realize this is very low priority.  If the graph theory tour ever gets back up, this would be ideal to put in it as well.",
    "created_at": "2009-11-30T22:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64363",
    "user": "kcrisman"
}
```

I will ask for more, if it isn't too much trouble.  Could there be a small wrapper to (the better one) called degree_sequence as well?  I realize this is very low priority.  If the graph theory tour ever gets back up, this would be ideal to put in it as well.



---

archive/issue_comments_064364.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-30T22:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64364",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064365.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> Could there be a small wrapper to (the better one) called degree_sequence as well?\n\nAs I mentioned in my [email](http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5) to sage-devel, I'm unable to find a function or method in the graph theory module that computes the degree sequence of a given graph. So there is no function or method for wrapping, unless you can point me to such a method/function. On the other hand, are you suggesting that there be a method in the class `GenericGraph` called `degree_sequence()` that does exactly as its name implies? If so, then that could be done.\n\n\n\n\n> If the graph theory tour ever gets back up, this would be ideal to put in it as well.\n\nNod.",
    "created_at": "2009-11-30T22:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64365",
    "user": "mvngu"
}
```

Replying to [comment:2 kcrisman]:
> Could there be a small wrapper to (the better one) called degree_sequence as well?

As I mentioned in my [email](http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5) to sage-devel, I'm unable to find a function or method in the graph theory module that computes the degree sequence of a given graph. So there is no function or method for wrapping, unless you can point me to such a method/function. On the other hand, are you suggesting that there be a method in the class `GenericGraph` called `degree_sequence()` that does exactly as its name implies? If so, then that could be done.




> If the graph theory tour ever gets back up, this would be ideal to put in it as well.

Nod.



---

archive/issue_comments_064366.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n> Replying to [comment:2 kcrisman]:\n> > Could there be a small wrapper to (the better one) called degree_sequence as well?\n> \n> As I mentioned in my [email](http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5) to sage-devel, I'm unable to find a function or method in the graph theory module that computes the degree sequence of a given graph. So there is no function or method for wrapping, unless you can point me to such a method/function. On the other hand, are you suggesting that there be a method in the class `GenericGraph` called `degree_sequence()` that does exactly as its name implies? If so, then that could be done.\n\nYes, that is exactly what I meant - wrapping the examples you provide, as it were.  I don't have time to do this, unfortunately, though it should be pretty easy.",
    "created_at": "2009-11-30T22:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64366",
    "user": "kcrisman"
}
```

Replying to [comment:3 mvngu]:
> Replying to [comment:2 kcrisman]:
> > Could there be a small wrapper to (the better one) called degree_sequence as well?
> 
> As I mentioned in my [email](http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5) to sage-devel, I'm unable to find a function or method in the graph theory module that computes the degree sequence of a given graph. So there is no function or method for wrapping, unless you can point me to such a method/function. On the other hand, are you suggesting that there be a method in the class `GenericGraph` called `degree_sequence()` that does exactly as its name implies? If so, then that could be done.

Yes, that is exactly what I meant - wrapping the examples you provide, as it were.  I don't have time to do this, unfortunately, though it should be pretty easy.



---

archive/issue_comments_064367.json:
```json
{
    "body": "The (new) patch `trac_7564-degree-sequences.patch` defines the method `GenericGraph.degree_sequence()` for computing the degree sequence of a graph.",
    "created_at": "2009-12-01T03:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64367",
    "user": "mvngu"
}
```

The (new) patch `trac_7564-degree-sequences.patch` defines the method `GenericGraph.degree_sequence()` for computing the degree sequence of a graph.



---

archive/issue_comments_064368.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-01T03:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64368",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064369.json:
```json
{
    "body": "Could it be possible to define in the same patch functions outdegree_sequence and indegree_sequence for DiGraphs ? :-)",
    "created_at": "2009-12-01T06:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64369",
    "user": "ncohen"
}
```

Could it be possible to define in the same patch functions outdegree_sequence and indegree_sequence for DiGraphs ? :-)



---

archive/issue_comments_064370.json:
```json
{
    "body": "based on Sage 4.3.alpha0",
    "created_at": "2009-12-01T07:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64370",
    "user": "mvngu"
}
```

based on Sage 4.3.alpha0



---

archive/issue_comments_064371.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:6 ncohen]:\n> Could it be possible to define in the same patch functions outdegree_sequence and indegree_sequence for DiGraphs ? :-)\n\nY-E-S, yes! :-)\n\n\n\nThe patch `trac_7564-degree-sequences.patch` implements the following degree sequences:\n\n1. `degree_sequence()` --- the degree sequence of a (di)graph. This is implemented in the class `GenericGraph`.\n2. `in_degree_sequence()` --- the indegree sequence of a digraph. This is implemented in the class `DiGraph`.\n3. `out_degree_sequence()` --- the outdegree sequence of a digraph, also implemented in the class `DiGraph`.\n \nI use the method names `in_degree_sequence()` and `out_degree_sequence()` to be consistent with how the graph theory module names the indegree and outdegree methods.",
    "created_at": "2009-12-01T07:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64371",
    "user": "mvngu"
}
```

Attachment

Replying to [comment:6 ncohen]:
> Could it be possible to define in the same patch functions outdegree_sequence and indegree_sequence for DiGraphs ? :-)

Y-E-S, yes! :-)



The patch `trac_7564-degree-sequences.patch` implements the following degree sequences:

1. `degree_sequence()` --- the degree sequence of a (di)graph. This is implemented in the class `GenericGraph`.
2. `in_degree_sequence()` --- the indegree sequence of a digraph. This is implemented in the class `DiGraph`.
3. `out_degree_sequence()` --- the outdegree sequence of a digraph, also implemented in the class `DiGraph`.
 
I use the method names `in_degree_sequence()` and `out_degree_sequence()` to be consistent with how the graph theory module names the indegree and outdegree methods.



---

archive/issue_comments_064372.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-01T07:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64372",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064373.json:
```json
{
    "body": "Excellent ! Approved :-)\n\nThank you for contributing to the Graph Section !! :-)",
    "created_at": "2009-12-01T07:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64373",
    "user": "ncohen"
}
```

Excellent ! Approved :-)

Thank you for contributing to the Graph Section !! :-)



---

archive/issue_comments_064374.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T08:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64374",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_064375.json:
```json
{
    "body": "A patch written, reviewed and merged in 11 hours ? O_O\n\nGod O_O",
    "created_at": "2009-12-01T08:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64375",
    "user": "ncohen"
}
```

A patch written, reviewed and merged in 11 hours ? O_O

God O_O
