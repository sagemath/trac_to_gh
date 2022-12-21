# Issue 1314: [graphs] calculate tutte polynomial

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-28 20:02:44

Assignee: mhansen

CC:  mvngu lkeough sdenton ncohen stefan azi simonking nbruin

Keywords: graphs




---

Comment by rlm created at 2007-12-17 15:15:27

Changing component from combinatorics to graph theory.


---

Comment by rlm created at 2007-12-17 15:15:27

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2007-12-17 15:15:27

Changing keywords from "graphs" to "".


---

Comment by ncohen created at 2009-05-17 16:17:20

http://homepages.mcs.vuw.ac.nz/~djp/tutte/

This software could be pretty useful.... But I know nothing about license matters :


--------------------------------------------------------------------------------
The majority of files are currently under the following simple and quite
unrestrictive license:

 "(C) Copyright David James Pearce and Gary Haggard, 2007.
  Permission to copy, use, modify, sell and distribute this software
  is granted provided this copyright notice appears in all copies.
  This software is provided "as is" without express or implied
  warranty, and with no claim as to its suitability for any purpose.

  Email: david.pearce`@`mcs.vuw.ac.nz"

This license may not be removed from any of the files in question.

This software makes use of Brendan McKay's excellent "Nauty" program
for determining (amongst other things) whether two graphs are
isomorphic or not.  You can find more information about this program
here: http://cs.anu.edu.au/~bdm/nauty

All files from the Nauty program are located in the nauty/
subdirectory.  The following license applies to all files in the
nauty/ directory (see nauty.h for more details):

  "Copyright (1984-2004) Brendan McKay.  All rights reserved.  Permission
   is hereby given for use and/or distribution with the exception of
   sale for profit or application with nontrivial military significance.
   You must not remove this copyright notice, and you must document any
   changes that you make to this program.
   This software is subject to this copyright only, irrespective of
   any copyright attached to any package of which this is a part.

   This program is only provided "as is".  No responsibility will be taken
   by the author, his employer or his pet rabbit for any misfortune which
   befalls you because of its use.  I don't think it will delete all your
   files, burn down your computer room or turn your children against you,
   but if it does: stiff cheddar.  On the other hand, I very much welcome
   bug reports, or at least I would if there were any bugs.
                                                        RIP, 1989
-----------------------------------------------------------------------------

So in the end it reads like the license is at least as GPL-uncompatible as Nauty's, and will then have to be included as an external software...


---

Comment by rlm created at 2009-05-17 18:51:37

Replying to [comment:3 ncohen]:
> So in the end it reads like the license is at least as GPL-uncompatible as Nauty's, and will then have to be included as an external software...

Not really. Sage includes software which could be used to replace this functionality. We just need to get the *rest* of the software relicensed, if this is possible.


---

Comment by mvngu created at 2009-10-01 16:13:00

CC myself.


---

Comment by timmcmillen created at 2009-11-06 12:33:13

Per discussion in Ticket http://trac.sagemath.org/sage_trac/ticket/7052 Pearce and Haggard's code could be included but nauty's license is incompatible. nauty could however be included as a separate optional spkg and the isomorphism function that it is used for replaced with Sage library calls. Then nauty could be used if available or called.

Since Pearce and Haggard's code is extremely efficient at computing the chromatic polynomial as well (between two and three orders of magnitude faster than the current Sage function) it could offer benefit there too.


---

Comment by jeremy.l.martin created at 2012-07-10 21:42:19

I have written code from scratch to compute the Tutte polynomial of a graph.  I think it is at least correct and maybe even sort of efficient.  Along the way I have written a couple of other routines for the Graph class that might be useful.  I am planning to submit a patch once I figure out how do that (I am brand new at Sage developing....)


---

Comment by ddrake created at 2012-07-12 16:53:53

This ticket requires an edge contraction method; the existing `merge_vertices` method doesn't work properly for the computation of Tutte polynomials. A working method is available at ticket #13239.


---

Comment by lkeough created at 2012-07-12 19:39:05

Tutte polynomial also needs code to determine whether an edge is a cut edge.  You can find this at ticket #13242.


---

Comment by mhansen created at 2012-07-13 02:18:40

