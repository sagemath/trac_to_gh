# Issue 6962: [with patch, needs review] Feedback vertex set, Feedback arc set

archive/issues_006962.json:
```json
{
    "body": "Assignee: @rlmill\n\nAdds the functions :\n* DiGraph.feedback_arc_set\n* DiGraph.feedback_vertex_set\n\nYou will find a full description of the problem in the docstrings, or there :\n* http://en.wikipedia.org/wiki/Feedback_vertex_set\n* http://en.wikipedia.org/wiki/Feedback_arc_set\n\nThe functions use Linear Programming, which needs one of the two optional packages GLPK \n\n``` \nsage: install_package('cbc')\n```\nor CBC \n\n```\nsage: install_package('glpk') \n```\ninstalled. You will find a helpful documentation about the construction of the Linear Program in the docstring.\n\nOne of the docstrings uses the function min_vertex_cover from #6680.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/6962\n\n",
    "created_at": "2009-09-19T18:45:45Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with patch, needs review] Feedback vertex set, Feedback arc set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6962",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

Adds the functions :
* DiGraph.feedback_arc_set
* DiGraph.feedback_vertex_set

You will find a full description of the problem in the docstrings, or there :
* http://en.wikipedia.org/wiki/Feedback_vertex_set
* http://en.wikipedia.org/wiki/Feedback_arc_set

The functions use Linear Programming, which needs one of the two optional packages GLPK 

``` 
sage: install_package('cbc')
```
or CBC 

```
sage: install_package('glpk') 
```
installed. You will find a helpful documentation about the construction of the Linear Program in the docstring.

One of the docstrings uses the function min_vertex_cover from #6680.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/6962





---

archive/issue_comments_057490.json:
```json
{
    "body": "We've used the terminology \"edge\" with a DiGraph, with the understanding that direction matters when you have a DiGraph.  Is it a possibility to change \"feedback_arc_set\" to \"feedback_edge_set\"?",
    "created_at": "2009-09-20T06:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57490",
    "user": "https://github.com/jasongrout"
}
```

We've used the terminology "edge" with a DiGraph, with the understanding that direction matters when you have a DiGraph.  Is it a possibility to change "feedback_arc_set" to "feedback_edge_set"?



---

archive/issue_comments_057491.json:
```json
{
    "body": "I mix them up myself sometimes, this distinction can almost always be deduced from the context, even outside of Sage... And anyway the word \"feedback\" is enough for anybody interested in the function to read its documentation, so I think it is OK. We can write \"feedback arc set\" in the documentation in case someones looks for this special string, besides !\n\nThe thing is that I will be going for one week in something like 10 minutes and will not have any access to any computer during this time. Could a reviewer fix this while reviewing the whole patch ? If this patch is not reviewed when I get back, I will do it myself, though... And I will remember that you already settled this question :-)\n\nNathann",
    "created_at": "2009-09-20T07:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57491",
    "user": "https://github.com/nathanncohen"
}
```

I mix them up myself sometimes, this distinction can almost always be deduced from the context, even outside of Sage... And anyway the word "feedback" is enough for anybody interested in the function to read its documentation, so I think it is OK. We can write "feedback arc set" in the documentation in case someones looks for this special string, besides !

The thing is that I will be going for one week in something like 10 minutes and will not have any access to any computer during this time. Could a reviewer fix this while reviewing the whole patch ? If this patch is not reviewed when I get back, I will do it myself, though... And I will remember that you already settled this question :-)

Nathann



---

archive/issue_comments_057492.json:
```json
{
    "body": "Done ! :-)\n\n( the patch now is written according to the changes brought to class MIP in #7012 )",
    "created_at": "2009-09-29T11:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57492",
    "user": "https://github.com/nathanncohen"
}
```

Done ! :-)

( the patch now is written according to the changes brought to class MIP in #7012 )



---

archive/issue_comments_057493.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T16:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57493",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057494.json:
```json
{
    "body": "This patch still applies ok, but none of the doctests work:\n\n```\nsage: cycle=graphs.CycleGraph(5)\nsage: dcycle=DiGraph(cycle)\nsage: cycle.size()\n5\nsage: dcycle.feedback_edge_set(value_only=True)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/rlmill/.sage/temp/rlm_book.local/96266/_Users_rlmill__sage_init_sage_0.py in <module>()\n\n/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in feedback_edge_set(self, value_only)\n  12540         from sage.numerical.mip import MixedIntegerLinearProgram\n  12541         \n> 12542         p=MixedIntegerLinearProgram(sense=-1)\n  12543         \n  12544         b=p.new_variable()\n\n/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/numerical/mip.so in sage.numerical.mip.MixedIntegerLinearProgram.__init__ (sage/numerical/mip.c:866)()\n\nTypeError: __init__() got an unexpected keyword argument 'sense'\nsage: cycle.min_vertex_cover()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Users/rlmill/.sage/temp/rlm_book.local/96266/_Users_rlmill__sage_init_sage_0.py in <module>()\n\nAttributeError: 'Graph' object has no attribute 'min_vertex_cover'\nsage: dcycle.feedback_vertex_set(value_only=True)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/rlmill/.sage/temp/rlm_book.local/96266/_Users_rlmill__sage_init_sage_0.py in <module>()\n\n/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in feedback_vertex_set(self, value_only)\n  12632         from sage.numerical.mip import MixedIntegerLinearProgram\n  12633         \n> 12634         p=MixedIntegerLinearProgram(sense=-1)\n  12635         \n  12636         b=p.new_variable()\n\n/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/numerical/mip.so in sage.numerical.mip.MixedIntegerLinearProgram.__init__ (sage/numerical/mip.c:866)()\n\nTypeError: __init__() got an unexpected keyword argument 'sense'\n```\n\nThere are two issues:\n\n1. `__init__() got an unexpected keyword argument 'sense'`\n\n2. `'Graph' object has no attribute 'min_vertex_cover'`",
    "created_at": "2009-12-15T16:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57494",
    "user": "https://github.com/rlmill"
}
```

This patch still applies ok, but none of the doctests work:

```
sage: cycle=graphs.CycleGraph(5)
sage: dcycle=DiGraph(cycle)
sage: cycle.size()
5
sage: dcycle.feedback_edge_set(value_only=True)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/rlmill/.sage/temp/rlm_book.local/96266/_Users_rlmill__sage_init_sage_0.py in <module>()

