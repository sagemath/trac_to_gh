# Issue 5294: Pickle Jar documentation

archive/issues_005294.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: picklejar, documentation\n\nOn sage-combinat-devel Michael wrote:\n\n \"The pickle jar is not in the documentation AFAIK and it definitely should be. So someone who thinks this is a good idea please open a ticket.\"\n\nI definitely think this is a good idea.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5294\n\n",
    "created_at": "2009-02-17T18:08:39Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "Pickle Jar documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5294",
    "user": "hivert"
}
```
Assignee: tba

Keywords: picklejar, documentation

On sage-combinat-devel Michael wrote:

 "The pickle jar is not in the documentation AFAIK and it definitely should be. So someone who thinks this is a good idea please open a ticket."

I definitely think this is a good idea.

Issue created by migration from https://trac.sagemath.org/ticket/5294





---

archive/issue_comments_040694.json:
```json
{
    "body": "The attached patch improves the pickle_jar documentation, with the primary aim of telling developers what to do (and not do) when their code breaks a pickle in the pickle_jar. I've added a version of the manual page produced so that people can comment on this without having to rebuild the manual -- unfortunately it doesn't display as html....",
    "created_at": "2012-10-19T00:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40694",
    "user": "andrew.mathas"
}
```

The attached patch improves the pickle_jar documentation, with the primary aim of telling developers what to do (and not do) when their code breaks a pickle in the pickle_jar. I've added a version of the manual page produced so that people can comment on this without having to rebuild the manual -- unfortunately it doesn't display as html....



---

archive/issue_comments_040695.json:
```json
{
    "body": "Currently one doc test fails, but I don't think that this is an issue with the patch. This seems to have nothing to do with the patch but, rather, is a consequence of the following which looks like a bug to me:\n\n\n```\nsage: from sage.structure.sage_object import unpickle_all\nsage: %timeit unpickle_all()\n/usr/local/src/sage/sage-5.3/local/lib/python/timeit.py:195: DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.\nSee http://trac.sagemath.org/4260 for details.\n  timing = self.inner(it, self.timer)\n\n------------------------------------------------------------------------\nUnhandled SIGABRT: An abort() occurred in Sage.\nThis probably occurred because a *compiled* component of Sage has a bug\nin it and is not properly wrapped with sig_on(), sig_off(). You might\nwant to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate.\n------------------------------------------------------------------------\n/usr/local/src/sage/sage-5.3/spkg/bin/sage: line 335: 73974 Abort trap: 6           sage-ipython \"$@\" -i\n```\n\nCan anyone confirm whether this is a bug or known issue? Either way, is there a way around this? \n\nAlternatively I could just remove this doc test from unpickle_all() as it is now referred to in the section in the developers guide.",
    "created_at": "2012-10-19T12:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40695",
    "user": "andrew.mathas"
}
```

Currently one doc test fails, but I don't think that this is an issue with the patch. This seems to have nothing to do with the patch but, rather, is a consequence of the following which looks like a bug to me:


```
sage: from sage.structure.sage_object import unpickle_all
sage: %timeit unpickle_all()
/usr/local/src/sage/sage-5.3/local/lib/python/timeit.py:195: DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.
See http://trac.sagemath.org/4260 for details.
  timing = self.inner(it, self.timer)

