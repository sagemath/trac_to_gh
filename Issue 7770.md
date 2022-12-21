# Issue 7770: Implement Tower of Hanoi graph

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-12-27 00:02:14

Assignee: rlm

Keywords: tower of hanoi graph

The Tower of Hanoi puzzle can be described by a graph whose vertices are possible states of the disks on the pegs, with edges represdenting legitimate moves of a single disk.


---

Comment by rbeezer created at 2009-12-27 00:14:42

Changing status from new to needs_review.


---

Comment by rbeezer created at 2009-12-27 00:14:42

Some rough timing information on a 3 GHZ Core 2 Duo:

4 pegs, 10 disks, no labels, no layout info

`2^20 = 1,048,576` vertices

3,142,656 edges

240 seconds

Distance between vertex 0 and `(4^10)-1`, ie

the minimum number of moves to solve the puzzle:

742 ms

I could probably provide timing on sage.math for a release tour (along with a nice graphic).


---

Attachment


---

Comment by wdj created at 2009-12-30 02:15:21

Changing status from needs_review to needs_work.


---

Comment by wdj created at 2009-12-30 02:15:21

This looks like an interesting patch but 


```
sage -t  "devel/sage/sage/graphs/graph_generators.py"
```

seems to fail (sage 4.3, imac, 10.6.2).


---

Comment by wdj created at 2009-12-30 02:23:12

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2009-12-30 02:23:12

Replying to [comment:2 wdj]:
> This looks like an interesting patch but 
> 
> {{{
> sage -t  "devel/sage/sage/graphs/graph_generators.py"
> }}}
> seems to fail (sage 4.3, imac, 10.6.2).

Arrgghh ... 

Ignore this. I'll keep refereeing it.


---

Comment by wdj created at 2009-12-30 12:13:16

Positive review.

Installs fine on 64bit ubuntu and imac 10.6.2 running sage 4.3. Passes sage -testall on the ubuntu machine and has (I think only) unrelated failures on the imac. Also I check the html output for the reference manual and it looks good.

Thanks for this patch Rob! I have used it already in some lecture notes I'm working on for next semester.


---

Comment by wdj created at 2009-12-30 12:13:16

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2009-12-30 17:49:14

Hi David,

Thanks for the quick review, and I'm especially glad to hear it is being used *immediately*.  ;-)

I'm going to send you some extra info on the graph off-list. (I don't have permission to post it yet).

Rob


---

Comment by mhansen created at 2010-01-03 21:05:01

Resolution: fixed
