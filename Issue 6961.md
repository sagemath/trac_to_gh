# Issue 6961: provide wrapper for psi function of GiNaC

archive/issues_006961.json:
```json
{
    "body": "From sage-support:\n\n\n```\nOn Fri, 18 Sep 2009 15:47:45 -0700 (PDT)\nThe_Fool <masterfulet@yahoo.com> wrote:\n\n> While working with the derivative of the Gamma function, the digamma\n> function is obviously involved.  The sage \"diff\" function does show \u0393\n> '(x) == \u0393(x)\u03c8(x) like it should, however, the digamma function (called\n> psi in sage) is not defined whenever I try to do anything with it.  It\n> seems as if only the output of \"diff\" can use this function.\n```\n\n\n`psi()` is defined in GiNaC, but we don't provide wrappers for it.\n\nDefining a function `psi`, similar to the way `arctan2` is defined in line 422 of `sage/functions/trig.py` should fix this.\n\n\nThe sage-support thread is here:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/1ad313c921b7dbc0\n\nIssue created by migration from https://trac.sagemath.org/ticket/6961\n\n",
    "created_at": "2009-09-19T15:32:32Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "provide wrapper for psi function of GiNaC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6961",
    "user": "burcin"
}
```
From sage-support:


```
On Fri, 18 Sep 2009 15:47:45 -0700 (PDT)
The_Fool <masterfulet@yahoo.com> wrote:

> While working with the derivative of the Gamma function, the digamma
> function is obviously involved.  The sage "diff" function does show Γ
> '(x) == Γ(x)ψ(x) like it should, however, the digamma function (called
> psi in sage) is not defined whenever I try to do anything with it.  It
> seems as if only the output of "diff" can use this function.
```


`psi()` is defined in GiNaC, but we don't provide wrappers for it.

Defining a function `psi`, similar to the way `arctan2` is defined in line 422 of `sage/functions/trig.py` should fix this.


The sage-support thread is here:

http://groups.google.com/group/sage-support/browse_thread/thread/1ad313c921b7dbc0

Issue created by migration from https://trac.sagemath.org/ticket/6961





---

archive/issue_comments_057575.json:
```json
{
    "body": "More precisely:\n\n```\nsage: diff(gamma(x), x)\ngamma(x)*psi(x)\n```\n\nbut \"psi\" is unknown to Sage...",
    "created_at": "2009-09-21T06:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57575",
    "user": "zimmerma"
}
```

More precisely:

```
sage: diff(gamma(x), x)
gamma(x)*psi(x)
```

but "psi" is unknown to Sage...



---

archive/issue_comments_057576.json:
```json
{
    "body": "Attachment [trac_6961-psi.patch](tarball://root/attachments/some-uuid/ticket6961/trac_6961-psi.patch) by burcin created at 2010-01-17 05:00:00\n\nwrappers for psi function from pynac",
    "created_at": "2010-01-17T05:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57576",
    "user": "burcin"
}
```

Attachment [trac_6961-psi.patch](tarball://root/attachments/some-uuid/ticket6961/trac_6961-psi.patch) by burcin created at 2010-01-17 05:00:00

wrappers for psi function from pynac



---

archive/issue_comments_057577.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-17T05:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57577",
    "user": "burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_057578.json:
```json
{
    "body": "It turns out defining this function wasn't as straightforward as I thought. Pynac defines 2 functions with the same name `psi`. :)\n\nattachment:trac_6961-psi.patch wraps these 2 functions, and provides a global `psi()` to call the appropriate one. Unpickling these correctly requires changes in pynac. I'll make a new pynac package available later this week.",
    "created_at": "2010-01-17T05:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57578",
    "user": "burcin"
}
```

It turns out defining this function wasn't as straightforward as I thought. Pynac defines 2 functions with the same name `psi`. :)

attachment:trac_6961-psi.patch wraps these 2 functions, and provides a global `psi()` to call the appropriate one. Unpickling these correctly requires changes in pynac. I'll make a new pynac package available later this week.



---

archive/issue_comments_057579.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-19T14:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57579",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057580.json:
```json
{
    "body": "New pynac package available here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg\n\nThe package contains fixes for #7822, #6961, #7876, #7363, #6465 and #6559. From these #7876 and #7363 contain printing fixes. Doctests should be run at least with patches from these two tickets.",
    "created_at": "2010-01-19T14:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57580",
    "user": "burcin"
}
```

New pynac package available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

The package contains fixes for #7822, #6961, #7876, #7363, #6465 and #6559. From these #7876 and #7363 contain printing fixes. Doctests should be run at least with patches from these two tickets.



---

archive/issue_comments_057581.json:
```json
{
    "body": "The patch on this ticket conflicts with #6207. If I first apply the patches on #6207 to Sage 4.3.1, and then [trac_6961-psi.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.patch), I would get a hunk failure:\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6207/trac_6207.patch && hg qpush\nadding trac_6207.patch to series file\napplying trac_6207.patch\nnow at: trac_6207.patch\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6207/trac_6207-part2.patch && hg qpush\nadding trac_6207-part2.patch to series file\napplying trac_6207-part2.patch\nnow at: trac_6207-part2.patch\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6207/trac_6207-review.patch && hg qpush\nadding trac_6207-review.patch to series file\napplying trac_6207-review.patch\nnow at: trac_6207-review.patch\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6961/trac_6961-psi.patch && hg qpush\nadding trac_6961-psi.patch to series file\napplying trac_6961-psi.patch\npatching file sage/symbolic/pynac.pyx\nHunk #2 FAILED at 1566\n1 out of 3 hunks FAILED -- saving rejects to file sage/symbolic/pynac.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_6961-psi.patch\n```\n\nPerhaps you want to rebase [trac_6961-psi.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.patch) on top of #6207?",
    "created_at": "2010-01-25T19:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57581",
    "user": "mvngu"
}
```

The patch on this ticket conflicts with #6207. If I first apply the patches on #6207 to Sage 4.3.1, and then [trac_6961-psi.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.patch), I would get a hunk failure:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6207/trac_6207.patch && hg qpush
adding trac_6207.patch to series file
applying trac_6207.patch
now at: trac_6207.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6207/trac_6207-part2.patch && hg qpush
adding trac_6207-part2.patch to series file
applying trac_6207-part2.patch
now at: trac_6207-part2.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6207/trac_6207-review.patch && hg qpush
adding trac_6207-review.patch to series file
applying trac_6207-review.patch
now at: trac_6207-review.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6961/trac_6961-psi.patch && hg qpush
adding trac_6961-psi.patch to series file
applying trac_6961-psi.patch
patching file sage/symbolic/pynac.pyx
Hunk #2 FAILED at 1566
1 out of 3 hunks FAILED -- saving rejects to file sage/symbolic/pynac.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_6961-psi.patch
```

