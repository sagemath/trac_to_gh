# Issue 5793: [with patch, needs review] New algorithm for Max Clique in Graph class using Cython

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-04-16 01:00:04

Assignee: rlm

CC:  rlm

After the discussion that has followed the following patch :
http://trac.sagemath.org/sage_trac/ticket/5669

I began to re-write the same functions using Cython. There is now no need of a spkg package, and I hope it will be faster this way (and prettier) ;-)


---

Comment by mabshoff created at 2009-04-16 05:47:05

Hi,

the patch as is will not go into Sage since you are putting the sources for cliquer-1.2 into the Sage library tree where they do not belong. 

I have not looked at the cython interface, but my guess would be that we need to change cliquer-1.2 to create a library. Please split the cython interface work (the code you wrote minus the cliquer-1.2 source code) and the cliquer-1.2.spkg work. The Cython code should remain here while spkg should go to #5669.

Cheers,

Michael


---

Comment by ncohen created at 2009-06-18 13:07:41

A new patch using the SPKG you can find at :
http://trac.sagemath.org/sage_trac/ticket/6355


---

Comment by rlm created at 2009-06-22 22:35:04

Resolution: duplicate


---

Comment by rlm created at 2009-06-22 22:35:04

Duplication of #6355.


---

Comment by jason created at 2009-07-01 05:40:44

