# Issue 812: add Pollack/Stevens overconvergent modular symbols code

Issue created by migration from https://trac.sagemath.org/ticket/812

Original creator: craigcitro

Original creation time: 2007-10-03 18:12:33

Assignee: craigcitro

CC:  davidloeffler roed craigcitro wuthrich

Keywords: p-adic L-functions

I'm just starting to work on implementing Pollack & Stevens' methods for using overconvergent modular symbols for p-adic L-functions, Stark-Heegner points, etc.


---

Comment by craigcitro created at 2007-10-03 18:12:45

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-31 04:08:20

Craig,

I know I must be bothering you by now, but what is the status here?

Cheers,

Michael


---

Comment by was created at 2009-06-25 09:17:20

Could somebody post a link to the Magma code here?


---

Comment by GeorgSWeber created at 2009-11-20 21:59:46

Sure,
it's part of the "shp package" at:

http://www.math.mcgill.ca/darmon/programs/shp/shp.html


---

Comment by was created at 2012-02-20 18:34:50

From Jennifer Balakrishnan:

Rob Pollack just ported over some of his p-adic L-series via
overconvergent modular symbols code to Sage, which could be very
useful for our p-adic BSD paper.

The code he sent me originally didn't quite produce results matching
our data, but I've worked on it over the last few days, fixed a few
bugs, noticed a few more, and thought this might be a good coding
sprint project for us this week.