Perhaps you want to rebase [trac_6961-psi.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.patch) on top of #6207?



---

archive/issue_comments_057582.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-25T19:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57582",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057583.json:
```json
{
    "body": "Attachment [trac_6961-psi.rebased.patch](tarball://root/attachments/some-uuid/ticket6961/trac_6961-psi.rebased.patch) by burcin created at 2010-01-25 20:23:22\n\nrebased",
    "created_at": "2010-01-25T20:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57583",
    "user": "burcin"
}
```

Attachment [trac_6961-psi.rebased.patch](tarball://root/attachments/some-uuid/ticket6961/trac_6961-psi.rebased.patch) by burcin created at 2010-01-25 20:23:22

rebased



---

archive/issue_comments_057584.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-25T20:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57584",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057585.json:
```json
{
    "body": "The unrebased patch is fine; I can't get the other patches in the symbolics queue to work off of the rebase, not yet anyway.\n\nIf there is time, would it be possible to make an alias polygamma = psi2?  Not just because Mma uses it, but because a lot of references call it that (such as the ones a students of mine is using for some research) in written form.  This is great functionality to add, though.",
    "created_at": "2010-01-28T21:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57585",
    "user": "kcrisman"
}
```

The unrebased patch is fine; I can't get the other patches in the symbolics queue to work off of the rebase, not yet anyway.

If there is time, would it be possible to make an alias polygamma = psi2?  Not just because Mma uses it, but because a lot of references call it that (such as the ones a students of mine is using for some research) in written form.  This is great functionality to add, though.



---

archive/issue_comments_057586.json:
```json
{
    "body": "Replying to [comment:3 burcin]:\n> New pynac package available here:\n> \n> http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg\n> \n\nNow apparently at boxen.math instead.",
    "created_at": "2010-02-04T03:23:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57586",
    "user": "kcrisman"
}
```

Replying to [comment:3 burcin]:
> New pynac package available here:
> 
> http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg
> 

Now apparently at boxen.math instead.



---

archive/issue_comments_057587.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-15T08:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57587",
    "user": "rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057588.json:
```json
{
    "body": "Changing keywords from \"\" to \"psi, gamma, digamma, polygamma\".",
    "created_at": "2010-02-15T08:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57588",
    "user": "rossk"
}
```

Changing keywords from "" to "psi, gamma, digamma, polygamma".



---

archive/issue_comments_057589.json:
```json
{
    "body": "\n```\nsage: diff(gamma(x),x)/gamma(x) # definition of digamma (or \"psi\")\npsi(x)\n\nsage: diff(gamma(x),x).subs(x=1)\n-euler_gamma\n\nsage: psi(1)\n-euler_gamma\n\n# analytical result\nsage: psi(1/2)\n-euler_gamma - 2*log(2)\n\n# numerical examples\nsage: psi(.5)\n-1.96351002602142\n\nsage: psi(.5r)\n-1.9635100260214233\n\nsage: psi(complex(.5))\n(-1.9635100260214233+0j)\n\n# 1st argument means 0'th derivative (so psi(0, x) = psi(x))\nsage: psi(0, .5)\npsi(0.500000000000000)\n\nsage: N(psi(0, .5))\n-1.96351002602142\n```\n",
    "created_at": "2010-02-15T08:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57589",
    "user": "rossk"
}
```


```
sage: diff(gamma(x),x)/gamma(x) # definition of digamma (or "psi")
psi(x)

