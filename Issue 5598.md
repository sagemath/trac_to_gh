# Issue 5598: allow post-creation (pre-use) declaration of coercions

archive/issues_005598.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  @nthiery\n\nOne can now do \n\na = A()\nmor = [morphism from X to A]\na.register_coercion(mor)\n\nThis works as long as coercion has not yet been used (otherwise information cached (both here and elsewhere) becomes invalid).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5598\n\n",
    "created_at": "2009-03-24T05:12:18Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "allow post-creation (pre-use) declaration of coercions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5598",
    "user": "@robertwb"
}
```
Assignee: @robertwb

CC:  @nthiery

One can now do 

a = A()
mor = [morphism from X to A]
a.register_coercion(mor)

This works as long as coercion has not yet been used (otherwise information cached (both here and elsewhere) becomes invalid).

Issue created by migration from https://trac.sagemath.org/ticket/5598





---

archive/issue_comments_043625.json:
```json
{
    "body": "Attachment [5598-coerce-declare.patch](tarball://root/attachments/some-uuid/ticket5598/5598-coerce-declare.patch) by @robertwb created at 2009-03-24 05:20:25\n\nDepends on #5597.",
    "created_at": "2009-03-24T05:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43625",
    "user": "@robertwb"
}
```

Attachment [5598-coerce-declare.patch](tarball://root/attachments/some-uuid/ticket5598/5598-coerce-declare.patch) by @robertwb created at 2009-03-24 05:20:25

Depends on #5597.



---

archive/issue_comments_043626.json:
```json
{
    "body": "One can now do \n\n\n```\nsage: A = SomeParent()\nsage: mor = [morphism from X to A]\nsage: A.register_coercion(mor)\n```\n\n\nThis works as long as coercion has not yet been used (otherwise information cached (both here and elsewhere) becomes invalid).",
    "created_at": "2009-03-24T05:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43626",
    "user": "@robertwb"
}
```

One can now do 


```
sage: A = SomeParent()
sage: mor = [morphism from X to A]
sage: A.register_coercion(mor)
```


This works as long as coercion has not yet been used (otherwise information cached (both here and elsewhere) becomes invalid).



---

archive/issue_comments_043627.json:
```json
{
    "body": "Actually, though I wrote it on top of #5597, there's probably not a dependance. Note that I don't have any doctests yet (as it's completely unused functionality at this point).",
    "created_at": "2009-03-24T10:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43627",
    "user": "@robertwb"
}
```

Actually, though I wrote it on top of #5597, there's probably not a dependance. Note that I don't have any doctests yet (as it's completely unused functionality at this point).



---

archive/issue_comments_043628.json:
```json
{
    "body": "> Note that I don't have any doctests yet (as it's completely unused \n> functionality at this point). \n\nHence I'm physically incapable of giving this a positive review.  Sorry.",
    "created_at": "2009-04-12T05:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43628",
    "user": "@williamstein"
}
```

> Note that I don't have any doctests yet (as it's completely unused 
> functionality at this point). 

Hence I'm physically incapable of giving this a positive review.  Sorry.



---

archive/issue_comments_043629.json:
```json
{
    "body": "Attachment [test-coercion.py](tarball://root/attachments/some-uuid/ticket5598/test-coercion.py) by @nthiery created at 2009-04-14 00:35:13\n\nI have been using this patch (or actually a plain python version of it; see the sage-combinat patch queue) relatively intensively, and it does its job well. However it's hard to extract any interesting unitary test from those uses, since they all rely on the rest of the category stuff.\n\nI have just attached a stupid test instead ... It just plays with register_coercion, but should be easy to adapt to the others.\n\nBtw: robert: would it be possible to have register_coercion just raise a warning if coercions have readily been used? There are cases where it can be handy to abuse the system a bit from the interpreter.",
    "created_at": "2009-04-14T00:35:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43629",
    "user": "@nthiery"
}
```

Attachment [test-coercion.py](tarball://root/attachments/some-uuid/ticket5598/test-coercion.py) by @nthiery created at 2009-04-14 00:35:13

I have been using this patch (or actually a plain python version of it; see the sage-combinat patch queue) relatively intensively, and it does its job well. However it's hard to extract any interesting unitary test from those uses, since they all rely on the rest of the category stuff.

I have just attached a stupid test instead ... It just plays with register_coercion, but should be easy to adapt to the others.

Btw: robert: would it be possible to have register_coercion just raise a warning if coercions have readily been used? There are cases where it can be handy to abuse the system a bit from the interpreter.



---

archive/issue_comments_043630.json:
```json
{
    "body": "Thanks for the tests. In retrospect, sometimes very simple tests like this are best at showing exactly what's going on. \n\nAs for warnings vs. errors, yes it's possible, but I am strongly against it. If you need to abuse it, you can do so from Cython (or even write a spyx file that allows you to do so from the interpreter). \n\nThere was talk about asserting coercions within contexts, but no one's gotten around to implementing them yet.",
    "created_at": "2009-04-14T11:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43630",
    "user": "@robertwb"
}
```

Thanks for the tests. In retrospect, sometimes very simple tests like this are best at showing exactly what's going on. 

As for warnings vs. errors, yes it's possible, but I am strongly against it. If you need to abuse it, you can do so from Cython (or even write a spyx file that allows you to do so from the interpreter). 

There was talk about asserting coercions within contexts, but no one's gotten around to implementing them yet.



---

archive/issue_comments_043631.json:
```json
{
    "body": "Hi Robert,\n\n> Thanks for the tests. In retrospect, sometimes very simple tests like this are best at showing exactly what's going on. \n\nYep.\n\nThe construction of the parents and morphisms in this test are still ugly, though. Both ought to be essentially one-liners. Hopefuly things will be nicer when the category patch will be in.\n\n> As for warnings vs. errors, yes it's possible, but I am strongly against it. If you need to abuse it, you can > do so from Cython (or even write a spyx file that allows you to do so from the interpreter). \n\nMy typical (ab)use case is someone constructing a couple parents in the interpreter, playing with them, and suddenly thinking \"oh, but wouldn't all be natural if I added a coercion there?\". The user will give it a try if this is trivial to do. Otherwise he won't and that's too bad.\n\nBtw: your patch changes the datastructure of parents to add the cython attribute `_coercions_used`. How does this work with unpickling old pickles? That is, will _coercions_used be set to an appropriate value?\n\n> \n> There was talk about asserting coercions within contexts, but no one's gotten around to implementing them yet.",
    "created_at": "2009-04-14T16:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43631",
    "user": "@nthiery"
}
```

Hi Robert,

> Thanks for the tests. In retrospect, sometimes very simple tests like this are best at showing exactly what's going on. 

Yep.

The construction of the parents and morphisms in this test are still ugly, though. Both ought to be essentially one-liners. Hopefuly things will be nicer when the category patch will be in.

> As for warnings vs. errors, yes it's possible, but I am strongly against it. If you need to abuse it, you can > do so from Cython (or even write a spyx file that allows you to do so from the interpreter). 

My typical (ab)use case is someone constructing a couple parents in the interpreter, playing with them, and suddenly thinking "oh, but wouldn't all be natural if I added a coercion there?". The user will give it a try if this is trivial to do. Otherwise he won't and that's too bad.

Btw: your patch changes the datastructure of parents to add the cython attribute `_coercions_used`. How does this work with unpickling old pickles? That is, will _coercions_used be set to an appropriate value?

> 
> There was talk about asserting coercions within contexts, but no one's gotten around to implementing them yet.



---

archive/issue_comments_043632.json:
```json
{
    "body": "This is all kinds of awesome, and yet totally useless.  For example, the following fails:\n\n\n```\nx = GF(3)['x'].0\nK.<a> = GF(3^2, 'a', modulus=x^2+1)\nL.<b> = GF(3^2, 'b', modulus=x^2 + x - 1)\n\nL_into_K = L.hom([a - 2], K, check=False)\nK.register_coercion(L_into_K)\n```\n\n\nWhy?  Because the `a-2` has used the coercion mechanism for K.  It will be essentially impossible to construct morphisms that are mathematically interesting without using coercion at some point.\n\nWhat is to be done?  I have no great ideas.  Personally I would be happy with a flag to `register_coercion` that \"broke the links\" of the coercion graph, or even tried to `reset_cache()` on the coercion_model.  Notice that I tried this, but it doesn't work, because `reset_cache` doesn't twiddle the flag on each parent.  (That's a bug, in my opinion.)",
    "created_at": "2009-05-06T03:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43632",
    "user": "@ncalexan"
}
```

This is all kinds of awesome, and yet totally useless.  For example, the following fails:


```
x = GF(3)['x'].0
K.<a> = GF(3^2, 'a', modulus=x^2+1)
L.<b> = GF(3^2, 'b', modulus=x^2 + x - 1)

