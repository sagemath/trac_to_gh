# Issue 9906: Move generally usable decorators from plot.misc to misc.decorators

archive/issues_009906.json:
```json
{
    "body": "Assignee: tdb\n\nCC:  jason mhansen\n\nKeywords: generality, decorators\n\nIn plot.misc there are some generally usable decorators for various nice stuff. These should be moved to a general library so other modules can use them without illogically depending on plot.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9907\n\n",
    "created_at": "2010-09-14T06:28:56Z",
    "labels": [
        "relocation",
        "minor",
        "enhancement"
    ],
    "title": "Move generally usable decorators from plot.misc to misc.decorators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9906",
    "user": "jsrn"
}
```
Assignee: tdb

CC:  jason mhansen

Keywords: generality, decorators

In plot.misc there are some generally usable decorators for various nice stuff. These should be moved to a general library so other modules can use them without illogically depending on plot.

Issue created by migration from https://trac.sagemath.org/ticket/9907





---

archive/issue_comments_098518.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-14T18:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98518",
    "user": "jsrn"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098519.json:
```json
{
    "body": "While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.",
    "created_at": "2010-09-15T13:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98519",
    "user": "jsrn"
}
```

While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.



---

archive/issue_comments_098520.json:
```json
{
    "body": "I'm not qualified to check out the \"work-around\" for classes.  But I've cc'ed Mike Hansen and Jason Grout, who I think were in on these in the first place back at #4201.\n\nI am running this through full tests as part of #6094 and a report will go there once concluded.\n\nCommit message on the ticket itself should probably change - there is no \"as before\" here to compare with, and in the final log it really won't make any sense.",
    "created_at": "2010-09-16T04:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98520",
    "user": "rbeezer"
}
```

I'm not qualified to check out the "work-around" for classes.  But I've cc'ed Mike Hansen and Jason Grout, who I think were in on these in the first place back at #4201.

I am running this through full tests as part of #6094 and a report will go there once concluded.

Commit message on the ticket itself should probably change - there is no "as before" here to compare with, and in the final log it really won't make any sense.



---

archive/issue_comments_098521.json:
```json
{
    "body": "Replying to [comment:2 jsrn]:\n> While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.\n\nDo you think you could just add the work-around to the sage_wraps decorator (sage.misc.misc.sage_wraps) and convert the decorators to use it?  There are other functions that use sage_wraps, and it would be nice to have all of that work-around code in one place.",
    "created_at": "2010-09-16T09:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98521",
    "user": "jason"
}
```

Replying to [comment:2 jsrn]:
> While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.

Do you think you could just add the work-around to the sage_wraps decorator (sage.misc.misc.sage_wraps) and convert the decorators to use it?  There are other functions that use sage_wraps, and it would be nice to have all of that work-around code in one place.



---