sage: diff(gamma(x),x).subs(x=1)
-euler_gamma

sage: psi(1)
-euler_gamma

# analytical result
sage: psi(1/2)
-euler_gamma - 2*log(2)

# numerical examples
sage: psi(.5)
-1.96351002602142

sage: psi(.5r)
-1.9635100260214233

sage: psi(complex(.5))
(-1.9635100260214233+0j)

# 1st argument means 0'th derivative (so psi(0, x) = psi(x))
sage: psi(0, .5)
psi(0.500000000000000)

sage: N(psi(0, .5))
-1.96351002602142
```




---

archive/issue_comments_057590.json:
```json
{
    "body": "Attachment [trac_6961-doctest.patch](tarball://root/attachments/some-uuid/ticket6961/trac_6961-doctest.patch) by mvngu created at 2010-02-18 04:00:05\n\nfix doctest failure",
    "created_at": "2010-02-18T04:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57590",
    "user": "mvngu"
}
```

Attachment [trac_6961-doctest.patch](tarball://root/attachments/some-uuid/ticket6961/trac_6961-doctest.patch) by mvngu created at 2010-02-18 04:00:05

fix doctest failure



---

archive/issue_comments_057591.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-18T04:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57591",
    "user": "mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_057592.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-18T04:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57592",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057593.json:
```json
{
    "body": "I applied patches in the following order against Sage 4.3.3.alpha0, together with the updated package [pynac-0.1.11.spkg](http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg):\n\n1. #6961: [trac_6961-psi.rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.rebased.patch)\n2. #7822: [trac_7822-py_log.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7822/trac_7822-py_log.take2.patch)\n3. #7876: [trac_7876-pynac_print.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7876/trac_7876-pynac_print.take2.patch)\n4. #7363\n5. #7957\n6. #7916: [trac_7916-same_name_method.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.take2.patch)\n7. #6465: \n   1. [trac_6465-chain_rule.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-chain_rule.take2.patch) \n   2. [trac_6465-moves-integration-into-sfunction-subclass.take3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-moves-integration-into-sfunction-subclass.take3.patch)\n   3. [trac_6465-integral.take4.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-integral.take4.patch)\n8. #6559: \n   1. [trac_6559-domain-and-latex_name-for-variable.take2.3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-domain-and-latex_name-for-variable.take2.3.patch) \n   2. [trac_6559-referee.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-referee.take2.patch)\n\nAll doctests passed except for this trivial failure:\n\n```\n[mvngu@sage sage-4.3.3.alpha0.1]$ ./sage -t -long devel/sage/sage/rings/arith.py\nsage -t -long \"devel/sage/sage/rings/arith.py\"              \n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/devel/sage/sage/rings/arith.py\", line 287:\n    sage: factorial(-32)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: factorial -- self = (-32) must be nonnegative\nGot:\n    Traceback (most recent call last):\n      File \"/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[10]>\", line 1, in <module>\n        factorial(-Integer(32))###line 287:\n    sage: factorial(-32)\n      File \"/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/lib/python/site-packages/sage/rings/arith.py\", line 315, in factorial\n        raise ValueError, \"factorial -- must be nonnegative\"\n    ValueError: factorial -- must be nonnegative\n**********************************************************************\n1 items had failures:\n   1 of  11 in __main__.example_3\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /dev/shm/mvngu/dot_sage/tmp/.doctest_arith.py\n\t [50.3 s]\n```\n\n\nThe failure is fixed via [trac_6961-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-doctest.patch), so only this latter patch needs some reviewing love. I'm happy with both #6465 and #6559. If my patch is OK, then these 8 tickets can be closed: #6961, #7822, #7876, #7363, #7957, #7916, #6465, #6559.",
    "created_at": "2010-02-18T04:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57593",
    "user": "mvngu"
}
```

I applied patches in the following order against Sage 4.3.3.alpha0, together with the updated package [pynac-0.1.11.spkg](http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg):

1. #6961: [trac_6961-psi.rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.rebased.patch)
2. #7822: [trac_7822-py_log.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7822/trac_7822-py_log.take2.patch)
3. #7876: [trac_7876-pynac_print.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7876/trac_7876-pynac_print.take2.patch)
4. #7363
5. #7957
6. #7916: [trac_7916-same_name_method.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.take2.patch)
7. #6465: 
   1. [trac_6465-chain_rule.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-chain_rule.take2.patch) 
   2. [trac_6465-moves-integration-into-sfunction-subclass.take3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-moves-integration-into-sfunction-subclass.take3.patch)
   3. [trac_6465-integral.take4.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-integral.take4.patch)
8. #6559: 
   1. [trac_6559-domain-and-latex_name-for-variable.take2.3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-domain-and-latex_name-for-variable.take2.3.patch) 
   2. [trac_6559-referee.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-referee.take2.patch)

All doctests passed except for this trivial failure:

```
[mvngu@sage sage-4.3.3.alpha0.1]$ ./sage -t -long devel/sage/sage/rings/arith.py
sage -t -long "devel/sage/sage/rings/arith.py"              
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/devel/sage/sage/rings/arith.py", line 287:
    sage: factorial(-32)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: factorial -- self = (-32) must be nonnegative