------------------------------------------------------------------------
Unhandled SIGABRT: An abort() occurred in Sage.
This probably occurred because a *compiled* component of Sage has a bug
in it and is not properly wrapped with sig_on(), sig_off(). You might
want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate.
------------------------------------------------------------------------
/usr/local/src/sage/sage-5.3/spkg/bin/sage: line 335: 73974 Abort trap: 6           sage-ipython "$@" -i
```

Can anyone confirm whether this is a bug or known issue? Either way, is there a way around this? 

Alternatively I could just remove this doc test from unpickle_all() as it is now referred to in the section in the developers guide.



---

archive/issue_comments_040696.json:
```json
{
    "body": "* The SIGABRT is certainly a bug, and a quick google search doesn't reveal any tickets related to it.\u00a0 Opening a new ticket seems reasonable.\u00a0 What's the doctest that fails?\n  * The changes in trac_5294--improving_pickle_jar_documentation-am.patch look great to me.  Here are a few more improvements I would suggest. \n   * Mention that pickling and unpickling is different for Cython classes and give some examples of how to write pickling code in this case.\u00a0 See http://ask.sagemath.org/question/808/pickling-extension-classes and http://docs.python.org/library/pickle.html#pickling-and-unpickling-extension-types.\u00a0 If you don't want to do this here we can open another ticket.\n   * Refer to sage.misc.explain_pickle as a tool to figure out what's in an old pickle that doesn't work any more.",
    "created_at": "2012-10-19T16:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40696",
    "user": "roed"
}
```

* The SIGABRT is certainly a bug, and a quick google search doesn't reveal any tickets related to it.  Opening a new ticket seems reasonable.  What's the doctest that fails?
  * The changes in trac_5294--improving_pickle_jar_documentation-am.patch look great to me.  Here are a few more improvements I would suggest. 
   * Mention that pickling and unpickling is different for Cython classes and give some examples of how to write pickling code in this case.  See http://ask.sagemath.org/question/808/pickling-extension-classes and http://docs.python.org/library/pickle.html#pickling-and-unpickling-extension-types.  If you don't want to do this here we can open another ticket.
   * Refer to sage.misc.explain_pickle as a tool to figure out what's in an old pickle that doesn't work any more.



---

archive/issue_comments_040697.json:
```json
{
    "body": "Replying to [comment:3 roed]:\n> The SIGABRT is certainly a bug, and a quick google search doesn't reveal any tickets related to it.  Opening a new ticket seems reasonable.  What's the doctest that fails?\n\nThe doctest that fails is essentially the problem above. The actual doctest, which appears below, is in unpickle_all() and it ends with the command unpickle_all(). It runs fine from the command line back buts when you run it via the doctest framework. The difference, I think, is that during a doctest the code is running inside of (something like) timeit(). Here is the doctest:\n\n\n```\nsage: from sage.structure.sage_object import unpickle_all, register_unpickle_override\nsage: class A(CombinatorialObject,sage.structure.element.Element):\n...       pass # to break a pickle\nsage: register_unpickle_override('sage.combinat.tableau','Tableau_class',A) # breaking the pickle\nsage: unpickle_all()  # long time\n```\n",
    "created_at": "2012-10-19T21:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40697",
    "user": "andrew.mathas"
}
```

Replying to [comment:3 roed]:
> The SIGABRT is certainly a bug, and a quick google search doesn't reveal any tickets related to it.  Opening a new ticket seems reasonable.  What's the doctest that fails?

The doctest that fails is essentially the problem above. The actual doctest, which appears below, is in unpickle_all() and it ends with the command unpickle_all(). It runs fine from the command line back buts when you run it via the doctest framework. The difference, I think, is that during a doctest the code is running inside of (something like) timeit(). Here is the doctest:


```
sage: from sage.structure.sage_object import unpickle_all, register_unpickle_override
sage: class A(CombinatorialObject,sage.structure.element.Element):
...       pass # to break a pickle
sage: register_unpickle_override('sage.combinat.tableau','Tableau_class',A) # breaking the pickle
sage: unpickle_all()  # long time
```




---

archive/issue_comments_040698.json:
```json
{
    "body": "I have added some comments about cython and explain_pickle (and filed the ticket #13636 for the bug). I also added sections to the developers guide at the end of the chapters \"Conventions for Coding in Sage\" and \"Coding in Cython about (un)pickling.",
    "created_at": "2012-10-22T02:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40698",
    "user": "andrew.mathas"
}
```

I have added some comments about cython and explain_pickle (and filed the ticket #13636 for the bug). I also added sections to the developers guide at the end of the chapters "Conventions for Coding in Sage" and "Coding in Cython about (un)pickling.



---

archive/issue_comments_040699.json:
```json
{
    "body": "I noticed that there were other calls to unpickle_all() in the documentation so after playing around for a little I worked out the register_unpickle_override calls in the doctests were causing the SEGABRT.  (However, the bug reported in #13636 appears to be real as it is independent of this patch.)\n\nI have rewritten the relevant examples in the documentation so all doc tests now pass.",
    "created_at": "2012-11-01T23:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40699",
    "user": "andrew.mathas"
}
```

I noticed that there were other calls to unpickle_all() in the documentation so after playing around for a little I worked out the register_unpickle_override calls in the doctests were causing the SEGABRT.  (However, the bug reported in #13636 appears to be real as it is independent of this patch.)

I have rewritten the relevant examples in the documentation so all doc tests now pass.



---

archive/issue_comments_040700.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-11-01T23:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40700",
    "user": "andrew.mathas"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_040701.json:
```json
{
    "body": "Changing assignee from tba to andrew.mathas.",
    "created_at": "2012-11-01T23:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40701",
    "user": "andrew.mathas"
}
```

Changing assignee from tba to andrew.mathas.



---

archive/issue_comments_040702.json:
```json
{
    "body": "A very valuable addition to the documentation!\n\nI think I found two minor issues though:\n\n* In the excerpt from the python docs about `object.__setstate__(state)` you lost some underscores (it should say `__setstate__` and not `setstate__`.)\n* You should probably remove the trailing whitespace in the `__reduce__` function that the patchbot complains about\n\nBtw., the patchbot coverage plugin complains that you added one method without a doctest. But this is actually just, the `__reduce___` method in the docstring.\n\nI don't have the time to look at the html version of the documentation now, I'll do that soon, write a review patch with the above two points, and set it to positive review.",
    "created_at": "2012-11-22T15:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40702",
    "user": "saraedum"
}
```

A very valuable addition to the documentation!

I think I found two minor issues though:

* In the excerpt from the python docs about `object.__setstate__(state)` you lost some underscores (it should say `__setstate__` and not `setstate__`.)
* You should probably remove the trailing whitespace in the `__reduce__` function that the patchbot complains about

Btw., the patchbot coverage plugin complains that you added one method without a doctest. But this is actually just, the `__reduce___` method in the docstring.

I don't have the time to look at the html version of the documentation now, I'll do that soon, write a review patch with the above two points, and set it to positive review.



---

archive/issue_comments_040703.json:
```json
{
    "body": "Thanks for this Julian. I have uploaded a new version of the patch which fixes the setstate  and the whitespace problems. To address the coverage plugin complaint I added in a doctest for dumps(), so now the coverage count is (should be) increased by the patch.\n\nAndrew",
    "created_at": "2012-11-23T04:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40703",
    "user": "andrew.mathas"
}
```

Thanks for this Julian. I have uploaded a new version of the patch which fixes the setstate  and the whitespace problems. To address the coverage plugin complaint I added in a doctest for dumps(), so now the coverage count is (should be) increased by the patch.

Andrew



---

archive/issue_comments_040704.json:
```json
{
    "body": "Changing keywords from \"picklejar, documentation\" to \"picklejar, documentation, beginner\".",
    "created_at": "2013-01-07T01:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40704",
    "user": "andrew.mathas"
}
```

Changing keywords from "picklejar, documentation" to "picklejar, documentation, beginner".



---

archive/issue_comments_040705.json:
```json
{
    "body": "Sorry this took so long to finally have a look at this :(\n\nOne minor issues:\n\n* your patch file should start with \"Trac #5294: Adds information ...\"\n\nI found a few small problems in your patch and wrote a review patch for it. If you're happy with these changes, feel free to set it to positive review.",
    "created_at": "2013-01-07T22:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40705",
    "user": "saraedum"
}
```

Sorry this took so long to finally have a look at this :(

One minor issues:

* your patch file should start with "Trac #5294: Adds information ..."

I found a few small problems in your patch and wrote a review patch for it. If you're happy with these changes, feel free to set it to positive review.



---

archive/issue_comments_040706.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-08T02:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40706",
    "user": "andrew.mathas"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040707.json:
```json
{
    "body": "Thanks very much Julian. I have folder in your review patch and set it to a positive review.",
    "created_at": "2013-01-08T02:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40707",
    "user": "andrew.mathas"
}
```

Thanks very much Julian. I have folder in your review patch and set it to a positive review.



---

archive/issue_comments_040708.json:
```json
{
    "body": "The docbuilder doesn't like all those weird characters on line 218 of `sage/structure/sage_object.pyx`:\n\n```\n! Package ucs Error: Unknown Unicode character 156 = U+009C,\n(ucs)                possibly declared in uni-0.def.\n(ucs)                Type H to see if it is available with options.\n\nSee the ucs package documentation for explanation.\nType  H <return>  for immediate help.\n ...\n\nl.111426 ...~T\u00c3\u00a4^^R\u00c2\u00ae{}` \u00c3~[^^_\u00c3~B,d\u00c3~Tl,d\u00c3~R\\PYGZca{}}\n\n?\n! Emergency stop.\n ...\n\nl.111426 ...~T\u00c3\u00a4^^R\u00c2\u00ae{}` \u00c3~[^^_\u00c3~B,d\u00c3~Tl,d\u00c3~R\\PYGZca{}}\n\n!  ==> Fatal error occurred, no output PDF file produced!\n```\n",
    "created_at": "2013-01-08T09:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40708",
    "user": "jdemeyer"
}
```

The docbuilder doesn't like all those weird characters on line 218 of `sage/structure/sage_object.pyx`:

```
! Package ucs Error: Unknown Unicode character 156 = U+009C,
(ucs)                possibly declared in uni-0.def.
(ucs)                Type H to see if it is available with options.

