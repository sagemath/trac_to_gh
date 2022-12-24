# Issue 7682: Customize printing of real numbers

archive/issues_007682.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  robertwb jkantor was kcrisman egourgoulhon\n\nFrom http://groups.google.com/group/sage-support/browse_thread/thread/06756df51d828bf4\n\n\n```\nwe probably ought to make this easier to just print the \nfirst n digits after the decimal by default for RR numbers, or to not \nprint out the trailing zeros.  I can't imagine telling my students, for \nexample, that they need to do '%.3f'%num every time they come across a \nnumber, especially since they just want to display the equation, not \nformat it as a string.\n\nWhat do people think about this interface?\n\nsage: RR.print_digits=3\nsage: 3.09384\n3.094\nsage: RR.print_trailing_zeros=False\nsage: RR.print_digits=None\nsage: 3.09384\n3.09384\n\nMake it something like the RR.scientific_notation flag that is currently \nin use.\n```\n\n\nAdditionally, and more flexibly, we could just have something like:\n\n\n```\n\nsage: RR.set_print_format('%.3f')\nsage: RR(pi)\n3.142\n```\n\n\nor more pythonically\n\n\n```\nsage: RR.print_format = '%.3f'\nsage: RR(pi)\n3.142\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7682\n\n",
    "created_at": "2009-12-14T20:29:00Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Customize printing of real numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7682",
    "user": "jason"
}
```
Assignee: AlexGhitza

CC:  robertwb jkantor was kcrisman egourgoulhon

From http://groups.google.com/group/sage-support/browse_thread/thread/06756df51d828bf4


```
we probably ought to make this easier to just print the 
first n digits after the decimal by default for RR numbers, or to not 
print out the trailing zeros.  I can't imagine telling my students, for 
example, that they need to do '%.3f'%num every time they come across a 
number, especially since they just want to display the equation, not 
format it as a string.

What do people think about this interface?

sage: RR.print_digits=3
sage: 3.09384
3.094
sage: RR.print_trailing_zeros=False
sage: RR.print_digits=None
sage: 3.09384
3.09384

Make it something like the RR.scientific_notation flag that is currently 
in use.
```


Additionally, and more flexibly, we could just have something like:


```

