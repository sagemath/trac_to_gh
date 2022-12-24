# Issue 9265: Remove `CombinatorialClass` from sage.combinat.tableau

archive/issues_009265.json:
```json
{
    "body": "Assignee: sage-combinat\n\nThe `CombinatorialClass` class is being deprecated.  See [Sage Combinat Roadmap](http://trac.sagemath.org/sage_trac/wiki/SageCombinatRoadMap) for more information.  This ticket will handle removing this class from sage.combinat.tableau.  See also some discussion of this on [this thread](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/1819418007f5157).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9265\n\n",
    "created_at": "2010-06-18T12:24:14Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Remove `CombinatorialClass` from sage.combinat.tableau",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9265",
    "user": "jbandlow"
}
```
Assignee: sage-combinat

The `CombinatorialClass` class is being deprecated.  See [Sage Combinat Roadmap](http://trac.sagemath.org/sage_trac/wiki/SageCombinatRoadMap) for more information.  This ticket will handle removing this class from sage.combinat.tableau.  See also some discussion of this on [this thread](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/1819418007f5157).

Issue created by migration from https://trac.sagemath.org/ticket/9265





---

archive/issue_comments_087202.json:
```json
{
    "body": "Milestone sage-4.4.5 deleted",
    "created_at": "2010-06-22T04:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87202",
    "user": "was"
}
```

Milestone sage-4.4.5 deleted



---

archive/issue_comments_087203.json:
```json
{
    "body": "There is now a patch on the sage-combinat queue, which can be viewed here:\n\nhttp://combinat.sagemath.org/hgwebdir.cgi/patches/file/tip/trac_9265_tableaux_categories_jb.patch\n\nThis needs some slight refactoring to apply to a clean 4.6.2, but anyone interested is very welcome to begin reviewing the patch and recording comments here.  Thanks!",
    "created_at": "2011-03-14T15:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87203",
    "user": "jbandlow"
}
```

There is now a patch on the sage-combinat queue, which can be viewed here:

http://combinat.sagemath.org/hgwebdir.cgi/patches/file/tip/trac_9265_tableaux_categories_jb.patch

This needs some slight refactoring to apply to a clean 4.6.2, but anyone interested is very welcome to begin reviewing the patch and recording comments here.  Thanks!



---

archive/issue_comments_087204.json:
```json
{
    "body": "I'm not setting to 'needs review' since #10603 is a dependency and is not finalized. But other than that, it is ready to review in the current state. Comments welcome!",
    "created_at": "2011-05-20T16:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87204",
    "user": "jbandlow"
}
```

I'm not setting to 'needs review' since #10603 is a dependency and is not finalized. But other than that, it is ready to review in the current state. Comments welcome!



---

archive/issue_comments_087205.json:
```json
{
    "body": "Updated the patch to reflect the discussion [here](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/b7989b8dfdadfed0).",
    "created_at": "2011-08-18T18:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87205",
    "user": "jbandlow"
}
```

Updated the patch to reflect the discussion [here](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/b7989b8dfdadfed0).



---

archive/issue_comments_087206.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-07-24T11:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87206",
    "user": "dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087207.json:
```json
{
    "body": "needs a (trivial, hopefully) rebase for Sage 5.2.rc0",
    "created_at": "2012-07-24T11:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87207",
    "user": "dimpase"
}
```

needs a (trivial, hopefully) rebase for Sage 5.2.rc0



---

archive/issue_comments_087208.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-07-24T11:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87208",
    "user": "dimpase"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087209.json:
```json
{
    "body": "I have rebased Jason's patch so that it apples to 5.2-rc0. I have to rename the patch as trac would not give me permission to delete some one else's patch.\n\nI'll look at 5.2 soonish. The patch probably won't apply cleanly as for trivial reasons (white space) it does not commute with the two patches\n\ntrac_5457-symmetric_functions-mz.patch        \ntrac_12943-skew-partition-construction-bug-ht.patch",
    "created_at": "2012-07-30T15:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87209",
    "user": "andrew.mathas"
}
```

I have rebased Jason's patch so that it apples to 5.2-rc0. I have to rename the patch as trac would not give me permission to delete some one else's patch.

I'll look at 5.2 soonish. The patch probably won't apply cleanly as for trivial reasons (white space) it does not commute with the two patches

trac_5457-symmetric_functions-mz.patch        
trac_12943-skew-partition-construction-bug-ht.patch



---

archive/issue_comments_087210.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-07-30T23:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87210",
    "user": "andrew.mathas"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087211.json:
```json
{
    "body": "Patch rebased so that it now applies cleanly to the top of sage 5.2.",
    "created_at": "2012-07-30T23:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87211",
    "user": "andrew.mathas"
}
```

Patch rebased so that it now applies cleanly to the top of sage 5.2.



---

archive/issue_comments_087212.json:
```json
{
    "body": "For the patchbot:\n\nApply: trac_9265_tableaux_categories_am.patch",
    "created_at": "2012-08-01T02:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87212",
    "user": "saliola"
}
```

For the patchbot:

Apply: trac_9265_tableaux_categories_am.patch



---

archive/issue_comments_087213.json:
```json
{
    "body": "Removed dependencies #10603 and #11314 are they were merged in 4.7 and 5.0, respectively.",
    "created_at": "2012-08-01T03:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87213",
    "user": "andrew.mathas"
}
```

Removed dependencies #10603 and #11314 are they were merged in 4.7 and 5.0, respectively.



---

archive/issue_comments_087214.json:
```json
{
    "body": "It looks like the colon after the \"Apply\" above is confusing the patchbot. So let's try:\n\nApply trac_9265_tableaux_categories_am.patch",
    "created_at": "2012-08-08T04:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87214",
    "user": "andrew.mathas"
}
```

It looks like the colon after the "Apply" above is confusing the patchbot. So let's try:

Apply trac_9265_tableaux_categories_am.patch



---

archive/issue_comments_087215.json:
```json
{
    "body": "Replying to [comment:15 andrew.mathas]:\n> It looks like the colon after the \"Apply\" above is confusing the patchbot. So let's try:\n> \n> Apply trac_9265_tableaux_categories_am.patch\n\nDear Andrew,\n\nI just tried to apply the above patch to a clean version of sage-5.3.beta0 and got a failure\n\napplying trac_9265_tableaux_categories_am.patch\npatching file sage/combinat/tableau.py\nHunk #5 FAILED at 260\nHunk #6 succeeded at 268 with fuzz 2 (offset -4 lines).\nHunk #40 FAILED at 4110\n2 out of 40 hunks FAILED -- saving rejects to file sage/combinat/tableau.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_9265_tableaux_categories_am.patch\n\nIf you do the same, you can look at sage/combinat/tableau.py.rej to see what the conflict is.\n\nAnne",
    "created_at": "2012-08-12T22:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87215",
    "user": "aschilling"
}
```

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

archive/issue_comments_087216.json:
```json
{
    "body": "Hi Anne,\n\nThanks for this. I have just uploaded a new version of the patch which applies to the very top of 5.3 (the patch does not commute with #5457, but as it is applied first that doesn't matter).\n\nIn a previous version of the patch I (not Jason) had renamed some of the tableaux classes such as\n\n* *Tableaux_n  --> *Tableaux_size\n* *Tableaux_p  --> *Tableaux_shape\n\netc. but the current version does not do this. Personally I think that the name on the right make more sense but I probably shouldn't change this without consulting people first.\n\nAndrew\n\n--\n\nFor the patchbot: \n\nApply trac_9265_tableaux_categories_am.patch \n\n--\n\nThe patchbot appears to be applying Jason's old patch before the new patch. I don't understand why this is happening but, as far as I can tell, this is why the patchbot is saying that the patch does not apply???",
    "created_at": "2012-08-13T07:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87216",
    "user": "andrew.mathas"
}
```

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

archive/issue_comments_087217.json:
```json
{
    "body": "As the patchbot was complaining, I just uploaded a new version of the patch which deletes all trailing white space. Probably this is unwise as previously I used to have my editor do this automatically but I found that it meant that I had to rebase my patch all of the time so this will probably cause havoc further down the queue? \n\nWhat is the accepted practise here?",
    "created_at": "2012-08-13T08:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87217",
    "user": "andrew.mathas"
}
```

As the patchbot was complaining, I just uploaded a new version of the patch which deletes all trailing white space. Probably this is unwise as previously I used to have my editor do this automatically but I found that it meant that I had to rebase my patch all of the time so this will probably cause havoc further down the queue? 

What is the accepted practise here?



---

archive/issue_comments_087218.json:
```json
{
    "body": "Replying to [comment:18 andrew.mathas]:\n> As the patchbot was complaining, I just uploaded a new version of the patch which deletes all trailing white space. Probably this is unwise as previously I used to have my editor do this automatically but I found that it meant that I had to rebase my patch all of the time so this will probably cause havoc further down the queue? \n> \n> What is the accepted practise here?\n\nDear Andrew,\n\nDid you actually upload the new version of the patch to the sage-combinat queue? I could not see it there. Usually trailing white spaces should be removed. But please check that the whole queue still applies (by trying hg qpush -a) in case you will post the patch there. If it causes many conflicts, it might be better not to remove them at this point.\n\nThanks,\n\nAnne",
    "created_at": "2012-08-13T21:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87218",
    "user": "aschilling"
}
```

Replying to [comment:18 andrew.mathas]:
> As the patchbot was complaining, I just uploaded a new version of the patch which deletes all trailing white space. Probably this is unwise as previously I used to have my editor do this automatically but I found that it meant that I had to rebase my patch all of the time so this will probably cause havoc further down the queue? 
> 
> What is the accepted practise here?

Dear Andrew,

Did you actually upload the new version of the patch to the sage-combinat queue? I could not see it there. Usually trailing white spaces should be removed. But please check that the whole queue still applies (by trying hg qpush -a) in case you will post the patch there. If it causes many conflicts, it might be better not to remove them at this point.

Thanks,

Anne



---

archive/issue_comments_087219.json:
```json
{
    "body": "Dear Andrew,\n\nHere are a couple of comments on the ticket:\n\n* Please add an extra line after lines 1872 and 3799\n* Delete line 3271\n* In line 3273 in __getitem__ EXAMPLE: should be replaced by EXAMPLES:: (there is an S and : missing)\n* In lines 3491, 3769, 4022, EXAMPLE:: should be replaced by EXAMPLES:: (there is an S missing)\n* In line 4029, what is p? Perhaps ``self``?\n\nI think it would be ok if you replaced \n\n* Tableaux_n --> Tableaux_size\n* Tableaux_p --> Tableaux_shape \n\nThis is indeed more descriptive!\n\nAnne",
    "created_at": "2012-08-14T02:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87219",
    "user": "aschilling"
}
```

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

archive/issue_comments_087220.json:
```json
{
    "body": "Hi Anne,\n\nSorry for the slow response. As you no doubt worked out I didn't push the previous patch onto the queue. I was avoiding doing this as I thought that moving the patch up in the queue, and rebasing to 5.3, would cause conflicts further down the queue.\n\nAny way, after making in the changes that you suggested above I decided to push the new version onto the queue. I have made all of the changes that you requested. In changing the names of the classes to Tableaux_size etc I went a little further and changed self.n to self.size etc and changed the named arguments to the parent classes, although the old named arguments are still accepted.\n\nAlso, when I was fixing up the documentation error in getitem that you found I remembered that I wanted to rewrite getitem so that it supports slices. It turned out that each of the semistandard tableaux parent classes had its own getitem, so I removed all of these and added a generic getitem to the SemistandardTableaux class which supports slices (the method came from my tableaux tuple classes). To make sure that this worked I put all of the doctests from the old getitems into the new generic getitem and then added a few more. To make the new getitem work I also had to add an is_finite method to these classes -- this probably should be implemented in the (In)FiniteEnumeratedSet category, but it is not and I couldn't see were to add this there....\n\nThe new patch is both on trac and on the queue.\n\nAndrew\n\n--\n\nFor the patchbot:\n\nApply trac_9265_tableaux_categories_am.patch",
    "created_at": "2012-08-14T12:48:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87220",
    "user": "andrew.mathas"
}
```

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

archive/issue_comments_087221.json:
```json
{
    "body": "Hi Andrew,\n\nThank you for your work on this. I ran sage -testall and got the following doctest failure:\n\n\n```\nsage -t  devel/sage-sf/sage/structure/sage_object.pyx\n**********************************************************************\nFile \"/Applications/sage-5.3.beta0/devel/sage-sf/sage/structure/sage_object.pyx\", line 1114:\n    sage: sage.structure.sage_object.unpickle_all()  # (4s on sage.math, 2011)\nExpected:\n    doctest:... DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.\n    See http://trac.sagemath.org/4260 for details.\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_crystals_affine_AffineCrystalFromClassicalAndPromotion_with_category_element_class__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_crystals_tensor_product_CrystalOfTableaux_with_category_element_class__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_crystals_tensor_product_TensorProductOfCrystalsWithGenerators_with_category__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_skew_tableau_SemistandardSkewTableaux_n__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_skew_tableau_SemistandardSkewTableaux_nmu__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_skew_tableau_SemistandardSkewTableaux_p__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_skew_tableau_SemistandardSkewTableaux_pmu__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_skew_tableau_StandardSkewTableaux_n__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_SemistandardTableaux_n__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_SemistandardTableaux_nmu__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_SemistandardTableaux_p__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_SemistandardTableaux_pmu__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_StandardTableaux_n__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_StandardTableaux_partition__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_Tableau_class__.sobj')\n     * unpickle failure: load('/Users/anne/.sage/temp/lolita_4.local/85064/dir_2/pickle_jar/_class__sage_combinat_tableau_Tableaux_n__.sobj')\n    doctest:1172: DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.\n    See http://trac.sagemath.org/4260 for details.\n    Failed:\n    _class__sage_combinat_crystals_affine_AffineCrystalFromClassicalAndPromotion_with_category_element_class__.sobj\n    _class__sage_combinat_crystals_tensor_product_CrystalOfTableaux_with_category_element_class__.sobj\n    _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystalsWithGenerators_with_category__.sobj\n    _class__sage_combinat_skew_tableau_SemistandardSkewTableaux_n__.sobj\n    _class__sage_combinat_skew_tableau_SemistandardSkewTableaux_nmu__.sobj\n    _class__sage_combinat_skew_tableau_SemistandardSkewTableaux_p__.sobj\n    _class__sage_combinat_skew_tableau_SemistandardSkewTableaux_pmu__.sobj\n    _class__sage_combinat_skew_tableau_StandardSkewTableaux_n__.sobj\n    _class__sage_combinat_tableau_SemistandardTableaux_n__.sobj\n    _class__sage_combinat_tableau_SemistandardTableaux_nmu__.sobj\n    _class__sage_combinat_tableau_SemistandardTableaux_p__.sobj\n    _class__sage_combinat_tableau_SemistandardTableaux_pmu__.sobj\n    _class__sage_combinat_tableau_StandardTableaux_n__.sobj\n    _class__sage_combinat_tableau_StandardTableaux_partition__.sobj\n    _class__sage_combinat_tableau_Tableau_class__.sobj\n    _class__sage_combinat_tableau_Tableaux_n__.sobj\n    Successfully unpickled 571 objects.\n    Failed to unpickle 16 objects.\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_25\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/anne/.sage/tmp/lolita_4.local-73054/sage_object_85063.py\n\t [14.0 s]\n```\n\n\nI suppose this is due to your renaming of the classes. Also, I am not sure, but you might have to put in deprecation warnings if certain parent classes suddenly disappear. The new deprecation syntax is available here http://trac.sagemath.org/sage_trac/ticket/13109.\n\nBest,\n\nAnne",
    "created_at": "2012-08-15T05:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87221",
    "user": "aschilling"
}
```

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

archive/issue_comments_087222.json:
```json
{
    "body": "Hi again,\n\nWhen building the docs using \n\n\n```\nsage -docbuild reference html\n```\n\n\nI got the following warning, which should most likely be fixed\n\n\n```\n/Applications/sage-5.3.beta0/local/lib/python2.7/site-packages/sage/combinat/tableau.py:docstring of sage.combinat.tableau.Tableau.lambda_katabolism:1: WARNING: Inline literal start-string without end-string.\n```\n\n\nBest,\n\nAnne",
    "created_at": "2012-08-15T05:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87222",
    "user": "aschilling"
}
```

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

archive/issue_comments_087223.json:
```json
{
    "body": "Thanks Anne!\n\nThe pickling error confused me no end:) It seems that sage keeps pickles of old objects and then checks that new code is still able to unpickle the saved pickles. One way to fix this error would be be to make a new pickle jar which would remove the references to these renamed classes and presumably solve this problem. Another option would be to include deprecation warnings for all of the old class names -- I am not sure but would this lead to deprecation warnings during the unpickling meaning that these tests would still fail?\n\nI am happy to deprecate all of the old class name if you like, although it does seem a little strange to deprecate classes that were never officially part of sage. Other the other hand, the patch has been around for a while so people may be using the old names in their own code, so it might be worth doing because of this. \n\nI am happy to defer to your expertise as to what is the best course of action. Please advise.\n\nThe doc string error is also a little strange. It is caused by a T'_a in the doc string, but as this is part of a (raw) string I would have thought that sphinx would not have a problem with this... Anyway, I have fixed this by changing T'_a into S_a etc which is more readable anyway.\n\nI won't upload a new patch until I hear back from about the best way to resolve the pickling issues.\n\nBest,\nAndrew",
    "created_at": "2012-08-15T12:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87223",
    "user": "andrew.mathas"
}
```

Thanks Anne!

The pickling error confused me no end:) It seems that sage keeps pickles of old objects and then checks that new code is still able to unpickle the saved pickles. One way to fix this error would be be to make a new pickle jar which would remove the references to these renamed classes and presumably solve this problem. Another option would be to include deprecation warnings for all of the old class names -- I am not sure but would this lead to deprecation warnings during the unpickling meaning that these tests would still fail?

I am happy to deprecate all of the old class name if you like, although it does seem a little strange to deprecate classes that were never officially part of sage. Other the other hand, the patch has been around for a while so people may be using the old names in their own code, so it might be worth doing because of this. 

I am happy to defer to your expertise as to what is the best course of action. Please advise.

The doc string error is also a little strange. It is caused by a T'_a in the doc string, but as this is part of a (raw) string I would have thought that sphinx would not have a problem with this... Anyway, I have fixed this by changing T'_a into S_a etc which is more readable anyway.

I won't upload a new patch until I hear back from about the best way to resolve the pickling issues.

Best,
Andrew



---

archive/issue_comments_087224.json:
```json
{
    "body": "Hi Anne,\n\nI have discovered the register_unpickle_override function. Using this I have eliminated all but the following four unpickling errors:\n\n* _class__sage_combinat_crystals_affine_AffineCrystalFromClassicalAndPromotion_with_category_element_class__.sobj\n* _class__sage_combinat_crystals_tensor_product_CrystalOfTableaux_with_category_element_class__.sobj\n* _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystalsWithGenerators_with_category__.sobj\n* _class__sage_combinat_tableau_Tableau_class__.sobj\n\nThese error are, I think, all due to the fact that the old Tableau_class has been replaced with the quite different Tableau class. My guess is that the only way to fix these unpicking errors is to update the pickle jar. Is this right? If so, then it probably is not worthwhile including all of the register_unpickle_override statements that I have just inserted. Let me know what you think.\n\nI will upload a patch which fixes the docbuild problem that you mentioned, together with a few typos in the documentation and most of the unpickling problems, but I will hold off deprecation and the four problems above until I hear from you.\n\nBest,\n\nAndrew",
    "created_at": "2012-08-15T14:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87224",
    "user": "andrew.mathas"
}
```

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

archive/issue_comments_087225.json:
```json
{
    "body": "Hi Andrew,\n\nI sent some comments to you by e-mail.\n\nAnne",
    "created_at": "2012-08-15T14:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87225",
    "user": "aschilling"
}
```

Hi Andrew,

I sent some comments to you by e-mail.

Anne



---

archive/issue_comments_087226.json:
```json
{
    "body": "Thanks for all of these Anne. I have updated the pickles and and added deprecations for all of the old tableaux class names. Perhaps I missed something obvious, but the later turned out to be quite painful as the deprecation scheme does not seem to support deprecation of internal classes -- there is a (one-sided) discussion about what I think goes wrong on sage-devel. I ended up writing dummy function wrappers for the deprecations, which came to about 140 lines of code because of the necessary doctests to keep sage --coverage happy. It would be nice if there was a better way...\n\nAndrew",
    "created_at": "2012-08-16T07:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87226",
    "user": "andrew.mathas"
}
```

Thanks for all of these Anne. I have updated the pickles and and added deprecations for all of the old tableaux class names. Perhaps I missed something obvious, but the later turned out to be quite painful as the deprecation scheme does not seem to support deprecation of internal classes -- there is a (one-sided) discussion about what I think goes wrong on sage-devel. I ended up writing dummy function wrappers for the deprecations, which came to about 140 lines of code because of the necessary doctests to keep sage --coverage happy. It would be nice if there was a better way...

Andrew



---

archive/issue_comments_087227.json:
```json
{
    "body": "Apply trac_9265_tableaux_categories_am.patch",
    "created_at": "2012-08-16T07:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87227",
    "user": "andrew.mathas"
}
```

Apply trac_9265_tableaux_categories_am.patch



---

archive/issue_comments_087228.json:
```json
{
    "body": "For the patchbot:\n\nApply trac_9265_tableaux_categories_am.patch",
    "created_at": "2012-08-16T14:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87228",
    "user": "andrew.mathas"
}
```

For the patchbot:

Apply trac_9265_tableaux_categories_am.patch



---

archive/issue_comments_087229.json:
```json
{
    "body": "Changing keywords from \"\" to \"tableaux, combinatorics\".",
    "created_at": "2012-08-16T18:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87229",
    "user": "aschilling"
}
```

Changing keywords from "" to "tableaux, combinatorics".



---

archive/issue_comments_087230.json:
```json
{
    "body": "This patch cleans up tableaux in combinatorics. Andrew took over Jason's patch and made all changes we discussed by e-mail. I ran all tests on the new machine in Washington combinat.math.washington.edu and all tests passed.\n\nPositive review!\n\nAnne",
    "created_at": "2012-08-16T18:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87230",
    "user": "aschilling"
}
```

This patch cleans up tableaux in combinatorics. Andrew took over Jason's patch and made all changes we discussed by e-mail. I ran all tests on the new machine in Washington combinat.math.washington.edu and all tests passed.

Positive review!

Anne



---

archive/issue_comments_087231.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-17T05:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87231",
    "user": "andrew.mathas"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087232.json:
```json
{
    "body": "Replying to [comment:18 andrew.mathas]:\n> As the patchbot was complaining, I just uploaded a new version of the patch which deletes all trailing white space. Probably this is unwise as previously I used to have my editor do this automatically but I found that it meant that I had to rebase my patch all of the time so this will probably cause havoc further down the queue? \n> \n> What is the accepted practise here?\n\nFor the record: removing all trailing white spaces is indeed likely to produce conflicts.\nSo I usually just make sure in my patch to not introduce new ones (sometimes, I edit the patch directly to remove those that I introduced accidently), and to remove those that are very close to the lines I change anyway.\n\nNow in the case at hand, you currently kind of own the tableau file, since everybody knows that you are working hard on it, and that it is thus not safe playing with it. Then, the potential conflicts are with yourself, so you are free to take whichever course of action which is practical for you. \n\nThanks for your work!\n                                  Nicolas",
    "created_at": "2012-08-19T18:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87232",
    "user": "nthiery"
}
```

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

archive/issue_comments_087233.json:
```json
{
    "body": "Please fix the commit message, it shouldn't refer to the `[mq]` patch name.",
    "created_at": "2012-08-27T11:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87233",
    "user": "jdemeyer"
}
```

Please fix the commit message, it shouldn't refer to the `[mq]` patch name.



---

archive/issue_comments_087234.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-08-27T11:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87234",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_087235.json:
```json
{
    "body": "Commit message fixed.",
    "created_at": "2012-08-27T12:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87235",
    "user": "andrew.mathas"
}
```

Commit message fixed.



---

archive/issue_comments_087236.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-08-27T12:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87236",
    "user": "andrew.mathas"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_087237.json:
```json
{
    "body": "Doctest failure:\n\n```\nsage -t  -force_lib devel/sage/sage/combinat/tableau.py\n**********************************************************************\nFile \"/release/merger/sage-5.4.beta0/devel/sage-main/sage/combinat/tableau.py\", line 4257:\n    sage: sage.combinat.tableau.StandardTableaux_partition([2,1])\nExpected:\n    doctest:1: DeprecationWarning: this class is deprecated. Use StandardTableaux_size instead\n    See http://trac.sagemath.org/9265 for details.\n    Standard tableaux of shape [2, 1]\nGot:\n    doctest:1: DeprecationWarning: this class is deprecated. Use StandardTableaux_shape instead\n    See http://trac.sagemath.org/9265 for details.\n    Standard tableaux of shape [2, 1]\n**********************************************************************\n```\n",
    "created_at": "2012-08-29T11:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87237",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_087238.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-08-29T11:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87238",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_087239.json:
```json
{
    "body": "Sorry, I uploaded the wrong \"new version\" of the patch. This one should be OK.\n\nAll of the tests pasted for the patchbot (except for the pickles which need to be updated), so I am changing this back to positive review.",
    "created_at": "2012-08-29T12:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87239",
    "user": "andrew.mathas"
}
```

Sorry, I uploaded the wrong "new version" of the patch. This one should be OK.

All of the tests pasted for the patchbot (except for the pickles which need to be updated), so I am changing this back to positive review.



---

archive/issue_comments_087240.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-08-29T13:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87240",
    "user": "andrew.mathas"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_087241.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-03T12:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87241",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_087242.json:
```json
{
    "body": "This patch badly abuses `assert` and `AssertionError`.  `assert` should not be used for control flow.  An assert checks something which should always be true, a failed assertion is always a bug in the program.\n\nFor example:\n\n```\n        sage: Tableau([[1],[2,3]])\n        Traceback (most recent call last):\n        ...\n        AssertionError: A tableau must be a list of lists of weakly decreasing length.\n```\n\nThis is a simple user mistake, for which `assert` is not right.\n\nI think this must be fixed.",
    "created_at": "2012-09-24T07:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87242",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_087243.json:
```json
{
    "body": "Hi Jeroen,\n\nReplying to [comment:42 jdemeyer]:\n> This patch badly abuses `assert` and `AssertionError`.  `assert` should not be used for control flow.  An assert checks something which should always be true, a failed assertion is always a bug in the program.\n> \n> For example:\n> {{{\n>         sage: Tableau([[1],[2,3]])\n>         Traceback (most recent call last):\n>         ...\n>         AssertionError: A tableau must be a list of lists of weakly decreasing length.\n> }}}\n> This is a simple user mistake, for which `assert` is not right.\n> \n> I think this must be fixed.\n\nThere is no control flow involved. It's quite a common public constructor, but speed matters because it's used a lot at a low level in combinatorics calculations. The error message is nice and explicit. Altogether, given the discussion on sage-devel, do we agree that it's ok as such?\n\nCheers,\n                                           Nicolas",
    "created_at": "2012-09-24T09:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87243",
    "user": "nthiery"
}
```

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

archive/issue_comments_087244.json:
```json
{
    "body": "Replying to [comment:43 nthiery]:\n> There is no control flow involved. \nI disagree.\n\n```\ntry:\n    ...\nexcept AssertionError:\n    ...\n```\n\nis certainly control flow.\n\n> It's quite a common public constructor, but speed matters because it's used a lot at a low level in combinatorics calculations.\nAre these *constructors* really that speed-critical?  Of the 3 patches (#9265, #8899, #5457), this one is certainly the worst offender.",
    "created_at": "2012-09-24T10:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87244",
    "user": "jdemeyer"
}
```

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
Are these *constructors* really that speed-critical?  Of the 3 patches (#9265, #8899, #5457), this one is certainly the worst offender.



---

archive/issue_comments_087245.json:
```json
{
    "body": "Replying to [comment:43 nthiery]:\n> speed matters because it's used a lot at a low level in combinatorics calculations.\nIf speed matters that much, you could probably get a lot more speedup by using Cython as opposed to less argument checking.",
    "created_at": "2012-09-24T10:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87245",
    "user": "jdemeyer"
}
```

Replying to [comment:43 nthiery]:
> speed matters because it's used a lot at a low level in combinatorics calculations.
If speed matters that much, you could probably get a lot more speedup by using Cython as opposed to less argument checking.



---

archive/issue_comments_087246.json:
```json
{
    "body": "Replying to [comment:44 jdemeyer]:\n> > There is no control flow involved. \n> I disagree.\n> {{{\n> try:\n>     ...\n> except AssertionError:\n>     ...\n> }}}\n> is certainly control flow.\n\nOuch, that piece? Yes certainly, it's bad and should be fixed, either by using a ValueError, or better by avoiding to feed Tableau with potential garbage.\n\nThere is a lot of action going on currently around Tableaux so, to keep things running, I recommend doing that in a later ticket to not delay other stuff.",
    "created_at": "2012-09-24T11:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87246",
    "user": "nthiery"
}
```

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

archive/issue_comments_087247.json:
```json
{
    "body": "Replying to [comment:45 jdemeyer]:\n> > speed matters because it's used a lot at a low level in combinatorics calculations.\n> If speed matters that much, you could probably get a lot more speedup by using Cython\n\nCertainly, that's the planned next step in the cleanup of tableaux :-)\nAnd then having checks that can be disabled will really become relevant.",
    "created_at": "2012-09-24T11:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87247",
    "user": "nthiery"
}
```

Replying to [comment:45 jdemeyer]:
> > speed matters because it's used a lot at a low level in combinatorics calculations.
> If speed matters that much, you could probably get a lot more speedup by using Cython

Certainly, that's the planned next step in the cleanup of tableaux :-)
And then having checks that can be disabled will really become relevant.



---

archive/issue_comments_087248.json:
```json
{
    "body": "Replying to [comment:46 nthiery]:\n> There is a lot of action going on currently around Tableaux so, to keep things running, I recommend doing that in a later ticket to not delay other stuff.\nGood for me, it's just something to keep in mind.",
    "created_at": "2012-09-24T11:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87248",
    "user": "jdemeyer"
}
```

Replying to [comment:46 nthiery]:
> There is a lot of action going on currently around Tableaux so, to keep things running, I recommend doing that in a later ticket to not delay other stuff.
Good for me, it's just something to keep in mind.



---

archive/issue_comments_087249.json:
```json
{
    "body": "Replying to [comment:43 nthiery]:\n> It's quite a common public constructor, but speed matters because it's used a lot at a low level in combinatorics calculations.\nThen I think the best solution is adding a \"check\" argument to the constructor defaulting to True and doing the expensive checks only when `check` is True.",
    "created_at": "2012-09-24T11:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87249",
    "user": "jdemeyer"
}
```

Replying to [comment:43 nthiery]:
> It's quite a common public constructor, but speed matters because it's used a lot at a low level in combinatorics calculations.
Then I think the best solution is adding a "check" argument to the constructor defaulting to True and doing the expensive checks only when `check` is True.



---

archive/issue_comments_087250.json:
```json
{
    "body": "Jason seemed to like these assertions checks, but I agree that are \"wrong\" -- in fact, they caused me some grief in #13074. I doubt that there will be speed implications in modifying them.\n\nUnfortunately, it may take me a while to fix this as I'm at a conference this week and I don't have a good internet connection.\n\nAndrew",
    "created_at": "2012-09-24T16:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87250",
    "user": "andrew.mathas"
}
```

Jason seemed to like these assertions checks, but I agree that are "wrong" -- in fact, they caused me some grief in #13074. I doubt that there will be speed implications in modifying them.

Unfortunately, it may take me a while to fix this as I'm at a conference this week and I don't have a good internet connection.

Andrew



---

archive/issue_comments_087251.json:
```json
{
    "body": "Removing assert statements",
    "created_at": "2012-09-24T19:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87251",
    "user": "andrew.mathas"
}
```

Removing assert statements



---

archive/issue_comments_087252.json:
```json
{
    "body": "Attachment [trac_9265_tableaux_categories_am.patch](tarball://root/attachments/some-uuid/ticket9265/trac_9265_tableaux_categories_am.patch) by andrew.mathas created at 2012-09-24 20:03:09\n\n...talk written, patch patched.",
    "created_at": "2012-09-24T20:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87252",
    "user": "andrew.mathas"
}
```

Attachment [trac_9265_tableaux_categories_am.patch](tarball://root/attachments/some-uuid/ticket9265/trac_9265_tableaux_categories_am.patch) by andrew.mathas created at 2012-09-24 20:03:09

...talk written, patch patched.



---

archive/issue_comments_087253.json:
```json
{
    "body": "Wow, thanks a lot!  Anne or Jason, could any of you do the review please?",
    "created_at": "2012-09-24T20:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87253",
    "user": "jdemeyer"
}
```

Wow, thanks a lot!  Anne or Jason, could any of you do the review please?



---

archive/issue_comments_087254.json:
```json
{
    "body": "The patch on the sage-combinat queue looks good to me (which I assume is the same as here).\n\nAnne",
    "created_at": "2012-09-25T03:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87254",
    "user": "aschilling"
}
```

The patch on the sage-combinat queue looks good to me (which I assume is the same as here).

Anne



---

archive/issue_comments_087255.json:
```json
{
    "body": "Replying to [comment:53 aschilling]:\n> The patch on the sage-combinat queue looks good to me (which I assume is the same as here).\n> \n> Anne\n\nThanks Anne! Yes, it's the same patch as the one on the queue.\nAndrew",
    "created_at": "2012-09-25T06:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87255",
    "user": "andrew.mathas"
}
```

Replying to [comment:53 aschilling]:
> The patch on the sage-combinat queue looks good to me (which I assume is the same as here).
> 
> Anne

Thanks Anne! Yes, it's the same patch as the one on the queue.
Andrew



---

archive/issue_comments_087256.json:
```json
{
    "body": "I'm a bit scared by this pickle jar update now that Andrew Mathas admitted on #13072 that he doesn't know how to update the pickle jar.",
    "created_at": "2012-10-15T08:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87256",
    "user": "jdemeyer"
}
```

I'm a bit scared by this pickle jar update now that Andrew Mathas admitted on #13072 that he doesn't know how to update the pickle jar.



---

archive/issue_comments_087257.json:
```json
{
    "body": "Hi Jeroen,\n\nI did this pickle jar update following detailed instructions that Anne Schilling sent me. What I asked for on #13072 was for ***proper documentation*** on how to update pickles because I thought that the pickle may not have been applied properly (in fact, everything is fine because I was looking at version 5.3 whereas the updated pickles are in 5.4). As far as I am aware, there is no documentation on how to update the pickle jar, only instructions passed on hand-to-mouth, which IS a problem. For example, this doesn't seem to be covered in the developer guide.\n\nAndrew",
    "created_at": "2012-10-15T09:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87257",
    "user": "andrew.mathas"
}
```

Hi Jeroen,

I did this pickle jar update following detailed instructions that Anne Schilling sent me. What I asked for on #13072 was for ***proper documentation*** on how to update pickles because I thought that the pickle may not have been applied properly (in fact, everything is fine because I was looking at version 5.3 whereas the updated pickles are in 5.4). As far as I am aware, there is no documentation on how to update the pickle jar, only instructions passed on hand-to-mouth, which IS a problem. For example, this doesn't seem to be covered in the developer guide.

Andrew



---

archive/issue_comments_087258.json:
```json
{
    "body": "You are not supposed to update the pickle jar, it is only here to ensure backward compatibility. If at all possible, you should be using the `register_unpickle_override` to work around the change and unpickle into the new class.",
    "created_at": "2012-10-15T11:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87258",
    "user": "vbraun"
}
```

You are not supposed to update the pickle jar, it is only here to ensure backward compatibility. If at all possible, you should be using the `register_unpickle_override` to work around the change and unpickle into the new class.



---

archive/issue_comments_087259.json:
```json
{
    "body": "I have just uploaded the patch* trac_9265--tableaux_categories_pickles-am.patch *which adds unpickle overrides for most of the old classes that are being deprecated. This fixes all but four of the unpickle problems, however, it does not fix unpickling for *Tableau_class.* I think that because *Tableau_class does not unpickle* the following four pickles still fail:\n\n* `sage_combinat_crystals_affine_AffineCrystalFromClassicalAndPromotion_with_category_element_class`\n* `sage_combinat_crystals_tensor_product_CrystalOfTableaux_with_category_element_class`\n* `sage_combinat_crystals_tensor_product_TensorProductOfCrystalsWithGenerators_with_category`\n* `sage_combinat_tableau_Tableau_class`\n\nI have tried to fix the unpickling of Tableau_class using\n\n  `register_unpickle_override('sage.combinat.tableau', 'Tableau_class',  Tableau)`\n\nbut this does not work. My guess is that it is not possible to unpickle the deprecated *Tableau_class* objects using the new *Tableau* class objects because the underlying classes are too different.\n\nIf some one can see how to do this please let me know.",
    "created_at": "2012-10-17T02:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87259",
    "user": "andrew.mathas"
}
```

I have just uploaded the patch* trac_9265--tableaux_categories_pickles-am.patch *which adds unpickle overrides for most of the old classes that are being deprecated. This fixes all but four of the unpickle problems, however, it does not fix unpickling for *Tableau_class.* I think that because *Tableau_class does not unpickle* the following four pickles still fail:

* `sage_combinat_crystals_affine_AffineCrystalFromClassicalAndPromotion_with_category_element_class`
* `sage_combinat_crystals_tensor_product_CrystalOfTableaux_with_category_element_class`
* `sage_combinat_crystals_tensor_product_TensorProductOfCrystalsWithGenerators_with_category`
* `sage_combinat_tableau_Tableau_class`

I have tried to fix the unpickling of Tableau_class using

  `register_unpickle_override('sage.combinat.tableau', 'Tableau_class',  Tableau)`

but this does not work. My guess is that it is not possible to unpickle the deprecated *Tableau_class* objects using the new *Tableau* class objects because the underlying classes are too different.

If some one can see how to do this please let me know.



---

archive/issue_comments_087260.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2012-10-17T07:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87260",
    "user": "jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_087261.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2012-10-17T07:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87261",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_087262.json:
```json
{
    "body": "Let's postpone this to sage-5.5 such that the pickling issues can quietly be ironed out.",
    "created_at": "2012-10-17T07:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87262",
    "user": "jdemeyer"
}
```

Let's postpone this to sage-5.5 such that the pickling issues can quietly be ironed out.



---

archive/issue_comments_087263.json:
```json
{
    "body": "All pickle problems resolved.",
    "created_at": "2012-10-17T08:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87263",
    "user": "andrew.mathas"
}
```

All pickle problems resolved.



---

archive/issue_comments_087264.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-10-17T08:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87264",
    "user": "andrew.mathas"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087265.json:
```json
{
    "body": "Attachment [trac_9265--tableaux_categories_pickles-am.patch](tarball://root/attachments/some-uuid/ticket9265/trac_9265--tableaux_categories_pickles-am.patch) by andrew.mathas created at 2012-10-17 12:37:41\n\nFixing a typo in a comment",
    "created_at": "2012-10-17T12:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87265",
    "user": "andrew.mathas"
}
```

Attachment [trac_9265--tableaux_categories_pickles-am.patch](tarball://root/attachments/some-uuid/ticket9265/trac_9265--tableaux_categories_pickles-am.patch) by andrew.mathas created at 2012-10-17 12:37:41

Fixing a typo in a comment



---

archive/issue_comments_087266.json:
```json
{
    "body": "Thanks andrew for going the extra mile for backward compatibility!",
    "created_at": "2012-10-17T14:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87266",
    "user": "nthiery"
}
```

Thanks andrew for going the extra mile for backward compatibility!



---

archive/issue_comments_087267.json:
```json
{
    "body": "Hi Anne,\n\nWould you mind reviewing the latest update to #9265 so that Jeroen can put in back in the merge queue. It is just a matter of testing that\n\n```\nsage -t  devel/sage-sf/sage/structure/sage_object.pyx\n```\n\nworks. The new patch trac_9265--tableaux_categories_pickles-am.patch is also in the sage-combinat queue and to test it you should use 5.3 as 5.4 has the wrong pickle_jar at present.\n\nCheers,\n\nAndrew",
    "created_at": "2012-10-17T22:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87267",
    "user": "andrew.mathas"
}
```

Hi Anne,

Would you mind reviewing the latest update to #9265 so that Jeroen can put in back in the merge queue. It is just a matter of testing that

```
sage -t  devel/sage-sf/sage/structure/sage_object.pyx
```

works. The new patch trac_9265--tableaux_categories_pickles-am.patch is also in the sage-combinat queue and to test it you should use 5.3 as 5.4 has the wrong pickle_jar at present.

Cheers,

Andrew



---

archive/issue_comments_087268.json:
```json
{
    "body": "Replying to [comment:64 nthiery]:\n> Thanks andrew for going the extra mile for backward compatibility!\n\nWell, I didn't have a lot of choice:) It's a pity (but understandable) that Jeroen bumped the patch out of the 5.4 release an hour before I uploaded the fix as I guess this will play havoc with the sage-combinat queue. I am sure sure how we can guard for different versions of 5.4.? in the queue as \"old\" pre-releases will have the patch but one current ones won't.",
    "created_at": "2012-10-18T10:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87268",
    "user": "andrew.mathas"
}
```

Replying to [comment:64 nthiery]:
> Thanks andrew for going the extra mile for backward compatibility!

Well, I didn't have a lot of choice:) It's a pity (but understandable) that Jeroen bumped the patch out of the 5.4 release an hour before I uploaded the fix as I guess this will play havoc with the sage-combinat queue. I am sure sure how we can guard for different versions of 5.4.? in the queue as "old" pre-releases will have the patch but one current ones won't.



---

archive/issue_comments_087269.json:
```json
{
    "body": "Hi Andrew,\n\nI ran all tests and looked at the new patch. It looks fine. All tests pass with sage-5.3, except, but this seems unrelated to your patch and more related to a file by Jeroen Demeyer. Hence I am setting a positive review.\n\nThanks!\n\nAnne\n\n------------------------------------\n\nsage -t sage/tests/cmdline.py \nsage -t  \"devel/sage-combinat/sage/tests/cmdline.py\"        \n**********************************************************************\nFile \"/Applications/sage-5.3/devel/sage-combinat/sage/tests/cmdline.py\", line 99:\n    sage: err\nExpected:\n    ''\nGot:\n    '---------------------------------------------------------------------------\\nAttributeError                            Traceback (most recent call last)\\n\\n/Applications/sage-5.3/devel/sage-combinat/<ipython console> in <module>()\\n\\n/Applications/sage-5.3/local/lib/python/site-packages/sage/misc/preparser.pyc in load(filename, globals, attach)\\n   1657         else:\\n   1658             # Preparse in memory only for speed.\\n-> 1659             exec(preparse_file(open(fpath).read()) + \"\\\\n\", globals)\\n   1660     elif fpath.endswith(\\'.spyx\\') or fpath.endswith(\\'.pyx\\'):\\n   1661         import interpreter\\n\\n/Applications/sage-5.3/devel/sage-combinat/<string> in <module>()\\n\\nAttributeError: Latex instance has no attribute \\'add_to_mathjax_avoid_list\\'\\n'\n**********************************************************************\nFile \"/Applications/sage-5.3/devel/sage-combinat/sage/tests/cmdline.py\", line 109:\n    sage: err\nExpected:\n    ''\nGot:\n    '---------------------------------------------------------------------------\\nAttributeError                            Traceback (most recent call last)\\n\\n/Applications/sage-5.3/devel/sage-combinat/<ipython console> in <module>()\\n\\n/Applications/sage-5.3/local/lib/python/site-packages/sage/misc/preparser.pyc in load(filename, globals, attach)\\n   1657         else:\\n   1658             # Preparse in memory only for speed.\\n-> 1659             exec(preparse_file(open(fpath).read()) + \"\\\\n\", globals)\\n   1660     elif fpath.endswith(\\'.spyx\\') or fpath.endswith(\\'.pyx\\'):\\n   1661         import interpreter\\n\\n/Applications/sage-5.3/devel/sage-combinat/<string> in <module>()\\n\\nAttributeError: Latex instance has no attribute \\'add_to_mathjax_avoid_list\\'\\n'\n**********************************************************************\nFile \"/Applications/sage-5.3/devel/sage-combinat/sage/tests/cmdline.py\", line 119:\n    sage: err\nExpected:\n    ''\nGot:\n    '---------------------------------------------------------------------------\\nAttributeError                            Traceback (most recent call last)\\n\\n/Applications/sage-5.3/devel/sage-combinat/<ipython console> in <module>()\\n\\n/Applications/sage-5.3/local/lib/python/site-packages/sage/misc/preparser.pyc in load(filename, globals, attach)\\n   1657         else:\\n   1658             # Preparse in memory only for speed.\\n-> 1659             exec(preparse_file(open(fpath).read()) + \"\\\\n\", globals)\\n   1660     elif fpath.endswith(\\'.spyx\\') or fpath.endswith(\\'.pyx\\'):\\n   1661         import interpreter\\n\\n/Applications/sage-5.3/devel/sage-combinat/<string> in <module>()\\n\\nAttributeError: Latex instance has no attribute \\'add_to_mathjax_avoid_list\\'\\n'\n**********************************************************************\n1 items had failures:\n   3 of 187 in __main__.example_1\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /Users/anne/.sage//tmp/cmdline_49442.py\n\t [27.8 s]",
    "created_at": "2012-10-18T17:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87269",
    "user": "aschilling"
}
```

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

archive/issue_comments_087270.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-18T17:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87270",
    "user": "aschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087271.json:
```json
{
    "body": "Replying to [comment:66 andrew.mathas]:\n> It's a pity (but understandable) that Jeroen bumped the patch out of the 5.4 release an hour before I uploaded the fix as I guess this will play havoc with the sage-combinat queue. I am sure sure how we can guard for different versions of 5.4.? in the queue as \"old\" pre-releases will have the patch but one current ones won't.\n\nWell, once 5.4 will be out, we will just state that we don't support anymore the beta/rc of 5.4. Only a few of us are using them anyway, so that's anoying but not critical.",
    "created_at": "2012-10-19T07:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87271",
    "user": "nthiery"
}
```

Replying to [comment:66 andrew.mathas]:
> It's a pity (but understandable) that Jeroen bumped the patch out of the 5.4 release an hour before I uploaded the fix as I guess this will play havoc with the sage-combinat queue. I am sure sure how we can guard for different versions of 5.4.? in the queue as "old" pre-releases will have the patch but one current ones won't.

Well, once 5.4 will be out, we will just state that we don't support anymore the beta/rc of 5.4. Only a few of us are using them anyway, so that's anoying but not critical.



---

archive/issue_comments_087272.json:
```json
{
    "body": "Thanks Anne",
    "created_at": "2012-10-20T04:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87272",
    "user": "andrew.mathas"
}
```

Thanks Anne



---

archive/issue_comments_087273.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-10-29T21:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9265#issuecomment-87273",
    "user": "jdemeyer"
}
```

Resolution: fixed