See the ucs package documentation for explanation.
Type  H <return>  for immediate help.
 ...

l.111426 ...~TÃ¤^^RÂ®{}` Ã~[^^_Ã~B,dÃ~Tl,dÃ~R\PYGZca{}}

?
! Emergency stop.
 ...

l.111426 ...~TÃ¤^^RÂ®{}` Ã~[^^_Ã~B,dÃ~Tl,dÃ~R\PYGZca{}}

!  ==> Fatal error occurred, no output PDF file produced!
```




---

archive/issue_comments_040709.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-01-08T09:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40709",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_040710.json:
```json
{
    "body": "Thanks for tracking down the code block for me. It's embarrassing that you keep on finding all of these errors that I don't...fixed now I think.\n\nAndrew",
    "created_at": "2013-01-08T12:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40710",
    "user": "andrew.mathas"
}
```

Thanks for tracking down the code block for me. It's embarrassing that you keep on finding all of these errors that I don't...fixed now I think.

Andrew



---

archive/issue_comments_040711.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-01-08T12:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40711",
    "user": "andrew.mathas"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_040712.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-01-08T15:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40712",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_040713.json:
```json
{
    "body": "There's an obvious doctest failure:\n\n```\nsage -t  -force_lib devel/sage/doc/en/developer/conventions.rst\n**********************************************************************\nFile \"/release/merger/sage-5.6.beta3/devel/sage-main/doc/en/developer/conventions.rst\", line 1040:\n    sage: sage -t structure/sage_object.pyx\nException raised:\n    Traceback (most recent call last):\n      File \"/release/merger/sage-5.6.beta3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/release/merger/sage-5.6.beta3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/release/merger/sage-5.6.beta3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_21[2]>\", line 1\n        sage -t structure/sage_object.pyx###line 1040:\n    sage: sage -t structure/sage_object.pyx\n                        ^\n    SyntaxError: invalid syntax\n**********************************************************************\n```\n",
    "created_at": "2013-01-08T15:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40713",
    "user": "jdemeyer"
}
```

There's an obvious doctest failure:

```
sage -t  -force_lib devel/sage/doc/en/developer/conventions.rst
**********************************************************************
File "/release/merger/sage-5.6.beta3/devel/sage-main/doc/en/developer/conventions.rst", line 1040:
    sage: sage -t structure/sage_object.pyx