sage: RR.set_print_format('%.3f')
sage: RR(pi)
3.142
```


or more pythonically


```
sage: RR.print_format = '%.3f'
sage: RR(pi)
3.142
```


Issue created by migration from https://trac.sagemath.org/ticket/7682





---

archive/issue_comments_065890.json:
```json
{
    "body": "Note that these extra zeros were introduced in the printing by the switch to pynac.  They were eliminated a while ago in maxima by #4572.",
    "created_at": "2009-12-14T20:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65890",
    "user": "jason"
}
```

Note that these extra zeros were introduced in the printing by the switch to pynac.  They were eliminated a while ago in maxima by #4572.



---

archive/issue_comments_065891.json:
```json
{
    "body": "I'm declaring a total feature freeze on sage-4.3.",
    "created_at": "2009-12-24T07:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65891",
    "user": "was"
}
```

I'm declaring a total feature freeze on sage-4.3.



---

archive/issue_comments_065892.json:
```json
{
    "body": "Here is a first cut of a print_options model for RealField that lets you specify default printing options for any RealField, all RealFields, and still lets you override the defaults when you actually print the numbers.\n\nIt mostly works.  Docs need to be updated, deprecation warnings need to be added, and the interface for scientific notation needs to be revamped (no_sci and sci_not are confusing and inconsistent keyword choices!).",
    "created_at": "2010-01-25T13:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65892",
    "user": "jason"
}
```

Here is a first cut of a print_options model for RealField that lets you specify default printing options for any RealField, all RealFields, and still lets you override the defaults when you actually print the numbers.

It mostly works.  Docs need to be updated, deprecation warnings need to be added, and the interface for scientific notation needs to be revamped (no_sci and sci_not are confusing and inconsistent keyword choices!).



---

archive/issue_comments_065893.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-25T13:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65893",
    "user": "jason"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_065894.json:
```json
{
    "body": "Changing component from basic arithmetic to numerical.",
    "created_at": "2010-01-25T13:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65894",
    "user": "jason"
}
```

Changing component from basic arithmetic to numerical.



---

archive/issue_comments_065895.json:
```json
{
    "body": "I refreshed the patch which a much more comprehensive patch.  This patch fixes all doctests in rings/*.pyx (running long doctests now).  Documentation still needs to be updated, though, and some new doctests to test the new functionality.",
    "created_at": "2010-01-26T05:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65895",
    "user": "jason"
}
```

I refreshed the patch which a much more comprehensive patch.  This patch fixes all doctests in rings/*.pyx (running long doctests now).  Documentation still needs to be updated, though, and some new doctests to test the new functionality.



---

archive/issue_comments_065896.json:
```json
{
    "body": "Okay, patch passes all (non-long) doctests in Sage.",
    "created_at": "2010-01-26T06:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65896",
    "user": "jason"
}
```

Okay, patch passes all (non-long) doctests in Sage.



---

archive/issue_comments_065897.json:
```json
{
    "body": "Usually rings are supposed to be immutable, but I think this general idea is worth it. As for the interface, setting attributes on RR directly isn't very consistent with the way we do things in Sage--it's probably be better to have a RR.print_options(...) that takes keywords. (This way it could have a nice docstring as well.)",
    "created_at": "2010-01-26T06:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65897",
    "user": "robertwb"
}
```

Usually rings are supposed to be immutable, but I think this general idea is worth it. As for the interface, setting attributes on RR directly isn't very consistent with the way we do things in Sage--it's probably be better to have a RR.print_options(...) that takes keywords. (This way it could have a nice docstring as well.)



---

archive/issue_comments_065898.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-01-26T06:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65898",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_065899.json:
```json
{
    "body": "Thanks for the style review.  Okay, I can change print_options to a function, though I don't think it's \"better\", maybe just more consistent and slightly worse (i.e., unpythonic and more typing)\n\nOn another note, I just changed the latexing of a real field to indicate the precision and rounding, so that RealField(100,rnd='RNDD') prints as \\Bold{R}^{-}_{100}.  The subscript is the precision, the superscript is '+' for RNDU, '-' for RNDD, 0 for RNDZ, and nothing for RNDN.  What do you think?  It mirrors better the textual description of the field that indicates precision and rounding.",
    "created_at": "2010-01-26T06:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65899",
    "user": "jason"
}
```

Thanks for the style review.  Okay, I can change print_options to a function, though I don't think it's "better", maybe just more consistent and slightly worse (i.e., unpythonic and more typing)

On another note, I just changed the latexing of a real field to indicate the precision and rounding, so that RealField(100,rnd='RNDD') prints as \Bold{R}^{-}_{100}.  The subscript is the precision, the superscript is '+' for RNDU, '-' for RNDD, 0 for RNDZ, and nothing for RNDN.  What do you think?  It mirrors better the textual description of the field that indicates precision and rounding.



---

archive/issue_comments_065900.json:
```json
{
    "body": "As for immutability; what if we don't consider the printing options as part of the ring (i.e., it's not part of the hash for the cache, like it is now)?  Then a user can temporarily change the ring's printing operations, but none of the printing options are considered in testing for equality, stored in pickles, etc.",
    "created_at": "2010-01-26T06:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65900",
    "user": "jason"
}
```

As for immutability; what if we don't consider the printing options as part of the ring (i.e., it's not part of the hash for the cache, like it is now)?  Then a user can temporarily change the ring's printing operations, but none of the printing options are considered in testing for equality, stored in pickles, etc.



---

archive/issue_comments_065901.json:
```json
{
    "body": "Replying to [comment:8 robertwb]:\n> it's probably be better to have a RR.print_options(...) that takes keywords. (This way it could have a nice docstring as well.) \n\nYes, but how do you get the value of a specific option (as opposed to setting it).",
    "created_at": "2010-01-26T07:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65901",
    "user": "jason"
}
```

Replying to [comment:8 robertwb]:
> it's probably be better to have a RR.print_options(...) that takes keywords. (This way it could have a nice docstring as well.) 

Yes, but how do you get the value of a specific option (as opposed to setting it).



---

archive/issue_comments_065902.json:
```json
{
    "body": "Replying to [comment:8 robertwb]:\n> (This way it could have a nice docstring as well.) \n\nThe Cython \"property\" construct can also take a nice docstring.  Is anything ever done with this docstring?",
    "created_at": "2010-01-26T07:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65902",
    "user": "jason"
}
```

Replying to [comment:8 robertwb]:
> (This way it could have a nice docstring as well.) 

The Cython "property" construct can also take a nice docstring.  Is anything ever done with this docstring?



---

archive/issue_comments_065903.json:
```json
{
    "body": "Attachment [trac-7682-realfield-printing-options.patch](tarball://root/attachments/some-uuid/ticket7682/trac-7682-realfield-printing-options.patch) by jason created at 2010-01-26 09:40:28\n\nOkay, this is getting big now.  I went through real_mpfr.pyx and added a lot of doctests and documentation.\n\nThere are four doctests failing right now because I'm not sure if they are bugs or if they are right.  Here they are:\n\n\n```\n**********************************************************************\nFile \"/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx\", line 3343:\n    sage: RR('nan').is_real() # fail until we decide what it should be\nExpected nothing\nGot:\n    True\n**********************************************************************\nFile \"/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx\", line 3344:\n    sage: RR('inf').is_real() # fail until we decide what it should be\nExpected nothing\nGot:\n    True\n**********************************************************************\nFile \"/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx\", line 3360:\n    sage: RR('nan').__nonzero__() # fail until we decide what it should be\nExpected nothing\nGot:\n    False\n**********************************************************************\nFile \"/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx\", line 3397:\n    sage: RR('nan')==RR('nan') # Fail until we decide what it should be\nExpected nothing\nGot:\n    True\n**********************************************************************\nFile \"/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx\", line 3419:\n    sage: RR('nan')==RR('nan') # fail until we decide what it should be\nExpected nothing\nGot:\n    True\n```\n\n\nAre those four answers right (the \"Got:\" parts)?  See #8074 for more corner cases.",
    "created_at": "2010-01-26T09:40:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65903",
    "user": "jason"
}
```

Attachment [trac-7682-realfield-printing-options.patch](tarball://root/attachments/some-uuid/ticket7682/trac-7682-realfield-printing-options.patch) by jason created at 2010-01-26 09:40:28

Okay, this is getting big now.  I went through real_mpfr.pyx and added a lot of doctests and documentation.

There are four doctests failing right now because I'm not sure if they are bugs or if they are right.  Here they are:


```
**********************************************************************
File "/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx", line 3343:
    sage: RR('nan').is_real() # fail until we decide what it should be
Expected nothing
Got:
    True
**********************************************************************
File "/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx", line 3344:
    sage: RR('inf').is_real() # fail until we decide what it should be
Expected nothing
Got:
    True
**********************************************************************
File "/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx", line 3360:
    sage: RR('nan').__nonzero__() # fail until we decide what it should be
Expected nothing
Got:
    False
**********************************************************************
File "/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx", line 3397:
    sage: RR('nan')==RR('nan') # Fail until we decide what it should be
Expected nothing
Got:
    True
**********************************************************************
File "/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx", line 3419:
    sage: RR('nan')==RR('nan') # fail until we decide what it should be
Expected nothing
Got:
    True
