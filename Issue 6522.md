# Issue 6522: replace .copy() with .__copy__() in graphs/graph.py

archive/issues_006522.json:
```json
{
    "body": "Assignee: was\n\nCC:  sage-combinat was mvngu alexghitza\n\nSee also #111, where this originates.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6522\n\n",
    "created_at": "2009-07-13T10:22:27Z",
    "labels": [
        "user interface",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "replace .copy() with .__copy__() in graphs/graph.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6522",
    "user": "AlexGhitza"
}
```
Assignee: was

CC:  sage-combinat was mvngu alexghitza

See also #111, where this originates.


Issue created by migration from https://trac.sagemath.org/ticket/6522





---

archive/issue_comments_053179.json:
```json
{
    "body": "Note that this has consequences for several files in combinat/.",
    "created_at": "2009-07-13T10:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53179",
    "user": "AlexGhitza"
}
```

Note that this has consequences for several files in combinat/.



---

archive/issue_comments_053180.json:
```json
{
    "body": "Note that we will likely need deprecation warnings.  See discussion at #6521.",
    "created_at": "2009-09-15T15:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53180",
    "user": "kcrisman"
}
```

Note that we will likely need deprecation warnings.  See discussion at #6521.



---

archive/issue_comments_053181.json:
```json
{
    "body": "There is one small problem with this.  Doing the naive change - \n\n```\n    def __copy__(self, implementation='networkx', sparse=None):\n```\n\nyields:\n\n```\nsage: g=Graph({0:[0,1,1,2]})\nsage: copy(g)\nLooped multi-graph on 3 vertices\nsage: g.__copy__(sparse=True)\nLooped multi-graph on 3 vertices\nsage: copy(g,sparse=True)\n---------------------------------------------------------------------------\nTypeError: copy() got an unexpected keyword argument 'sparse'\n```\n\nIt's not clear to me how to deal with this; changing the global 'copy' to handle keywords seems ill-advised.  On the other hand, there definitely is code (elsewhere) that uses the keywords implementation and sparse, at least in graph_generators.py.",
    "created_at": "2009-11-18T15:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53181",
    "user": "kcrisman"
}
```

There is one small problem with this.  Doing the naive change - 

```
    def __copy__(self, implementation='networkx', sparse=None):
```

yields:

```
sage: g=Graph({0:[0,1,1,2]})
sage: copy(g)
Looped multi-graph on 3 vertices
sage: g.__copy__(sparse=True)
Looped multi-graph on 3 vertices
sage: copy(g,sparse=True)
---------------------------------------------------------------------------
TypeError: copy() got an unexpected keyword argument 'sparse'
```

It's not clear to me how to deal with this; changing the global 'copy' to handle keywords seems ill-advised.  On the other hand, there definitely is code (elsewhere) that uses the keywords implementation and sparse, at least in graph_generators.py.



---

archive/issue_comments_053182.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-18T17:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53182",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053183.json:
```json
{
    "body": "I resolved this as best I could.  Attached patch *should* catch all remaining instances of .copy() that don't belong to Python objects that require it (i.e. dicts have only copy, not '__copy__'!)",
    "created_at": "2009-11-18T17:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53183",
    "user": "kcrisman"
}
```

I resolved this as best I could.  Attached patch *should* catch all remaining instances of .copy() that don't belong to Python objects that require it (i.e. dicts have only copy, not '__copy__'!)



---

archive/issue_comments_053184.json:
```json
{
    "body": "Based on 4.2.1",
    "created_at": "2009-11-18T17:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53184",
    "user": "kcrisman"
}
```

Based on 4.2.1



---

archive/issue_comments_053185.json:
```json
{
    "body": "Attachment [trac_6522.patch](tarball://root/attachments/some-uuid/ticket6522/trac_6522.patch) by ncohen created at 2009-12-08 17:13:08\n\nHello !!! Could you use the new methods defined in #7515 for the functions you deprecate ? It would ease the work in #7559 :-)",
    "created_at": "2009-12-08T17:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53185",
    "user": "ncohen"
}
```

