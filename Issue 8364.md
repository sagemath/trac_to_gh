# Issue 8364: Make Cbc support multithread. Other LP solvers too if available

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-02-25 15:47:15

Assignee: jkantor

CC:  jason rlm wdj

Cbc supports multithread, and it is a shame Sage does not tell it to ! :-)

Nathann


---

Comment by ncohen created at 2010-02-28 19:13:20

Changing component from numerical to graph theory.


---

Comment by ncohen created at 2010-02-28 19:13:20

Changing status from new to needs_review.


---

Comment by schilly created at 2010-03-01 14:58:17

Changing status from needs_review to positive_review.


---

Comment by schilly created at 2010-03-01 14:58:17

patch is pretty straight forward and indeed does what it should. log=T/F works, too.


---

Comment by mvngu created at 2010-03-03 04:07:31

With Sage 4.3.3, I have the following patch queue:

```sh
[mvngu`@`sage sage-main]$ hg qapplied
trac_7671.patch
trac_7854.patch
trac_7966.patch
trac_8273_digraphs_cycles_enumerations-abm.patch
trac_8273_with_heap-abm.patch
trac_8331-bipartite-dict-initializer.patch
```

Now when applying [http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch), I got a hunk failure:

```sh
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8364/trac_8364.patch && hg qpush
adding trac_8364.patch to series file
applying trac_8364.patch
patching file sage/graphs/generic_graph.py
Hunk #24 FAILED at 4063
Hunk #26 succeeded at 4249 with fuzz 1 (offset 48 lines).
1 out of 29 hunks FAILED -- saving rejects to file sage/graphs/generic_graph.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8364.patch
[mvngu`@`sage sage-main]$ cat sage/graphs/generic_graph.py.rej
--- generic_graph.py
+++ generic_graph.py
`@``@` -4032,13 +4064,13 `@``@`
         p.set_integer(b)
 
         if value_only:
-            return p.solve(objective_only=True,log=log)
-        else:
-            obj=p.solve(log=log)
+            return p.solve(objective_only=True, **kwds)
+        else:
+            obj=p.solve(**kwds)
             b=p.get_values(b)
             return [v for v in g.vertices() if b[v]==1]
 
-    def edge_connectivity(self,value_only=True,use_edge_labels=True, vertices=False):
+    def edge_connectivity(self,value_only=True,use_edge_labels=True, vertices=False, **kwds):
         r"""
         Returns the edge connectivity of the graph
         ( cf. http://en.wikipedia.org/wiki/Connectivity_(graph_theory) )
```

Could you rebase [trac_8364.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch) on top of the above patch queue? That is, first apply the following tickets in this order:

 1. #7671
 1. #7854
 1. #7966
 1. #8273
 1. #8273
 1. #8331

Then rebase [trac_8364.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch) with the patches at the above tickets.


---

Comment by mvngu created at 2010-03-03 04:07:31

Changing status from positive_review to needs_work.


---

Comment by ncohen created at 2010-03-21 13:02:58

Here is a new version based on the latest Sage release :-)

Nathann


---

Comment by ncohen created at 2010-03-21 13:02:58

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-04-15 03:43:24

How about we specify the solver options as a solver_options dictionary, instead of just blindly passing on whatever is passed into the function on to the solver?  For example:


```
def feedback_edge_set(self,value_only=False, solver_options=dict()): 

   ...
   p.solve(**solver_options)

```


This seems a bit cleaner to me.


---

Comment by ncohen created at 2010-04-15 07:32:17

Hello !!!!

Well, it is indeed cleaner, but it would give longer lines... Well, the only two options I like to tune through this patch are "solver" or "log". Most of the time, you just want your function to give you more output than usual, and for the moment you can do it like this :

```
graphs.PetersenGraph.matching(log=1)
```


If you want to change the solver you use, it gives 


```
graphs.PetersenGraph.matching(solver="GLPK")
```


I agree your version would be cleaner, but it would mean that getting more output has to be said like this :


```
graphs.PetersenGraph.matching(solver_options = {"log" : 1})
```


Which begins to be quite long... Well, I'm just giving you my idea of it. It you still want me to change it to solver_options, I'll do it immediately, as it is indeed cleaner :-)

Nathann


---

Comment by ncohen created at 2010-04-15 07:32:17

Changing status from needs_review to needs_info.


---

Comment by schilly created at 2010-04-15 09:06:29

Replying to [comment:6 jason]:
> How about we specify the solver options as a solver_options dictionary, instead of just blindly passing on whatever is passed into the function on to the solver?

Nice idea, but regarding the scip solver this doesn't work. It has another way of specifying it's parameters:

```
s = scip.solver()
s.categoryX['keyY'].paramZ = value
```


see here [http://code.google.com/p/python-zibopt/source/browse/trunk/src/zibopt/scip.py#251](http://code.google.com/p/python-zibopt/source/browse/trunk/src/zibopt/scip.py#251)

So, if you want to specify solver parameters, you would need a mechanism where the users instantiates the solver class in an object, configures it, and then passes it on inside the solve method! i.e. `solve(instance=s)` and the code in this patch then uses that `s` instead of instantiating its own solver.


---

Comment by ncohen created at 2010-04-15 09:50:05

Well, I understood "passed to the solver" as "passed to the MixedIntegerLinearProgram" object, or to its solve function, which is exactly an abstraction above all solvers :-)

But it is perfectly true that because of this class, it becomes very difficult to access solver-specific options... :-/