archive/issue_comments_098522.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> Replying to [comment:2 jsrn]:\n> > While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.\n> \n> Do you think you could just add the work-around to the sage_wraps decorator (sage.misc.misc.sage_wraps) and convert the decorators to use it?  There are other functions that use sage_wraps, and it would be nice to have all of that work-around code in one place.\n\nThat should be no problem, I guess; I wasn't aware of sage_wraps. However, that might affect a lot of places outside the original scope of this ticket; should it be a new ticket then? What's the precedence here?",
    "created_at": "2010-09-16T11:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98522",
    "user": "jsrn"
}
```

Replying to [comment:4 jason]:
> Replying to [comment:2 jsrn]:
> > While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.
> 
> Do you think you could just add the work-around to the sage_wraps decorator (sage.misc.misc.sage_wraps) and convert the decorators to use it?  There are other functions that use sage_wraps, and it would be nice to have all of that work-around code in one place.

That should be no problem, I guess; I wasn't aware of sage_wraps. However, that might affect a lot of places outside the original scope of this ticket; should it be a new ticket then? What's the precedence here?



---

archive/issue_comments_098523.json:
```json
{
    "body": "Replying to [comment:5 jsrn]:\n> Replying to [comment:4 jason]:\n> > Replying to [comment:2 jsrn]:\n> > > While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.\n> > \n> > Do you think you could just add the work-around to the sage_wraps decorator (sage.misc.misc.sage_wraps) and convert the decorators to use it?  There are other functions that use sage_wraps, and it would be nice to have all of that work-around code in one place.\n> \n> That should be no problem, I guess; I wasn't aware of sage_wraps. However, that might affect a lot of places outside the original scope of this ticket; should it be a new ticket then? What's the precedence here?\n\nI started Trac #9919 for doing this patch in sage_wraps. I'm also thinking that, when the problems with this patch are identified, we might move sage_wraps and other decorators in sage.misc.misc into sage.misc.decorators as well.",
    "created_at": "2010-09-16T14:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98523",
    "user": "jsrn"
}
```

Replying to [comment:5 jsrn]:
> Replying to [comment:4 jason]:
> > Replying to [comment:2 jsrn]:
> > > While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.
> > 
> > Do you think you could just add the work-around to the sage_wraps decorator (sage.misc.misc.sage_wraps) and convert the decorators to use it?  There are other functions that use sage_wraps, and it would be nice to have all of that work-around code in one place.
> 
> That should be no problem, I guess; I wasn't aware of sage_wraps. However, that might affect a lot of places outside the original scope of this ticket; should it be a new ticket then? What's the precedence here?

I started Trac #9919 for doing this patch in sage_wraps. I'm also thinking that, when the problems with this patch are identified, we might move sage_wraps and other decorators in sage.misc.misc into sage.misc.decorators as well.



---

archive/issue_comments_098524.json:
```json
{
    "body": "Starting another ticket sounds good.",
    "created_at": "2010-09-16T15:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98524",
    "user": "jason"
}
```

Starting another ticket sounds good.



---

archive/issue_comments_098525.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-17T08:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98525",
    "user": "jsrn"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098526.json:
```json
{
    "body": "Rob Beezer posted the following problem with the current patch for Trac #6094, but that is actually a problem with the current patch for this trac. When testing the unpickle-function in sage.structure.sage_object, the relocation of the decorators yield problems:\n\n\n```\nrob@wave:/sage/dev$ ./sage -t  devel/sage/sage/structure/sage_object.pyx\nsage -t  \"devel/sage/sage/structure/sage_object.pyx\"        \n**********************************************************************\nFile \"/sage/dev/devel/sage/sage/structure/sage_object.pyx\", line 1001:\n    sage: print \"x\"; sage.structure.sage_object.unpickle_all(std)\nExpected:\n    x...\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n    x\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead\n    ** failed:  _class__sage_plot_misc_options__.sobj\n    ** failed:  _class__sage_plot_misc_rename_keyword__.sobj\n    Failed:\n    _class__sage_plot_misc_options__.sobj\n    _class__sage_plot_misc_rename_keyword__.sobj\n    Successfully unpickled 584 objects.\n    Failed to unpickle 2 objects.\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_23\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/rob/.sage//tmp/.doctest_sage_object.py\n         [5.2 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/structure/sage_object.pyx\"\n```\n\n\nThe deprecation-warnings are just garbage from words.py, so the important thing to note is the \"** failed\"-lines. The problem, as far as I can see, is simply that there is a standard pickle jar which has a pickle for all the functions etc. shipped with sage. This needs to be updated when applying this patch. Does anyone know how this is done and possibly included in the patch?\n\nCheers, Johan",
    "created_at": "2010-09-17T08:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98526",
    "user": "jsrn"
}
```

Rob Beezer posted the following problem with the current patch for Trac #6094, but that is actually a problem with the current patch for this trac. When testing the unpickle-function in sage.structure.sage_object, the relocation of the decorators yield problems:


```
rob@wave:/sage/dev$ ./sage -t  devel/sage/sage/structure/sage_object.pyx
sage -t  "devel/sage/sage/structure/sage_object.pyx"        
**********************************************************************
File "/sage/dev/devel/sage/sage/structure/sage_object.pyx", line 1001:
    sage: print "x"; sage.structure.sage_object.unpickle_all(std)