```


Are those four answers right (the "Got:" parts)?  See #8074 for more corner cases.



---

archive/issue_comments_065904.json:
```json
{
    "body": "I rebased this patch to apply to 4.3.3 (it conflicted with a big rewrite by was and a small patch by robertwb).  The patch touches a lot of areas (and adds lots of doctests!), so a quick review would help avoid having to rebase it again.",
    "created_at": "2010-02-27T22:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65904",
    "user": "jason"
}
```

I rebased this patch to apply to 4.3.3 (it conflicted with a big rewrite by was and a small patch by robertwb).  The patch touches a lot of areas (and adds lots of doctests!), so a quick review would help avoid having to rebase it again.



---

archive/issue_comments_065905.json:
```json
{
    "body": "Attachment [trac-7682-realfield-printing-options.2.patch](tarball://root/attachments/some-uuid/ticket7682/trac-7682-realfield-printing-options.2.patch) by jason created at 2010-02-28 04:58:59\n\napply instead of previous patch.  Rebased to Sage 4.3.3",
    "created_at": "2010-02-28T04:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65905",
    "user": "jason"
}
```

Attachment [trac-7682-realfield-printing-options.2.patch](tarball://root/attachments/some-uuid/ticket7682/trac-7682-realfield-printing-options.2.patch) by jason created at 2010-02-28 04:58:59

apply instead of previous patch.  Rebased to Sage 4.3.3



---

archive/issue_comments_065906.json:
```json
{
    "body": "I uploaded a new patch which corrects several doctests; all doctests in Sage now seem to pass with this patch applied.",
    "created_at": "2010-02-28T05:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65906",
    "user": "jason"
}
```

I uploaded a new patch which corrects several doctests; all doctests in Sage now seem to pass with this patch applied.



---

archive/issue_comments_065907.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65907",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_065908.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-03-17T05:13:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65908",
    "user": "jason"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_065909.json:
```json
{
    "body": "rebase to 4.4.1, apply only this patch",
    "created_at": "2010-05-14T17:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65909",
    "user": "jason"
}
```

rebase to 4.4.1, apply only this patch



---

archive/issue_comments_065910.json:
```json
{
    "body": "Attachment [trac-7682-realfield-printing-options.3.patch](tarball://root/attachments/some-uuid/ticket7682/trac-7682-realfield-printing-options.3.patch) by jason created at 2010-05-14 17:07:52\n\nI removed a bunch of fixes unrelated to the printing option change and put them on other tickets.  I also fixed at least one accidental code removal.  In 4.4.1, Sage won't start after this patch is applied, due to\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\ninit2.c:52: MPFR assertion failed: p >= 2 && p <= ((mpfr_prec_t)((mpfr_prec_t)(~(mpfr_prec_t)0)>>1))\n/Users/grout/sage/local/bin/sage-sage: line 206: 16842 Abort trap              sage-ipython \"$@\" -i\n| Sage Version 4.4.1, Release Date: 2010-05-02                       |\n| Type notebook() for the GUI, and license() for information.        |\n```\n",
    "created_at": "2010-05-14T17:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65910",
    "user": "jason"
}
```

Attachment [trac-7682-realfield-printing-options.3.patch](tarball://root/attachments/some-uuid/ticket7682/trac-7682-realfield-printing-options.3.patch) by jason created at 2010-05-14 17:07:52

I removed a bunch of fixes unrelated to the printing option change and put them on other tickets.  I also fixed at least one accidental code removal.  In 4.4.1, Sage won't start after this patch is applied, due to


```
----------------------------------------------------------------------
----------------------------------------------------------------------
init2.c:52: MPFR assertion failed: p >= 2 && p <= ((mpfr_prec_t)((mpfr_prec_t)(~(mpfr_prec_t)0)>>1))
/Users/grout/sage/local/bin/sage-sage: line 206: 16842 Abort trap              sage-ipython "$@" -i
| Sage Version 4.4.1, Release Date: 2010-05-02                       |
| Type notebook() for the GUI, and license() for information.        |
```




---

archive/issue_comments_065911.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-14T17:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65911",
    "user": "jason"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065912.json:
```json
{
    "body": "rebase to 4.4.1, fix startup bug,  apply only this patch",
    "created_at": "2010-05-14T18:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65912",
    "user": "jason"
}
```

rebase to 4.4.1, fix startup bug,  apply only this patch



---

archive/issue_comments_065913.json:
```json
{
    "body": "Attachment [trac-7682-realfield-printing-options.5.patch](tarball://root/attachments/some-uuid/ticket7682/trac-7682-realfield-printing-options.5.patch) by jason created at 2010-05-14 19:21:11\n\nrebase to 4.4.1, fix startup bug,  fix one doctest to test for the startup bug; apply only this patch",
    "created_at": "2010-05-14T19:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65913",
    "user": "jason"
}
```

Attachment [trac-7682-realfield-printing-options.5.patch](tarball://root/attachments/some-uuid/ticket7682/trac-7682-realfield-printing-options.5.patch) by jason created at 2010-05-14 19:21:11

rebase to 4.4.1, fix startup bug,  fix one doctest to test for the startup bug; apply only this patch



---

archive/issue_comments_065914.json:
```json
{
    "body": "Slightly OT: Regarding the thread that started this, in finance you don't need less/limited precision, but *fixed*-point numbers. ;-)",
    "created_at": "2010-05-28T01:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65914",
    "user": "leif"
}
```

Slightly OT: Regarding the thread that started this, in finance you don't need less/limited precision, but *fixed*-point numbers. ;-)



---

archive/issue_comments_065915.json:
```json
{
    "body": "Replying to [comment:19 leif]:\n> Slightly OT: Regarding the thread that started this, in finance you don't need less/limited precision, but *fixed*-point numbers. ;-)\n> \n\nOf course, then you would probably use the python Decimal module :).",
    "created_at": "2010-05-28T02:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65915",
    "user": "jason"
}
```

Replying to [comment:19 leif]:
> Slightly OT: Regarding the thread that started this, in finance you don't need less/limited precision, but *fixed*-point numbers. ;-)
> 

Of course, then you would probably use the python Decimal module :).



---

archive/issue_comments_065916.json:
```json
{
    "body": "My reason for initially working on this was for a numerical analysis class, where we wanted to see *all* the digits of the real number, and not just have the last few digits rounded off.",
    "created_at": "2010-05-28T02:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65916",
    "user": "jason"
}
```

My reason for initially working on this was for a numerical analysis class, where we wanted to see *all* the digits of the real number, and not just have the last few digits rounded off.



---

archive/issue_comments_065917.json:
```json
{
    "body": "#9261 asks for one of the features implemented in this patch (setting the printing style for real interval fields).",
    "created_at": "2010-06-18T16:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65917",
    "user": "jason"
}
```

#9261 asks for one of the features implemented in this patch (setting the printing style for real interval fields).



---

archive/issue_comments_065918.json:
```json
{
    "body": "After experimenting for a few minutes, it looks like something like #9261 is almost implemented in this patch, but not quite.",
    "created_at": "2010-06-18T16:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65918",
    "user": "jason"
}
```

After experimenting for a few minutes, it looks like something like #9261 is almost implemented in this patch, but not quite.



---

archive/issue_comments_065919.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2010-06-18T17:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65919",
    "user": "jason"
}
```

