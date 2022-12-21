# Issue 9567: Networkx-1.1 spkg

Issue created by migration from Trac.

Original creator: bedwards

Original creation time: 2010-07-21 21:07:33

Assignee: jason, ncohen, rlm

CC:  ncohen

Keywords: networkx spkg graph theory

This is the updated networkx package. It includes new features, bug fixes, and a couple of API changes. More information can be found here:

http://networkx.lanl.gov/reference/news.html

Package:

http://spkg-upload.googlecode.com/files/networkx-1.1.spkg

MD5 Sum

http://spkg-upload.googlecode.com/files/networkx-1.1.spkg.md5



---

Comment by mvngu created at 2010-07-21 21:27:48

Is this ready for review?


---

Comment by rlm created at 2010-07-21 21:35:31

Three files with doctest failures, most look pretty harmless, different number of arguments, etc.:

The failures were

```
----------------------------------------------------------------------

The following tests failed:

	sage -t --long devel/sage-main/sage/graphs/graph_generators.py # 1 doctests failed
	sage -t --long devel/sage-main/sage/graphs/generic_graph.py # 8 doctests failed
	sage -t --long devel/sage-main/sage/graphs/graph.py # 19 doctests failed
----------------------------------------------------------------------
```



http://sage.pastebin.com/bTMLkp1H


---

Comment by rlm created at 2010-07-21 23:22:46

The `graph_generators.py` failure looks like a new NX bug:

```
sage: networkx.random_powerlaw_tree(10, 2)
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/scratch/rlmill/sage-4.5-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/<ipython console> in <module>()

/scratch/rlmill/sage-4.5-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/local/lib/python/networkx/generators/random_graphs.pyc in random_powerlaw_tree(n, gamma, create_using, seed, tries)
    930 
    931     """
--> 932     from nx.generators.degree_seq import degree_sequence_tree
    933     try:
    934         s=random_powerlaw_tree_sequence(n,

ImportError: No module named nx.generators.degree_seq
```



---

Comment by rlm created at 2010-07-21 23:26:49

Several API changes:

```
sage: networkx.triangles?
Type:		function
Base Class:	<type 'function'>
String Form:	<function triangles at 0x4899b18>
Namespace:	Interactive
File:		/scratch/rlmill/sage-4.5-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/local/lib/python/networkx/algorithms/cluster.py
Definition:	networkx.triangles(G, nbunch=None)
Docstring:
    <no docstring>
```

(triangles used to take another argument) -- `cluster_triangles()` in Sage will need to be updated to reflect this.


```
sage: networkx.clustering?
Type:		function
Base Class:	<type 'function'>
String Form:	<function clustering at 0x4899c80>
Namespace:	Interactive
File:		/scratch/rlmill/sage-4.5-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/local/lib/python/networkx/algorithms/cluster.py
Definition:	networkx.clustering(G, nbunch=None, weights=False)
Docstring:
    <no docstring>
```

this is Sage's `clustering_coeff()`

These are both coming from the argument `with_weights` disappearing in NX.


---

Comment by rlm created at 2010-07-21 23:27:27

No idea here:

```
**********************************************************************
File "/scratch/rlmill/sage-4.5-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/devel/sage-main/sage/graphs/graph.py", line 2411:
    sage: (graphs.ChvatalGraph()).centrality_betweenness(normalized=False)
Expected:
    {0: 7.6666666666666661, 1: 7.6666666666666661, 2: 6.6666666666666661, 3: 6.6666666666666661, 4: 7.6666666666666661, 5: 7.6666666666666661, 6: 6.6666666666666661, 7: 6.6666666666666661, 8: 6.6666666666666661, 9: 6.6666666666666661, 10: 6.6666666666666661, 11: 6.6666666666666661}
Got:
    {0: 3.833333333333333, 1: 3.833333333333333, 2: 3.333333333333333, 3: 3.333333333333333, 4: 3.833333333333333, 5: 3.833333333333333, 6: 3.333333333333333, 7: 3.333333333333333, 8: 3.333333333333333, 9: 3.333333333333333, 10: 3.333333333333333, 11: 3.333333333333333}
**********************************************************************
```



