# Issue 5911: greatly improve the documentation one gets from Graph?

archive/issues_005911.json:
```json
{
    "body": "Assignee: @rlmill\n\nImagine a new user who wants to create a graph.  They do `Graph?` and they get (in order):\n\n1. Two pages of parameters, which they can't possibly read through.\n\n2. The first *page* of examples all involve networkx (they think -- huh?) and starts like this.\n\n\n```\n  \n    EXAMPLES: We illustrate the first six input formats (the other two\n    involve packages that are currently not standard in Sage):\n    \n    #. A NetworkX XGraph::\n    \n          sage: import networkx\n          sage: g = networkx.XGraph({0:[1,2,3], 2:[4]})\n          sage: Graph(g)\n          Graph on 5 vertices\n....\n```\n\n\nI propose:\n \n1. Putting a few simple straightforward examples (which is all most users need) right *before* the INPUT: block.\n\n2. Moving any mention of networkx lower in the lists, e.g., when defining the data input, don't put networkx first, and when documenting things later with examples, don't put networkx first. \n\n3. That one can do \"graphs.<tab>\" and get constructors for any family of graphs should be noted clearly and prominently, also before the INPUT: block.  This is not even noted anywhere right now, though it is used in two examples.\n\nThe above are all easy changes, I think. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5911\n\n",
    "created_at": "2009-04-27T13:02:05Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "greatly improve the documentation one gets from Graph?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5911",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill

Imagine a new user who wants to create a graph.  They do `Graph?` and they get (in order):

1. Two pages of parameters, which they can't possibly read through.

2. The first *page* of examples all involve networkx (they think -- huh?) and starts like this.


```
  
    EXAMPLES: We illustrate the first six input formats (the other two
    involve packages that are currently not standard in Sage):
    
    #. A NetworkX XGraph::
    
          sage: import networkx
          sage: g = networkx.XGraph({0:[1,2,3], 2:[4]})
          sage: Graph(g)
          Graph on 5 vertices
....
```


I propose:
 
1. Putting a few simple straightforward examples (which is all most users need) right *before* the INPUT: block.

2. Moving any mention of networkx lower in the lists, e.g., when defining the data input, don't put networkx first, and when documenting things later with examples, don't put networkx first. 

3. That one can do "graphs.<tab>" and get constructors for any family of graphs should be noted clearly and prominently, also before the INPUT: block.  This is not even noted anywhere right now, though it is used in two examples.

The above are all easy changes, I think. 

Issue created by migration from https://trac.sagemath.org/ticket/5911





---

archive/issue_comments_046621.json:
```json
{
    "body": "+1!\n\nSo you're saying that Graph? should be something like graphs?",
    "created_at": "2009-04-27T15:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46621",
    "user": "https://github.com/jasongrout"
}
```

+1!

So you're saying that Graph? should be something like graphs?



---

archive/issue_comments_046622.json:
```json
{
    "body": "I began to write something, as I thought nobody was working on it seeing that last message was posted 3 months ago ;-)\n\nWhat I have written is just a short introduction meant for user **really** unfamiliar with graphs in Sage and in general.. I expect a lot of critics from you, and I will change it accordingly, but I have spent much time in the past days trying to explain how to use graphs in Sage to some of my friends that I thought the best way may be to directly document this section... Tell me what you would change to this :\n\nhttp://www-sop.inria.fr/members/Nathann.Cohen/infograph.py",
    "created_at": "2009-08-03T17:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46622",
    "user": "https://github.com/nathanncohen"
}
```

I began to write something, as I thought nobody was working on it seeing that last message was posted 3 months ago ;-)

What I have written is just a short introduction meant for user **really** unfamiliar with graphs in Sage and in general.. I expect a lot of critics from you, and I will change it accordingly, but I have spent much time in the past days trying to explain how to use graphs in Sage to some of my friends that I thought the best way may be to directly document this section... Tell me what you would change to this :

http://www-sop.inria.fr/members/Nathann.Cohen/infograph.py



---

archive/issue_comments_046623.json:
```json
{
    "body": "Nathann,\n\nThis looks pretty good. Can you change the examples a bit, though? For example, a lot of the docstrings about creating graphs from graph6 strings include test cases where an error is triggered. As long as these failures are somewhere in the documentation, they're tested. Maybe the docs here should focus more on how to properly work with them. Also, you should get this into the appropriate place in `graph.py` and post it as an actual patch, so that e.g. we can post modifications and more people can pitch in to help. Finally, I believe that a few code blocks at the beginning need the `::` and indentation, e.g.:\n\n```\n    If you want to see what they look like, begin this way :\n   \n    sage: g=graphs.PetersenGraph()\n    sage: g.plot()\n\n    or\n\n    sage: g=graphs.ChvatalGraph()\n    sage: g.plot()\n```\n",
    "created_at": "2009-08-05T16:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46623",
    "user": "https://github.com/rlmill"
}
```

Nathann,

