# Issue 7364: Implement eulerian orientation of a graph

Issue created by migration from https://trac.sagemath.org/ticket/7364

Original creator: ncohen

Original creation time: 2009-10-31 20:48:07

Assignee: rlm

Implement a method in Graph returning a DiGraph which corresponds to an eulerian orientation of the graph.

An eulerian orientation of an eulerian graph is an orientation such that d^+ = d^- = d/2 for any vertex.

If the graph is not eulerian, this method should return a DiGraph such that d^+ + d^- = d and | d^+ - d^- | <= 1

Nathann


---

Comment by ncohen created at 2009-11-01 10:57:50

Changing status from new to needs_review.


---

Comment by hivert created at 2009-11-22 18:40:19

Hi Nathann

Patch looks good. All tests passed! I'm ready to put a Positive review.

However, I'm not a graph expert so I've no idea how clever is the algorithm.
So maybe it should be reviewed by a graph expert. Speaking about clever algorithm, if the complexity is known and in particular if it's known to be optimal or not, it could be a good idea to put a "..note:" in the doc giving this information. Of course the preceding remarks apply to any graph algorithm (and even to any algorithm). So maybe you want to put a positive review anyway.

Cheers,

Florent


---

Comment by ncohen created at 2009-11-22 19:08:21

From the "complexity" point of view, this algorithm is linear in the number of edges in the graph, so I think it could be filed as "optimal".

From the "practical" point of view, I do not think it would be easy to improve, though I am more and more thinking about trying to write such methods in C rather than in Python... Most of the time in these algorithms is spent on Python considerations rather than on actual Graph computations...

I am sending a mail to sage-devel about your great idea of a general "Complexity" note in algorithms.

Nathann


---

Comment by rlm created at 2009-11-22 19:55:04

Replying to [comment:7 ncohen]:
> ... though I am more and more thinking about trying to write such methods in C rather than in Python... Most of the time in these algorithms is spent on Python considerations rather than on actual Graph computations...

You should use Sage's c_graphs directly: this will eliminate Python noise without forcing you to use pure C. Check out `sage/graphs/graph_fast.pyx` for an example...


---

Comment by rlm created at 2009-11-22 20:00:17

Sorry, I should have pointed you to `sage/graphs/trees.pyx` for a good example. It all starts with either
`from sage.graphs.base.sparse_graph cimport SparseGraph`
or
`from sage.graphs.base.dense_graph cimport DenseGraph`


---

Comment by hivert created at 2009-11-23 00:47:45

Replying to [comment:7 ncohen]:
> From the "complexity" point of view, this algorithm is linear in the number of edges in the graph, so I think it could be filed as "optimal".
> 
> From the "practical" point of view, I do not think it would be easy to improve, though I am more and more thinking about trying to write such methods in C rather than in Python... Most of the time in these algorithms is spent on Python considerations rather than on actual Graph computations...

If the complexity is optimal, going from python to C will only improve the speed by a constant factor. Be sure it's really worth it before spending to much time. I'm a little extreme on this, but is it worth spending hours of researchears time, where we can spend money for a faster computer ? ;-)

Note: this does *not* mean I'm not trying to improve the speed of my code ! It only means that a good algorithm is an slow language is much better than a bad algorithm in a fast language. When needed the first is much easier to improve. I'm generally reluctant towards premature optimization.  

Cheers,

Florent


---

Comment by ncohen created at 2009-11-23 06:57:55

To Robert : Thank you very much !!!! I'll definitely give it a look ! But you make it sound like I would then have to work on a new graph rather than use the Python one ! In this case, I do not really need to create a new graph but I would like the functions "get an edge coming out of this vertex" and "tell me where it goes" to be extremely fast... When will the default Sage Graph the be C ones ?

To Florent : I'm aware this only means changing a "factor", but I am living among computer scientists who find it extremely hard to stop thinking like "it is NP-complete : there is no algooorithm to solve it". And I swear I did not forget the word "polynomial". At some point I also wanted to write an algorithm ion Sage to compute the crossign number of a graph. Bruce Reed published a Linear Time algorithm for this problem, using Graph Minor theory. The result is a (2<sup>2</sup>2<sup>2</sup>2<sup>2</sup>2^2.... ) * n algorithm which no one can implement, even less use. That's why I prefer mentionning the "two". Besides, one of the reasons people in my lab keep from really switching to Sage is that they currently use Java, which is way faster. ( of course they have less algorithms, of course they miss many things, but Still, it is faster )

I'll update this patch today !

Nathann


---

Comment by ncohen created at 2009-11-23 07:00:49

I actually wrote 2<sup>{2</sup>{2<sup>{2</sup>{2^{...}}}}*n.


---

Comment by ncohen created at 2009-11-23 07:01:30

My god. I wrote what is called a "tower of exponentials". :-p


---

Comment by ncohen created at 2009-11-23 12:42:35

This patch should suit you :-)

Nathann


---

Comment by hivert created at 2009-11-23 15:28:28

Replying to [comment:14 ncohen]:
> This patch should suit you :-)

I'm really sorry to bother you again:

> This algorithm has complexity `O(m)`.

Is this a standard in graph theory to call 'm' the number of ??? Actually what ? Edge, Vertex or sum of Both... Maybe this is obvious but better explicit than implicit ;-)

I promiss I'll give you a positive review after that !


---

Comment by ncohen created at 2009-11-23 15:35:24

Done ! :-)


---

Attachment


---

Comment by hivert created at 2009-11-23 16:33:44

Ok ! Ready to go !


---

Comment by hivert created at 2009-11-23 16:33:44

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-29 05:24:11

Resolution: fixed