apply on top of previous patch



---

archive/issue_comments_065920.json:
```json
{
    "body": "Attachment [trac-7682-realintervalfield-printing.patch](tarball://root/attachments/some-uuid/ticket7682/trac-7682-realintervalfield-printing.patch) by jason created at 2010-06-18 17:34:43\n\nI added a patch which implements the feature wanted in #9261:\n\n\n```\nsage: R=RealIntervalField(print_options=dict(style='brackets'))\nsage: R.print_options\n{'style': 'brackets', 'error_digits': 0}\nsage: R(1,2)\n[1.0000000000000000 .. 2.0000000000000000]\n```\n\n\nDoctests and documentation still needs to be written for this.  And maybe convenience functions for setting these two options (i.e., make the syntax in #9261 work).",
    "created_at": "2010-06-18T17:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65920",
    "user": "jason"
}
```

Attachment [trac-7682-realintervalfield-printing.patch](tarball://root/attachments/some-uuid/ticket7682/trac-7682-realintervalfield-printing.patch) by jason created at 2010-06-18 17:34:43

I added a patch which implements the feature wanted in #9261:


```
sage: R=RealIntervalField(print_options=dict(style='brackets'))
sage: R.print_options
{'style': 'brackets', 'error_digits': 0}
sage: R(1,2)
[1.0000000000000000 .. 2.0000000000000000]
```


Doctests and documentation still needs to be written for this.  And maybe convenience functions for setting these two options (i.e., make the syntax in #9261 work).



---

archive/issue_comments_065921.json:
```json
{
    "body": "Jason,\n\nsorry, I was not aware of this ticket. I see you have invested a lot of time in it. However I am\nnot in favour of removing trailing zeroes by default. Those zeroes are quite helpful to give an\nidea of the accuracy of the computation.\n\nAbout reducing or increasing the number of printed zeroes with respect to the internal precision,\nI don't see why this could be desirable. If we reduce the number of printed zeroes, then if we\ncopy/paste the number, we will loose some accuracy (because of the decimal<->binary conversion).\nIf we increase the number of printed zeroes, the user will see more significant digits (due to\nthe internal binary representation) and this will lead to more user questions:\n\n```\nsage: a=n(pi); a\n3.14159265358979\nsage: print '%.3f'%a\n3.142\nsage: b=3.142; a-b\n-0.000407346410206788\nsage: print '%.30f'%a\n3.141592653589793115997963468544\n```\n\n\nIn addition I don't understand how you achieve this:\n\n```\nsage: RR.print_trailing_zeros=False\nsage: RR.print_digits=None\nsage: 3.09384\n3.09384\n```\n\nWhat happens with `RR.print_digits=16`?\n\nAlso, what happens with numbers with tiny or huge exponent, say `3.09384e-100` or\n`3.09384e+100`?\n\nJust my 2 cents.\n\nPaul\n\nPS: however, the patch for #9261 looks very nice. Can't you make it independent of that ticket?",
    "created_at": "2010-06-19T09:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65921",
    "user": "zimmerma"
}
```

Jason,

sorry, I was not aware of this ticket. I see you have invested a lot of time in it. However I am
not in favour of removing trailing zeroes by default. Those zeroes are quite helpful to give an
idea of the accuracy of the computation.

About reducing or increasing the number of printed zeroes with respect to the internal precision,
I don't see why this could be desirable. If we reduce the number of printed zeroes, then if we
copy/paste the number, we will loose some accuracy (because of the decimal<->binary conversion).
If we increase the number of printed zeroes, the user will see more significant digits (due to
the internal binary representation) and this will lead to more user questions:

```
sage: a=n(pi); a
3.14159265358979
sage: print '%.3f'%a
3.142
sage: b=3.142; a-b
-0.000407346410206788
sage: print '%.30f'%a
3.141592653589793115997963468544
```


In addition I don't understand how you achieve this:

```
sage: RR.print_trailing_zeros=False
sage: RR.print_digits=None
sage: 3.09384
3.09384
```

What happens with `RR.print_digits=16`?

Also, what happens with numbers with tiny or huge exponent, say `3.09384e-100` or
`3.09384e+100`?

Just my 2 cents.

Paul

PS: however, the patch for #9261 looks very nice. Can't you make it independent of that ticket?



---

archive/issue_comments_065922.json:
```json
{
    "body": "Replying to [comment:25 zimmerma]:\n> Jason,\n> \n> sorry, I was not aware of this ticket. I see you have invested a lot of time in it. However I am\n> not in favour of removing trailing zeroes by default. Those zeroes are quite helpful to give an\n> idea of the accuracy of the computation.\n\nI agree. That's the default in Sage now, though (and led to this patch, as it was hiding too much in my numerical analysis class!)\n\nSo changing it should probably be a different ticket, and after this patch, should just be a one liner change to the defaults.\n\n\n> \n> About reducing or increasing the number of printed zeroes with respect to the internal precision,\n> I don't see why this could be desirable. If we reduce the number of printed zeroes, then if we\n> copy/paste the number, we will loose some accuracy (because of the decimal<->binary conversion).\n> If we increase the number of printed zeroes, the user will see more significant digits (due to\n> the internal binary representation) and this will lead to more user questions:\n> {{{\n> sage: a=n(pi); a\n> 3.14159265358979\n> sage: print '%.3f'%a\n> 3.142\n> sage: b=3.142; a-b\n> -0.000407346410206788\n> sage: print '%.30f'%a\n> 3.141592653589793115997963468544\n> }}}\n> \n> In addition I don't understand how you achieve this:\n> {{{\n> sage: RR.print_trailing_zeros=False\n> sage: RR.print_digits=None\n> sage: 3.09384\n> 3.09384\n> }}}\n> What happens with `RR.print_digits=16`?\n> \n> Also, what happens with numbers with tiny or huge exponent, say `3.09384e-100` or\n> `3.09384e+100`?\n\nGood questions.  It's been a while since I worked with this patch (other than the rough patch from yesterday).  I'll try to see what changes are changes I made, as opposed to what things were already in Sage.  The things that were already in Sage can be dealt with on another ticket.\n\n\n> \n> Just my 2 cents.\n> \n> Paul\n> \n> PS: however, the patch for #9261 looks very nice. Can't you make it independent of that ticket?\n\nYes, though it's easier to build on top of the framework here, and I hope better in the long run.",
    "created_at": "2010-06-19T12:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65922",
    "user": "jason"
}
```

Replying to [comment:25 zimmerma]:
> Jason,
> 
> sorry, I was not aware of this ticket. I see you have invested a lot of time in it. However I am
> not in favour of removing trailing zeroes by default. Those zeroes are quite helpful to give an
> idea of the accuracy of the computation.

I agree. That's the default in Sage now, though (and led to this patch, as it was hiding too much in my numerical analysis class!)

So changing it should probably be a different ticket, and after this patch, should just be a one liner change to the defaults.


> 
> About reducing or increasing the number of printed zeroes with respect to the internal precision,
> I don't see why this could be desirable. If we reduce the number of printed zeroes, then if we
> copy/paste the number, we will loose some accuracy (because of the decimal<->binary conversion).
> If we increase the number of printed zeroes, the user will see more significant digits (due to
> the internal binary representation) and this will lead to more user questions:
> {{{
> sage: a=n(pi); a
> 3.14159265358979
> sage: print '%.3f'%a
> 3.142
> sage: b=3.142; a-b
> -0.000407346410206788
> sage: print '%.30f'%a
> 3.141592653589793115997963468544
> }}}
> 
> In addition I don't understand how you achieve this:
> {{{
> sage: RR.print_trailing_zeros=False
> sage: RR.print_digits=None
> sage: 3.09384
> 3.09384
> }}}
> What happens with `RR.print_digits=16`?
> 
> Also, what happens with numbers with tiny or huge exponent, say `3.09384e-100` or
> `3.09384e+100`?

Good questions.  It's been a while since I worked with this patch (other than the rough patch from yesterday).  I'll try to see what changes are changes I made, as opposed to what things were already in Sage.  The things that were already in Sage can be dealt with on another ticket.


> 
> Just my 2 cents.
> 
> Paul
> 
> PS: however, the patch for #9261 looks very nice. Can't you make it independent of that ticket?

Yes, though it's easier to build on top of the framework here, and I hope better in the long run.



---

archive/issue_comments_065923.json:
```json
{
    "body": "Applying these patches to 4.4.2 gives several doctest errors like this:\n\n\n```\nsage -t  \"4.4.2-test3/devel/sage-main/sage/rings/rational_field.py\"\n**********************************************************************\nFile \"/Users/grout/sage-4.4.2-test3/devel/sage-main/sage/rings/rational_field.py\", line 26:\n    sage: QQ(RealField(9).pi())\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/grout/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/grout/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/grout/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[4]>\", line 1, in <module>\n        QQ(RealField(Integer(9)).pi())###line 26:\n    sage: QQ(RealField(9).pi())\n      File \"parent.pyx\", line 854, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)\n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)\n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)\n      File \"rational.pyx\", line 367, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)\n        self.__set_value(x, base)\n      File \"rational.pyx\", line 455, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:6223)\n        set_from_Rational(self, x.simplest_rational())\n      File \"real_mpfr.pyx\", line 2762, in sage.rings.real_mpfr.RealNumber.simplest_rational (sage/rings/real_mpfr.c:17811)\n        return hp_intv.simplest_rational(low_open=odd, high_open=odd)\n      File \"real_mpfi.pyx\", line 2742, in sage.rings.real_mpfi.RealIntervalFieldElement.simplest_rational (sage/rings/real_mpfi.c:14640)\n        highprec = RealIntervalField_class(int(self.prec() * 1.2))(self)\n      File \"real_mpfi.pyx\", line 472, in sage.rings.real_mpfi.RealIntervalField_class.__init__ (sage/rings/real_mpfi.c:3522)\n        for key,val in print_options.items():\n    AttributeError: 'NoneType' object has no attribute 'items'\n\n```\n",
    "created_at": "2010-07-11T06:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65923",
    "user": "jason"
}
```

Applying these patches to 4.4.2 gives several doctest errors like this:


```
sage -t  "4.4.2-test3/devel/sage-main/sage/rings/rational_field.py"
**********************************************************************
File "/Users/grout/sage-4.4.2-test3/devel/sage-main/sage/rings/rational_field.py", line 26:
    sage: QQ(RealField(9).pi())
Exception raised:
    Traceback (most recent call last):
      File "/Users/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[4]>", line 1, in <module>
        QQ(RealField(Integer(9)).pi())###line 26:
    sage: QQ(RealField(9).pi())
      File "parent.pyx", line 854, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)
      File "rational.pyx", line 367, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)
        self.__set_value(x, base)
      File "rational.pyx", line 455, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:6223)
        set_from_Rational(self, x.simplest_rational())
      File "real_mpfr.pyx", line 2762, in sage.rings.real_mpfr.RealNumber.simplest_rational (sage/rings/real_mpfr.c:17811)
        return hp_intv.simplest_rational(low_open=odd, high_open=odd)
      File "real_mpfi.pyx", line 2742, in sage.rings.real_mpfi.RealIntervalFieldElement.simplest_rational (sage/rings/real_mpfi.c:14640)
        highprec = RealIntervalField_class(int(self.prec() * 1.2))(self)
      File "real_mpfi.pyx", line 472, in sage.rings.real_mpfi.RealIntervalField_class.__init__ (sage/rings/real_mpfi.c:3522)
        for key,val in print_options.items():
    AttributeError: 'NoneType' object has no attribute 'items'

