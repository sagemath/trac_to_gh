# Issue 9805: Constellations

Issue created by migration from Trac.

Original creator: vdelecroix

Original creation time: 2010-08-26 14:18:20

Assignee: vdelecroix

CC:  vdelecroix slelievre

Keywords: constellation, permutation, surfaces, graphs

A constellation is a combinatorial description (via elements of the symmetric group) of graphs embedded in surfaces (also called G-map). This ticket aims to implement a basic class for it with:
  * fast data type
  * normal form and isomorphism test
  * enumeration/generation with constraints


---

Comment by davidloeffler created at 2011-01-23 11:00:48

Changing component from algebra to combinatorics.


---

Comment by chapoton created at 2012-05-18 12:51:54

I just had a quick look at the code. There are many procedures without documentation and tests. This should be corrected. 

Moreover, near the beginning of the patch, an example is given

```
sage: c = Constellation(['(0,1)', '(0,2)', None])
```

and the syntax is rather unclear. What is the meaning of none ? Why do we need quotes around permutations ?


---

Comment by chapoton created at 2012-06-07 09:15:44

Hello,

The following line appears twice at the beginning:


```
from sage.combinat.partition import Partition 
```



---

Comment by chapoton created at 2012-06-08 19:58:30

Using the latest sage-combinat queue, the doctest coverage is clearly bad :


```
SCORE constellation.py: 25% (18 of 70)
```


And some tests are failing :


```
2 items had failures:
   1 of   5 in __main__.example_0
   2 of   5 in __main__.example_14
***Test Failed*** 3 failures.
```



---

Comment by chapoton created at 2012-06-08 19:58:30

Changing status from new to needs_review.


---

Comment by chapoton created at 2012-06-08 19:59:02

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2012-06-28 09:21:15

Here is a patch with more documentation, but there is still lacking a lot of tests.

I have also corrected the previously failing tests, but now some of the new tests are failing, because the procedures last() and first() do not work !


---

Comment by chapoton created at 2012-07-23 19:50:22

Could you please upload the most recent constellation patch from the sage-combinat queue ? It seems that the version there is not the same, and my review patch does not apply ..


---

Attachment

Replying to [comment:7 chapoton]:
> Could you please upload the most recent constellation patch from the sage-combinat queue ? It seems that the version there is not the same, and my review patch does not apply ..

Done.


---

Comment by chapoton created at 2012-08-28 19:08:47

Apply:

  * [attachment:trac_9806-constellations-vd.patch]
  * [attachment:trac_9806-constellations-doc-patch-fc.patch]


---

Attachment


---

Comment by chapoton created at 2012-09-22 12:30:39

Apply:

trac_9806-constellations-vd.patch 
trac_9806-constellations-doc-patch-fc.patch


---

Comment by chapoton created at 2012-11-09 16:02:05

Apply trac_9806-constellations-vd.patch trac_9806-constellations-doc-patch-fc.patch


---

Comment by chapoton created at 2013-05-20 09:48:33

more clean up

still one failing doctest that I am not able to correct

and of course, coverage is only 60% !


---

Comment by chapoton created at 2013-05-20 20:00:59

coverage 70%


---

Comment by chapoton created at 2013-05-23 18:38:17

coverage 80%


---

Attachment


---

Comment by chapoton created at 2013-05-24 18:59:45

coverage 92 %


---

Comment by vdelecroix created at 2013-05-25 12:05:51

Replying to [comment:16 chapoton]:
> coverage 92 %

Thanks working on doctests !

I would like to split the file in two parts. More precisely, I intend to move the first part (the little functions on permutations) in a file like sage.misc.permutations. What do you think ? Do I have the green light to fold your patch with mine and do the splitting ?

Best,
Vincent


---

Comment by chapoton created at 2013-05-25 12:09:37

Yes, you can fold and split if you want.

And what about removing the Test class ?


---

Comment by chapoton created at 2013-05-30 19:54:11

By the way, could you also solve the failing doctest ? Most likely, I have not been able to figure out what input should be fed to this method..


---

Comment by vdelecroix created at 2013-05-30 20:58:38

