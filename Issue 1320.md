# Issue 1320: [graphs] planarity testing

Issue created by migration from https://trac.sagemath.org/ticket/1320

Original creator: jason

Original creation time: 2007-11-28 20:08:11

Assignee: mhansen

CC:  bober

Keywords: graphs

From Chris Godsil's wishlist.


```
>>> Someone is eventually going to ask for a routine to test for planarity. I
>>> believe that there are good ones in existence, but it's going to be
>>> hard to get
>>> a good one with an open source licence.
>> The nauty README has this to say about the new planarity testing feature:
>> "New program planarg to test for planarity and find planar embeddings:
>> planarg -help for details. The planarity code was written by Paulette
>> Lieby for the Magma project and used with permission."
>>
>> Does anyone know Paulette Lieby? Can we ask about releasing the code
>> under GPL? It looks like the source has now been released as a part of
>> nauty.
> Emily Kirkman understands a linear time algorithm for testing for
> planarity. There is one in BOOST, which is GPL, and has been nominated
> for inclusion in Sage several times.
```




---

Comment by ekirkman created at 2007-11-30 03:56:03

I plan to begin implementing the Boyer-Myrvold linear time planar test/embedding algorithm right after autumn quarter finals.  (Dec 13th).  It should be available in early January.


---

Comment by ekirkman created at 2007-11-30 03:56:03

Changing assignee from mhansen to ekirkman.


---

Comment by rlm created at 2007-12-17 15:22:30

Changing keywords from "graphs" to "".


---

Comment by rlm created at 2007-12-17 15:22:30

Changing component from combinatorics to graph theory.


---

Attachment


---

Comment by mabshoff created at 2008-02-28 06:03:58

Hi, I had a single, easy to fix merge conflict:

```
<<<<<<< /scratch/mabshoff/release-cycle/sage-2.10.3.rc0/devel/sage-main/sage/graphs/graph.py.orig.1734827483
from sage.graphs.graph_coloring import chromatic_number, chromatic_polynomial
=======
from sage.rings.rational import Rational
```

The above was caused by the work on the chromatic number and chromatic polynomial by Tom.
||||||| /tmp/graph.py~base.vsk2R5
Cheers,

Michael


---

Comment by mabshoff created at 2008-02-28 06:08:32

Merged in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-28 06:08:32

Resolution: fixed