---

Comment by rlm created at 2010-07-21 23:28:09

This function no longer takes a vertex as input:

```

sage: networkx.degree_centrality?
Type:		function
Base Class:	<type 'function'>
String Form:	<function degree_centrality at 0x87e9b0>
Namespace:	Interactive
File:		/scratch/rlmill/sage-4.5-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/local/lib/python/networkx/algorithms/centrality/degree.py
Definition:	networkx.degree_centrality(G)
Docstring:
    <no docstring>
```



---

Comment by rlm created at 2010-07-21 23:30:13

Changing status from new to needs_work.


---

Comment by rlm created at 2010-07-21 23:30:13

There are also some failures related to changes in the API of cliques functionality, but since we ship cliquer standard, which is an optimized C library for just this purpose, it seems we should be using that instead anyway.

All in all, these don't look bad at all. Not nearly as bad as upgrading to 1.0.

Ben -- If you want to submit a patch, I'd be glad to review it.


---

Comment by bedwards created at 2010-07-21 23:41:12

The betweenness centrality test is a little concerning, and at a glance I am unsure about the bug in the random_powerlaw_tree, it seems that should work just fine... I'll start working on a patch. The API changes are improvements in the package, imho, returning dictionaries instead of lists, do we change the tests or is that a whole other process? Sorry, I'm new at this.


---

Comment by ncohen created at 2010-07-22 01:28:17

I just creaed #9569 to deal with new methods defined in NetworkX 1-1. I will also touch the "triangles" version as it looks like #9420 should make it faster to count them using our tools.

Nathann


---

Comment by ncohen created at 2010-07-22 01:35:18

Ok, what I just did sounds stupid. It will be way easier to solve all the bugs and expose methods in the same patch. Let's talk discuss it through emails :-)

Nathann


---

Comment by rlm created at 2010-07-22 08:25:01

Replying to [comment:8 bedwards]:
> The API changes are improvements in the package, imho, returning dictionaries instead of lists, do we change the tests or is that a whole other process? Sorry, I'm new at this.

We should change everything to support the new syntax, especially since it is so easy. If the pickle jar were having problems, it might mean we would have more work to do, but it seems that 1.0->1.1 involves very minimal changes.


---

Comment by bedwards created at 2010-07-23 17:23:01

Started working on this a bit. I think the bug is in the test for the betweenness centrality, I tested it using igraph in R, and it returns the same betweenness centrality as networkx-1.1. Also this was noted as a bug fix in the networkx change log.


---

Comment by bedwards created at 2010-07-26 16:23:05

I've completed the patch, and the new version of the package. I've installed this on sage 4.5.1. Adding the spkg, and applying the patch should result in passing tests!

http://groups.google.com/group/sage-devel/attach/8cb10fd6e32e6380/networkx-1.1.p1.spkg?part=4

http://groups.google.com/group/sage-devel/attach/8cb10fd6e32e6380/networkx-1.1.p1.spkg.md5?part=5

http://groups.google.com/group/sage-devel/attach/8cb10fd6e32e6380/14602.patch?part=6

http://groups.google.com/group/sage-devel/attach/15cfd72f79082382/14602.patch.md5?part=4


---

Comment by rlm created at 2010-07-26 16:26:45

Ben,

Can you simply attach the patch to the ticket? Hit the attach button towards the top of the page :)


---

Comment by bedwards created at 2010-07-26 16:39:04

No, problem, wasn't quite sure of the protocol, here you go.


---

Attachment


---

Comment by bedwards created at 2010-07-26 20:37:19

Changing status from needs_work to needs_review.


---

Comment by bedwards created at 2010-08-02 20:19:11

networkx develops fast. Here is a new package for version 1.2. With the patch already attached above this should pass all the graphs/ tests with sage 4.5.1.

http://groups.google.com/group/sage-devel/attach/9521dbae9b6b22db/networkx-1.2.spkg?part=5

http://groups.google.com/group/sage-devel/attach/9521dbae9b6b22db/networkx-1.2.spkg.md5?part=4


---

Comment by ncohen created at 2010-08-03 02:11:45