```




---

archive/issue_comments_065924.json:
```json
{
    "body": "It appears that the problem above occurs with just the last patch.",
    "created_at": "2010-07-11T06:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65924",
    "user": "jason"
}
```

It appears that the problem above occurs with just the last patch.



---

archive/issue_comments_065925.json:
```json
{
    "body": "Paul: I think I understand your comment now.  I did not implement the original suggestion, but instead provided a framework for field-wide printing options and just wrapped what Sage currently provides.  You bring up some good questions about the design which are out of scope for the current patch attached.  Given this, I think it would be best to either change the scope of the ticket to reflect what the patch actually does, or make a new ticket for the patch and keep this ticket around for a design discussion of how (or whether it is desirable!) to implement the features described in the description.",
    "created_at": "2010-07-11T07:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65925",
    "user": "jason"
}
```

Paul: I think I understand your comment now.  I did not implement the original suggestion, but instead provided a framework for field-wide printing options and just wrapped what Sage currently provides.  You bring up some good questions about the design which are out of scope for the current patch attached.  Given this, I think it would be best to either change the scope of the ticket to reflect what the patch actually does, or make a new ticket for the patch and keep this ticket around for a design discussion of how (or whether it is desirable!) to implement the features described in the description.



---

archive/issue_comments_065926.json:
```json
{
    "body": "Replying to [comment:29 jason]:\n> it would be best to either change the scope of the ticket to reflect what the patch actually does\nI would prefer this.\n\nPaul",
    "created_at": "2010-07-11T16:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65926",
    "user": "zimmerma"
}
```

Replying to [comment:29 jason]:
> it would be best to either change the scope of the ticket to reflect what the patch actually does
I would prefer this.

Paul



---

archive/issue_comments_065927.json:
```json
{
    "body": "I actually dislike the goal of this patch: I don't think it's a good idea to have `RealNumber` printing varied per-parent, and certainly not if the printing is mutable.  Consider:\n\nSomebody wants to know what 128 bits of $\\pi$ prints as in scientific notation:\n\n\n```\nsage: RR128 = RealField(128)\nsage: RR128.print_options['scientific_notation'] = 'always'\nsage: RR128(pi)\n3.1415926535897932384626433832795028842e0\n```\n\n\nThen, days later (but in the same Sage session) they're playing around with the internals of AA/QQbar:\n\n\n```\nsage: rt2 = AA(sqrt(2))\nsage: rt2._value.center()\n1.41421356237309505\nsage: RealIntervalField(100)(rt2)\n1.414213562373095048801688724210?\nsage: rt2._value.center()\n1.4142135623730950488016887242096980786e0\n```\n\n\nWhy is that last number printed in scientific notation?  Oh yes, it's because we changed RR128 days ago.\n\nI realize that you're just extending a design that's been in Sage for years (since before I started working on Sage), but IMHO it's a bad design, and this just makes it worse.\n\nI can think of two ways to fix this:\n\n1) Get rid of per-field printing options altogether; only have a single global setting that affects all `RealField`s.\n\n2) Make the print options immutable, so that creating RR128scientific_notation doesn't affect anybody else who might create RR128 without scientific notation.\n\nMy vote would be for option 1, but I could live with either option.",
    "created_at": "2010-07-11T19:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65927",
    "user": "cwitty"
}
```

I actually dislike the goal of this patch: I don't think it's a good idea to have `RealNumber` printing varied per-parent, and certainly not if the printing is mutable.  Consider:

Somebody wants to know what 128 bits of $\pi$ prints as in scientific notation:


```
sage: RR128 = RealField(128)
sage: RR128.print_options['scientific_notation'] = 'always'
sage: RR128(pi)
3.1415926535897932384626433832795028842e0
```


Then, days later (but in the same Sage session) they're playing around with the internals of AA/QQbar:


```
sage: rt2 = AA(sqrt(2))
sage: rt2._value.center()
1.41421356237309505
sage: RealIntervalField(100)(rt2)
1.414213562373095048801688724210?
sage: rt2._value.center()
1.4142135623730950488016887242096980786e0
```


Why is that last number printed in scientific notation?  Oh yes, it's because we changed RR128 days ago.

I realize that you're just extending a design that's been in Sage for years (since before I started working on Sage), but IMHO it's a bad design, and this just makes it worse.

I can think of two ways to fix this:

1) Get rid of per-field printing options altogether; only have a single global setting that affects all `RealField`s.

2) Make the print options immutable, so that creating RR128scientific_notation doesn't affect anybody else who might create RR128 without scientific notation.

My vote would be for option 1, but I could live with either option.



---

archive/issue_comments_065928.json:
```json
{
    "body": "Replying to [comment:32 cwitty]:\n> I actually dislike the goal of this patch: I don't think it's a good idea to have `RealNumber` printing varied per-parent, and certainly not if the printing is mutable.  Consider:\n> \n> Somebody wants to know what 128 bits of $\\pi$ prints as in scientific notation:\n> \n> {{{\n> sage: RR128 = RealField(128)\n> sage: RR128.print_options['scientific_notation'] = 'always'\n> sage: RR128(pi)\n> 3.1415926535897932384626433832795028842e0\n> }}}\n> \n> Then, days later (but in the same Sage session) they're playing around with the internals of AA/QQbar:\n> \n> {{{\n> sage: rt2 = AA(sqrt(2))\n> sage: rt2._value.center()\n> 1.41421356237309505\n> sage: RealIntervalField(100)(rt2)\n> 1.414213562373095048801688724210?\n> sage: rt2._value.center()\n> 1.4142135623730950488016887242096980786e0\n> }}}\n> \n> Why is that last number printed in scientific notation?  Oh yes, it's because we changed RR128 days ago.\n> \n> I realize that you're just extending a design that's been in Sage for years (since before I started working on Sage), but IMHO it's a bad design, and this just makes it worse.\n> \n> I can think of two ways to fix this:\n> \n> 1) Get rid of per-field printing options altogether; only have a single global setting that affects all `RealField`s.\n> \n> 2) Make the print options immutable, so that creating RR128scientific_notation doesn't affect anybody else who might create RR128 without scientific notation.\n> \n> My vote would be for option 1, but I could live with either option.\n\n\nI agree.  Another reason to add to your argument above is that Sage does coercing between different realfield precisions, so you might have a number that is printed one way, then Sage automatically coerces to a different precision for an operation and your result is printed a different way.  I think (1) is a better option, given the caching strategy used.\n\nFor my use-case (teaching numerical analysis), option (1) is better than the patch on this ticket.\n\nSo do you propose eliminating the sci_not options to RealField?  Do you propose eliminating the arguments to the str function?\n\nNote that I think your suggestion will be relatively straightforward to accommodate on this patch, since the patch defines module-level defaults.  We should be able to just remove the code that overrides the module-level defaults and stores a user value.  Note that this patch also unifies several different options for scientific notation that were scattered in different places in the code, so I think it is better to build (or cut things out) on this patch rather than throw it away altogether.",
    "created_at": "2010-07-12T14:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65928",
    "user": "jason"
}
```

Replying to [comment:32 cwitty]:
> I actually dislike the goal of this patch: I don't think it's a good idea to have `RealNumber` printing varied per-parent, and certainly not if the printing is mutable.  Consider:
> 
> Somebody wants to know what 128 bits of $\pi$ prints as in scientific notation:
> 
> {{{
> sage: RR128 = RealField(128)
> sage: RR128.print_options['scientific_notation'] = 'always'
> sage: RR128(pi)
> 3.1415926535897932384626433832795028842e0
> }}}
> 
> Then, days later (but in the same Sage session) they're playing around with the internals of AA/QQbar:
> 
> {{{
> sage: rt2 = AA(sqrt(2))
> sage: rt2._value.center()
> 1.41421356237309505
> sage: RealIntervalField(100)(rt2)
> 1.414213562373095048801688724210?
> sage: rt2._value.center()
> 1.4142135623730950488016887242096980786e0
> }}}
> 
> Why is that last number printed in scientific notation?  Oh yes, it's because we changed RR128 days ago.
> 
> I realize that you're just extending a design that's been in Sage for years (since before I started working on Sage), but IMHO it's a bad design, and this just makes it worse.
> 
> I can think of two ways to fix this:
> 
> 1) Get rid of per-field printing options altogether; only have a single global setting that affects all `RealField`s.
> 
> 2) Make the print options immutable, so that creating RR128scientific_notation doesn't affect anybody else who might create RR128 without scientific notation.
> 
> My vote would be for option 1, but I could live with either option.


I agree.  Another reason to add to your argument above is that Sage does coercing between different realfield precisions, so you might have a number that is printed one way, then Sage automatically coerces to a different precision for an operation and your result is printed a different way.  I think (1) is a better option, given the caching strategy used.

For my use-case (teaching numerical analysis), option (1) is better than the patch on this ticket.

So do you propose eliminating the sci_not options to RealField?  Do you propose eliminating the arguments to the str function?

Note that I think your suggestion will be relatively straightforward to accommodate on this patch, since the patch defines module-level defaults.  We should be able to just remove the code that overrides the module-level defaults and stores a user value.  Note that this patch also unifies several different options for scientific notation that were scattered in different places in the code, so I think it is better to build (or cut things out) on this patch rather than throw it away altogether.



---

archive/issue_comments_065929.json:
```json
{
    "body": "So do you propose eliminating the sci_not options to RealField?? Do you propose eliminating the arguments to the str function? \n\nYes, my vote would be to eliminate sci_not in `RealField`.  No, I don't see any reason to eliminate the arguments to str(); if you want to convert a single number to a string in some special way (with scientific notation, say), then it's a lot easier to call .str(scientific_notation='always') than to type something like:\n\n\n```\n  old = sage.rings.real_mpfr._PRINT_OPTIONS['scientific_notation']\n  sage.rings.real_mpfr._PRINT_OPTIONS['scientific_notation'] = 'always'\n  foostr = foo.str()\n  sage.rings.real_mpfr._PRINT_OPTIONS['scientific_notation'] = old\n```\n\n\nFurther comments:\n\nI haven't really reviewed the actual patch, but I did just notice that the new docstring for .str() has no doctests for no_sci.  I think it should end with something like:\n\n\n```\nTESTS:\n\nHere we test the deprecated no_sci argument to .str()::\n```\n\n\nfollowed by the tests for no_sci that used to be there (assuming there were some, I haven't actually checked).",
    "created_at": "2010-07-12T16:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65929",
    "user": "cwitty"
}
```

So do you propose eliminating the sci_not options to RealField?? Do you propose eliminating the arguments to the str function? 

Yes, my vote would be to eliminate sci_not in `RealField`.  No, I don't see any reason to eliminate the arguments to str(); if you want to convert a single number to a string in some special way (with scientific notation, say), then it's a lot easier to call .str(scientific_notation='always') than to type something like:


```
  old = sage.rings.real_mpfr._PRINT_OPTIONS['scientific_notation']
  sage.rings.real_mpfr._PRINT_OPTIONS['scientific_notation'] = 'always'
  foostr = foo.str()
  sage.rings.real_mpfr._PRINT_OPTIONS['scientific_notation'] = old