Replying to [comment:19 chapoton]:
> By the way, could you also solve the failing doctest ? Most likely, I have not been able to figure out what input should be fed to this method..

I am currently reworking on that ticket. I folded your patch with mine but there are still some code to complete (especially doctests). I hope it will be finished soon.


---

Comment by vdelecroix created at 2013-06-18 06:38:32

apply trac_9806-constellations-all_in_one-vdfc.patch


---

Comment by vdelecroix created at 2013-06-18 11:44:25

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2013-06-18 11:44:25

apply trac_9806-constellations-all_in_one-vdfc.patch


---

Comment by chapoton created at 2013-06-19 08:06:09

documentation is not 100%, see bot report


---

Comment by chapoton created at 2013-06-19 08:06:09

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2013-06-22 20:26:05

in addition to complete the missing doc, 

you should also replace 2 assert statements with some raise statements


---

Comment by chapoton created at 2013-07-05 20:01:53

I have taken care of the assert statements, but there is still a gap in the documentation of perms_canonical_labels


---

Attachment


---

Comment by chapoton created at 2013-07-25 14:38:29

Well, the bot has turned green. Now we can maybe *start* to discuss the content.

I am still not happy with the function "perms_canonical_labels". could you explain what it does, please ?


---

Comment by vdelecroix created at 2013-07-25 16:17:45

Thanks for your corrections.

`perms_canonical_labels` is a way to conjugate a tuple of permutations (s_1,s_2,\ldots,s_k) in such way that two conjugate tuples have the same image under this canonical labeling. The reason is that (as in topological graph) we want to consider isomorphism class of objects. Though, in `Graph/DiGraph` the method is simply named `relabel` and perhaps I should stick to this convention. One advantage here is that this method is very fast (complexity O(n<sup>2</sup>) for a tuple of degree n).

I am starting to use intinsively the patch. And the most interesting part is not yet in there: I am interested in the set of constellations with fixed profile (or passport). In other words, I want to fix the conjugacy classes of all permutations. There is no such parent in the current patch. Note that generating constellations of fixed profile is far less trivial than generating constellations. . We have at least one interesting thing: we know the cardinality of that set via representation theory (Frobenius formula). But I do not know how much the formula is praticable (there is a sum over all characters of the group).


---

Attachment


---

Attachment


---

Comment by vdelecroix created at 2013-09-22 14:30:21

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2013-09-22 14:30:21

apply trac_9806-constellations-all_in_one-vdfc.patch trac_9806_review_fc.patch trac_9806_doc_canonical_labels-vd.patch


---

Comment by chapoton created at 2014-01-04 20:08:55

New commits:


---

Comment by vdelecroix created at 2014-04-08 19:18:46

Rebase on sage-6.2.beta6 and bug corrected in connected_components.
----
New commits:


---

Comment by chapoton created at 2014-05-10 06:56:17

I have made minor corrections, there were unused imports and undefined variables (found using pyflakes)
----
New commits:


---

Comment by git created at 2015-01-21 12:50:18

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-01-21 20:35:44

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2015-01-21 20:44:06

Hello,

Better than pep8 standard, we now have permutations in Sage that start with `0`. The code has to be rewritten using that and not the standalone implementation in `sage.misc.permutation`.

Vincent


---

Comment by vdelecroix created at 2015-01-21 20:44:06

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2015-01-23 12:51:24

Well, great. This was my main problem with this branch. Where are the permutations starting with 0 inside sage ?


---

Comment by vdelecroix created at 2015-01-23 13:07:43

Replying to [comment:41 chapoton]:
> Well, great. This was my main problem with this branch. Where are the permutations starting with 0 inside sage ?


```
sage: S5 = SymmetricGroup(range(5))
sage: S5.an_element()
(0,1,2,3,4)
```


Vincent


---

Comment by git created at 2015-10-28 19:53:17

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-11-20 21:27:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-03-01 11:16:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-03-26 12:07:23

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-03-26 12:09:29

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-03-26 12:10:54

New commits:


---

Comment by git created at 2016-03-26 18:10:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-03-27 08:32:22

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-03-27 13:34:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-03-27 13:37:28

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2016-03-27 13:37:28

