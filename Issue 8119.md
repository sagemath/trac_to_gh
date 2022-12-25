# Issue 8119: Rename change the hash value of some objects

archive/issues_008119.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jasongrout simonking\n\nFor many objects the hash value is computed from `__repr__`. This is a bad idea since renaming the object change its hash value.\n\n```\nsage: bla = PolynomialRing(ZZ,\"x\")\nsage: hash(bla)\n-1525918542791298668\nsage: bla.rename(\"toto\")\nsage: hash(bla)\n2314052222105390764\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8119\n\n",
    "created_at": "2010-01-29T15:22:48Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Rename change the hash value of some objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8119",
    "user": "https://github.com/hivert"
}
```
Assignee: tbd

CC:  @jasongrout simonking

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

archive/issue_comments_071209.json:
```json
{
    "body": "For immutable objects, like Parents, the default __hash__ could store the value used the first time it is computed. This doesn't solve the problem of \n\n\n```\nsage: bla = PolynomialRing(ZZ,\"x\")\nsage: hash(bla['t'])\n-1733828288\nsage: bla.rename(\"toto\")\nsage: hash(bla['t'])\n-1924319844\n```\n",
    "created_at": "2010-03-12T09:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71209",
    "user": "https://github.com/robertwb"
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

archive/issue_comments_071210.json:
```json
{
    "body": "Attachment [8119-parent-hash.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash.patch) by @robertwb created at 2010-03-12 09:57:30",
    "created_at": "2010-03-12T09:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71210",
    "user": "https://github.com/robertwb"
}
```

Attachment [8119-parent-hash.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash.patch) by @robertwb created at 2010-03-12 09:57:30



---

archive/issue_comments_071211.json:
```json
{
    "body": "This is a partial fix (that won't work for SageObject in general, unless we enforce that mutable objects maintain their own hash, and I don't think we want to put an extra field on all Elements), but resolves the most important case. It's also a performance gain.",
    "created_at": "2010-03-12T09:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71211",
    "user": "https://github.com/robertwb"
}
```

This is a partial fix (that won't work for SageObject in general, unless we enforce that mutable objects maintain their own hash, and I don't think we want to put an extra field on all Elements), but resolves the most important case. It's also a performance gain.



---

archive/issue_comments_071212.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-12T09:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71212",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071213.json:
```json
{
    "body": "Hi Robert,\n\nI've one question related to this and I like to have the confirmation from an expert. After your patch, upon pickling/unpickling the hash value can change because it is not pickled and neither is the name, right ? As far as I manage to test this is not harmful to pickle a dict containing a renamed parent. Indeed, trying to read `cPickle.c`, I understood that the dict is reconstructed from it's items and thus even if the hash changed the element is inserted correctly in the dict during unpickling. Can you confirm this ?\n\nIf this is not both this patch and #8120 are broken.\n\nAlso, after this, do you still need #8506 ?\n\nFlorent",
    "created_at": "2010-03-12T22:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71213",
    "user": "https://github.com/hivert"
}
```

Hi Robert,

I've one question related to this and I like to have the confirmation from an expert. After your patch, upon pickling/unpickling the hash value can change because it is not pickled and neither is the name, right ? As far as I manage to test this is not harmful to pickle a dict containing a renamed parent. Indeed, trying to read `cPickle.c`, I understood that the dict is reconstructed from it's items and thus even if the hash changed the element is inserted correctly in the dict during unpickling. Can you confirm this ?

If this is not both this patch and #8120 are broken.

Also, after this, do you still need #8506 ?

Florent



---

archive/issue_comments_071214.json:
```json
{
    "body": "Replying to [comment:3 hivert]:\n> Hi Robert,\n> \n> I've one question related to this and I like to have the confirmation from an expert. After your patch, upon pickling/unpickling the hash value can change because it is not pickled and neither is the name, right ? As far as I manage to test this is not harmful to pickle a dict containing a renamed parent. Indeed, trying to read `cPickle.c`, I understood that the dict is reconstructed from it's items and thus even if the hash changed the element is inserted correctly in the dict during unpickling. Can you confirm this ?\n\nThat is correct. Hashes in general are not guaranteed to be consistent from run to run, all that really matters is that they satisfy (to the best they can) the equality constraints. \n\n> If this is not both this patch and #8120 are broken.\n> \n> Also, after this, do you still need #8506 ?\n\nYes, #8506 is still important--in my case I'm reducing a curve mod many, many primes, doing just a bit of stuff on each before throwing them away. I suppose eventually caching the hash value would eventually be a win, but that's a separate optimization.",
    "created_at": "2010-03-13T09:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71214",
    "user": "https://github.com/robertwb"
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

archive/issue_comments_071215.json:
```json
{
    "body": "hivert: do you want to review this ticket?",
    "created_at": "2010-10-02T19:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71215",
    "user": "https://github.com/jasongrout"
}
```

hivert: do you want to review this ticket?



---

archive/issue_comments_071216.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-04T17:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71216",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071217.json:
```json
{
    "body": "> hivert: do you want to review this ticket?\n\nSure ! I completely forgot about this one. Sorry !\n\nThey are a few place where we should remove the bad implementation using `__repr__` since they all inherits from `CategoryObject`: \n\n```\npopcorn-*ge-combinat/sage $ grep \"hash(self.__repr__())\" **/*.py*\ngroups/group.pyx:        return hash(self.__repr__())\nmodules/module.pyx:        return hash(self.__repr__())\nmodules/module.pyx:        return hash(self.__repr__())\nrings/polynomial/multi_polynomial_libsingular.pyx:        return hash(self.__repr__())\nrings/ring.pyx:        return hash(self.__repr__())\nstructure/sage_object.pyx:        return hash(self.__repr__())\n```\n\nI don't have time to do it right now. I'll do it soon if you don't beat me.",
    "created_at": "2011-04-04T17:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71217",
    "user": "https://github.com/hivert"
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

archive/issue_comments_071218.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-04T18:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71218",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071219.json:
```json
{
    "body": "> They are a few place where we should remove the bad implementation using\n> `__repr__` since they all inherits from `CategoryObject`:\n\nI just added a review patch which removes the wrong hash methods.\n\nPlease review. I'm ok with the original patch, so if my review patch is ok\nyou can put a positive review on my behalf.",
    "created_at": "2011-04-04T18:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71219",
    "user": "https://github.com/hivert"
}
```

> They are a few place where we should remove the bad implementation using
> `__repr__` since they all inherits from `CategoryObject`:

I just added a review patch which removes the wrong hash methods.

Please review. I'm ok with the original patch, so if my review patch is ok
you can put a positive review on my behalf.



---

archive/issue_comments_071220.json:
```json
{
    "body": "Attachment [8119-parent-hash-review.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash-review.patch) by @nthiery created at 2011-04-21 01:45:08\n\nFlorent's review patch looks good. However ``consistant* should be written ``consistent* in the first patch. I also did not yet set a positive review because of the ongoing discussion on sage-devel. Please feel free to go ahead and set a positive review once the typo is fixed and if it is decided that the PolynomialRing issue shall be fixed in a follow up patch.\n\nCheers,\n                                   Nicolas",
    "created_at": "2011-04-21T01:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71220",
    "user": "https://github.com/nthiery"
}
```

Attachment [8119-parent-hash-review.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash-review.patch) by @nthiery created at 2011-04-21 01:45:08

Florent's review patch looks good. However ``consistant* should be written ``consistent* in the first patch. I also did not yet set a positive review because of the ongoing discussion on sage-devel. Please feel free to go ahead and set a positive review once the typo is fixed and if it is decided that the PolynomialRing issue shall be fixed in a follow up patch.

Cheers,
                                   Nicolas



---

archive/issue_comments_071221.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-21T01:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71221",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071222.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-04-21T09:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71222",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_071223.json:
```json
{
    "body": "Attachment [8119-parent-hash.2.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash.2.patch) by @robertwb created at 2011-04-21 09:27:06\n\nFixed the typo, I don't think the issue with sparse PolynomialRing #11231 should hold this ticket up any longer (it's had a patch sitting on it for over a year...)",
    "created_at": "2011-04-21T09:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71223",
    "user": "https://github.com/robertwb"
}
```

Attachment [8119-parent-hash.2.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash.2.patch) by @robertwb created at 2011-04-21 09:27:06

Fixed the typo, I don't think the issue with sparse PolynomialRing #11231 should hold this ticket up any longer (it's had a patch sitting on it for over a year...)



---

archive/issue_comments_071224.json:
```json
{
    "body": "I'm assuming the \"apply\" should be changed...",
    "created_at": "2011-04-21T19:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71224",
    "user": "https://github.com/jdemeyer"
}
```

I'm assuming the "apply" should be changed...



---

archive/issue_comments_071225.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-04-22T19:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71225",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071226.json:
```json
{
    "body": "Please change the commit message of [attachment:8119-parent-hash.2.patch] (use hg qrefresh -e for that).",
    "created_at": "2011-04-22T19:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71226",
    "user": "https://github.com/jdemeyer"
}
```

Please change the commit message of [attachment:8119-parent-hash.2.patch] (use hg qrefresh -e for that).



---

archive/issue_comments_071227.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-23T10:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71227",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071228.json:
```json
{
    "body": "Attachment [8119-parent-hash.3.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash.3.patch) by @hivert created at 2011-04-23 10:47:52\n\nI just re-uploaded roberts patch with a correct log message. I'm not sure I'm allowed to put a positive review though. \n\nFlorent",
    "created_at": "2011-04-23T10:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71228",
    "user": "https://github.com/hivert"
}
```

Attachment [8119-parent-hash.3.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash.3.patch) by @hivert created at 2011-04-23 10:47:52

I just re-uploaded roberts patch with a correct log message. I'm not sure I'm allowed to put a positive review though. 

Florent



---

archive/issue_comments_071229.json:
```json
{
    "body": "Bonjour Florent!\n\nI am not sure the log message for 8119-parent-hash-review.patch is proper. While you are at it, I'd suggest to just fold it in the other patch. The review history does not bring much information here, so having a single patch will give a better overview to the future reader.\n\nI'll set a positive review right after.",
    "created_at": "2011-04-23T13:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71229",
    "user": "https://github.com/nthiery"
}
```

Bonjour Florent!

I am not sure the log message for 8119-parent-hash-review.patch is proper. While you are at it, I'd suggest to just fold it in the other patch. The review history does not bring much information here, so having a single patch will give a better overview to the future reader.

I'll set a positive review right after.



---

archive/issue_comments_071230.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-23T13:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71230",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071231.json:
```json
{
    "body": "> I'd suggest to just fold it in the other patch.\n\nDone.",
    "created_at": "2011-04-23T13:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71231",
    "user": "https://github.com/hivert"
}
```

> I'd suggest to just fold it in the other patch.

Done.



---

archive/issue_comments_071232.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-23T13:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71232",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071233.json:
```json
{
    "body": "Thanks!\n\nIt seems the buildbot is getting confused about which patch to apply though.",
    "created_at": "2011-04-23T15:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71233",
    "user": "https://github.com/nthiery"
}
```

Thanks!

It seems the buildbot is getting confused about which patch to apply though.



---

archive/issue_comments_071234.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-23T15:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71234",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071235.json:
```json
{
    "body": "Apply 8119-parent-hash-final.patch\n\nGranted, the patchbot doesn't bother testing positively reviewed tickets (not that anything it's concerned with changed). Thanks for getting to this for me.",
    "created_at": "2011-04-24T05:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71235",
    "user": "https://github.com/robertwb"
}
```

Apply 8119-parent-hash-final.patch

Granted, the patchbot doesn't bother testing positively reviewed tickets (not that anything it's concerned with changed). Thanks for getting to this for me.