Attachment [trac_6522.patch](tarball://root/attachments/some-uuid/ticket6522/trac_6522.patch) by ncohen created at 2009-12-08 17:13:08

Hello !!! Could you use the new methods defined in #7515 for the functions you deprecate ? It would ease the work in #7559 :-)



---

archive/issue_comments_053186.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-08T17:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53186",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_053187.json:
```json
{
    "body": "I can't say that I agree with the point of this ticket.\n\nCertainly there should be a `__copy__` defined for graphs, so that\n\n```\nsage: G = copy(Graph())\n```\n\nworks. However, the main use case of the `copy` method for graphs (for me, at least) is when I want to change underlying implementations. What was\n\n```\nsage: G = graphs.PetersenGraph()\nsage: C = G.copy(implementation='c_graph', sparse=False)\n```\n\nwon't work as\n\n```\nsage: G = graphs.PetersenGraph()\nsage: copy(G, implementation='c_graph', sparse=False)\n```\n\nbut instead we now need to do:\n\n```\nsage: G = graphs.PetersenGraph()\nsage: C = G.__copy__(implementation='c_graph', sparse=False)\n```\n\n\nWhich is an ugly, pointless change in API. Why don't we just define `__copy__`, and acknowledge that in some cases, it makes sense for objects to have a `copy` method?",
    "created_at": "2009-12-15T21:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53187",
    "user": "rlm"
}
```

I can't say that I agree with the point of this ticket.

Certainly there should be a `__copy__` defined for graphs, so that

```
sage: G = copy(Graph())
```

works. However, the main use case of the `copy` method for graphs (for me, at least) is when I want to change underlying implementations. What was

```
sage: G = graphs.PetersenGraph()
sage: C = G.copy(implementation='c_graph', sparse=False)
```

won't work as

```
sage: G = graphs.PetersenGraph()
sage: copy(G, implementation='c_graph', sparse=False)
```

but instead we now need to do:

```
sage: G = graphs.PetersenGraph()
sage: C = G.__copy__(implementation='c_graph', sparse=False)
```


Which is an ugly, pointless change in API. Why don't we just define `__copy__`, and acknowledge that in some cases, it makes sense for objects to have a `copy` method?



---

archive/issue_comments_053188.json:
```json
{
    "body": "I think that is fine (despite the time it took to do this), because that point makes tons of sense!  But perhaps the people who originated this idea in #111 should weigh in before we just add a __copy__ and don't remove copy - I am cc:ing a few of them.",
    "created_at": "2009-12-16T03:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53188",
    "user": "kcrisman"
}
```

I think that is fine (despite the time it took to do this), because that point makes tons of sense!  But perhaps the people who originated this idea in #111 should weigh in before we just add a __copy__ and don't remove copy - I am cc:ing a few of them.



---

archive/issue_comments_053189.json:
```json
{
    "body": "Ok, let's forget about #7515 and #7559 for this patch, if you are short on time it is not worth making this patch wait :-)\n\nBesides, taking care of #7559 will be a huge work, with of without 10 modifications more !\n\nNathann",
    "created_at": "2009-12-16T12:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53189",
    "user": "ncohen"
}
```

Ok, let's forget about #7515 and #7559 for this patch, if you are short on time it is not worth making this patch wait :-)

Besides, taking care of #7559 will be a huge work, with of without 10 modifications more !

Nathann



---

archive/issue_comments_053190.json:
```json
{
    "body": "Changing the component to graph theory so I can track this:\n\nsee http://groups.google.com/group/sage-devel/browse_thread/thread/70aacbd1dcc83497",
    "created_at": "2009-12-16T18:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53190",
    "user": "rlm"
}
```

Changing the component to graph theory so I can track this:

see http://groups.google.com/group/sage-devel/browse_thread/thread/70aacbd1dcc83497



---

archive/issue_comments_053191.json:
```json
{
    "body": "Changing component from user interface to graph theory.",
    "created_at": "2009-12-16T18:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53191",
    "user": "rlm"
}
```

Changing component from user interface to graph theory.



---

archive/issue_comments_053192.json:
```json
{
    "body": "Based on 4.3.alpha1",
    "created_at": "2009-12-17T21:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53192",
    "user": "kcrisman"
}
```

Based on 4.3.alpha1



---

archive/issue_comments_053193.json:
```json
{
    "body": "Attachment [trac_6522-final.patch](tarball://root/attachments/some-uuid/ticket6522/trac_6522-final.patch) by kcrisman created at 2009-12-17 21:54:05\n\nOkay, here is how I dealt with these issues.\n\n1. We can't use the generic deprecation thing from #7515 here, because it would say to use copy instead of copy!  Unfortunately.  On the plus side, that's one less for #7559. \n\n2. I have not deprecated copy() from the generic graph class, only the yang-baxter one.  There is now a __copy__ for generic graphs.  In order to deal with a tricky thing on Dynkin diagrams, I had to define a __copy__ method for them, which however is EXACTLY the same as the generic Python copy from the copy module.\n\nI really, really worked hard to make sure I caught every possible place where this causes problems, and it passes all doctests, but please think hard where it would make a difference.  I also hope I won't have to rebase it again :)",
    "created_at": "2009-12-17T21:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53193",
    "user": "kcrisman"
}
```

Attachment [trac_6522-final.patch](tarball://root/attachments/some-uuid/ticket6522/trac_6522-final.patch) by kcrisman created at 2009-12-17 21:54:05

Okay, here is how I dealt with these issues.

1. We can't use the generic deprecation thing from #7515 here, because it would say to use copy instead of copy!  Unfortunately.  On the plus side, that's one less for #7559. 

2. I have not deprecated copy() from the generic graph class, only the yang-baxter one.  There is now a __copy__ for generic graphs.  In order to deal with a tricky thing on Dynkin diagrams, I had to define a __copy__ method for them, which however is EXACTLY the same as the generic Python copy from the copy module.

I really, really worked hard to make sure I caught every possible place where this causes problems, and it passes all doctests, but please think hard where it would make a difference.  I also hope I won't have to rebase it again :)



---

archive/issue_comments_053194.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-17T21:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53194",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053195.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-17T22:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53195",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053196.json:
```json
{
    "body": "Ran tests in sage/graphs and sage/combinat. Looks good to me (I think some of those imports are unnecessary, but not a showstopper)",
    "created_at": "2009-12-17T22:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53196",
    "user": "rlm"
}
```

Ran tests in sage/graphs and sage/combinat. Looks good to me (I think some of those imports are unnecessary, but not a showstopper)



---

archive/issue_comments_053197.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-20T07:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6522#issuecomment-53197",
    "user": "mhansen"
}
```

Resolution: fixed
