# Issue 6812: Enumerate integer list up to the action of a Permutation Group

Issue created by migration from https://trac.sagemath.org/ticket/6812

Original creator: nborie

Original creation time: 2009-08-23 07:58:26

Assignee: tbd

CC:  sage-combinat

Keywords: enumaration, integer, list, permutation, group

The goal is to enumerate lists up to the action of a Permutation Group. The final function is generate_list_of_sum(integer) which give all list which sum over all element is the integer.

The module in patch use the orderly generating algorithm. The goal is to select list which are maximals according the lexicographic order.

There is a lot of test on this module( strong_generating_system() are also test indirectly in this module... )

depends on #6647


---

Comment by nborie created at 2009-08-23 08:09:34

Changing component from algebra to combinatorics.


---

Comment by nborie created at 2009-08-23 08:09:34

Changing assignee from tbd to mhansen.


---

Comment by nborie created at 2009-08-25 20:46:11

I fixed some language mistakes. I already tell reviewers that there are probably still some typos, misunderstood or mistakes. I am sorry for that... It's hard!


---

Comment by nborie created at 2009-09-04 11:52:47

Changing status from new to assigned.


---

Comment by nborie created at 2009-09-04 11:52:47

Refactoring : 
-> I move the code in sage/combinat/invariant_ring_perm_gps (advise form Nicolas Thiéry)
-> I implemented a new class InfiniteEnumeratedSet (with category)

There is no a shortcut in sage to IntegerVectorsUptoPermGroup which is a user friendly parent (with hope).
This code stay really strongly connected to the Invariant theory and connected with a the graded algebras of multivariate polynomial view as combination of orbit sum. This really why the code enter this new folder : sage/combinat/invariant_ring_perm_gps (other things have to come here....)


---

Comment by nborie created at 2009-09-04 11:52:47

Changing assignee from mhansen to nborie.


---

Comment by nborie created at 2009-11-22 09:14:47

Changing status from needs_work to needs_review.


---

Comment by AlexGhitza created at 2009-11-22 10:21:55

Changing keywords from "enumaration, integer, list, permutation, group" to "enumeration, integer, list, permutation, group".


---

Comment by SimonKing created at 2010-02-08 19:21:51

Hi!

This is not a review yet, just some remarks.

Indeed it seems to me that the comments and the documentation should be proof read by a native speaker. I am not a native speaker, I'm afraid.

I also suggest to rename some methods. For example, the purpose of "generate_list_of_sum" is not clear from that name:

 * "generate" suggests a process. Therefore, I expected that the method would return an iterator. But in fact, an actual list is returned. A similar statement applies to "get_orbit". Why not simply "orbit"?
 * "list_of_sums" is not clear at all. I mean, there is the notion of "partition", so, there is no reason to describe it as "list of sums". Of course, not all partitions are returned, but representatives for each permutation class of partitions.

So, I think "partition_class_representatives" or slightly less precise "partition_classes" would be clearer.

And "generate_canonicals": The return value is the list of canonical representatives of all children of the input. So, why not "children_representatives" or "canonical_children"?

Best regards, Simon


---

Comment by nborie created at 2010-02-11 18:52:05

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2010-02-11 18:52:05

Hi Simon,

Thank for these advises, I start a new cleanup and will update a better version shortly!


---

Comment by nborie created at 2010-02-19 17:22:43

The patch use now the generic code from Search Forest (breadth_first_search....). So this patch now depends on #8288


---

Comment by nborie created at 2010-02-19 17:22:43

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by nborie created at 2010-02-20 11:19:13

Add a canonical_representative method... This will perhaps help later...


---

Comment by nborie created at 2010-03-05 19:00:22

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2010-06-09 12:38:15

Please apply and look only the last patch...


---

Comment by nborie created at 2010-06-09 12:38:15

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-09-21 15:42:31

This looks very interesting, and I could definitely use it in my research (instead of looping over *all* integer vectors).  A few comments:

The syntax seems rather different than `IntegerVectors`, though; for instance, to access these vectors with a given sum one has to use a fairly awkward notation, instead of something analogous to `IntegerVectors(5,6)` for those sum 5, length 6.  Is it possible to streamline that?  

Also, there is fairly non-idiomatic English in some of the docstrings.  

Finally, you should put your normal name in the "Author" field, instead of your Trac username, since the script which generates contributor lists uses this information directly.

I am sorry that I am not familiar enough with the category framework to properly review this properly, though :(


---

Comment by nborie created at 2010-09-21 16:07:20

Thanks for your remarks,

I am going to open right now a vote for a better name and access to these class of parents on sage-combinat-devel (and you in CC to vote too). 

Feel free to point language mistakes to me! I have to improve my English. Use classical e-mail if you don't want to charge the trac.

Thanks very much, the code will be as much better as it will be used.

Nicolas.


---

Comment by nborie created at 2011-01-19 22:29:10

I cleaned it, try to correct the language with some help and try to integrate previous advises... 

apply trac_6812_integer_vectors_mod_permgroup.patch


---

Comment by nborie created at 2011-02-17 16:00:42

I will clean that after Nicolas (Thiéry) would have review #8288...


---

Comment by nborie created at 2011-02-17 16:00:42

Changing status from needs_review to needs_info.


---

Comment by nborie created at 2011-04-05 14:14:47

Changing status from needs_info to needs_review.


---

Comment by nborie created at 2011-04-05 14:14:47

For this last upload : 

 * Cythonize the is_canonical test
 * Change syntax to have IntegerVectorsModPermgroup(G, sum=n) like IntegerVectors or other
 * Add a very heavy collection of tests in documentation for developers in the cython part

I feel that my code is not very well polished, but I need advises, corrections and comments. Especially, I hope my English is not too much horrible. Flyspell is well configured on my emacs to american but I don't always use the right words. Sorry for that.

Other things, I know the importance to have good tests in the code. But here, as the method `strong_generating_system` is very slow, test the module on any group take a very long time (around 3 seconds per group). I will be happy to get some advise and opinion on what deserve to be launch in doctest, what deserve to be kept in comment inside the code and what deserve to be trashed. Currently, the patch present a lot of tests in comments inside the code. It is perhaps too much (or the tests are not the goods one).


---

Comment by kcrisman created at 2011-04-05 15:14:11

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-04-05 15:14:11

Any reason why you don't just use the tests but with this?

```
sage: long_test() # long time
```

It's too much work to remove all the #s anyway if one wanted to try them out.

I like the splitting things into pyx and not.  Also, any reason not to incorporate the pyx file into the documentation?  

You might want to add a couple examples to the cdef'd functions.  I realize this isn't required, but why not? :) 