---

archive/issue_comments_071236.json:
```json
{
    "body": "Some of these doctests should be differentiated on 32-bit systems (in particular, all the results of `hash()`).",
    "created_at": "2011-05-03T08:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71236",
    "user": "https://github.com/jdemeyer"
}
```

Some of these doctests should be differentiated on 32-bit systems (in particular, all the results of `hash()`).



---

archive/issue_comments_071237.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-05-03T08:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71237",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071238.json:
```json
{
    "body": "*bump*",
    "created_at": "2011-05-19T08:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71238",
    "user": "https://github.com/jdemeyer"
}
```

*bump*



---

archive/issue_comments_071239.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-29T14:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71239",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071240.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-29T14:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71240",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071241.json:
```json
{
    "body": "On boxen (Linux x86_64), I get:\n\n```\nsage -t  -force_lib devel/sage/sage/structure/category_object.pyx\n**********************************************************************\nFile \"/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx\", line 757:\n    sage: hash(bla)\nExpected:\n    -1525918542791298668\nGot:\n    -5279516879544852222\n**********************************************************************\nFile \"/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx\", line 761:\n    sage: hash(bla)\nExpected:\n    -1525918542791298668\nGot:\n    -5279516879544852222\n**********************************************************************\n```\n",
    "created_at": "2012-04-06T06:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71241",
    "user": "https://github.com/jdemeyer"
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