L_into_K = L.hom([a - 2], K, check=False)
K.register_coercion(L_into_K)
```


Why?  Because the `a-2` has used the coercion mechanism for K.  It will be essentially impossible to construct morphisms that are mathematically interesting without using coercion at some point.

What is to be done?  I have no great ideas.  Personally I would be happy with a flag to `register_coercion` that "broke the links" of the coercion graph, or even tried to `reset_cache()` on the coercion_model.  Notice that I tried this, but it doesn't work, because `reset_cache` doesn't twiddle the flag on each parent.  (That's a bug, in my opinion.)



---

archive/issue_comments_043633.json:
```json
{
    "body": "Apply both `5598-` patches.  My fixes make actions work (they're still broken pretty hard in parent_old, but they work here) and test this code in a non-combinat tree.  In order to make this work I include an ugly hack.\n\nrobertwb, this badly needs documentation; it really can't be accepted without *something*.",
    "created_at": "2009-05-06T06:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43633",
    "user": "@ncalexan"
}
```

Apply both `5598-` patches.  My fixes make actions work (they're still broken pretty hard in parent_old, but they work here) and test this code in a non-combinat tree.  In order to make this work I include an ugly hack.

robertwb, this badly needs documentation; it really can't be accepted without *something*.



---

archive/issue_comments_043634.json:
```json
{
    "body": "Yes, I just haven't had time to work on any coercion-related stuff for a while. I'll be attacking issues like this during Sage days.",
    "created_at": "2009-05-06T06:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43634",
    "user": "@robertwb"
}
```

Yes, I just haven't had time to work on any coercion-related stuff for a while. I'll be attacking issues like this during Sage days.



---

archive/issue_comments_043635.json:
```json
{
    "body": "Attachment [5598-ncalexan-fixes-and-tests.patch](tarball://root/attachments/some-uuid/ticket5598/5598-ncalexan-fixes-and-tests.patch) by @ncalexan created at 2009-05-08 23:04:25",
    "created_at": "2009-05-08T23:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43635",
    "user": "@ncalexan"
}
```

Attachment [5598-ncalexan-fixes-and-tests.patch](tarball://root/attachments/some-uuid/ticket5598/5598-ncalexan-fixes-and-tests.patch) by @ncalexan created at 2009-05-08 23:04:25



---

archive/issue_comments_043636.json:
```json
{
    "body": "Updated `fixes` patch includes a few line of documentation.  robertwb, this is ready for you to review.",
    "created_at": "2009-05-08T23:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43636",
    "user": "@ncalexan"
}
```

Updated `fixes` patch includes a few line of documentation.  robertwb, this is ready for you to review.



---

archive/issue_comments_043637.json:
```json
{
    "body": "5598-ncalexan-fixes-and-tests.patch seems malformed, could you try recreating this patch?",
    "created_at": "2009-05-14T23:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43637",
    "user": "@robertwb"
}
```

5598-ncalexan-fixes-and-tests.patch seems malformed, could you try recreating this patch?



---

archive/issue_comments_043638.json:
```json
{
    "body": "Attachment [5598-ncalexan-fixes-and-tests.2.patch](tarball://root/attachments/some-uuid/ticket5598/5598-ncalexan-fixes-and-tests.2.patch) by @ncalexan created at 2009-05-17 21:14:08",
    "created_at": "2009-05-17T21:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43638",
    "user": "@ncalexan"
}
```

Attachment [5598-ncalexan-fixes-and-tests.2.patch](tarball://root/attachments/some-uuid/ticket5598/5598-ncalexan-fixes-and-tests.2.patch) by @ncalexan created at 2009-05-17 21:14:08



---

archive/issue_comments_043639.json:
```json
{
    "body": "Attachment [5598-ncalexan-fixes-and-tests.3.patch](tarball://root/attachments/some-uuid/ticket5598/5598-ncalexan-fixes-and-tests.3.patch) by @ncalexan created at 2009-05-17 21:21:52\n\nAh, the mystery of the malformed patches.  hg export -o *DOESN'T* overwrite an existing file, it appends!  I think this is totally wrong, but I can work around it.  This has been biting me for weeks, I now realize.  Anyway, only tests.3.patch should be applied.",
    "created_at": "2009-05-17T21:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43639",
    "user": "@ncalexan"
}
```

Attachment [5598-ncalexan-fixes-and-tests.3.patch](tarball://root/attachments/some-uuid/ticket5598/5598-ncalexan-fixes-and-tests.3.patch) by @ncalexan created at 2009-05-17 21:21:52

Ah, the mystery of the malformed patches.  hg export -o *DOESN'T* overwrite an existing file, it appends!  I think this is totally wrong, but I can work around it.  This has been biting me for weeks, I now realize.  Anyway, only tests.3.patch should be applied.



---

archive/issue_comments_043640.json:
```json
{
    "body": "Attachment [5598-test-coercion.patch](tarball://root/attachments/some-uuid/ticket5598/5598-test-coercion.patch) by @robertwb created at 2009-05-23 06:47:24\n\nI made a patch out of test-coercion. Apply, in order\n\n* 5598-coerce-declare.patch\n* 5598-ncalexan-fixes-and-tests.3.patch\n* 5598-test-coercion.patch (1.9 KB)\n\nI give the tests/documentation a positive review, if someone is willing to give a +1 on the original patch we can get this ticket in.",
    "created_at": "2009-05-23T06:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43640",
    "user": "@robertwb"
}
```

Attachment [5598-test-coercion.patch](tarball://root/attachments/some-uuid/ticket5598/5598-test-coercion.patch) by @robertwb created at 2009-05-23 06:47:24

I made a patch out of test-coercion. Apply, in order

* 5598-coerce-declare.patch
* 5598-ncalexan-fixes-and-tests.3.patch
* 5598-test-coercion.patch (1.9 KB)

I give the tests/documentation a positive review, if someone is willing to give a +1 on the original patch we can get this ticket in.



---

archive/issue_comments_043641.json:
```json
{
    "body": "It's not perfect but it's better than what was there before -- and doctested more than it was before!",
    "created_at": "2009-05-23T06:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43641",
    "user": "@ncalexan"
}
```

It's not perfect but it's better than what was there before -- and doctested more than it was before!



---

archive/issue_comments_043642.json:
```json
{
    "body": "Just a note: the added test adds a dependency on #5967. The later has a positive review, but Michael asked for a confirmation from a non sage-combinat person. Robert told me he would do this shortly.",
    "created_at": "2009-05-23T07:12:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43642",
    "user": "@nthiery"
}
```

Just a note: the added test adds a dependency on #5967. The later has a positive review, but Michael asked for a confirmation from a non sage-combinat person. Robert told me he would do this shortly.



---

archive/issue_comments_043643.json:
```json
{
    "body": "I merged \n\n\n```\n5598-coerce-declare.patch\n5598-ncalexan-fixes-and-tests.3.patch\n5598-test-coercion.patch\n```\n\n\nand got the following failures:\n\n\n```\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 863:\n    sage: K.unset_coercions_used()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_21[5]>\", line 1, in <module>\n        K.unset_coercions_used()###line 863:\n    sage: K.unset_coercions_used()\n    AttributeError: 'PolynomialRing_integral_domain' object has no attribute 'unset_coercions_used'\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 864:\n    sage: K.register_coercion(L_into_K)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_21[6]>\", line 1, in <module>\n        K.register_coercion(L_into_K)###line 864:\n    sage: K.register_coercion(L_into_K)\n      File \"parent.pyx\", line 853, in sage.structure.parent.Parent.register_coercion (sage/structure/parent.c:7450)\n        cpdef register_coercion(self, mor):\n      File \"parent.pyx\", line 878, in sage.structure.parent.Parent.register_coercion (sage/structure/parent.c:7239)\n        assert not self._coercions_used, \"coercions must all be registered up before use\"\n    AssertionError: coercions must all be registered up before use\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 866:\n    sage: K(0) + b\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_21[7]>\", line 1, in <module>\n        K(Integer(0)) + b###line 866:\n    sage: K(0) + b\n      File \"element.pyx\", line 729, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6533)\n        return coercion_model.bin_op(left, right, add)\n      File \"coerce.pyx\", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6589)\n        raise TypeError, arith_error_message(x,y,op)\n    TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in a over Integer Ring' and 'Univariate Polynomial Ring in b over Integer Ring'\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 868:\n    sage: a + b\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_21[8]>\", line 1, in <module>\n        a + b###line 868:\n    sage: a + b\n      File \"element.pyx\", line 729, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6533)\n        return coercion_model.bin_op(left, right, add)\n      File \"coerce.pyx\", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6589)\n        raise TypeError, arith_error_message(x,y,op)\n    TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in a over Integer Ring' and 'Univariate Polynomial Ring in b over Integer Ring'\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 870:\n    sage: K(b) # check that convert calls coerce first; normally this is just a\nExpected:\n    -a\nGot:\n    a\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 873:\n    sage: L(0) + a in K # this goes through the coercion mechanism of K\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_21[10]>\", line 1, in <module>\n        L(Integer(0)) + a in K # this goes through the coercion mechanism of K###line 873:\n    sage: L(0) + a in K # this goes through the coercion mechanism of K\n      File \"element.pyx\", line 729, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6533)\n        return coercion_model.bin_op(left, right, add)\n      File \"coerce.pyx\", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6589)\n        raise TypeError, arith_error_message(x,y,op)\n    TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in b over Integer Ring' and 'Univariate Polynomial Ring in a over Integer Ring'\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 931:\n    sage: R.unset_coercions_used()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_22[12]>\", line 1, in <module>\n        R.unset_coercions_used()###line 931:\n    sage: R.unset_coercions_used()\n    AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'unset_coercions_used'\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 945:\n    sage: R.unset_coercions_used()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_22[16]>\", line 1, in <module>\n        R.unset_coercions_used()###line 945:\n    sage: R.unset_coercions_used()\n    AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'unset_coercions_used'\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 975:\n    sage: K.unset_coercions_used()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_23[5]>\", line 1, in <module>\n        K.unset_coercions_used()###line 975:\n    sage: K.unset_coercions_used()\n    AttributeError: 'PolynomialRing_integral_domain' object has no attribute 'unset_coercions_used'\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 976:\n    sage: K.register_conversion(M_into_K)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_23[6]>\", line 1, in <module>\n        K.register_conversion(M_into_K)###line 976:\n    sage: K.register_conversion(M_into_K)\n      File \"parent.pyx\", line 965, in sage.structure.parent.Parent.register_conversion (sage/structure/parent.c:8015)\n        cpdef register_conversion(self, mor):\n      File \"parent.pyx\", line 985, in sage.structure.parent.Parent.register_conversion (sage/structure/parent.c:7825)\n        assert not self._coercions_used, \"coercions must all be registered up before use\"\n    AssertionError: coercions must all be registered up before use\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 1016:\n    sage: K.unset_coercions_used()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[7]>\", line 1, in <module>\n        K.unset_coercions_used()###line 1016:\n    sage: K.unset_coercions_used()\n    AttributeError: 'NumberField_quadratic' object has no attribute 'unset_coercions_used'\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 1017:\n    sage: K.register_embedding(K_into_MS)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[8]>\", line 1, in <module>\n        K.register_embedding(K_into_MS)###line 1017:\n    sage: K.register_embedding(K_into_MS)\n      File \"parent.pyx\", line 1000, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8246)\n        cpdef register_embedding(self, embedding):\n      File \"parent.pyx\", line 1039, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8084)\n        assert not self._coercions_used, \"coercions must all be registered up before use\"\n    AssertionError: coercions must all be registered up before use\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 1022:\n    sage: L.unset_coercions_used()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[12]>\", line 1, in <module>\n        L.unset_coercions_used()###line 1022:\n    sage: L.unset_coercions_used()\n    AttributeError: 'NumberField_quadratic' object has no attribute 'unset_coercions_used'\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 1023:\n    sage: L.register_embedding(L_into_MS)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[13]>\", line 1, in <module>\n        L.register_embedding(L_into_MS)###line 1023:\n    sage: L.register_embedding(L_into_MS)\n      File \"parent.pyx\", line 1000, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8246)\n        cpdef register_embedding(self, embedding):\n      File \"parent.pyx\", line 1039, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8084)\n        assert not self._coercions_used, \"coercions must all be registered up before use\"\n    AssertionError: coercions must all be registered up before use\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 1025:\n    sage: K.coerce_embedding()(a)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[14]>\", line 1, in <module>\n        K.coerce_embedding()(a)###line 1025:\n    sage: K.coerce_embedding()(a)\n    TypeError: 'NoneType' object is not callable\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 1028:\n    sage: L.coerce_embedding()(b)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[15]>\", line 1, in <module>\n        L.coerce_embedding()(b)###line 1028:\n    sage: L.coerce_embedding()(b)\n    TypeError: 'NoneType' object is not callable\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 1032:\n    sage: a.matrix() * b\nExpected:\n    [-272118       0]\n    [      0    -462]\nGot:\n    [           0      b521155]\n    [-462*b521155            0]\n**********************************************************************\nFile \"/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx\", line 1035:\n    sage: a * b.matrix()\nExpected:\n    [-272118       0]\n    [      0    -462]\nGot:\n    [              0         a161099]\n    [-272118*a161099               0]\n**********************************************************************\n4 items had failures:\n   6 of  12 in __main__.example_21\n   2 of  19 in __main__.example_22\n   2 of   9 in __main__.example_23\n   8 of  18 in __main__.example_24\n***Test Failed*** 18 failures.\n```\n",
    "created_at": "2009-06-01T00:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43643",
    "user": "@mwhansen"
}
```

I merged 


```
5598-coerce-declare.patch
5598-ncalexan-fixes-and-tests.3.patch
5598-test-coercion.patch
```


and got the following failures:


```
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 863:
    sage: K.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[5]>", line 1, in <module>
        K.unset_coercions_used()###line 863:
    sage: K.unset_coercions_used()
    AttributeError: 'PolynomialRing_integral_domain' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 864:
    sage: K.register_coercion(L_into_K)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[6]>", line 1, in <module>
        K.register_coercion(L_into_K)###line 864:
    sage: K.register_coercion(L_into_K)
      File "parent.pyx", line 853, in sage.structure.parent.Parent.register_coercion (sage/structure/parent.c:7450)
        cpdef register_coercion(self, mor):
      File "parent.pyx", line 878, in sage.structure.parent.Parent.register_coercion (sage/structure/parent.c:7239)
        assert not self._coercions_used, "coercions must all be registered up before use"
    AssertionError: coercions must all be registered up before use
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 866:
    sage: K(0) + b
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[7]>", line 1, in <module>
        K(Integer(0)) + b###line 866:
    sage: K(0) + b
      File "element.pyx", line 729, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6533)
        return coercion_model.bin_op(left, right, add)
      File "coerce.pyx", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6589)
        raise TypeError, arith_error_message(x,y,op)
    TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in a over Integer Ring' and 'Univariate Polynomial Ring in b over Integer Ring'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 868:
    sage: a + b
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[8]>", line 1, in <module>
        a + b###line 868:
    sage: a + b
      File "element.pyx", line 729, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6533)
        return coercion_model.bin_op(left, right, add)
      File "coerce.pyx", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6589)
        raise TypeError, arith_error_message(x,y,op)
    TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in a over Integer Ring' and 'Univariate Polynomial Ring in b over Integer Ring'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 870:
    sage: K(b) # check that convert calls coerce first; normally this is just a