What happens when you `list()` one of the infinite classes?  That should raise an error - I feel like we just had something like this somewhere else, but I can't remember where.  Also, you should put an example of how to get elements of the infinite class in the main class, since people may not ever read the documentation for something other than `IntegerVectorsModPermutationGroup`, which is the one intended to be used by people, right?  (It's the only one imported into the global namespace, at any rate.)  For this one, I put 'needs work'.

Finally, you are right about the English; there are a few places where I'm not quite sure what is intended, even.  But that can be fixed.  Keep it up - this will be great!  (And very useful for me once I figure out how to use it correctly in my situation.)


---

Comment by nborie created at 2011-04-05 16:10:52

Thanks a lot for having regarded this...

For # long time, I do not know. I think I will select a subpart of the tests and include them with long time. The developer guide say : "These will not be run regularly during Sage development, but will get run before major releases. No example should take more than about 30 seconds.". Currently, on my three years old macbook, all tests take something like 6 minutes. Especially, there are also # optional - gap_database tests here. I will select some groups and add some tests with long time.

I didn't know we can add pyx file in the doctree, I will add it. I will also add comments on the fact that the is_canonical test is polymorph. I just checked the only thing required is a comparison test:

```
sage: from sage.combinat.enumeration_mod_permgroup import is_canonical
sage: G = PermutationGroup([[(1,2,3,4,5,6)]])
sage: sgs = [map(lambda x: Permutation(x), trans) for trans in G.strong_generating_system()]
sage: is_canonical(sgs, ['c','b','a','b','b','a'])
True
sage: is_canonical(sgs, [3,2,1,2,2,1])
True
```

As string can be compared with `<` and `>`, the function can be also used on such object.

I think that examples in cdef functions aren't required just because one cannot import them in the sage console. Try from file.pyx import <tab>. There is perhaps another way to import them, but I don't know...

For the behavior of list(), I think it is ok. The category framework do the job:

```
sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
sage: list(I)
...
NotImplementedError: infinite list
sage: I = IntegerRange(1,+Infinity, 5)
sage: I
{1, 6, ..}
sage: list(I)
...
NotImplementedError: infinite list
sage: I = InfiniteEnumeratedSets().example()
sage: I
An example of an infinite enumerated set: the non negative integers
sage: list(I)
...
NotImplementedError: infinite list
```


I going to improve the doc of IntegerVectorsModPermutationGroup. You're definitely right and I think it deserves to stay the only entrance point for this module.

Thanks for your comments.


---

Comment by nborie created at 2011-04-08 22:46:01

Ok, I tried to include all previous remarks...

