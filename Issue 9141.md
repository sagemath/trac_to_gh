# Issue 9141: find cospectral graphs

archive/issues_009141.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @nathanncohen @rlmill\n\nThis patch adds a function to the graphs object that finds cospectral graphs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9141\n\n",
    "created_at": "2010-06-04T20:29:27Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "find cospectral graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9141",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, ncohen, rlm

CC:  @nathanncohen @rlmill

This patch adds a function to the graphs object that finds cospectral graphs.

Issue created by migration from https://trac.sagemath.org/ticket/9141





---

archive/issue_comments_085199.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-04T20:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85199",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085200.json:
```json
{
    "body": "This patch has a doctest which depends on #9140",
    "created_at": "2010-06-04T20:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85200",
    "user": "https://github.com/jasongrout"
}
```

This patch has a doctest which depends on #9140



---

archive/issue_comments_085201.json:
```json
{
    "body": "Well... I do not work with spectral theory very often (perhaps read about it once or twice...) but I can check this is correct :-)\n\nFrom the look of it though, there seems to be an interest in the spectra of very small graphs, as enumerating all the graphs is admissible. One question though : what would you think of \"graph_set\" instead of \"test\" ? It sounds a bit wide to me otherwise :-)\n\nToday, I was thinking about some future patches (when all these dependencies will have disappeared). They would be methods taking as an argument a list of graphs, and returning, depending on the flags, the set of minimal elements of this list according to subgraph containment, induced subgraph containment, or minor containment.\n\nI was also thinking of a function taking as an argument a graph and a lambda function (lambda representing a property), and returning one smallest (or all the smallests) subgraphs (possibly induced, or minors) of the graphs given as an argument satisfying the property given by lambda. We could then \"clean\" it with the functions mentionned before. Well, I just thought, considering this function, that this also may be of interest to you !\n\nNathann",
    "created_at": "2010-06-04T21:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85201",
    "user": "https://github.com/nathanncohen"
}
```

Well... I do not work with spectral theory very often (perhaps read about it once or twice...) but I can check this is correct :-)

From the look of it though, there seems to be an interest in the spectra of very small graphs, as enumerating all the graphs is admissible. One question though : what would you think of "graph_set" instead of "test" ? It sounds a bit wide to me otherwise :-)

Today, I was thinking about some future patches (when all these dependencies will have disappeared). They would be methods taking as an argument a list of graphs, and returning, depending on the flags, the set of minimal elements of this list according to subgraph containment, induced subgraph containment, or minor containment.

I was also thinking of a function taking as an argument a graph and a lambda function (lambda representing a property), and returning one smallest (or all the smallests) subgraphs (possibly induced, or minors) of the graphs given as an argument satisfying the property given by lambda. We could then "clean" it with the functions mentionned before. Well, I just thought, considering this function, that this also may be of interest to you !

Nathann



---