Hello Ben !!!

I added a small patch containing the method cycle_basis (with a long doctest), that just calls NetworkX's. I haven't been able to properly write a cycle_space method (see http://groups.google.com/group/sage-support/browse_thread/thread/f99b59eaabf679a5/8bf34d54c183ab6b?lnk=gst&q=labelled#8bf34d54c183ab6b), so I tried to give a satisfying example in this docstring.

I give a positive review to your own patch for your patch/spkg, short of these two details :

 * I fixed some occurences of "dictionary" in my own patch
 * Your NetworkX SPKG has "uncommitted changes". Could you do a "hg commit", then upload the new version ? ( You can notice this when using the "sage -pkg" command to build spkg).

Nathann


---

Comment by bedwards created at 2010-08-03 15:02:51

Sorry forgot to commit, last time I built the package. Here is the newest one. Sorry about my bad spelling...


---

Comment by bedwards created at 2010-08-03 15:05:52

Here is the updated package.

http://groups.google.com/group/sage-devel/attach/6f6fb1d613bf3332/networkx-1.2.spkg?part=4

and the md5sum

http://groups.google.com/group/sage-devel/attach/6f6fb1d613bf3332/networkx-1.2.spkg.md5?part=5


---

Comment by ncohen created at 2010-08-03 15:31:28

Well, then if you can review my patch and find everything to your taste, you can set this whole ticket as having received a positive review :-)

Nathann


---

Comment by bedwards created at 2010-08-03 15:41:21

On google code, in case they disappear

http://spkg-upload.googlecode.com/files/networkx-1.2.spkg.md5

http://spkg-upload.googlecode.com/files/networkx-1.2.spkg


---

Comment by bedwards created at 2010-08-03 16:14:23

Nathan, you're patch looks great, and I learned a little about cycle basis! Thanks again for correcting my spelling. This one is ready.


---

Comment by bedwards created at 2010-08-03 16:14:23

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-07 05:31:39

Should I apply exactly

 * http://spkg-upload.googlecode.com/files/networkx-1.2.spkg
 * [attachment:14602.patch]
 * [attachment:trac_9567-cycle_basis.patch]

to merge this ticket?

I'm changing the status to 'needs_work' for this: The first patch is missing the ticket number in the first line of its commit string.  The first line itself should also be short (< 80 characters) but stand on its own, in order to keep `hg log` listings succinct and informative.  Of course, there's no problem with extra lines that describe the changes in detail.

The second patch's commit string should perhaps be a bit more descriptive.

Also, please update the Author(s) and Reviewer(s) fields.


---

Comment by mpatel created at 2010-08-07 05:31:39

Changing status from positive_review to needs_work.


---

Comment by ncohen created at 2010-08-08 11:11:23

The ordering is correct...

Ben : could you update your patch ? I can not overwrite it, and that's the only thing left to do.

Nathann


---

Comment by bedwards created at 2010-08-09 16:47:41

Sorry, I was out of town for the weekend. Saw that sage-4.5.2 came out over the weekend, rebuilt the patch for that version, fixing my spelling as well. The appropriate order would be to merge:

http://spkg-upload.googlecode.com/files/networkx-1.2.spkg
trac_9567-network-1.2.patch 
trac_9567-cycle_basis.patch

Nathann, maybe update yours for sage 4.5.2?


---

Attachment


---

Comment by bedwards created at 2010-08-10 23:19:10

Here is a new patched networkx-1.2 spkg that patches networkx to make it compatible with matplotlib.pyparsing.

http://spkg-upload.googlecode.com/files/networkx-1.2.p1.spkg

http://spkg-upload.googlecode.com/files/networkx-1.2.p1.spkg.md5


---

Comment by ncohen created at 2010-08-12 03:32:45

Updated !

Nathann


---

Attachment


---

Comment by ncohen created at 2010-08-12 03:38:47

Changing status from needs_work to positive_review.


---

Comment by ncohen created at 2010-08-12 03:38:47

And back to positive review, as the fiels/descriptions have been filled `:-)`

Nathann


---

Comment by mpatel created at 2010-08-15 08:02:08

Resolution: fixed