I would say also that it is one of my first time with cython (I don't know if it is very well done...). This version integrate the tests with some with decorators long time.


---

Comment by nborie created at 2011-04-08 22:46:01

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2011-04-09 23:21:58

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2011-04-09 23:21:58

I put a needs work because we must set on sage-combinat-devel if we plan to refactor integer vector as hashable type...

I mainly implement this object to create an algebra whose basis is indexed by orbit_sum of monomial. But CombinatorialFreeModule requires hashable elements as basis keys. There is a choice here and I don't have the language overview to decide such direction.


---

Comment by kcrisman created at 2011-06-04 11:49:20

Just a question, as I've returned to the research where this could be helpful...

I see at [this link](http://combinat.sagemath.org/doc/reference/sage/combinat/integer_vectors_mod_permgroup.html) that this stuff appears to actually be in the combinat branch already?  If so, is it possible that the 'needs work' issue has been resolved?


---

Comment by nborie created at 2011-06-05 22:08:42

As SearchForest as been integrated, let me one or two weeks (and FPSAC...) to finalize this... Stay in the area if you want to give review to this work. Feel free to give some comments, requests or advises especially if you have also use cases on this features.


---

Comment by nborie created at 2011-06-07 15:27:23

I cleaned the imports, I improved a little the documentation...

I am very sorry but it needs a STRONG REVIEW OF ENGLISH. My flyspell is well configured in my emacs but I feel that there are probably some not very well expressed sentences in my documentation. I tried to do my best... About the code, it is strongly tested, there is a lot of tests of consistences with other parts of combinat.


```
nicolas@lancelot:/opt/sage/devel/sage-combinat$ sage -t sage/combinat/integer_vectors_mod_permgroup.py -optional -long
sage -t -optional -long "devel/sage-combinat/sage/combinat/integer_vectors_mod_permgroup.py"
	 [10.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 10.3 seconds
nicolas@lancelot:/opt/sage/devel/sage-combinat$ sage -t sage/combinat/enumeration_mod_permgroup.pyx -optional -long
sage -t -optional -long "devel/sage-combinat/sage/combinat/enumeration_mod_permgroup.pyx"
	 [38.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 38.5 seconds
```


apply trac_6812_integer_vectors_mod_permgroup.patch (only)


---

Comment by nborie created at 2011-06-07 15:27:23

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2011-06-07 17:15:07

It depends on something in the sage combinat queue...


---

Comment by nborie created at 2011-06-07 17:15:07

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2011-06-07 18:51:51

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2011-06-07 18:51:51

Ok, it depends on #10335


```
la pile de patchs est maintenant vide
nicolas@lancelot:/opt/sage/devel/sage-review$ hg qpush
application de trac_10334-permgroup_cleanup-rebase-mh.patch
actuellement à : trac_10334-permgroup_cleanup-rebase-mh.patch
nicolas@lancelot:/opt/sage/devel/sage-review$ hg qpush
application de trac_10335-permgroup_domain-mh.patch
actuellement à : trac_10335-permgroup_domain-mh.patch
nicolas@lancelot:/opt/sage/devel/sage-review$ hg qpush
application de trac_6812_integer_vectors_mod_permgroup.patch
actuellement à : trac_6812_integer_vectors_mod_permgroup.patch
nicolas@lancelot:/opt/sage/devel/sage-review$ sage -b
...
nicolas@lancelot:/opt/sage/devel/sage-review$ sage -t sage/combinat/enumeration_mod_permgroup.pyx 
sage -t  "devel/sage-review/sage/combinat/enumeration_mod_permgroup.pyx"
	 [14.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 14.3 seconds
nicolas@lancelot:/opt/sage/devel/sage-review$ sage -t sage/combinat/integer_vectors_mod_permgroup.py 
sage -t  "devel/sage-review/sage/combinat/integer_vectors_mod_permgroup.py"
	 [5.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.7 seconds
```



---

Comment by nborie created at 2011-06-08 20:26:03

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2011-06-08 20:29:21

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2011-10-16 11:37:33

After a big big rush on thesis finalization, I will try to dealt with this ticket as soon as possible... With all the comments that Karl-Dieter sent to me 4 months ago, I should be able to propose something interesting shortly.


---

Comment by nborie created at 2011-10-16 11:37:33

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2011-10-17 22:16:39

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2011-10-17 22:16:39

The last version should be ready for review.


---

Comment by nborie created at 2011-10-17 22:19:31

please patchbot, 

apply only [attachment:trac_6812_integer_vectors_mod_permgroup.patch]


---

Comment by nborie created at 2011-10-17 22:27:03

Second try for the buildbot:

apply trac_6812_integer_vectors_mod_permgroup.patch


---

Comment by nborie created at 2011-10-17 22:39:36

Ok, it can't apply... I am sick of human dependencies coming from sharing a Mercurial queue... Sorry for all spam!


---

Comment by nborie created at 2011-10-17 22:39:36

Changing status from needs_review to needs_work.


---

Comment by jason created at 2011-10-18 02:35:34

Are you talking about this patch depending on something in the combinat queue?


---

Comment by nborie created at 2011-10-18 07:36:57

Yes, precisely.

All works fine on the queue and I really spent a lot of time on that. But some patches (before me in the queue) and supposed to have the status "Needs review" on the trac make this patch can be apply (typically, file like '\modules_list' or '\doc\bla\foo' are concerned). As It was late in the night and I was tired, realize It doesn't work make me a little angry. Sorry for that.

I will finalize it on a separate branch as much of Sage contributors usually do.


---

Comment by nborie created at 2011-10-18 14:51:57

apply trac_6812_integer_vectors_mod_permgroup.patch


---

Comment by nborie created at 2011-10-18 14:51:57

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2011-10-19 17:42:28

All tests pass with -long and -optinal on the sage-combinat repository. I think the problems come from the two dependencies.


---

Comment by nborie created at 2011-10-19 19:00:32

Why does want the patchbot applies systematically the two patches... Where should I put the following line to make the patchbot remember it permanently ?

apply trac_6812_integer_vectors_mod_permgroup.patch


---

Comment by nborie created at 2011-11-16 21:01:36

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2011-11-16 21:01:36

This deserves a proper refactoring with ClonableIntArray...

A new version is on the way.


---

Comment by SimonKing created at 2012-05-18 14:04:19

Hi Nicolas!

Some questions: When we met in Orsay, we discussed some speed-ups of your code. Are they part of the attached patch? And couldn't one say that _for now_ the patch needs review, and the transition to ClonableIntArray can be done on a different ticket? It would be nice to have the stuff in Sage, finally!


---

Comment by nborie created at 2012-05-18 15:06:35

Yes, it would be very nice to have it in Sage...

The latest version of the patch is in the combinat queue. I didn't touch it for one mounth. However, finalize this patch is one of the things around the top of my todo list. After, the next week (positions application time en France...), the plan is to resubmit a version of the patch handling 0-1 enumeration (using a 'max_part' extra argument like in IntegerVectors and like) and implement the parent also as a QuotientSet with lift and retract method from IntegerVectors.

If no problem come to me before, I will update a new version before the end of the month.


---

Comment by SimonKing created at 2012-05-18 15:25:37

Replying to [comment:47 nborie]:
> 
> The latest version of the patch is in the combinat queue.

That means, including our discussion of last November, I guess.

Could you remind me how I can obtain the current version of the patch?


---

Comment by nborie created at 2012-05-18 15:47:18

Unfortunetly, I can update the last version...

I need to download the 5.0, update the combinat queue and probably rebase my patch...

Possibly, you can have access to it browsing the sources at : http://combinat.sagemath.org/patches/ 

However, I don't know if this latest version can be applied on any version of Sage.


---

Comment by nborie created at 2012-05-18 15:57:10

I am currently donwloading the 5.0 . Florent and Nicolas already make the queue apply on 5.0 .
If you can provide a relatively "small" reviewer patch (including correcting my English), I can promise you to do something this week end. I have no technical or algorithmical problem to finalize this patch. The code is already in my head and I have just to write it down.

Dima visited me last week in Orsay and he is also interested by the enumeration of integer vectors over 0 and 1 modulo the action of a permutation group. I already fixed all the details, just a (possible) rebase and some doctests should be fine before reuplaoding it.

I will begin to compile the 5.0 in 5 minutes...


---

Comment by SimonKing created at 2012-05-18 20:35:16

Replying to [comment:49 nborie]:
> I need to download the 5.0, update the combinat queue and probably rebase my patch...

At least the patch from here smoothly applies to sage-5.0. And since there are only few changes to existing files, I don't think there will be conflicts.

> Possibly, you can have access to it browsing the sources at : http://combinat.sagemath.org/patches/ 

No, I can't. I was searching for "Borie", and all I got was

```
3 weeks ago 	Nicolas Borie 	Guards the refactor of integer vectors and dependencies...
3 weeks ago 	Nicolas Borie 	Some changes for integer vectors
6 weeks ago 	Nicolas Borie 	Move in Series and fold of the import fix made by florent (thanks you one more time!)
6 weeks ago 	Nicolas Borie 	Move in series
7 weeks ago 	Nicolas Borie 	Small changes in integer vector experimental patch
3 months ago 	Nicolas Borie 	Refactoring IntegerVectors using SetFactories...
3 months ago 	Nicolas Borie 	First implementation of Schur/Schubert decomposition for multivariate polynomials
3 months ago 	Nicolas Borie 	First implementation od Schur / Schubert Decomposition of multivariate polynomials
3 months ago 	Nicolas Borie 	Merge
3 months ago 	Nicolas Borie 	Fix two patch in the series (delete a name patch qremoved and replace a name qnewed)
```


Searching for "integer vectors modulo permgroup" (the commit message of the patch) didn't help either.

So, please provide an exact reference.


---

Comment by nborie created at 2012-05-18 21:07:17

From http://combinat.sagemath.org/patches/, I click on "browse" thus the URL become on MY computer : http://combinat.sagemath.org/patches/file/0079d727f7b8 (I don't know about the exadécimal code after file/ ). Here I see a list of all files (patches and the series) in the repository and I click on the good patch. The URL become : 
http://combinat.sagemath.org/patches/file/0079d727f7b8/trac_6812_integer_vectors_mod_permgroup.patch

I don't know if the links will work on your computer. Once you will have this page, click on 'raw', it downloaded the patch from the repository when I tested just 1 minute ago.

I am sorry but I really don't manage the use of this mercurial web interface for repository. And as I said before, I will try to do something in the two days to come..

Currently, I just finish to build Sage and the patch doesn't need rebase for 5.0, I apply and Sage started with errors. This patch currently depends on : refactor_integer_vectors_clonableintarray-nb.patch #-4_7_2 # very experimental
which is just before in the combinat-queue. I will make the patch for 6812 independent shortly.


---

Comment by SimonKing created at 2012-05-18 21:30:57

Great, thank you! To my surprise, there is fuzz 2 for two hunks. But it does apply!


---

Comment by SimonKing created at 2012-05-18 21:33:06

Too bad. Apparently, it has another dependency, namely one that creates the module integer_vector_cython. What are the dependencies?


---

Comment by SimonKing created at 2012-05-18 21:36:13

Replying to [comment:54 SimonKing]:
> What are the dependencies?

Sorry, now I see that you name refactor_integer_vectors_clonableintarray-nb.patch as a dependency. Anyway, if you intend to lift that dependency, I'll just wait the few days until you previde a new patch.


---

Comment by nborie created at 2012-05-18 22:14:40

Yes, I will follow your comments done before... I will propose a new version this week end and the possible ameliorations will be part of separate tickets. The use of Clonable integer array is ok and fine because all is in Sage. For the rest, I will skip the dependencies and place some TODO in the code for further links with the combinat code.


---

Comment by SimonKing created at 2012-05-18 22:22:53

Replying to [comment:56 nborie]:
> I will propose a new version this week end and the possible ameliorations will be part of separate tickets. The use of Clonable integer array is ok and fine because all is in Sage.

Great! And will the Cython stuff we discussed in Paris also be part of that patch?

For the record: I finally re-implemented my algorithm for the computation of fundamental invariants of non-modular invariant rings of finite groups for the special case of permutation groups, using your implementation of orbits. I should have done that earlier. After all, thanks to your work on enumerating orbits, it will probably be a lot faster than my original implementation in Singular (which dealt very inefficiently with orbits).


---

Comment by nborie created at 2012-05-20 09:20:35

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2012-05-20 09:20:35

Ok, here is a last version :

- Including categories of quotient of set and (In)finite enumerated set
- Using the cython data structure based on C array
- Tests of coherences with others features from combinat (Partition, monomials, graphs)
- Handling of 0-1 enumeration (like adjacent matrix of graph)

On this last Patch, all tests pass with --long and --optional for the two new files. I didn't run all tests of Sage but this new feature is orthogonal with other part of Sage. The docbuild produce no warning and the doc looks clean.

To present one other test, here is the way to build all unlabeled graphs over 7 vertices :

```
sage: G = TransitiveGroup(21,38)
sage: G.cardinality() == factorial(7)
True
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: S._cardinality_from_iterator()
1044
```

This module, not optimized for the graphs do that in less than 1 minutes on my 4 years old macbook. As improvement for the future, the code is trivially "parallelizable". But this parallelization should be done on SearchForest and not on this module.

For the reviewer, please be careful with my English. I still try to correct myself as much but I am sure some sentences are not full-sense and there are probably some mistakes that flyspell (and me) didn't catch.

apply trac_6812_integer_vectors_mod_permgroup.patch


---

Attachment


---

Comment by nborie created at 2012-05-20 11:03:03

I just fix an import :

IncreasingIntArray will move from sage.structure.list_clone to sage.structure.list_clone_demo (the patch moving the code is in the combinat queue) and I anticipate this change. All tests should pass on this new version.


---

Comment by nborie created at 2012-05-20 11:04:40

As the patchbot change of mind every time, I had the following :

apply trac_6812_integer_vectors_mod_permgroup.patch


---

Comment by SimonKing created at 2012-05-20 12:42:10

We have

```
    def orbit(self, v):
        assert isinstance(v, (list, ClonableIntArray)), '%s shoud be a Python list or an element of %s'%(v, self)
        try:
            if v.parent() is self:
                return orbit(self._sgs, v)
        except:
            return orbit(self._sgs, self.element_class(self, v, check=False))
```


By consequence, if the input is a clonable int array that belongs to a different parent, None is returned. I think there should better an error be raised.


---

Comment by nborie created at 2012-05-20 13:09:20

Thanks for this comment and for the further to come. There are probably much more things to improve in the current code. I hope the current patch can allow you to play with invariants of permutation groups. However, I won't touch this patch anymore until one or two weeks. I am sorry but I need to prepare important dates for my future. I have an audition Tuesday for an associate professor position in the Faugère'team PolSys and I must focus my work around the preparation of such appointments.

Anyway, I will read all this page once I could come back to this stuff. Feel free to give some comments and commands around this module to improve the code.

the algorithmic details are explain in French in (with some Benchmarks):
http://tel.archives-ouvertes.fr/docs/00/65/67/89/PDF/VD2_BORIE_NICOLAS_07122011.pdf
It is from page 39 to 51. It is in French but pictures should make things easy to understand.


---

Comment by SimonKing created at 2012-05-20 15:04:18

Some more comments:

There should not only be a fast `ClonableIntArray.list()`, but also a fast
`ClonableIntArray.tuple()`: Sometimes, one needs a tuple, not a list, and it
would be awkward and slow to first transfrom the clonable int array into a list
and transform that into a tuple.

I think that could be done here, or do you prefer a different ticket?

You know that my application of your work would be: Compute non-modular
invariant rings of permutation groups. For that purpose, it would be good if
clonable int arrays could be used to define exponent vectors of a monomial. But
that should clearly be on a different ticket.


---

Comment by nborie created at 2012-05-20 16:21:30

> There should not only be a fast `ClonableIntArray.list()`, but also a fast
> `ClonableIntArray.tuple()`: Sometimes, one needs a tuple, not a list, and it
> would be awkward and slow to first transfrom the clonable int array into a list
> and transform that into a tuple.

Added on the todo list... But not mine todo list in fact. Florent Hivert (clone C array structure author) is going to patch his module. I will ask him if he can do something. The conversion to tuple should be implemented on the ClonableArray class in sage/structure/list_clone.pyx and thus we will get the fast conversion by inheritance. If we can optimize the conversion for integer, we will override it on the ClonableIntArray class. To avoid any conflict on merging, I will tell some words to Florent.

> You know that my application of your work would be: Compute non-modular
> invariant rings of permutation groups. For that purpose, it would be good if
> clonable int arrays could be used to define exponent vectors of a monomial. But
> that should clearly be on a different ticket.

Yep, I had to deal the same problem. For information, for the case I managed to compute with symmetric polynomials as homogeneous set of parameter (the powersums polynomials), selecting only the canonical monomials under staircase whose automorphism group is not the whole symmetric group (the orbit sum over G of the monomial is not trivially a symmetric polynomial), the enumeration engine make you find NEW secondary invariants with an average of 70% of chance. So, I can imagine your algorithmic will really save a lot of normal form computation. This rate is ok until 10 variables but falls at 30% for the only case at 14 variables (TransitiveGroup(14,61)) my algorithmic managed to compute. (you can see my algorithmic verbose here http://www.math.u-psud.fr/~borie/papers/14_61.txt)


---

Comment by SimonKing created at 2012-05-20 19:50:44

Out of interest, I am trying to use my algorithm to find fundamental invariants for `TransitiveGroup(14,61)` over the rationals. The main bottleneck is the reduction of orbit sums modulo the previously found fundamental reductions (if the reduction is non-zero then the orbit sum is a new fundamental invariant). For some orbit sums in degree 8, the reduction takes several minutes!


---

Comment by nthiery created at 2012-05-20 20:11:24

Replying to [comment:65 SimonKing]:
> Out of interest, I am trying to use my algorithm to find fundamental invariants for `TransitiveGroup(14,61)` over the rationals. The main bottleneck is the reduction of orbit sums modulo the previously found fundamental reductions (if the reduction is non-zero then the orbit sum is a new fundamental invariant). For some orbit sums in degree 8, the reduction takes several minutes!

Yup. That's the purpose of Nicolas's algorithm: to handle large groups by avoiding such reductions.

Speaking of comparison of algorithms: we just got a Magma license to run systematic benchmarks on our computation server in Orsay in the coming months for Nicolas's paper. We should do this benchmark all together to get the best of all systems/algorithms.


---

Comment by kcrisman created at 2012-05-24 23:17:03

What still needs review here?  Any English help still needed?

A couple points on the built doc:
* Some inconsistency in formatting, e.g. 

```
If sum is an integer, it returns a finite enumerated set containing all integer vectors maximum in their orbit for the lexicographic order and whose entries sum to `sum`.
```

  should pick `sum` or sum, preferably `sum`, I guess?
* Similarly, sometimes there are no links, as in 

```
To get the orbit of any integer vector  under the action of the group, use the method orbit:
```

  but others are indeed hyperlinked.  Might as well get it all done for ease of browsing.
* `last corner case :` should be `last corner case:`
* There are lots of missing periods at ends of sentences.  That is, at the ends of sentences which are not ended by colons, which is fine.


---

Comment by SimonKing created at 2012-05-25 06:51:23

Replying to [comment:67 kcrisman]:
> What still needs review here?  Any English help still needed?

Sorry, I really should have focused on reviewing. Instead, I tried to use the patch in order to provide a better implementation of my algorithm on computing fundamental invariants of non-modular representations of finite groups, in the case of permutation groups.

Yes, the patch basically works (as confirmed by the patch bot). However, I will do some checks: My impression is that the combinat people tend to keep the most recent patch versions in the combinat queue, rather than posting them on trac.

Anyway, the plan is that I provide a reviewer patch. But since I am no native speaker either, some additional help with English is certainly appreciated.


---

Comment by SimonKing created at 2012-05-25 11:55:04

I am puzzled: Is there anything special to do in order to build the combinat documentation? I tried sage -docbuild reference html, but even though integer_vectors_mod_permgroup is part of combinat/index.rst, I don't see it in the resulting documentation.


---

Comment by kcrisman created at 2012-05-25 14:03:15

> I am puzzled: Is there anything special to do in order to build the combinat documentation? I tried sage -docbuild reference html, but even though integer_vectors_mod_permgroup is part of combinat/index.rst, I don't see it in the resulting documentation.
Try `sage -b` first (maybe after touching the file); sometimes I forget to do that.


---

Comment by SimonKing created at 2012-05-25 14:58:04

Replying to [comment:70 kcrisman]:
> Try `sage -b` first (maybe after touching the file);

I had done that. But it seems I was simply stupid. For whatever reason, I did not find the html file, even though it was present. Anyway, I am now reading it...


---

Comment by SimonKing created at 2012-05-25 16:31:55

In the function lex_cmp_partial, I see that the `__getitem__` method of clonable int arrays is called repeatedly. Calling `__getitem__` means: It is tested whether the argument is an integer or a slice, and whether the integer is non-negative and smaller than the length of the array.

I would think that lex_cmp_partial is called very often and is thus time critical, isn't it? Then, one should be a bit more direct: One should test saneness of the argument "`step`" only once, and should then directly access `v1._list[i]` and `v2._list[i]`. After all, v1 and v2 already are cdefined.

I suppose the corresponding change will be part of my reviewer patch, but I'd appreciate if Nicolas would send me a couple of examples, so that I can see whether there is a speed-up.


---

Comment by SimonKing created at 2012-05-25 16:40:11

Still in lex_cmp_partial: If the two list segments are equal, then each pair of items is compared twice, namely:

```
    for i in range(step):
        if v1[i] > v2[i]:
            return 1
        if v1[i] < v2[i]:
            return -1
```

Hence, if they coincide in the first 10 positions and differ in the 11th, then 21 or 22 comparisons are needed to find the bigger vector. But if one does

```
    for i in range(step):
        if v1[i] != v2[i]:
            break
    if i<step:
        if v1[i]<v2[i]:
            return -1
        else:
            return 1
    return 0
```

then only 11 or 12 comparisons are needed.


---

Comment by SimonKing created at 2012-05-25 16:47:26

For example:

```
sage: cython("""
....: def test1(list L1, list L2, int step):
....:     cdef int i
....:     for i in range(step):
....:         if L1[i]>L2[i]:
....:             return 1
....:         if L1[i]<L2[i]:
....:             return -1
....:     return 0
....: def test2(list L1, list L2, int step):
....:     cdef int i
....:     for i in range(step):
....:         if L1[i]!=L2[i]:
....:             break
....:     if i<step:
....:         if L1[i]<L2[i]:
....:             return -1
....:         if L1[i]>L2[i]:
....:             return 1
....:     return 0
....: """)
sage: L1 = [1]*10+[1,2,3,4,5]
sage: L2 = [1]*10+[5,4,3,2,1,0]
sage: test1(L1,L2,9)
0
sage: test2(L1,L2,9)
0
sage: test1(L1,L2,14)
-1
sage: test2(L1,L2,14)
-1
sage: test1(L2,L1,14)
1
sage: test2(L2,L1,14)
1
sage: %timeit test1(L1,L2,14)
625 loops, best of 3: 1.41 µs per loop
sage: %timeit test2(L1,L2,14)
625 loops, best of 3: 872 ns per loop
sage: %timeit test1(L2,L1,14)
625 loops, best of 3: 1.22 µs per loop
sage: %timeit test2(L2,L1,14)
625 loops, best of 3: 976 ns per loop
sage: %timeit test1(L1,L2,10)
625 loops, best of 3: 1.17 µs per loop
sage: %timeit test2(L1,L2,10)
625 loops, best of 3: 872 ns per loop
```

So, it seems to make a small but noticeable difference.


---

Comment by SimonKing created at 2012-05-25 17:19:13

When I see

```
            for child in children:
                if child not in new_to_analyse:
                    new_to_analyse.append(child)
```

in the cpdef function "orbit" in sage.combinat.enumeration_mod_permgroup.pyx, it seems to me that new_to_analyse should rather be a set, not a list, since the containment test "child not in new_to_analyse" works a _lot_ faster on (long) sets than lists.

Create a relatively large set of random ints, and get the corresponding list (unsorted, apparently):

```
sage: S = set(randint(1,20000) for _ in range(5000))
sage: L = list(S)
sage: L[:10]
[16384, 5019, 16203, 8195, 16388, 8197, 16391, 600, 16394, 8204]
```

Now, define one function operating on lists and another operating on sets that add the integers from 0 to 10000 to the list or set - but only if it isn't in the list/set yet.

```
sage: cython("""
....: def test1(list L):
....:     cdef int i
....:     for i in range(10000):
....:         if i not in L:
....:             L.append(i)
....: def test2(set S):
....:     cdef int i
....:     for i in range(10000):
....:         S.add(i)
....: """)
sage: len(L)
4426
sage: %time test1(L)
CPU times: user 2.11 s, sys: 0.00 s, total: 2.12 s
Wall time: 2.12 s
sage: len(L)
12240
```

The operation on the set is so much faster that I'm measuring it with timeit, also taking the time to copy the set (so that the length is preserved when running the loop for the timing):

```
sage: len(S)
4426
sage: %timeit test2(copy(S))
625 loops, best of 3: 1.12 ms per loop
sage: len(S)
4426
```


Hence, the same operation (at least in my proof-of-concept) is roughly 2000 times faster on sets than on lists.

The disadvantage is that the output of orbit() would be in a random order, so that to the very least it has to be sorted in the doc tests. Do you want that the output of orbit() is a sorted list (which would of course be easy to implement)?


---

Comment by nborie created at 2012-05-25 17:56:06

Thanks so much for your comments!!!

I didn't know Cython have a set data structure and YES, deleting the doubles at each step is the right way to take care of automorphism group of the vector, I must have used set!

You already explain to me at Orsay for the getitem with ClonableIntArray, it is an another mistake from me to not having updated the old code with that.

I worked a lot on the algorithmic but I am a poor python/cython programmer. All your detailed comments make me understand what need to be done to produce an efficient code, thanks very much for this didactical approach.

From my point of view, orbit() should return a set and not a list (mathematically and computationally speaking). Sorting it deserve to be only the choice of the user.

I prepare for you some interesting benchmarks. Most of them consists in generating all canonical vectors under staircase for cyclic groups, symmetric groups and some transitive groups if you have installed the optional packages database_gap.


---

Attachment

Function to use for a good k-tests


---

Attachment

Old results of speed


---

Comment by nborie created at 2012-05-25 19:44:01

I just added two files providing a good k-test (especially for invariant theory):

The function to use is: TEST_generation_orbit_sum
The function is in the file: benchmarks_generating_orbit_sum.py

The good tests to run are the following (depending the size you want to test):
 * TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True) (~2 sec)
 * TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True) (~20 sec)
 * TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True) (~3 min)

