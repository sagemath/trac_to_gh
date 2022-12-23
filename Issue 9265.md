# Issue 9265: Remove `CombinatorialClass` from sage.combinat.tableau

Issue created by migration from https://trac.sagemath.org/ticket/9265

Original creator: jbandlow

Original creation time: 2010-06-18 12:24:14

Assignee: sage-combinat

The `CombinatorialClass` class is being deprecated.  See [Sage Combinat Roadmap](http://trac.sagemath.org/sage_trac/wiki/SageCombinatRoadMap) for more information.  This ticket will handle removing this class from sage.combinat.tableau.  See also some discussion of this on [this thread](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/1819418007f5157).


---

Comment by was created at 2010-06-22 04:36:54

Milestone sage-4.4.5 deleted


---

Comment by jbandlow created at 2011-03-14 15:07:42

There is now a patch on the sage-combinat queue, which can be viewed here:

http://combinat.sagemath.org/hgwebdir.cgi/patches/file/tip/trac_9265_tableaux_categories_jb.patch

This needs some slight refactoring to apply to a clean 4.6.2, but anyone interested is very welcome to begin reviewing the patch and recording comments here.  Thanks!


---

Comment by jbandlow created at 2011-05-20 16:59:36

I'm not setting to 'needs review' since #10603 is a dependency and is not finalized. But other than that, it is ready to review in the current state. Comments welcome!


---

Comment by jbandlow created at 2011-08-18 18:36:12

Updated the patch to reflect the discussion [here](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/b7989b8dfdadfed0).


---

Comment by dimpase created at 2012-07-24 11:51:57

Changing status from new to needs_review.


---

Comment by dimpase created at 2012-07-24 11:51:57

needs a (trivial, hopefully) rebase for Sage 5.2.rc0


---

Comment by dimpase created at 2012-07-24 11:52:10

Changing status from needs_review to needs_work.


---

Comment by andrew.mathas created at 2012-07-30 15:35:43

I have rebased Jason's patch so that it apples to 5.2-rc0. I have to rename the patch as trac would not give me permission to delete some one else's patch.

I'll look at 5.2 soonish. The patch probably won't apply cleanly as for trivial reasons (white space) it does not commute with the two patches

trac_5457-symmetric_functions-mz.patch        
trac_12943-skew-partition-construction-bug-ht.patch


---

Comment by andrew.mathas created at 2012-07-30 23:15:40

Changing status from needs_work to needs_review.


---

Comment by andrew.mathas created at 2012-07-30 23:15:40

Patch rebased so that it now applies cleanly to the top of sage 5.2.


---

Comment by saliola created at 2012-08-01 02:25:32

For the patchbot:

Apply: trac_9265_tableaux_categories_am.patch


---

Comment by andrew.mathas created at 2012-08-01 03:02:53

Removed dependencies #10603 and #11314 are they were merged in 4.7 and 5.0, respectively.


---

Comment by andrew.mathas created at 2012-08-08 04:20:14

It looks like the colon after the "Apply" above is confusing the patchbot. So let's try:

Apply trac_9265_tableaux_categories_am.patch


---

Comment by aschilling created at 2012-08-12 22:18:40

Replying to [comment:15 andrew.mathas]:
> It looks like the colon after the "Apply" above is confusing the patchbot. So let's try:
> 
> Apply trac_9265_tableaux_categories_am.patch

Dear Andrew,

I just tried to apply the above patch to a clean version of sage-5.3.beta0 and got a failure

applying trac_9265_tableaux_categories_am.patch
patching file sage/combinat/tableau.py
Hunk #5 FAILED at 260
Hunk #6 succeeded at 268 with fuzz 2 (offset -4 lines).
Hunk #40 FAILED at 4110
2 out of 40 hunks FAILED -- saving rejects to file sage/combinat/tableau.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_9265_tableaux_categories_am.patch

If you do the same, you can look at sage/combinat/tableau.py.rej to see what the conflict is.

Anne


---

Comment by andrew.mathas created at 2012-08-13 07:54:50

Hi Anne,

Thanks for this. I have just uploaded a new version of the patch which applies to the very top of 5.3 (the patch does not commute with #5457, but as it is applied first that doesn't matter).

In a previous version of the patch I (not Jason) had renamed some of the tableaux classes such as

* *Tableaux_n  --> *Tableaux_size
* *Tableaux_p  --> *Tableaux_shape

etc. but the current version does not do this. Personally I think that the name on the right make more sense but I probably shouldn't change this without consulting people first.

Andrew

--

For the patchbot: 

Apply trac_9265_tableaux_categories_am.patch 

--

The patchbot appears to be applying Jason's old patch before the new patch. I don't understand why this is happening but, as far as I can tell, this is why the patchbot is saying that the patch does not apply???


---

Comment by andrew.mathas created at 2012-08-13 08:24:07

As the patchbot was complaining, I just uploaded a new version of the patch which deletes all trailing white space. Probably this is unwise as previously I used to have my editor do this automatically but I found that it meant that I had to rebase my patch all of the time so this will probably cause havoc further down the queue? 

What is the accepted practise here?


---

Comment by aschilling created at 2012-08-13 21:09:56

Replying to [comment:18 andrew.mathas]:
> As the patchbot was complaining, I just uploaded a new version of the patch which deletes all trailing white space. Probably this is unwise as previously I used to have my editor do this automatically but I found that it meant that I had to rebase my patch all of the time so this will probably cause havoc further down the queue? 
> 
> What is the accepted practise here?

Dear Andrew,

Did you actually upload the new version of the patch to the sage-combinat queue? I could not see it there. Usually trailing white spaces should be removed. But please check that the whole queue still applies (by trying hg qpush -a) in case you will post the patch there. If it causes many conflicts, it might be better not to remove them at this point.

Thanks,

Anne


---

Comment by aschilling created at 2012-08-14 02:43:44

Dear Andrew,

Here are a couple of comments on the ticket:

* Please add an extra line after lines 1872 and 3799
* Delete line 3271
* In line 3273 in __getitem__ EXAMPLE: should be replaced by EXAMPLES:: (there is an S and : missing)
* In lines 3491, 3769, 4022, EXAMPLE:: should be replaced by EXAMPLES:: (there is an S missing)
* In line 4029, what is p? Perhaps ``self``?

I think it would be ok if you replaced 

* Tableaux_n --> Tableaux_size
* Tableaux_p --> Tableaux_shape 

This is indeed more descriptive!

Anne


---

Comment by andrew.mathas created at 2012-08-14 12:48:03

Hi Anne,

Sorry for the slow response. As you no doubt worked out I didn't push the previous patch onto the queue. I was avoiding doing this as I thought that moving the patch up in the queue, and rebasing to 5.3, would cause conflicts further down the queue.

Any way, after making in the changes that you suggested above I decided to push the new version onto the queue. I have made all of the changes that you requested. In changing the names of the classes to Tableaux_size etc I went a little further and changed self.n to self.size etc and changed the named arguments to the parent classes, although the old named arguments are still accepted.

Also, when I was fixing up the documentation error in getitem that you found I remembered that I wanted to rewrite getitem so that it supports slices. It turned out that each of the semistandard tableaux parent classes had its own getitem, so I removed all of these and added a generic getitem to the SemistandardTableaux class which supports slices (the method came from my tableaux tuple classes). To make sure that this worked I put all of the doctests from the old getitems into the new generic getitem and then added a few more. To make the new getitem work I also had to add an is_finite method to these classes -- this probably should be implemented in the (In)FiniteEnumeratedSet category, but it is not and I couldn't see were to add this there....

The new patch is both on trac and on the queue.

Andrew

--

For the patchbot:

Apply trac_9265_tableaux_categories_am.patch


---

Comment by aschilling created at 2012-08-15 05:05:38

Hi Andrew,

Thank you for your work on this. I ran sage -testall and got the following doctest failure:


```
sage -t  devel/sage-sf/sage/structure/sage_object.pyx
**********************************************************************
File "/Applications/sage-5.3.beta0/devel/sage-sf/sage/structure/sage_object.pyx", line 1114:
    sage: sage.structure.sage_object.unpickle_all()  # (4s on sage.math, 2011)
Expected:
    doctest:... DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.
    See http://trac.sagemath.org/4260 for details.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_crystals_affine_AffineCrystalFromClassicalAndPromotion_with_category_element_class__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_crystals_tensor_product_CrystalOfTableaux_with_category_element_class__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_crystals_tensor_product_TensorProductOfCrystalsWithGenerators_with_category__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_skew_tableau_SemistandardSkewTableaux_n__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_skew_tableau_SemistandardSkewTableaux_nmu__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_skew_tableau_SemistandardSkewTableaux_p__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_skew_tableau_SemistandardSkewTableaux_pmu__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_skew_tableau_StandardSkewTableaux_n__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_SemistandardTableaux_n__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_SemistandardTableaux_nmu__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_SemistandardTableaux_p__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_SemistandardTableaux_pmu__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_StandardTableaux_n__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_StandardTableaux_partition__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_Tableau_class__.sobj')
     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_Tableaux_n__.sobj')
    doctest:1172: DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.
    See http://trac.sagemath.org/4260 for details.
    Failed:
    _class__sage_combinat_crystals_affine_AffineCrystalFromClassicalAndPromotion_with_category_element_class__.sobj
    _class__sage_combinat_crystals_tensor_product_CrystalOfTableaux_with_category_element_class__.sobj
    _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystalsWithGenerators_with_category__.sobj
    _class__sage_combinat_skew_tableau_SemistandardSkewTableaux_n__.sobj
    _class__sage_combinat_skew_tableau_SemistandardSkewTableaux_nmu__.sobj
    _class__sage_combinat_skew_tableau_SemistandardSkewTableaux_p__.sobj
    _class__sage_combinat_skew_tableau_SemistandardSkewTableaux_pmu__.sobj
    _class__sage_combinat_skew_tableau_StandardSkewTableaux_n__.sobj
    _class__sage_combinat_tableau_SemistandardTableaux_n__.sobj
    _class__sage_combinat_tableau_SemistandardTableaux_nmu__.sobj
    _class__sage_combinat_tableau_SemistandardTableaux_p__.sobj
    _class__sage_combinat_tableau_SemistandardTableaux_pmu__.sobj
    _class__sage_combinat_tableau_StandardTableaux_n__.sobj
    _class__sage_combinat_tableau_StandardTableaux_partition__.sobj
    _class__sage_combinat_tableau_Tableau_class__.sobj
    _class__sage_combinat_tableau_Tableaux_n__.sobj
    Successfully unpickled 571 objects.
    Failed to unpickle 16 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_25
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/anne/.sage/tmp/lolita_4.local-73054/sage_object_85063.py
	 [14.0 s]
```


I suppose this is due to your renaming of the classes. Also, I am not sure, but you might have to put in deprecation warnings if certain parent classes suddenly disappear. The new deprecation syntax is available here http://trac.sagemath.org/sage_trac/ticket/13109.

Best,

Anne


---

Comment by aschilling created at 2012-08-15 05:22:59

Hi again,

When building the docs using 


```
sage -docbuild reference html
```


I got the following warning, which should most likely be fixed


```
/Applications/sage-5.3.beta0/local/lib/python2.7/site-packages/sage/combinat/tableau.py:docstring of sage.combinat.tableau.Tableau.lambda_katabolism:1: WARNING: Inline literal start-string without end-string.
```


Best,

Anne


---

Comment by andrew.mathas created at 2012-08-15 12:49:36

Thanks Anne!

The pickling error confused me no end:) It seems that sage keeps pickles of old objects and then checks that new code is still able to unpickle the saved pickles. One way to fix this error would be be to make a new pickle jar which would remove the references to these renamed classes and presumably solve this problem. Another option would be to include deprecation warnings for all of the old class names -- I am not sure but would this lead to deprecation warnings during the unpickling meaning that these tests would still fail?

I am happy to deprecate all of the old class name if you like, although it does seem a little strange to deprecate classes that were never officially part of sage. Other the other hand, the patch has been around for a while so people may be using the old names in their own code, so it might be worth doing because of this. 

I am happy to defer to your expertise as to what is the best course of action. Please advise.

The doc string error is also a little strange. It is caused by a T'_a in the doc string, but as this is part of a (raw) string I would have thought that sphinx would not have a problem with this... Anyway, I have fixed this by changing T'_a into S_a etc which is more readable anyway.

I won't upload a new patch until I hear back from about the best way to resolve the pickling issues.

Best,
Andrew


---

Comment by andrew.mathas created at 2012-08-15 14:29:41

Hi Anne,

I have discovered the register_unpickle_override function. Using this I have eliminated all but the following four unpickling errors:

    * _class__sage_combinat_crystals_affine_AffineCrystalFromClassicalAndPromotion_with_category_element_class__.sobj
    * _class__sage_combinat_crystals_tensor_product_CrystalOfTableaux_with_category_element_class__.sobj
    * _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystalsWithGenerators_with_category__.sobj
    * _class__sage_combinat_tableau_Tableau_class__.sobj

These error are, I think, all due to the fact that the old Tableau_class has been replaced with the quite different Tableau class. My guess is that the only way to fix these unpicking errors is to update the pickle jar. Is this right? If so, then it probably is not worthwhile including all of the register_unpickle_override statements that I have just inserted. Let me know what you think.

I will upload a patch which fixes the docbuild problem that you mentioned, together with a few typos in the documentation and most of the unpickling problems, but I will hold off deprecation and the four problems above until I hear from you.

Best,

Andrew


---

Comment by aschilling created at 2012-08-15 14:33:24

Hi Andrew,

I sent some comments to you by e-mail.

Anne


---

Comment by andrew.mathas created at 2012-08-16 07:53:29

Thanks for all of these Anne. I have updated the pickles and and added deprecations for all of the old tableaux class names. Perhaps I missed something obvious, but the later turned out to be quite painful as the deprecation scheme does not seem to support deprecation of internal classes -- there is a (one-sided) discussion about what I think goes wrong on sage-devel. I ended up writing dummy function wrappers for the deprecations, which came to about 140 lines of code because of the necessary doctests to keep sage --coverage happy. It would be nice if there was a better way...

Andrew


---

Comment by andrew.mathas created at 2012-08-16 07:54:34

Apply trac_9265_tableaux_categories_am.patch


---

Comment by andrew.mathas created at 2012-08-16 14:53:29

For the patchbot:

Apply trac_9265_tableaux_categories_am.patch


---

Comment by aschilling created at 2012-08-16 18:41:17

Changing keywords from "" to "tableaux, combinatorics".


---

Comment by aschilling created at 2012-08-16 18:43:17

This patch cleans up tableaux in combinatorics. Andrew took over Jason's patch and made all changes we discussed by e-mail. I ran all tests on the new machine in Washington combinat.math.washington.edu and all tests passed.

Positive review!

Anne


---

Comment by andrew.mathas created at 2012-08-17 05:00:11

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2012-08-19 18:36:15

Replying to [comment:18 andrew.mathas]:
> As the patchbot was complaining, I just uploaded a new version of the patch which deletes all trailing white space. Probably this is unwise as previously I used to have my editor do this automatically but I found that it meant that I had to rebase my patch all of the time so this will probably cause havoc further down the queue? 
> 
> What is the accepted practise here?

For the record: removing all trailing white spaces is indeed likely to produce conflicts.
So I usually just make sure in my patch to not introduce new ones (sometimes, I edit the patch directly to remove those that I introduced accidently), and to remove those that are very close to the lines I change anyway.

Now in the case at hand, you currently kind of own the tableau file, since everybody knows that you are working hard on it, and that it is thus not safe playing with it. Then, the potential conflicts are with yourself, so you are free to take whichever course of action which is practical for you. 

Thanks for your work!
                                  Nicolas


---

Comment by jdemeyer created at 2012-08-27 11:56:26

Please fix the commit message, it shouldn't refer to the `[mq]` patch name.


---

Comment by jdemeyer created at 2012-08-27 11:56:26

Changing status from positive_review to needs_work.


---

Comment by andrew.mathas created at 2012-08-27 12:06:36

Commit message fixed.


---

Comment by andrew.mathas created at 2012-08-27 12:06:36

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-08-29 11:41:52

Doctest failure:

```
sage -t  -force_lib devel/sage/sage/combinat/tableau.py
**********************************************************************
File "/release/merger/sage-5.4.beta0/devel/sage-main/sage/combinat/tableau.py", line 4257:
    sage: sage.combinat.tableau.StandardTableaux_partition([2,1])
Expected:
    doctest:1: DeprecationWarning: this class is deprecated. Use StandardTableaux_size instead
    See http://trac.sagemath.org/9265 for details.
    Standard tableaux of shape [2, 1]
Got:
    doctest:1: DeprecationWarning: this class is deprecated. Use StandardTableaux_shape instead
    See http://trac.sagemath.org/9265 for details.
    Standard tableaux of shape [2, 1]
**********************************************************************
```



---

Comment by jdemeyer created at 2012-08-29 11:41:52

Changing status from positive_review to needs_work.


---

Comment by andrew.mathas created at 2012-08-29 12:44:04

Sorry, I uploaded the wrong "new version" of the patch. This one should be OK.

All of the tests pasted for the patchbot (except for the pickles which need to be updated), so I am changing this back to positive review.


---

Comment by andrew.mathas created at 2012-08-29 13:00:53

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-09-03 12:50:58

Resolution: fixed


---

Comment by jdemeyer created at 2012-09-24 07:07:42

This patch badly abuses `assert` and `AssertionError`.  `assert` should not be used for control flow.  An assert checks something which should always be true, a failed assertion is always a bug in the program.

For example:

```
        sage: Tableau([[1],[2,3]])
        Traceback (most recent call last):
        ...
        AssertionError: A tableau must be a list of lists of weakly decreasing length.
```

This is a simple user mistake, for which `assert` is not right.

I think this must be fixed.


---

Comment by nthiery created at 2012-09-24 09:22:33

Hi Jeroen,

Replying to [comment:42 jdemeyer]:
> This patch badly abuses `assert` and `AssertionError`.  `assert` should not be used for control flow.  An assert checks something which should always be true, a failed assertion is always a bug in the program.
> 
> For example:
> {{{
>         sage: Tableau([[1],[2,3]])
>         Traceback (most recent call last):
>         ...
>         AssertionError: A tableau must be a list of lists of weakly decreasing length.
> }}}
> This is a simple user mistake, for which `assert` is not right.
> 
> I think this must be fixed.

There is no control flow involved. It's quite a common public constructor, but speed matters because it's used a lot at a low level in combinatorics calculations. The error message is nice and explicit. Altogether, given the discussion on sage-devel, do we agree that it's ok as such?

Cheers,
                                           Nicolas


---

Comment by jdemeyer created at 2012-09-24 10:01:34

Replying to [comment:43 nthiery]:
> There is no control flow involved. 
I disagree.

```
try:
    ...
except AssertionError:
    ...
```

is certainly control flow.

> It's quite a common public constructor, but speed matters because it's used a lot at a low level in combinatorics calculations.
Are these _constructors_ really that speed-critical?  Of the 3 patches (#9265, #8899, #5457), this one is certainly the worst offender.


---

Comment by jdemeyer created at 2012-09-24 10:08:10

Replying to [comment:43 nthiery]:
> speed matters because it's used a lot at a low level in combinatorics calculations.
If speed matters that much, you could probably get a lot more speedup by using Cython as opposed to less argument checking.


---

Comment by nthiery created at 2012-09-24 11:22:13

Replying to [comment:44 jdemeyer]:
> > There is no control flow involved. 
> I disagree.
> {{{
> try:
>     ...
> except AssertionError:
>     ...
> }}}
> is certainly control flow.

Ouch, that piece? Yes certainly, it's bad and should be fixed, either by using a ValueError, or better by avoiding to feed Tableau with potential garbage.

There is a lot of action going on currently around Tableaux so, to keep things running, I recommend doing that in a later ticket to not delay other stuff.


---

Comment by nthiery created at 2012-09-24 11:26:25

Replying to [comment:45 jdemeyer]:
> > speed matters because it's used a lot at a low level in combinatorics calculations.
> If speed matters that much, you could probably get a lot more speedup by using Cython

Certainly, that's the planned next step in the cleanup of tableaux :-)
And then having checks that can be disabled will really become relevant.


---

Comment by jdemeyer created at 2012-09-24 11:48:42

Replying to [comment:46 nthiery]:
> There is a lot of action going on currently around Tableaux so, to keep things running, I recommend doing that in a later ticket to not delay other stuff.
Good for me, it's just something to keep in mind.


---

Comment by jdemeyer created at 2012-09-24 11:52:28

Replying to [comment:43 nthiery]:
> It's quite a common public constructor, but speed matters because it's used a lot at a low level in combinatorics calculations.
Then I think the best solution is adding a "check" argument to the constructor defaulting to True and doing the expensive checks only when `check` is True.


---

Comment by andrew.mathas created at 2012-09-24 16:44:53

Jason seemed to like these assertions checks, but I agree that are "wrong" -- in fact, they caused me some grief in #13074. I doubt that there will be speed implications in modifying them.

Unfortunately, it may take me a while to fix this as I'm at a conference this week and I don't have a good internet connection.

Andrew


---

Comment by andrew.mathas created at 2012-09-24 19:46:51

Removing assert statements


---

Attachment

...talk written, patch patched.


---

Comment by jdemeyer created at 2012-09-24 20:41:48

Wow, thanks a lot!  Anne or Jason, could any of you do the review please?


---

Comment by aschilling created at 2012-09-25 03:24:45

The patch on the sage-combinat queue looks good to me (which I assume is the same as here).

Anne


---

Comment by andrew.mathas created at 2012-09-25 06:34:25

Replying to [comment:53 aschilling]:
> The patch on the sage-combinat queue looks good to me (which I assume is the same as here).
> 
> Anne

Thanks Anne! Yes, it's the same patch as the one on the queue.
Andrew


---

Comment by jdemeyer created at 2012-10-15 08:06:27

I'm a bit scared by this pickle jar update now that Andrew Mathas admitted on #13072 that he doesn't know how to update the pickle jar.


---

Comment by andrew.mathas created at 2012-10-15 09:07:17

Hi Jeroen,

I did this pickle jar update following detailed instructions that Anne Schilling sent me. What I asked for on #13072 was for *_proper documentation*_ on how to update pickles because I thought that the pickle may not have been applied properly (in fact, everything is fine because I was looking at version 5.3 whereas the updated pickles are in 5.4). As far as I am aware, there is no documentation on how to update the pickle jar, only instructions passed on hand-to-mouth, which IS a problem. For example, this doesn't seem to be covered in the developer guide.

Andrew


---

Comment by vbraun created at 2012-10-15 11:13:32

You are not supposed to update the pickle jar, it is only here to ensure backward compatibility. If at all possible, you should be using the `register_unpickle_override` to work around the change and unpickle into the new class.


---

Comment by andrew.mathas created at 2012-10-17 02:26:58

I have just uploaded the patch_ trac_9265--tableaux_categories_pickles-am.patch _which adds unpickle overrides for most of the old classes that are being deprecated. This fixes all but four of the unpickle problems, however, it does not fix unpickling for _Tableau_class._ I think that because _Tableau_class does not unpickle_ the following four pickles still fail:

 * `sage_combinat_crystals_affine_AffineCrystalFromClassicalAndPromotion_with_category_element_class`
 * `sage_combinat_crystals_tensor_product_CrystalOfTableaux_with_category_element_class`
 * `sage_combinat_crystals_tensor_product_TensorProductOfCrystalsWithGenerators_with_category`
 * `sage_combinat_tableau_Tableau_class`

I have tried to fix the unpickling of Tableau_class using

  `register_unpickle_override('sage.combinat.tableau', 'Tableau_class',  Tableau)`

but this does not work. My guess is that it is not possible to unpickle the deprecated _Tableau_class_ objects using the new _Tableau_ class objects because the underlying classes are too different.

If some one can see how to do this please let me know.


---

Comment by jdemeyer created at 2012-10-17 07:28:38

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2012-10-17 07:28:38

Changing status from closed to new.


---

Comment by jdemeyer created at 2012-10-17 07:28:38

Let's postpone this to sage-5.5 such that the pickling issues can quietly be ironed out.


---

Comment by andrew.mathas created at 2012-10-17 08:44:44

All pickle problems resolved.


---

Comment by andrew.mathas created at 2012-10-17 08:46:49

Changing status from new to needs_review.


---

Attachment

Fixing a typo in a comment


---

Comment by nthiery created at 2012-10-17 14:55:17

Thanks andrew for going the extra mile for backward compatibility!


---

Comment by andrew.mathas created at 2012-10-17 22:32:59

Hi Anne,

Would you mind reviewing the latest update to #9265 so that Jeroen can put in back in the merge queue. It is just a matter of testing that

```
sage -t  devel/sage-sf/sage/structure/sage_object.pyx
```

works. The new patch trac_9265--tableaux_categories_pickles-am.patch is also in the sage-combinat queue and to test it you should use 5.3 as 5.4 has the wrong pickle_jar at present.

Cheers,

Andrew


---

Comment by andrew.mathas created at 2012-10-18 10:44:28

Replying to [comment:64 nthiery]:
> Thanks andrew for going the extra mile for backward compatibility!

Well, I didn't have a lot of choice:) It's a pity (but understandable) that Jeroen bumped the patch out of the 5.4 release an hour before I uploaded the fix as I guess this will play havoc with the sage-combinat queue. I am sure sure how we can guard for different versions of 5.4.? in the queue as "old" pre-releases will have the patch but one current ones won't.


---

Comment by aschilling created at 2012-10-18 17:50:14

Hi Andrew,

I ran all tests and looked at the new patch. It looks fine. All tests pass with sage-5.3, except, but this seems unrelated to your patch and more related to a file by Jeroen Demeyer. Hence I am setting a positive review.

Thanks!

Anne

------------------------------------

sage -t sage/tests/cmdline.py 
sage -t  "devel/sage-combinat/sage/tests/cmdline.py"        
**********************************************************************
File "/Applications/sage-5.3/devel/sage-combinat/sage/tests/cmdline.py", line 99:
    sage: err
Expected:
    ''
Got:
    '---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Applications/sage-5.3/devel/sage-combinat/<ipython console> in <module>()\n\n/Applications/sage-5.3/local/lib/python/site-packages/sage/misc/preparser.pyc in load(filename, globals, attach)\n   1657         else:\n   1658             # Preparse in memory only for speed.\n-> 1659             exec(preparse_file(open(fpath).read()) + "\\n", globals)\n   1660     elif fpath.endswith(\'.spyx\') or fpath.endswith(\'.pyx\'):\n   1661         import interpreter\n\n/Applications/sage-5.3/devel/sage-combinat/<string> in <module>()\n\nAttributeError: Latex instance has no attribute \'add_to_mathjax_avoid_list\'\n'
**********************************************************************
File "/Applications/sage-5.3/devel/sage-combinat/sage/tests/cmdline.py", line 109:
    sage: err
Expected:
    ''
Got:
    '---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Applications/sage-5.3/devel/sage-combinat/<ipython console> in <module>()\n\n/Applications/sage-5.3/local/lib/python/site-packages/sage/misc/preparser.pyc in load(filename, globals, attach)\n   1657         else:\n   1658             # Preparse in memory only for speed.\n-> 1659             exec(preparse_file(open(fpath).read()) + "\\n", globals)\n   1660     elif fpath.endswith(\'.spyx\') or fpath.endswith(\'.pyx\'):\n   1661         import interpreter\n\n/Applications/sage-5.3/devel/sage-combinat/<string> in <module>()\n\nAttributeError: Latex instance has no attribute \'add_to_mathjax_avoid_list\'\n'
**********************************************************************
File "/Applications/sage-5.3/devel/sage-combinat/sage/tests/cmdline.py", line 119:
    sage: err
Expected:
    ''
Got:
    '---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Applications/sage-5.3/devel/sage-combinat/<ipython console> in <module>()\n\n/Applications/sage-5.3/local/lib/python/site-packages/sage/misc/preparser.pyc in load(filename, globals, attach)\n   1657         else:\n   1658             # Preparse in memory only for speed.\n-> 1659             exec(preparse_file(open(fpath).read()) + "\\n", globals)\n   1660     elif fpath.endswith(\'.spyx\') or fpath.endswith(\'.pyx\'):\n   1661         import interpreter\n\n/Applications/sage-5.3/devel/sage-combinat/<string> in <module>()\n\nAttributeError: Latex instance has no attribute \'add_to_mathjax_avoid_list\'\n'
**********************************************************************
1 items had failures:
   3 of 187 in __main__.example_1
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/anne/.sage//tmp/cmdline_49442.py
	 [27.8 s]


---

Comment by aschilling created at 2012-10-18 17:50:33

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2012-10-19 07:15:43

Replying to [comment:66 andrew.mathas]:
> It's a pity (but understandable) that Jeroen bumped the patch out of the 5.4 release an hour before I uploaded the fix as I guess this will play havoc with the sage-combinat queue. I am sure sure how we can guard for different versions of 5.4.? in the queue as "old" pre-releases will have the patch but one current ones won't.

Well, once 5.4 will be out, we will just state that we don't support anymore the beta/rc of 5.4. Only a few of us are using them anyway, so that's anoying but not critical.


---

Comment by andrew.mathas created at 2012-10-20 04:40:55

Thanks Anne


---

Comment by jdemeyer created at 2012-10-29 21:24:32

Resolution: fixed