archive/issue_comments_085202.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-06-04T21:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85202",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_085203.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-06-04T21:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85203",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_085204.json:
```json
{
    "body": "Replying to [comment:2 ncohen]:\n\n> From the look of it though, there seems to be an interest in the spectra of very small graphs, as enumerating all the graphs is admissible. One question though : what would you think of \"graph_set\" instead of \"test\" ? It sounds a bit wide to me otherwise :-)\n\nSince \"test\" can be either a function or an iterable object, I don't think graph_set is a good name.  I thought \"test\" could have two meanings: 1. a test function, 2. a set of graphs to test.  This covers the two possible inputs.\n\nIf you can think of a more natural way to have these sorts of inputs, please let me know!\n\n> \n> Today, I was thinking about some future patches (when all these dependencies will have disappeared). They would be methods taking as an argument a list of graphs, and returning, depending on the flags, the set of minimal elements of this list according to subgraph containment, induced subgraph containment, or minor containment.\n\nThat sounds fantastic!\n\n> \n> I was also thinking of a function taking as an argument a graph and a lambda function (lambda representing a property), and returning one smallest (or all the smallests) subgraphs (possibly induced, or minors) of the graphs given as an argument satisfying the property given by lambda. We could then \"clean\" it with the functions mentionned before. Well, I just thought, considering this function, that this also may be of interest to you !\n\nDefinitely!  I've done much of my research in minimal forbidden subgraphs, so these types of functions are definitely of interest!",
    "created_at": "2010-06-04T21:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85204",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:2 ncohen]:

> From the look of it though, there seems to be an interest in the spectra of very small graphs, as enumerating all the graphs is admissible. One question though : what would you think of "graph_set" instead of "test" ? It sounds a bit wide to me otherwise :-)

Since "test" can be either a function or an iterable object, I don't think graph_set is a good name.  I thought "test" could have two meanings: 1. a test function, 2. a set of graphs to test.  This covers the two possible inputs.

If you can think of a more natural way to have these sorts of inputs, please let me know!

> 
> Today, I was thinking about some future patches (when all these dependencies will have disappeared). They would be methods taking as an argument a list of graphs, and returning, depending on the flags, the set of minimal elements of this list according to subgraph containment, induced subgraph containment, or minor containment.

That sounds fantastic!

> 
> I was also thinking of a function taking as an argument a graph and a lambda function (lambda representing a property), and returning one smallest (or all the smallests) subgraphs (possibly induced, or minors) of the graphs given as an argument satisfying the property given by lambda. We could then "clean" it with the functions mentionned before. Well, I just thought, considering this function, that this also may be of interest to you !

Definitely!  I've done much of my research in minimal forbidden subgraphs, so these types of functions are definitely of interest!



---

archive/issue_comments_085205.json:
```json
{
    "body": "> Since \"test\" can be either a function or an iterable object, I don't think graph_set is a good name.  I thought \"test\" could have two meanings: 1. a test function, 2. a set of graphs to test.  This covers the two possible inputs.\n> \n> If you can think of a more natural way to have these sorts of inputs, please let me know!\n\nI was thinking of your lambda function as defining a set... I'll give it another try, though ! What would you think of \"domain\" ? If you still don't find it fitting, just forget about it ! :-)\n\nNathann",
    "created_at": "2010-06-04T21:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85205",
    "user": "https://github.com/nathanncohen"
}
```

> Since "test" can be either a function or an iterable object, I don't think graph_set is a good name.  I thought "test" could have two meanings: 1. a test function, 2. a set of graphs to test.  This covers the two possible inputs.
> 
> If you can think of a more natural way to have these sorts of inputs, please let me know!

I was thinking of your lambda function as defining a set... I'll give it another try, though ! What would you think of "domain" ? If you still don't find it fitting, just forget about it ! :-)

Nathann



---

archive/issue_comments_085206.json:
```json
{
    "body": "Replying to [comment:4 ncohen]:\n\n\n> I was thinking of your lambda function as defining a set... I'll give it another try, though ! What would you think of \"domain\" ? If you still don't find it fitting, just forget about it ! :-)\n\nI still have a problem with \"domain\", since it still indicates a set rather than a function restricting the set (at least to me).  If test=function, then it is a restriction on graphs with \"vertices\" vertices.  If test=iterable, then it is a domain or graph_set.  I guess I just don't see either graph_set or domain having the double-meaning that \"test\" has.",
    "created_at": "2010-06-04T21:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85206",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:4 ncohen]:


> I was thinking of your lambda function as defining a set... I'll give it another try, though ! What would you think of "domain" ? If you still don't find it fitting, just forget about it ! :-)

I still have a problem with "domain", since it still indicates a set rather than a function restricting the set (at least to me).  If test=function, then it is a restriction on graphs with "vertices" vertices.  If test=iterable, then it is a domain or graph_set.  I guess I just don't see either graph_set or domain having the double-meaning that "test" has.



---

