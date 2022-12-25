# Issue 7473: Sphinx hangs when making a clone

archive/issues_007473.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri @nthiery @nathanncohen\n\nThis is a follow-up to #6187.\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/433ec95cba086551/f4286b67d64a19dd?#f4286b67d64a19dd), [sage-release](http://groups.google.com/group/sage-release/msg/76c956312e4de13d), [#sage-devel log](http://sage.math.washington.edu/home/mpatel/projects/irclogs/logs/sage-devel-2009-10-26.log.html#t21:56).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7473\n\n",
    "created_at": "2009-11-16T10:20:23Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Sphinx hangs when making a clone",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7473",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  @jhpalmieri @nthiery @nathanncohen

This is a follow-up to #6187.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/433ec95cba086551/f4286b67d64a19dd?#f4286b67d64a19dd), [sage-release](http://groups.google.com/group/sage-release/msg/76c956312e4de13d), [#sage-devel log](http://sage.math.washington.edu/home/mpatel/projects/irclogs/logs/sage-devel-2009-10-26.log.html#t21:56).

Issue created by migration from https://trac.sagemath.org/ticket/7473





---

archive/issue_comments_062845.json:
```json
{
    "body": "What if we run `hg clone`, then `cp -pr` just the files Sphinx checks?",
    "created_at": "2009-11-18T21:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62845",
    "user": "https://github.com/qed777"
}
```

What if we run `hg clone`, then `cp -pr` just the files Sphinx checks?



---

archive/issue_comments_062846.json:
```json
{
    "body": "What if we capture `stderr` and `stdin`, too, in\n\n```python\n    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)\n```\n\n?  Or do the opposite?  For example, `builder.py` issues `subprocess.call(build_command, shell=True)`, which is shorthand for `subprocess.Popen(build_command, shell=True).wait()`.   But this may not be relevant.\n\nI'll try to take a closer look soon.",
    "created_at": "2009-11-18T22:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62846",
    "user": "https://github.com/qed777"
}
```

What if we capture `stderr` and `stdin`, too, in

```python
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
```

?  Or do the opposite?  For example, `builder.py` issues `subprocess.call(build_command, shell=True)`, which is shorthand for `subprocess.Popen(build_command, shell=True).wait()`.   But this may not be relevant.

I'll try to take a closer look soon.



---

archive/issue_comments_062847.json:
```json
{
    "body": "I've noticed that switching among *existing branches* via `sage -b`, even if I've changed no files, can touch or byte-compile files in `SAGE_LOCAL/lib/python/site-packages/sage`.  Sphinx notices the changed dependencies and rebuilds the manual.",
    "created_at": "2009-11-19T23:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62847",
    "user": "https://github.com/qed777"
}
```

I've noticed that switching among *existing branches* via `sage -b`, even if I've changed no files, can touch or byte-compile files in `SAGE_LOCAL/lib/python/site-packages/sage`.  Sphinx notices the changed dependencies and rebuilds the manual.



---

archive/issue_comments_062848.json:
```json
{
    "body": "It strange that\n\n```sh\ncd SAGE_ROOT/devel\nls -lsFi `find -name environment.pickle`|grep ref\n```\n\nshows the clones to have different Sphinx pickles --- their inodes (the first column on sage.math) are distinct.  Compare with\n\n```sh\nls -lsFi `find -name steenrod_algebra.html`\nls -lsFi `find -name steenrod_algebra.py`|grep -v build\n```\n\nBut aren't the pickles hard linked?",
    "created_at": "2009-11-20T00:02:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62848",
    "user": "https://github.com/qed777"
}
```

It strange that

```sh
cd SAGE_ROOT/devel
ls -lsFi `find -name environment.pickle`|grep ref
```

shows the clones to have different Sphinx pickles --- their inodes (the first column on sage.math) are distinct.  Compare with

```sh
ls -lsFi `find -name steenrod_algebra.html`
ls -lsFi `find -name steenrod_algebra.py`|grep -v build
```

But aren't the pickles hard linked?



---

archive/issue_comments_062849.json:
```json
{
    "body": "I think this happens because `sphinx.environment.BuildEnvironment.topickle` first dumps the environment to a temporary file, then moves it `environment.pickle`.",
    "created_at": "2009-11-20T00:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62849",
    "user": "https://github.com/qed777"
}
```