To get this going again, here are some specific suggestions for patch 12427.patch and the associated spkg:

  * copy the header files to somewhere in $SAGE_LOCAL/include (maybe $SAGE_LOCAL/include/cliquer/*.h

  * Make a cliquer.pxd file that declares the necessary functions and structs from the header files.  Make sure that you are only doing cdef externs from the header files, not the .c files like the patch is currently doing.  Don't include the path; just do  `cdef extern from "cliquer/graph.h":` since the header is in the include path.  This cliquer.pxd file can go into sage/graphs.

  * Make a cliquer.pyx in sage/graphs that contains the definitions of max_clique, all_max_clique, and clique_number.  Document and add doctests to these functions.

  * Delete the lines

```
from sage.graphs.graph import Graph 
#from distutils.core import setup 
#from distutils.extension import Extension 
from Cython.Distutils import build_ext 
```


  * In module_list.py, add a `libraries = ['cliquer']` option (see the surrounding declarations for examples of this).

  * Compile the cliquer sources into a shared library, named libcliquer.so, using the instructions in the HowTo William posted.  Place this shared library into $SAGE_LOCAL/lib.

  * In the graphs.py, I don't think you need to do `from sage.graphs.cliquer import clique_number`.  Since the module will be in that directory, I think it would be sufficient to do `from cliquer import clique_number`.


---

Comment by jason created at 2009-07-01 05:45:26

Changing status from closed to reopened.


---

Comment by jason created at 2009-07-01 05:45:26

rlm: this ticket has what looks like the most current patch, whereas #6355 does not have a patch.  I'm reopening this ticket so that the "active" patch is not closed (but I am not opposed to moving this patch to #6355 to consolidate things!).  I feel a bit silly commenting on a patch here when the ticket is closed, but the patch clearly has not been moved/merged/etc.


---

Comment by jason created at 2009-07-01 05:45:26

Resolution changed from duplicate to 


---

Comment by jason created at 2009-07-01 05:50:44

Suggestions 1 and 6 in my comment above apply to the spkg, not the patch.


---

Comment by robertwb created at 2009-07-01 06:01:41

Whence the "../../../../local/lib/cliquer-1.2/cliquer.h" if there's no spkg. Also, I belive local/include is in the include path, so no need to have this long path. (And include files belong in local/include, not local/lib.) I would probably drop the 1.2 suffix so we don't have to update the link paths every time the version gets bumped.


---

Comment by jason created at 2009-07-01 06:47:44

that's what I meant by point 2 (just do `cdef extern from "cliquer/graph.h"`) and point 1 (put the headers in $SAGE_LOCAL/include/cliquer/*.h)


---

Comment by ncohen created at 2009-07-07 13:14:48

Here is a new patch ( number 12428 ) using a shared library !!! I hope you will appreciate it as it took me some time to figure out the inner behavior of Sage ;-)

The new spkg is available on http://trac.sagemath.org/sage_trac/ticket/6355

Nathann


---

Comment by ncohen created at 2009-07-17 19:01:59

My version is working, but I am a bit lost with all the patches... How can I produce a patch containing all the modifications I made since the begining ( since I cloned the original branch, actually ) ?

Thanks !!!


---

Comment by rlm created at 2009-07-17 19:05:30

One option is to clone the branch using `hg_sage.clone`, but to give it the revision number corresponding to the last patch not part of your changes (the base). Then you can copy the affected files over, and it is as if you have done all the work, but you have not checked anything in.


---

Comment by ncohen created at 2009-07-17 19:26:05

New patch "cliquer.patch" containing all the modifications for cliquer since the beginning. And with the good directory's name ;-)


---

Attachment

Cliquer, from the beginning to the end, with the good directory's name !


---

Comment by rlm created at 2009-07-18 17:48:51

Nathann,

I have deleted the previous patches to avoid confusion.

When addressing the following issues, please post another patch to be applied on top of the first (this makes review easier).

1. `algorithm=='networkx'` is never tested, and if it were, it would fail, due to the `cliques` parameter

2. Why are you using `cliquer.pxi` instead of `cliquer.pxd`? If it were `pxd` instead, then other Cython files could `cimport` the same data types.

3. It should go:

```
if algorithm=='networkx':
    ...
elif algorithm=='cliquer':
    ...
else:
    raise NotImplementedError("Only 'networkx' and 'cliquer' are supported.")
```

Also you need to change one instance of `'Cliquer'` to `'cliquer'`.

4. In maximum_cliques, "vertex set" should be "vertex sets"


---

Comment by ncohen created at 2009-07-19 19:24:59

I hope all is fixed now... Though I just renamed cliquer.pxi to cliquer.pxd without really understanding the difference ^^;

By the way, I am not really sure this possibility to change the algorithm used to compute the cliquer number is that useful... Just take a look at this :

sage: g=graphs.RandomGNP(100,.5)
sage: time g.clique_number(algorithm="networkx")
CPU times: user 2.49 s, sys: 0.00 s, total: 2.49 s
Wall time: 2.49 s
9
sage: time g.clique_number()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
9
sage: g=graphs.RandomGNP(150,.5)
sage: time g.clique_number(algorithm="networkx")
CPU times: user 18.45 s, sys: 0.04 s, total: 18.49 s
Wall time: 18.49 s
10
sage: time g.clique_number()
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03 s
10
sage: g=graphs.RandomGNP(200,.5)
sage: time g.clique_number(algorithm="networkx")
CPU times: user 82.33 s, sys: 0.18 s, total: 82.52 s
Wall time: 82.54 s
11
sage: time g.clique_number()
CPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s
Wall time: 0.07 s
11

Anyway, from the practical point of view, it works now ;-)

Nathann


---

Comment by ncohen created at 2009-07-19 19:28:42

Second patch


---

Attachment


---

Comment by rlm created at 2009-07-20 15:17:59

Replying to [comment:15 ncohen]:
> By the way, I am not really sure this possibility to change the algorithm used to compute the cliquer number is that useful...

There are plenty of reasons to have two different implementations, and one I can think of right off the top of my head is to compare results for correctness.

1. You have removed the input "cliques," which is used by NetworkX. You need to put this back in, and mention that it is ignored unless the algorithm is "networkx."

2. The `include '../ext/cliquer.pxd'` line at the beginning of cliquer.pyx is not necessary. "include" is a plain text include, and `pxd` files are forward declarations, which get automatically included by Cython as long as the other part of the filename is the same.

3. One thing I should have mentioned last round: the three functions introduced in cliquer.pyx need to be documented, including some nontrivial doctests.

After all this is done, we should be very close to finished!


---

Comment by ncohen created at 2009-07-20 18:04:29

Hmmmmmm.... There is a perhaps-not-so-small problem :

G = Graph({0:[1,2,3], 1:[2], 3:[0,1]})
G.maximum_clique()
2

When it is obviously 3...

What do we do in this situation ? ^^;


---

Comment by rlm created at 2009-07-20 18:20:55

Replying to [comment:18 ncohen]:
> What do we do in this situation ? ^^;

We debug! I'm looking into this now, but I'm not sure what I'll be able to find out...

4. Another thing is that `cliquer.pxd` needs to be in the same directory as `cliquer.pyx`.


---

Comment by ncohen created at 2009-07-20 18:23:02

it does not come from cliquer itself, which is a relief. I ran cliquer on the command lineand on this file :
p edges 4 5
e 1 2
e 1 3
e 1 4
e 2 3
e 2 4

~/cliquer-1.2$ ./cl example 
Reading graph from example...OK
Searching for a single maximum weight clique...
  2/4 (max  2)  0.00 s  (0.00 s/round)
  3/4 (max  3)  0.00 s  (0.00 s/round)
  4/4 (max  3)  0.00 s  (0.00 s/round)
size=3, weight=3:   1 2 4
~/cliquer-1.2$


---

Comment by ncohen created at 2009-07-20 18:26:22

It works when I replace : 

buf=' e %d %d' %(u,v)

by

buf=' e %d %d' %(u+1,v+1)

in cliquer.pyx. I thought it may come from the difference between 0....n-1 and 1...n and it seems correct. I am running other tests with NetworkX to check.


---

Attachment

DO NOT APPLY!


---

Comment by rlm created at 2009-07-20 18:28:21

It seems as if Cliquer is subtracting one from each vertex in the input, and so the input needs to have one added to it. To see this, apply `trac_5793_debug_only.patch`, and you get:


```
sage: G = Graph({0:[1,2,3], 1:[2], 3:[0,1]}); G.maximum_clique()
(0, 1, None)
 e 0 1
Unweighted graph has 4 vertices, 0 edges (density 0.00).
 0 ->
 1 ->
 2 ->
 3 ->
(0, 2, None)
 e 0 2
Unweighted graph has 4 vertices, 0 edges (density 0.00).
 0 ->
 1 ->
 2 ->
 3 ->
(0, 3, None)
 e 0 3
Unweighted graph has 4 vertices, 0 edges (density 0.00).
 0 ->
 1 ->
 2 ->
 3 ->
(1, 2, None)
 e 1 2
Unweighted graph has 4 vertices, 1 edges (density 0.17).
 0 -> 1
 1 -> 0
 2 ->
 3 ->
(1, 3, None)
 e 1 3
Unweighted graph has 4 vertices, 2 edges (density 0.33).
 0 -> 1 2
 1 -> 0
 2 -> 0
 3 ->
[0, 2]
```


You should probably also expose at least this `print_graph` function in the official versions.


---

Comment by rlm created at 2009-07-20 18:29:13

Oops, looks like we were duplicating effort! But I'll be online for a while, so this might get positively reviewed today!


---

Comment by ncohen created at 2009-07-20 18:39:17

New patch !!


---

Attachment


---

Comment by rlm created at 2009-07-20 18:56:41

OK, I have a few more requests:

1. I think you should expose Cliquer's `graph_print` function in `cliquer.pxd`, so other people see it when they try to play around with the interface.

2. In general, doctests should be indented, so e.g.

```
EXAMPLES:: 

sage: C=graphs.PetersenGraph() 
sage: max_clique(C) 
[7, 9] 
""" 
```

should be

```
EXAMPLES:: 

    sage: C=graphs.PetersenGraph() 
    sage: max_clique(C) 
    [7, 9] 

""" 
```


3. In fact, you should probably check out

http://www.sagemath.org/doc/developer/conventions.html

For example, the following belongs in an `INPUT:` block, and would look much more professional there:


```
The parameter 'cliques' is an optional list of cliques that can be input if already computed. 
ONLY USED BY NetworkX !!!
```


4. There are several functions in `graph.py` which compute with cliques, which haven't been exposed to this new interface. For example, `G.cliques()`. It would be nice to take care of those functions now too, so people don't unnecessarily complain about these functions being slow later. They are all in the same part of the file, which starts with `### Cliques`.


---

Comment by rlm created at 2009-07-20 19:21:04

5. There is one other thing to be aware of. You are assuming that the vertex set is *always* {0,...,n-1}. In fact, this will cause some trouble:

```
sage: C = graphs.CubeGraph(4)
sage: C.maximum_clique()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: cannot concatenate 'str' and 'int' objects
sage: C.vertices()[0]
'0000'
```


Here is the idea to get around this, since this problem has come up many times before:

```
sage: C = graphs.CubeGraph(4)
sage: G,d = C.relabel(inplace=False, return_map=True)
sage: d_inv = {}
sage: for v in d:
....:     d_inv[d[v]] = v
....:     
sage: C.vertices()

['0000',
 '0001',
 '0010',
 '0011',
 '0100',
 '0101',
 '0110',
 '0111',
 '1000',
 '1001',
 '1010',
 '1011',
 '1100',
 '1101',
 '1110',
 '1111']
sage: G.vertices()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sage: d

{'0000': 0,
 '0001': 1,
 '0010': 2,
 '0011': 3,
 '0100': 4,
 '0101': 5,
 '0110': 6,
 '0111': 7,
 '1000': 8,
 '1001': 9,
 '1010': 10,
 '1011': 11,
 '1100': 12,
 '1101': 13,
 '1110': 14,
 '1111': 15}
sage: d_inv

{0: '0000',
 1: '0001',
 2: '0010',
 3: '0011',
 4: '0100',
 5: '0101',
 6: '0110',
 7: '0111',
 8: '1000',
 9: '1001',
 10: '1010',
 11: '1011',
 12: '1100',
 13: '1101',
 14: '1110',
 15: '1111'}
```



---

Comment by ncohen created at 2009-07-21 08:15:57

Patch number 4 :
- Cliquer now deals with graphs with vertex labels not in 0..n-1
- Some functions of Graph could use cliquer and now can. ( some functions dealing with MAXIMAL cliques instead of MAXIMUM cliques can not use cliquer, though ! )
- Some documentations have been rearranged
- Cliquer's graph_print function is added to cliquer.pxd if needed


---

Attachment


---

Comment by rlm created at 2009-07-21 14:26:25

OK, you've done a ton of work on this. There are a few minor details left, but I will take care of them myself, and post a referee patch. This ticket should be ready today.

PS -- A maximum clique is just a clique of maximal size, so those functions are also applicable to Cliquer, but I'll update those myself. :)


---

Comment by ncohen created at 2009-07-21 14:36:47

Thank you very much !! ;-)

Concerning the cliques, I agree when you say that a "A maximum clique is just a clique of maximal size", but a "maximal clique" is a clique such that there is no bigger clique in the graph -- according to the subset inclusion order (all the maximal cliques of a graph need not have the same cardinality) -- and this I what I thought I had read in the descriptions of the others functions.

And.... now that this seems to be finished, I only have left to take care of the LP/MIP patch, which seems quite another adventure... ;-) 

Thanks again !


---

Attachment


---

Comment by rlm created at 2009-07-21 18:04:16

Replying to [comment:29 ncohen]:
> Concerning the cliques, I agree when you say that a "A maximum clique is just a clique of maximal size", but a "maximal clique" is a clique such that there is no bigger clique in the graph -- according to the subset inclusion order (all the maximal cliques of a graph need not have the same cardinality) -- and this I what I thought I had read in the descriptions of the others functions.

I had realized this some time after writing that comment. Please forgive me.


---

Comment by rlm created at 2009-07-21 18:56:33

Editing.


---

Attachment

Flattened patch based on sage-4.1.


---

Comment by rlm created at 2009-07-21 19:03:15

In the last patch:

1. I made all clique related functions start with `clique_` so that you can do `G.clique<tab>` and see all of them.

2. Added a few doctests here and there

3. Deprecated cliques, since it is ambiguous.


---

Comment by mvngu created at 2009-07-23 04:32:09

With the SPKG at #6355 and the patch on this ticket, I got the following doctest failures:

```
sage -t -long devel/sage-main/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx", line 318:
    sage: clqs = (HS.complement()).cliques()
Expected nothing
Got:
    doctest:1: DeprecationWarning: The function 'cliques' has been deprecated. Use 'cliques_maximal' or 'cliques_maximum'.
**********************************************************************
1 items had failures:
   1 of  89 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_refinement_graphs.py
	 [231.6 s]

<SNIP>

sage -t -long devel/sage-main/sage/graphs/graph_coloring.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/graphs/graph_coloring.py", line 208:
    sage: chromatic_number(G)
Expected:
    3
Got:
    doctest:224: DeprecationWarning: The function 'cliques' has been deprecated. Use 'cliques_maximal' or 'cliques_maximum'.
    3
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_graph_coloring.py
	 [2.3 s]
```



---

Comment by rlm created at 2009-07-23 16:55:43

Note: making the `refinement_graphs` doctest use Cliquer instead of NetworkX shaves about 21 seconds from the doctest time for the file!


---

Comment by ncohen created at 2009-07-23 17:31:22

I do not really know how to read patch files, but it seems to me you replaced :
m = max([len(c) for c in G.cliques()]) 
by
m = max([len(c) for c in G.cliques_maximum()]) 

If right, I have two remarks :
- The syntax of max([len(c) for c in G.cliques()])  makes me think that G.cliques() was meant to return the list of the maximAL cliques, and m is then meant to be the clique number of G. The expression max([len(c) for c in G.cliques_maximum()])  is syntaxically correct, thought as cliques_maximum returns only the maxiMUM cliques we may as well return the length of the first one as they all have the same size.
- In the end, and if I make no mistake, why about just setting m=G.clique_number() ?

I expect it to be way faster than an enumeration of all the cliques ! ;-)


---

Comment by rlm created at 2009-07-23 17:37:19

Apply on top of flattened patch


---

Attachment

Nathann,

Thanks for spotting that. The patch is updated!


---

Comment by mvngu created at 2009-07-31 17:50:10

I applied patches in the following order:
 1. the SPKG at #6355
 1. `trac_5793-cliquer-flattened.patch`
 1. `trac_5793-part-6.patch`
All doctests passed with Sage 4.1.1.rc0. So positive review.


---

Comment by mvngu created at 2009-07-31 23:32:09

Resolution: fixed
