# Issue 9501: Make an @fork decorator

archive/issues_009501.json:
```json
{
    "body": "Assignee: jason\n\nCC:  mvngu\n\nSimon King mentioned that sometimes his code crashes/leaks/etc.  So make it so one can do:\n\n```\n@fork\ndef f(x,y,z,...):\n    ...\n```\n\nand then f gets computed in a blocking forked process, and the result is returned via pickling. This is 100% to thwart mem leaks, segfaults, and guaranteed timeout possibility.   This could be basically just a light wrapper around `@`parallel(1).  Also, make a global flag to turn this off, so `@`fork does nothing.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9501\n\n",
    "created_at": "2010-07-14T22:32:17Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "title": "Make an @fork decorator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9501",
    "user": "was"
}
```
Assignee: jason

CC:  mvngu

Simon King mentioned that sometimes his code crashes/leaks/etc.  So make it so one can do:

```
@fork
def f(x,y,z,...):
    ...
```

and then f gets computed in a blocking forked process, and the result is returned via pickling. This is 100% to thwart mem leaks, segfaults, and guaranteed timeout possibility.   This could be basically just a light wrapper around `@`parallel(1).  Also, make a global flag to turn this off, so `@`fork does nothing.

Issue created by migration from https://trac.sagemath.org/ticket/9501





---

archive/issue_comments_091235.json:
```json
{
    "body": "Keep in mind #8410, though this doesn't depend on that.\n\nSee http://sagenb.org/home/pub/2248/ for a demo.",
    "created_at": "2010-07-14T23:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91235",
    "user": "was"
}
```

Keep in mind #8410, though this doesn't depend on that.

See http://sagenb.org/home/pub/2248/ for a demo.



---

archive/issue_comments_091236.json:
```json
{
    "body": "The code is a little longer than necessary, since:\n\n\n* I improved the documentation and doctesting to get coverage to 100% (it wasn't really before).\n\n* I implemented an option to not kill the interfaces, but it's not used.  It could be useful for some users.",
    "created_at": "2010-07-15T18:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91236",
    "user": "was"
}
```

The code is a little longer than necessary, since:


* I improved the documentation and doctesting to get coverage to 100% (it wasn't really before).

* I implemented an option to not kill the interfaces, but it's not used.  It could be useful for some users.



---

archive/issue_comments_091237.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-15T18:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91237",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091238.json:
```json
{
    "body": "\n```\nFile \"/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/parallel/decorate.py\", line 292:\n\n    sage: g()\n\nExpected:\n\n    '10'\n\nGot:\n\n    [Errno 16] Device or resource busy: '/home/malb/.sage/temp/sage.math.washington.edu/29514/dir_0/.nfs000000000482d3cd00028d9f'\n\n    '10'\n\n**********************************************************************\n\nFile \"/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/parallel/decorate.py\", line 303:\n\n    sage: g()\n\nExpected:\n\n    'a'\n\nGot:\n\n    [Errno 16] Device or resource busy: '/home/malb/.sage/temp/sage.math.washington.edu/29514/dir_1/.nfs000000000482d3d300028da0'\n\n    'a'\n\n\n```\n",
    "created_at": "2010-07-15T18:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91238",
    "user": "malb"
}
```


```
File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/parallel/decorate.py", line 292:

    sage: g()

Expected:

    '10'

Got:

    [Errno 16] Device or resource busy: '/home/malb/.sage/temp/sage.math.washington.edu/29514/dir_0/.nfs000000000482d3cd00028d9f'

    '10'

**********************************************************************

File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/parallel/decorate.py", line 303:

    sage: g()

Expected:

    'a'

Got:

    [Errno 16] Device or resource busy: '/home/malb/.sage/temp/sage.math.washington.edu/29514/dir_1/.nfs000000000482d3d300028da0'

    'a'