Got:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[10]>", line 1, in <module>
        factorial(-Integer(32))###line 287:
    sage: factorial(-32)
      File "/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/lib/python/site-packages/sage/rings/arith.py", line 315, in factorial
        raise ValueError, "factorial -- must be nonnegative"
    ValueError: factorial -- must be nonnegative
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /dev/shm/mvngu/dot_sage/tmp/.doctest_arith.py
	 [50.3 s]
```


The failure is fixed via [trac_6961-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-doctest.patch), so only this latter patch needs some reviewing love. I'm happy with both #6465 and #6559. If my patch is OK, then these 8 tickets can be closed: #6961, #7822, #7876, #7363, #7957, #7916, #6465, #6559.



---

archive/issue_comments_057594.json:
```json
{
    "body": "Hi Minh,\n\nYour patch looks ok to me. I'm switching this to positive review.\n\nIt's be truly awesome if all those tickets can get merged in this release. :)\n\nCheers,\n\nBurcin",
    "created_at": "2010-02-18T09:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57594",
    "user": "burcin"
}
```

Hi Minh,

Your patch looks ok to me. I'm switching this to positive review.

It's be truly awesome if all those tickets can get merged in this release. :)

Cheers,

Burcin



---

archive/issue_comments_057595.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-18T09:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57595",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-18T21:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57596",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057597.json:
```json
{
    "body": "Merged in this order:\n\n1. #6961: [trac_6961-psi.rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.rebased.patch)\n2. #7822\n3. #7876\n4. #7363\n5. #7957\n6. #7916\n7. #6465\n8. #6559\n9. #6961: [trac_6961-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-doctest.patch)",
    "created_at": "2010-02-18T21:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6961#issuecomment-57597",
    "user": "mvngu"
}
```

Merged in this order:

1. #6961: [trac_6961-psi.rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.rebased.patch)
2. #7822
3. #7876
4. #7363
5. #7957
6. #7916
7. #6465
8. #6559
9. #6961: [trac_6961-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-doctest.patch)
