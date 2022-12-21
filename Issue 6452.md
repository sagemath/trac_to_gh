# Issue 6452: codes over rings

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2009-07-01 01:05:53

Assignee: rlm

CC:  cesarnda@gmail.com dlucas jsrn

This module constructs codes over rings of the form ZZ/mZZ, that is, submodules of FreeModule(IntegerModRing(m), n).
The main authors are Cesar Agustin Garcia-Vazquez (who was an undergrad in Mexico when he wrote this) and Carlos A. Lopez-Andrade (his advisor). I made some changes to make it more consistent with LinearCode. (It still has some hidden differences - the basic problem being that FreeModule has no submodule or span method analogous that of VectorSpace.)

It is in Cython, which I confess I don't really understand well. My role is simply to take Cesar's code (which he emailed to me), tweek it a bit, and create a patch. He has explicitly agreed to distributing it under GPLv2+.


---

Comment by wdj created at 2009-07-01 01:07:07

applies to 4.1.alpha1


---

Attachment

This applies to 4.1.alpha1. This passed sage -testall except for


```
The following tests failed:                                                                             


        sage -t  "devel/sage/doc/fr/tutorial/programming.rst"
        sage -t  "devel/sage/sage/misc/darwin_utilities.pyx" 
Total time for all tests: 6017.1 seconds                     
```

Neither of these failures seem related to this ticket.


---

Comment by AlexGhitza created at 2009-07-11 09:16:17

The patch doesn't contain the crucial file `ring_code.pyx`.  Maybe you forgot to add this file to the hg repository?


---

Comment by wdj created at 2009-10-18 19:49:52

ignore the previous patch; this applies to 4.1.2.rc2


---

Attachment

This latest patch fixes some problems prointed out in private emails from Dan Gordon.


---

Comment by wdj created at 2009-10-18 19:52:43

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2009-10-18 20:00:54

I can also say that the module in coding pass sage -t, with this patch applied, in OS 10.6 on an imac. OS10.6 does not pass sage -testall. However, I do have ubuntu 9.04 32bit installed under vmware on this machine and can test it there if desired.


---

Comment by dgordon created at 2009-10-30 01:46:14

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 07:48:59

Is there any way we can get documentation for the cdef methods as well as possibly some more code comments?  I'm just worried that there's no one who is able to maintain this code.

Also, it's not clear to me that there are not memory leak issues with this code as there are lots of malloc's and only one free.


---

Comment by mhansen created at 2009-10-31 07:48:59

Changing status from positive_review to needs_work.


---

Comment by wdj created at 2009-11-17 00:22:53

If someone can explain to me what those functions will do, I will add comments on them.
As I said, I am basically doing a favor by posting a patch of someone else's code. I had to make a lot of additions to make it consistent with other parts of the codes library, but basically it is Cesar's code. Personally, I really don't understand the cython stuff.

Does this mean that the code will not be accepted?


---

Comment by wdj created at 2009-12-22 12:05:08

Replying to [comment:7 mhansen]:
> Is there any way we can get documentation for the cdef methods as well as 
> possibly some more code comments?  I'm just worried that there's no one who is 
> able to maintain this code.
> 
> Also, it's not clear to me that there are not memory leak issues with this 
> code as there are lots of malloc's and only one free.

As I said, I could try to add comments to the code, but I really don't know cython
nearly well enough to deal with malloc issues.

I've emailed Cesar and not gotten any response about the memory leak issues.

Given that, should the status change to "resolve as won't fix"? That would be too bad since Sage could really use "linear codes" over rings.


---

Comment by vdelecroix created at 2015-09-13 22:49:24

Hello,

I updated a git branch with the patch provided + some corrections. It is not yet in final stage but not far from it!

Vincent
----
New commits:


---

Comment by jsrn created at 2015-09-14 14:58:55

I'm not particularly fond of this patch, I must admit. It doesn't seem very well thought out. I prefer not putting in code which is weak and not thought through, rather than superficially being able to claim that "Sage can do codes over rings". For instance, what can the code actually do right now, besides computing the list of codewords?

Some concrete complaints:

* `gen_mat` should (nowadays) be `generator_matrix`.
* The class has many non-hidden-but-actually-private-and-stupidly-named fields
  `self.codeSet`, `self.minimum`, etc. They should be renamed and start with an underscore.
* `next(self)` is not the way we implement iterators, AFAIK.
* The name `RingCode` is not sensible, since only `ZZ/mZZ` is supported.
* The mathematical object of such a code is a free `ZZ/mZZ` module. Shouldn't
  this be reflected by some parent/category magic in `__init__`?
* `__latex__` is wrong: it says "Linear code".
* English is bad in some texts, e.g. for `length()`, a "the" is missing.
* What's the point of `spanning_codewords`? The nomenclature is not used in
  `LinearCode`, and function just returns the rows of the generator matrix
  anyway.