All the complexity are contained in such examples.

For graphs lovers and the change from list to set, you should use a test including vector with large automorphism group like :

```
sage: G = TransitiveGroup(15,28)          
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: timeit('S._cardinality_from_iterator()')
5 loops, best of 3: 1.3 s per loop
```

This test build the 156 graphs over 6 vertices enumerated up to an isomorphism. And vectors whose entries are 0 or 1 have 'often' large automorphism group.

Comparing the old implementation with Python list (and 2 years of development of Sage), the module is currently 3 or 4 times faster.


---

Comment by SimonKing created at 2012-05-25 19:54:50

Replying to [comment:76 nborie]:
> From my point of view, orbit() should return a set and not a list (mathematically and computationally speaking). Sorting it deserve to be only the choice of the user.

OK. What I had a few minutes ago was: Compute with sets internally and return an ordered list. But if you agree that a set is nicer then I can change it (means: Change the doc tests and the specification of the output).

And thank you for the benchmarks!


---

Comment by SimonKing created at 2012-05-25 20:00:57

There are two problems with the orbit() method:

```
        assert isinstance(v, (list, ClonableIntArray)), '%s shoud be a Python list or an element of %s'%(v, self)
        try:
            if v.parent() is self:
                return orbit(self._sgs, v)
        except:
            return orbit(self._sgs, self.element_class(self, v, check=False))
```

