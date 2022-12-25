# Issue 8054: roots(algorithm='numpy') does not work in arbitrary precision

archive/issues_008054.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @rbeezer\n\nConsider the following example:\n\n```\nsage: R.<x> = PolynomialRing(ComplexField(3322))\nsage: p=x^4+54*x^2+154\nsage: z=p.roots(algorithm='pari')\nsage: e=p-mul([x-z[i][0] for i in range(4)])\nsage: n(max(abs(e.coeffs()[i]) for i in range(0,e.degree()+1)))\n6.08883742371831e-999\n```\n\nThis is ok. Compare now with:\n\n```\nsage: R.<x> = PolynomialRing(ComplexField(3322))\nsage: p=x^4+54*x^2+154\nsage: z=p.roots(algorithm='numpy')\nsage: e=p-mul([x-z[i][0] for i in range(4)])\nsage: n(max(abs(e.coeffs()[i]) for i in range(0,e.degree()+1)))\n6.06533797844328e-14\n```\n\nClearly the precision given by numpy is only 14 digits, not 1000\ndigits as expected.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8054\n\n",
    "created_at": "2010-01-25T12:08:01Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "roots(algorithm='numpy') does not work in arbitrary precision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8054",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: jkantor

CC:  @rbeezer

Consider the following example:

```
sage: R.<x> = PolynomialRing(ComplexField(3322))
sage: p=x^4+54*x^2+154
sage: z=p.roots(algorithm='pari')
sage: e=p-mul([x-z[i][0] for i in range(4)])
sage: n(max(abs(e.coeffs()[i]) for i in range(0,e.degree()+1)))
6.08883742371831e-999
```

This is ok. Compare now with:

```
sage: R.<x> = PolynomialRing(ComplexField(3322))
sage: p=x^4+54*x^2+154
sage: z=p.roots(algorithm='numpy')
sage: e=p-mul([x-z[i][0] for i in range(4)])
sage: n(max(abs(e.coeffs()[i]) for i in range(0,e.degree()+1)))
6.06533797844328e-14
```

Clearly the precision given by numpy is only 14 digits, not 1000
digits as expected.

Issue created by migration from https://trac.sagemath.org/ticket/8054





---

archive/issue_comments_070332.json:
```json
{
    "body": "Numpy does not do arbitrary precision things.  So I suppose we should just document this.",
    "created_at": "2010-01-25T13:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70332",
    "user": "https://github.com/jasongrout"
}
```

Numpy does not do arbitrary precision things.  So I suppose we should just document this.



---

archive/issue_comments_070333.json:
```json
{
    "body": "> Numpy does not do arbitrary precision things. So I suppose we should just document this. \n\nstill not done in 4.3.1.",
    "created_at": "2010-02-05T20:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70333",
    "user": "https://github.com/zimmermann6"
}
```

> Numpy does not do arbitrary precision things. So I suppose we should just document this. 

still not done in 4.3.1.



---