Expected:
    -a
Got:
    a
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 873:
    sage: L(0) + a in K # this goes through the coercion mechanism of K
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[10]>", line 1, in <module>
        L(Integer(0)) + a in K # this goes through the coercion mechanism of K###line 873:
    sage: L(0) + a in K # this goes through the coercion mechanism of K
      File "element.pyx", line 729, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6533)
        return coercion_model.bin_op(left, right, add)
      File "coerce.pyx", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6589)
        raise TypeError, arith_error_message(x,y,op)
    TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in b over Integer Ring' and 'Univariate Polynomial Ring in a over Integer Ring'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 931:
    sage: R.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[12]>", line 1, in <module>
        R.unset_coercions_used()###line 931:
    sage: R.unset_coercions_used()
    AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 945:
    sage: R.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[16]>", line 1, in <module>
        R.unset_coercions_used()###line 945:
    sage: R.unset_coercions_used()
    AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 975:
    sage: K.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_23[5]>", line 1, in <module>
        K.unset_coercions_used()###line 975:
    sage: K.unset_coercions_used()
    AttributeError: 'PolynomialRing_integral_domain' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 976:
    sage: K.register_conversion(M_into_K)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_23[6]>", line 1, in <module>
        K.register_conversion(M_into_K)###line 976:
    sage: K.register_conversion(M_into_K)
      File "parent.pyx", line 965, in sage.structure.parent.Parent.register_conversion (sage/structure/parent.c:8015)
        cpdef register_conversion(self, mor):
      File "parent.pyx", line 985, in sage.structure.parent.Parent.register_conversion (sage/structure/parent.c:7825)
        assert not self._coercions_used, "coercions must all be registered up before use"
    AssertionError: coercions must all be registered up before use
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1016:
    sage: K.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[7]>", line 1, in <module>
        K.unset_coercions_used()###line 1016:
    sage: K.unset_coercions_used()
    AttributeError: 'NumberField_quadratic' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1017:
    sage: K.register_embedding(K_into_MS)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[8]>", line 1, in <module>
        K.register_embedding(K_into_MS)###line 1017:
    sage: K.register_embedding(K_into_MS)
      File "parent.pyx", line 1000, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8246)
        cpdef register_embedding(self, embedding):
      File "parent.pyx", line 1039, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8084)
        assert not self._coercions_used, "coercions must all be registered up before use"
    AssertionError: coercions must all be registered up before use
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1022:
    sage: L.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[12]>", line 1, in <module>
        L.unset_coercions_used()###line 1022:
    sage: L.unset_coercions_used()
    AttributeError: 'NumberField_quadratic' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1023:
    sage: L.register_embedding(L_into_MS)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[13]>", line 1, in <module>
        L.register_embedding(L_into_MS)###line 1023:
    sage: L.register_embedding(L_into_MS)
      File "parent.pyx", line 1000, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8246)
        cpdef register_embedding(self, embedding):
      File "parent.pyx", line 1039, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8084)
        assert not self._coercions_used, "coercions must all be registered up before use"
    AssertionError: coercions must all be registered up before use
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1025:
    sage: K.coerce_embedding()(a)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[14]>", line 1, in <module>
        K.coerce_embedding()(a)###line 1025:
    sage: K.coerce_embedding()(a)
    TypeError: 'NoneType' object is not callable
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1028:
    sage: L.coerce_embedding()(b)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[15]>", line 1, in <module>
        L.coerce_embedding()(b)###line 1028:
    sage: L.coerce_embedding()(b)
    TypeError: 'NoneType' object is not callable
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1032:
    sage: a.matrix() * b
