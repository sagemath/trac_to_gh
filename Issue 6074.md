# Issue 6074: Planar graph generation

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-05-18 19:06:13

Assignee: rlm

CC:  ncohen mvngu slelievre

Essentially, this shouldn't be too difficult to implement in Sage:

http://cs.anu.edu.au/~bdm/papers/plantri-full.pdf

The basic steps to generate plane graphs (graphs embedded in the plane) of minimum degree at least `d`, connectivity at least `k`, number of edges at least `e`, and max face size at most `p`, are:

1. Implement section 1.3 of the above paper. This allows for a much faster implementation of automorphism group and isomorphism in the case of plane graphs.

2. Generate all planar triangluations, with min degree at least `max(d,3)`, connectivity at least `max(k,3)`. This is described in section 1.2, mainly the third paragraph. Essentially, you start with K_4, and you augment by one of the three moves E_3, E_4, or E_5. The "backwards" step in canonical augmentation here is to first try to remove the least-labeled vertex of degree 3, i.e. try to undo E_3 if possible, or degree 4 if that is possible, i.e. try to undo E_4 if possible, then finally checking for degree 5.

3. Use these, together with edge deletion and canonical augmentation, to generate all plane graphs.


---

Comment by mvngu created at 2009-05-19 02:08:59

Add myself since I'm interested in (implementing the ideas of) this ticket.


---

Comment by ncohen created at 2009-07-04 09:11:11

Related subject, recently published : Uniform random sampling of planar graphs in linear time 

The paper and a Java implementation are available on :
http://algo.inria.fr/fusy/


---

Comment by chapoton created at 2014-11-14 13:09:25

Now partially available via plantri spkg : #16970


---

Comment by slelievre created at 2018-06-27 07:57:31

Changing keywords from "" to "planar graph, triangulation".


---

Comment by slelievre created at 2018-06-27 07:57:31

Replying to [comment:2 ncohen]:
> Related subject, recently published : Uniform random sampling of planar graphs in linear time 
> 
> The paper and a Java implementation are available on :
> http://algo.inria.fr/fusy/

For future reference, Eric Fusy's page is now at:
http://www.lix.polytechnique.fr/Labo/Eric.Fusy/

Excerpt of that page about that paper and Java implementation:

> **Uniform random sampling of planar graphs in linear time.**
>
> Random Structures and Algorithms 35(4): 464-522 (2009).
> [pdf](http://www.lix.polytechnique.fr/Labo/Eric.Fusy/Articles/Fusy08_planar_graphs.pdf)
>
> Short version, under the title "Quadratic exact-size and linear approximate-size random generation of planar graphs": Proceedings of the AofA'05 Conference (Analysis of Algorithms-2005), published in Discrete Mathematics and Theoretical Computer Science (DMTCS) Proceedings, vol AD, pp. 125-138 (2005).
> [pdf](http://www.lix.polytechnique.fr/Labo/Eric.Fusy/Articles/FusyAofa.pdf)
>
> Implementation (in java) [tar.gz](http://www.lix.polytechnique.fr/Labo/Eric.Fusy/Programs/BoltzmannPlanarGraphs.tar.gz)

Regarding plantri, one can now install it as an optional package by running the following in a terminal

```
sage -i plantri
```

(not sure if one needs to then run `make` from the directory where Sage is installed).