On a broader design level: I dislike that tons of computation is done at `__init__`, in particular tabulating all codewords. In coding theory stuff that I have been involved in, we have tried very hard to postpone computation until it becomes necessary. In particular, construction should be cheap.

For instance, I think that e.g. the cardinality of such a code can be relatively easily computed without tabulating the entire code.

The design of ring codes should also think the new (well, almost-accepted) `Encoder` and `Decoder` structure into it: #18376, #18813.

Note that I did not run or test the code -- I just looked at it.


---

Comment by vdelecroix created at 2015-09-14 15:55:59

Thanks for having a look. (disclaimer: I actually only ended up here because of [this question on ask](http://ask.sagemath.org/question/29424/liner-code-over-integerring/)).

Replying to [comment:17 jsrn]:
> I'm not particularly fond of this patch, I must admit. It doesn't seem very well thought out. I prefer not putting in code which is weak and not thought through, rather than superficially being able to claim that "Sage can do codes over rings". For instance, what can the code actually do right now, besides computing the list of codewords?

Nothing I guess. But it is already something and it seems to be done efficiently.

> Some concrete complaints:
> 
> * The mathematical object of such a code is a free `ZZ/mZZ` module. Shouldn't
>   this be reflected by some parent/category magic in `__init__`?

Nope. It is not necessarily free. The submodule of `(ZZ/4ZZ)` generated by `2` is *not* free.

> On a broader design level: I dislike that tons of computation is done at `__init__`, in particular tabulating all codewords. In coding theory stuff that I have been involved in, we have tried very hard to postpone computation until it becomes necessary. In particular, construction should be cheap.

I guess it would be reasonable to turn it into a function or method.

> For instance, I think that e.g. the cardinality of such a code can be relatively easily computed without tabulating the entire code.

True. It would basically be equivalent to implement a generalized echelon form for matrices over `ZZ/nZZ` that give you a "pseudo-basis" of submodules of `(ZZ/nZZ)^r`. I have no idea where to find such algorithm.

> The design of ring codes should also think the new (well, almost-accepted) `Encoder` and `Decoder` structure into it: #18376, #18813.

+1
 
> Note that I did not run or test the code -- I just looked at it.

The tests do not pass, but at least some examples run just nicely. Moreover, there was at least one person interested. This is why I thought it would be worse to make it a branch.

Vincent


---

Comment by jsrn created at 2015-09-15 07:33:21

> Nothing I guess. But it is already something and it seems to be done efficiently.

Well, it's perhaps efficient if what you want is to tabulate the entire code and immediately ask it for various stuff (like minimum distance). It's inefficient if you are only interested in some of the properties.

On the other hand, the implementation forces Cython on pretty base functionality. I'm not sure what kind of speed-up Cython brings here as opposed to pure Python -- after all, the actual work is done in finite field arithmetic. It would be interesting to compare and see whether Cython is worth it.

> Nope. It is not necessarily free. The submodule of `(ZZ/4ZZ)` generated by `2` is *not* free.

No of course you're right that it's not -- the word "free" slipped in there by mistake. But it *is* a module.

> I guess it would be reasonable to turn it into a function or method.

Minimum distance and minimum codeword computation should also be extracted from the code tabulation. I might want the list of codewords but not care about the minimum distance, and so computing the hamming weight of all the vectors is a huge waste.

> True. It would basically be equivalent to implement a generalized echelon form for matrices over `ZZ/nZZ` that give you a "pseudo-basis" of submodules of `(ZZ/nZZ)^r`. I have no idea where to find such algorithm.

It's interesting: I'll think more on this. For instance, would the Hermite Normal form be sufficient?

> The tests do not pass, but at least some examples run just nicely. Moreover, there was at least one person interested. This is why I thought it would be worse to make it a branch.

You are right, it would be nice to support codes over `ZZ/mZZ`. I just want to avoid adding stuff that will have to be reformed through a heavy reviewing process just a bit further down the road ;-)


---

Comment by vdelecroix created at 2015-10-02 02:48:35

Replying to [comment:19 jsrn]:
> > True. It would basically be equivalent to implement a generalized echelon form for matrices over `ZZ/nZZ` that give you a "pseudo-basis" of submodules of `(ZZ/nZZ)^r`. I have no idea where to find such algorithm.
> 
> It's interesting: I'll think more on this. For instance, would the Hermite Normal form be sufficient?

I don't think that it is enough to determine the structure. An example of a problem is if `R=ZZ/4ZZ` and a matrix of the form

```
2 * *
0 2 *
0 0 2
```

If you have a vector which is a sum of its row with coefficients `0` or `2` then the leading coefficient vanish... and you lose the nice Hermite form!

But I guess that the Smith normal form would be of more help. If I intrepret correctly what I read, it tells you that any submodule of `R^r` where `R = ZZ/nZZ` is actually of the form `R / (I1) + R / (I2) + ... + R / (Ik)` for some ideals `I1`, ..., `Ik`. These ideals are basically the product `SAT` (which is diagonal) and the decomposition is explicitly given by `T` (my source and notations from [wikipedia](https://en.wikipedia.org/wiki/Smith_normal_form)).


---

Comment by jsrn created at 2015-10-02 22:33:56

I think you're right that the Smith form is exactly what is needed, for the reasons you mention. Ok, so that would be elegant to have in this patch :-)


---

Comment by vdelecroix created at 2015-10-02 22:53:42

All right, I will try to do something. I had a more careful look at the code (and the corresponding master thesis) but I was not able to understand anything. With the Smith form it will also be straightforward to implement a (possibly very efficient) iterator over the elements of the module.

One non trivial point is to decide equality of sub-modules. The only canonical part of the Smith form is the diagonal matrix (which only gives you a hint about isomorphisms between submodules). But I guess that we can somehow echelonize the part corresponding to a given ideal. I would be much more happy with a clean reference...

Since this is more about submodules of `(ZZ/nZZ)^r` I am not sure it should go at all inside `sage.codings`. I would rather put it in `sage.modules`. And (as I already told you), it would be better to factorize more between `sage.modules` and `sage.codings` when the code is *only* given by a generator matrix. So, for the sake of this ticket, my concrete proposal is:
 - implement submodules of `(ZZ/nZZ)^r` with a canonical form
 - have an efficient iterator
If you think it is not too far from the original purpose of this ticket, I will modify the ticket description accordingly.


---

Comment by jsrn created at 2015-10-02 23:12:04

Replying to [comment:22 vdelecroix]:
> All right, I will try to do something. I had a more careful look at the code (and the corresponding master thesis) but I was not able to understand anything. With the Smith form it will also be straightforward to implement a (possibly very efficient) iterator over the elements of the module.

Nice, I didn't consider that.

> One non trivial point is to decide equality of sub-modules. The only canonical part of the Smith form is the diagonal matrix (which only gives you a hint about isomorphisms between submodules). But I guess that we can somehow echelonize the part corresponding to a given ideal. I would be much more happy with a clean reference...
> 
> Since this is more about submodules of `(ZZ/nZZ)^r` I am not sure it should go at all inside `sage.codings`. I would rather put it in `sage.modules`. And (as I already told you), it would be better to factorize more between `sage.modules` and `sage.codings` when the code is *only* given by a generator matrix. So, for the sake of this ticket, my concrete proposal is:
>  - implement submodules of `(ZZ/nZZ)^r` with a canonical form
>  - have an efficient iterator
> If you think it is not too far from the original purpose of this ticket, I will modify the ticket description accordingly.

Such a ticket would definitely make sense. And it seem to cover most of the functionality here (I mean, the minimum distance is right now just exhaustive checking distances...)

The distinction between vector subspaces and linear codes (given only by their generator matrix) is right now that the latter exposes a list of specialised coding theory functions. Such functions might be interesting for non-coding theorists, but probably won't be. That's an argument for having a special class which basically just wraps vector subspaces. Exactly the same argument could be made for submodules of `(ZZ/nZZ)^r`. But no need to get ahead of ourselves here, though...

A different matter: the current patch is Cython. Do we want that? I remember Jeroen's advice to always try Cython only after you have determined that you really need the performance, and that Cython will give this to you.


---

Comment by vdelecroix created at 2015-10-03 00:42:29

Replying to [comment:23 jsrn]:
> Replying to [comment:22 vdelecroix]: 
> A different matter: the current patch is Cython. Do we want that? I remember Jeroen's advice to always try Cython only after you have determined that you really need the performance, and that Cython will give this to you.

Most of it will be in Python. Only the iterator can possibly be in Cython and it should not be more than 20 lines of code. But it makes sense to do it in a second time.


---

Comment by vdelecroix created at 2015-10-04 01:38:50

New commits:


---

Comment by vdelecroix created at 2015-10-04 01:38:50

Changing component from coding theory to linear algebra.


---

Comment by vdelecroix created at 2015-10-04 01:38:50

Changing status from needs_work to needs_review.


---

Comment by git created at 2015-10-04 18:16:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-10-04 18:31:32

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2015-10-04 22:22:44

For the iterator, see #19345


---

Comment by jsrn created at 2015-10-05 00:23:10

Great work Vincent!

Just to be sure: is this "In review"? You made many changes but didn't change the state of "needs review".

I will look at it in detail later, and when I'm sure it's ready. But in any case, some preliminary remarks:

- Could you explain to me (reviewer) the reason for the patch in the category
  files? Something with you using the `Facade` in a previously unthought case.
  Is this related to the `Free`-thing below?

- `FreeModule_ambient_IntegerModRing.span` never uses its `check` argument.

- Since you compute the smith form at construction, then construction is expensive even when nothing is asked of the object afterwards. Is the argument for this that nothing interesting can be said about the module without computing the smith form anyway? Generally, I like construction to be cheap and postponing computation till the user asks it.

Generally, it looks pretty good though.


---

Comment by vdelecroix created at 2015-10-05 01:06:24

Hi,

Replying to [comment:29 jsrn]:
> Great work Vincent!

Thanks ;-)
 
> Just to be sure: is this "In review"? You made many changes but didn't change the state of "needs review".

It is in needs review. After the first commit, it appears that one doctest failed. And then, I found many typos and some better conventions. This is why there are so much commits afterwards. Shortly: it is ready and in needs review.

> I will look at it in detail later, and when I'm sure it's ready. But in any case, some preliminary remarks:
> 
> - Could you explain to me (reviewer) the reason for the patch in the category
>   files? Something with you using the `Facade` in a previously unthought case.
>   Is this related to the `Free`-thing below?

Nope. There is no `TestSuite(U).run()` anywhere for submodules. And this is the reason why.

A facade is a concept from the Sage category. A parent is a facade if its elements do not belong to itself, as for submodules

```
sage: F = FreeModule(ZZ,2)
sage: U = F.span([F((3,0))])
sage: U.an_element().parent() is U
False
sage: U.an_element().parent() is F
True
```

So `U` is a *facade* for `F`. But this is currently not properly done

```
sage: U in Sets().Facade()
False
```

I did it for the submodules over `ZZ/nZZ`. I will fix it later on for the other base rings as well and add some `TestSuite`.

There are many generic tests in category (that are automatically run with the `TestSuite` thing) but some of them do not care about facades. In particulal the `_test_zero` and `_test_one` that I modified.

> - `FreeModule_ambient_IntegerModRing.span` never uses its `check` argument.

True. I did it for compatibility with the other `span` functions. Maybe I could remove it.

> - Since you compute the smith form at construction, then construction is expensive even when nothing is asked of the object afterwards. Is the argument for this that nothing interesting can be said about the module without computing the smith form anyway? Generally, I like construction to be cheap and postponing computation till the user asks it.

Without this nothing can be computed (number of generators, cardinality). Note that I postponed the `_lift` argument computation.


---

Comment by vdelecroix created at 2015-10-05 01:08:51

Note that in the other functions there is a `already_echelonized` function that precisely prevent any computation (assuming that the fed data is in good shape). Perhaps we can add a `already_schmidt_reduced` argument?


---

Comment by vdelecroix created at 2015-10-05 01:56:20

About facade sets, you can read the documentation of `sage.categories.sets_cat.Sets.SubcategoryMethods.Facade`.


---

Comment by vdelecroix created at 2015-10-05 02:01:34

And I just notice that the other submodules are actually *not* facade sets... I should definitely follow the same convention!


---

Comment by vdelecroix created at 2015-10-05 02:01:34

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-10-05 03:37:43

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by vdelecroix created at 2015-10-05 03:39:03

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2015-10-05 03:39:03

Warning: this is a forced push (branch restarted from zero)

Disclaimer: since I had to get rid of facades it did not make sense to just revert all what I did before

Now, no worries about facades... they do not appear anymore. Needs review again.

Vincent


---

Comment by vdelecroix created at 2015-12-07 21:25:32

(ping)


---

Comment by chapoton created at 2016-07-12 09:59:50

there is an old-style print somewhere, see bot report


---

Comment by chapoton created at 2016-07-29 06:59:35

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2019-03-05 10:17:52

Changing status from needs_work to needs_info.


---

Comment by chapoton created at 2019-03-05 10:17:52

New commits:


---

Comment by chapoton created at 2019-03-05 12:52:23

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2019-03-07 20:33:46

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2019-03-07 20:33:46

this need a python3 refreshment, to avoid cmp and long


---

Comment by embray created at 2019-06-14 14:50:27

Tickets still needing working or clarification should be moved to the next release milestone at the soonest (please feel free to revert if you think the ticket is close to being resolved).


---

Comment by embray created at 2019-12-30 14:48:17

Ticket retargeted after milestone closed


---

Comment by mkoeppe created at 2020-04-14 19:41:51

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.


---

Comment by mkoeppe created at 2021-02-13 20:51:01

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.


---

Comment by mkoeppe created at 2021-07-19 00:44:56

Setting a new milestone for this ticket based on a cursory review.