Expected:
    [-272118       0]
    [      0    -462]
Got:
    [           0      b521155]
    [-462*b521155            0]
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1035:
    sage: a * b.matrix()
Expected:
    [-272118       0]
    [      0    -462]
Got:
    [              0         a161099]
    [-272118*a161099               0]
**********************************************************************
4 items had failures:
   6 of  12 in __main__.example_21
   2 of  19 in __main__.example_22
   2 of   9 in __main__.example_23
   8 of  18 in __main__.example_24
***Test Failed*** 18 failures.
```




---

archive/issue_comments_043644.json:
```json
{
    "body": "Attachment [trac_5598.patch](tarball://root/attachments/some-uuid/ticket5598/trac_5598.patch) by @mwhansen created at 2009-10-19 13:20:46\n\nI've attached trac_5598.patch which folds the above three together and is rebased for 4.2.  I believe this should pass all tests.",
    "created_at": "2009-10-19T13:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43644",
    "user": "@mwhansen"
}
```

Attachment [trac_5598.patch](tarball://root/attachments/some-uuid/ticket5598/trac_5598.patch) by @mwhansen created at 2009-10-19 13:20:46

I've attached trac_5598.patch which folds the above three together and is rebased for 4.2.  I believe this should pass all tests.



---

archive/issue_comments_043645.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-19T13:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43645",
    "user": "@mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043646.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-19T13:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43646",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043647.json:
```json
{
    "body": "The faliures above were just because in the tests \"unset_coercions_used\" should have been \"_unset_coercions_used\".\n\nAll tests pass with trac_5598.patch.",
    "created_at": "2009-10-19T13:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43647",
    "user": "@mwhansen"
}
```

The faliures above were just because in the tests "unset_coercions_used" should have been "_unset_coercions_used".

All tests pass with trac_5598.patch.



---

archive/issue_comments_043648.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-19T13:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5598#issuecomment-43648",
    "user": "@mwhansen"
}
```

Resolution: fixed
