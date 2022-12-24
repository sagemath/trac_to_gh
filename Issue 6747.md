# Issue 6747: Improve plotting of trees

archive/issues_006747.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  sage-combinat @jasongrout myurko\n\nWhen one plots a tree with  `G.plot(layout='tree')`, the result is ugly.  For one thing, a tree plot should never have crossing lines.  I have code that makes a nice tree plot in nearly-linear time, which should be included in Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6747\n\n",
    "created_at": "2009-08-14T18:02:05Z",
    "labels": [
        "graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Improve plotting of trees",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6747",
    "user": "boothby"
}
```
Assignee: boothby

CC:  sage-combinat @jasongrout myurko

When one plots a tree with  `G.plot(layout='tree')`, the result is ugly.  For one thing, a tree plot should never have crossing lines.  I have code that makes a nice tree plot in nearly-linear time, which should be included in Sage.

Issue created by migration from https://trac.sagemath.org/ticket/6747





---

archive/issue_comments_055504.json:
```json
{
    "body": "old plot",
    "created_at": "2009-08-14T18:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55504",
    "user": "boothby"
}
```

old plot



---

archive/issue_comments_055505.json:
```json
{
    "body": "Attachment [tree.png](tarball://root/attachments/some-uuid/ticket6747/tree.png) by boothby created at 2009-08-14 18:02:51\n\ndesired output",
    "created_at": "2009-08-14T18:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55505",
    "user": "boothby"
}
```

Attachment [tree.png](tarball://root/attachments/some-uuid/ticket6747/tree.png) by boothby created at 2009-08-14 18:02:51

desired output



---

archive/issue_comments_055506.json:
```json
{
    "body": "You code looks like it first chooses the center vertex in the graph, then converts is as a Poset by picking this special vertex as a root, and plotting this Poset... But you did not post the patch :-)",
    "created_at": "2009-08-14T19:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55506",
    "user": "@nathanncohen"
}
```

You code looks like it first chooses the center vertex in the graph, then converts is as a Poset by picking this special vertex as a root, and plotting this Poset... But you did not post the patch :-)



---

archive/issue_comments_055507.json:
```json
{
    "body": "Attachment [6747_tree_layout.patch](tarball://root/attachments/some-uuid/ticket6747/6747_tree_layout.patch) by boothby created at 2009-08-14 23:24:48\n\nUhm... my code does nothing like what you said.  And I didn't post the patch because I hadn't cleaned it up / incorporated it into the GraphPlot class / documented it.  But now I have!",
    "created_at": "2009-08-14T23:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55507",
    "user": "boothby"
}
```

Attachment [6747_tree_layout.patch](tarball://root/attachments/some-uuid/ticket6747/6747_tree_layout.patch) by boothby created at 2009-08-14 23:24:48

Uhm... my code does nothing like what you said.  And I didn't post the patch because I hadn't cleaned it up / incorporated it into the GraphPlot class / documented it.  But now I have!



---

archive/issue_comments_055508.json:
```json
{
    "body": "I just tried your patch, and as I never plotted any tree in Sage, I tried to generate some for a start.... I tried your algorithm on graphs.BalancedTree(3,4) and graphs.BalancedTree(3,5). They are displayed on my machine in a very odd shape ( the picture had a large width and a very small height ). I admit these graphs contain a lot of vertices and may not be good examples, but what do you think of this result ? Do you think there would be a way to slightly change you code so that in such cases the plot could have a look closer from what one gets with the current layout=tree parameter ?\n\nI know it is very easy to criticize in such cases, and much harder to come up with a good algorithm.. Thinking about it, I thought that maybe the best way to draw a tree properly would be to begin with a cross-free embedding of the tree in the plane ( as you mentionned ), then to use the usual trick of repulsion between vertices to obtain a balanced shape ? I know it is not a good solution because of its complexity. I'll continue thinking about it, though O_o",
    "created_at": "2009-08-18T12:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55508",
    "user": "@nathanncohen"
}
```

I just tried your patch, and as I never plotted any tree in Sage, I tried to generate some for a start.... I tried your algorithm on graphs.BalancedTree(3,4) and graphs.BalancedTree(3,5). They are displayed on my machine in a very odd shape ( the picture had a large width and a very small height ). I admit these graphs contain a lot of vertices and may not be good examples, but what do you think of this result ? Do you think there would be a way to slightly change you code so that in such cases the plot could have a look closer from what one gets with the current layout=tree parameter ?

I know it is very easy to criticize in such cases, and much harder to come up with a good algorithm.. Thinking about it, I thought that maybe the best way to draw a tree properly would be to begin with a cross-free embedding of the tree in the plane ( as you mentionned ), then to use the usual trick of repulsion between vertices to obtain a balanced shape ? I know it is not a good solution because of its complexity. I'll continue thinking about it, though O_o



---

archive/issue_comments_055509.json:
```json
{
    "body": "These are extreme examples, and I'm not sure that a top-down layout will ever look good.  I believe that the solution for this particular problem would be to implement a circular tree layout algorithm.  However, if you play with the parameters, you can get a fairly nice plot.\n\n\n```\n    T = graphs.BalancedTree(3,5)\n    P = T.plot(layout='tree',tree_root=0)\n    P.show(aspect_ratio=.1,figsize=(15,15))\n```\n",
    "created_at": "2009-08-19T16:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55509",
    "user": "boothby"
}
```

These are extreme examples, and I'm not sure that a top-down layout will ever look good.  I believe that the solution for this particular problem would be to implement a circular tree layout algorithm.  However, if you play with the parameters, you can get a fairly nice plot.


```
    T = graphs.BalancedTree(3,5)
    P = T.plot(layout='tree',tree_root=0)
    P.show(aspect_ratio=.1,figsize=(15,15))
