# Issue 8364: Make Cbc support multithread. Other LP solvers too if available

archive/issues_008364.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @jasongrout @rlmill @wdjoyner\n\nCbc supports multithread, and it is a shame Sage does not tell it to ! :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8364\n\n",
    "created_at": "2010-02-25T15:47:15Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "Make Cbc support multithread. Other LP solvers too if available",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8364",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jkantor

CC:  @jasongrout @rlmill @wdjoyner

Cbc supports multithread, and it is a shame Sage does not tell it to ! :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8364





---

archive/issue_comments_074617.json:
```json
{
    "body": "Changing component from numerical to graph theory.",
    "created_at": "2010-02-28T19:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74617",
    "user": "https://github.com/nathanncohen"
}
```

Changing component from numerical to graph theory.



---

archive/issue_comments_074618.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-28T19:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74618",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074619.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-01T14:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74619",
    "user": "https://github.com/haraldschilly"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074620.json:
```json
{
    "body": "patch is pretty straight forward and indeed does what it should. log=T/F works, too.",
    "created_at": "2010-03-01T14:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74620",
    "user": "https://github.com/haraldschilly"
}
```

patch is pretty straight forward and indeed does what it should. log=T/F works, too.



---

archive/issue_comments_074621.json:
```json
{
    "body": "With Sage 4.3.3, I have the following patch queue:\n\n```sh\n[mvngu@sage sage-main]$ hg qapplied\ntrac_7671.patch\ntrac_7854.patch\ntrac_7966.patch\ntrac_8273_digraphs_cycles_enumerations-abm.patch\ntrac_8273_with_heap-abm.patch\ntrac_8331-bipartite-dict-initializer.patch\n```\n\nNow when applying [http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch), I got a hunk failure:\n\n```sh\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8364/trac_8364.patch && hg qpush\nadding trac_8364.patch to series file\napplying trac_8364.patch\npatching file sage/graphs/generic_graph.py\nHunk #24 FAILED at 4063\nHunk #26 succeeded at 4249 with fuzz 1 (offset 48 lines).\n1 out of 29 hunks FAILED -- saving rejects to file sage/graphs/generic_graph.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8364.patch\n[mvngu@sage sage-main]$ cat sage/graphs/generic_graph.py.rej\n--- generic_graph.py\n+++ generic_graph.py\n@@ -4032,13 +4064,13 @@\n         p.set_integer(b)\n \n         if value_only:\n-            return p.solve(objective_only=True,log=log)\n-        else:\n-            obj=p.solve(log=log)\n+            return p.solve(objective_only=True, **kwds)\n+        else:\n+            obj=p.solve(**kwds)\n             b=p.get_values(b)\n             return [v for v in g.vertices() if b[v]==1]\n \n-    def edge_connectivity(self,value_only=True,use_edge_labels=True, vertices=False):\n+    def edge_connectivity(self,value_only=True,use_edge_labels=True, vertices=False, **kwds):\n         r\"\"\"\n         Returns the edge connectivity of the graph\n         ( cf. http://en.wikipedia.org/wiki/Connectivity_(graph_theory) )\n```\n\nCould you rebase [trac_8364.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch) on top of the above patch queue? That is, first apply the following tickets in this order:\n\n1. #7671\n2. #7854\n3. #7966\n4. #8273\n5. #8273\n6. #8331\n\nThen rebase [trac_8364.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch) with the patches at the above tickets.",
    "created_at": "2010-03-03T04:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74621",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

With Sage 4.3.3, I have the following patch queue:

```sh
[mvngu@sage sage-main]$ hg qapplied
trac_7671.patch
trac_7854.patch
trac_7966.patch
trac_8273_digraphs_cycles_enumerations-abm.patch
trac_8273_with_heap-abm.patch
trac_8331-bipartite-dict-initializer.patch
```

Now when applying [http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch), I got a hunk failure:

```sh
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8364/trac_8364.patch && hg qpush
adding trac_8364.patch to series file
applying trac_8364.patch
patching file sage/graphs/generic_graph.py
Hunk #24 FAILED at 4063
Hunk #26 succeeded at 4249 with fuzz 1 (offset 48 lines).
1 out of 29 hunks FAILED -- saving rejects to file sage/graphs/generic_graph.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8364.patch
[mvngu@sage sage-main]$ cat sage/graphs/generic_graph.py.rej
--- generic_graph.py
+++ generic_graph.py
@@ -4032,13 +4064,13 @@
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
2. #7854
3. #7966
4. #8273
5. #8273
6. #8331

Then rebase [trac_8364.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8364/trac_8364.patch) with the patches at the above tickets.



---

archive/issue_comments_074622.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-03T04:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74622",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074623.json:
```json
{
    "body": "Here is a new version based on the latest Sage release :-)\n\nNathann",
    "created_at": "2010-03-21T13:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74623",
    "user": "https://github.com/nathanncohen"
}
```

Here is a new version based on the latest Sage release :-)

Nathann



---

archive/issue_comments_074624.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-21T13:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74624",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074625.json:
```json
{
    "body": "How about we specify the solver options as a solver_options dictionary, instead of just blindly passing on whatever is passed into the function on to the solver?  For example:\n\n\n```\ndef feedback_edge_set(self,value_only=False, solver_options=dict()): \n\n   ...\n   p.solve(**solver_options)\n\n```\n\n\nThis seems a bit cleaner to me.",
    "created_at": "2010-04-15T03:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74625",
    "user": "https://github.com/jasongrout"
}
```

How about we specify the solver options as a solver_options dictionary, instead of just blindly passing on whatever is passed into the function on to the solver?  For example:


```
def feedback_edge_set(self,value_only=False, solver_options=dict()): 

   ...
   p.solve(**solver_options)