Exception raised:
    Traceback (most recent call last):
      File "/release/merger/sage-5.6.beta3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/release/merger/sage-5.6.beta3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/release/merger/sage-5.6.beta3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[2]>", line 1
        sage -t structure/sage_object.pyx###line 1040:
    sage: sage -t structure/sage_object.pyx
                        ^
    SyntaxError: invalid syntax
**********************************************************************
```




---

archive/issue_comments_040714.json:
```json
{
    "body": "And perhaps this failure is also caused by this ticket:\n\n```\nsage -t  --long -force_lib devel/sage/sage/structure/sage_object.pyx\n/release/merger/sage-5.6.beta3/local/lib/libcsage.so(print_backtrace+0x2b)[0x2ba301ee166e]\n/release/merger/sage-5.6.beta3/local/lib/libcsage.so(sigdie+0x14)[0x2ba301ee169b]\n/release/merger/sage-5.6.beta3/local/lib/libcsage.so(sage_signal_handler+0x1d8)[0x2ba301ee1156]\n/lib/libpthread.so.0[0x2ba2fff4b7d0]\n/lib/libc.so.6(gsignal+0x35)[0x2ba3008140c5]\n/lib/libc.so.6(abort+0x110)[0x2ba300815b20]\n/release/merger/sage-5.6.beta3/local/lib/libcsage.so(init_csage+0x0)[0x2ba301ee1fc8]\n/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL5ErrorEPKc+0x1f)[0x2ba30255e4cf]\n/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL6InvModEll+0x39)[0x2ba3024ad1a9]\n/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL8PlainRemERNS_5zz_pXERKS0_S3_+0x2a9)[0x2ba3025222a9]\n/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL3GCDERNS_5zz_pXERKS0_S3_+0x19a)[0x2ba30252f7fa]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so[0x2ba31acb0216]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z8gcd_polyRK13CanonicalFormS1_+0x605)[0x2ba31acabda5]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z3gcdRK13CanonicalFormS1_+0x257)[0x2ba31acac2e7]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so[0x2ba31acae0fd]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z7contentRK13CanonicalFormRK8Variable+0xce)[0x2ba31acae29e]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z7contentRK13CanonicalFormRK8Variable+0x62)[0x2ba31acae232]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z7EZGCD_PRK13CanonicalFormS1_+0xde8)[0x2ba31acc5378]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z8gcd_polyRK13CanonicalFormS1_+0x59f)[0x2ba31acabd3f]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z11chinrem_gcdRK13CanonicalFormS1_+0xbab)[0x2ba31acad13b]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z8gcd_polyRK13CanonicalFormS1_+0x656)[0x2ba31acabdf6]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z3gcdRK13CanonicalFormS1_+0x257)[0x2ba31acac2e7]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z14singclap_gcd_rP8spolyrecS0_P9sip_sring+0xf8)[0x2ba31ab0ba28]\n/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z12singclap_gcdP8spolyrecS0_+0x56)[0x2ba31ab0eb26]\n/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so[0x2ba31a7851df]\n/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so[0x2ba31a7868ef]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_CallObjectWithKeywords+0x56)[0x2ba2ffc3eb26]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbbad06]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/element.so[0x2ba3093808c3]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/fraction_field_element.so[0x2ba315661005]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/fraction_field_element.so[0x2ba31565941c]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbfa5a8]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/fraction_field_element.so[0x2ba31564b644]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_CallObjectWithKeywords+0x56)[0x2ba2ffc3eb26]\n/release/merger/sage-5.6.beta3/local/lib/python2.7/lib-dynload/cPickle.so[0x2ba30528381e]\n/release/merger/sage-5.6.beta3/local/lib/python2.7/lib-dynload/cPickle.so[0x2ba30528a162]\n/release/merger/sage-5.6.beta3/local/lib/python2.7/lib-dynload/cPickle.so[0x2ba30528dc35]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/sage_object.so[0x2ba305d2bbc4]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/sage_object.so[0x2ba305d1c693]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/sage_object.so[0x2ba305d23d06]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5de2)[0x2ba2ffc45662]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x2ba2ffc47472]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x714e)[0x2ba2ffc469ce]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbcb9b9]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbae8bf]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x1299)[0x2ba2ffc40b19]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbcb9b9]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbae8bf]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x1299)[0x2ba2ffc40b19]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbcb9b9]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbae8bf]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x1299)[0x2ba2ffc40b19]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x2ba2ffc47472]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyRun_FileExFlags+0xc1)[0x2ba2ffc6b1f1]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyRun_SimpleFileExFlags+0x1f9)[0x2ba2ffc6b4c9]\n/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(Py_Main+0xb15)[0x2ba2ffc7e115]\n/lib/libc.so.6(__libc_start_main+0xf4)[0x2ba3008001f4]\npython[0x400679]\n\n------------------------------------------------------------------------\nUnhandled SIGABRT: An abort() occurred in Sage.\nThis probably occurred because a *compiled* component of Sage has a bug\nin it and is not properly wrapped with sig_on(), sig_off(). You might\nwant to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate.\n------------------------------------------------------------------------\nAborted\n```\n",
    "created_at": "2013-01-08T15:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40714",
    "user": "jdemeyer"
}
```

And perhaps this failure is also caused by this ticket:

```
sage -t  --long -force_lib devel/sage/sage/structure/sage_object.pyx
/release/merger/sage-5.6.beta3/local/lib/libcsage.so(print_backtrace+0x2b)[0x2ba301ee166e]
/release/merger/sage-5.6.beta3/local/lib/libcsage.so(sigdie+0x14)[0x2ba301ee169b]
/release/merger/sage-5.6.beta3/local/lib/libcsage.so(sage_signal_handler+0x1d8)[0x2ba301ee1156]
/lib/libpthread.so.0[0x2ba2fff4b7d0]
/lib/libc.so.6(gsignal+0x35)[0x2ba3008140c5]
/lib/libc.so.6(abort+0x110)[0x2ba300815b20]
/release/merger/sage-5.6.beta3/local/lib/libcsage.so(init_csage+0x0)[0x2ba301ee1fc8]
/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL5ErrorEPKc+0x1f)[0x2ba30255e4cf]
/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL6InvModEll+0x39)[0x2ba3024ad1a9]
/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL8PlainRemERNS_5zz_pXERKS0_S3_+0x2a9)[0x2ba3025222a9]
/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL3GCDERNS_5zz_pXERKS0_S3_+0x19a)[0x2ba30252f7fa]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so[0x2ba31acb0216]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z8gcd_polyRK13CanonicalFormS1_+0x605)[0x2ba31acabda5]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z3gcdRK13CanonicalFormS1_+0x257)[0x2ba31acac2e7]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so[0x2ba31acae0fd]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z7contentRK13CanonicalFormRK8Variable+0xce)[0x2ba31acae29e]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z7contentRK13CanonicalFormRK8Variable+0x62)[0x2ba31acae232]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z7EZGCD_PRK13CanonicalFormS1_+0xde8)[0x2ba31acc5378]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z8gcd_polyRK13CanonicalFormS1_+0x59f)[0x2ba31acabd3f]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z11chinrem_gcdRK13CanonicalFormS1_+0xbab)[0x2ba31acad13b]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z8gcd_polyRK13CanonicalFormS1_+0x656)[0x2ba31acabdf6]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z3gcdRK13CanonicalFormS1_+0x257)[0x2ba31acac2e7]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z14singclap_gcd_rP8spolyrecS0_P9sip_sring+0xf8)[0x2ba31ab0ba28]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z12singclap_gcdP8spolyrecS0_+0x56)[0x2ba31ab0eb26]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so[0x2ba31a7851df]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so[0x2ba31a7868ef]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_CallObjectWithKeywords+0x56)[0x2ba2ffc3eb26]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbbad06]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/element.so[0x2ba3093808c3]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/fraction_field_element.so[0x2ba315661005]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/fraction_field_element.so[0x2ba31565941c]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbfa5a8]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/fraction_field_element.so[0x2ba31564b644]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_CallObjectWithKeywords+0x56)[0x2ba2ffc3eb26]
/release/merger/sage-5.6.beta3/local/lib/python2.7/lib-dynload/cPickle.so[0x2ba30528381e]
/release/merger/sage-5.6.beta3/local/lib/python2.7/lib-dynload/cPickle.so[0x2ba30528a162]
/release/merger/sage-5.6.beta3/local/lib/python2.7/lib-dynload/cPickle.so[0x2ba30528dc35]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/sage_object.so[0x2ba305d2bbc4]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/sage_object.so[0x2ba305d1c693]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/sage_object.so[0x2ba305d23d06]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5de2)[0x2ba2ffc45662]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x2ba2ffc47472]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x714e)[0x2ba2ffc469ce]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbcb9b9]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbae8bf]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x1299)[0x2ba2ffc40b19]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbcb9b9]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbae8bf]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x1299)[0x2ba2ffc40b19]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbcb9b9]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbae8bf]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x1299)[0x2ba2ffc40b19]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x2ba2ffc47472]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyRun_FileExFlags+0xc1)[0x2ba2ffc6b1f1]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyRun_SimpleFileExFlags+0x1f9)[0x2ba2ffc6b4c9]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(Py_Main+0xb15)[0x2ba2ffc7e115]
/lib/libc.so.6(__libc_start_main+0xf4)[0x2ba3008001f4]
python[0x400679]

