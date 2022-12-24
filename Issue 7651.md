# Issue 7651: c_graph backends should include a "reversed" copy for digraphs in the sparse case

archive/issues_007651.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  ncohen jason\n\nThis is because the data structure for sparse graphs is itself directed, and in_neighbors is a slow function, as it needs to check each node.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7651\n\n",
    "created_at": "2009-12-10T06:17:45Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "c_graph backends should include a \"reversed\" copy for digraphs in the sparse case",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7651",
    "user": "rlm"
}
```
Assignee: rlm

CC:  ncohen jason

This is because the data structure for sparse graphs is itself directed, and in_neighbors is a slow function, as it needs to check each node.

Issue created by migration from https://trac.sagemath.org/ticket/7651





---

archive/issue_comments_065431.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-14T23:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65431",
    "user": "rlm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065432.json:
```json
{
    "body": "line 945 in `c_graphs.pyx`, shouldn't it be `in_neighbors` ?",
    "created_at": "2009-12-15T00:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65432",
    "user": "ylchapuy"
}
```

line 945 in `c_graphs.pyx`, shouldn't it be `in_neighbors` ?



---

archive/issue_comments_065433.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T00:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65433",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065434.json:
```json
{
    "body": "Yes! Good catch!",
    "created_at": "2009-12-15T00:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65434",
    "user": "rlm"
}
```

Yes! Good catch!



---

archive/issue_comments_065435.json:
```json
{
    "body": "Attachment [trac_7651.patch](tarball://root/attachments/some-uuid/ticket7651/trac_7651.patch) by rlm created at 2009-12-15 01:02:26\n\napply to sage-4.3.rc0 + #7640 + #7674 + #7673",
    "created_at": "2009-12-15T01:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65435",
    "user": "rlm"
}
```

Attachment [trac_7651.patch](tarball://root/attachments/some-uuid/ticket7651/trac_7651.patch) by rlm created at 2009-12-15 01:02:26

apply to sage-4.3.rc0 + #7640 + #7674 + #7673



---

archive/issue_comments_065436.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-15T01:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65436",
    "user": "rlm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065437.json:
```json
{
    "body": "I saw you replaced \n\n```\nfor w in (self._cg.out_neighbors(v) if side == 1 else self._cg.in_neighbors(v)): \n```\n\nwith\n\n```\nif side == 1: \n   neighbors = self._cg.out_neighbors(v) \nelif self._cg_rev is not None: # Sparse \n   neighbors = self._cg_rev.out_neighbors(v) \nelse: # Dense \n   neighbors = self._cg.in_neighbors(v) \n```\n\nI understand what you mean, but wouldn't it easier for developpers to define a function \"in_neighbors\" or \"out_neighbors\" doing this stuff to avoid dealing with the implementation of graphs when in the c_graph.pyx file ( where the algorithm are more graph-theoretic and a bit further from the implementation ) ?\n\nThis kind of thing is bound to reappear very often as we write algorithms in Cython... :-)\n\nNathann",
    "created_at": "2009-12-15T11:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65437",
    "user": "ncohen"
}
```

I saw you replaced 

```
for w in (self._cg.out_neighbors(v) if side == 1 else self._cg.in_neighbors(v)): 
```

with

```
if side == 1: 
   neighbors = self._cg.out_neighbors(v) 
elif self._cg_rev is not None: # Sparse 
   neighbors = self._cg_rev.out_neighbors(v) 
else: # Dense 
   neighbors = self._cg.in_neighbors(v) 
