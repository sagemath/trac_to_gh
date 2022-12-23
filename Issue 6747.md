# Issue 6747: Improve plotting of trees

Issue created by migration from https://trac.sagemath.org/ticket/6747

Original creator: boothby

Original creation time: 2009-08-14 18:02:05

Assignee: boothby

CC:  sage-combinat jason myurko

When one plots a tree with  `G.plot(layout='tree')`, the result is ugly.  For one thing, a tree plot should never have crossing lines.  I have code that makes a nice tree plot in nearly-linear time, which should be included in Sage.


---

Comment by boothby created at 2009-08-14 18:02:25

old plot


---

Attachment

desired output


---

Comment by ncohen created at 2009-08-14 19:18:33

You code looks like it first chooses the center vertex in the graph, then converts is as a Poset by picking this special vertex as a root, and plotting this Poset... But you did not post the patch :-)


---

Attachment

Uhm... my code does nothing like what you said.  And I didn't post the patch because I hadn't cleaned it up / incorporated it into the GraphPlot class / documented it.  But now I have!


---

Comment by ncohen created at 2009-08-18 12:23:21

I just tried your patch, and as I never plotted any tree in Sage, I tried to generate some for a start.... I tried your algorithm on graphs.BalancedTree(3,4) and graphs.BalancedTree(3,5). They are displayed on my machine in a very odd shape ( the picture had a large width and a very small height ). I admit these graphs contain a lot of vertices and may not be good examples, but what do you think of this result ? Do you think there would be a way to slightly change you code so that in such cases the plot could have a look closer from what one gets with the current layout=tree parameter ?

I know it is very easy to criticize in such cases, and much harder to come up with a good algorithm.. Thinking about it, I thought that maybe the best way to draw a tree properly would be to begin with a cross-free embedding of the tree in the plane ( as you mentionned ), then to use the usual trick of repulsion between vertices to obtain a balanced shape ? I know it is not a good solution because of its complexity. I'll continue thinking about it, though O_o


---

Comment by boothby created at 2009-08-19 16:51:47

These are extreme examples, and I'm not sure that a top-down layout will ever look good.  I believe that the solution for this particular problem would be to implement a circular tree layout algorithm.  However, if you play with the parameters, you can get a fairly nice plot.


```
    T = graphs.BalancedTree(3,5)
    P = T.plot(layout='tree',tree_root=0)
    P.show(aspect_ratio=.1,figsize=(15,15))
```



---

Comment by ncohen created at 2009-10-13 09:42:32

Applies fines, and I could not find any bug in it. Clearly improves the plotting for "human" trees. This new patch includes the previous one, plus :
    * A INPUT section
    * A new semicolumn after EXAMPLES ::

If you agree with these changes, you can set this ticket to positive review !

Nathann


---

Attachment

Thanks much for improving the layout of trees!

Please have a look at #7004, which also started splitting the layout algorithms in different methods. So we need to decide on a naming convention. 

Then I guess this patch can get in, and #7400 be rebased on it.


---

Comment by ncohen created at 2009-10-19 21:24:31

Changing status from needs_work to needs_review.


---

Comment by myurko created at 2009-10-30 20:56:53

Changing status from needs_review to positive_review.


---

Comment by myurko created at 2009-10-30 20:56:53

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

Comment by mhansen created at 2009-10-31 16:44:14

Resolution: fixed
