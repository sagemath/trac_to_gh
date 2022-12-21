# Issue 9143: Speed up graph generation using Cython

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-06-04 22:05:44

Assignee: jason, ncohen, rlm

CC:  ncohen rlm robertwb

It's amazing how slow our graph generator is:


```
sage: %time gg=list(graphs(7))
CPU times: user 12.31 s, sys: 0.10 s, total: 12.41 s
Wall time: 12.87 s
```


Compare this to nauty's C implementation (with approximately the same algorithm)


```
sage: %timeit hh=graphs.nauty_geng('-q 7')
5 loops, best of 3: 171 ms per loop
```


Notice that the vast majority of the time is spent in some python calls, which presumably could be much, much faster if we instead used the underlying C structure via Cython.


```
sage: %prun gg=list(graphs(7))
         4355876 function calls (4284237 primitive calls) in 14.011 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    46134    2.668    0.000    2.923    0.000 {iterator_edges}
   362828    1.897    0.000    1.897    0.000 {add_edge}
    33007    1.698    0.000    7.775    0.000 graph.py:760(__init__)
   289792    1.209    0.000    1.209    0.000 {has_edge}
   125832    0.625    0.000    0.625    0.000 {iterator_verts}
     6564    0.604    0.000    5.020    0.001 {sage.groups.perm_gps.partn_ref.refinement_graphs.search_tree}
    33006    0.476    0.000    8.523    0.000 generic_graph.py:416(__copy__)
13050/1045    0.441    0.000   14.000    0.013 graph_generators.py:5059(canaug_traverse_edge)
    33007    0.395    0.000    0.470    0.000 function_mangling.py:205(fix_to_pos)
20064/13314    0.321    0.000    2.453    0.000 generic_graph.py:10582(relabel)
    33006    0.318    0.000    0.318    0.000 {add_vertices}
   289792    0.282    0.000    1.491    0.000 generic_graph.py:5256(has_edge)
     6750    0.255    0.000    1.923    0.000 generic_graph.py:72(__eq__)
     5893    0.235    0.000    0.354    0.000 graph_generators.py:5228(check_aut_edge)
142579/89695    0.195    0.000    7.128    0.000 copy.py:65(copy)
   546806    0.191    0.000    3.114    0.000 generic_graph.py:5386(edge_iterator)
    46692    0.175    0.000    0.524    0.000 generic_graph.py:4817(vertices)
    33007    0.166    0.000    0.824    0.000 generic_graph.py:28(__init__)
    13314    0.162    0.000    0.162    0.000 {relabel}
   128177    0.135    0.000    0.135    0.000 {sorted}
   132025    0.126    0.000    0.171    0.000 generic_graph.py:1531(name)
   125832    0.124    0.000    0.749    0.000 generic_graph.py:4731(vertex_iterator)
   105955    0.110    0.000    0.110    0.000 {hasattr}
```





---

Comment by rlm created at 2010-06-04 22:53:01

Every time I ask about "yield" statements in Cython, I always get the same response: very close, not there yet. It will be very easy for me to fix this, once they are implemented. Until then, it's probably ten times the work...


---

Comment by jason created at 2010-06-05 00:25:16

Ah, okay, thanks for the update. I'm CCing robertwb so that he sees (yet again) another vote for yield statements in Cython.  I'm sure they'll come in time.


---

Comment by robertwb created at 2010-06-05 04:18:24

Well, we're very close, but not there yet ;). Realistically, I'm 90% sure they'll be implemented by the time the summer is out, now that I don't have to spend every waking minute on my thesis.


---

Comment by rlm created at 2010-06-05 05:33:08

Replying to [comment:3 robertwb]:
> ... now that I don't have to spend every waking minute on my thesis. 

+1!

I was also going to mention in response to

> I'm CCing robertwb so that he sees (yet again) another vote for yield statements in Cython.

that I believe in one-person-one-vote, and I must disclose that I have already voted for this :)


---

Comment by rlm created at 2011-12-27 18:41:36

This is now part of #9559.


---

Comment by @DaveWitteMorris created at 2020-03-30 01:09:04

Changing status from new to needs_review.


---

Comment by @DaveWitteMorris created at 2020-03-30 01:09:04

As mentioned in comment:5, the problem has been fixed, so this ticket can be closed as a duplicate of #9559.

```
sage: ### try sage
sage: %time gg=list(graphs(7))
CPU times: user 83.6 ms, sys: 15.4 ms, total: 99.1 ms
Wall time: 117 ms
sage: ###
sage: ### now compare with nauty
sage: %timeit hh=graphs.nauty_geng('-q 7')
The slowest run took 11.31 times longer than the fastest. This could mean that an intermediate result is being cached.
1000000 loops, best of 5: 409 ns per loop
sage: ###
sage: ### try a larger example with sage
sage: %time gg=list(graphs(8))
CPU times: user 390 ms, sys: 17.6 ms, total: 407 ms
Wall time: 426 ms
sage: ###
sage: ### now compare with nauty again
sage: %timeit hh=graphs.nauty_geng('-q 8')
The slowest run took 9.17 times longer than the fastest. This could mean that an intermediate result is being cached.
1000000 loops, best of 5: 456 ns per loop
```



---

Comment by @DaveWitteMorris created at 2020-03-30 01:09:15

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-04-14 16:06:06

Resolution: duplicate