Here's where the code currently stands:
-- it can compute the p-adic L-series in the split p case (with data
matching what we've already computed naively)
-- Rob says inert p is straightforward, just a matter of knowing how
to call the right objects in Sage, which I think I can do
-- I've tested it against the regulators I computed in my thesis, and
we can easily produce 10+ digits of precision in the L-value!!
-- for some primes, it results in memory errors (I've put examples,
working and not, in the docstring in the test file). I'm not sure how
to fix these.

As an enhancement, maybe we could also use some of your very fast code
for modular symbols?

Perhaps most mathematically interesting, the special values computed
by his program also result in the same +/-1 "sign" in the BSD formula
that our previous methods produced!

The code is available here:

http://sage.math.washington.edu/home/jen/OMS

To run it, attach master.sage and Jen/test_run_generic.sage. The
second file (http://sage.math.washington.edu/home/jen/OMS/Jen/test_run_generic.sage)
has some examples in the docstring.

Jen


---

Comment by mmasdeu created at 2014-03-14 14:25:22

Changing assignee from craigcitro to mmasdeu.


---

Comment by mmasdeu created at 2014-03-14 14:25:22

New commits:


---

Comment by mmasdeu created at 2014-03-14 14:31:17

Changing status from new to needs_review.


---

Comment by mmasdeu created at 2014-03-14 14:34:39

I think the code is usable enough that it should made into Sage. It includes the btquotients code, which is in a quite stable state as well. Several parts of the code are in need for more debugging, though. Especially the dist.pyx and distributions.py, which are not very robust.


---

Comment by chapoton created at 2014-03-21 21:07:04

There are some failing doctests, see patchbot's report


---

Comment by chapoton created at 2014-03-21 21:07:04

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-03-23 18:14:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmasdeu created at 2014-03-23 18:16:46

OK, I just learned that:
# long time optional - magma
does not work. One has to do:
# long time, optional - magma

So hopefully now it works!


---

Comment by was created at 2014-03-23 18:21:13

I just (very) quickly skimmed the patches -- this is some beautiful code!


---

Comment by mmasdeu created at 2014-03-25 17:58:19

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2014-05-06 01:22:47

Just some general "top-level" remarks, without really looking at the code yet:
- In `sage/modular/all.py`, the `import *` commands may not be what you want; this will all end up in the global namespace.
- It would be nice to add the new modules to the relevant `src/doc/en/reference/*/index.rst` files, probably with `*` = `modfrm`, `modmisc` and/or `modsym`.


---

Comment by roed created at 2014-05-06 01:49:47

Hi Marc,
Jen and I worked on reviewing this last weekend, but I'm getting married on Saturday and haven't had time to upload our progress, etc.  I'll try to have some comments and changes next week.


---

Comment by rws created at 2014-05-07 12:53:13

patchbot:

```
sage -t --long src/sage/doctest/sources.py  # 1 doctest failed
sage -t --long src/sage/modular/pollack_stevens/distributions.py  # 1 doctest failed
sage -t --long src/sage/modular/btquotients/pautomorphicform.py  # 2 doctests failed
```



---

Comment by rws created at 2014-05-07 12:53:13

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2014-05-09 19:33:31

I have made some large scale cleanup of the file btquotient (pyflakes and pep8 compliance). And also taken care of the "doctest continuation" plugin failure.
----
New commits:


---

Comment by git created at 2014-05-10 07:42:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-05-10 11:35:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-05-10 12:48:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-05-10 16:09:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-05-10 19:19:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-05-10 20:47:31

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmasdeu created at 2014-06-04 10:05:19

New commits:


---

Comment by mmasdeu created at 2014-06-04 10:05:19

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2014-08-23 06:34:17

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2014-08-23 06:34:17

one doctest is failing, and needs more doc, see patchbot report


---

Comment by git created at 2016-01-24 23:36:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-01-24 23:55:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-01-25 20:11:23

is this needs review now ?


---

Comment by roed created at 2016-01-25 21:45:27

Thanks for asking.  It's not yet: there are still doctest failures.  I was setting up an SMC project with this code and updated it to 7.0, so I figured I would push the changes here.  But there's more work to be done before Needs Review, which I don't have time to do this week.


---

Comment by davidloeffler created at 2016-01-26 09:14:34

It would be nice to get this in at long last. It's been an open Sage ticket since the dawn of time. Working on this at SD44 in Madison must have absorbed hundreds of person-hours and thousands of dollars of grant money, and we all flew home thinking the job was 95% done; that was three years ago. 

Can you say what would be the absolute minimum amount of work needed for this to get merged? Is it just a case of identifying the doctest failures and fixing them?


---

Comment by roed created at 2016-01-26 21:43:10

Agreed.  I think mostly it's a matter of fixing the doctest problems, and then splitting off further problems into followup tickets.  I will try to work on it soon....


---

Comment by chapoton created at 2016-01-27 14:45:14

I have added the authors (please check), so that patchbots can run on this ticket once it is put in needs_review.


---

Comment by chapoton created at 2016-03-06 17:31:45

I put this into needs_review, so that the patchbots can work on it.


---

Comment by chapoton created at 2016-03-06 17:31:51

Changing status from needs_work to needs_review.


---

Comment by wuthrich created at 2016-03-27 13:16:31

New commits:


---

Comment by git created at 2016-04-04 16:48:15

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:


---

Comment by mmasdeu created at 2016-04-04 17:00:19

All doctests pass now, finally! I have also checked for whitespace. There are still things that one can work on, but my feeling is that they should be relegated to other tickets depending on this one. Here is a list of these:

1. The distributions code is embarrassingly slow. It would be drastically improved by having an implementation that uses Sage's integers (no need to use longs here) instead of Qp and Zp.

2. More functions/methods to interact with other implementations of modular symbols could be added. For example, it is straightforward to have a method to construct a Pollack-Stevens modular symbol from a one-dimensional modular symbols space. Such a method exists if one starts from an elliptic curve already.

3. The p-adic L-function returned by this implementation is quite different to what is returned by the current (not overconvergent) implementation. Fixing this involves deciding where the overconvergent lift is done: one needs to know a target precision for this, whereas the non-overconvergent implementation only requires the precision parameter when evaluating a particular term of the series.

4. The normalization of the p-adic L-series is different than the one used in the current implementation. This is noted in the examples, and it can be easy to fix (once this ticket is accepted).

I am sure that there are many other improvements that other people will suggest, but let's first ensure that this ticket doesn't see its 10th birthday.


---

Comment by chapoton created at 2016-04-06 19:52:22

See the latest patchbot report for several failing plugins, that needs to be corrected. And doc does not build.


---

Comment by git created at 2016-04-07 11:52:21

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-04-07 12:40:08

Thanks. But doc still does not build.
The problem is probably here:

```
+        -  ``sign`` - None (default), 0, +1 or -1. If None, choose the default
+        according to the implementation, which currently is 0 for pollack-stevens,
+        and 1 otherwise.
```

where the last two lines should be indented by 2.

You can check that the doc build using something like that

```
sage -docbuild reference/plane_curves html
```



You also used a wrong newstyle doctest continuation, the correct one is `....:`
Please correct.


---

Comment by git created at 2016-04-07 15:58:23

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-04-07 16:03:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmasdeu created at 2016-04-07 16:06:41

<rant>Am I the only one that thinks that this is becoming ridiculous?</rant>


---

Comment by roed created at 2016-04-07 17:45:30

I'm looking at it now Marc.  It is really annoying how many little things come up.


---

Comment by pbruin created at 2016-04-12 19:02:22

I think the following points from comment:16 are still valid:
> - In `sage/modular/all.py`, the `import *` commands may not be what you want; this will all end up in the global namespace.
> - It would be nice to add the new modules to the relevant `src/doc/en/reference/*/index.rst` files, probably with `*` = `modfrm`, `modmisc` and/or `modsym`.


---

Comment by mmasdeu created at 2016-04-13 21:58:32

Peter,

- The import * commands are not added by this ticket, which only concerns .../pollack_stevens and .../btquotients. In sage/modular/all.py we do import everything in btquotients/all.py (and same for pollack_stevens) but this should be fine, since that file contains only the modules that need to be put in the global namespace.

- I am working on the docs now.


---

Comment by pbruin created at 2016-04-13 22:15:46

Hi Marc,
> The import * commands are not added by this ticket, which only concerns .../pollack_stevens and .../btquotients. In sage/modular/all.py we do import everything in btquotients/all.py (and same for pollack_stevens) but this should be fine, since that file contains only the modules that need to be put in the global namespace.
It is actually less bad than I thought, but if I understand the import statements correctly, all of the following will end up in the global namespace:
- `BTQuotient`
- `DoubleCosetReduction`
- `HarmonicCocycleElement`
- `HarmonicCocycles`
- `pAutomorphicFormElement`
- `pAutomorphicForms`
- `PSModularSymbols`
- `Distributions`
- `Symk`
- `ManinRelations`
- `pAdicLseries`
I think most mathematicians who are not specialists in automorphic forms couldn't guess what any of these means, let alone the average Sage user...


---

Comment by mmasdeu created at 2016-04-13 22:25:31

Replying to [comment:51 pbruin]:
> - `BTQuotient`
> - `DoubleCosetReduction` - removed
> - `HarmonicCocycleElement` - removed
> - `HarmonicCocycles`
> - `pAutomorphicFormElement` - removed
> - `pAutomorphicForms`
> - `PSModularSymbols`
> - `Distributions`
> - `Symk`
> - `ManinRelations` - removed
> - `pAdicLseries` - removed
> I think most mathematicians who are not specialists in automorphic forms couldn't guess what any of these means, let alone the average Sage user...
So the new proposed list would be:
- `BTQuotient`
- `HarmonicCocycles`
- `pAutomorphicForms`
- `PSModularSymbols
- `Distributions`
- `Symk`
Would this be more reasonable? Considering that objects like `CrystalOfProjectedLevelZeroLSPaths` is also in the global namespace, I mean. Also, have you seen Magma's global namespace? It doesn't prevent people from using it :-).


---

Comment by pbruin created at 2016-04-13 22:32:10

Replying to [comment:52 mmasdeu]:
> So the new proposed list would be:
> - `BTQuotient`
> - `HarmonicCocycles`
> - `pAutomorphicForms`
> - `PSModularSymbols
> - `Distributions`
> - `Symk`
> Would this be more reasonable? Considering that objects like `CrystalOfProjectedLevelZeroLSPaths` is also in the global namespace, I mean.
This does sound more reasonable, although `Distributions`, `HarmonicCocycles` and `Symk` should definitely get a more descriptive name that makes it clear that they are _p_-adic objects (all of them would make sense in the complex world or in even greater generality).

By the way, I do hope you agree that having something called `CrystalOfProjectedLevelZeroLSPaths` in the global namespace is pretty ridiculous and should be deprecated...
> Also, have you seen Magma's global namespace? It doesn't prevent people from using it :-).
Well, many things are functions in Magma that are methods in Sage, so in principle the global namespace should be cleaner in Sage...

*Edit:* And maybe `pAutomorphicForms` should be called `pAdicAutomorphicForms`?  Also, I guess it would be less cryptic to expand `BT` to `BruhatTits` and `PS` to `PollackStevens`.


---

Comment by mmasdeu created at 2016-04-13 22:41:14

> This does sound more reasonable, although `Distributions`, `HarmonicCocycles` and `Symk` should definitely get a more descriptive name that makes it clear that they are _p_-adic objects (all of them would make sense in the complex world or in even greater generality).

I am renaming HarmonicCocycles to BTHarmonicCocycles, and Distributions to OverconvergentDistributions. The Symk does not need to be p-adic, it's pretty general.

> By the way, I do hope you agree that having something called `CrystalOfProjectedLevelZeroLSPaths` in the global namespace is pretty ridiculous and should be deprecated...

I do agree, but it's quite low in my list of priorities. I'd rather have Sage create an Eichler order in a quaternion algebra...

> *Edit:* And maybe `pAutomorphicForms` should be called `pAdicAutomorphicForms`?  Also, I guess it would be less cryptic to expand `BT` to `BruhatTits` and `PS` to `PollackStevens`.

I agree, too.


---

Comment by git created at 2016-04-13 22:48:41

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-04-13 23:01:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmasdeu created at 2016-04-13 23:02:29

I think it looks good now.


---

Comment by pbruin created at 2016-04-14 09:27:58

OK, thanks!  I still haven't got the time for a real review, unfortunately...


---

Comment by chapoton created at 2016-05-22 20:27:16

needs rebase on latest develop


---

Comment by rws created at 2016-06-14 08:04:09

Changing status from needs_review to needs_work.


---

Comment by wuthrich created at 2016-06-14 12:54:58

I started to work on this a bit.

I will try to merge it. But I also found a lot of things that I am not totally happy with, before that ticket goes in. See below. There is a real danger that this patch-bomb ticket never makes it into sage at this rate. I would be really sorry about this. Here are the possibilities:

 1. One option  would be to split it up: Put the basic code (i.e. the new files) in then in further tickets starts incorporating it into sage step by step.

 2. Another option is to accept it in an incomplete version as soon as it is rebased and doc-test are corrected and then open new tickets. But that means that certain functions will change and deprecation will be all over the place.

 3. We try to fix all issues here slowly and hope this converges in finite time.

Right, option 1 would have been the correct decision at the start but I fear it is too late for this. Marc probably favours 2 and I would prefer 3, I must admit, although I am not sure I can put in the effort needed.


---

Comment by wuthrich created at 2016-06-14 12:56:04

(I am having issues posting. So I will do it in small portions, sorry)

Now here to a list of issues that I spotted this morning.

* I don't think it is a good idea that `m = E.modular_symbol(implementation="pollack-stevens")` gives a completely different type of thing back. It is not even callable. Is it even desirable to have them in the same function. I would have left `modular_symbols` as before and added a `overconvergent_modular_symbols` as a separate method. (Personally, I would revert this function to before and think about it in a next ticket.)


---

Comment by wuthrich created at 2016-06-14 12:56:41

* The normalisation of the p-adic L-function is wrong. One has to divide by the number of real connected components of the elliptic curve. This matters for p=2, otherwise it is a choice of normalisation. But it is better to be consistent with sage.

* If we leave `E.modular_symbol()` as modified here, then it should take eclib as default (as stated in the new docstring). Without having resolved #10256, `ps_modsym_from_elliptic_curve` should take eclib for positive and sage for negative. Or is sage for both a better choice? Certainly much slower. (Again I opt, for keeping as before and use slow sage for overconvergent ms by now)


---

Comment by wuthrich created at 2016-06-14 12:57:23

* The arguments `n` and `prec` in series of the overconvergent p-adic L-functions are not clear to me. They are probably the wrong way around. The new precision should have a default value, also it should have another name, not to confuse it with the precision in T.

* Many functions have incomplete documentations. E.g. no description of what the input arguments mean and what the output means.

If there is anyone else working on this, please let me know. I might not update my changes too often, but I will try to work on these issues over the next two weeks.


---

Comment by wuthrich created at 2016-06-22 19:46:39

Last 10 new commits:


---

Comment by wuthrich created at 2016-06-22 21:11:24

Last 10 new commits:


---

Comment by wuthrich created at 2016-06-22 21:15:27

Thanks Marc, for fixing the last problems and improving the docstrings. A spotted a few last things. Now there is one very last thing that should be changed before this goes in: Please change the title line of pollack_stevens/modsym.py.
I will be running the tests.

I opend a few follow up tickets:

* #20863 : Improve documentation. There are some # mm TODO left. 
* #20864 : The caching of modular_symbols should be modernised and the keyword use_eclib should be dropped
* #20865 : General ticket to ask for improving the code so that the p-adic L-functions are as fast as we could hope for.


---

Comment by chapoton created at 2016-06-23 11:37:45

please take care of using python2/3 compatible print. See patchbot report
(plugin oldstyle_print)

and

https://wiki.sagemath.org/PrintFunction


---

Comment by wuthrich created at 2016-06-23 12:04:01

It only screamed about commented lines. I changed them too.

(I am not sure the bot should tell us it failed when print is wrongly used on comment lines and I am very certain it should say nothing about the "print" apprearing in the middle of a docstring as in "Return the print representation" in `_repr_` )
----
New commits:


---

Comment by chapoton created at 2016-06-23 12:07:52

Indeed, the plugin is not very smart, and should not care about commented lines. Sorry for the noise.


---

Comment by wuthrich created at 2016-06-23 14:48:53

It all compiles fine now and tests all pass. So if that one title line is changed this can be set to positive review.


---

Comment by mmasdeu created at 2016-06-23 15:21:29

Changing status from needs_work to needs_review.


---

Comment by mmasdeu created at 2016-06-23 15:21:29

Done. I have also changed the title in space.py, since the modular symbols in it are not necessarily overconvergent.
----
New commits:


---

Comment by wuthrich created at 2016-06-23 15:53:06

Thanks Marc.

This 9 year old ticket is now done ! Yeah.


---

Comment by wuthrich created at 2016-06-23 15:53:06

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-06-23 17:57:26

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2016-06-23 17:57:26


```
[sagelib-7.3.beta4] [2/7] Cythonizing sage/modular/pollack_stevens/dist.pyx
[sagelib-7.3.beta4] [3/7] Cythonizing sage/numerical/backends/cplex_backend.pyx
[sagelib-7.3.beta4] 
[sagelib-7.3.beta4] Error compiling Cython file:
[sagelib-7.3.beta4] ------------------------------------------------------------
[sagelib-7.3.beta4] ...
[sagelib-7.3.beta4]         if negate:
[sagelib-7.3.beta4]             rmoments = -rmoments
[sagelib-7.3.beta4]         ans._moments = smoments + rmoments
[sagelib-7.3.beta4]         return ans
[sagelib-7.3.beta4] 
[sagelib-7.3.beta4]     cpdef ModuleElement _add_(self, ModuleElement _right):
[sagelib-7.3.beta4]          ^
[sagelib-7.3.beta4] ------------------------------------------------------------
[sagelib-7.3.beta4] 
[sagelib-7.3.beta4] sage/modular/pollack_stevens/dist.pyx:957:10: Signature not compatible with previous declaration
```



---

Comment by mmasdeu created at 2016-06-24 08:46:58

I don't know how to reproduce the above error in my machine. I removed a superfluous import (in dist.pyx and dist.pxd), which I think is unrelated but was giving out warnings while cythonizing. Also, to make the patchbot happy I changed "print" into "string" in some of the docstrings.
----
New commits:


---

Comment by mmasdeu created at 2016-06-24 08:46:58

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2016-06-24 08:50:20

Hello. You should not care about stupid patchbot remarks. Having the patchbot complete
approval is not a requirement, as long as *you* understand why.


---

Comment by mmasdeu created at 2016-06-24 14:41:10

I'm just worried about Volker's remarks, not the patchbot's. Can someone see how to fix the issue (or at least how to reproduce it?). I have looked at the signature in sage/structure/element.pxd and it looks the same as the one used in dist.pyx...


---

Comment by pbruin created at 2016-06-24 16:57:13

Replying to [comment:78 mmasdeu]:
> I'm just worried about Volker's remarks, not the patchbot's. Can someone see how to fix the issue (or at least how to reproduce it?). I have looked at the signature in sage/structure/element.pxd and it looks the same as the one used in dist.pyx...
It must be because of #20740, which is apparently merged in Volker's branch, but is not in the latest beta.


---

Comment by wuthrich created at 2016-06-26 21:34:29

Changing status from needs_review to needs_work.


---

Comment by wuthrich created at 2016-06-26 21:34:29

I think that is right. Even with the updated branch here, when merged into the current develop, there are Error compiling Cython file: dist.pyx.


---

Comment by git created at 2016-06-27 14:05:04

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmasdeu created at 2016-06-27 14:06:14

Changing status from needs_work to needs_review.


---

Comment by mmasdeu created at 2016-06-27 14:06:14

I believe that it works now.


---

Comment by wuthrich created at 2016-06-27 14:27:02

It compiles fine for me. Running the tests now.


---

Comment by wuthrich created at 2016-06-27 15:24:34

Changing status from needs_review to positive_review.


---

Comment by wuthrich created at 2016-06-27 15:24:34

they passed


---

Comment by vbraun created at 2016-06-27 22:52:31

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2016-06-27 22:52:31

Failures on 32-bit:

```
sage -t --long src/sage/modular/btquotients/btquotient.py
**********************************************************************
File "src/sage/modular/btquotients/btquotient.py", line 1502, in sage.modular.btquotients.btquotient.BruhatTitsQuotient._cache_key
Failed example:
    X._cache_key()
Expected:
    1375458358400022881
Got:
    -406423199
**********************************************************************
File "src/sage/modular/btquotients/btquotient.py", line 2478, in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion
Failed example:
    l[3]
Expected:
    [-1]
    [ 0]
    [ 1]
    [ 1]
Got:
    [-1]
    [ 1]
    [ 0]
    [ 1]
**********************************************************************
File "src/sage/modular/btquotients/btquotient.py", line 2483, in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion
Failed example:
    X.embed_quaternion(l[3])
Expected:
    [    O(7) 3 + O(7)]
    [2 + O(7) 6 + O(7)]
Got:
    [4 + O(7)     O(7)]
    [1 + O(7) 2 + O(7)]
**********************************************************************
File "src/sage/modular/btquotients/btquotient.py", line 2487, in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion
Failed example:
    X.embed_quaternion(l[3])
Expected:
    [                7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)             3 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)]
    [            2 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6) 6 + 5*7 + 3*7^2 + 5*7^3 + 2*7^4 + 6*7^5 + O(7^6)]
Got:
    [4 + 5*7 + 3*7^2 + 5*7^3 + 2*7^4 + 6*7^5 + O(7^6)                 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)]
    [            1 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)             2 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)]
**********************************************************************
2 items had failures:
   1 of   3 in sage.modular.btquotients.btquotient.BruhatTitsQuotient._cache_key
   3 of   8 in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion
    [375 tests, 4 failures, 8.18 s]
```



---

Comment by git created at 2016-06-28 12:36:43

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by wuthrich created at 2016-06-28 12:44:44

That is fine by me. Is the first output really random ? Otherwise you can use `# 32-bit` and `# 64-bit` in the doctest.

In any case, I have no means of checking as I don't have access to magma or 32-bit. If someone listening has, they should run the test for us, otherwise we have to bother the release manager again with a "positive review"....


---

Comment by mmasdeu created at 2016-06-28 12:45:36

I fixed the problem with the doctests, plus another bug that arised when using Magma. Tests in btquotients and in pollackstevens pass in my machine.


---

Comment by mmasdeu created at 2016-06-28 12:49:09

The `__cache_key` is not random, but I have put it as it were since it is not of much use. The test done after is more relevant. The embedding functions depend on a call to `pMatrixRing` in Magma, so it would be random, or at least fairly unpredictable.


---

Comment by mmasdeu created at 2016-06-28 12:49:17

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2016-06-28 13:33:00

You can use this:

```
            sage: hash(SR(19.23))
            -1458111714  # 32-bit
            2836855582   # 64-bit
```



---

Comment by git created at 2016-06-28 13:50:23

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmasdeu created at 2016-06-28 13:58:52

I have followed Volker's suggestion. I leave it as needs_review...


---

Comment by wuthrich created at 2016-06-28 17:17:17

To me all tests still pass and I can't check 32-bit or optional magma. So I set this to positive review, fearing of course that a bot or vbraun will find yet another issue.

The patchbot complains about something, but I don't understand it.


---

Comment by wuthrich created at 2016-06-28 17:17:17

Changing status from needs_review to positive_review.


---

Comment by git created at 2016-06-29 11:00:34

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by git created at 2016-06-29 11:00:34

Changing status from positive_review to needs_review.


---

Comment by mmasdeu created at 2016-06-29 11:02:34

I realized that there was one doctest missing in `btquotient.py`. This is fixed now. I'm keeping it as "needs review" and hope that the patchbot is happier now.


---

Comment by wuthrich created at 2016-06-29 11:31:32

Well, you deleted lots of commented code and moved an undocumented function to a place where coverage won't complain about it. I guess this is not the optimal solutions, but one can deal with this in #20863.

Coverage also complains about another missing docstring:


```
SCORE src/sage/schemes/elliptic_curves/padics.py: 92.3% (12 of 13)

Missing doctests:
     * line 72: def _normalize_padic_lseries(self, p, normalize, use_eclib, implementation, precision)
```



---

Comment by git created at 2016-06-29 13:13:21

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmasdeu created at 2016-06-29 13:14:04

I fixed the missing doctest in `padics.py` as well.
----
New commits:


---

Comment by wuthrich created at 2016-06-29 14:36:56

Changing status from needs_review to positive_review.


---

Comment by wuthrich created at 2016-06-29 14:36:56

tests pass.


---

Comment by vbraun created at 2016-06-29 23:05:06

Building the pdf docs fails

```
[docpdf] LaTeX Warning: Hyper reference `sage/modular/pollack_stevens/modsym:sage.modula
[docpdf] r.pollack_stevens.modsym.PSModularSymbolElement' on page 162 undefined on input
[docpdf]  line 13297.
[docpdf] 
[docpdf] [162] [163] [164] [165] [166]
[docpdf] Underfull \hbox (badness 10000) in paragraph at lines 13628--13628
[docpdf] \T1/ptm/m/it/10 char-ac-ter=None\T1/ptm/m/n/10 ,
[docpdf] 
[docpdf] Underfull \hbox (badness 10000) in paragraph at lines 13628--13628
[docpdf] \T1/ptm/m/it/10 use_magma=False\T1/ptm/m/n/10 ,
[docpdf] 
[docpdf] Overfull \hbox (152.67451pt too wide) in paragraph at lines 13629--13630
[docpdf] \T1/ptm/m/n/10 Bases: \T1/pcr/m/n/10 sage.structure.sage_object.SageObject\T1/p
[docpdf] tm/m/n/10 , \T1/pcr/m/n/10 sage.structure.unique_representation.UniqueRepresent
[docpdf] ation 
[docpdf] [167] [168] [169] [170] [171] [172] [173] [174] [175] [176] [177] [178]
[docpdf] Overfull \hbox (152.67451pt too wide) in paragraph at lines 14890--14891
[docpdf] \T1/ptm/m/n/10 Bases: \T1/pcr/m/n/10 sage.structure.sage_object.SageObject\T1/p
[docpdf] tm/m/n/10 , \T1/pcr/m/n/10 sage.structure.unique_representation.UniqueRepresent
[docpdf] ation 
[docpdf] [179] [180] [181]
[docpdf] ! Undefined control sequence.
[docpdf] l.15130 modulo \(p\) is not in \(\FF
[docpdf]                                     _p\):
[docpdf] ? 
[docpdf] ! Emergency stop.
[docpdf] l.15130 modulo \(p\) is not in \(\FF
[docpdf]                                     _p\):
[docpdf] !  ==> Fatal error occurred, no output PDF file produced!
[docpdf] Transcript written on modsym.log.
[docpdf] Makefile:68: recipe for target 'modsym.pdf' failed
```



---

Comment by vbraun created at 2016-06-29 23:05:06

Changing status from positive_review to needs_work.


---

Comment by wuthrich created at 2016-06-30 12:17:09

pdf documentation now build for me.
----
Last 10 new commits:


---

Comment by wuthrich created at 2016-06-30 16:13:07

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2016-07-01 16:57:15

Resolution: fixed
