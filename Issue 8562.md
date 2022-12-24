# Issue 8562: Categories for IntegerMod rings

archive/issues_008562.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  sage-combinat\n\nKeywords: categories, integer mod rings\n\nAfter this patch, IntegerModRing's inherit properly from categories:\n\n```\n    sage: Z3 = IntegerModRing(3)\n    sage: Z3.category()\n    Category of fields\n    sage: TestSuite(Z3).run(verbose = True)\n    running ._test_additive_associativity() . . . pass\n    running ._test_an_element() . . . pass\n    running ._test_associativity() . . . pass\n    running ._test_category() . . . pass\n    running ._test_elements() . . . \n      Running the test suite of self.an_element()\n      running ._test_category() . . . pass\n      running ._test_not_implemented_methods() . . . pass\n      running ._test_pickling() . . . pass\n      pass\n    running ._test_not_implemented_methods() . . . pass\n    running ._test_one() . . . pass\n    running ._test_pickling() . . . pass\n    running ._test_prod() . . . pass\n    running ._test_some_elements() . . . pass\n    running ._test_zero() . . . pass\n```\n\n\nThis is required to use the cool features from #7555.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8562\n\n",
    "created_at": "2010-03-19T21:48:27Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Categories for IntegerMod rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8562",
    "user": "nthiery"
}
```
Assignee: AlexGhitza

CC:  sage-combinat

Keywords: categories, integer mod rings

After this patch, IntegerModRing's inherit properly from categories:

```
    sage: Z3 = IntegerModRing(3)
    sage: Z3.category()
    Category of fields
    sage: TestSuite(Z3).run(verbose = True)
    running ._test_additive_associativity() . . . pass
    running ._test_an_element() . . . pass
    running ._test_associativity() . . . pass
    running ._test_category() . . . pass
    running ._test_elements() . . . 
      Running the test suite of self.an_element()
      running ._test_category() . . . pass
      running ._test_not_implemented_methods() . . . pass
      running ._test_pickling() . . . pass
      pass
    running ._test_not_implemented_methods() . . . pass
    running ._test_one() . . . pass
    running ._test_pickling() . . . pass
    running ._test_prod() . . . pass
    running ._test_some_elements() . . . pass
    running ._test_zero() . . . pass