```


This seems a bit cleaner to me.



---

archive/issue_comments_074626.json:
```json
{
    "body": "Hello !!!!\n\nWell, it is indeed cleaner, but it would give longer lines... Well, the only two options I like to tune through this patch are \"solver\" or \"log\". Most of the time, you just want your function to give you more output than usual, and for the moment you can do it like this :\n\n```\ngraphs.PetersenGraph.matching(log=1)\n```\n\n\nIf you want to change the solver you use, it gives \n\n\n```\ngraphs.PetersenGraph.matching(solver=\"GLPK\")\n```\n\n\nI agree your version would be cleaner, but it would mean that getting more output has to be said like this :\n\n\n```\ngraphs.PetersenGraph.matching(solver_options = {\"log\" : 1})\n```\n\n\nWhich begins to be quite long... Well, I'm just giving you my idea of it. It you still want me to change it to solver_options, I'll do it immediately, as it is indeed cleaner :-)\n\nNathann",
    "created_at": "2010-04-15T07:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74626",
    "user": "https://github.com/nathanncohen"
}
```

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

archive/issue_comments_074627.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-04-15T07:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74627",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_074628.json:
```json
{
    "body": "Replying to [comment:6 jason]:\n> How about we specify the solver options as a solver_options dictionary, instead of just blindly passing on whatever is passed into the function on to the solver?\n\nNice idea, but regarding the scip solver this doesn't work. It has another way of specifying it's parameters:\n\n```\ns = scip.solver()\ns.categoryX['keyY'].paramZ = value\n```\n\n\nsee here [http://code.google.com/p/python-zibopt/source/browse/trunk/src/zibopt/scip.py#251](http://code.google.com/p/python-zibopt/source/browse/trunk/src/zibopt/scip.py#251)\n\nSo, if you want to specify solver parameters, you would need a mechanism where the users instantiates the solver class in an object, configures it, and then passes it on inside the solve method! i.e. `solve(instance=s)` and the code in this patch then uses that `s` instead of instantiating its own solver.",
    "created_at": "2010-04-15T09:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74628",
    "user": "https://github.com/haraldschilly"
}
```

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

archive/issue_comments_074629.json:
```json
{
    "body": "Well, I understood \"passed to the solver\" as \"passed to the MixedIntegerLinearProgram\" object, or to its solve function, which is exactly an abstraction above all solvers :-)\n\nBut it is perfectly true that because of this class, it becomes very difficult to access solver-specific options... :-/\n\nNathann",
    "created_at": "2010-04-15T09:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74629",
    "user": "https://github.com/nathanncohen"
}
```

Well, I understood "passed to the solver" as "passed to the MixedIntegerLinearProgram" object, or to its solve function, which is exactly an abstraction above all solvers :-)

But it is perfectly true that because of this class, it becomes very difficult to access solver-specific options... :-/

Nathann



---

archive/issue_comments_074630.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-04-24T09:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74630",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_074631.json:
```json
{
    "body": "New (working) version, based on #8892 ! :-)\n\nNathann",
    "created_at": "2010-05-08T01:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74631",
    "user": "https://github.com/nathanncohen"
}
```

New (working) version, based on #8892 ! :-)

Nathann



---

archive/issue_comments_074632.json:
```json
{
    "body": "**kwds are replaced by two arguments : verbose and solver",
    "created_at": "2010-05-08T01:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74632",
    "user": "https://github.com/nathanncohen"
}
```

**kwds are replaced by two arguments : verbose and solver



---

archive/issue_comments_074633.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-15T03:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74633",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074634.json:
```json
{
    "body": "I like this patch.  Two comments:\n\nApplying to 4.4.2.alpha0 gives:\n\n```\napplying trac_8364.patch\npatching file sage/graphs/generic_graph.py\nHunk #13 FAILED at 3526\nHunk #14 FAILED at 3639\nHunk #17 succeeded at 3566 with fuzz 1 (offset -227 lines).\nHunk #20 succeeded at 3838 with fuzz 1 (offset -226 lines).\nHunk #22 succeeded at 3907 with fuzz 1 (offset -227 lines).\nHunk #24 succeeded at 3997 with fuzz 2 (offset -226 lines).\nHunk #27 succeeded at 4206 with fuzz 2 (offset -225 lines).\n2 out of 29 hunks FAILED -- saving rejects to file sage/graphs/generic_graph.py.rej\npatching file sage/graphs/graph.py\nHunk #3 succeeded at 1470 with fuzz 1 (offset -1 lines).\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8364.patch\n\n```\n\n\nSecond: about half of the docstrings for the solver option seem to be missing words.  I like the solver option docstring that is given for feedback_vertex_set the best.\n\nWith those two changes, this should be an easy, quick review.",
    "created_at": "2010-05-15T03:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74634",
    "user": "https://github.com/jasongrout"
}
```

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

archive/issue_comments_074635.json:
```json
{
    "body": "Oops, I didn't see that #8892 was not merged into alpha0.  I'll try compiling rc0 and applying the patch there---this may not need a rebase after all.\n\nHowever, the solver option docstrings still need to be fixed.",
    "created_at": "2010-05-15T03:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74635",
    "user": "https://github.com/jasongrout"
}
```

Oops, I didn't see that #8892 was not merged into alpha0.  I'll try compiling rc0 and applying the patch there---this may not need a rebase after all.

However, the solver option docstrings still need to be fixed.



---

archive/issue_comments_074636.json:
```json
{
    "body": "Okay, applying to 4.4.2.rc0:\n\n\n```\napplying trac_8364.patch\npatching file sage/graphs/generic_graph.py\nHunk #13 FAILED at 3526\nHunk #14 FAILED at 3639\nHunk #17 succeeded at 3569 with fuzz 1 (offset -224 lines).\nHunk #20 succeeded at 3842 with fuzz 1 (offset -222 lines).\nHunk #22 succeeded at 3913 with fuzz 1 (offset -221 lines).\nHunk #24 succeeded at 4003 with fuzz 2 (offset -220 lines).\nHunk #27 succeeded at 4213 with fuzz 2 (offset -218 lines).\n2 out of 29 hunks FAILED -- saving rejects to file sage/graphs/generic_graph.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8364.patch\n```\n\n\nSo this patch still needs a rebase (note that #8892 is included in 4.4.2.rc0).",
    "created_at": "2010-05-15T04:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74636",
    "user": "https://github.com/jasongrout"
}
```

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

archive/issue_comments_074637.json:
```json
{
    "body": "Attachment [trac_8364.patch](tarball://root/attachments/some-uuid/ticket8364/trac_8364.patch) by @nathanncohen created at 2010-05-15 17:59:04\n\nThe amount of times I have rewritten this whole patch is just obscene :-D\n\nOk, so what's new in this version ? First, it is based on 4.4.2.rc0, into which #8892 in already included (thanks Jason !), and it does the same job as usual, plus one or two fixesin the docstrings. By the way, I fixed a bug in function at line 3152 or graph.py (last entry in the .patch file), by removing a \",t\"... I have to admit I have absolutely NO IDEA how this \",t\" appeared there, but well, it prevented the function from working, though... I also hadn't noticed the function max_weight_matching from networkx had been exposed, which makes ticket #8166 useless... But I will modify it so that we do not have in Sage 2 different functions for max matching (at the moment, matching() and max_weight_matching()).\n\nPlease Jason, if you can review this ticket again, help me !! I could not stand rewriting all these modifications again if it needs to be rebased once more ! :-)\n\nThank youuuuuuu !!\n\nNathann",
    "created_at": "2010-05-15T17:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74637",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_8364.patch](tarball://root/attachments/some-uuid/ticket8364/trac_8364.patch) by @nathanncohen created at 2010-05-15 17:59:04

The amount of times I have rewritten this whole patch is just obscene :-D

Ok, so what's new in this version ? First, it is based on 4.4.2.rc0, into which #8892 in already included (thanks Jason !), and it does the same job as usual, plus one or two fixesin the docstrings. By the way, I fixed a bug in function at line 3152 or graph.py (last entry in the .patch file), by removing a ",t"... I have to admit I have absolutely NO IDEA how this ",t" appeared there, but well, it prevented the function from working, though... I also hadn't noticed the function max_weight_matching from networkx had been exposed, which makes ticket #8166 useless... But I will modify it so that we do not have in Sage 2 different functions for max matching (at the moment, matching() and max_weight_matching()).

Please Jason, if you can review this ticket again, help me !! I could not stand rewriting all these modifications again if it needs to be rebased once more ! :-)

