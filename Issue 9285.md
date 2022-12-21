# Issue 9285: Challenge: iterating through E8 in 5 minutes

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-06-20 21:05:43

Assignee: sage-combinat

CC:  sage-combinat

Keywords: Coxeter groups, Chevie

The current code for iterating trough all elements of a Coxeter group is currently ridiculously slow. For E8, it should take no more than a couple minutes, as Franck Lubeck's reported was possible in GAP.

There are several routes to this end, which all deserve to be explored:

 * Using GAP's code; this will require at least fixing a `select` issue in GAP's interface (TODO: add ticket), if not using libGAP

 * Optimizing the underlying CombinatorialFreeModule's code

 * Optimizing the generic Coxeter group code

 * Using properly Coxeter 3


---

Comment by bransingh created at 2015-09-05 04:57:13

Instead of taking the nomenclature ["E",8], if we take  Cartan matrix of E8 manually
cm= CartanMatrix([
 [2,-1,0,0,0,0,0,0],
 [-1,2,-1,0,0,0,0,0],
 [0,-1,2,-1,0,0,0,0],
 [0,0,-1,2,-1,0,0,0],
 [0,0,0,-1,2,-1,0,-1],
 [0,0,0,0,-1,2,-1,0],
 [0,0,0,0,0,-1,2,0],
 [0,0,0,0,-1,0,0,2]],cartan_type_check = False);cm
R=RootSystem(cm).root_lattice()
alpha = R.simple_roots();alpha
W = R.weyl_group(prefix="s")
for w in W:
 w.action(alpha[2]) ==alpha[4] :
  print w
then we are able to act weyl group action on any element with a reasonable time.
Although it is taking more time. it is not showing now error insufficient memory).


---

Comment by tscrim created at 2016-01-03 10:10:21

On my Asus with i7 quad-core (hyperthreaded to 8) and 8GB RAM and #19821 (and doing other things), I get the following running serially (on 1 thread):

```
sage: W = CoxeterGroup(['E',6], base_ring=ZZ)
sage: %time for x in W: pass
CPU times: user 11.2 s, sys: 32 ms, total: 11.2 s
Wall time: 11.2 s

sage: W = CoxeterGroup(['E',7], base_ring=ZZ)
sage: %time for x in W: pass
CPU times: user 5min 47s, sys: 14.4 ms, total: 5min 47s
Wall time: 5min 46s
```

Since E<sub>8</sub> is 240 times larger than E<sub>7</sub>, I expect it to take roughly 240 times longer (although from E<sub>6</sub> to E<sub>7</sub>, it only took 31x longer whereas there is a 56x size difference). That is roughly 23 hours... (in reality, it is probably a lot less, but still on the order of hours).


---

Comment by tscrim created at 2016-01-03 11:33:53

With the recent changes to #19821, I now get:

```
sage: sage: W = CoxeterGroup(['E',6], base_ring=ZZ)
sage: sage: %time for x in W: pass
CPU times: user 4.28 s, sys: 36.1 ms, total: 4.31 s
Wall time: 4.23 s

sage: sage: W = CoxeterGroup(['E',7], base_ring=ZZ)
sage: %time for x in W: pass
CPU times: user 4min 28s, sys: 20 ms, total: 4min 28s
Wall time: 4min 28s
```



---

Comment by tscrim created at 2016-04-10 13:06:54

With #11187, on my laptop (see comment:4) I get

```
sage: W = ReflectionGroup(['E',8])
sage: %time for x in W.iteration('depth', False): pas
CPU times: user 8min 44s, sys: 38.2 ms, total: 8min 44s
Wall time: 8min 43s
```

There are a number of changes from #11187 (the cythonization) that could be lifted up to be used for the general Coxeter group iteration.


---

Comment by tscrim created at 2016-04-10 18:56:09

With Gap3 in Sage, it took 6m20s to go through E<sub>8</sub> on my laptop (serially, comment:4):

```
gap> i:=0;;
gap> W:=CoxeterGroup("E",7);;
gap> ForEachElement(W,function(x)i:=i+1;end);
```

