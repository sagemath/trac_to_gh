# Issue 9594: Spring layout for graphs is currently random across platforms: mark the doctest accordingly

Issue created by migration from Trac.

Original creator: leif

Original creation time: 2010-07-24 23:12:42

Assignee: jason, ncohen, rlm

CC:  ddrake mpatel rbeezer schilly cremona

On 32-bit systems, we get the following doctest error in Sage 4.5.2.alpha0:

```sh
$ ./sage -t devel/sage/sage/graphs/generic_graph.py
...
    sage: G.get_pos()
Expected:
    {0: [1.17..., -0.855...],
     1: [1.81..., -0.0990...],
     2: [1.35..., 0.184...],
     3: [1.51..., 0.644...],
     4: [2.00..., -0.507...],
     5: [0.597..., -0.236...],
     6: [2.04..., 0.687...],
     7: [1.46..., -0.473...],
     8: [0.902..., 0.773...],
     9: [2.48..., -0.119...]}
Got:
    {0: [1.1644236010005358, -0.83686858657215979], 1: [1.7943839700815074, -0.066920666682206337], 2: [1.2689961125613971,
0.14359096356381118], 3: [1.511860539628787, 0.59162048325984706], 4:
[1.9941403734258905, -0.53845815492480542], 5: [0.59110867097474395,
-0.2204272806589378], 6: [2.0144421480067041, 0.70158250822163282], 7:
[1.4603696336476519, -0.46717593533332896], 8: [0.90427280509063312,
0.79073173670301911], 9: [2.4603584159299983, -0.097675067576871527]}
...
```


(See #9593 for making spring layout reproducible.)


---

Comment by leif created at 2010-07-24 23:16:32

See also [this comment at #9584](http://trac.sagemath.org/sage_trac/ticket/9584#comment:1); the doctest error reported there is now split off into this ticket.


---

Comment by leif created at 2010-07-25 08:31:30

Just adds a random tag to the failing doctest.


---

Attachment

I cannot _really_ test this myself, because `generic_graph.py` does still not terminate on my 32-bit system, and on 64-bit it wasn't an issue...

(At least the patch doesn't introduce new failures. ;-) )

Please review s.t. this can be merged into 4.5.2.alpha1.


---

Comment by leif created at 2010-07-25 08:39:12

Changing status from new to needs_review.


---

Comment by schilly created at 2010-07-25 09:16:19

are these the positions of the petersen graph? the odd thing is this is tested [at line 1565 much more unspecific](http://sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.get_pos).

I would also suggest to introduce some [iterations=some max val ](http://sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.plot) at those plots that do not stop when doing layout.


---

Comment by leif created at 2010-07-25 09:58:26

Replying to [comment:2 leif]:
> I cannot _really_ test this myself, because `generic_graph.py` does still not terminate on my 32-bit system, and on 64-bit it wasn't an issue...

I've reduced the problem size of the previously not terminating doctest and with the patch here applied now all doctests pass on the 32-bit system, too.


---

Comment by jhpalmieri created at 2010-07-25 15:27:58

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-07-25 15:27:58

With the possible patch at #9584 so that doctests actually terminate, this passes on the skynet machines cleo and iras.  Should the comment also mention this ticket (both #9583 and #9584)?  If you think so, replace the current patch, no need for another review.

Positive review, in any case.


---

Comment by jhpalmieri created at 2010-07-25 19:54:51

> (both #9583 and #9584)

Sorry, I meant "both #9593 and #9594".


---

Comment by leif created at 2010-07-25 20:02:29

Replying to [comment:6 jhpalmieri]:
> > (both #9583 and #9584)
> 
> Sorry, I meant "both #9593 and #9594".

Obviously... ;-)

I simply forgot to add the "backlink" at #9593, which should fix the problem in the long run (so I mentioned only that ticket in the patch's comment; with both, the line had gotten to long).


---

Comment by ddrake created at 2010-07-26 01:21:49

Resolution: fixed