archive/issue_comments_085207.json:
```json
{
    "body": "It's just that for me, your function does not \"restricts\" the set but defines it ! :-)\n\nNathann",
    "created_at": "2010-06-04T21:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85207",
    "user": "https://github.com/nathanncohen"
}
```

It's just that for me, your function does not "restricts" the set but defines it ! :-)

Nathann



---

archive/issue_comments_085208.json:
```json
{
    "body": "I guess I can see what you're saying now.  How about \"graphs\", since it doesn't have to be a set, and that is more descriptive than \"domain\"?",
    "created_at": "2010-06-04T21:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85208",
    "user": "https://github.com/jasongrout"
}
```

I guess I can see what you're saying now.  How about "graphs", since it doesn't have to be a set, and that is more descriptive than "domain"?



---

archive/issue_comments_085209.json:
```json
{
    "body": "Hmmmmm :-/\n\nBecause it is already the name of our generator class ? It's not that awful, though... Ok, let's settle on \"graphs\" :-)\n\nI will now work on this patch and add a patch myself for this change !\n\nNathann",
    "created_at": "2010-06-04T21:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85209",
    "user": "https://github.com/nathanncohen"
}
```

Hmmmmm :-/

Because it is already the name of our generator class ? It's not that awful, though... Ok, let's settle on "graphs" :-)

I will now work on this patch and add a patch myself for this change !

Nathann



---

archive/issue_comments_085210.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n\n> I will now work on this patch and add a patch myself for this change !\n> \n\nWait.  I'm almost done!",
    "created_at": "2010-06-04T21:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85210",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:8 ncohen]:

> I will now work on this patch and add a patch myself for this change !
> 

Wait.  I'm almost done!



---

archive/issue_comments_085211.json:
```json
{
    "body": "Okok :-)",
    "created_at": "2010-06-04T21:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85211",
    "user": "https://github.com/nathanncohen"
}
```

Okok :-)



---

archive/issue_comments_085212.json:
```json
{
    "body": "Attachment [trac-9141-cospectral_graphs.patch](tarball://root/attachments/some-uuid/ticket9141/trac-9141-cospectral_graphs.patch) by @jasongrout created at 2010-06-04 21:52:29",
    "created_at": "2010-06-04T21:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85212",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9141-cospectral_graphs.patch](tarball://root/attachments/some-uuid/ticket9141/trac-9141-cospectral_graphs.patch) by @jasongrout created at 2010-06-04 21:52:29



---

archive/issue_comments_085213.json:
```json
{
    "body": "Okay, patch updated.",
    "created_at": "2010-06-04T21:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85213",
    "user": "https://github.com/jasongrout"
}
```

Okay, patch updated.



---

archive/issue_comments_085214.json:
```json
{
    "body": "Positive review to your patch, and a small modification, as in 9142, for the math formulas :-)\n\nNathann",
    "created_at": "2010-06-04T22:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85214",
    "user": "https://github.com/nathanncohen"
}
```

Positive review to your patch, and a small modification, as in 9142, for the math formulas :-)

Nathann



---

archive/issue_comments_085215.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-04T22:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85215",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085216.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-09T03:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85216",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085217.json:
```json
{
    "body": "Thanks for the review!  If you change \"ommitted\" to \"omitted\" (http://www.merriam-webster.com/dictionary/omitted), positive review on your changes.",
    "created_at": "2010-07-09T03:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85217",
    "user": "https://github.com/jasongrout"
}
```

Thanks for the review!  If you change "ommitted" to "omitted" (http://www.merriam-webster.com/dictionary/omitted), positive review on your changes.



---

archive/issue_comments_085218.json:
```json
{
    "body": "Attachment [trac_9141-smallfixes.patch](tarball://root/attachments/some-uuid/ticket9141/trac_9141-smallfixes.patch) by @nathanncohen created at 2010-07-09 06:50:14",
    "created_at": "2010-07-09T06:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85218",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9141-smallfixes.patch](tarball://root/attachments/some-uuid/ticket9141/trac_9141-smallfixes.patch) by @nathanncohen created at 2010-07-09 06:50:14



---

archive/issue_comments_085219.json:
```json
{
    "body": "Done ! Sorry for the delay :-)\n\nNathann",
    "created_at": "2010-07-09T06:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85219",
    "user": "https://github.com/nathanncohen"
}
```

Done ! Sorry for the delay :-)

