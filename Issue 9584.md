# Issue 9584: Some graph-related doctest failures and timeouts with 4.5.2.alpha0

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-23 08:12:35

Assignee: mvngu

CC:  jhpalmieri leif ncohen

Reported by John Palmieri and Leif Leonhardy on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/da2dfbbe52d9917b#da2dfbbe52d9917b):

```
On 07/23/2010 12:18 AM, leif wrote:
> John H Palmieri wrote:
>> On iras (ia64-Linux-suse), after continuing the build, one failure:
>>
>> sage -t -long "devel/sage/sage/graphs/genus.pyx"
>> **********************************************************************
>> File "/home/palmieri/iras/sage-4.5.2.alpha0/devel/sage/sage/graphs/
>> genus.pyx", line 129:
>>     sage: get_memory_usage(t)
>> Expected:
>>     0.0
>> Got:
>>     -0.28125
>> **********************************************************************
> 
> So whenever you run out of memory on that machine, start a few instances
> of that program... :D :D :D
> 
>> Several machines (cleo, iras) get timeouts on generic_graph.py.
> 
> (Doesn't terminate within an hour here on 32-bit Ubuntu, Pentium 4...)
```

These may be unrelated to each other, however.


---

Comment by leif created at 2010-07-23 09:24:39

''Copied from the sage-release thread (slightly beautified):
''
  1: `devel/sage/sage/graphs/generic_graph.py`
  
    Doesn't terminate at all(?), gets killed even if I test just that file, with `SAGE_TIMEOUT_LONG=3600` (1 hour)!

Testing with `-verbose`, I now experience the same doctest failure John [Cremona]
reported (and only that):

```
...
Trying:
    P = G.plot(save_pos=True, layout='spring')###line 11577:_sage_    >>> P = G.plot(save_pos=True, layout='spring')
Expecting nothing
ok
Trying:
    G.get_pos()###line 11581:_sage_    >>> G.get_pos()
Expecting:
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
**********************************************************************
File "/home/leif/sage-4.5.2.alpha0/devel/sage/sage/graphs/generic_graph.py", line 8617, in __main__.example_191
Failed example:
    G.get_pos()###line 11581:_sage_    >>> G.get_pos()
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
    {0: [1.1644236010005358, -0.83686858657215979], 1:
[1.7943839700815074, -0.066920666682206337], 2: [1.2689961125613971,
0.14359096356381118], 3: [1.511860539628787, 0.59162048325984706], 4:
[1.9941403734258905, -0.53845815492480542], 5: [0.59110867097474395,
-0.2204272806589378], 6: [2.0144421480067041, 0.70158250822163282], 7:
[1.4603696336476519, -0.46717593533332896], 8: [0.90427280509063312,
0.79073173670301911], 9: [2.4603584159299983, -0.097675067576871527]}
Trying:
    T = list(graphs.trees(Integer(7)))###line 11595:_sage_    >>> T = list(graphs.trees(7))
Expecting nothing
ok
...
```


The following is the last output I get (note that the examples aren't tested in order, i.e. original source line numbers usually aren't monotonic):

```
Trying:
    D.connected_component_containing_vertex(Integer(0))###line 3090:_sage_    >>> D.connected_component_containing_vertex(0)
Expecting:
    [0, 1, 2, 3]
ok
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    change_warning_output(sys.stdout)
Expecting nothing
ok
Trying:
    graphs.PetersenGraph().blocks_and_cut_vertices()###line 3117:_sage_    >>> graphs.PetersenGraph().blocks_and_cut_vertices()
Expecting:
    ([This is the Trac macro *6, 4, 9, 7, 5, 8, 3, 2, 1, 0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#6, 4, 9, 7, 5, 8, 3, 2, 1, 0-macro), [])
ok
Trying:
    graphs.PathGraph(Integer(6)).blocks_and_cut_vertices()###line 3119:_sage_    >>> graphs.PathGraph(6).blocks_and_cut_vertices()
Expecting:
    ([[5, 4], [*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

	 [3600.9 s]

----------------------------------------------------------------------
The following tests failed:


	sage -t -long -verbose "devel/sage/sage/graphs/generic_graph.py" # Time out
Total time for all tests: 3600.9 seconds

real	60m1.029s
user	0m2.360s
sys	0m0.884s
```

_[Note the real/CPU time.]_

The funny thing is that with `-verbose`, I do not even get the shell prompt back (I redirected stderr to stdout and tee'd it); `./sage -t -long ...` terminates, but I guess its now orphan child (`python /home/leif/.sage//tmp/.doctest_generic_graph.py`[sic], which is actually running - consuming CPU time, in contrast to its two `gap` children, which sleep due to blocking reads) keeps at least one of the file descriptors open...

_[This was on *32-bit* Ubuntu 9.04 (P4 Prescott 3.2GHz, gcc 4.3.3, native code). John Cremona experienced the doctest failure on *32-bit* SuSE...]_


---

Comment by leif created at 2010-07-23 09:51:49

Replying to [comment:1 leif]:
> 

```
...
real	60m1.029s
user	0m2.360s
sys	0m0.884s
```

> _[Note the real/CPU time.]_

Should read _"*user*/CPU time"_; i.e. the process does idle/sleep/wait most of the first hour. After gotten "killed", gets busy somehow... :)


---

Comment by rlm created at 2010-07-24 11:11:44

What are the relevant tickets which were merged since 4.5.1? Looking at the list on the Roadmap, under graph theory, none of them really look like they could cause something like this...

If I try running the command last printed above on geom.math, I instantly get:

```
sage: graphs.PathGraph(Integer(6)).blocks_and_cut_vertices()
([[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]], [4, 3, 2, 1])
```


Hmmm...


---

Comment by rlm created at 2010-07-24 11:23:11

Also, when trying to reproduce this on cleo, sage fails to start (this is the one in wstein's build dir), and I can't copy all the bits because of permission issues. Has anyone else tried to isolate the command causing this on cleo?


---

Comment by leif created at 2010-07-24 14:14:53

Replying to [comment:3 rlm]:
> If I try running the command last printed above on geom.math, I instantly get:

```
sage: graphs.PathGraph(Integer(6)).blocks_and_cut_vertices()
([[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]], [4, 3, 2, 1])
```

> 
> Hmmm...
I've added some flushs in `ncadoctest.py`, now the log ends with:

```
Trying:
    g = graphs.RandomGNP(Integer(30),RealNumber('.5'))###line 3276:_sage_    >>> g = graphs.RandomGNP(30,.5)
Expecting nothing
ok
Trying:
    st = g.steiner_tree(g.vertices()[:Integer(5)])###line 3277:_sage_    >>> st = g.steiner_tree(g.vertices()[:5])
Expecting nothing
ok
Trying:
    st.is_tree()###line 3278:_sage_    >>> st.is_tree()
Expecting:
    True
ok
Trying:
    all([v in st for v in g.vertices()[:Integer(5)] ])###line 3283:_sage_    >>> all([v in st for v in g.vertices()[:5] ])
Expecting:
    True
ok
Trying:
    g = Integer(2) * graphs.PetersenGraph()###line 3290:_sage_    >>> g = 2 * graphs.PetersenGraph()
Expecting nothing
ok
Trying:
    st = g.steiner_tree([Integer(5),Integer(15)])###line 3291:_sage_    >>> st = g.steiner_tree([5,15])
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: The given vertices do not all belong to the same connected component. This problem has no solution !
ok
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

	 [1801.4 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -verbose "devel/sage/sage/graphs/generic_graph.py" # Time out
Total time for all tests: 1801.4 seconds

real	30m1.590s
user	0m1.912s
sys	0m0.536s
^C
leif`@`californication:~/sage-4.5.2.alpha0-j6$ 
```

(Note that again I don't get a shell prompt, and `python`, `gap` and `sage-cleaner` are still "running", only `python .../.doctest_generic_graph.py` consumes CPU time. I've decreased `SAGE_TIMEOUT_LONG` to half an hour, the shown tests take much shorter, about 55 seconds.)


---

Comment by leif created at 2010-07-24 14:28:40

Ooops, I just noticed the log above is even *without* `-long`, so I actually _increased_ `SAGE_TIMEOUT`, and did not include the long tests (that was yesterday). The behavior is samewhat similar though.


---

Comment by leif created at 2010-07-24 15:07:36

*With* `-long` (and `SAGE_TIMEOUT_LONG` decreased to 15 minutes):

```sh
Trying:
    all([v in st for v in g.vertices()[:Integer(5)] ])###line 3283:_sage_    >>> all([v in st for v in g.vertices()[:5] ])
Expecting:
    True
ok
Trying:
    g = Integer(2) * graphs.PetersenGraph()###line 3290:_sage_    >>> g = 2 * graphs.PetersenGraph()
Expecting nothing
ok
Trying:
    st = g.steiner_tree([Integer(5),Integer(15)])###line 3291:_sage_    >>> st = g.steiner_tree([5,15])
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: The given vertices do not all belong to the same connected component. This problem has no solution !
ok
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

	 [900.9 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long -verbose "devel/sage/sage/graphs/generic_graph.py" # Time out
Total time for all tests: 900.9 seconds

real	15m1.016s
user	0m1.084s
sys	0m0.360s
^C
leif`@`californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ 
```

I simply forgot it was the same; the shown tests take roughly 2 minutes and a few seconds.


---

Comment by jhpalmieri created at 2010-07-24 15:23:02

Replying to [comment:4 rlm]:
> Also, when trying to reproduce this on cleo, sage fails to start (this is the one in wstein's build dir), and I can't copy all the bits because of permission issues. Has anyone else tried to isolate the command causing this on cleo?

Today the doctest is passing for me.  I don't know why.  (A few days ago it failed with "make ptestlong", and then it failed repeatedly from the command line.)  If you want to try it yourself, I think my account on skynet is now readable: look in `/home/palmieri/cleo/sage-4.5.2.alpha0/`.

I'm trying generic_graph.py again with longer values for SAGE_TIMEOUT_LONG.  Back in a few hours :)


---

Comment by leif created at 2010-07-24 16:31:46

Replying to [comment:8 jhpalmieri]:
> I'm trying generic_graph.py again with longer values for SAGE_TIMEOUT_LONG.  Back in a few hours :)

Also on cicero (32-bit)?


---

Comment by leif created at 2010-07-24 16:36:27

Replying to [comment:9 leif]:
> Replying to [comment:8 jhpalmieri]:
> > I'm trying generic_graph.py again with longer values for SAGE_TIMEOUT_LONG.  Back in a few hours :)
> 
> Also on cicero (32-bit)?
Or did all tests (except #9554) pass on that machine? (I haven't seen a report.)


---

Comment by jhpalmieri created at 2010-07-24 16:42:20

On cicero, I get the failure reported by John Cremona on sage-release:

```
sage -t  -long "devel/sage/sage/graphs/generic_graph.py"
**********************************************************************
File "/home/palmieri/cicero/sage-4.5.2.alpha0/devel/sage/sage/graphs/generic_graph.py", line 11581\
:
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
    {0: [1.1644236010005358, -0.83686858657215979], 1: [1.7943839700815074, -0.066920666682206337]\
, 2: [1.2689961125613971, 0.14359096356381118], 3: [1.511860539628787, 0.59162048325984706], 4: [1\
.9941403734258905, -0.53845815492480542], 5: [0.59110867097474395, -0.2204272806589378], 6: [2.014\
4421480067041, 0.70158250822163282], 7: [1.4603696336476519, -0.46717593533332896], 8: [0.90427280\
509063312, 0.79073173670301911], 9: [2.4603584159299983, -0.097675067576871527]}
**********************************************************************
```

Is there a separate ticket for this one?  Testing completes in under 5 minutes: no timeout.

I get the timeout on iras, and I've started that test again now, too.


---

Comment by leif created at 2010-07-24 17:52:23

Replying to [comment:11 jhpalmieri]:
> On cicero, I get the failure reported by John Cremona on sage-release:
<snip>
> Is there a separate ticket for this one?

Not that I know of; it's also in my [first comment above](http://trac.sagemath.org/sage_trac/ticket/9584#comment:1).

Should we split off one of the issues? The doctest failure is likely to get fixed quicker I think.


---

Comment by leif created at 2010-07-24 18:02:09

Just curious: Cicero runs Fedora 12 I think, what version is gcc?


---

Comment by jhpalmieri created at 2010-07-24 18:08:58

All of the skynet machines run gcc 4.5.0.


---

Comment by jhpalmieri created at 2010-07-24 18:09:26

(See [http://wiki.sagemath.org/skynet](http://wiki.sagemath.org/skynet).)


---

Comment by leif created at 2010-07-24 18:13:54

Replying to [comment:15 jhpalmieri]:
> (See [http://wiki.sagemath.org/skynet](http://wiki.sagemath.org/skynet).)
Sorry, missed that... :)


---

Comment by leif created at 2010-07-24 20:11:01

Replying to [comment:12 leif]:
> Replying to [comment:11 jhpalmieri]:
> > On cicero, I get the failure reported by John Cremona on sage-release:
> <snip>
> > Is there a separate ticket for this one?
> 
> Not that I know of; it's also in my [first comment above](http://trac.sagemath.org/sage_trac/ticket/9584#comment:1).
> 
> Should we split off one of the issues? The doctest failure is likely to get fixed quicker I think.

Carl Witty has opened #9593, which doesn't (yet) focus on the doctest error though, but seems to be adequate for fixing the numeric noise which causes it, too.


---

Comment by jhpalmieri created at 2010-07-24 20:15:07

I've set SAGE_TIMEOUT_LONG to 10000, and on both cleo and iras the test is still timing out.  On iras I ran it "verbose", and it stalled at this point:

```
Trying:
    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)
Expecting nothing
```

But that command works fine from the command line, and I'm not flushing any buffers.  Is it worth pursuing this further?  If so, how should I modify ncadoctest to flush buffers appropriately?


---

Attachment

As the name says... Apply to scripts repo.


---

Comment by leif created at 2010-07-24 20:43:44

Replying to [comment:18 jhpalmieri]:
> I've set SAGE_TIMEOUT_LONG to 10000, and on both cleo and iras the test is still timing out.
Wow... ;-) (Single test? Sysload?)

> On iras I ran it "verbose", and it stalled at this point:

```
Trying:
    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)
Expecting nothing
```

> But that command works fine from the command line, and I'm not flushing any buffers.
I don't think this is the point where it really starts hanging.

> Is it worth pursuing this further?  If so, how should I modify ncadoctest to flush buffers appropriately?

IMO yes; I've uploaded a patch to `ncadoctest.py` (which I think could be merged into Sage anyway, since if at all it slows down only doctesting in verbose mode).

Btw, you could look for Python and GAP orphans after the test has timed out. (GAP processes should be the children of the orphaned Python doctest process.)


---

Comment by leif created at 2010-07-24 20:45:20

Changing keywords from "" to "generic_graph, generic graph, time-out, time out".


---

Comment by leif created at 2010-07-24 21:19:56

schilly did *not* get time-outs on 32-bit Ubuntu 8.10 (gcc 4.3.2), with a *64-bit* CPU (Core2 quad) though...


---

Comment by jhpalmieri created at 2010-07-24 21:36:20

I'm only seeing the timeout problem on cleo and iras, both itanium machines.  All of the other skynet linux machines finish doctesting in a sane amount of time.


---

Comment by leif created at 2010-07-24 23:22:40

Replying to [comment:17 leif]:
> Replying to [comment:12 leif]:
> > Replying to [comment:11 jhpalmieri]:
> > > On cicero, I get the failure reported by John Cremona on sage-release:
> > <snip>
> > > Is there a separate ticket for this one?

I've now opened #9594 (as a 4.5.2 blocker) for the failing doctest.

> > Not that I know of; it's also in my [first comment above](http://trac.sagemath.org/sage_trac/ticket/9584#comment:1).
> > 
> > Should we split off one of the issues? The doctest failure is likely to get fixed quicker I think.
> 
> Carl Witty has opened #9593, which doesn't (yet) focus on the doctest error though, but seems to be adequate for fixing the numeric noise which causes it, too.

Carl's ticket is intended to address reproducible spring layout in general, not the current doctest error.


---

Comment by leif created at 2010-07-24 23:31:59

John, did you face the funny doctest error in `sage/graphs/genus.pyx` again?

If so, we should open yet another ticket for that one.


---

Comment by jhpalmieri created at 2010-07-24 23:48:34

Replying to [comment:25 leif]:
> John, did you face the funny doctest error in `sage/graphs/genus.pyx` again?

I'm seeing it now, while iras is also running the doctest on generic_graph.py.  Maybe it only pops up when the system is sufficiently loaded.


---

Comment by jhpalmieri created at 2010-07-25 01:37:04

Here's cleo (verbose doctesting, version of ncadoctest which has been patched with the attached patch):

```
Trying:
    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)
Expecting nothing
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
         [10000.8 s]
```

iras is still going, but I expect it to behave the same way.


---

Comment by leif created at 2010-07-25 01:44:44

Replying to [comment:27 jhpalmieri]:
> Here's cleo (verbose doctesting, version of ncadoctest which has been patched with the attached patch):

```
Trying:
    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)
Expecting nothing
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
         [10000.8 s]
```


I get exactly that far if I run the doctest file _"manually"_ with `./sage -python ~/.sage/tmp/.doctest_generic_graph.py`, without the time-out messages of course. (The file itself looks ok to me.)


---

Comment by leif created at 2010-07-25 01:53:29

I'll leave it running for the moment, and wait if it ever terminates... ;-)

While the GAP process sleeps (waiting for input), the Python process eagerly does _something_, I just wonder what.


---

Comment by jhpalmieri created at 2010-07-25 05:58:28

I applied this patch on cleo and on iras:

```diff
diff -r af5f40a73eda sage/graphs/generic_graph.py
--- a/sage/graphs/generic_graph.py      Wed Jul 21 20:13:55 2010 -0700
+++ b/sage/graphs/generic_graph.py      Sun Jul 25 01:50:04 2010 -0400
`@``@` -3424,14 +3424,6 `@``@`
         By Edmond's theorem, a graph which is `k`-connected always has `k` edge-disjoint
         arborescences, regardless of the root we pick::
 
-            sage: g = digraphs.RandomDirectedGNP(30,.3)
-            sage: k = Integer(g.edge_connectivity())
-            sage: arborescences = g.edge_disjoint_spanning_trees(k)
-            sage: all([a.is_directed_acyclic() for a in arborescences])
-            True
-            sage: all([a.is_connected() for a in arborescences])
-            True            
-
         In the undirected case, we can only ensure half of it::
 
             sage: g = graphs.RandomGNP(30,.3)
```

Afterwards, doctesting finished in under three minutes with one failure:

```
sage -t -long "devel/sage/sage/graphs/generic_graph.py"
**********************************************************************
File "/home/palmieri/iras/sage-4.5.2.alpha0/devel/sage/sage/graphs/generic_graph.py", line 11573:
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
    {0: [1.1721936005708948, -0.85595703323182004], 1: [1.8124415978053314, -0.098957722760544126], 2: [1.3556834715997623, 0.18555735660955996], 3: [1.5071993658897154, 0.64583234825810909], 4: [2.0052086204051096, -0.50880746601197047], 5: [0.59719922887682242, -0.23674243624132649], 6: [2.0421969942849465, 0.68675223944817765], 7: [1.4629031375326151, -0.47198785673207005], 8: [0.90114500185020652, 0.77411663137336129], 9: [2.4857090090237808, -0.11980606071147699]}
**********************************************************************
```

(Exactly the same failure on both machines.)

Completely deleting the doctests is too drastic, I think, but it certainly suggests where the problem lies.


---

Comment by ncohen created at 2010-07-25 07:32:20

Hmmmm.... :-/

Then perhaps setting the number of vertices to 20 instead of 30 ? With CPLEX as a solver, this test is actually much faster, this may be why I originally put a 30 there, which may be too big for GLPK.


```
sage:  T = lambda x: x.edge_disjoint_spanning_trees(x.edge_connectivity())
sage: %timeit T(digraphs.RandomDirectedGNP(30,.3))
5 loops, best of 3: 6.03 s per loop
```



```
sage:  T = lambda x: x.edge_disjoint_spanning_trees(x.edge_connectivity(), solver= "CPLEX")
sage: %timeit T(digraphs.RandomDirectedGNP(30,.3))
5 loops, best of 3: 668 ms per loop
```


In this case, though, we should increase the probability, lest we find non-strongly-connected graphs, but this still takes a lot of time 

```

sage:  T = lambda x: x.edge_disjoint_spanning_trees(x.edge_connectivity())
sage: %timeit T(digraphs.RandomDirectedGNP(20,.5))
5 loops, best of 3: 4.52 s per loop
```


As I still haven't found a way to write #7303, perhaps the following would be a good alternative :

We build a directed circulant graph on n vertices by linking the i th vertex to i+1, i+2, ... , i+k, thus ensuring our graph is k-connected. Then, by Edmond's theorem, we know this graph has `k` edge-disjoint spanning arborescences


```
sage: n = 20
sage: k = 3
sage: g = DiGraph()
sage: g.add_edges( (Integer(i),Integer(Mod(i+j,n))) for i in range(n) for j in range(1,k+1) )
sage: k == g.edge_connectivity()
True
sage: arborescences = g.edge_disjoint_spanning_trees(k)
sage: all([a.is_directed_acyclic() for a in arborescences])
True
sage: all([a.is_connected() for a in arborescences]) 
True
}}} 

It is nicer now :

{{{
sage: %timeit g.edge_disjoint_spanning_trees(k)
5 loops, best of 3: 283 ms per loop
}}}

Plus it is a bit "cleaner" without the random graphs in this case, methinks :-)

Sorry for the trouble !!!!!!!!!!!!!!!!!!

Nathann


---

Comment by leif created at 2010-07-25 07:46:16

Well, I wouldn't mind if it only took very long... It simply _does not terminate_ on some systems, i.e. there must be some bug in the underlying code that only shows up with specific CPU/compiler/OS constellations, but don't ask _me_ which and why. ;-)


---

Comment by ncohen created at 2010-07-25 08:03:47

Oh. Actually, I do not know what Sage is doing during the doctests. The "timeit" method may say it only takes 6 seconds, but if you type the commands I gave you will wait much, much longer to get the answer (and not only 5 times this -- the number of loop). Is it really computer-specific ? There is still the probability that the given graph is not strongly connected, but it should be *veeeeeeeery* low !!!

Nathann


---

Comment by jhpalmieri created at 2010-07-25 14:55:49

Hi Nathann,

> Sorry for the trouble !!!!!!!!!!!!!!!!!!

I cc'ed you on the ticket not because I thought you caused trouble, but because I knew you had worked on the file and could suggest ways to fix it.

So are you suggesting this patch?  It seems to work for me.

```diff
diff -r af5f40a73eda sage/graphs/generic_graph.py
--- a/sage/graphs/generic_graph.py      Wed Jul 21 20:13:55 2010 -0700
+++ b/sage/graphs/generic_graph.py      Sun Jul 25 10:53:22 2010 -0400
`@``@` -3424,13 +3424,17 `@``@`
         By Edmond's theorem, a graph which is `k`-connected always has `k` edge-disjoint
         arborescences, regardless of the root we pick::

-            sage: g = digraphs.RandomDirectedGNP(30,.3)
-            sage: k = Integer(g.edge_connectivity())
+            sage: n = 20
+            sage: k = 3
+            sage: g = DiGraph()
+            sage: g.add_edges( (Integer(i),Integer(Mod(i+j,n))) for i in range(n) for j in range(1
,k+1))
+            sage: k == g.edge_connectivity()
+            True
             sage: arborescences = g.edge_disjoint_spanning_trees(k)
             sage: all([a.is_directed_acyclic() for a in arborescences])
             True
             sage: all([a.is_connected() for a in arborescences])
-            True
+            True

         In the undirected case, we can only ensure half of it::
```



---

Comment by jhpalmieri created at 2010-07-25 15:17:04

With this patch, does the docstring still make sense as a whole?  That is, does the new doctest fit with the ones before and after?


---

Comment by leif created at 2010-07-25 18:49:22

The following works _for me_:

```patch
diff --git a/sage/graphs/generic_graph.py b/sage/graphs/generic_graph.py
--- a/sage/graphs/generic_graph.py
+++ b/sage/graphs/generic_graph.py
`@``@` -3424,7 +3424,7 `@``@`
         By Edmond's theorem, a graph which is `k`-connected always has `k` edge-disjoint
         arborescences, regardless of the root we pick::
 
-            sage: g = digraphs.RandomDirectedGNP(30,.3)
+            sage: g = digraphs.RandomDirectedGNP(28,.3) # reduced from 30, cf. #9584
             sage: k = Integer(g.edge_connectivity())
             sage: arborescences = g.edge_disjoint_spanning_trees(k)
             sage: all([a.is_directed_acyclic() for a in arborescences])
```

So I've simply changed the size of the random graph, not the doctest in principle. Someone should look at the code though, since it seems to run into an infinite loop under some circumstances. (I also tried 20, 25, 27 and 29; the latter again did not terminate; I've not yet tried _larger_ values, which _might_ work as well...)

With the above change (and the patch at #9594), all doctests pass in reasonable time:

```sh
leif`@`californication:~/sage-4.5.2.alpha0-j6$ time ./sage -t devel/sage/sage/graphs/      
sage -t  "devel/sage/sage/graphs/digraph_generators.py"     
	 [13.8 s]
sage -t  "devel/sage/sage/graphs/cliquer.pyx"               
	 [3.5 s]
...
sage -t  "devel/sage/sage/graphs/graph_coloring.py"         
	 [18.4 s]
sage -t  "devel/sage/sage/graphs/bipartite_graph.py"        
	 [7.5 s]
sage -t  "devel/sage/sage/graphs/digraph.py"                
	 [9.8 s]
sage -t  "devel/sage/sage/graphs/chrompoly.pyx"             
	 [13.4 s]
sage -t  "devel/sage/sage/graphs/graph_generators.py"       
	 [87.4 s]
sage -t  "devel/sage/sage/graphs/generic_graph.py"          
	 [72.1 s]
sage -t  "devel/sage/sage/graphs/trees.pyx"                 
	 [10.9 s]
...
sage -t  "devel/sage/sage/graphs/dot2tex_utils.py"          
	 [3.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 383.5 seconds

real	6m23.599s
user	6m2.251s
sys	0m18.253s
leif`@`californication:~/sage-4.5.2.alpha0-j6$ time ./sage -t -long devel/sage/sage/graphs/
sage -t -long "devel/sage/sage/graphs/digraph_generators.py"
	 [22.5 s]
sage -t -long "devel/sage/sage/graphs/cliquer.pyx"          
	 [3.5 s]
...
sage -t -long "devel/sage/sage/graphs/graph_coloring.py"    
	 [18.4 s]
sage -t -long "devel/sage/sage/graphs/bipartite_graph.py"   
	 [7.5 s]
sage -t -long "devel/sage/sage/graphs/digraph.py"           
	 [9.8 s]
sage -t -long "devel/sage/sage/graphs/chrompoly.pyx"        
	 [13.4 s]
sage -t -long "devel/sage/sage/graphs/graph_generators.py"  
	 [228.7 s]
sage -t -long "devel/sage/sage/graphs/generic_graph.py"     
	 [148.5 s]
sage -t -long "devel/sage/sage/graphs/trees.pyx"            
	 [10.8 s]
...
sage -t -long "devel/sage/sage/graphs/genus.pyx"            
	 [49.3 s]
sage -t -long "devel/sage/sage/graphs/graph_database.py"    
	 [3.4 s]
sage -t -long "devel/sage/sage/graphs/dot2tex_utils.py"     
	 [3.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 655.7 seconds

real	10m55.784s
user	10m55.949s
sys	0m19.829s
```

(Pentium 4 Prescott 3.2GHz)

I've also built Sage 4.5.2.alpha0 on an older Pentium 4 (Northwood, 2.66GHz; only 768MB RAM, Ubuntu 7.10 x86 with rebuilt gcc/g++/gfortran 4.2.1, new gmp and mpfr); `make testlong` is still running...


---

Comment by jhpalmieri created at 2010-07-25 19:49:04

Using `g = digraphs.RandomDirectedGNP(28,.3)` works for me too: doctesting generic_graph.py finishes in under 180 seconds on both cleo and iras.  Maybe the problem is indeed that 30 vertices is too many for GLPK, as ncohen suggested.

I'm more or less happy with this patch: it doesn't change the doctests in any qualitative way, so it isn't very intrusive.  The only problem is that we still don't know what the underlying issue is.  CPLEX is not installed on any skynet machine as far as I can tell, so I have no way of testing whether it might work in this case.  So how should we proceed?


---

Comment by leif created at 2010-07-25 22:58:29

Replying to [comment:36 leif]:
> I've also built Sage 4.5.2.alpha0 on an older Pentium 4 (Northwood, 2.66GHz; only 768MB RAM, Ubuntu 7.10 x86 with rebuilt gcc/g++/gfortran 4.2.1, new gmp and mpfr); `make testlong` is still running...

Funny, that machine has just passed `generic_graph.py` in 281 seconds, with only the `get_pos()` graph layout doctest error (#9594). (I'm testing vanilla 4.5.2.alpha0 first.)


---

Comment by leif created at 2010-07-26 20:39:21

Just for the record: I've verified that the random graph is exactly the same on the 32-bit system (where `edge_disjoint_spanning_trees()` does not terminate).


---

Attachment


---

Comment by jhpalmieri created at 2010-07-26 20:58:55

Here's Leif's patch, which I will review positively.


---

Comment by jhpalmieri created at 2010-07-26 20:58:55

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-07-26 20:59:06

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-07-26 21:03:30

Well, this is just an ugly work-around to make the doctest pass, so we should (change the ticket's title and) address the cause on another one...


---

Comment by jhpalmieri created at 2010-07-26 21:34:23

On the one hand, that's true.  On the other, we were only hitting this problem on one or two platforms.  So it might be a bug in some component of Sage (like GLPK?), but it might be something out of our control entirely.  So a work-around seems like an acceptable solution right now.

Have you tried setting the number of vertices higher on other machines, to try to replicate the issue elsewhere?  I just tried with 40 instead of 30 on sage.math, and it worked just fine.  50 vertices took a while, but it finished, too.


---

Comment by leif created at 2010-07-26 22:01:01

Replying to [comment:43 jhpalmieri]:
> On the one hand, that's true.  On the other, we were only hitting this problem on one or two platforms.  So it might be a bug in some component of Sage (like GLPK?), but it might be something out of our control entirely.

Nothing is out of my control... ;-)

I mean we should try to find the reason. If it's outside of Sage, fine, and we can at least document it, whether it lies in GLPK or some OS/compiler specifics.

And the "failing" doctest, i.e. the behavior after timing out, in addition shows (again) that something's wrong with the doctesting framework, to also be addressed on another ticket.

> So a work-around seems like an acceptable solution right now.

I'm ok with merging this work-around at this moment.

 
> Have you tried setting the number of vertices higher on other machines, to try to replicate the issue elsewhere?  I just tried with 40 instead of 30 on sage.math, and it worked just fine.  50 vertices took a while, but it finished, too.

Not yet, currently trying to track this issue (with 30 vertices) further down.

Please cc me if anyone opens a follow-up.


---

Comment by ddrake created at 2010-07-27 00:42:21

Resolution: fixed


---

Comment by ddrake created at 2010-07-27 00:42:21

Merged trac_9584-generic_graph.patch in 4.5.2.alpha1.


---

Comment by ncohen created at 2010-07-27 00:49:14

Oh, by the way : when you are trying to work on long linear programs like this one, you may find useful too add "verbosity = 2" or higher to the edge_disjoint_spanning_trees method. It will give you some idea of what GLPK is doing :-)

Nathann


---

Comment by leif created at 2010-07-27 00:53:26

Replying to [comment:46 ncohen]:
> Oh, by the way : when you are trying to work on long linear programs like this one, you may find useful too add "verbosity = 2" or higher to the edge_disjoint_spanning_trees method. It will give you some idea of what GLPK is doing :-)

LOL, I'm currently hacking it, with `log=3`... (and trying to write out MPS files to test on the other machine, but two of them seem to be invalid?!)


---

Comment by leif created at 2010-07-27 00:54:13

Nathann, do you open a new ticket?


---

Comment by ncohen created at 2010-07-27 00:57:01

> Nathann, do you open a new ticket?
Well, I've never been able to produce this error on my computer actually ... :-/

This being said, if Sage is exporting invalid linear programs, that's a very bad news, as it does it using GLPK. So if the problem stored in the file is invalid, then the problem solved by GLPK should be too, as they behave the same way : to solve it, Sage first feeds it to GLPK using method A, then calls "solve". To export it, Sage first feeds it to GLPK using method A, then calls the export method from GLPK.

So if the files are invalid, that's a very bad news indeed !!

Nathann


---

Comment by leif created at 2010-07-27 03:09:43

Replying to [comment:49 ncohen]:
> [...] if Sage is exporting invalid linear programs, that's a very bad news, as it does it using GLPK. So if the problem stored in the file is invalid, then the problem solved by GLPK should be too, as they behave the same way [...]

Well, Sage does not run `glpsol` on a generated file, but uses the library interface, so there's a slight difference, and: names are only set when calling `write_mps()` or `write_lp()` - which goes wrong somehow in at least two cases. (I'm calling both `p.write_mps()` and `p.write_lp()` right before `p.solve()` in `GenericGraph.edge_disjoint_spanning_trees()`, and afterwards run `glpsol (--freemps|--lp)` on those files.)


```
$ local/bin/glpsol --freemps ../trac_9584-edge_disjoint_spanning_trees-5.mps
GLPSOL: GLPK LP/MIP Solver, v4.44
Parameter(s) specified in the command line:
 --freemps ../trac_9584-edge_disjoint_spanning_trees-5.mps
Reading problem data from `../trac_9584-edge_disjoint_spanning_trees-5.mps'...
../trac_9584-edge_disjoint_spanning_trees-5.mps:8: warning: missing model name in field 3
Objective: R0000000
../trac_9584-edge_disjoint_spanning_trees-5.mps:1735: duplicate coefficient in row `R0000001'
MPS file processing error
$ local/bin/glpsol --lp ../trac_9584-edge_disjoint_spanning_trees-5.lp
GLPSOL: GLPK LP/MIP Solver, v4.44
Parameter(s) specified in the command line:
 --lp ../trac_9584-edge_disjoint_spanning_trees-5.lp
Reading problem data from `../trac_9584-edge_disjoint_spanning_trees-5.lp'...
../trac_9584-edge_disjoint_spanning_trees-5.lp:7: multiple use of variable `V0(None)((0,_1))' not allowed
CPLEX LP file processing error
```



> So if the files are invalid, that's a very bad news indeed !!

Indeed, though the GLPK _library_ works on th 64-bit system. On the 32-bit system where the doctest did not terminate, it's actually the solver that runs "forever" (trying to find a solution) - I do not yet know why... :(


---

Comment by jhpalmieri created at 2010-07-27 03:52:49

If I run the doctest on iras with "sage -t -verbose" and with the argument "log=3", I get this:

```

Trying:
    arborescences = g.edge_disjoint_spanning_trees(k, log=Integer(3))###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k, log=3)
Expecting nothing
GLPK Integer Optimizer, v4.44
1719 rows, 3650 columns, 10040 non-zeros
1370 integer variables, all of which are binary
Preprocessing...
1670 rows, 3605 columns, 9790 non-zeros
1325 integer variables, all of which are binary
Scaling...
 A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00
Problem data seem to be well scaled
Constructing initial basis...
Size of triangular part = 1670
Solving LP relaxation...
GLPK Simplex Optimizer, v4.44
1670 rows, 3605 columns, 9790 non-zeros
      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)
   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)
*  1589: obj =   0.000000000e+00  infeas =  0.000e+00 (0)
OPTIMAL SOLUTION FOUND
Integer optimization begins...
+  1589: mip =     not found yet <=              +inf        (1; 0)
+  3341: mip =     not found yet <=   0.000000000e+00        (12; 0)
+  4583: mip =     not found yet <=   0.000000000e+00        (25; 0)
+  5915: mip =     not found yet <=   0.000000000e+00        (39; 0)
+  7295: mip =     not found yet <=   0.000000000e+00        (53; 0)
+  9064: mip =     not found yet <=   0.000000000e+00        (68; 0)
+ 10470: mip =     not found yet <=   0.000000000e+00        (86; 0)
+ 12453: mip =     not found yet <=   0.000000000e+00        (104; 0)
+ 15172: mip =     not found yet <=   0.000000000e+00        (122; 0)
+ 19359: mip =     not found yet <=   0.000000000e+00        (143; 1)
+ 25674: mip =     not found yet <=   0.000000000e+00        (147; 19)
+ 30995: mip =     not found yet <=   0.000000000e+00        (156; 40)
Time used: 60.0 secs.  Memory used: 4.5 Mb.
+ 36038: mip =     not found yet <=   0.000000000e+00        (178; 73)
+ 41514: mip =     not found yet <=   0.000000000e+00        (188; 126)
+ 45778: mip =     not found yet <=   0.000000000e+00        (213; 179)
+ 51616: mip =     not found yet <=   0.000000000e+00        (232; 244)
+ 56429: mip =     not found yet <=   0.000000000e+00        (215; 395)
+ 61588: mip =     not found yet <=   0.000000000e+00        (220; 483)
+ 66918: mip =     not found yet <=   0.000000000e+00        (219; 610)
+ 71927: mip =     not found yet <=   0.000000000e+00        (225; 691)
+ 77942: mip =     not found yet <=   0.000000000e+00        (218; 802)
+ 82716: mip =     not found yet <=   0.000000000e+00        (219; 910)
+ 87340: mip =     not found yet <=   0.000000000e+00        (216; 1034)
+ 92302: mip =     not found yet <=   0.000000000e+00        (215; 1149)
Time used: 120.0 secs.  Memory used: 5.1 Mb.
+ 98199: mip =     not found yet <=   0.000000000e+00        (216; 1267)
+103543: mip =     not found yet <=   0.000000000e+00        (209; 1380)
+109695: mip =     not found yet <=   0.000000000e+00        (205; 1475)
+115375: mip =     not found yet <=   0.000000000e+00        (194; 1626)
+120734: mip =     not found yet <=   0.000000000e+00        (191; 1775)
+126850: mip =     not found yet <=   0.000000000e+00        (192; 1890)
+132308: mip =     not found yet <=   0.000000000e+00        (195; 1994)
+137437: mip =     not found yet <=   0.000000000e+00        (200; 2119)
+142222: mip =     not found yet <=   0.000000000e+00        (185; 2285)
+147918: mip =     not found yet <=   0.000000000e+00        (194; 2358)
+152167: mip =     not found yet <=   0.000000000e+00        (211; 2444)
+157139: mip =     not found yet <=   0.000000000e+00        (188; 2631)
Time used: 180.0 secs.  Memory used: 5.2 Mb.
+162974: mip =     not found yet <=   0.000000000e+00        (194; 2717)
+167746: mip =     not found yet <=   0.000000000e+00        (185; 2875)
+173860: mip =     not found yet <=   0.000000000e+00        (189; 2945)
+179993: mip =     not found yet <=   0.000000000e+00        (185; 3036)
+184852: mip =     not found yet <=   0.000000000e+00        (186; 3167)
+190815: mip =     not found yet <=   0.000000000e+00        (184; 3260)
+195443: mip =     not found yet <=   0.000000000e+00        (191; 3340)
+200019: mip =     not found yet <=   0.000000000e+00        (199; 3441)
+205299: mip =     not found yet <=   0.000000000e+00        (193; 3550)
+211558: mip =     not found yet <=   0.000000000e+00        (190; 3643)
+217128: mip =     not found yet <=   0.000000000e+00        (205; 3721)
+222749: mip =     not found yet <=   0.000000000e+00        (193; 3851)
Time used: 240.1 secs.  Memory used: 5.2 Mb.
+228284: mip =     not found yet <=   0.000000000e+00        (192; 3966)
+234369: mip =     not found yet <=   0.000000000e+00        (187; 4068)
+239753: mip =     not found yet <=   0.000000000e+00        (186; 4177)
+245044: mip =     not found yet <=   0.000000000e+00        (203; 4260)
+251418: mip =     not found yet <=   0.000000000e+00        (191; 4393)
+257305: mip =     not found yet <=   0.000000000e+00        (184; 4511)
+262969: mip =     not found yet <=   0.000000000e+00        (192; 4590)
+268135: mip =     not found yet <=   0.000000000e+00        (187; 4714)
+274100: mip =     not found yet <=   0.000000000e+00        (192; 4792)
+279175: mip =     not found yet <=   0.000000000e+00        (185; 4929)
+285635: mip =     not found yet <=   0.000000000e+00        (177; 5033)
+291442: mip =     not found yet <=   0.000000000e+00        (189; 5090)
Time used: 300.1 secs.  Memory used: 5.2 Mb.
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
```

Increasing the timeout threshold just lets this continue longer.


---

Comment by leif created at 2010-07-27 04:08:46

Replying to [comment:51 jhpalmieri]:
> Increasing the timeout threshold just lets this continue longer.

I'm at 9500s+ and it keeps writing to the screen, though `sage -t ...` has already terminated... :D


---

Comment by ncohen created at 2010-07-27 08:27:11

Well, it is not a surprise that such LP can run for a long time... Right now, a LP has been running on one of our lab's machine (Something like 8 CPU, some fearful amount of RAM) for more that 2 days straight. And there is some hope it will finish ! That's one of the things I accept coming from LP. Sometimes, they are too slow ;-)

Nathann


---

Comment by leif created at 2010-07-27 16:05:26

Replying to [comment:53 ncohen]:
> Well, it is not a surprise that such LP can run for a long time...

As mentioned above, the whole test (`-long`) of `generic_graph.py` - with _in theory_ *the same* LP program (30 vertices) - took 281 seconds on a much slower machine.

I still don't know if the GLPK library or the Sage interface/code that builds the LP program structure is broken on the other (very similar, btw) machine.

(I've killed the Python process running the solver after 42138+ seconds, which was still searching for a solution.)

Nathann, could you take a look at the variable name generation which causes the MPS and LP file errors? (These should be reproducible on all systems I think, at least I've met them on a 64-bit system, running Ubuntu 9.04.)


---

Comment by ncohen created at 2010-07-28 03:10:01

The corresponding ticket is #9617 . Thank you for finding this one ! :-)

Nathann


---

Comment by jdemeyer created at 2010-12-05 14:43:16

The error in the ticket (negative `get_memory_usage()`) still occurs today on the Skynet machine iras with sage-4.6.1.alpha3.


---

Comment by mpatel created at 2010-12-05 14:57:54

Replying to [comment:56 jdemeyer]:
> The error in the ticket (negative `get_memory_usage()`) still occurs today on the Skynet machine iras with sage-4.6.1.alpha3.

Please see #9863 for this problem.
