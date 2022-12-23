# Issue 5428: Doctest failure in devel/sage/doc/en/bordeaux_2008/method_of_graphs.rst

Issue created by migration from https://trac.sagemath.org/ticket/5428

Original creator: jsp

Original creation time: 2009-03-03 13:01:22

Assignee: mabshoff

CC:  georgsweber was

John Palmieri reported this first in sage-3.4.alpha. I is still here
in rc0:



```
File "/home/jaap/downloads/sage-3.4.alpha0/devel/sage/doc/en/bordeaux_2008/method_of_graphs.rst", line 25:
    sage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]
Expected:
    (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 1,
     -1, 1, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1, -1, -1)
Got:
    (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 1, -1, -1)
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_0

```



Jaap


---

Comment by jsp created at 2009-03-03 13:43:22

In sage-3.3 we have:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.3, Release Date: 2009-02-21                         |
| Type notebook() for the GUI, and license() for information.        |
sage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]
 (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 1, -1, -1)


```


versus


```
(3, 0, -1, 0, 0, -1, 1, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1, -1, -1)
```


in sage-3.4.xxx


Jaap


---

Comment by GeorgSWeber created at 2009-03-03 19:45:26

I'm more than a bit baffled. I have looked twice now over the patches that went into Sage in between 3.3 and 3.4.alpha0, but still I have no idea why this change would possibly be caused by any of them.

The least unplausible one (for me) is the patch about NTL (#5340) --- but I would not really believe that until I see it, i.e. testing with removing/reapplying it. (And I'm currently busy with other things.)


---

Comment by mabshoff created at 2009-03-04 04:13:17

Replying to [comment:3 GeorgSWeber]:

Hi Georg,

> I'm more than a bit baffled. I have looked twice now over the patches that went into Sage in between 3.3 and 3.4.alpha0, but still I have no idea why this change would possibly be caused by any of them.

The issue exists in both 3.3 and 3.4.alpha0/rc0 - the Bordeaux document was written in October 2008 by William and never doctested until the ReST patches. 

> The least unplausible one (for me) is the patch about NTL (#5340) --- but I would not really believe that until I see it, i.e. testing with removing/reapplying it. (And I'm currently busy with other things.) 

That patch isn't the cause. It would be interesting to see if it is a generic 32 vs. 64 bit problem or 32 bit linux specific.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-03-04 20:10:00

Thanks Michael,

given that information seems to make the patch trivial. William and Craig did some optimization in calculating the underlying P1List for modular symbols (trac #3502 I strongly guess), now using some caching of xgcd's and such.

From what I remember in the code, this hardly could be a 32bit/64bit issue anyway.

So the patch attached just is the "new" correct answer.


---

Comment by GeorgSWeber created at 2009-03-04 20:12:31

Hmmm,

I was too fast and just now re-read the description from Jaap, where he explicitly posted a Sage 3.3 session with the "other" answer.


---

Comment by GeorgSWeber created at 2009-03-04 20:19:47

OK,

to add more confusion: I re-re-read what Jaap posted above and looked again at the doctest failure with vanilla 3.4.rc0:

 * the Bordeaux October talk shows answer "A"
 * my computation with Sage 3.4.rc0 shows answer "B"
 * Jaap's computation with Sage 3.3 shows answer "B"
 * my own computation with Sage 3.3 shows answer "B"
 * the patch attached implements the new answer "B"

So it seems that only Jaap's description did mislead me, and the patch is good.


---

Comment by jsp created at 2009-03-04 20:32:30

I don't think the patch will do:

On sage.math, 64 bits:

```
jsp@sage:/scratch/jsp/sage-3.4.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]
(3, 0, -1, 0, 0, -1, 1, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1, -1, -1)
| Sage Version 3.4.rc0, Release Date: 2009-03-02                     |
| Type notebook() for the GUI, and license() for information.        |
```


On Fedora 9, 32 bits:


```
[jaap@paix sage-3.4.alpha0]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.4.rc0, Release Date: 2009-03-02                     |
| Type notebook() for the GUI, and license() for information.        |
sage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]
 (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 1, -1, -1)