archive/issue_comments_071242.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-04-06T06:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71242",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071243.json:
```json
{
    "body": "Attachment [8119-parent-hash-final-fix32.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash-final-fix32.patch) by @nthiery created at 2012-04-06 14:45:27\n\nReplying to [comment:23 jdemeyer]:\n> On boxen (Linux x86_64), I get:\n> {{{\n> sage -t  -force_lib devel/sage/sage/structure/category_object.pyx\n> **********************************************************************\n> File \"/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx\", line 757:\n>     sage: hash(bla)\n> Expected:\n>     -1525918542791298668\n> Got:\n>     -5279516879544852222\n> **********************************************************************\n> File \"/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx\", line 761:\n>     sage: hash(bla)\n> Expected:\n>     -1525918542791298668\n> Got:\n>     -5279516879544852222\n> **********************************************************************\n> }}}\n\nWeird, I get here the same result as you on boxen, both with 4.8 and 5.0.beta8. I don't know how a wrong return value ended up in the patch. \n\nOh well, I updated the patch to expect the result obtained on boxen.",
    "created_at": "2012-04-06T14:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71243",
    "user": "https://github.com/nthiery"
}
```

Attachment [8119-parent-hash-final-fix32.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash-final-fix32.patch) by @nthiery created at 2012-04-06 14:45:27

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