```


This is required to use the cool features from #7555.

Issue created by migration from https://trac.sagemath.org/ticket/8562





---

archive/issue_comments_077514.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-03-19T22:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77514",
    "user": "nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_077515.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-19T23:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77515",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077516.json:
```json
{
    "body": "Ok, the tests passed fine up to some trivialities (*_with_category class name changes). I'll fix this and upload an updated patch soon. The review can start in parallel",
    "created_at": "2010-03-19T23:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77516",
    "user": "nthiery"
}
```

Ok, the tests passed fine up to some trivialities (*_with_category class name changes). I'll fix this and upload an updated patch soon. The review can start in parallel



---

archive/issue_comments_077517.json:
```json
{
    "body": "This applies, builds and limited testing (prime and composite orders) indicates that it plays nicely with \"addition tables\" at #7555 which rely heavily on the category framework.  Didn't run tests, but witnessed no problems otherwise.\n\nGood to see how easy it is to insert a new object into the category framework.\n\nI'll come back when the patch is completed.",
    "created_at": "2010-03-20T04:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77517",
    "user": "rbeezer"
}
```

This applies, builds and limited testing (prime and composite orders) indicates that it plays nicely with "addition tables" at #7555 which rely heavily on the category framework.  Didn't run tests, but witnessed no problems otherwise.

Good to see how easy it is to insert a new object into the category framework.

I'll come back when the patch is completed.



---

archive/issue_comments_077518.json:
```json
{
    "body": "Just a heads-up: this looks rather like it might clash with #8218, which is the first of several patches by David Roe which do a substantial amount of work improving finite fields. #8218 has been held up for ages because it moves loads of files around (without substantially changing their content) so even small changes to finite fields will cause conflicts, and there is a lot of really good code waiting on it, so it would be a shame to have to put it off even longer.\n\nDavid",
    "created_at": "2010-03-21T14:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77518",
    "user": "davidloeffler"
}
```

Just a heads-up: this looks rather like it might clash with #8218, which is the first of several patches by David Roe which do a substantial amount of work improving finite fields. #8218 has been held up for ages because it moves loads of files around (without substantially changing their content) so even small changes to finite fields will cause conflicts, and there is a lot of really good code waiting on it, so it would be a shame to have to put it off even longer.

David



---

archive/issue_comments_077519.json:
```json
{
    "body": "Replying to [comment:4 davidloeffler]:\n> Just a heads-up: this looks rather like it might clash with #8218, which is the first of several patches by David Roe which do a substantial amount of work improving finite fields. #8218 has been held up for ages because it moves loads of files around (without substantially changing their content) so even small changes to finite fields will cause conflicts, and there is a lot of really good code waiting on it, so it would be a shame to have to put it off even longer.\n\nThanks for the notice. There is no urgency for that one, so sure, if there is any conflict, #8218 should go first.\n\nDavid: I won't be touching this patch further. Feel free to update / refactor / merge /... it within the other series of patch whenever it feels right.",
    "created_at": "2010-03-21T20:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77519",
    "user": "nthiery"
}
```

Replying to [comment:4 davidloeffler]:
> Just a heads-up: this looks rather like it might clash with #8218, which is the first of several patches by David Roe which do a substantial amount of work improving finite fields. #8218 has been held up for ages because it moves loads of files around (without substantially changing their content) so even small changes to finite fields will cause conflicts, and there is a lot of really good code waiting on it, so it would be a shame to have to put it off even longer.

Thanks for the notice. There is no urgency for that one, so sure, if there is any conflict, #8218 should go first.

David: I won't be touching this patch further. Feel free to update / refactor / merge /... it within the other series of patch whenever it feels right.



---

archive/issue_comments_077520.json:
```json
{
    "body": "> David: I won't be touching this patch further. Feel free to update / refactor / merge /... it within the other series of patch whenever it feels right.\n\nNote: I meant David Roe, but any other David is welcome too :-)\n\nOh: would you agree to take over that patch, and finalize it (or ping me) when it's ripe to get in?\n\n(then I could forget about it).",
    "created_at": "2010-03-21T20:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77520",
    "user": "nthiery"
}
```

> David: I won't be touching this patch further. Feel free to update / refactor / merge /... it within the other series of patch whenever it feels right.

Note: I meant David Roe, but any other David is welcome too :-)

Oh: would you agree to take over that patch, and finalize it (or ping me) when it's ripe to get in?

(then I could forget about it).



---

archive/issue_comments_077521.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-21T20:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77521",
    "user": "nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077522.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-22T22:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77522",
    "user": "nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_077523.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-22T22:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77523",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077524.json:
```json
{
    "body": "Replying to [comment:6 nthiery]:\n> > David: I won't be touching this patch further. Feel free to update / refactor / merge /... it within the other series of patch whenever it feels right.\n\nWell, actually I did. But I should be done now, unless I notice a test failure.",
    "created_at": "2010-03-22T22:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77524",
    "user": "nthiery"
}
```

Replying to [comment:6 nthiery]:
> > David: I won't be touching this patch further. Feel free to update / refactor / merge /... it within the other series of patch whenever it feels right.

Well, actually I did. But I should be done now, unless I notice a test failure.



---

archive/issue_comments_077525.json:
```json
{
    "body": "Attachment [trac_8562-category-integer_mod_ring-nt.patch](tarball://root/attachments/some-uuid/ticket8562/trac_8562-category-integer_mod_ring-nt.patch) by nthiery created at 2010-03-22 22:24:12",
    "created_at": "2010-03-22T22:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77525",
    "user": "nthiery"
}
```

Attachment [trac_8562-category-integer_mod_ring-nt.patch](tarball://root/attachments/some-uuid/ticket8562/trac_8562-category-integer_mod_ring-nt.patch) by nthiery created at 2010-03-22 22:24:12



---

archive/issue_comments_077526.json:
```json
{
    "body": "Here's a rebased patch.  It looks good and all tests pass for me so I'm willing to give it a positive review, but since I made the rebased patch, can someone else (Nicolas, for example) take a look at it also?",
    "created_at": "2010-06-21T18:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77526",
    "user": "jhpalmieri"
}
```

Here's a rebased patch.  It looks good and all tests pass for me so I'm willing to give it a positive review, but since I made the rebased patch, can someone else (Nicolas, for example) take a look at it also?



---

archive/issue_comments_077527.json:
```json
{
    "body": "Hi John!\n\nThanks much for rebasing the patch. I looked through the changes, and am happy to give my green light, up to three minor comments:\n\n* Is the convention to use as ticket summary \"trac 8562:\" or \"#8562:\"? (I personally prefer the later).\n* With the updated patch, sage -coverage complains because of the absence of #indirect doctest for create_object in sage/rings/finite_rings/integer_mod_ring.py. Just wanted to check; if this is voluntary, because you consider that this requires better tests, that's all fine with me.\n* I like the options `nodates=1` and `showfunc = 1` of hg :-)\n\nI let you set up the positive review as you feel appropriate.\n\nThanks again,\n                          Nicolas",
    "created_at": "2010-06-21T20:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77527",
    "user": "nthiery"
}
```

Hi John!

Thanks much for rebasing the patch. I looked through the changes, and am happy to give my green light, up to three minor comments:

* Is the convention to use as ticket summary "trac 8562:" or "#8562:"? (I personally prefer the later).
* With the updated patch, sage -coverage complains because of the absence of #indirect doctest for create_object in sage/rings/finite_rings/integer_mod_ring.py. Just wanted to check; if this is voluntary, because you consider that this requires better tests, that's all fine with me.
* I like the options `nodates=1` and `showfunc = 1` of hg :-)

I let you set up the positive review as you feel appropriate.

Thanks again,
                          Nicolas



---

archive/issue_comments_077528.json:
```json
{
    "body": "Replying to [comment:10 nthiery]:\n \n> Is the convention to use as ticket summary \"trac 8562:\" or \"#8562:\"? (I personally prefer the later).\n\nI think either is fine.  I've been using \"trac 8562\" for a while and have not had any complaints from release managers.\n\n>  * With the updated patch, sage -coverage complains because of the absence of #indirect doctest for create_object in sage/rings/finite_rings/integer_mod_ring.py. Just wanted to check; if this is voluntary, because you consider that this requires better tests, that's all fine with me.\n\nThis wasn't voluntary, it was an oversight.  I'll fix it.\n\n>  * I like the options `nodates=1` and `showfunc = 1` of hg :-)\n\nNice, I didn't know about those.",
    "created_at": "2010-06-21T20:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77528",
    "user": "jhpalmieri"
}
```

Replying to [comment:10 nthiery]:
 
> Is the convention to use as ticket summary "trac 8562:" or "#8562:"? (I personally prefer the later).

I think either is fine.  I've been using "trac 8562" for a while and have not had any complaints from release managers.

>  * With the updated patch, sage -coverage complains because of the absence of #indirect doctest for create_object in sage/rings/finite_rings/integer_mod_ring.py. Just wanted to check; if this is voluntary, because you consider that this requires better tests, that's all fine with me.

This wasn't voluntary, it was an oversight.  I'll fix it.

>  * I like the options `nodates=1` and `showfunc = 1` of hg :-)

Nice, I didn't know about those.



---

archive/issue_comments_077529.json:
```json
{
    "body": "rebased version. apply only this patch.",
    "created_at": "2010-06-21T20:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77529",
    "user": "jhpalmieri"
}
```

rebased version. apply only this patch.



---

archive/issue_comments_077530.json:
```json
{
    "body": "Attachment [trac_8562-rebased.patch](tarball://root/attachments/some-uuid/ticket8562/trac_8562-rebased.patch) by jhpalmieri created at 2010-06-21 20:37:58",
    "created_at": "2010-06-21T20:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77530",
    "user": "jhpalmieri"
}
```

Attachment [trac_8562-rebased.patch](tarball://root/attachments/some-uuid/ticket8562/trac_8562-rebased.patch) by jhpalmieri created at 2010-06-21 20:37:58



---

archive/issue_comments_077531.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-21T20:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77531",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077532.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8562#issuecomment-77532",
    "user": "mpatel"
}
```

Resolution: fixed