```



Can't explain the different output.

Jaap


---

Comment by GeorgSWeber created at 2009-03-04 20:50:08

Hi Jaap,

I just re-re-re-read the posts on sage-devel --- there Rob Beezer reported *not* to have this doctest failure on his 64-bit box, but to see it on his 32bit box.

And yes, sigh, I just did the calculation, too, on sage.math (it's 64bit --- or 256bit :-)) and you are right. I'll redo the patch in a minute, on the assumption it is 32 bit versus 64 bit.


---

Attachment

tested against 3.4.rc0 on 32-bit (OS X)


---

Comment by mabshoff created at 2009-03-04 21:09:45

I doubt this is the fix. AFAIK no other modular form doctest has 32 vs. 64 bit specific result, so this fix might not address the root cause.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-03-04 21:38:20

Matter-of-factly, the following:

```
ModularSymbols(389,sign=1).basis()
```

gives different output on 32 bit OS X versus 64 bit sage.math. It seems to be consistent w.r.t. architecture , though.

The modular symbols code is old, and definitely should have more examples and doctests. Especially the above one should be added, if only to show clearly that an architecture dependency is there. The doctests that are there do focus on the important stuff, not on how the modular symbols bases are enumerated, or the explicit matrices of Hecke operators. (But e.g. on characteristic polynomials of the Hecke operators and their factorization instead --- which are *not* architecture dependent, as I just did check!) It would be interesting if the Cremona EC-lib modular symbol implementation (also in Sage) yields the same architecture dependency.

I admit I don't know yet where the architecture dependency actually creeps in.

But I believe what I see, and do think the (current) patch does its job.


---

Comment by GeorgSWeber created at 2009-03-04 21:50:59

Hooray,

I just checked that the documentation still builds fine (it does). I think this is the first time I did this after submitting a patch. I do love the new ReST documentation!

(But cloning did not copy over all the html files and such docbuild output, so there is potential left for further polishing.)


---

Comment by cwitty created at 2009-03-04 23:55:45

I tracked down some architecture-dependence in sage.modular when I was working on randstate.pyx (trying to remove "# random"), but then I never got around to submitting the patch.  Perhaps this is the problem?

Untested, very old, possibly no-longer-applies patch chunk:

```
--- a/sage/modular/modsym/relation_matrix.py	Sat Mar 29 12:28:22 2008 -0700
+++ b/sage/modular/modsym/relation_matrix.py	Sun Mar 30 07:09:50 2008 -0700
@@ -391,7 +391,8 @@ def sparse_2term_quotient(rels, n, F):
     ZERO = F(0)
     coef = [ONE for i in xrange(n)] 
     related_to_me = [[] for i in xrange(n)]
-    for v0, v1 in rels:
+    # Sort rels so that we get the same answer on 32-bit and 64-bit platforms.
+    for v0, v1 in sorted(rels):
         c0 = coef[v0[0]] * F(v0[1])
         c1 = coef[v1[0]] * F(v1[1])
         # Mod out by the relation 
