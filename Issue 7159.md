# Issue 7159: [with patch, needs review] Graph.merge_vertices, and a bug in edge_boundary

Issue created by migration from https://trac.sagemath.org/ticket/7159

Original creator: ncohen

Original creation time: 2009-10-08 17:17:02

Assignee: rlm

This patch adds to the Graph class the function merge_vertices.

It is a very common operation in Graph Theory. In a Graph G, one merges two vertices u and v by deleting them and adding a new vertex, which is linked to any other vertex w such that there was an edge uw or vw in G. This can be done with any number of vertices at a time.

Besides, writing this class I noticed there was an error in function edge_boundary :

the function Graph.edge_boundary([u,v]) returns a list of edges, BUT :
    * the edges returned do not always contain u or v as their first element. it can be the second one in undirected graphs
    * The edges between u and v are returned, which is not the expected behaviour of this function

This patch fixes this too.


---

Comment by ncohen created at 2009-10-15 13:40:58

Changing status from new to needs_review.


---

Comment by AJonsson created at 2009-10-25 21:07:03

Changing status from needs_review to needs_work.


---

Comment by AJonsson created at 2009-10-25 21:07:03

Great minds think alike ;-)
I just made a ticket ( #7304 ) for edge contraction, but this ticket is more general, so closing mine as a duplicate.

However, there is something wrong in your patch, as my first try revealed this:

```
sage: P=graphs.PetersenGraph()
sage: P.merge_vertices([5,7])
sage: P.vertices()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```



---

Comment by ncohen created at 2009-10-25 23:16:01

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-10-25 23:16:01

Then I hope you will prefer this new version of the patch !!! I thought edge_boundary behaved a bit more nicely ( and mainly got worried about the directed case, thus overlooking the undirected one ... )

Nathann


---

Attachment

By the way, I can not find your email on the internet... It's good to see new people in Sage's graph theory section !! What are you studying ?


---

Comment by AJonsson created at 2009-10-26 18:03:24

I have looked at your new patch, and it seems good. The only thing I found to object against was

```
if (v in vertices) and not (u in vertices) and v != vertices[0]:
```

If edge_boundary works as expected, the second test should not be needed as u and v can never be in vertices at the same time. I attach a patch to remove the unneeded test. It applies on top of your patch.

If you agree with this, you can count this as a positive review.




Replying to [comment:4 ncohen]:
> By the way, I can not find your email on the internet... It's good to see new people in Sage's graph theory section !! What are you studying ?

I'm a student in mathematics and a bit of computer science. I use Sage for diverse calculations in graph theory, and when I find that Sage can't do all that I want it to, I have to do something about it ;-P


---

Attachment

Remove no-op tests


---

Comment by ncohen created at 2009-10-26 18:43:16

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-10-26 18:43:16

Amazing... I even forgot that I had already fixed this in the same patch :-p

Thank you for your help !!!


---

Comment by AJonsson created at 2009-10-31 09:30:57

Changing status from positive_review to needs_work.


---

Comment by AJonsson created at 2009-10-31 09:30:57

I read the trac guidelines more closely and there is a last tiny issue before this patch can be said to be perfect:

"Bug Fixes Must Be Doctested: The patch that fixes an issue must also contain a doctest specifically to test the problem."

So all that is missing is a test that displays the expected behavior of edge_boundary(), and that would fail without your patch. For example something like this:

```
sage: G=graphs.DiamondGraph()
sage: G.edge_boundary([0,1])
[(0, 2, None), (1, 2, None), (1, 3, None)]
```



---

Comment by ncohen created at 2009-10-31 10:28:37

Adds one test


---

Attachment

Perhaps the last one ? :-)


---

Comment by ncohen created at 2009-10-31 10:30:55

Changing status from needs_work to needs_review.


---

Comment by AJonsson created at 2009-10-31 18:41:41

Changing status from needs_review to positive_review.


---

Comment by AJonsson created at 2009-10-31 18:41:41

Replying to [comment:8 ncohen]:
> Perhaps the last one ? :-)

Let's hope so :-)

All looks fine to me. Positive review.


---

Comment by mhansen created at 2009-11-02 04:32:55

Resolution: fixed