/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in feedback_edge_set(self, value_only)
  12540         from sage.numerical.mip import MixedIntegerLinearProgram
  12541         
> 12542         p=MixedIntegerLinearProgram(sense=-1)
  12543         
  12544         b=p.new_variable()

/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/numerical/mip.so in sage.numerical.mip.MixedIntegerLinearProgram.__init__ (sage/numerical/mip.c:866)()

TypeError: __init__() got an unexpected keyword argument 'sense'
sage: cycle.min_vertex_cover()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/rlmill/.sage/temp/rlm_book.local/96266/_Users_rlmill__sage_init_sage_0.py in <module>()

AttributeError: 'Graph' object has no attribute 'min_vertex_cover'
sage: dcycle.feedback_vertex_set(value_only=True)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/rlmill/.sage/temp/rlm_book.local/96266/_Users_rlmill__sage_init_sage_0.py in <module>()

/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in feedback_vertex_set(self, value_only)
  12632         from sage.numerical.mip import MixedIntegerLinearProgram
  12633         
> 12634         p=MixedIntegerLinearProgram(sense=-1)
  12635         
  12636         b=p.new_variable()

/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/numerical/mip.so in sage.numerical.mip.MixedIntegerLinearProgram.__init__ (sage/numerical/mip.c:866)()

TypeError: __init__() got an unexpected keyword argument 'sense'
```

There are two issues:

1. `__init__() got an unexpected keyword argument 'sense'`

2. `'Graph' object has no attribute 'min_vertex_cover'`



---

archive/issue_comments_057495.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-16T11:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57495",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057496.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-16T11:37:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57496",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057497.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-17T13:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57497",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057498.json:
```json
{
    "body": "Updated !",
    "created_at": "2009-12-17T13:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57498",
    "user": "https://github.com/nathanncohen"
}
```

Updated !



---

archive/issue_comments_057499.json:
```json
{
    "body": "Attachment [trac_6962-doctest-fixes.patch](tarball://root/attachments/some-uuid/ticket6962/trac_6962-doctest-fixes.patch) by @rlmill created at 2009-12-17 21:51:06",
    "created_at": "2009-12-17T21:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57499",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6962-doctest-fixes.patch](tarball://root/attachments/some-uuid/ticket6962/trac_6962-doctest-fixes.patch) by @rlmill created at 2009-12-17 21:51:06



---

archive/issue_comments_057500.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-17T21:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57500",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_016367.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-19T20:06:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6962#event-16367"
}
```



---

archive/issue_comments_057501.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T20:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6962#issuecomment-57501",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_016368.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-20T07:45:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6962",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6962#event-16368"
}
```