```

I understand what you mean, but wouldn't it easier for developpers to define a function "in_neighbors" or "out_neighbors" doing this stuff to avoid dealing with the implementation of graphs when in the c_graph.pyx file ( where the algorithm are more graph-theoretic and a bit further from the implementation ) ?

This kind of thing is bound to reappear very often as we write algorithms in Cython... :-)

Nathann



---

archive/issue_comments_065438.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-12-15T14:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65438",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_065439.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-15T15:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65439",
    "user": "rlm"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_065440.json:
```json
{
    "body": "Replying to [comment:7 ncohen]:\n> I saw you replaced \n> ...\n> with\n> ...\n> I understand what you mean, but wouldn't it easier for developpers to define a function \"in_neighbors\" or \"out_neighbors\" doing this stuff to avoid dealing with the implementation of graphs when in the c_graph.pyx file ( where the algorithm are more graph-theoretic and a bit further from the implementation ) ?\n\nOn the level of c_graphs, there is no way to avoid the implementation of graphs. You're using ints as vertices which may not line up with the actual labels, and since you're calling methods of self._cg, there's no way around it. If you want to write on a more friendly level, you need to sacrifice some speed, since on the level of (mostly Python) backends, the vertex labels are honest, and 'in_neighbors' is the appropriate function there.\n\n> This kind of thing is bound to reappear very often as we write algorithms in Cython... :-)\n\nThis is only relevant to very low-level functions. In which case you *are* implementing graphs :)",
    "created_at": "2009-12-15T15:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65440",
    "user": "rlm"
}
```

Replying to [comment:7 ncohen]:
> I saw you replaced 
> ...
> with
> ...
> I understand what you mean, but wouldn't it easier for developpers to define a function "in_neighbors" or "out_neighbors" doing this stuff to avoid dealing with the implementation of graphs when in the c_graph.pyx file ( where the algorithm are more graph-theoretic and a bit further from the implementation ) ?

On the level of c_graphs, there is no way to avoid the implementation of graphs. You're using ints as vertices which may not line up with the actual labels, and since you're calling methods of self._cg, there's no way around it. If you want to write on a more friendly level, you need to sacrifice some speed, since on the level of (mostly Python) backends, the vertex labels are honest, and 'in_neighbors' is the appropriate function there.

> This kind of thing is bound to reappear very often as we write algorithms in Cython... :-)

This is only relevant to very low-level functions. In which case you *are* implementing graphs :)



---

archive/issue_comments_065441.json:
```json
{
    "body": "I should have pointed out that `self._cg.in_neighbors(v)` would still work in the case you point out. It's just that using `self._cg_rev.out_neighbors(v)` is faster when it's available. The point is that you only have to worry about these things when you're writing a function in the GraphBackends.\n\nI'm more and more becoming convinced that #7634 is the appropriate place to break up `graph.py`. It will already be an invasive change to sage/graphs, and this will encourage people to get their pet patches merged before the switch. When I break up the file, part of the result will be a Cython layer, which sits \"above\" the graph backends. That way, when people are writing more advanced graph theory functions in Cython, they can do it there, safely away from the implementation-level stuff you're talking about.",
    "created_at": "2009-12-15T16:04:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65441",
    "user": "rlm"
}
```

I should have pointed out that `self._cg.in_neighbors(v)` would still work in the case you point out. It's just that using `self._cg_rev.out_neighbors(v)` is faster when it's available. The point is that you only have to worry about these things when you're writing a function in the GraphBackends.

I'm more and more becoming convinced that #7634 is the appropriate place to break up `graph.py`. It will already be an invasive change to sage/graphs, and this will encourage people to get their pet patches merged before the switch. When I break up the file, part of the result will be a Cython layer, which sits "above" the graph backends. That way, when people are writing more advanced graph theory functions in Cython, they can do it there, safely away from the implementation-level stuff you're talking about.



---

archive/issue_comments_065442.json:
```json
{
    "body": "Got it :-)\n\nD you think there could be a *nice* way, though, to prevent people from using in_neighbors on sparse graphs having a reversed version of themselves ?",
    "created_at": "2009-12-15T16:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65442",
    "user": "ncohen"
}
```

Got it :-)

D you think there could be a *nice* way, though, to prevent people from using in_neighbors on sparse graphs having a reversed version of themselves ?



---

archive/issue_comments_065443.json:
```json
{
    "body": "Positive review for this patch ! Applies fine, pass tests, and as far as I could I found nothing wrong inside... :-)",
    "created_at": "2009-12-15T16:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65443",
    "user": "ncohen"
}
```

Positive review for this patch ! Applies fine, pass tests, and as far as I could I found nothing wrong inside... :-)



---

archive/issue_comments_065444.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-15T16:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65444",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065445.json:
```json
{
    "body": "Replying to [comment:11 ncohen]:\n> Got it :-)\n> \n> D you think there could be a *nice* way, though, to prevent people from using in_neighbors on sparse graphs having a reversed version of themselves ?\n\nSparseGraphs will never have a reversed version. CGraphBackends may have a reversed version (i.e. two SparseGraphs), in which case in_neighbors will call it. I don't think we need to worry too much about lots of people implementing functions for the backends.",
    "created_at": "2009-12-15T16:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65445",
    "user": "rlm"
}
```

Replying to [comment:11 ncohen]:
> Got it :-)
> 
> D you think there could be a *nice* way, though, to prevent people from using in_neighbors on sparse graphs having a reversed version of themselves ?

SparseGraphs will never have a reversed version. CGraphBackends may have a reversed version (i.e. two SparseGraphs), in which case in_neighbors will call it. I don't think we need to worry too much about lots of people implementing functions for the backends.



---

archive/issue_comments_065446.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-15T17:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7651#issuecomment-65446",
    "user": "mhansen"
}
```

Resolution: fixed