This looks pretty good. Can you change the examples a bit, though? For example, a lot of the docstrings about creating graphs from graph6 strings include test cases where an error is triggered. As long as these failures are somewhere in the documentation, they're tested. Maybe the docs here should focus more on how to properly work with them. Also, you should get this into the appropriate place in `graph.py` and post it as an actual patch, so that e.g. we can post modifications and more people can pitch in to help. Finally, I believe that a few code blocks at the beginning need the `::` and indentation, e.g.:

```
    If you want to see what they look like, begin this way :
   
    sage: g=graphs.PetersenGraph()
    sage: g.plot()

    or

    sage: g=graphs.ChvatalGraph()
    sage: g.plot()
```




---

archive/issue_comments_046624.json:
```json
{
    "body": "Hello !\n\nSeveral questions :\n\n* I agree that way to raise errors and exceptions have no real place in Graph?. Where should I put them ? In the looooooooong docstring at the beginning of file graph.py ?\n\n* I do not understand their purpose anyway. There or elsewhere O_o\n\n* No problem with '::' as I can see some occurences of them in this docstring... What are they meant to do, though ? ;-)\n\n* I did not post a patch thinking it would be much easier to read it this way as it seemed far from a final version. The next one will be a patch ;-)",
    "created_at": "2009-08-05T18:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46624",
    "user": "https://github.com/nathanncohen"
}
```

Hello !

Several questions :

* I agree that way to raise errors and exceptions have no real place in Graph?. Where should I put them ? In the looooooooong docstring at the beginning of file graph.py ?

* I do not understand their purpose anyway. There or elsewhere O_o

* No problem with '::' as I can see some occurences of them in this docstring... What are they meant to do, though ? ;-)

* I did not post a patch thinking it would be much easier to read it this way as it seemed far from a final version. The next one will be a patch ;-)



---

archive/issue_comments_046625.json:
```json
{
    "body": "Here is the patch you requested.. Where do you think we should store these doctests you mentionned if not in this docstring ?",
    "created_at": "2009-08-17T15:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46625",
    "user": "https://github.com/nathanncohen"
}
```

Here is the patch you requested.. Where do you think we should store these doctests you mentionned if not in this docstring ?



---

archive/issue_comments_046626.json:
```json
{
    "body": "Attachment [doc_graph.patch](tarball://root/attachments/some-uuid/ticket5911/doc_graph.patch) by @nathanncohen created at 2009-08-17 15:08:24",
    "created_at": "2009-08-17T15:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46626",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [doc_graph.patch](tarball://root/attachments/some-uuid/ticket5911/doc_graph.patch) by @nathanncohen created at 2009-08-17 15:08:24



---

archive/issue_comments_046627.json:
```json
{
    "body": "I've added some editing in a second patch, and I'd like to give this a positive review, but the documentation for `DiGraph?` suffers from the same fault, and I would feel less guilty if this ticket addressed that as well.",
    "created_at": "2009-08-26T18:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46627",
    "user": "https://github.com/rlmill"
}
```

I've added some editing in a second patch, and I'd like to give this a positive review, but the documentation for `DiGraph?` suffers from the same fault, and I would feel less guilty if this ticket addressed that as well.



---

archive/issue_comments_046628.json:
```json
{
    "body": "apply on top of doc_graph.patch",
    "created_at": "2009-08-26T18:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46628",
    "user": "https://github.com/rlmill"
}
```

apply on top of doc_graph.patch



---

archive/issue_comments_046629.json:
```json
{
    "body": "Attachment [trac_5911-editing.patch](tarball://root/attachments/some-uuid/ticket5911/trac_5911-editing.patch) by @nathanncohen created at 2009-08-26 19:40:54\n\nWhat about a good old  : \"cf. Graph\" (or a plain copy of Graph?), as it is exactly the same ? ^^;\n\nWe could just write a list of the functions of DiGraph that are unaavailable in Graph, couldn't we ?",
    "created_at": "2009-08-26T19:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46629",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_5911-editing.patch](tarball://root/attachments/some-uuid/ticket5911/trac_5911-editing.patch) by @nathanncohen created at 2009-08-26 19:40:54

What about a good old  : "cf. Graph" (or a plain copy of Graph?), as it is exactly the same ? ^^;

We could just write a list of the functions of DiGraph that are unaavailable in Graph, couldn't we ?



---

archive/issue_comments_046630.json:
```json
{
    "body": "Still around ? ;-)",
    "created_at": "2009-10-03T09:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46630",
    "user": "https://github.com/nathanncohen"
}
```

Still around ? ;-)



---