------------------------------------------------------------------------
Unhandled SIGABRT: An abort() occurred in Sage.
This probably occurred because a *compiled* component of Sage has a bug
in it and is not properly wrapped with sig_on(), sig_off(). You might
want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate.
------------------------------------------------------------------------
Aborted
```




---

archive/issue_comments_040715.json:
```json
{
    "body": "I'm confused because the first test\n\n```\nsage -t -force_lib devel/sage/doc/en/developer/conventions.rst\n```\n\npasses on sage 5.5. So I compiled 5.6.beta2 (beta3 has not been released yet) and it works there too. Nonetheless, even though I can't replicate the error I agree that there is a problem here so I've fixed it, but I can't check that it's fixed.\n\nWith the second test, \n\n```\nsage -t --long -force_lib devel/sage/sage/structure/sage_object.pyx\n```\n\nI get a timeout error rather than a SIGBART. It's caused by a call to \n\n```\nsage: unpickle_all() # long time\n```\n\nThis test works but it would take longer than the *#long time* tests are supposed to take so I have replaced this with\n\n```\nsage: unpickle_all()  # todo: not tested\n```\n",
    "created_at": "2013-01-09T02:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40715",
    "user": "andrew.mathas"
}
```

I'm confused because the first test

```
sage -t -force_lib devel/sage/doc/en/developer/conventions.rst
```

passes on sage 5.5. So I compiled 5.6.beta2 (beta3 has not been released yet) and it works there too. Nonetheless, even though I can't replicate the error I agree that there is a problem here so I've fixed it, but I can't check that it's fixed.

With the second test, 

```
sage -t --long -force_lib devel/sage/sage/structure/sage_object.pyx
```

I get a timeout error rather than a SIGBART. It's caused by a call to 

```
sage: unpickle_all() # long time
```

This test works but it would take longer than the *#long time* tests are supposed to take so I have replaced this with

```
sage: unpickle_all()  # todo: not tested
```




---

archive/issue_comments_040716.json:
```json
{
    "body": "Replying to [comment:19 andrew.mathas]:\n> I'm confused because the first test\n> {{{\n> sage -t -force_lib devel/sage/doc/en/developer/conventions.rst\n> }}}\n> passes on sage 5.5.\nSorry, I know what happened. There are some formatting errors in that file with the consequence that doctests aren't run. This is fixed by #13899.",
    "created_at": "2013-01-09T07:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40716",
    "user": "jdemeyer"
}
```

Replying to [comment:19 andrew.mathas]:
> I'm confused because the first test
> {{{
> sage -t -force_lib devel/sage/doc/en/developer/conventions.rst
> }}}
> passes on sage 5.5.
Sorry, I know what happened. There are some formatting errors in that file with the consequence that doctests aren't run. This is fixed by #13899.



---

archive/issue_comments_040717.json:
```json
{
    "body": "Replying to [comment:20 jdemeyer]:\n\n> Sorry, I know what happened. There are some formatting errors in that file with the consequence that doctests aren't run. This is fixed by #13899.\n\nThanks for the explanation. Does that mean that the problem with this patch is fixed or should it depend on, and need to be rebased over, #13899?\n\nAndrew",
    "created_at": "2013-01-09T08:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40717",
    "user": "andrew.mathas"
}
```

Replying to [comment:20 jdemeyer]:

> Sorry, I know what happened. There are some formatting errors in that file with the consequence that doctests aren't run. This is fixed by #13899.

Thanks for the explanation. Does that mean that the problem with this patch is fixed or should it depend on, and need to be rebased over, #13899?

Andrew



---

archive/issue_comments_040718.json:
```json
{
    "body": "This patch doesn't depend on #13899, but it should be tested with #13899 applied.",
    "created_at": "2013-01-09T08:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40718",
    "user": "jdemeyer"
}
```

This patch doesn't depend on #13899, but it should be tested with #13899 applied.



---

archive/issue_comments_040719.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-01-10T09:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40719",
    "user": "andrew.mathas"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_040720.json:
```json
{
    "body": "I've just tested the patch against 5.6.beta3, which has #13899 applied, and the tests above pass. I'm checking everything else now but given that the patch only touches doctests I don't think that they can possibly fail, so I'll put it back to a positive review.",
    "created_at": "2013-01-10T09:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40720",
    "user": "andrew.mathas"
}
```

I've just tested the patch against 5.6.beta3, which has #13899 applied, and the tests above pass. I'm checking everything else now but given that the patch only touches doctests I don't think that they can possibly fail, so I'll put it back to a positive review.



---

archive/issue_comments_040721.json:
```json
{
    "body": "Replying to [comment:23 andrew.mathas]:\n> I've just tested the patch against 5.6.beta3, which has #13899 applied, and the tests above pass. I'm checking everything else now but given that the patch only touches doctests I don't think that they can possibly fail, so I'll put it back to a positive review.\n\n\nJust to confirm: all tests pass on 5.6.beta3",
    "created_at": "2013-01-10T10:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40721",
    "user": "andrew.mathas"
}
```

Replying to [comment:23 andrew.mathas]:
> I've just tested the patch against 5.6.beta3, which has #13899 applied, and the tests above pass. I'm checking everything else now but given that the patch only touches doctests I don't think that they can possibly fail, so I'll put it back to a positive review.


Just to confirm: all tests pass on 5.6.beta3



---

archive/issue_comments_040722.json:
```json
{
    "body": "There is still:\n\n```\nsage -t  -force_lib devel/sage/doc/en/developer/conventions.rst\n**********************************************************************\nFile \"/release/merger/sage-5.7.alpha0/devel/sage-main/doc/en/developer/conventions.rst\", line 1052:\n    sage: sage -t devel/sage-main/sage/structure/sage_object.pyx\nException raised:\n    Traceback (most recent call last):\n      File \"/release/merger/sage-5.7.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/release/merger/sage-5.7.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/release/merger/sage-5.7.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_21[2]>\", line 1\n        sage -t devel/sage-main/sage/structure/sage_object.pyx###line 1052:\n    sage: sage -t devel/sage-main/sage/structure/sage_object.pyx\n                    ^\n    SyntaxError: invalid syntax\n**********************************************************************\n```\n",
    "created_at": "2013-01-12T15:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40722",
    "user": "jdemeyer"
}
```

There is still:

```
sage -t  -force_lib devel/sage/doc/en/developer/conventions.rst
**********************************************************************
File "/release/merger/sage-5.7.alpha0/devel/sage-main/doc/en/developer/conventions.rst", line 1052:
    sage: sage -t devel/sage-main/sage/structure/sage_object.pyx
