# Issue 9727: RepresentationGraph method that generalizes IntervalGraph

Issue created by migration from Trac.

Original creator: edward.scheinerman

Original creation time: 2010-08-11 20:43:30

Assignee: jason, ncohen, rlm

CC:  ncohen

This patch creates a new graph constructor called RepresentationGraph. This method generalizes IntervalGraph. 


---

Comment by edward.scheinerman created at 2010-08-11 20:46:17

The old IntervalGraph method did not permit the same interval to be used twice for different vertices (and gave an erroneous result in some cases). The new IntervalGraph method in this patch fixes those issues.


---

Comment by ncohen created at 2010-08-12 04:19:16

Changing status from new to needs_work.


---

Attachment


---

Comment by edward.scheinerman created at 2010-08-15 20:33:37

Hello. This latest version of the patch now passes all tests!


---

Comment by edward.scheinerman created at 2010-08-15 20:33:37

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-08-23 02:55:34

Hmmm.. I know that I would never had noticed it had I not been working on Sage's graphs for a long time, but it looks like what RepresentationGraph does is already a feature of the Graph constructor : it is illustrated as the third example of `Graph?`. What do you think we should do in this case ? Clearly, this information is not very easy to get, and my method IntervalGraph should just call this constructor instead of doing the same job again (though we can slightly optimise if we know it is an interval graph)... Well, what do you think ? `:-/`

Nathann


---

Comment by ncohen created at 2010-08-23 02:55:34

Changing status from needs_review to needs_info.


---

Comment by edward.scheinerman created at 2010-08-23 22:20:56

Interesting, but the Graph constructor works differently and does not provide all the functionality that GraphRepresentation does. For example, it will not solve the problem of repeated intervals being recognized as separate vertices (but with the same closed neighborhoods). It will also not accept a dictionary instead of a list as we have set up in RepresentationGraph. 

One solution might be to rework the Graph() constructor to accept a [dictionary,function] pair. In that case, the vertices would be the keys of the dictionary. Two vertices would be adjacent if the function, applied to the values associated with two keys, returns True. How difficult would that be? If easy, then that may be a preferable route. If difficult, then I prefer this route.

It is true that if one sorts the intervals before iterating over pairs, some speed up can be realized (especially for a sparse interval graph); but this efficiency comes at a cost of some generality. Also, for a random interval graph, the speedup will not be so dramatic as these random graphs are dense.

Ed


---

Comment by edward.scheinerman created at 2010-08-25 12:13:21

Changing status from needs_info to needs_review.


---

Comment by edward.scheinerman created at 2010-09-06 18:58:05

I withdraw this ticket. A new version of IntervalGraph is posted as tickect #9862. RepresentationGraph is probably not needed as its functionality is (mostly) available in the Graph() constructor. Modifications to Graph() to accept [dictionary,function] may be forthcoming at a later date.


---

Comment by edward.scheinerman created at 2010-09-06 18:58:05

Remove assignee jason, ncohen, rlm.


---

Comment by edward.scheinerman created at 2010-09-07 01:42:48

Set assignee to edward.scheinerman.


---

Comment by edward.scheinerman created at 2010-09-07 01:43:18

Remove assignee edward.scheinerman.


---

Comment by ddrake created at 2010-09-08 02:20:47

Resolution: wontfix


---

Comment by ddrake created at 2010-09-08 02:20:47

Ed has request that this ticket be closed. He sent an email that said:


```
Dear Sage Manager:

A few weeks ago I posted Trac ticket #9727 entitled "RepresentationGraph method
that generalizes IntervalGraph". Since that time, working with Nathann Cohen, I
posted an alternative, more focused solution to minor glitches in the
IntervalGraph method. Further, the RepresentationGraph method functionality is
partially already present in the Graph() constructor and I am considering a
direct enhancement of Graph() at some future time to add a bit more
functionality.

So, to make a long story short, I would like to cancel my posting of 9727, but I
don't see how to do that in Trac. Can you please do this for me?

Thanks,

Ed Scheinerman
```


I'm setting this as "wontfix" since it seems like they, well, won't use this enhancement and work on things later.
