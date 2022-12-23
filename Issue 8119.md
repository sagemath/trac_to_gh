# Issue 8119: Rename change the hash value of some objects

archive/issues_008119.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jason simonking\n\nFor many objects the hash value is computed from `__repr__`. This is a bad idea since renaming the object change its hash value.\n\n```\nsage: bla = PolynomialRing(ZZ,\"x\")\nsage: hash(bla)\n-1525918542791298668\nsage: bla.rename(\"toto\")\nsage: hash(bla)\n2314052222105390764\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8119\n\n",
    "created_at": "2010-01-29T15:22:48Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "Rename change the hash value of some objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8119",
    "user": "hivert"
}
```
Assignee: tbd

CC:  jason simonking

For many objects the hash value is computed from `__repr__`. This is a bad idea since renaming the object change its hash value.

```
sage: bla = PolynomialRing(ZZ,"x")
sage: hash(bla)
-1525918542791298668
sage: bla.rename("toto")
sage: hash(bla)
2314052222105390764
```


Issue created by migration from https://trac.sagemath.org/ticket/8119





---

archive/issue_comments_071330.json:
```json
{
    "body": "For immutable objects, like Parents, the default __hash__ could store the value used the first time it is computed. This doesn't solve the problem of \n\n\n```\nsage: bla = PolynomialRing(ZZ,\"x\")\nsage: hash(bla['t'])\n-1733828288\nsage: bla.rename(\"toto\")\nsage: hash(bla['t'])\n-1924319844\n```\n",
    "created_at": "2010-03-12T09:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71330",
    "user": "robertwb"
}
```

For immutable objects, like Parents, the default __hash__ could store the value used the first time it is computed. This doesn't solve the problem of 


```
sage: bla = PolynomialRing(ZZ,"x")
sage: hash(bla['t'])
-1733828288
sage: bla.rename("toto")
sage: hash(bla['t'])
-1924319844
```




---

archive/issue_comments_071331.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-12T09:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71331",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_071332.json:
```json
{
    "body": "This is a partial fix (that won't work for SageObject in general, unless we enforce that mutable objects maintain their own hash, and I don't think we want to put an extra field on all Elements), but resolves the most important case. It's also a performance gain.",
    "created_at": "2010-03-12T09:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71332",
    "user": "robertwb"
}
```

This is a partial fix (that won't work for SageObject in general, unless we enforce that mutable objects maintain their own hash, and I don't think we want to put an extra field on all Elements), but resolves the most important case. It's also a performance gain.



---

archive/issue_comments_071333.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-12T09:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71333",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071334.json:
```json
{
    "body": "Hi Robert,\n\nI've one question related to this and I like to have the confirmation from an expert. After your patch, upon pickling/unpickling the hash value can change because it is not pickled and neither is the name, right ? As far as I manage to test this is not harmful to pickle a dict containing a renamed parent. Indeed, trying to read `cPickle.c`, I understood that the dict is reconstructed from it's items and thus even if the hash changed the element is inserted correctly in the dict during unpickling. Can you confirm this ?\n\nIf this is not both this patch and #8120 are broken.\n\nAlso, after this, do you still need #8506 ?\n\nFlorent",
    "created_at": "2010-03-12T22:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71334",
    "user": "hivert"
}
```

Hi Robert,

I've one question related to this and I like to have the confirmation from an expert. After your patch, upon pickling/unpickling the hash value can change because it is not pickled and neither is the name, right ? As far as I manage to test this is not harmful to pickle a dict containing a renamed parent. Indeed, trying to read `cPickle.c`, I understood that the dict is reconstructed from it's items and thus even if the hash changed the element is inserted correctly in the dict during unpickling. Can you confirm this ?

If this is not both this patch and #8120 are broken.

Also, after this, do you still need #8506 ?

Florent



---

archive/issue_comments_071335.json:
```json
{
    "body": "Replying to [comment:3 hivert]:\n> Hi Robert,\n> \n> I've one question related to this and I like to have the confirmation from an expert. After your patch, upon pickling/unpickling the hash value can change because it is not pickled and neither is the name, right ? As far as I manage to test this is not harmful to pickle a dict containing a renamed parent. Indeed, trying to read `cPickle.c`, I understood that the dict is reconstructed from it's items and thus even if the hash changed the element is inserted correctly in the dict during unpickling. Can you confirm this ?\n\nThat is correct. Hashes in general are not guaranteed to be consistent from run to run, all that really matters is that they satisfy (to the best they can) the equality constraints. \n\n> If this is not both this patch and #8120 are broken.\n> \n> Also, after this, do you still need #8506 ?\n\nYes, #8506 is still important--in my case I'm reducing a curve mod many, many primes, doing just a bit of stuff on each before throwing them away. I suppose eventually caching the hash value would eventually be a win, but that's a separate optimization.",
    "created_at": "2010-03-13T09:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71335",
    "user": "robertwb"
}
```

Replying to [comment:3 hivert]:
> Hi Robert,
> 
> I've one question related to this and I like to have the confirmation from an expert. After your patch, upon pickling/unpickling the hash value can change because it is not pickled and neither is the name, right ? As far as I manage to test this is not harmful to pickle a dict containing a renamed parent. Indeed, trying to read `cPickle.c`, I understood that the dict is reconstructed from it's items and thus even if the hash changed the element is inserted correctly in the dict during unpickling. Can you confirm this ?

That is correct. Hashes in general are not guaranteed to be consistent from run to run, all that really matters is that they satisfy (to the best they can) the equality constraints. 

> If this is not both this patch and #8120 are broken.
> 
> Also, after this, do you still need #8506 ?

Yes, #8506 is still important--in my case I'm reducing a curve mod many, many primes, doing just a bit of stuff on each before throwing them away. I suppose eventually caching the hash value would eventually be a win, but that's a separate optimization.



---

archive/issue_comments_071336.json:
```json
{
    "body": "hivert: do you want to review this ticket?",
    "created_at": "2010-10-02T19:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71336",
    "user": "jason"
}
```

hivert: do you want to review this ticket?



---

archive/issue_comments_071337.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-04T17:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71337",
    "user": "hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071338.json:
```json
{
    "body": "> hivert: do you want to review this ticket?\n\nSure ! I completely forgot about this one. Sorry !\n\nThey are a few place where we should remove the bad implementation using `__repr__` since they all inherits from `CategoryObject`: \n\n```\npopcorn-*ge-combinat/sage $ grep \"hash(self.__repr__())\" **/*.py*\ngroups/group.pyx:        return hash(self.__repr__())\nmodules/module.pyx:        return hash(self.__repr__())\nmodules/module.pyx:        return hash(self.__repr__())\nrings/polynomial/multi_polynomial_libsingular.pyx:        return hash(self.__repr__())\nrings/ring.pyx:        return hash(self.__repr__())\nstructure/sage_object.pyx:        return hash(self.__repr__())\n```\n\nI don't have time to do it right now. I'll do it soon if you don't beat me.",
    "created_at": "2011-04-04T17:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71338",
    "user": "hivert"
}
```

> hivert: do you want to review this ticket?

Sure ! I completely forgot about this one. Sorry !

They are a few place where we should remove the bad implementation using `__repr__` since they all inherits from `CategoryObject`: 

```
popcorn-*ge-combinat/sage $ grep "hash(self.__repr__())" **/*.py*
groups/group.pyx:        return hash(self.__repr__())
modules/module.pyx:        return hash(self.__repr__())
modules/module.pyx:        return hash(self.__repr__())
rings/polynomial/multi_polynomial_libsingular.pyx:        return hash(self.__repr__())
rings/ring.pyx:        return hash(self.__repr__())
structure/sage_object.pyx:        return hash(self.__repr__())
```

I don't have time to do it right now. I'll do it soon if you don't beat me.



---

archive/issue_comments_071339.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-04T18:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71339",
    "user": "hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071340.json:
```json
{
    "body": "> They are a few place where we should remove the bad implementation using\n> `__repr__` since they all inherits from `CategoryObject`:\n\nI just added a review patch which removes the wrong hash methods.\n\nPlease review. I'm ok with the original patch, so if my review patch is ok\nyou can put a positive review on my behalf.",
    "created_at": "2011-04-04T18:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71340",
    "user": "hivert"
}
```

> They are a few place where we should remove the bad implementation using
> `__repr__` since they all inherits from `CategoryObject`:

I just added a review patch which removes the wrong hash methods.

Please review. I'm ok with the original patch, so if my review patch is ok
you can put a positive review on my behalf.



---

archive/issue_comments_071341.json:
```json
{
    "body": "Attachment\n\nFlorent's review patch looks good. However ``consistant* should be written ``consistent* in the first patch. I also did not yet set a positive review because of the ongoing discussion on sage-devel. Please feel free to go ahead and set a positive review once the typo is fixed and if it is decided that the PolynomialRing issue shall be fixed in a follow up patch.\n\nCheers,\n                                   Nicolas",
    "created_at": "2011-04-21T01:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71341",
    "user": "nthiery"
}
```

Attachment

Florent's review patch looks good. However ``consistant* should be written ``consistent* in the first patch. I also did not yet set a positive review because of the ongoing discussion on sage-devel. Please feel free to go ahead and set a positive review once the typo is fixed and if it is decided that the PolynomialRing issue shall be fixed in a follow up patch.

Cheers,
                                   Nicolas



---

archive/issue_comments_071342.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-21T01:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71342",
    "user": "nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071343.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-04-21T09:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71343",
    "user": "robertwb"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_071344.json:
```json
{
    "body": "Attachment\n\nFixed the typo, I don't think the issue with sparse PolynomialRing #11231 should hold this ticket up any longer (it's had a patch sitting on it for over a year...)",
    "created_at": "2011-04-21T09:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71344",
    "user": "robertwb"
}
```

Attachment

Fixed the typo, I don't think the issue with sparse PolynomialRing #11231 should hold this ticket up any longer (it's had a patch sitting on it for over a year...)



---

archive/issue_comments_071345.json:
```json
{
    "body": "I'm assuming the \"apply\" should be changed...",
    "created_at": "2011-04-21T19:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71345",
    "user": "jdemeyer"
}
```

I'm assuming the "apply" should be changed...



---

archive/issue_comments_071346.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-04-22T19:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71346",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071347.json:
```json
{
    "body": "Please change the commit message of [attachment:8119-parent-hash.2.patch] (use hg qrefresh -e for that).",
    "created_at": "2011-04-22T19:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71347",
    "user": "jdemeyer"
}
```

Please change the commit message of [attachment:8119-parent-hash.2.patch] (use hg qrefresh -e for that).



---

archive/issue_comments_071348.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-23T10:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71348",
    "user": "hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071349.json:
```json
{
    "body": "Attachment\n\nI just re-uploaded roberts patch with a correct log message. I'm not sure I'm allowed to put a positive review though. \n\nFlorent",
    "created_at": "2011-04-23T10:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71349",
    "user": "hivert"
}
```

Attachment

I just re-uploaded roberts patch with a correct log message. I'm not sure I'm allowed to put a positive review though. 

Florent



---

archive/issue_comments_071350.json:
```json
{
    "body": "Bonjour Florent!\n\nI am not sure the log message for 8119-parent-hash-review.patch is proper. While you are at it, I'd suggest to just fold it in the other patch. The review history does not bring much information here, so having a single patch will give a better overview to the future reader.\n\nI'll set a positive review right after.",
    "created_at": "2011-04-23T13:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71350",
    "user": "nthiery"
}
```

Bonjour Florent!

I am not sure the log message for 8119-parent-hash-review.patch is proper. While you are at it, I'd suggest to just fold it in the other patch. The review history does not bring much information here, so having a single patch will give a better overview to the future reader.

I'll set a positive review right after.



---

archive/issue_comments_071351.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-23T13:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71351",
    "user": "nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071352.json:
```json
{
    "body": "> I'd suggest to just fold it in the other patch.\n\nDone.",
    "created_at": "2011-04-23T13:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71352",
    "user": "hivert"
}
```

> I'd suggest to just fold it in the other patch.

Done.



---

archive/issue_comments_071353.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-23T13:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71353",
    "user": "hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071354.json:
```json
{
    "body": "Thanks!\n\nIt seems the buildbot is getting confused about which patch to apply though.",
    "created_at": "2011-04-23T15:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71354",
    "user": "nthiery"
}
```

Thanks!

It seems the buildbot is getting confused about which patch to apply though.



---

archive/issue_comments_071355.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-23T15:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71355",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071356.json:
```json
{
    "body": "Apply 8119-parent-hash-final.patch\n\nGranted, the patchbot doesn't bother testing positively reviewed tickets (not that anything it's concerned with changed). Thanks for getting to this for me.",
    "created_at": "2011-04-24T05:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71356",
    "user": "robertwb"
}
```

Apply 8119-parent-hash-final.patch

Granted, the patchbot doesn't bother testing positively reviewed tickets (not that anything it's concerned with changed). Thanks for getting to this for me.



---

archive/issue_comments_071357.json:
```json
{
    "body": "Some of these doctests should be differentiated on 32-bit systems (in particular, all the results of `hash()`).",
    "created_at": "2011-05-03T08:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71357",
    "user": "jdemeyer"
}
```

Some of these doctests should be differentiated on 32-bit systems (in particular, all the results of `hash()`).



---

archive/issue_comments_071358.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-05-03T08:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71358",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071359.json:
```json
{
    "body": "*bump*",
    "created_at": "2011-05-19T08:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71359",
    "user": "jdemeyer"
}
```

*bump*



---

archive/issue_comments_071360.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-29T14:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71360",
    "user": "nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071361.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-29T14:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71361",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071362.json:
```json
{
    "body": "On boxen (Linux x86_64), I get:\n\n```\nsage -t  -force_lib devel/sage/sage/structure/category_object.pyx\n**********************************************************************\nFile \"/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx\", line 757:\n    sage: hash(bla)\nExpected:\n    -1525918542791298668\nGot:\n    -5279516879544852222\n**********************************************************************\nFile \"/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx\", line 761:\n    sage: hash(bla)\nExpected:\n    -1525918542791298668\nGot:\n    -5279516879544852222\n**********************************************************************\n```\n",
    "created_at": "2012-04-06T06:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71362",
    "user": "jdemeyer"
}
```

On boxen (Linux x86_64), I get:

```
sage -t  -force_lib devel/sage/sage/structure/category_object.pyx
**********************************************************************
File "/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx", line 757:
    sage: hash(bla)
Expected:
    -1525918542791298668
Got:
    -5279516879544852222
**********************************************************************
File "/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx", line 761:
    sage: hash(bla)
Expected:
    -1525918542791298668
Got:
    -5279516879544852222
**********************************************************************
```




---

archive/issue_comments_071363.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-04-06T06:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71363",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071364.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:23 jdemeyer]:\n> On boxen (Linux x86_64), I get:\n> {{{\n> sage -t  -force_lib devel/sage/sage/structure/category_object.pyx\n> **********************************************************************\n> File \"/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx\", line 757:\n>     sage: hash(bla)\n> Expected:\n>     -1525918542791298668\n> Got:\n>     -5279516879544852222\n> **********************************************************************\n> File \"/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx\", line 761:\n>     sage: hash(bla)\n> Expected:\n>     -1525918542791298668\n> Got:\n>     -5279516879544852222\n> **********************************************************************\n> }}}\n\nWeird, I get here the same result as you on boxen, both with 4.8 and 5.0.beta8. I don't know how a wrong return value ended up in the patch. \n\nOh well, I updated the patch to expect the result obtained on boxen.",
    "created_at": "2012-04-06T14:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71364",
    "user": "nthiery"
}
```

Attachment

Replying to [comment:23 jdemeyer]:
> On boxen (Linux x86_64), I get:
> {{{
> sage -t  -force_lib devel/sage/sage/structure/category_object.pyx
> **********************************************************************
> File "/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx", line 757:
>     sage: hash(bla)
> Expected:
>     -1525918542791298668
> Got:
>     -5279516879544852222
> **********************************************************************
> File "/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx", line 761:
>     sage: hash(bla)
> Expected:
>     -1525918542791298668
> Got:
>     -5279516879544852222
> **********************************************************************
> }}}

Weird, I get here the same result as you on boxen, both with 4.8 and 5.0.beta8. I don't know how a wrong return value ended up in the patch. 

Oh well, I updated the patch to expect the result obtained on boxen.



---

archive/issue_comments_071365.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-06T14:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71365",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071366.json:
```json
{
    "body": "Apply 8119-parent-hash-final-fix32.patch\n\n(for patchbot)",
    "created_at": "2012-04-07T12:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71366",
    "user": "davidloeffler"
}
```

Apply 8119-parent-hash-final-fix32.patch

(for patchbot)



---

archive/issue_comments_071367.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-04-26T22:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71367",
    "user": "hivert"
}
```

Attachment



---

archive/issue_comments_071368.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-04-26T22:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71368",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071369.json:
```json
{
    "body": "Hi there,\n\nI'm setting a positive review here but I uploaded a new patch removing a\ntrailling whitespace which bothered the patchbot. The only difference between\n[attachment:8119-parent-hash-final-fix32.patch] and\n[attachment:8119-parent-hash-final.patch] is the trailling space (and of course\nMercurials header), so I don't think a new review is needed.\n\nFlorent",
    "created_at": "2012-04-26T22:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71369",
    "user": "hivert"
}
```

Hi there,

I'm setting a positive review here but I uploaded a new patch removing a
trailling whitespace which bothered the patchbot. The only difference between
[attachment:8119-parent-hash-final-fix32.patch] and
[attachment:8119-parent-hash-final.patch] is the trailling space (and of course
Mercurials header), so I don't think a new review is needed.

Florent



---

archive/issue_comments_071370.json:
```json
{
    "body": "Thanks for the final review!",
    "created_at": "2012-04-27T17:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71370",
    "user": "nthiery"
}
```

Thanks for the final review!



---

archive/issue_comments_071371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-04-30T09:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71371",
    "user": "jdemeyer"
}
```

Resolution: fixed