I have just done a lot of work on that ticket.

I think this is getting closer to be ready. I would like to have somebody else have a look at that.


---

Comment by git created at 2016-03-27 17:01:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-03-29 18:26:57

Vincent, would you _please_ have a look ?

What should I do with the three remaining functions in permutations.py ? transfer them
back to the constellation file ?


---

Comment by git created at 2016-03-29 19:02:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-03-29 19:13:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2016-03-29 21:59:56

I guess that it makes sense to move the remaining functions from `sage.misc.permutation` inside `constellation.py`.

Since you are now using permutations, I would actually allow any domain. In other words, add a fixed symmetric group attribute to `Constellations`.

When you check matching with the oeis sequence 220754, you can also do that in Sage

```
sage: seq = oeis('A220754')
sage: seq
A220754: Number of ordered triples (a,b,c) of elements of the symmetric group S_n such that the triple a,b,c generates a transitive group.
sage: seq.first_terms()
(1,
 7,
 194,
 12858,
 1647384,
 361351560,
 125116670160,
 64439768489040,
 47159227114392960,
 47285264408385951360,
 63057420721939066617600,
 109118766834521171299756800,
 239996135160204867851157273600,
 659114500480471292127627441484800)
```


The fact that the associated permutation group is transitive is equivalent to the "connectedness". You should either use one or the other.


---

Comment by git created at 2016-03-30 07:47:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-03-30 08:37:13

Replying to [comment:62 vdelecroix]:
> I guess that it makes sense to move the remaining functions from `sage.misc.permutation` inside `constellation.py`.

ok, done

> Since you are now using permutations, I would actually allow any domain. In other words, add a fixed symmetric group attribute to `Constellations`.

maybe for a later ticket ? this one has been waiting for years

> When you check matching with the oeis sequence 220754, you can also do that in Sage
> {{{
> sage: seq = oeis('A220754')
> sage: seq
> A220754: Number of ordered triples (a,b,c) of elements of the symmetric group S_n such that the triple a,b,c generates a transitive group.
> sage: seq.first_terms()
> (1,
>  7,
>  194,
>  12858,
>  1647384,
>  361351560,
>  125116670160,
>  64439768489040,
>  47159227114392960,
>  47285264408385951360,
>  63057420721939066617600,
>  109118766834521171299756800,
>  239996135160204867851157273600,
>  659114500480471292127627441484800)
> }}}

I know. I would prefer not to depend on "optional internet". The current test is good enough.

> The fact that the associated permutation group is transitive is equivalent to the "connectedness". You should either use one or the other.

Sorry, but where is the exact problem you talk about ?


---

Comment by git created at 2016-04-02 09:39:20

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-04-06 19:17:38

Vincent, is the current state good enough for you ?


---

Comment by vdelecroix created at 2016-04-11 01:46:07

The support for any symmetric group was completely broken! Moreover, I double checked and many methods were broken.

You can start the review from the current code. And please keep the code in `perm_X` to work only with list on `0, 1, ..., d-1`.
----
New commits:


---

Comment by git created at 2016-04-11 01:49:49

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2016-04-11 01:55:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-04-11 08:04:47

Hello,

* you need to doctest the two functions that you re-introduced 

* you need to correct the doctest for hash, which is failing on 32-bit machines (see patchbot reports)


---

Comment by chapoton created at 2016-04-11 09:37:32

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2016-04-26 19:06:47

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2016-04-26 19:06:47

New commits:


---

Comment by git created at 2016-04-27 06:49:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-04-27 09:54:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-04-29 19:46:51

vincent, would you like to get this in sage ?


---

Comment by git created at 2016-05-19 12:35:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-05-27 07:57:06

I would like to set this to `positive review`. `@`vdelecroix, do you agree ?


---

Comment by vdelecroix created at 2016-05-27 14:23:05

Yes it looks good.


---

Comment by chapoton created at 2016-05-27 14:25:17

ok, I take this as a green light ot positive review. Thanks.


---

Comment by chapoton created at 2016-05-27 14:25:17

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-05-28 12:13:45

Resolution: fixed