```


Further comments:

I haven't really reviewed the actual patch, but I did just notice that the new docstring for .str() has no doctests for no_sci.  I think it should end with something like:


```
TESTS:

Here we test the deprecated no_sci argument to .str()::
```


followed by the tests for no_sci that used to be there (assuming there were some, I haven't actually checked).



---

archive/issue_comments_065930.json:
```json
{
    "body": "ping (?)",
    "created_at": "2011-07-22T09:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65930",
    "user": "leif"
}
```

ping (?)



---

archive/issue_comments_065931.json:
```json
{
    "body": "pong.  I would love to see this ticket resolved, but as you can see, there is another major rewrite needed before it is ready.",
    "created_at": "2011-07-22T14:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65931",
    "user": "jason"
}
```

pong.  I would love to see this ticket resolved, but as you can see, there is another major rewrite needed before it is ready.



---

archive/issue_comments_065932.json:
```json
{
    "body": "How lovely to revive an 8 year old ticket ...\n\nIn the mean time, python has grown a new string formatting method. If we implement a `__format__` method on our mpfr wrapper, one could just do something like\n\n```\nsage: a=RealField(200)(2).sqrt()\nsage: \"{:.20e}\".format(a)\n'1.414213562373095049e0'\n```\n\nNo need to fuss with global state ... if people want more control over the typesetting of their floats, they can just use the standard python tools (or the tools already available on `str`).\n\nIt might be a nice beginner's exercise to write the appropriate `__format__`.",
    "created_at": "2018-05-20T06:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65932",
    "user": "nbruin"
}
```

How lovely to revive an 8 year old ticket ...

In the mean time, python has grown a new string formatting method. If we implement a `__format__` method on our mpfr wrapper, one could just do something like

```
sage: a=RealField(200)(2).sqrt()
sage: "{:.20e}".format(a)
'1.414213562373095049e0'
```

No need to fuss with global state ... if people want more control over the typesetting of their floats, they can just use the standard python tools (or the tools already available on `str`).

It might be a nice beginner's exercise to write the appropriate `__format__`.



---

archive/issue_comments_065933.json:
```json
{
    "body": "I wanted to have fun with `e` to the power of `\u03c0\u221a163`\n\nI expected Sage would print me `262537412640768743.99999999999925`\n\n```\nsage: R = RealField(1500)\nsage: a = R(e) ** (R(pi) * R(163).sqrt())\nsage: a.n(digits=33)\n2.62537412640768743999999999999250e17\nsage: \"{:.70f}\".format(a)\nTypeError: unsupported format string passed to sage.rings.real_mpfr.RealNumber.__format__\n```\n\nis there a way to print `2.62537412640768743999999999999250e17` as `262537412640768743.99999999999925`?",
    "created_at": "2019-04-14T09:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65933",
    "user": "@sheerluck"
}
```

I wanted to have fun with `e` to the power of `π√163`

I expected Sage would print me `262537412640768743.99999999999925`

```
sage: R = RealField(1500)
sage: a = R(e) ** (R(pi) * R(163).sqrt())
sage: a.n(digits=33)
2.62537412640768743999999999999250e17
sage: "{:.70f}".format(a)
TypeError: unsupported format string passed to sage.rings.real_mpfr.RealNumber.__format__
```

is there a way to print `2.62537412640768743999999999999250e17` as `262537412640768743.99999999999925`?



---

archive/issue_comments_065934.json:
```json
{
    "body": "Replying to [comment:44 gh-sheerluck]:\n> I wanted to have fun with `e` to the power of `\u03c0\u221a163`\n> \n> I expected Sage would print me `262537412640768743.99999999999925`\n> {{{\n> sage: R = RealField(1500)\n> sage: a = R(e) ** (R(pi) * R(163).sqrt())\n> sage: a.n(digits=33)\n> 2.62537412640768743999999999999250e17\n> sage: \"{:.70f}\".format(a)\n> TypeError: unsupported format string passed to sage.rings.real_mpfr.RealNumber.__format__\n> }}}\n> is there a way to print `2.62537412640768743999999999999250e17` as `262537412640768743.99999999999925`?\n\nA solution is:\n\n```\nsage: n(exp(pi*sqrt(163)), digits=33).str(no_sci=2)\n'262537412640768743.999999999999249212'\n```\n",
    "created_at": "2019-04-14T09:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65934",
    "user": "egourgoulhon"
}
```

Replying to [comment:44 gh-sheerluck]:
> I wanted to have fun with `e` to the power of `π√163`
> 
> I expected Sage would print me `262537412640768743.99999999999925`
> {{{
> sage: R = RealField(1500)
> sage: a = R(e) ** (R(pi) * R(163).sqrt())
> sage: a.n(digits=33)
> 2.62537412640768743999999999999250e17
> sage: "{:.70f}".format(a)
> TypeError: unsupported format string passed to sage.rings.real_mpfr.RealNumber.__format__
> }}}
> is there a way to print `2.62537412640768743999999999999250e17` as `262537412640768743.99999999999925`?

A solution is:

```
sage: n(exp(pi*sqrt(163)), digits=33).str(no_sci=2)
'262537412640768743.999999999999249212'
```




---

archive/issue_comments_065935.json:
```json
{
    "body": "Replying to [comment:45 egourgoulhon]:\n> \n> A solution is:\n> {{{\n> sage: n(exp(pi*sqrt(163)), digits=33).str(no_sci=2)\n> '262537412640768743.999999999999249212'\n> }}}\nThank you!",
    "created_at": "2019-04-14T10:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7682#issuecomment-65935",
    "user": "@sheerluck"
}
```

Replying to [comment:45 egourgoulhon]:
> 
> A solution is:
> {{{
> sage: n(exp(pi*sqrt(163)), digits=33).str(no_sci=2)
> '262537412640768743.999999999999249212'
> }}}
Thank you!