Exception raised:
    Traceback (most recent call last):
      File "/release/merger/sage-5.7.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/release/merger/sage-5.7.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/release/merger/sage-5.7.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[2]>", line 1
        sage -t devel/sage-main/sage/structure/sage_object.pyx###line 1052:
    sage: sage -t devel/sage-main/sage/structure/sage_object.pyx
                    ^
    SyntaxError: invalid syntax
**********************************************************************
```




---

archive/issue_comments_040723.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-01-12T15:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40723",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_040724.json:
```json
{
    "body": "UPdated patch fixing conventions.srt problem",
    "created_at": "2013-01-13T08:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40724",
    "user": "andrew.mathas"
}
```

UPdated patch fixing conventions.srt problem



---

archive/issue_comments_040725.json:
```json
{
    "body": "Attachment\n\nSorry in all of the excitement I forgot to update the patch on the ticket.",
    "created_at": "2013-01-13T08:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40725",
    "user": "andrew.mathas"
}
```

Attachment

Sorry in all of the excitement I forgot to update the patch on the ticket.



---

archive/issue_comments_040726.json:
```json
{
    "body": "I have tested the patch against 5.6.rc1 and the tests pass. For some reason the patchbot isn't checking the ticket, possibly because it's flagged as needing work? I am going to put it back to a positive review in the hope that the patchbot confirms my tests before Jeronen looks at it.",
    "created_at": "2013-01-22T12:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40726",
    "user": "andrew.mathas"
}
```

I have tested the patch against 5.6.rc1 and the tests pass. For some reason the patchbot isn't checking the ticket, possibly because it's flagged as needing work? I am going to put it back to a positive review in the hope that the patchbot confirms my tests before Jeronen looks at it.



---

archive/issue_comments_040727.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-01-22T12:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40727",
    "user": "andrew.mathas"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_040728.json:
```json
{
    "body": "Concerning the pickle jar, I use this opportunity to make some publicity for #10705.",
    "created_at": "2013-01-25T00:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40728",
    "user": "slabbe"
}
```

Concerning the pickle jar, I use this opportunity to make some publicity for #10705.



---

archive/issue_comments_040729.json:
```json
{
    "body": "Replying to [comment:30 slabbe]:\n> Concerning the pickle jar, I use this opportunity to make some publicity for #10705.\n\nSee #13636 for another seg fault associated with unpickle_all.",
    "created_at": "2013-01-25T00:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40729",
    "user": "andrew.mathas"
}
```

Replying to [comment:30 slabbe]:
> Concerning the pickle jar, I use this opportunity to make some publicity for #10705.

See #13636 for another seg fault associated with unpickle_all.



---

archive/issue_comments_040730.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-01-26T09:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5294#issuecomment-40730",
    "user": "jdemeyer"
}
```

Resolution: fixed