Thank youuuuuuu !!

Nathann



---

archive/issue_comments_074638.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-15T17:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74638",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074639.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-05-20T20:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74639",
    "user": "https://github.com/nathanncohen"
}
```

Changing priority from major to critical.



---

archive/issue_comments_074640.json:
```json
{
    "body": "Attachment [trac_8364-reviewer.patch](tarball://root/attachments/some-uuid/ticket8364/trac_8364-reviewer.patch) by mvngu created at 2010-05-21 10:22:18",
    "created_at": "2010-05-21T10:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74640",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8364-reviewer.patch](tarball://root/attachments/some-uuid/ticket8364/trac_8364-reviewer.patch) by mvngu created at 2010-05-21 10:22:18



---

archive/issue_comments_074641.json:
```json
{
    "body": "Changes in reviewer patch include:\n\n* Some consistency along the lines of [PEP 008](http://www.python.org/dev/peps/pep-0008/).\n* Some documentation fixes.\n* Sphinx fixes to get LaTeX markups processed and displayed on the reference manual.\n* Cross reference classes and methods.\n\nSome issues:\n\n* In `graphs/generic_graph.py`, for the method `dominating_set()`, the following change was made:\n {{{\n`@``@` -3941,13 +4002,13 `@``@`\n         p.set_integer(b)\n \n         if value_only:\n-            return p.solve(objective_only=True,log=log)\n-        else:\n-            obj=p.solve(log=log)\n+            return p.solve(objective_only=True, solver = solver, log = verbose)\n+        else:\n+            obj=p.solve(solver = solver, log = verbose)\n             b=p.get_values(b)\n             return [v for v in g.vertices() if b[v]==1]\n \n }}}\n And yet from thereon, \"obj\" isn't used at all. I have changed that to\n {{{\np.solve(solver=solver, log=verbose)\n }}}\n* Remove a redundant import in `graphs/graph.py` in the method `minor()`:\n {{{\n    from sage.sets.set import Set\n\trs_dict = {}\n        for h in H:\n            rs_dict[h] = [v for v in self if rs[h][v]==1]\n\n\treturn rs_dict\n }}}\n The class `Set` is imported there, but is never used from thereon within the method.\n \nIn short, my reviewer patch is about making the documentation added by ncohen consistent. Anyone care for a final review?",
    "created_at": "2010-05-21T10:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74641",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

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

archive/issue_comments_074642.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-21T12:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74642",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074643.json:
```json
{
    "body": "Thank you very much for your patch Minh !! I will try to remember, this time, how you want the INPUT sections to be formatted :-)\n\nPositive review !",
    "created_at": "2010-05-21T12:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74643",
    "user": "https://github.com/nathanncohen"
}
```

Thank you very much for your patch Minh !! I will try to remember, this time, how you want the INPUT sections to be formatted :-)

Positive review !



---

archive/issue_comments_074644.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T04:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8364#issuecomment-74644",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_008552.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-06-03T04:21:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8364",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8364#event-8552"
}
```
