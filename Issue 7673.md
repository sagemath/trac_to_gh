# Issue 7673: implement Dijkstra's algorithm for C graphs

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-12-12 19:51:21

Assignee: rlm

CC:  ncohen

As a follow up of #7640.


---

Comment by ncohen created at 2009-12-12 21:57:47

To write it I could need an implementation of heaps in Cython ( I would need top keep a list sorted through the execution of the algorithm, with insertion/deletions ). If anybody knows about such a thing, please tell me :-)


---

Comment by wdj created at 2009-12-12 22:19:12

I think these are implemented in 
http://trac.sagemath.org/sage_trac/attachment/ticket/6452/trac_6452-ring-codes.patch
However, the patch was rejected due to memory errors. The author has not fixed them
yet.

Please be my guest:-)


---

Comment by ncohen created at 2009-12-13 13:19:19

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-12-13 13:19:19

Here is one version using heapq from Python.... Once we will have a good Cython implementation of heaps, it will take something like 20 seconds to update it ! :-)


---

Comment by rlm created at 2009-12-14 02:30:55

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2009-12-14 02:30:55

This is going to conflict with the patch at #7640. Can you rebase this patch on 4.3.rc0 + #7640?


---

Comment by rlm created at 2009-12-14 02:53:40

rebased on 4.3.rc0 + #7640


---

Attachment

Replying to [comment:4 rlm]:
> This is going to conflict with the patch at #7640. Can you rebase this patch on 4.3.rc0 + #7640?

OK, I've posted a new patch.


---

Comment by rlm created at 2009-12-14 02:54:06

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-12-14 03:04:25

Changing status from needs_review to positive_review.


---

Comment by ylchapuy created at 2009-12-14 09:18:39

Changing status from positive_review to needs_work.


---

Comment by ylchapuy created at 2009-12-14 09:18:39

Hi,
I'm sorry, but this implementation is buggy...

```
sage: G = Graph()
sage: G.add_edge(0,1,9)
sage: G.add_edge(0,2,8)
sage: G.add_edge(1,2,7)
sage: G.shortest_path(0,1,by_weight=True)
[0, 1]
sage: G.shortest_path_length(0,1,by_weight=True)
9
sage: Gc = G.copy(implementation='c_graph')
sage: Gc.shortest_path(0,1,by_weight=True)
[0, 2, 1]
sage: Gc.shortest_path_length(0,1,by_weight=True)
15
```



---

Comment by ncohen created at 2009-12-14 11:12:52

Clearly, it is !! Thank you for taking a lot at it :-)

Well, the only bugfix I can think about is to keep in memory the vertex v such that dist_y[v] + dist_x[v] is minimal, and only build the path when the neighborhoods of x and y at distance 2*(dist_y[v] + dist_x[v]) have been explored. It clearly fixes your counter-example, and I think it should solve all others, but I woud be glad to write a nicer solution... Any idea ? :-)

Thank you very much again ! :-)

Nathann


---

Comment by ylchapuy created at 2009-12-14 11:58:41

I don't know if it's nicer, but did you look at how it's done in networkx? 

Replying to [comment:9 ncohen]:
> I woud be glad to write a nicer solution... Any idea ? :-)


---

Comment by wdj created at 2009-12-14 12:23:23

Replying to [comment:9 ncohen]:
> Clearly, it is !! Thank you for taking a lot at it :-)
> 
> Well, the only bugfix I can think about is to keep in memory the vertex v such 
> that dist_y[v] + dist_x[v] is minimal, and only build the path when 
> the neighborhoods of x and y at distance 2*(dist_y[v] + dist_x[v]) have 
> been explored. It clearly fixes your counter-example, and I think it 


Maybe this is related to the "piority queue" in Demaine's descrition
of the algorithm in


```
http://ocw.mit.edu/NR/rdonlyres/Electrical-Engineering-and-Computer-Science/6-046JFall-2005/651C0FC9-55D1-4404-A801-A9D0392A668C/0/lec17.pdf
```

at

```
http://ocw.mit.edu/OcwWeb/Electrical-Engineering-and-Computer-Science/6-046JFall-2005/VideoLectures/detail/embed17.htm
```



> should solve all others, but I woud be glad to write a nicer solution... 
> Any idea ? :-)
> 
> Thank you very much again ! :-)
> 
> Nathann


---

Comment by ncohen created at 2009-12-14 12:30:07

Here is a fixed version :-)


---

Comment by ncohen created at 2009-12-14 12:30:07

Changing status from needs_work to needs_review.


---

Attachment

I do not think so, this bug just came from the fact that this version of dijkstra is bidirectional, and I wrongly assumed that as in the simple version of it, the first path found was the correct path. Obviously ( see your example ) it is not, and I expect this version of the algorithm to be correct :-)

Nathann


---

Comment by rlm created at 2009-12-14 21:23:45

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2009-12-14 21:23:45

Sorry I missed that mistake! :o

The new patch looks good.


---

Comment by mhansen created at 2009-12-15 16:03:23

Resolution: fixed
