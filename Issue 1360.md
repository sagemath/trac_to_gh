# Issue 1360: Investigate long time graph_isom case

Issue created by migration from https://trac.sagemath.org/ticket/1360

Original creator: rlm

Original creation time: 2007-12-02 04:21:06

Assignee: mhansen

The full discussion is here.

http://groups.google.com/group/sage-support/browse_thread/thread/4c615950a190e3f3



---

Comment by rlm created at 2007-12-02 04:36:17

Changing status from new to assigned.


---

Comment by rlm created at 2007-12-02 04:36:17

Changing keywords from "" to "graph isomorphism".


---

Comment by rlm created at 2007-12-02 04:36:17

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2007-12-17 15:09:57

Changing component from combinatorics to graph theory.


---

Comment by rlm created at 2007-12-17 15:09:57

Changing keywords from "graph isomorphism" to "isomorphism, canonical labeling".


---

Comment by rlm created at 2008-02-18 21:01:35

After all of the patches that lead to the fix in #1961, this case no longer takes any real time. Once #1961 is merged, this ticket should also be closed!


---

Comment by rlm created at 2008-02-18 21:01:58

In fact:

```
sage: time GAut = G.automorphism_group(partition=Pi)
CPU times: user 0.10 s, sys: 0.04 s, total: 0.14 s
Wall time: 0.15
```



---

Comment by mabshoff created at 2008-02-19 22:25:00

Resolution: fixed


---

Comment by mabshoff created at 2008-02-19 22:25:00

I ran the computation with #1961 applied and rlm confirms that the result is as expected:

```
sage: GAut = G.automorphism_group(partition=Pi)
sage: GAut
Permutation Group with generators [(1,6)(9,14)(18,28)(19,29)(34,44)(35,45)(50,60)(51,61)(66,76)(67,77), 
(6,7)(8,9)(28,30)(29,31)(32,34)(33,35)(60,62)(61,63)(64,66)(65,67), 
(5,8)(7,10)(26,32)(27,33)(30,36)(31,37)(58,64)(59,65)(62,68)(63,69), (4,5)(10,11)(24,26)(25,27)(36,38)(37,39)(56,58)(57,59)(68,70)(69,71), 
(3,4)(11,12)(22,24)(23,25)(38,40)(39,41)(54,56)(55,57)(70,72)(71,73),
(2,3)(12,13)(20,22)(21,23)(40,42)(41,43)(52,54)(53,55)(72,74)(73,75)]
```


Cheers,

Michael