That means that _None_ is returned if v happens to be a ClonableIntArray with a different parent. Shouldn't v be transformed into an element of `self` instead?

And is it really a good idea to convert v into an element of `self` without checking?


---

Comment by SimonKing created at 2012-05-25 20:13:44

Here is orbit() returning None:

```
sage: I =  IntegerVectorsModPermutationGroup(SymmetricGroup(5),5)
sage: J =  IntegerVectorsModPermutationGroup(AlternatingGroup(5),5)
sage: v = J([1,1,1,2,0], check=False)
sage: print I.orbit(v)
None
```



---

Comment by SimonKing created at 2012-05-25 20:33:37

With the patch that I almost finished (not posted yet), I get

```
sage: TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True)
For G be the transitive group number 1 of degree 8
Cardinality of G : 8
  
Cardinality of secondary invariants : 5040
Number of canonical monomials under staircase : 18297
Total time : 1.49698710442
 ------------------------------------- 
(1.4969871044158936, 18297, 8)
sage: TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True)
For G be the transitive group number 1 of degree 9
Cardinality of G : 9
  
Cardinality of secondary invariants : 40320
Number of canonical monomials under staircase : 153974
Total time : 13.5961458683
 ------------------------------------- 
(13.596145868301392, 153974, 9)
sage: TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True)
For G be the transitive group number 1 of degree 10
Cardinality of G : 10
  
Cardinality of secondary invariants : 362880
Number of canonical monomials under staircase : 1452325
Total time : 140.386005878
 ------------------------------------- 
(140.3860058784485, 1452325, 10)
sage: G = TransitiveGroup(15,28)
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: timeit('S._cardinality_from_iterator()')
5 loops, best of 3: 415 ms per loop
```