Nathann



---

archive/issue_comments_085220.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-09T06:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85220",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085221.json:
```json
{
    "body": "I'm about to attach V2 of Jason's patch, which is rebased for the following queue:\n\n```\n[...other, non-graph theory patches to be merged into 4.5.2.alpha0...]\ntrac_9111.patch\ntrac_9111-doc-edits.patch\ntrac_9111-doc_addition.patch\ntrac_9373.patch\ntrac_9375-graph-doctests.patch\ntrac_9485-strongly_connected_componnents_digraph-fix-nt.patch\ntrac_8953.patch\ntrac_9532-graphs-randstate.patch\ntrac-9141-cospectral_graphs.2.patch\ntrac_9141-smallfixes.patch\n```\n\nPlease check and let me know if there are any problems.",
    "created_at": "2010-07-21T02:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85221",
    "user": "https://github.com/qed777"
}
```

I'm about to attach V2 of Jason's patch, which is rebased for the following queue:

```
[...other, non-graph theory patches to be merged into 4.5.2.alpha0...]
trac_9111.patch
trac_9111-doc-edits.patch
trac_9111-doc_addition.patch
trac_9373.patch
trac_9375-graph-doctests.patch
trac_9485-strongly_connected_componnents_digraph-fix-nt.patch
trac_8953.patch
trac_9532-graphs-randstate.patch
trac-9141-cospectral_graphs.2.patch
trac_9141-smallfixes.patch
```

Please check and let me know if there are any problems.



---

archive/issue_comments_085222.json:
```json
{
    "body": "Attachment [trac-9141-cospectral_graphs.2.patch](tarball://root/attachments/some-uuid/ticket9141/trac-9141-cospectral_graphs.2.patch) by @qed777 created at 2010-07-21 02:18:33\n\nRebased for queue in comment 15.  Replaces previous version.",
    "created_at": "2010-07-21T02:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85222",
    "user": "https://github.com/qed777"
}
```

Attachment [trac-9141-cospectral_graphs.2.patch](tarball://root/attachments/some-uuid/ticket9141/trac-9141-cospectral_graphs.2.patch) by @qed777 created at 2010-07-21 02:18:33

Rebased for queue in comment 15.  Replaces previous version.



---

archive/issue_comments_085223.json:
```json
{
    "body": "By the way, the reason is that I got\n\n```\n$ hg qpush\napplying trac-9141-cospectral_graphs.patch\npatching file sage/graphs/graph_generators.py\nHunk #1 FAILED at 152\n1 out of 2 hunks FAILED -- saving rejects to file sage/graphs/graph_generators.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac-9141-cospectral_graphs.patch\n```\n\nwith V1.",
    "created_at": "2010-07-21T02:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85223",
    "user": "https://github.com/qed777"
}
```

By the way, the reason is that I got

```
$ hg qpush
applying trac-9141-cospectral_graphs.patch
patching file sage/graphs/graph_generators.py
Hunk #1 FAILED at 152
1 out of 2 hunks FAILED -- saving rejects to file sage/graphs/graph_generators.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac-9141-cospectral_graphs.patch
```

with V1.



---

archive/issue_comments_085224.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-21T02:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85224",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_085225.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-21T02:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85225",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085226.json:
```json
{
    "body": "The rebased patch is fine.",
    "created_at": "2010-07-22T00:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85226",
    "user": "https://github.com/dandrake"
}
```

The rebased patch is fine.



---

archive/issue_comments_085227.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-22T00:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85227",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009301.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-22T01:02:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9141#event-9301"
}
```



---

archive/issue_comments_085228.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T01:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9141#issuecomment-85228",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