I had some old code from awhile back for computing this which I've attached, along with some commented out possible optimizations.  I think I remember when doing this in practice, avoiding copying the graph saved quite a bit of time (hence the unmerge function).


---

Comment by jeremy.l.martin created at 2012-07-13 15:09:15

Replying to [comment:12 mhansen]:

> I had some old code from awhile back for computing this which I've attached, along with some commented out possible optimizations.  I think I remember when doing this in practice, avoiding copying the graph saved quite a bit of time (hence the unmerge function).

mhansen, thanks for sharing this code.  Unfortunately, it does not seem to give the right answer for K_4:

sage: G = graphs.[This is the Trac macro *CompleteGraph* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#CompleteGraph-macro)(4); G.allow_loops(true); G.allow_multiple_edges(true); tp = tutte_polynomial(G,x,y); tp

x<sup>2</sup>*y<sup>2</sup> + x*y<sup>3</sup> + x<sup>3</sup> + x<sup>2</sup>*y + x*y<sup>2</sup> + x<sup>2</sup> + x*y

The actual Tutte polynomial of K4 is x<sup>3</sup> + 3*x<sup>2</sup> + y<sup>3</sup> + 4*x*y + 3*y<sup>2</sup> + 2*x + 2*y.  

I currently do not see a way to implement the Tutte polynomial without making lots of copies of graphs, but maybe someone else can.


---

Comment by mhansen created at 2012-07-13 20:06:12

Sorry -- there was a typo in that one.  I've uploaded a new version which works and implements caching which should save quite a bit of time.


---

Comment by lkeough created at 2012-07-15 20:57:44

I timed both Jeremy's code and mhansen's code and it seems that mhansen's is much faster.  

The two codes give two different looking (but potentially the same) answers on the Petersen graph.

This is about a third of the tutte.sage output
14*x^4 + 22*(x + y)^2*x + 8*(x + y)*((x + y)*x + y^2 + x + y)*x + (x^4 +
x^3 + (x + y)*(x^2 + x + y) + x^2 + x + y)*x^2 + ((x + y)^2*x + (x +
y)^2 + y^3 + ((x + y)*x^2 + (x + y)*x + y^2 + x + y)*x + y^2 + x +
y)*x^2 + 22*(x + y)^2 + 13*(y^2 + x + y)^2 + 14*x^3 + 22*y^3 + 14*(x +
y)*(x^2 + x + y) + 4*(y^2 + x + y)*((x + y)^2 + y^3 + y^2 + x + y) +
5*((x + y)*x + (x^2 + x + y)*x + y^2 + x + y)*y + 9*((x + y)*x^2 + (x +
y)*x + y^2 + x + y)*x + 9*(x^4 + x^3 + x^2 + x + y)*x + ((x + y)^2*x +
(x + y)^2 + y^3 + ((x + y)*x^2 + (x + y)*x + y^2 + x + y)*x + y^2 + x +
y)*x + (x^4 + (x^4 + x^3 + x^2 + x + y)*x^2 + x^3 + (x + y)*(x^2 + x +
y) + (x^4 + x^3 + x^2 + x + y)*x + x^2 + x + y)*x + 4*(x^4 + (x + y)^2*x
+ (x + y)^2 + x^3 + y^3 + (x + y)*(x^2 + x + y) + ((x + y)*x^2 + (x +
y)*x + y^2 + x + y)*x + (x^4 + x^3 + x^2 + x + y)*x + x^2 + y^2 + 2*x +
2*y)*x + 2*(x^4 + (x + y)^2*x + (x + y)^2 + x^3 + y^3 + (x + y)*(x^2 + x
+ y) + ((x + y)*x^2 + (x + y)*x + y^2 + x + y)*x + (x^4 + x^3 + x^2 + x
+ y)*x + (x^4 + x^3 + (x + y)*(x^2 + x + y) + (x^4 + x^3 + x^2 + x +
y)*x + x^2 + x + y)*x + x^2 + y^2 + 2*x + 2*y)*x + 2*(x^4 + 2*(x +....

And this is the output of Jeremy's:
x^9 + 6*x^8 + 21*x^7 + 56*x^6 + 12*x^5*y + 114*x^5 + y^6 + 70*x^4*y +
30*x<sup>3*y</sup>2 + 15*x<sup>2*y</sup>3 + 10*x*y^4 + 170*x^4 + 180*x^3 + 120*x^2 + 9*y^5
+ 170*x^3*y + 105*x<sup>2*y</sup>2 + 65*x*y^3 + 35*y^4 + 240*x^2*y + 171*x*y^2 +
75*y^3 + 168*x*y + 84*y^2 + 36*x + 36*y

Although they are both showing up funny looking here...

Is there an easy way to multiply out and gather like terms in sage?


---

Attachment

You also need the patches from #13242


---

Comment by lkeough created at 2012-07-15 21:01:53

I attached Jeremy's code as Tuttepolynomial.sage in case anyone else wants to timeit.


---

Comment by mhansen created at 2012-07-15 21:04:27

`x` and `y` should ideally be integer polynomials (i.e., `R.<x,y> = ZZ[]`) -- then you don't have to deal with manually "expanding".

Additionally, in the `tuttepolynomial.sage` code, you should probably be caching a canonical label of the graph -- see the `cache_key` method in my patch.


---

Comment by lkeough created at 2012-07-15 21:21:53

Replying to [comment:17 mhansen]:
> `x` and `y` should ideally be integer polynomials (i.e., `R.<x,y> = ZZ[]`) -- then you don't have to deal with manually "expanding".
> 

I see now!  This makes it much better.  If we put R.<x,y> = ZZ[] as the first line in the Tutte polynomial code it does this for us.  Doing that shouldn't mess anything up, right?

> Additionally, in the `tuttepolynomial.sage` code, you should probably be caching a canonical label of the graph -- see the `cache_key` method in my patch.

Will do!


---

Comment by mhansen created at 2012-07-16 23:25:51

I was curious and went ahead an implemented the optimizations at http://homepages.ecs.vuw.ac.nz/~djp/files/TOMS10.pdf .  It seems our primary bottleneck is computing the canonical label of the graphs.


---

Attachment


---

Comment by azi created at 2013-05-05 14:30:55

What is the current status of this code?


---

Comment by mhansen created at 2013-05-05 14:43:36

tutte.sage works -- it just needs to be added as a patch, documented, etc.  I haven't had time to do this myself.


---

Comment by azi created at 2013-05-05 14:58:56

Nice, perhaps I'll do that one time if you wish.

Btw, there is a minor bug in tutte.sage. In the corner case 


```
257     if G.num_edges() == 0:
258         return 1
```


we should actually still return a polynomial since otherwise:


```
tutte_polynomial(graphs.CompleteGraph(10).complement())(0,3)
```


would break.


---

Comment by mhansen created at 2013-05-05 15:25:11

Replying to [comment:24 azi]:
> Btw, there is a minor bug in tutte.sage. In the corner case 
> 
> {{{
> 257     if G.num_edges() == 0:
> 258         return 1
> }}}

Yep.  One of the things that helps a lot is being able to avoid copying the graph.  For the Tutte polynomial code, we just make one copy of the graph on the initial call, but never copy it afterward.  I found context managers useful to manage mutating the graph and restoring it.

Also, I think the edge selection strategy has a bit of an effect on the speed of the chromatic polynomial computation as well.


---

Comment by azi created at 2013-05-11 07:24:40

I am in the process of integrating this code into Sage. There appears to be a memory issue when calculating the Tutte polynomial of a number of small graphs sequentially. Namely, Sage gets killed by the OS after exhausting all the physical memory.

Do you happen to have an idea where the fault for this could be?


---

Comment by mhansen created at 2013-05-11 08:45:27

Can you give some code to reproduce this?  I've been running code like


```python
for g in graphs.nauty_geng("7"):
    print tutte_polynomial(g, x, y)
```


but haven't been able to reproduce this.


---

Comment by azi created at 2013-05-11 08:52:40

Sure here is an example.


```
load tutte.sage
c = 0 
for G in graphs.nauty_geng("13 39:39"):
    
    if sorted(G.degree_sequence()) != sorted(G.complement().degree_sequence()):
        c+=1
        if tutte_polynomial(G,x,y) == tutte_polynomial(G.complement(),x,y):
            print G.graph6_string()
            from time import sleep
            sleep(24*60*60)
        if c % 1000 == 0:
            print c
```


The motivation of this code stems from an open problem that I am now working on.


---

Comment by mhansen created at 2013-05-11 18:14:41

My guess is just that the cache in that version isn't reset after each run.  If you add `tutte_polynomial.cache.clear()` before the `if tutte_polynomial(G,x,y) == tutte_polynomial(G.complement(),x,y):` line, you won't have that problem.


---

Comment by azi created at 2013-05-11 18:19:39

Good! I'll play with that and see what happens.

BTW, could you add yourself to the main TRAC page at the bottom so that I know what to write in the code under as the author ?


---

Attachment

Okay !

Attached is the nhansen's code factored into Sage. Before having any changes of being positively reviewed I we need to figure out how can we allow the users to use the edge selectors in the code and document that.

Let me know if you have any other comments and of course don't be shy to modify this yourself as well.


---

Comment by azi created at 2013-06-22 10:16:30

Changing status from new to needs_review.


---

Comment by azi created at 2013-06-27 20:22:13

Just a quick remark! The code computing the Tutte polynomial is correct (I reviewed that) so I only need someone to check if this patch is integrated correctly into Sage.


---

Comment by ncohen created at 2013-06-28 22:00:04

Hellooooooooo !!

If you just want comments on the integration into Sage, it would be nice if you could add it to the reference manual, perhaps rename the file to `tutte_polynomial.py`, and add documentation to the new functions until `sage -coverage yourfile.py` says that everything is filled. In particular it would be nice if you could be more verbose about what `VertexOrder` and `MinimizeDegree` actually do `:-)`

Oh, and people around do not like the `raise ValueError, "something"`. They say it's not pep8 or not Python3-ready, and prefer `ValueError("something")`.

This contextmanager decorator really is a funny thing `:-)`

Nathann


---

Comment by ncohen created at 2013-06-28 22:01:31

By the way, could you define what an "ear" is somewhere ? You say that it is a "sequence of vertices" which is a tad vague, and your code seems to imply somewhere that a vertex of degree 2 adjacent to two vertices of degree 3 is not an ear, while I thought that it was.

Well, .. `:-)`

Nathann


---

Comment by ncohen created at 2013-06-29 08:48:06

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2013-07-17 12:24:08

here is small clean-up patch. There remains to write doc for all functions.

for the bot:

apply trac_1314_tuttePoly.patch trac_1314_addon_fc.patch


---

Comment by chapoton created at 2013-07-22 09:02:29

Here is a new patch, that includes

* renaming of the file tutte_poly.py into tutte_polynomial.py

* inclusion into the reference manual

There still remains work to be done to have 100% doctesting and clean documentation


---

Comment by azi created at 2013-07-29 12:28:06

Hello!

What exactly is still required to be done? Also, is there a reason for renaming it to tutte_polynomial? I am wondering whether we should name it tuttepoly to be consistent with chrompoly?


---

Comment by chapoton created at 2013-07-29 12:38:33

There is nothing like chrompoly, the function is called 

```
G.chromatic_polynomial
```


What remains to be done: add explanations, and document every function. See the previous comments (see comments 34 and 35 in particular)


---

Comment by azi created at 2013-07-29 12:42:37

Yes! But the file is called chrompoly.py. And so is the file for the matching polynomial called matchpoly.

OK I'll  look into Nathann's comments!


---

Comment by chapoton created at 2013-08-31 19:09:53

I have started adding the doc, but there remains several functions with no doc.

In particular, it is necessary to explain more precisely *what is an ear*.


---

Comment by chapoton created at 2013-09-01 08:13:51

more doc, doctest coverage is now 65%


---

Comment by chapoton created at 2013-10-01 20:03:51

more doc, doctest coverage is now *95%*

There remains only one function to doctest, but this is a decorator and I do not know what to do ! Could anybody please help ?


---

Comment by ncohen created at 2013-10-02 08:09:35

You could just call a function which is decorated with it, and add a `#indirect doctest` flag to the corresponding doctest line.

Nathann


---

Comment by chapoton created at 2013-10-02 18:30:22

*100 %* doctested and almost ready for review !

_But_ the doc of `tutte_polynomial` does not appear, because it is cached (in a custom way, not by the usual `cached_function`) !


---

Comment by mhansen created at 2013-10-03 08:27:14

Yep, I think this was before cached_function existed.  Anyway, you can add "`@`sage_wraps(func)" before "def wrapper" to make things nicer on that front.  I also feel that at the end of the tutte_polynomial function, we should add something like 


```
if initial_call is True:
    tutte_polynomial.cache.clear()
```


so that the cache is valid for only the computation of one "tree".  This does play bad with threads (which aren't used much).  It might be better to just manually pass the cache along as a default argument throughout the call tree.  I think that's probably best.


---

Attachment

The docs seems to be ok now, thanks Mike !

I have not taken care of the cache cleaning, as I do not know where to put the lines you suggested.

Still I think it deserves to be "need review"


---

Comment by chapoton created at 2013-10-03 17:02:14

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2013-10-15 19:05:29

Changing keywords from "" to "tutte, graph".


---

Comment by ncohen created at 2013-10-16 15:17:17

> I have not taken care of the cache cleaning, as I do not know where to put the lines you suggested.

At the end of the block `if initial_call is True`, you can add the following :


```
ans = tutte_polynomial(G, initial_call=False, edge_selector=edge_selector)
tutte_polynomial.cache.clear()
return ans
```


Nathann


---

Comment by mhansen created at 2013-10-16 15:25:56

I think it's better to just have a cache=None default keyword.  On the initial call, this can be detected and a new cache can be created or the user could pass in their own to use across multiple runs.


---

Comment by chapoton created at 2013-10-18 19:51:21

Mike, could you please add a review patch implementing what you suggest ? I do not feel able to guess and try to do it myself.


---

Comment by chapoton created at 2014-01-04 20:13:58

New commits:


---

Comment by ncohen created at 2014-01-07 09:45:21

Ping ?


---

Comment by chapoton created at 2014-01-07 11:48:41

This is now available via matroids.


---

Comment by ncohen created at 2014-01-07 11:50:30

What does that mean ? `O_o`


---

Comment by chapoton created at 2014-01-07 11:52:23

This mean that somebody else has done the job for matroids.

```
sage: Matroid(graphs.PetersenGraph()).tutte_polynomial()
x^9 + 6*x^8 + 21*x^7 + 56*x^6 + 12*x^5*y + y^6 + 114*x^5 + 70*x^4*y + 30*x^3*y^2 + 15*x^2*y^3 + 10*x*y^4 + 9*y^5 + 170*x^4 + 170*x^3*y + 105*x^2*y^2 + 65*x*y^3 + 35*y^4 + 180*x^3 + 240*x^2*y + 171*x*y^2 + 75*y^3 + 120*x^2 + 168*x*y + 84*y^2 + 36*x + 36*y
```



---

Comment by ncohen created at 2014-01-07 11:56:28

Oh. Right. They enumerate all spanning trees, though. They would probably be glad to have another implementation `:-P``

Nathann


---

Comment by ncohen created at 2014-01-07 12:08:08

Anyway Frederic, is this patch in `needs_review` or in `needs_work` (cf the caching thing above), and what is left to be reviewed ? Jernej said some time ago that the mathematical part of the algorithm was correct, but as it seems he wrote the code himself that does not count `:-P`

Nathann


---

Comment by Stefan created at 2014-01-07 12:35:42

The  Matroid implementation is hopelessly slow, and an optimized implementation as in this ticket would be most welcome for matroids too. Until that day, there is definitely a use for the implementation on this ticket!


---

Comment by ncohen created at 2014-01-07 13:15:21

Stefan : how should this method be exposed in the matroid code ? It only works for graph, and I guess matroids need something more general ?

Nathann


---

Comment by Stefan created at 2014-01-07 13:19:30

Yeah. The main idea (caching small graphs) generalizes to matroids, but the code needs to be changed properly, and probably tweaked a lot to get good speeds.


---

Comment by ncohen created at 2014-01-07 13:21:18

Okay. Does it mean that the function that this patch implements is of no direct use for Matroids, and that there is no need to expose it anywhere right now ?

Nathann


---

Comment by ncohen created at 2014-01-07 16:01:42

Okayyyyyyy... Let's sum it up : Mike Hansen wrote the initial code, Jernej checked the math and cleaned bits of it, and Frédéric cleaned it again and add some documentation.

Cool. I just changed the branch as I have a couple of commits to add 

* Rebase on 6.1.beta4
* An option to clean the cache, as mentionned earlier

I agree with the non-mathematical part of what was above. Soooooo we just need somebody to review my two commits and we are done.

Have fuuuuuuuuun !

Nathann


---

Comment by git created at 2014-01-07 16:02:07

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-01-07 17:16:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2014-01-07 17:19:36

I've removed the `initial_call` argument since it was prone to be abused (especially since it was the first one), and doing it this way should give some (marginal) speedup. I'm going to run some timings now. I'm also going to now try it by converting to use `cached_function`.

Edit - I just realized I forgot to move the ``@`_cache` to the internal function...


---

Comment by tscrim created at 2014-01-07 17:54:47

Okay, ``@`cached_function` doesn't work because we can't pass a key function to it... (aside: I think such a feature would be quite useful) Back to the custom ``@`_cache`.

With my changes (including some other optimizations):

```
sage: P = graphs.PetersenGraph()
sage: %timeit P.tutte_polynomial()
1 loops, best of 3: 256 ms per loop
```

Before:

```
sage: P = graphs.PetersenGraph()
sage: %timeit P.tutte_polynomial()
1000 loops, best of 3: 1.08 ms per loop
```


Now I'm currently perplexed...currently the best involves extra if statements, creation of parents, and unused arguments being passed. So we might just want to merge `6ef434e` instead. Still testing stuff...


---

Comment by git created at 2014-01-07 18:09:24

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2014-01-07 18:23:03

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-01-07 18:26:23

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2014-01-07 18:28:16

I put my changes in the branch `u/tscrim/tutte_polynomial-1314` and reverted back the public branch. It seems like I'm making a whole bunch of extra function calls that I have NO idea why...stuff it getting put into the cache as it should, everything is calling the internal function... IMO this is a better way of doing things, but something is being hyper-sensitive.

Anyways, I did make a few tweaks. I put `initial_call` as the last argument to make the user less likely to touch it. I also allowed the cache to take non-keyword arguments. I also made some other micro-optimizations by moving the `if edge_selector is None:` into the `initial_call` block and moved the `x,y = R.gens()`.


---

Comment by tscrim created at 2014-01-07 19:14:25

Changing status from needs_review to needs_info.


---

Comment by tscrim created at 2014-01-07 19:14:25

Okay, I figured out what was changing. I wasn't caching the final result of the Tutte polynomial, and how it currently is done will overly clear the cache. For example, say you compute the Tutte polynomial on some large graph `G`, then you compute it on a very small graph `H` and ask it to clear the cache. Now the cached data for `G` is gone. I think we should always cache the final results, and with the current implementation, there is the possibility we've already computed the Tutte polynomial of a small graph. However I think this will be infrequent or you should not be clearing the utility cache.

Although there is a problem, we get memory leaks. Now one can argue with the previous behavior along with the default implementation, this is not a leak. If the user was deciding to keep the cache, this would be the user knowing what (s)he is doing. Yet I wouldn't want my small computation to destroy the data of my big one, nor store it myself. So which way should we go, and if we go with 2 caches, how usable would the weak caches be? Feedback is needed.

Simon, Nils -- I cc-ed you here because we might need a good weak cache solution here and I'd like your thoughts and expertise.
----
New commits:


---

Comment by ncohen created at 2014-01-07 19:37:16

Ahahahah. So you will not do without a "local cache" and a "global cache". You want to use the global cache to speedup the results, and you want to clear the local cache only. And merge the two if the user wants to keep it.

And what happens if the local cache generates values that exist in the global cache too ? `:-P` What do you cache then ? `:-P`

I think you are overthinking very simple needs `:-)`

Nathann


---

Comment by SimonKing created at 2014-01-07 21:54:12

Replying to [comment:71 tscrim]:
> Okay, ``@`cached_function` doesn't work because we can't pass a key function to it...

I don't understand what you mean with this. Note that in the `@`_cached decorator you are not passing an arbitrary key function either: You have _cache_key hardcoded.


---

Comment by tscrim created at 2014-01-07 21:54:59

Replying to [comment:77 ncohen]:
> Ahahahah. So you will not do without a "local cache" and a "global cache". You want to use the global cache to speedup the results, and you want to clear the local cache only. And merge the two if the user wants to keep it.

What we should probably do, if we do keep a global cache, is during the computation check if the key is in the global cache as well. However I'm thinking we should not have a global cache because we get a memory leak. Create a graph `G`, compute it's Tutte polynomial, then delete `G`. The polynomial is now stuck in the global cache (that we don't want to have to manually clear). I'm thinking the better way to do things is only have a local cache and make `tutte_polynomial()` a cached method of the graphs. That way when we delete the graph (along with the local cache), the resulting polynomial can be garbage collected. It's probably better to call the local cache the computation cache.

> And what happens if the local cache generates values that exist in the global cache too ? `:-P` What do you cache then ? `:-P`

In effect what I'm proposing is we keep them completely separate, I think that would create the least amount of problems. One other thing we could do is keep a small fixed-size permanent cache.

That gives me an idea about something else to do: have an option for the max size of a truly local cache when doing the computations. A priority queue up to some fixed size which keeps track of computed Tutte polynomials (with the priority being most often computed or some other heuristic) from that in the local cache. However the above, which turns it into a paging problem, might be an over-thought approach.

How big of a concern is it for recomputing Tutte polynomials for isomorphic-but-not-identical graphs?

Simon, I was trying to convert it to use the usual ``@`cached_function` instead of the custom cache.


---

Comment by SimonKing created at 2014-01-07 21:58:26

Replying to [comment:77 ncohen]:
> Ahahahah. So you will not do without a "local cache" and a "global cache". You want to use the global cache to speedup the results, and you want to clear the local cache only. And merge the two if the user wants to keep it.

Where are the two merged? I can't see it in the code.

> And what happens if the local cache generates values that exist in the global cache too ?

What should happen? You have two caches caching the same value. You clear the first cache. The value is still in the second cache.


---

Comment by SimonKing created at 2014-01-07 22:05:26

Replying to [comment:79 tscrim]:
> I'm thinking the better way to do things is only have a local cache and make `tutte_polynomial()` a cached method of the graphs.

Sounds reasonable.

> Simon, I was trying to convert it to use the usual ``@`cached_function` instead of the custom cache.

Can you use immutable graphs? See #15278, #15603, #15619 and #15622. These can be used as dictionary key and are thus acceptable input for a cached function.


---

Comment by tscrim created at 2014-01-07 23:23:18

The problem is we can't currently do any preprocessing  on the arguments for ``@`cached_function`(like we do for `UniqueRepresentation`), or at least that I'm aware of. So if we pass in a mutable graph, we can't convert it into something immutable and ``@`cached_function` returns an error (or do any other form of standardization).


---

Comment by mhansen created at 2014-01-08 01:41:32

I pushed a change which just makes the cache an optional keyword argument.  All of the sub-calls to tutte_polynomial use the same cache as the top-level one.  Additionally, if the use does not want the cache destroyed at the end of the computation, they just provide their own dictionary to the method.
----
New commits:


---

Comment by tscrim created at 2014-01-09 16:33:58

I like the elegance of it; so positive review from me. Nathann and anyone else, any objections?


---

Comment by tscrim created at 2014-01-09 16:34:07

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2014-01-09 16:36:45

> I like the elegance of it; so positive review from me. Nathann and anyone else, any objections?

Nono, it's fine `:-)`

Nathann


---

Comment by tscrim created at 2014-01-09 16:43:58

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2014-01-09 16:43:58

For a future ticket with #15657 - make `Graph.tutte_polynomial` a ``@`cached_method` once ``@`cached_method` can ignore the cache argument.


---

Comment by vbraun created at 2014-01-11 14:56:12

Resolution: fixed