Without the patch, I get

```
sage: TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True)
For G be the transitive group number 1 of degree 8
Cardinality of G : 8
  
Cardinality of secondary invariants : 5040
Number of canonical monomials under staircase : 18297
Total time : 1.58537387848
 ------------------------------------- 
(1.585373878479004, 18297, 8)
sage: TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True)
For G be the transitive group number 1 of degree 9
Cardinality of G : 9
  
Cardinality of secondary invariants : 40320
Number of canonical monomials under staircase : 153974
Total time : 15.0423038006
 ------------------------------------- 
(15.042303800582886, 153974, 9)
sage: TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True)
For G be the transitive group number 1 of degree 10
Cardinality of G : 10
  
Cardinality of secondary invariants : 362880
Number of canonical monomials under staircase : 1452325
Total time : 162.007292032
 ------------------------------------- 
(162.00729203224182, 1452325, 10)
sage: G = TransitiveGroup(15,28)
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: timeit('S._cardinality_from_iterator()')
5 loops, best of 3: 933 ms per loop
```


So, it is roughly 10% to 50% improvement (even though I am currently still converting the set to sorted lists).


---

Comment by nborie created at 2012-05-25 20:51:21

Replying to [comment:79 SimonKing]:
> There are two problems with the orbit() method:
> {{{
>         assert isinstance(v, (list, ClonableIntArray)), '%s shoud be a Python list or an element of %s'%(v, self)
>         try:
>             if v.parent() is self:
>                 return orbit(self._sgs, v)
>         except:
>             return orbit(self._sgs, self.element_class(self, v, check=False))
> }}}
> That means that _None_ is returned if v happens to be a ClonableIntArray with a different parent. Shouldn't v be transformed into an element of `self` instead?
> 
> And is it really a good idea to convert v into an element of `self` without checking?