archive/issue_comments_046631.json:
```json
{
    "body": "Replying to [comment:10 ncohen]:\n> What about a good old  : \"cf. Graph\" (or a plain copy of Graph?), as it is exactly the same ? ^^;\n> \n> We could just write a list of the functions of DiGraph that are unaavailable in Graph, couldn't we ?\n\nImagine you have never used Sage before, and you really really like DiGraphs. So one of the first things you do in Sage, aside from `2+2` or `factor(factorial(12))`, is type `DiGraph?`. I think there are such (potential) users out there, and the documentation there should be independently helpful. Certainly a reference to `Graph?` would be appropriate, but the docs you get from `DiGraph?` should also be self-contained and helpful.",
    "created_at": "2009-10-08T16:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46631",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:10 ncohen]:
> What about a good old  : "cf. Graph" (or a plain copy of Graph?), as it is exactly the same ? ^^;
> 
> We could just write a list of the functions of DiGraph that are unaavailable in Graph, couldn't we ?

Imagine you have never used Sage before, and you really really like DiGraphs. So one of the first things you do in Sage, aside from `2+2` or `factor(factorial(12))`, is type `DiGraph?`. I think there are such (potential) users out there, and the documentation there should be independently helpful. Certainly a reference to `Graph?` would be appropriate, but the docs you get from `DiGraph?` should also be self-contained and helpful.



---

archive/issue_comments_046632.json:
```json
{
    "body": "Then a plain copy could do, couldn't it ? Plus some DiGraph-specific functions .. ;-)",
    "created_at": "2009-10-08T16:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46632",
    "user": "https://github.com/nathanncohen"
}
```

Then a plain copy could do, couldn't it ? Plus some DiGraph-specific functions .. ;-)



---

archive/issue_comments_046633.json:
```json
{
    "body": "Replying to [comment:13 ncohen]:\n> Then a plain copy could do, couldn't it ?\n\nEssentially, yes, subject to `s/Graph/DiGraph`.\n\n> Plus some DiGraph-specific functions .. ;-)\n\nFor the DiGraph fans!",
    "created_at": "2009-10-08T16:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46633",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:13 ncohen]:
> Then a plain copy could do, couldn't it ?

Essentially, yes, subject to `s/Graph/DiGraph`.

> Plus some DiGraph-specific functions .. ;-)

For the DiGraph fans!



---

archive/issue_comments_046634.json:
```json
{
    "body": "New version with an updated DiGraph section. Some problem, still : when running a sage -t on graph.py, Python does not like to see g.diameter ? which is mentioned in the doc.\n\nDo you know how to fix this ?\n\nThis new patch is a flattened version of the previous ones, plus the updates. Only this one should be applied.\n\nNathann",
    "created_at": "2009-10-13T08:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46634",
    "user": "https://github.com/nathanncohen"
}
```

New version with an updated DiGraph section. Some problem, still : when running a sage -t on graph.py, Python does not like to see g.diameter ? which is mentioned in the doc.

Do you know how to fix this ?

This new patch is a flattened version of the previous ones, plus the updates. Only this one should be applied.

Nathann



---

archive/issue_comments_046635.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-13T08:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46635",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046636.json:
```json
{
    "body": "Attachment [trac_5911.patch](tarball://root/attachments/some-uuid/ticket5911/trac_5911.patch) by @nathanncohen created at 2009-10-13 08:22:07\n\nHmmm.. This -- should -- have been a flattened version of all the patches, though it is not and I wonder why. This patch needs doc_graph.patch to be applied first, and contains trac_5911-editing.patch. So only doc_graph.patch and this patch should be applied.\n\nI tried to build a real flattened version, but for some reason I can not O_o\n\nNathann",
    "created_at": "2009-10-13T08:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46636",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_5911.patch](tarball://root/attachments/some-uuid/ticket5911/trac_5911.patch) by @nathanncohen created at 2009-10-13 08:22:07

Hmmm.. This -- should -- have been a flattened version of all the patches, though it is not and I wonder why. This patch needs doc_graph.patch to be applied first, and contains trac_5911-editing.patch. So only doc_graph.patch and this patch should be applied.

I tried to build a real flattened version, but for some reason I can not O_o

Nathann



---

archive/issue_comments_046637.json:
```json
{
    "body": "Attachment [trac_5911-reviewer.patch](tarball://root/attachments/some-uuid/ticket5911/trac_5911-reviewer.patch) by mvngu created at 2009-10-28 14:59:49\n\nreviewer patch",
    "created_at": "2009-10-28T14:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46637",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5911-reviewer.patch](tarball://root/attachments/some-uuid/ticket5911/trac_5911-reviewer.patch) by mvngu created at 2009-10-28 14:59:49

reviewer patch



---

archive/issue_comments_046638.json:
```json
{
    "body": "I have attached a reviewer patch. So patches should be applied in the following order:\n\n1. `doc_graph.patch`\n2. `trac_5911.patch`\n3. `trac_5911-reviewer.patch`\n\nThe reviewer patch fixes some typos and grammar issues. It also adjusts some examples to prevent doctest failures. Only my patch needs to be reviewed.",
    "created_at": "2009-10-28T15:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46638",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I have attached a reviewer patch. So patches should be applied in the following order:

1. `doc_graph.patch`
2. `trac_5911.patch`
3. `trac_5911-reviewer.patch`

The reviewer patch fixes some typos and grammar issues. It also adjusts some examples to prevent doctest failures. Only my patch needs to be reviewed.



---

archive/issue_comments_046639.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-05T01:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46639",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046640.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-05T01:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46640",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_006165.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-05T01:33:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5911#event-6165"
}
```



---

archive/issue_comments_046641.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-05T01:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5911#issuecomment-46641",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