archive/issue_comments_071244.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-06T14:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71244",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071245.json:
```json
{
    "body": "Apply 8119-parent-hash-final-fix32.patch\n\n(for patchbot)",
    "created_at": "2012-04-07T12:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71245",
    "user": "https://github.com/loefflerd"
}
```

Apply 8119-parent-hash-final-fix32.patch

(for patchbot)



---

archive/issue_comments_071246.json:
```json
{
    "body": "Attachment [8119-parent-hash-final.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash-final.patch) by @hivert created at 2012-04-26 22:17:25",
    "created_at": "2012-04-26T22:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71246",
    "user": "https://github.com/hivert"
}
```

Attachment [8119-parent-hash-final.patch](tarball://root/attachments/some-uuid/ticket8119/8119-parent-hash-final.patch) by @hivert created at 2012-04-26 22:17:25



---

archive/issue_comments_071247.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-04-26T22:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71247",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071248.json:
```json
{
    "body": "Hi there,\n\nI'm setting a positive review here but I uploaded a new patch removing a\ntrailling whitespace which bothered the patchbot. The only difference between\n[attachment:8119-parent-hash-final-fix32.patch] and\n[attachment:8119-parent-hash-final.patch] is the trailling space (and of course\nMercurials header), so I don't think a new review is needed.\n\nFlorent",
    "created_at": "2012-04-26T22:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71248",
    "user": "https://github.com/hivert"
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

archive/issue_comments_071249.json:
```json
{
    "body": "Thanks for the final review!",
    "created_at": "2012-04-27T17:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71249",
    "user": "https://github.com/nthiery"
}
```

Thanks for the final review!



---

archive/issue_comments_071250.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-04-30T09:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8119#issuecomment-71250",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