Yes, this piece of code is horribly ugly... The point is that the orbit method will work with any integer vector. v doesn't need to be canonical. I don't have a use case but I was thinking it would be more convenient to allow the user to use this method for any integer vector (canonical or not). 

After for safety, I don't know the consequence of such a choice on the lung run.

Anyway, the test is_canonical should be very very much faster than the full expansion of an orbit and a user who want just an orbit can also compute his own function.


---

Comment by SimonKing created at 2012-05-25 21:03:33

Replying to [comment:82 nborie]:
> Yes, this piece of code is horribly ugly... The point is that the orbit method will work with any integer vector. v doesn't need to be canonical. I don't have a use case but I was thinking it would be more convenient to allow the user to use this method for any integer vector (canonical or not). 

Agreed. So, check=False should be fine.

But I do think that the orbit method should try to convert the input vector from a different parent into self, and should certainly not return "None".

> Anyway, the test is_canonical should be very very much faster than the full expansion of an orbit

Of course. The algorithm for is_canonical looks almost the same as the full expansion of an orbit, but if it is in fact non-canonical then the function will return "False" before finishing the computation of the whole orbit.

By the way, I made some further tweaks and am now down to

```
sage: TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True)
For G be the transitive group number 1 of degree 8
Cardinality of G : 8
  
Cardinality of secondary invariants : 5040
Number of canonical monomials under staircase : 18297
Total time : 1.43067121506
 ------------------------------------- 
(1.430671215057373, 18297, 8)
sage: TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True)
For G be the transitive group number 1 of degree 9
Cardinality of G : 9
  
Cardinality of secondary invariants : 40320
Number of canonical monomials under staircase : 153974
Total time : 12.9384939671
 ------------------------------------- 
(12.938493967056274, 153974, 9)
sage: TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True)
For G be the transitive group number 1 of degree 10
Cardinality of G : 10
  
Cardinality of secondary invariants : 362880
Number of canonical monomials under staircase : 1452325
Total time : 134.613152981
 ------------------------------------- 
(134.61315298080444, 1452325, 10)
sage: G = TransitiveGroup(15,28)
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: timeit('S._cardinality_from_iterator()')
5 loops, best of 3: 408 ms per loop
```