```


Iterating through a set uses an order that depends on the `__hash__`, and `__hash__` values are different between 32-bit and 64-bit platforms.  I think I remember that sorting rels fixed that.  (I don't know what the performance implications are, but probably not much; sorting is pretty fast.)


---

Comment by jsp created at 2009-03-05 18:23:53

Replying to [comment:13 cwitty]:
> I tracked down some architecture-dependence in sage.modular when I was working on randstate.pyx (trying to remove "# random"), but then I never got around to submitting the patch.  Perhaps this is the problem?
> 
> Untested, very old, possibly no-longer-applies patch chunk:

Applying this "patch" introduced a ton of test failures all over the place.

Jaap


---

Comment by cwitty created at 2009-03-05 18:44:00

I don't see any way that this change could break the algorithm, so I'm guessing that these test failures are changing from one mathematically-correct answer to another mathematically-correct answer.  (But this should definitely be checked by somebody who understands the mathematics.)

I'm adding wstein to the CC list on the theory that he may have written the original code.  (The code is present in the very first revision that got checked in to mercurial, so version history doesn't say who wrote it.)


---

Comment by jsp created at 2009-03-05 19:00:11

Replying to [comment:15 cwitty]:
> I don't see any way that this change could break the algorithm, so I'm guessing that these test failures are changing from one mathematically-correct answer to another mathematically-correct answer.  (But this should definitely be checked by somebody who understands the mathematics.)
> 
> I'm adding wstein to the CC list on the theory that he may have written the original code.  (The code is present in the very first revision that got checked in to mercurial, so version history doesn't say who wrote it.)


I saw some weird results in here:



```
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage/doc/en/constructions/modular_forms.rst"
	sage -t  "devel/sage/doc/en/bordeaux_2008/method_of_graphs.rst"
	sage -t  "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
	sage -t  "devel/sage/sage/modular/cusps.py"
	sage -t  "devel/sage/sage/modular/modsym/space.py"
	sage -t  "devel/sage/sage/modular/modsym/heilbronn.pyx"
	sage -t  "devel/sage/sage/modular/modsym/boundary.py"
	sage -t  "devel/sage/sage/modular/modsym/ambient.py"
	sage -t  "devel/sage/sage/modular/modsym/hecke_operator.py"
	sage -t  "devel/sage/sage/modular/modform/numerical.py"
	sage -t  "devel/sage/sage/modular/hecke/ambient_module.py"
	sage -t  "devel/sage/sage/modular/hecke/module.py"
	sage -t  "devel/sage/sage/modular/abvar/abvar.py"
	sage -t  "devel/sage/sage/modular/abvar/homology.py"
	sage -t  "devel/sage/sage/modular/abvar/cuspidal_subgroup.py"
	sage -t  "devel/sage/sage/modular/abvar/finite_subgroup.py"
	sage -t  "devel/sage/sage/matrix/matrix_integer_dense.pyx"
	sage -t  "devel/sage/sage/matrix/matrix2.pyx"
	sage -t  "devel/sage/sage/schemes/elliptic_curves/padic_lseries.py"
	sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py"
	sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
Total time for all tests: 2885.1 seconds
Please see /scratch/jsp/sage-3.4.alpha0/tmp/test.log for the complete log from this test.
jsp@sage:/scratch/jsp/sage-3.4.alpha0$ 
```



Jaap


---

Comment by cwitty created at 2009-03-06 01:51:17

Oops, I had the wrong TRAC username when I tried to CC william...


---

Comment by was created at 2009-03-06 16:49:02

> I'm adding wstein to the CC list on the theory that he may 
> have written the original code. 

I did write the code.  A big +1 to sorted(rels), even though that will mean changing lots of doctests.   That's definitely the right fix. 

I tried the change and ran doctests and the many failures are all consistent with making a specific change of basis like sorted rels would do.   So this is the right fix, but requires a lot of work to update all the doctests.  Somebody let me know when a patch is up so I can referee it :-)


---

Comment by GeorgSWeber created at 2009-03-07 10:07:16

Mmmh, using "sorted(rels)" instead of "rels" certainly points in the right direction. 

But IMHO, the fix(es) should not be done inside "sparse_2term_quotient(rels, n, F)", where the first argument "rels" is processed, but way before in the calling functions.

More precisely, the function "modS_relations(syms)" should not do "return rels" but should do "return sorted(rels)", and in the function "relation_matrix_wtk_g0(...)" we should do "rels = sorted(rels.update(modI_relations(syms, sign)))", and possibly there are one or two other places more like this.

But could we not postpone this to a point release 3.4.x, and open another ticket for that?!? (The Bordeaux ReST file would have to be touched a second time, but that's trivial.)


---

Comment by mabshoff created at 2009-03-08 06:40:02

Replying to [comment:19 GeorgSWeber]:

Hi Georg,

> But could we not postpone this to a point release 3.4.x, and open another ticket for that?!? (The Bordeaux ReST file would have to be touched a second time, but that's trivial.)

I talked to William about this: positive review for the workaround patch, please open another ticket for the above fixes so it will be sorted out later.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-08 07:12:51

Resolution: fixed


---

Comment by mabshoff created at 2009-03-08 07:12:51

Merged in Sage 3.4.rc1.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-03-08 10:17:03

The follow-up ticket is #5456.