Expected:
    x...
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    x
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead
    ** failed:  _class__sage_plot_misc_options__.sobj
    ** failed:  _class__sage_plot_misc_rename_keyword__.sobj
    Failed:
    _class__sage_plot_misc_options__.sobj
    _class__sage_plot_misc_rename_keyword__.sobj
    Successfully unpickled 584 objects.
    Failed to unpickle 2 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_23
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/rob/.sage//tmp/.doctest_sage_object.py
         [5.2 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/structure/sage_object.pyx"
```


The deprecation-warnings are just garbage from words.py, so the important thing to note is the "** failed"-lines. The problem, as far as I can see, is simply that there is a standard pickle jar which has a pickle for all the functions etc. shipped with sage. This needs to be updated when applying this patch. Does anyone know how this is done and possibly included in the patch?

Cheers, Johan



---

archive/issue_comments_098527.json:
```json
{
    "body": "The pickle jar contains old pickles of objects that we want to ensure work in the future. For example, if you made the changes at\u00a0[9907](http://trac.sagemath.org/sage_trac/ticket/9907)\u00a0as the are, then possibly many pickles out in the wild would break. Instead of trying to update the pickle jar, the appropriate thing to do would be to add the following to\u00a0sage/plot/misc.py\n\n\n```\n#For backward compatibility -- see #9907.\nfrom sage.misc.decorators import options, suboptions, rename_keyword\n\n```\n\nThat way, the old pickles will still work as they will still be able to find the decorators in\u00a0sage.plot.misc.",
    "created_at": "2010-09-19T20:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98527",
    "user": "mhansen"
}
```

The pickle jar contains old pickles of objects that we want to ensure work in the future. For example, if you made the changes at [9907](http://trac.sagemath.org/sage_trac/ticket/9907) as the are, then possibly many pickles out in the wild would break. Instead of trying to update the pickle jar, the appropriate thing to do would be to add the following to sage/plot/misc.py


```
#For backward compatibility -- see #9907.
from sage.misc.decorators import options, suboptions, rename_keyword

```

That way, the old pickles will still work as they will still be able to find the decorators in sage.plot.misc.



---

archive/issue_comments_098528.json:
```json
{
    "body": "Replying to [comment:9 mhansen]:\n> The pickle jar contains old pickles of objects that we want to ensure work in the future. For example, if you made the changes at\u00a0[9907](http://trac.sagemath.org/sage_trac/ticket/9907)\u00a0as the are, then possibly many pickles out in the wild would break. Instead of trying to update the pickle jar, the appropriate thing to do would be to add the following to\u00a0sage/plot/misc.py\n> \n> {{{\n> #For backward compatibility -- see #9907.\n> from sage.misc.decorators import options, suboptions, rename_keyword\n> \n> }}}\n> That way, the old pickles will still work as they will still be able to find the decorators in\u00a0sage.plot.misc.\n\nOk, thanks -- I will update the patch for #9907. I was actually wondering a bit about backward compatibility, so good to know this is the system. Does the above fix then have a one-year lifetime like for keyword-deprecation? If so, should it be flagged somehow (e.g. with the comment containing the term \"backward compatibility\") so it can be found and removed one year from now?",
    "created_at": "2010-09-20T06:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98528",
    "user": "jsrn"
}
```

Replying to [comment:9 mhansen]:
> The pickle jar contains old pickles of objects that we want to ensure work in the future. For example, if you made the changes at [9907](http://trac.sagemath.org/sage_trac/ticket/9907) as the are, then possibly many pickles out in the wild would break. Instead of trying to update the pickle jar, the appropriate thing to do would be to add the following to sage/plot/misc.py
> 
> {{{
> #For backward compatibility -- see #9907.
> from sage.misc.decorators import options, suboptions, rename_keyword
> 
> }}}
> That way, the old pickles will still work as they will still be able to find the decorators in sage.plot.misc.

Ok, thanks -- I will update the patch for #9907. I was actually wondering a bit about backward compatibility, so good to know this is the system. Does the above fix then have a one-year lifetime like for keyword-deprecation? If so, should it be flagged somehow (e.g. with the comment containing the term "backward compatibility") so it can be found and removed one year from now?



---

archive/issue_comments_098529.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-23T12:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98529",
    "user": "jsrn"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098530.json:
```json
{
    "body": "Changing assignee from tdb to jsrn.",
    "created_at": "2010-09-23T12:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98530",
    "user": "jsrn"
}
```

Changing assignee from tdb to jsrn.



---

archive/issue_comments_098531.json:
```json
{
    "body": "Note that the added patch assumes the patch for Trac #9919.",
    "created_at": "2010-09-23T12:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98531",
    "user": "jsrn"
}
```

Note that the added patch assumes the patch for Trac #9919.



---

archive/issue_comments_098532.json:
```json
{
    "body": "Added a comment about when then bug in #9919 was fixed in Python. Accidentally uploaded two.",
    "created_at": "2010-09-24T06:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98532",
    "user": "jsrn"
}
```

Added a comment about when then bug in #9919 was fixed in Python. Accidentally uploaded two.



---

archive/issue_comments_098533.json:
```json
{
    "body": "Ok, uploaded a new one, as it seems you can't manually change the patch-files because of some hashes in the top of the file. So this one was done the right way. Remember to use the newest and \n*NOT* the one called \".2.patch\".",
    "created_at": "2010-09-24T07:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98533",
    "user": "jsrn"
}
```

Ok, uploaded a new one, as it seems you can't manually change the patch-files because of some hashes in the top of the file. So this one was done the right way. Remember to use the newest and 
*NOT* the one called ".2.patch".



---

archive/issue_comments_098534.json:
```json
{
    "body": "Can I delete the .2.patch file, then?",
    "created_at": "2010-10-02T04:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98534",
    "user": "jason"
}
```

Can I delete the .2.patch file, then?



---

archive/issue_comments_098535.json:
```json
{
    "body": "I've opened up #10057 to address an import change that needs to be made in sagenb after this is merged.",
    "created_at": "2010-10-02T19:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98535",
    "user": "jason"
}
```

I've opened up #10057 to address an import change that needs to be made in sagenb after this is merged.



---

archive/issue_comments_098536.json:
```json
{
    "body": "apply only this patch; rebased to 4.6.alpha1+some patches",
    "created_at": "2010-10-02T19:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98536",
    "user": "jason"
}
```

apply only this patch; rebased to 4.6.alpha1+some patches



---

archive/issue_comments_098537.json:
```json
{
    "body": "Attachment [trac_9907_move_decorators.patch](tarball://root/attachments/some-uuid/ticket9907/trac_9907_move_decorators.patch) by jsrn created at 2010-10-05 09:39:11\n\nReplying to [comment:17 jason]:\n> Can I delete the .2.patch file, then?\nSure; I just don't have the privileges to do that myself.",
    "created_at": "2010-10-05T09:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98537",
    "user": "jsrn"
}
```

Attachment [trac_9907_move_decorators.patch](tarball://root/attachments/some-uuid/ticket9907/trac_9907_move_decorators.patch) by jsrn created at 2010-10-05 09:39:11

Replying to [comment:17 jason]:
> Can I delete the .2.patch file, then?
Sure; I just don't have the privileges to do that myself.



---

archive/issue_comments_098538.json:
```json
{
    "body": "This needs to be coordinated with #10107.",
    "created_at": "2010-10-09T20:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98538",
    "user": "mhansen"
}
```

This needs to be coordinated with #10107.



---

archive/issue_comments_098539.json:
```json
{
    "body": "Attachment [trac_9907_move_decorators.2.patch](tarball://root/attachments/some-uuid/ticket9907/trac_9907_move_decorators.2.patch) by jsrn created at 2010-11-02 13:58:34\n\nRebased to 4.6. Still requires first applying patch for Trac #9919",
    "created_at": "2010-11-02T13:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98539",
    "user": "jsrn"
}
```

Attachment [trac_9907_move_decorators.2.patch](tarball://root/attachments/some-uuid/ticket9907/trac_9907_move_decorators.2.patch) by jsrn created at 2010-11-02 13:58:34

Rebased to 4.6. Still requires first applying patch for Trac #9919



---

archive/issue_comments_098540.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-09T20:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98540",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098541.json:
```json
{
    "body": "If I apply #6094, #9907, #9919, and #10107 together on top of sage-4.6, all long tests pass. The code looks good.",
    "created_at": "2010-11-09T20:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98541",
    "user": "rlm"
}
```

If I apply #6094, #9907, #9919, and #10107 together on top of sage-4.6, all long tests pass. The code looks good.



---

archive/issue_comments_098542.json:
```json
{
    "body": "Should this be merged in Sage 4.6.1? (if yes, please set the Milestone)",
    "created_at": "2010-11-11T16:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98542",
    "user": "jdemeyer"
}
```

Should this be merged in Sage 4.6.1? (if yes, please set the Milestone)



---

archive/issue_comments_098543.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-16T08:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9906#issuecomment-98543",
    "user": "jdemeyer"
}
```

Resolution: fixed