---

Comment by nborie created at 2012-05-25 21:27:02

Replying to [comment:83 SimonKing]:
> But I do think that the orbit method should try to convert the input vector from a different parent into self, and should certainly not return "None".

Yes! None is not an option here. It must return a set or raise an error.

> Of course. The algorithm for is_canonical looks almost the same as the full expansion of an orbit, but if it is in fact non-canonical then the function will return "False" before finishing the computation of the whole orbit.

And more than that, there is a king of gardener lemma inside the is_canonical method, the partial_lex comparison cut some branches of the orbit just by reading the first entries.

I also think the change from list to set produce more than x2 speedup, it is probably an exponential optimization, you should try before and after with graphs over 7 vertices :

```
sage: G = TransitiveGroup(21,38)          
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: time S._cardinality_from_iterator()
1044
Time: CPU 128.64 s, Wall: 136.10 s
```

It become to be a large test for this last one. (1044 symmetric matrices of size 7)

A student of Florent Hivert had to master project to parallelize SearchForest. Imagine what such module can need by inheritance... (with possible adaptations according changes of SearchForest)


---

Comment by SimonKing created at 2012-05-25 21:48:20

Without patch

```
sage: G = TransitiveGroup(21,38)
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: %time S._cardinality_from_iterator()
CPU times: user 54.56 s, sys: 0.02 s, total: 54.58 s
Wall time: 54.64 s
1044
```

With patch

```
sage: G = TransitiveGroup(21,38)
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: %time S._cardinality_from_iterator()
CPU times: user 9.36 s, sys: 0.01 s, total: 9.37 s
Wall time: 9.38 s
1044
```

So, yes, it scales well...


---

Comment by SimonKing created at 2012-05-25 22:03:42

Speed-ups and doc fixes


---

Attachment

My patch is posted.

I hesitate to directly give it a positive review, since I somehow think that my patch is not just a reviewer patch (in spite of its name), because it changes the code non-trivially. So, please have a closer look on it!

Apart from the code changes, I went through the doc strings and tried to fix some grammar. But I am not a native speaker - take my changes with a grain of salt...

Apply trac_6812_integer_vectors_mod_permgroup.patch trac_6812_reviewer.patch]


---

Comment by SimonKing created at 2012-05-25 22:11:02

It seems the patch bot didn't get it.

Apply trac_6812_integer_vectors_mod_permgroup.patch trac_6812_reviewer.patch


---

Comment by SimonKing created at 2012-05-26 07:22:36

Fixing a corner case, adding a doc test


---

Attachment

I posted an additional reviewer patch. Namely, in my first patch, I forgot to add a doctest (shame on me), and consequently the code contained a bug: Integer vectores `[1,2,3,1]` and `[1,2,3]` would have compared equal. That' fixed and tested with the second reviewer patch.

For the record: I give a positive review to Nicolas' patch. My first reviewer patch needs review, I believe. The second patch is trivial enough to be considered a "real" reviewer patch.

Apply trac_6812_integer_vectors_mod_permgroup.patch trac_6812_reviewer.patch trac_6812_reviewer2.patch


---

Comment by nborie created at 2012-05-26 07:33:28

I was just double checking everything... You really done a lot of work finally, really much as I expected. My first patch was not so much ready.

As you posted another reviewer patch, once I will test everything, I will perhaps merge the 3 patches into a final one for the release manager.


---

Attachment

I am completely agree with all corrections and improvements provided by the two reviewer patches from Simon. I just merge them into my first proposition.

The current implementation pass all my corner cases around invariant theory. All tests pass, the documentation seems good to me and the code looks ready to go. I give the patch a positive review.

This is a three years old wanted improvement (beginning of my PhD thesis) and Sage changed so much these last three years.... Thanks you Simon for the hours you spent on finalizing this and thanks you Karl for English suggestions/corrections (especially those sent by mail 6 month ago...)

apply trac_6812_integer_vectors_mod_permgroup-final.patch


---

Comment by nborie created at 2012-05-26 08:41:12

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-05-26 15:39:22

I'm adding a very minor review patch for a few issues.  This is an amazing contribution!

Also, can you fix this?

```
# User "sage-combinat script"
```



---

Attachment

Patchbot apply trac_6812_integer_vectors_mod_permgroup-final.patch and trac_6812-reviewer.patch.


---

Comment by nborie created at 2012-05-29 11:38:10

Karl reasonably didn't change the status of the ticket. I definitely agree with his patch which fix a lot of typos. Thanks a lot for this reading and the associated patch which applied smoothly on the previous one.

If needed (or just for convenience), the release manager can ask me merging the two patch, if not

apply trac_6812_integer_vectors_mod_permgroup-final.patch trac_6812-reviewer.patch


---

Comment by jdemeyer created at 2012-06-14 06:37:01

Resolution: fixed


---

Comment by nthiery created at 2012-06-15 20:23:19

Congratulations Nicolas!

And thanks you all for getting this great new feature into Sage.