```




---

archive/issue_comments_091239.json:
```json
{
    "body": "* the timeout documentation should mention that 0 means Infinity\n  * the fork decorator talks about parallel subprocesses (copy 'n' paste oversight)\n  * I don't know whether the above failures are a real issue or not\n\nIf these are addressed I'm happy to give this a positive review.",
    "created_at": "2010-07-15T18:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91239",
    "user": "malb"
}
```

* the timeout documentation should mention that 0 means Infinity
  * the fork decorator talks about parallel subprocesses (copy 'n' paste oversight)
  * I don't know whether the above failures are a real issue or not

If these are addressed I'm happy to give this a positive review.



---

archive/issue_comments_091240.json:
```json
{
    "body": "William and I discussed the doctest failure and tried it again: we couldn't reproduce it so we assume it's okay for now, the machine (disk?) was just quite busy.",
    "created_at": "2010-07-15T19:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91240",
    "user": "malb"
}
```

William and I discussed the doctest failure and tried it again: we couldn't reproduce it so we assume it's okay for now, the machine (disk?) was just quite busy.



---

archive/issue_comments_091241.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-15T19:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91241",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091242.json:
```json
{
    "body": "William, you just mentioned that you have not added a doctest illustrating that a segmentation fault is no disaster when one uses the fork decorator. But in the worksheet you link at, there is a segfaulting example. So, why not add such thing as a doctest?",
    "created_at": "2010-07-15T19:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91242",
    "user": "SimonKing"
}
```

William, you just mentioned that you have not added a doctest illustrating that a segmentation fault is no disaster when one uses the fork decorator. But in the worksheet you link at, there is a segfaulting example. So, why not add such thing as a doctest?



---

archive/issue_comments_091243.json:
```json
{
    "body": "SimonKing -- that's a good idea.  I've refreshed the patch with this example.",
    "created_at": "2010-07-15T23:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91243",
    "user": "was"
}
```

SimonKing -- that's a good idea.  I've refreshed the patch with this example.



---

archive/issue_comments_091244.json:
```json
{
    "body": "Attachment [trac_9501.patch](tarball://root/attachments/some-uuid/ticket9501/trac_9501.patch) by was created at 2010-07-15 23:54:12",
    "created_at": "2010-07-15T23:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91244",
    "user": "was"
}
```

Attachment [trac_9501.patch](tarball://root/attachments/some-uuid/ticket9501/trac_9501.patch) by was created at 2010-07-15 23:54:12



---

archive/issue_comments_091245.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-15T23:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91245",
    "user": "was"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091246.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-15T23:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91246",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091247.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-16T08:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91247",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091248.json:
```json
{
    "body": "Patch looks good, tests passed.",
    "created_at": "2010-07-16T08:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91248",
    "user": "malb"
}
```

Patch looks good, tests passed.



---

archive/issue_comments_091249.json:
```json
{
    "body": "I think the 'warning' sections need to be in proper REsT format, which I *think* (but won't guarantee) should look more like\n\n```\n.. warning::\n```\n\nor something like that.  I'm cc:ing mvngu since he will know :)",
    "created_at": "2010-07-16T14:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91249",
    "user": "kcrisman"
}
```

I think the 'warning' sections need to be in proper REsT format, which I *think* (but won't guarantee) should look more like

```
.. warning::
```

or something like that.  I'm cc:ing mvngu since he will know :)



---

archive/issue_comments_091250.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-16T14:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91250",
    "user": "kcrisman"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091251.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> I think the 'warning' sections need to be in proper REsT format, which I *think* (but won't guarantee) should look more like\n\n```\n.. warning::\n```\n\n> or something like that.\n\nThat's right. See [this section](http://sphinx.pocoo.org/markup/para.html#dir-warning) of the Sphinx reference manual.",
    "created_at": "2010-07-17T02:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91251",
    "user": "mvngu"
}
```

Replying to [comment:12 kcrisman]:
> I think the 'warning' sections need to be in proper REsT format, which I *think* (but won't guarantee) should look more like

```
.. warning::
```

> or something like that.

That's right. See [this section](http://sphinx.pocoo.org/markup/para.html#dir-warning) of the Sphinx reference manual.



---

archive/issue_comments_091252.json:
```json
{
    "body": "Attachment [trac_9501.2.patch](tarball://root/attachments/some-uuid/ticket9501/trac_9501.2.patch) by was created at 2010-07-17 12:53:25\n\nnew version with fixed warnings.",
    "created_at": "2010-07-17T12:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91252",
    "user": "was"
}
```

Attachment [trac_9501.2.patch](tarball://root/attachments/some-uuid/ticket9501/trac_9501.2.patch) by was created at 2010-07-17 12:53:25

new version with fixed warnings.



---

archive/issue_comments_091253.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-17T12:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91253",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091254.json:
```json
{
    "body": "Looks good, but the file doesn't seem to be included in the reference manual anyway.",
    "created_at": "2010-07-18T14:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91254",
    "user": "malb"
}
```

Looks good, but the file doesn't seem to be included in the reference manual anyway.



---

archive/issue_comments_091255.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T12:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91255",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091256.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T08:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91256",
    "user": "ddrake"
}
```

Resolution: fixed



---

archive/issue_comments_091257.json:
```json
{
    "body": "Merged trac_9501.2.patch in 4.5.2.alpha1.",
    "created_at": "2010-07-22T08:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91257",
    "user": "ddrake"
}
```

Merged trac_9501.2.patch in 4.5.2.alpha1.



---

archive/issue_comments_091258.json:
```json
{
    "body": "This ticket was backed out at #9616.  The new ticket for merging this is #9631.",
    "created_at": "2010-08-08T22:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9501#issuecomment-91258",
    "user": "mpatel"
}
```

This ticket was backed out at #9616.  The new ticket for merging this is #9631.