Nathann


---

Comment by ncohen created at 2010-04-24 09:43:01

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2010-05-08 01:12:31

New (working) version, based on #8892 ! :-)

Nathann


---

Comment by ncohen created at 2010-05-08 01:28:20

**kwds are replaced by two arguments : verbose and solver


---

Comment by jason created at 2010-05-15 03:53:06

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-05-15 03:53:06

I like this patch.  Two comments:

Applying to 4.4.2.alpha0 gives:

```
applying trac_8364.patch
patching file sage/graphs/generic_graph.py
Hunk #13 FAILED at 3526
Hunk #14 FAILED at 3639
Hunk #17 succeeded at 3566 with fuzz 1 (offset -227 lines).
Hunk #20 succeeded at 3838 with fuzz 1 (offset -226 lines).
Hunk #22 succeeded at 3907 with fuzz 1 (offset -227 lines).
Hunk #24 succeeded at 3997 with fuzz 2 (offset -226 lines).
Hunk #27 succeeded at 4206 with fuzz 2 (offset -225 lines).
2 out of 29 hunks FAILED -- saving rejects to file sage/graphs/generic_graph.py.rej
patching file sage/graphs/graph.py
Hunk #3 succeeded at 1470 with fuzz 1 (offset -1 lines).
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8364.patch

```


Second: about half of the docstrings for the solver option seem to be missing words.  I like the solver option docstring that is given for feedback_vertex_set the best.

With those two changes, this should be an easy, quick review.


---

Comment by jason created at 2010-05-15 03:54:29

Oops, I didn't see that #8892 was not merged into alpha0.  I'll try compiling rc0 and applying the patch there---this may not need a rebase after all.

However, the solver option docstrings still need to be fixed.


---

Comment by jason created at 2010-05-15 04:20:03

Okay, applying to 4.4.2.rc0:


```
applying trac_8364.patch
patching file sage/graphs/generic_graph.py
Hunk #13 FAILED at 3526
Hunk #14 FAILED at 3639
Hunk #17 succeeded at 3569 with fuzz 1 (offset -224 lines).
Hunk #20 succeeded at 3842 with fuzz 1 (offset -222 lines).
Hunk #22 succeeded at 3913 with fuzz 1 (offset -221 lines).
Hunk #24 succeeded at 4003 with fuzz 2 (offset -220 lines).
Hunk #27 succeeded at 4213 with fuzz 2 (offset -218 lines).
2 out of 29 hunks FAILED -- saving rejects to file sage/graphs/generic_graph.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8364.patch
```


So this patch still needs a rebase (note that #8892 is included in 4.4.2.rc0).


---

Attachment

The amount of times I have rewritten this whole patch is just obscene :-D

Ok, so what's new in this version ? First, it is based on 4.4.2.rc0, into which #8892 in already included (thanks Jason !), and it does the same job as usual, plus one or two fixesin the docstrings. By the way, I fixed a bug in function at line 3152 or graph.py (last entry in the .patch file), by removing a ",t"... I have to admit I have absolutely NO IDEA how this ",t" appeared there, but well, it prevented the function from working, though... I also hadn't noticed the function max_weight_matching from networkx had been exposed, which makes ticket #8166 useless... But I will modify it so that we do not have in Sage 2 different functions for max matching (at the moment, matching() and max_weight_matching()).

Please Jason, if you can review this ticket again, help me !! I could not stand rewriting all these modifications again if it needs to be rebased once more ! :-)

Thank youuuuuuu !!

Nathann


---

Comment by ncohen created at 2010-05-15 17:59:04

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-05-20 20:07:04

Changing priority from major to critical.


---

Attachment


---

Comment by mvngu created at 2010-05-21 10:36:31

Changes in reviewer patch include:

 * Some consistency along the lines of [PEP 008](http://www.python.org/dev/peps/pep-0008/).
 * Some documentation fixes.
 * Sphinx fixes to get LaTeX markups processed and displayed on the reference manual.
 * Cross reference classes and methods.

Some issues:

 * In `graphs/generic_graph.py`, for the method `dominating_set()`, the following change was made:
 {{{
`@``@` -3941,13 +4002,13 `@``@`
         p.set_integer(b)
 
         if value_only:
-            return p.solve(objective_only=True,log=log)
-        else:
-            obj=p.solve(log=log)
+            return p.solve(objective_only=True, solver = solver, log = verbose)
+        else:
+            obj=p.solve(solver = solver, log = verbose)
             b=p.get_values(b)
             return [v for v in g.vertices() if b[v]==1]
 
 }}}
 And yet from thereon, "obj" isn't used at all. I have changed that to
 {{{
p.solve(solver=solver, log=verbose)
 }}}
 * Remove a redundant import in `graphs/graph.py` in the method `minor()`:
 {{{
    from sage.sets.set import Set
	rs_dict = {}
        for h in H:
            rs_dict[h] = [v for v in self if rs[h][v]==1]

	return rs_dict
 }}}
 The class `Set` is imported there, but is never used from thereon within the method.
 
In short, my reviewer patch is about making the documentation added by ncohen consistent. Anyone care for a final review?


---

Comment by ncohen created at 2010-05-21 12:28:32

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-05-21 12:28:32

Thank you very much for your patch Minh !! I will try to remember, this time, how you want the INPUT sections to be formatted :-)

Positive review !


---

Comment by was created at 2010-06-03 04:21:32

Resolution: fixed