archive/issue_comments_070334.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-26T19:02:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70334",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070335.json:
```json
{
    "body": "Attachment [trac_8054.patch](tarball://root/attachments/some-uuid/ticket8054/trac_8054.patch) by @mwhansen created at 2010-08-26 19:02:59",
    "created_at": "2010-08-26T19:02:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70335",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_8054.patch](tarball://root/attachments/some-uuid/ticket8054/trac_8054.patch) by @mwhansen created at 2010-08-26 19:02:59



---

archive/issue_comments_070336.json:
```json
{
    "body": "Mike, the warning message is just printed once, i.e., if one calls roots(algorithm='numpy') twice,\nit is not printed the second time. Is it wanted?\n\nPaul",
    "created_at": "2010-08-30T13:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70336",
    "user": "https://github.com/zimmermann6"
}
```

Mike, the warning message is just printed once, i.e., if one calls roots(algorithm='numpy') twice,
it is not printed the second time. Is it wanted?

Paul



---

archive/issue_comments_070337.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-30T14:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70337",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070338.json:
```json
{
    "body": "All test pass (with Sage 4.4.4). Thus I give a positive review.",
    "created_at": "2010-08-30T14:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70338",
    "user": "https://github.com/zimmermann6"
}
```

All test pass (with Sage 4.4.4). Thus I give a positive review.



---

archive/issue_comments_070339.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-18T07:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70339",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_070340.json:
```json
{
    "body": "Could someone rebase the patch against 4.6.alpha1 when it's released (soon) and restore the positive review?",
    "created_at": "2010-09-18T07:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70340",
    "user": "https://github.com/qed777"
}
```

Could someone rebase the patch against 4.6.alpha1 when it's released (soon) and restore the positive review?



---

archive/issue_comments_070341.json:
```json
{
    "body": "If someone is rebasing it, they might also correct a typo:\n\nNote that one should not use NumPy when wanting high precicion -> precision",
    "created_at": "2010-09-18T12:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70341",
    "user": "https://github.com/jasongrout"
}
```

If someone is rebasing it, they might also correct a typo:

Note that one should not use NumPy when wanting high precicion -> precision



---

archive/issue_comments_070342.json:
```json
{
    "body": "by the way, is there a documentation somewhere explaining how to rebase a patch?\n\nPaul",
    "created_at": "2010-09-18T19:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70342",
    "user": "https://github.com/zimmermann6"
}
```

by the way, is there a documentation somewhere explaining how to rebase a patch?

Paul



---

archive/issue_comments_070343.json:
```json
{
    "body": "Replying to [comment:8 zimmerma]:\n> by the way, is there a documentation somewhere explaining how to rebase a patch?\n\nOne way is to use [Mercurial queues](http://wiki.sagemath.org/MercurialQueues):\n\n```sh\n$ cd SAGE_ROOT/devel/sage\n$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8054/trac_8054.patch\nadding trac_8054.patch to series file\n$ hg qpush\napplying trac_8054.patch\npatching file sage/rings/polynomial/polynomial_element.pyx\nHunk #2 FAILED at 4256\n1 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8054.patch\n```\n\nThe file `polynomial_element.pyx.rej` is a diff of the changes that Mercurial was unable to apply.  Editing `polynomial_element.pyx` by hand to incorporate the leftover changes and then doing\n\n```sh\n$ hg qrefresh\n$ hg export qtip > /path/to/trac_8054.2.patch\n$ hg qpop\n$ hg qdelete trac_8054.patch\n```\n\nshould write out an updated patch and restore the original state of the repository.  If you choose not to delete the patch from the queue, e.g., for doctesting, then for convenience you can use\n\n```sh\n$ hg qrename trac_8054.2.patch\n```\n\nto rename it in the queue.  After this, `hg qseries`, `hg qapplied`, and `hg qunapplied` will use the updated name (until you `qdelete` the patch).\n\nThere's more on using queues in the [Developer's Guide](http://www.sagemath.org/doc/developer/walk_through.html#being-more-efficient-mercurial-queues), but as far as I can tell, there's no mention of rebasing patches.  Let us know if you have questions.",
    "created_at": "2010-09-18T22:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70343",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:8 zimmerma]:
> by the way, is there a documentation somewhere explaining how to rebase a patch?

