# Issue 7634: switch default Sage graphs over to c_graph

Issue created by migration from https://trac.sagemath.org/ticket/7634

Original creator: rlm

Original creation time: 2009-12-09 02:07:02

Assignee: rlm

CC:  ncohen mvngu was robertwb jason

This is currently under discussion here:

http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5/c584929f270b2de3

I realized that it's probably actually time to switch over, since there are a few other developers working on Sage graphs besides just me now. That way if anything slows down, we are likely to find it out pretty quickly, and get it fixed. And, with the new defaults, things already feel more speedy:

BEFORE:

```
sage -t  "devel/sage-main/sage/graphs/graph.py"             
	 [113.1 s]
```

AFTER:

```
sage -t  "devel/sage-main/sage/graphs/graph.py"             
	 [78.5 s]
```



---

Comment by ncohen created at 2009-12-09 10:04:37

Hmmm... When applying your patch here is what I get :

```
~/sage/sage-A/sage/graphs$ sage -t graph.py 
sage -t  "devel/sage-A/sage/graphs/graph.py"                
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [360.5 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage-A/sage/graphs/graph.py"
Total time for all tests: 360.5 seconds
```

I know that this could not give you much information, but I do not know of any way to make -t more verbose... any idea ? 

Nathann


---

Comment by ncohen created at 2009-12-09 10:04:37

Changing status from new to needs_info.


---

Comment by ncohen created at 2009-12-09 11:10:27

Hmmm, it seems to come from the docstring 

```
G = graphs.CubeGraph(8)
H = G.distance_graph([1,3,5,7])
```


Which is *very* long !


---

Comment by AlexGhitza created at 2009-12-09 11:18:17

Replying to [comment:2 ncohen]:
> ----------------------------------------------------------------------
> The following tests failed:
> 
> 
>         sage -t  "devel/sage-A/sage/graphs/graph.py"
> Total time for all tests: 360.5 seconds
> }}}
> I know that this could not give you much information, but I do not know of any way to make -t more verbose... any idea ? 

I would try this :)


```
sage -t -verbose graph.py
```



---

Comment by ncohen created at 2009-12-09 11:57:20

Changing status from needs_info to needs_work.


---

Comment by ncohen created at 2009-12-09 11:57:20

Yes, I found it... So stupid of not having checked :-)

By the way, the problem indeed comes from this distance_graph doctest !

Nathann


---

Comment by rlm created at 2009-12-09 17:03:45

This is because `distance_graph` ultimately relies on `shortest_path`, which uses the networkx graphs. In other words, for each pair of vertices `distance_graphs` calls `shortest_path`, which creates a copy of the graph, calls a NetworkX distance function on it, and discards it. I have created a separate ticket for this issue at #7640.


---

Comment by rlm created at 2009-12-10 17:00:47

I guess it should be somewhere on the ticket that #7651 should be taken care of first, also.


---

Comment by ncohen created at 2009-12-12 18:05:10

With the patch from #7640, it gives :

BEFORE:

```
G = graphs.CubeGraph(8)
sage: time a=G.distance_graph([1,3,5,7])
CPU times: user 8.15 s, sys: 0.03 s, total: 8.17 s
Wall time: 8.18 s
```


AFTER:

```
G = graphs.CubeGraph(8)
sage: time a=G.distance_graph([1,3,5,7])
CPU times: user 6.51 s, sys: 0.03 s, total: 6.55 s
Wall time: 6.56 s
```



---

Comment by rlm created at 2009-12-12 19:04:27

Also need to be closed first: #7671 and #7672


---

Comment by rlm created at 2009-12-12 20:02:22

Add #7673 to the list.


---

Comment by rlm created at 2009-12-12 20:38:28

sorry, jason, i accidentally removed you from the cc block (not sure what happened there)


---

Comment by rlm created at 2009-12-15 18:20:24

The current patch does not split up graph.py, but the final version will...


---

Attachment

depends on 4.3.1.alpha1


---

Comment by rlm created at 2010-01-06 07:25:47

depends on trac_7634-switchover.patch


---

Comment by rlm created at 2010-01-06 07:26:31

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by jason created at 2010-01-06 07:30:35

Oh boy.  I spent some time yesterday and today adding a few functions and cleaning up some documentation to graph.py. Well, you beat me to being ready, so I guess I'll rebase my patch on top of this one, hoping it gets into 4.3.1 so my patch on top of it can get in too.


---

Comment by ncohen created at 2010-01-06 09:31:30

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-01-06 09:31:30

Well, this one does its jobs, and *finally* splits the graph.py file. c_graphs are now the default ones in Sage, and this patch renames what has to be. 

Positive review/Good work/Excellent news !

Nathann


---

Comment by rlm created at 2010-01-06 14:07:51

based on trac_7634-refactor.patch


---

Comment by rlm created at 2010-01-13 04:35:52

Resolution: fixed


---

Attachment
