# Issue 5911: greatly improve the documentation one gets from Graph?

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-27 13:02:05

Assignee: rlm

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


---

Comment by jason created at 2009-04-27 15:59:15

+1!

So you're saying that Graph? should be something like graphs?


---

Comment by ncohen created at 2009-08-03 17:09:13

I began to write something, as I thought nobody was working on it seeing that last message was posted 3 months ago ;-)

What I have written is just a short introduction meant for user **really** unfamiliar with graphs in Sage and in general.. I expect a lot of critics from you, and I will change it accordingly, but I have spent much time in the past days trying to explain how to use graphs in Sage to some of my friends that I thought the best way may be to directly document this section... Tell me what you would change to this :

http://www-sop.inria.fr/members/Nathann.Cohen/infograph.py


---

Comment by rlm created at 2009-08-05 16:30:36

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

Comment by ncohen created at 2009-08-05 18:37:55

Hello !

Several questions :

* I agree that way to raise errors and exceptions have no real place in Graph?. Where should I put them ? In the looooooooong docstring at the beginning of file graph.py ?

* I do not understand their purpose anyway. There or elsewhere O_o

* No problem with '::' as I can see some occurences of them in this docstring... What are they meant to do, though ? ;-)

* I did not post a patch thinking it would be much easier to read it this way as it seemed far from a final version. The next one will be a patch ;-)


---

Comment by ncohen created at 2009-08-17 15:06:14

Here is the patch you requested.. Where do you think we should store these doctests you mentionned if not in this docstring ?


---

Attachment


---

Comment by rlm created at 2009-08-26 18:36:33

I've added some editing in a second patch, and I'd like to give this a positive review, but the documentation for `DiGraph?` suffers from the same fault, and I would feel less guilty if this ticket addressed that as well.


---

Comment by rlm created at 2009-08-26 18:37:58

apply on top of doc_graph.patch


---

Attachment

What about a good old  : "cf. Graph" (or a plain copy of Graph?), as it is exactly the same ? ^^;

We could just write a list of the functions of DiGraph that are unaavailable in Graph, couldn't we ?


---

Comment by ncohen created at 2009-10-03 09:32:18

Still around ? ;-)


---

Comment by rlm created at 2009-10-08 16:38:03

Replying to [comment:10 ncohen]:
> What about a good old  : "cf. Graph" (or a plain copy of Graph?), as it is exactly the same ? ^^;
> 
> We could just write a list of the functions of DiGraph that are unaavailable in Graph, couldn't we ?

Imagine you have never used Sage before, and you really really like DiGraphs. So one of the first things you do in Sage, aside from `2+2` or `factor(factorial(12))`, is type `DiGraph?`. I think there are such (potential) users out there, and the documentation there should be independently helpful. Certainly a reference to `Graph?` would be appropriate, but the docs you get from `DiGraph?` should also be self-contained and helpful.


---

Comment by ncohen created at 2009-10-08 16:47:16

Then a plain copy could do, couldn't it ? Plus some DiGraph-specific functions .. ;-)


---

Comment by rlm created at 2009-10-08 16:50:14

Replying to [comment:13 ncohen]:
> Then a plain copy could do, couldn't it ?

Essentially, yes, subject to `s/Graph/DiGraph`.

> Plus some DiGraph-specific functions .. ;-)

For the DiGraph fans!


---

Comment by ncohen created at 2009-10-13 08:15:04

New version with an updated DiGraph section. Some problem, still : when running a sage -t on graph.py, Python does not like to see g.diameter ? which is mentioned in the doc.

Do you know how to fix this ?

This new patch is a flattened version of the previous ones, plus the updates. Only this one should be applied.

Nathann


---

Comment by ncohen created at 2009-10-13 08:15:04

Changing status from needs_work to needs_review.


---

Attachment

Hmmm.. This -- should -- have been a flattened version of all the patches, though it is not and I wonder why. This patch needs doc_graph.patch to be applied first, and contains trac_5911-editing.patch. So only doc_graph.patch and this patch should be applied.

I tried to build a real flattened version, but for some reason I can not O_o

Nathann


---

Attachment

reviewer patch


---

Comment by mvngu created at 2009-10-28 15:02:37

I have attached a reviewer patch. So patches should be applied in the following order:

 1. `doc_graph.patch`
 1. `trac_5911.patch`
 1. `trac_5911-reviewer.patch`

The reviewer patch fixes some typos and grammar issues. It also adjusts some examples to prevent doctest failures. Only my patch needs to be reviewed.


---

Comment by mhansen created at 2009-11-05 01:26:21

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-05 01:26:21

Looks good to me.


---

Comment by mhansen created at 2009-11-05 01:33:06

Resolution: fixed