I think this happens because `sphinx.environment.BuildEnvironment.topickle` first dumps the environment to a temporary file, then moves it `environment.pickle`.



---

archive/issue_comments_062850.json:
```json
{
    "body": "Attachment [trac_7473-sage_builder.patch](tarball://root/attachments/some-uuid/ticket7473/trac_7473-sage_builder.patch) by @qed777 created at 2009-11-20 14:17:49\n\nMake pickle saving preserve the hard link.  Apply to sage repo.",
    "created_at": "2009-11-20T14:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62850",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7473-sage_builder.patch](tarball://root/attachments/some-uuid/ticket7473/trac_7473-sage_builder.patch) by @qed777 created at 2009-11-20 14:17:49

Make pickle saving preserve the hard link.  Apply to sage repo.



---

archive/issue_comments_062851.json:
```json
{
    "body": "Don't capture Sphinx clone output.  This *may* prevent the hang.  Apply to scripts repo.",
    "created_at": "2009-11-20T14:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62851",
    "user": "https://github.com/qed777"
}
```

Don't capture Sphinx clone output.  This *may* prevent the hang.  Apply to scripts repo.



---

archive/issue_comments_062852.json:
```json
{
    "body": "Attachment [trac_7473-scripts_clone.patch](tarball://root/attachments/some-uuid/ticket7473/trac_7473-scripts_clone.patch) by @qed777 created at 2009-11-20 14:29:39\n\nI *think* the [attachment:trac_7473-scripts_clone.patch attached patch] for the scripts repository prevents the hang when cloning.  The [attachment:trac_7473-sage_builder.patch sage repository patch] should ensure that we usually keep just one copy of the reference manual's `environment.pickle`.\n\nBut I'm still not sure about how to avoid rebuilding nearly all of the manual when cloning or after trivially switching branches.  The latter may be a separate problem.",
    "created_at": "2009-11-20T14:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62852",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7473-scripts_clone.patch](tarball://root/attachments/some-uuid/ticket7473/trac_7473-scripts_clone.patch) by @qed777 created at 2009-11-20 14:29:39

I *think* the [attachment:trac_7473-scripts_clone.patch attached patch] for the scripts repository prevents the hang when cloning.  The [attachment:trac_7473-sage_builder.patch sage repository patch] should ensure that we usually keep just one copy of the reference manual's `environment.pickle`.

But I'm still not sure about how to avoid rebuilding nearly all of the manual when cloning or after trivially switching branches.  The latter may be a separate problem.



---

archive/issue_comments_062853.json:
```json
{
    "body": "Attachment [trac_7473-scripts_clone_v2.patch](tarball://root/attachments/some-uuid/ticket7473/trac_7473-scripts_clone_v2.patch) by @qed777 created at 2009-11-22 18:57:53\n\nUse `cp -pr` to preserve .rst file times.  This may work.  Apply only this patch to scripts repo.",
    "created_at": "2009-11-22T18:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62853",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7473-scripts_clone_v2.patch](tarball://root/attachments/some-uuid/ticket7473/trac_7473-scripts_clone_v2.patch) by @qed777 created at 2009-11-22 18:57:53

Use `cp -pr` to preserve .rst file times.  This may work.  Apply only this patch to scripts repo.



---

archive/issue_comments_062854.json:
```json
{
    "body": "Version 2 of the scripts repo (i.e., `sage-clone`) patch uses `cp -pr` instead of [shutil.copytree](http://docs.python.org/library/shutil.html#shutil.copytree) to copy the auto-generated .rst files.  Could someone please test this and the sage repo patch?  It appears to prevent the hang and unnecessary rebuilds of the reference manual on sage.math.\n\nAccording to its documentation, `shutil.copytree` is very similar to `cp -pr`.  But their results aren't identical, it seems.\n\nI don't know if `cp -pr` is cross-platform.",
    "created_at": "2009-11-22T19:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62854",
    "user": "https://github.com/qed777"
}
```

Version 2 of the scripts repo (i.e., `sage-clone`) patch uses `cp -pr` instead of [shutil.copytree](http://docs.python.org/library/shutil.html#shutil.copytree) to copy the auto-generated .rst files.  Could someone please test this and the sage repo patch?  It appears to prevent the hang and unnecessary rebuilds of the reference manual on sage.math.

According to its documentation, `shutil.copytree` is very similar to `cp -pr`.  But their results aren't identical, it seems.

I don't know if `cp -pr` is cross-platform.



---

archive/issue_comments_062855.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-22T19:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62855",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062856.json:
```json
{
    "body": "#7407 provides the following link, saying that it describes the only options to \"cp\" which should be used:\n\n[http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html](http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html)\n\nReading this, I wonder if we should use \"cp -pR\" instead of \"cp -pr\".\n\nI made a new clone, applied the patch, built the documentation, and then made another clone.  The new cloning process took 2-3 minutes on my iMac running OS X 10.6, and when done the documentation did not need to be rebuilt again.  On sage.math, the same thing happened, with the cloning process taking about the same amount of time.  In both cases, updating the modification times was quick.  Also in both cases, using \"cp -pR\" worked just as well as \"cp -pr\".\n\nShall we take the cited web page as enough evidence that this is cross-platform?  And should we change \"r\" to \"R\"?",
    "created_at": "2009-11-22T20:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62856",
    "user": "https://github.com/jhpalmieri"
}
```

#7407 provides the following link, saying that it describes the only options to "cp" which should be used:

[http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html](http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html)

Reading this, I wonder if we should use "cp -pR" instead of "cp -pr".

I made a new clone, applied the patch, built the documentation, and then made another clone.  The new cloning process took 2-3 minutes on my iMac running OS X 10.6, and when done the documentation did not need to be rebuilt again.  On sage.math, the same thing happened, with the cloning process taking about the same amount of time.  In both cases, updating the modification times was quick.  Also in both cases, using "cp -pR" worked just as well as "cp -pr".

Shall we take the cited web page as enough evidence that this is cross-platform?  And should we change "r" to "R"?



---

archive/issue_comments_062857.json:
```json
{
    "body": "Attachment [trac_7473-scripts_clone_v3.patch](tarball://root/attachments/some-uuid/ticket7473/trac_7473-scripts_clone_v3.patch) by @qed777 created at 2009-11-23 21:36:50\n\nUse cp -pR for auto-generated .rst files.  Apply only this patch to the scripts repo.",
    "created_at": "2009-11-23T21:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62857",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7473-scripts_clone_v3.patch](tarball://root/attachments/some-uuid/ticket7473/trac_7473-scripts_clone_v3.patch) by @qed777 created at 2009-11-23 21:36:50

Use cp -pR for auto-generated .rst files.  Apply only this patch to the scripts repo.



---

archive/issue_comments_062858.json:
```json
{
    "body": "Version 3 uses `cp -pR` instead of `cp -pr`.  Does the Windows build environment support `cp -pR`?",
    "created_at": "2009-11-23T21:47:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62858",
    "user": "https://github.com/qed777"
}
```

Version 3 uses `cp -pR` instead of `cp -pr`.  Does the Windows build environment support `cp -pR`?



---

archive/issue_comments_062859.json:
```json
{
    "body": "nthiery, ncohen:  If you have a chance, could you let us know if the patches above work?  In particular,\n\n* Apply [attachment:trac_7473-sage_builder.patch] to the sage repository.\n* Apply [attachment:trac_7473-scripts_clone_v3.patch] to the scripts repository.\n\nIf this is yet another false positive, I apologize.",
    "created_at": "2009-11-23T21:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62859",
    "user": "https://github.com/qed777"
}
```

nthiery, ncohen:  If you have a chance, could you let us know if the patches above work?  In particular,

* Apply [attachment:trac_7473-sage_builder.patch] to the sage repository.
* Apply [attachment:trac_7473-scripts_clone_v3.patch] to the scripts repository.

If this is yet another false positive, I apologize.



---

archive/issue_comments_062860.json:
```json
{
    "body": "I'm happy with it (Mac OS X 10.6 and sage.math).\n\nOn what other platforms does it need to be tested?",
    "created_at": "2009-11-23T23:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62860",
    "user": "https://github.com/jhpalmieri"
}
```

I'm happy with it (Mac OS X 10.6 and sage.math).

On what other platforms does it need to be tested?



---

archive/issue_comments_062861.json:
```json
{
    "body": "I tried it on my Fedora ( built from sources ) and it applies fine and does its job ( I'm not stuck anymore when cloning ) !\n\n( Even though I can not control your script as I have no idea of how Sage works at this level... ) :-)\n\nThank you for your patch !!!\n\nNathann",
    "created_at": "2009-11-24T07:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62861",
    "user": "https://github.com/nathanncohen"
}
```

I tried it on my Fedora ( built from sources ) and it applies fine and does its job ( I'm not stuck anymore when cloning ) !

( Even though I can not control your script as I have no idea of how Sage works at this level... ) :-)

Thank you for your patch !!!

Nathann



---

archive/issue_comments_062862.json:
```json
{
    "body": "Replying to [comment:11 mpatel]:\n> nthiery, ncohen:  If you have a chance, could you let us know if the patches above work?  In particular,\n> \n>  * Apply [attachment:trac_7473-sage_builder.patch] to the sage repository.\n>  * Apply [attachment:trac_7473-scripts_clone_v3.patch] to the scripts repository.\n> \n> If this is yet another false positive, I apologize.\n\nI tried sage -combinat install (which calls clone), and it worked smoothly (ubuntu 9.4, sage 4.2.1, macbook pro)!\n\nThanks!",
    "created_at": "2009-11-24T12:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62862",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:11 mpatel]:
> nthiery, ncohen:  If you have a chance, could you let us know if the patches above work?  In particular,
> 
>  * Apply [attachment:trac_7473-sage_builder.patch] to the sage repository.
>  * Apply [attachment:trac_7473-scripts_clone_v3.patch] to the scripts repository.
> 
> If this is yet another false positive, I apologize.

I tried sage -combinat install (which calls clone), and it worked smoothly (ubuntu 9.4, sage 4.2.1, macbook pro)!

Thanks!



---

archive/issue_comments_062863.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-26T06:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62863",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062864.json:
```json
{
    "body": "On the grounds that this is an improvement on some systems and I hope isn't any worse on any systems, I'm giving this a positive review.  I really would like this to be merged, because cloning is so painful right now.",
    "created_at": "2009-11-26T06:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62864",
    "user": "https://github.com/jhpalmieri"
}
```

On the grounds that this is an improvement on some systems and I hope isn't any worse on any systems, I'm giving this a positive review.  I really would like this to be merged, because cloning is so painful right now.



---

archive/issue_comments_062865.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62865",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_062866.json:
```json
{
    "body": "It seems that the [attachment:trac_7473-sage_builder.patch sage repo patch] didn't make it into 4.3.alpha1.  This patch will prevent some unnecessary doc rebuilds when changing branches.",
    "created_at": "2009-12-04T07:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62866",
    "user": "https://github.com/qed777"
}
```

It seems that the [attachment:trac_7473-sage_builder.patch sage repo patch] didn't make it into 4.3.alpha1.  This patch will prevent some unnecessary doc rebuilds when changing branches.



---

archive/issue_comments_062867.json:
```json
{
    "body": "Oops, I must only seen the last patch.  I'll add it first thing to the next release.",
    "created_at": "2009-12-04T08:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62867",
    "user": "https://github.com/mwhansen"
}
```

Oops, I must only seen the last patch.  I'll add it first thing to the next release.



---

archive/issue_comments_062868.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-12-04T08:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62868",
    "user": "https://github.com/mwhansen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_062869.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2009-12-04T08:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62869",
    "user": "https://github.com/mwhansen"
}
```

Changing status from closed to new.



---

archive/issue_comments_062870.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-04T08:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62870",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062871.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-04T08:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62871",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062872.json:
```json
{
    "body": "Thanks!",
    "created_at": "2009-12-04T08:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62872",
    "user": "https://github.com/qed777"
}
```

Thanks!



---

archive/issue_comments_062873.json:
```json
{
    "body": "Merged trac_7473-sage_builder.patch in 4.3.rc0.",
    "created_at": "2009-12-06T08:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62873",
    "user": "https://github.com/mwhansen"
}
```

Merged trac_7473-sage_builder.patch in 4.3.rc0.



---

archive/issue_comments_062874.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-06T08:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7473#issuecomment-62874",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
