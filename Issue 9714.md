# Issue 9714: Graph(..., format='incidence_matrix') doesn't work with graphs that have loops, but G.incidence_matrix() does.  So?

Issue created by migration from https://trac.sagemath.org/ticket/9714

Original creator: was

Original creation time: 2010-08-10 00:16:47

Assignee: jason, ncohen, rlm

We have

```
sage: M = matrix(3, [1,2,0, 0,2,0, 0,0,1])
sage: g = Graph(M, format='adjacency_matrix')
sage: I = g.incidence_matrix(); I
[-1 -1  0  0  0  1]
[ 1  1  0  1  1  0]
[ 0  0  1  0  0  0]
```

But then:

```
sage: Graph(I, format='incidence_matrix').show(graph_border=True)
kaboom!
```


Either the first .incidence_matrix() should fail, or the second Graph(...) should work.


---

Comment by rlm created at 2010-08-10 00:43:29

Easy to fix, just replace (on line 944 of `graph.py`)

```
if len(NZ) != 2:
    msg += "There must be two nonzero entries (-1 & 1) per column."
    assert False
```

with something like

```
if len(NZ) == 1:
    if loops is None:
        loops = True
    elif not loops:
        msg += "There must be two nonzero entries (-1 & 1) per column."
        assert False
elif len(NZ) != 2:
    msg += "There must be two nonzero entries (-1 & 1) per column."
    assert False
```



---

Attachment


---

Comment by brunellus created at 2012-01-23 19:54:53

Then there is another problem: checking forgets possibility that there are only two vertices defined. I tried to fix that: see the second doctest.


---

Comment by brunellus created at 2012-01-23 19:54:53

Changing status from new to needs_review.


---

Comment by ncohen created at 2012-01-29 19:04:22

Helloooooooooooooooo !!!

I find a bit weird that this code deals with -1 and 1 entries for *undirected* graphs, but well... `^^;`

Anyway, here is a very small patch that just avoid some unnecessary computations. 

I give a positive review to your patch, and you can review mine if you have some time `:-)`

Nathann


---

Comment by brunellus created at 2012-01-31 11:50:45

Hi, thanks for the review. You are certainly right that -1 is weird thing in this context and constructor should accept a normal incidence matrix with two ones in each column. I'll start another ticket for this.

I'll set positive review as soon as the tests pass.


---

Comment by brunellus created at 2012-01-31 15:20:10

What do you say to this adjustment? :-)

Lukáš.


---

Comment by ncohen created at 2012-01-31 17:40:21

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2012-01-31 17:40:21

> What do you say to this adjustment? :-)

"Stupid me"

Ok, now it's good to go `:-)`

Nathann


---

Comment by jdemeyer created at 2012-02-03 11:23:33

Please state clearly which patches have to be applied.


---

Comment by brunellus created at 2012-02-06 09:55:48

Oh, sorry. :-)


---

Comment by brunellus created at 2012-02-06 10:15:14

(Just adding a proper commit message.)


---

Comment by jdemeyer created at 2012-02-15 10:05:34

The last two patches have one annoyingly long line as commit message.  Could you please shorten the line length.  Multiple lines are allowed, but the first line should make sense by itself.


---

Comment by jdemeyer created at 2012-02-15 10:05:42

Changing status from positive_review to needs_work.


---

Attachment


---

Attachment

Fixed too `:-)`

Nathann


---

Comment by ncohen created at 2012-02-15 10:59:53

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-02-22 10:44:18

Resolution: fixed