One way is to use [Mercurial queues](http://wiki.sagemath.org/MercurialQueues):

```sh
$ cd SAGE_ROOT/devel/sage
$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8054/trac_8054.patch
adding trac_8054.patch to series file
$ hg qpush
applying trac_8054.patch
patching file sage/rings/polynomial/polynomial_element.pyx
Hunk #2 FAILED at 4256
1 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8054.patch
```

The file `polynomial_element.pyx.rej` is a diff of the changes that Mercurial was unable to apply.  Editing `polynomial_element.pyx` by hand to incorporate the leftover changes and then doing

```sh
$ hg qrefresh
$ hg export qtip > /path/to/trac_8054.2.patch
$ hg qpop
$ hg qdelete trac_8054.patch
```

should write out an updated patch and restore the original state of the repository.  If you choose not to delete the patch from the queue, e.g., for doctesting, then for convenience you can use

```sh
$ hg qrename trac_8054.2.patch
```

to rename it in the queue.  After this, `hg qseries`, `hg qapplied`, and `hg qunapplied` will use the updated name (until you `qdelete` the patch).

There's more on using queues in the [Developer's Guide](http://www.sagemath.org/doc/developer/walk_through.html#being-more-efficient-mercurial-queues), but as far as I can tell, there's no mention of rebasing patches.  Let us know if you have questions.



---

archive/issue_comments_070344.json:
```json
{
    "body": "Replying to [comment:9 mpatel]:\n\nthank you. I will try when 4.6.alpha1 is available. Do you know when?\n\nPaul",
    "created_at": "2010-09-19T08:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70344",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:9 mpatel]:

thank you. I will try when 4.6.alpha1 is available. Do you know when?

Paul



---

archive/issue_comments_070345.json:
```json
{
    "body": "Replying to [comment:10 zimmerma]:\n> Replying to [comment:9 mpatel]:\n> thank you. I will try when 4.6.alpha1 is available. Do you know when?\n\nNo problem.  I hope I haven't made any mistakes!\n\nI very recently [announced 4.6.alpha1 on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/1a01378099b9d5e).\n\nI've cc'd Rob Beezer about [comment:8 rebasing patches].",
    "created_at": "2010-09-19T08:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70345",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:10 zimmerma]:
> Replying to [comment:9 mpatel]:
> thank you. I will try when 4.6.alpha1 is available. Do you know when?

No problem.  I hope I haven't made any mistakes!

I very recently [announced 4.6.alpha1 on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/1a01378099b9d5e).

I've cc'd Rob Beezer about [comment:8 rebasing patches].



---

archive/issue_comments_070346.json:
```json
{
    "body": "Attachment [trac_8054.2.patch](tarball://root/attachments/some-uuid/ticket8054/trac_8054.2.patch) by @zimmermann6 created at 2010-09-19 18:56:36\n\noriginal patch rebased on 4.6.alpha1",
    "created_at": "2010-09-19T18:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70346",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_8054.2.patch](tarball://root/attachments/some-uuid/ticket8054/trac_8054.2.patch) by @zimmermann6 created at 2010-09-19 18:56:36

original patch rebased on 4.6.alpha1



---

archive/issue_comments_070347.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-19T18:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70347",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_070348.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> Could someone rebase the patch against 4.6.alpha1 when it's released (soon) and restore the positive review? \n\ndone.\n\nPaul",
    "created_at": "2010-09-19T18:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70348",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:6 mpatel]:
> Could someone rebase the patch against 4.6.alpha1 when it's released (soon) and restore the positive review? 

done.

Paul



---

archive/issue_comments_070349.json:
```json
{
    "body": "I'll try to send Paul some rebase instructions that he might look over and then and maybe grow those into something for the Developer's Guide.\n\nRob",
    "created_at": "2010-09-19T19:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70349",
    "user": "https://github.com/rbeezer"
}
```

I'll try to send Paul some rebase instructions that he might look over and then and maybe grow those into something for the Developer's Guide.

Rob



---

archive/issue_comments_070350.json:
```json
{
    "body": "The rebased patch applies cleanly to 4.6.alpha1.  But testing just the changed file, I get\n\n```\nsage -t -long \"devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\"\n**********************************************************************\nError: TAB character found.\n\n         [13.2 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\"\nTotal time for all tests: 13.2 seconds\n```\n\nThere's a stray tab in this line\n\n```diff\n+       ``algorithm='numpy'`` with high-precision types.)                       \n```\n\n(in the patch).",
    "created_at": "2010-09-19T21:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70350",
    "user": "https://github.com/qed777"
}
```

The rebased patch applies cleanly to 4.6.alpha1.  But testing just the changed file, I get

```
sage -t -long "devel/sage-main/sage/rings/polynomial/polynomial_element.pyx"
**********************************************************************
Error: TAB character found.

         [13.2 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-main/sage/rings/polynomial/polynomial_element.pyx"
Total time for all tests: 13.2 seconds
```

There's a stray tab in this line

```diff
+       ``algorithm='numpy'`` with high-precision types.)                       
```

(in the patch).



---

archive/issue_comments_070351.json:
```json
{
    "body": "Replying to [comment:13 rbeezer]:\n> I'll try to send Paul some rebase instructions that he might look over and then and maybe grow those into something for the Developer's Guide.\n\nThanks, Rob.  I wasn't sure whether this is in the Guide.  I should reread it in full, soon.",
    "created_at": "2010-09-19T21:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70351",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:13 rbeezer]:
> I'll try to send Paul some rebase instructions that he might look over and then and maybe grow those into something for the Developer's Guide.

Thanks, Rob.  I wasn't sure whether this is in the Guide.  I should reread it in full, soon.



---

archive/issue_comments_070352.json:
```json
{
    "body": "Attachment [trac_8054.3.patch](tarball://root/attachments/some-uuid/ticket8054/trac_8054.3.patch) by @zimmermann6 created at 2010-09-20 07:47:48",
    "created_at": "2010-09-20T07:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70352",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_8054.3.patch](tarball://root/attachments/some-uuid/ticket8054/trac_8054.3.patch) by @zimmermann6 created at 2010-09-20 07:47:48



---

archive/issue_comments_070353.json:
```json
{
    "body": "sorry, I've replaced the tab. Apply only the last patch.\n\nPaul",
    "created_at": "2010-09-20T07:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70353",
    "user": "https://github.com/zimmermann6"
}
```

sorry, I've replaced the tab. Apply only the last patch.

Paul



---

archive/issue_comments_070354.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70354",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_008263.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-28T09:11:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8054#event-8263"
}
```



---

archive/issue_comments_070355.json:
```json
{
    "body": "Replying to [comment:9 mpatel]:\n> Replying to [comment:8 zimmerma]:\n> > by the way, is there a documentation somewhere explaining how to rebase a patch?\n> \n> One way is to use [Mercurial queues](http://wiki.sagemath.org/MercurialQueues):\n\nAnother possible way:\n\n```sh\n$ hg import --no-commit filename.patch\n```\n\nwhich just updates the working directory.  Then you can check the .rej file, make changes, re-commit, and export anew.",
    "created_at": "2010-10-04T22:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8054#issuecomment-70355",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:9 mpatel]:
> Replying to [comment:8 zimmerma]:
> > by the way, is there a documentation somewhere explaining how to rebase a patch?
> 
> One way is to use [Mercurial queues](http://wiki.sagemath.org/MercurialQueues):

Another possible way:

```sh
$ hg import --no-commit filename.patch
```

which just updates the working directory.  Then you can check the .rej file, make changes, re-commit, and export anew.