```




---

archive/issue_comments_055510.json:
```json
{
    "body": "Applies fines, and I could not find any bug in it. Clearly improves the plotting for \"human\" trees. This new patch includes the previous one, plus :\n* A INPUT section\n* A new semicolumn after EXAMPLES ::\n\nIf you agree with these changes, you can set this ticket to positive review !\n\nNathann",
    "created_at": "2009-10-13T09:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55510",
    "user": "@nathanncohen"
}
```

Applies fines, and I could not find any bug in it. Clearly improves the plotting for "human" trees. This new patch includes the previous one, plus :
* A INPUT section
* A new semicolumn after EXAMPLES ::

If you agree with these changes, you can set this ticket to positive review !

Nathann



---

archive/issue_comments_055511.json:
```json
{
    "body": "Attachment [trac_6747-reviewer.patch](tarball://root/attachments/some-uuid/ticket6747/trac_6747-reviewer.patch) by @nthiery created at 2009-10-14 10:53:50\n\nThanks much for improving the layout of trees!\n\nPlease have a look at #7004, which also started splitting the layout algorithms in different methods. So we need to decide on a naming convention. \n\nThen I guess this patch can get in, and #7400 be rebased on it.",
    "created_at": "2009-10-14T10:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55511",
    "user": "@nthiery"
}
```

Attachment [trac_6747-reviewer.patch](tarball://root/attachments/some-uuid/ticket6747/trac_6747-reviewer.patch) by @nthiery created at 2009-10-14 10:53:50

Thanks much for improving the layout of trees!

Please have a look at #7004, which also started splitting the layout algorithms in different methods. So we need to decide on a naming convention. 

Then I guess this patch can get in, and #7400 be rebased on it.



---

archive/issue_comments_055512.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-19T21:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55512",
    "user": "@nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055513.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-30T20:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55513",
    "user": "myurko"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055514.json:
```json
{
    "body": "Replying to [comment:7 ncohen]:\n> Applies fines, and I could not find any bug in it. Clearly improves the plotting for \"human\" trees. This new patch includes the previous one, plus :\n>     * A INPUT section\n>     * A new semicolumn after EXAMPLES ::\n> \n> If you agree with these changes, you can set this ticket to positive review !\n> \n> Nathann\n\nThe change look fine.",
    "created_at": "2009-10-30T20:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55514",
    "user": "myurko"
}
```

Replying to [comment:7 ncohen]:
> Applies fines, and I could not find any bug in it. Clearly improves the plotting for "human" trees. This new patch includes the previous one, plus :
>     * A INPUT section
>     * A new semicolumn after EXAMPLES ::
> 
> If you agree with these changes, you can set this ticket to positive review !
> 
> Nathann

The change look fine.



---

archive/issue_comments_055515.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T16:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6747#issuecomment-55515",
    "user": "@mwhansen"
}
```

Resolution: fixed
