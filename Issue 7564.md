# Issue 7564: graph theory: examples on degree sequences

archive/issues_007564.json:
```json
{
    "body": "Assignee: @rlmill\n\nThe degree sequence of a graph is a basic property that is studied in an introductory course on graph theory. There should be examples explaining how to compute the degree sequence of a given graph.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7564\n\n",
    "created_at": "2009-11-30T20:07:28Z",
    "labels": [
        "component: graph theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "graph theory: examples on degree sequences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7564",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: @rlmill

The degree sequence of a graph is a basic property that is studied in an introductory course on graph theory. There should be examples explaining how to compute the degree sequence of a given graph.

Issue created by migration from https://trac.sagemath.org/ticket/7564





---

archive/issue_comments_064245.json:
```json
{
    "body": "The patch `trac_7564-degree-sequences.patch` adds two examples to the method `GenericGraph.degree()`, showcasing how to obtain the degree sequence of a graph using that method.",
    "created_at": "2009-11-30T21:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch `trac_7564-degree-sequences.patch` adds two examples to the method `GenericGraph.degree()`, showcasing how to obtain the degree sequence of a graph using that method.



---

archive/issue_comments_064246.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-30T21:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064247.json:
```json
{
    "body": "I will ask for more, if it isn't too much trouble.  Could there be a small wrapper to (the better one) called degree_sequence as well?  I realize this is very low priority.  If the graph theory tour ever gets back up, this would be ideal to put in it as well.",
    "created_at": "2009-11-30T22:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64247",
    "user": "https://github.com/kcrisman"
}
```

I will ask for more, if it isn't too much trouble.  Could there be a small wrapper to (the better one) called degree_sequence as well?  I realize this is very low priority.  If the graph theory tour ever gets back up, this would be ideal to put in it as well.



---

archive/issue_comments_064248.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-30T22:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64248",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064249.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> Could there be a small wrapper to (the better one) called degree_sequence as well?\n\nAs I mentioned in my [email](http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5) to sage-devel, I'm unable to find a function or method in the graph theory module that computes the degree sequence of a given graph. So there is no function or method for wrapping, unless you can point me to such a method/function. On the other hand, are you suggesting that there be a method in the class `GenericGraph` called `degree_sequence()` that does exactly as its name implies? If so, then that could be done.\n\n\n\n\n> If the graph theory tour ever gets back up, this would be ideal to put in it as well.\n\nNod.",
    "created_at": "2009-11-30T22:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64249",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 kcrisman]:
> Could there be a small wrapper to (the better one) called degree_sequence as well?

As I mentioned in my [email](http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5) to sage-devel, I'm unable to find a function or method in the graph theory module that computes the degree sequence of a given graph. So there is no function or method for wrapping, unless you can point me to such a method/function. On the other hand, are you suggesting that there be a method in the class `GenericGraph` called `degree_sequence()` that does exactly as its name implies? If so, then that could be done.




> If the graph theory tour ever gets back up, this would be ideal to put in it as well.

Nod.



---

archive/issue_comments_064250.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n> Replying to [comment:2 kcrisman]:\n> > Could there be a small wrapper to (the better one) called degree_sequence as well?\n> \n> As I mentioned in my [email](http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5) to sage-devel, I'm unable to find a function or method in the graph theory module that computes the degree sequence of a given graph. So there is no function or method for wrapping, unless you can point me to such a method/function. On the other hand, are you suggesting that there be a method in the class `GenericGraph` called `degree_sequence()` that does exactly as its name implies? If so, then that could be done.\n\nYes, that is exactly what I meant - wrapping the examples you provide, as it were.  I don't have time to do this, unfortunately, though it should be pretty easy.",
    "created_at": "2009-11-30T22:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64250",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:3 mvngu]:
> Replying to [comment:2 kcrisman]:
> > Could there be a small wrapper to (the better one) called degree_sequence as well?
> 
> As I mentioned in my [email](http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5) to sage-devel, I'm unable to find a function or method in the graph theory module that computes the degree sequence of a given graph. So there is no function or method for wrapping, unless you can point me to such a method/function. On the other hand, are you suggesting that there be a method in the class `GenericGraph` called `degree_sequence()` that does exactly as its name implies? If so, then that could be done.

Yes, that is exactly what I meant - wrapping the examples you provide, as it were.  I don't have time to do this, unfortunately, though it should be pretty easy.



---

archive/issue_comments_064251.json:
```json
{
    "body": "The (new) patch `trac_7564-degree-sequences.patch` defines the method `GenericGraph.degree_sequence()` for computing the degree sequence of a graph.",
    "created_at": "2009-12-01T03:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The (new) patch `trac_7564-degree-sequences.patch` defines the method `GenericGraph.degree_sequence()` for computing the degree sequence of a graph.



---

archive/issue_comments_064252.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-01T03:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64252",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064253.json:
```json
{
    "body": "Could it be possible to define in the same patch functions outdegree_sequence and indegree_sequence for DiGraphs ? :-)",
    "created_at": "2009-12-01T06:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64253",
    "user": "https://github.com/nathanncohen"
}
```

Could it be possible to define in the same patch functions outdegree_sequence and indegree_sequence for DiGraphs ? :-)



---

archive/issue_comments_064254.json:
```json
{
    "body": "based on Sage 4.3.alpha0",
    "created_at": "2009-12-01T07:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64254",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.3.alpha0



---

archive/issue_comments_064255.json:
```json
{
    "body": "Attachment [trac_7564-degree-sequences.patch](tarball://root/attachments/some-uuid/ticket7564/trac_7564-degree-sequences.patch) by mvngu created at 2009-12-01 07:37:23\n\nReplying to [comment:6 ncohen]:\n> Could it be possible to define in the same patch functions outdegree_sequence and indegree_sequence for DiGraphs ? :-)\n\nY-E-S, yes! :-)\n\n\n\nThe patch `trac_7564-degree-sequences.patch` implements the following degree sequences:\n\n1. `degree_sequence()` --- the degree sequence of a (di)graph. This is implemented in the class `GenericGraph`.\n2. `in_degree_sequence()` --- the indegree sequence of a digraph. This is implemented in the class `DiGraph`.\n3. `out_degree_sequence()` --- the outdegree sequence of a digraph, also implemented in the class `DiGraph`.\n \nI use the method names `in_degree_sequence()` and `out_degree_sequence()` to be consistent with how the graph theory module names the indegree and outdegree methods.",
    "created_at": "2009-12-01T07:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64255",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7564-degree-sequences.patch](tarball://root/attachments/some-uuid/ticket7564/trac_7564-degree-sequences.patch) by mvngu created at 2009-12-01 07:37:23

Replying to [comment:6 ncohen]:
> Could it be possible to define in the same patch functions outdegree_sequence and indegree_sequence for DiGraphs ? :-)

Y-E-S, yes! :-)



The patch `trac_7564-degree-sequences.patch` implements the following degree sequences:

1. `degree_sequence()` --- the degree sequence of a (di)graph. This is implemented in the class `GenericGraph`.
2. `in_degree_sequence()` --- the indegree sequence of a digraph. This is implemented in the class `DiGraph`.
3. `out_degree_sequence()` --- the outdegree sequence of a digraph, also implemented in the class `DiGraph`.
 
I use the method names `in_degree_sequence()` and `out_degree_sequence()` to be consistent with how the graph theory module names the indegree and outdegree methods.



---

archive/issue_comments_064256.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-01T07:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64256",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064257.json:
```json
{
    "body": "Excellent ! Approved :-)\n\nThank you for contributing to the Graph Section !! :-)",
    "created_at": "2009-12-01T07:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64257",
    "user": "https://github.com/nathanncohen"
}
```

Excellent ! Approved :-)

Thank you for contributing to the Graph Section !! :-)



---

archive/issue_events_007793.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-01T08:23:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7564#event-7793"
}
```



---

archive/issue_comments_064258.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T08:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64258",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_064259.json:
```json
{
    "body": "A patch written, reviewed and merged in 11 hours ? O_O\n\nGod O_O",
    "created_at": "2009-12-01T08:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7564#issuecomment-64259",
    "user": "https://github.com/nathanncohen"
}
```

A patch written, reviewed and merged in 11 hours ? O_O

God O_O
