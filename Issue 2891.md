# Issue 2891: inline_fortran -- completely rewrite to not save a global variable and *not* got hacked into various global structures all over

archive/issues_002891.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  jdemeyer\n\nThe InlineFortran stuff in misc/inline_fortran.py is bad.  That global variable should be explicitly passed into the __eval__ and __call__ methods, and should *not* be set on creation.   I've attached what the file *should* roughly be, but I can't get it to work.\n\nAlso, it's terrible the hacking in server/support.py to get the fortran stuff in there.  This is just really wrong. \n\nNOTE -- this all works -- it's not a bug.  It's just not good programming.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2891\n\n",
    "created_at": "2008-04-12T03:14:41Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.5",
    "title": "inline_fortran -- completely rewrite to not save a global variable and *not* got hacked into various global structures all over",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2891",
    "user": "was"
}
```
Assignee: cwitty

CC:  jdemeyer

The InlineFortran stuff in misc/inline_fortran.py is bad.  That global variable should be explicitly passed into the __eval__ and __call__ methods, and should *not* be set on creation.   I've attached what the file *should* roughly be, but I can't get it to work.

Also, it's terrible the hacking in server/support.py to get the fortran stuff in there.  This is just really wrong. 

NOTE -- this all works -- it's not a bug.  It's just not good programming.

Issue created by migration from https://trac.sagemath.org/ticket/2891





---

archive/issue_comments_019872.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-04-12T03:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19872",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_019873.json:
```json
{
    "body": "Attachment [inline_fortran.py](tarball://root/attachments/some-uuid/ticket2891/inline_fortran.py) by was created at 2008-04-12 03:17:57",
    "created_at": "2008-04-12T03:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19873",
    "user": "was"
}
```

Attachment [inline_fortran.py](tarball://root/attachments/some-uuid/ticket2891/inline_fortran.py) by was created at 2008-04-12 03:17:57



---

archive/issue_comments_019874.json:
```json
{
    "body": "Hey Jeroen, you worked on several related tickets like #13992 and #13887 - is this ticket even needed at this point?  \n\n~~(Also, I can't figure out how exactly `src/sage/misc/inline_fortran.py` gets used, as it doesn't seem to ever be imported, and is only mentioned a comment in the scripts...)~~ The notebook is the only place this is used in any case (maybe also SMC?).  See also #8427.",
    "created_at": "2014-12-09T16:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19874",
    "user": "kcrisman"
}
```

Hey Jeroen, you worked on several related tickets like #13992 and #13887 - is this ticket even needed at this point?  

~~(Also, I can't figure out how exactly `src/sage/misc/inline_fortran.py` gets used, as it doesn't seem to ever be imported, and is only mentioned a comment in the scripts...)~~ The notebook is the only place this is used in any case (maybe also SMC?).  See also #8427.



---

archive/issue_comments_019875.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n> Hey Jeroen, you worked on several related tickets like #13992 and #13887 - is this ticket even needed at this point?\nFor sure, the issue that this ticket talks about (the `globals` variable) hasn't been changed.",
    "created_at": "2014-12-09T17:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19875",
    "user": "jdemeyer"
}
```

Replying to [comment:8 kcrisman]:
> Hey Jeroen, you worked on several related tickets like #13992 and #13887 - is this ticket even needed at this point?
For sure, the issue that this ticket talks about (the `globals` variable) hasn't been changed.



---

archive/issue_comments_019876.json:
```json
{
    "body": "The problem is also that there isn't a single example using this `globals` argument, so it's hard to even know what the code *should* do.",
    "created_at": "2014-12-09T17:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19876",
    "user": "jdemeyer"
}
```

The problem is also that there isn't a single example using this `globals` argument, so it's hard to even know what the code *should* do.



---

archive/issue_comments_019877.json:
```json
{
    "body": "We could probably remove this whole `inline_fortran` thing without anybody noticing...",
    "created_at": "2014-12-09T17:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19877",
    "user": "jdemeyer"
}
```

We could probably remove this whole `inline_fortran` thing without anybody noticing...



---

archive/issue_comments_019878.json:
```json
{
    "body": "If you care, the `inline_fortran` stuff was added in Sage by\n\n```\ncommit d46359f9384268204bd687e2a7aaded15938399d\nAuthor: William Stein <wstein@gmail.com>\nDate:   Tue Jun 26 16:37:36 2007 -0700\n\n    (Josh Kantor and W Stein) Add support for %fortran in the notebook.\n\n```\n",
    "created_at": "2014-12-09T17:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19878",
    "user": "jdemeyer"
}
```

If you care, the `inline_fortran` stuff was added in Sage by

```
commit d46359f9384268204bd687e2a7aaded15938399d
Author: William Stein <wstein@gmail.com>
Date:   Tue Jun 26 16:37:36 2007 -0700

    (Josh Kantor and W Stein) Add support for %fortran in the notebook.

```




---

archive/issue_comments_019879.json:
```json
{
    "body": "> We could probably remove this whole `inline_fortran` thing without anybody noticing...\nI thought so too, but I figured out where it is used - in sagenb for `%fortran`.  As it says in the thing you quote, in fact.",
    "created_at": "2014-12-09T18:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19879",
    "user": "kcrisman"
}
```

> We could probably remove this whole `inline_fortran` thing without anybody noticing...
I thought so too, but I figured out where it is used - in sagenb for `%fortran`.  As it says in the thing you quote, in fact.



---

archive/issue_comments_019880.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-12-09T20:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19880",
    "user": "jdemeyer"
}
```

New commits:



---

archive/issue_comments_019881.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-12-09T20:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19881",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_019882.json:
```json
{
    "body": "Overall looks good to me, but I would have to take some time to look at the details in a few instances, especially the \n\n```\n# Note that f2py() doesn't raise an exception if it fails.\n```\n\nbit and checking that the deprecations work.  The reorganization, importing, and removal of much of server/support.py is just fine.",
    "created_at": "2014-12-09T20:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19882",
    "user": "kcrisman"
}
```

Overall looks good to me, but I would have to take some time to look at the details in a few instances, especially the 

```
# Note that f2py() doesn't raise an exception if it fails.
```

bit and checking that the deprecations work.  The reorganization, importing, and removal of much of server/support.py is just fine.



---

archive/issue_comments_019883.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-12-09T21:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19883",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_019884.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-12-12T10:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19884",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_019885.json:
```json
{
    "body": "I'm not sure why you removed the doctest file, since after you remove `sage/server/misc.py` there are no doctests left in that directory :-) but surely it can't hurt.\n\nHowever, this needs a slight bit of work to be compatible with https://github.com/sagemath/sagenb/pull/291 now in upstream.  Before:\n\n```\nsage: from sage.server.support import save_session\nsage: save_session()\nDeprecationWarning: \nImporting save_session from here is deprecated. If you need to use it, please import it directly from sagenb.misc.support\nSee http://trac.sagemath.org/2891 for details.\n\n```\n\nafter:\n\n```\nsage: from sage.server.support import save_session\nsage: save_session()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\nAttributeError: 'module' object has no attribute 'save_session'\n```\n\nand likewise for `load_session` and `variables`, I believe.",
    "created_at": "2014-12-12T16:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19885",
    "user": "kcrisman"
}
```

I'm not sure why you removed the doctest file, since after you remove `sage/server/misc.py` there are no doctests left in that directory :-) but surely it can't hurt.

However, this needs a slight bit of work to be compatible with https://github.com/sagemath/sagenb/pull/291 now in upstream.  Before:

```
sage: from sage.server.support import save_session
sage: save_session()
DeprecationWarning: 
Importing save_session from here is deprecated. If you need to use it, please import it directly from sagenb.misc.support
See http://trac.sagemath.org/2891 for details.

```

after:

```
sage: from sage.server.support import save_session
sage: save_session()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
AttributeError: 'module' object has no attribute 'save_session'
```

and likewise for `load_session` and `variables`, I believe.



---

archive/issue_comments_019886.json:
```json
{
    "body": "Glad the deprecation works, but I don't know why this failed - and shouldn't your exception `imp` code take care of this if it wasn't there?\n\n```\nsage: fortran('fib1.f')\n/Users/.../sage/local/lib/python2.7/site-packages/sage/misc/inline_fortran.py:23: DeprecationWarning: Calling fortran() with a filename is deprecated, use fortran(open(f).read) instead\nSee http://trac.sagemath.org/2891 for details.\n  return self.eval(*args, **kwds)\nsage: import numpy\nsage: a = numpy.array(range(10), dtype=float)\nsage: fib(a,10)\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n<ipython-input-5-a86fea2d23a9> in <module>()\n----> 1 fib(a,Integer(10))\n\nNameError: name 'fib' is not defined\nsage: \n```\n\n\nBut it did find the right file, if I do something else it complains a few lines later because it can't load the file, which makes sense.  If I use `globals` (wasn't that the deprecated part? maybe only elsewhere) I get\n\n```\n\nsage: fortran('./fib1.f',globals())\nsage: fib(a,10)  # so now it exists, anyway!\nsage: a = numpy.array(range(10), dtype=float)\nsage: a\narray([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])\n```\n\nI'm not saying 'needs work', but I am saying 'reviewer doesn't understand'.",
    "created_at": "2014-12-12T16:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19886",
    "user": "kcrisman"
}
```

Glad the deprecation works, but I don't know why this failed - and shouldn't your exception `imp` code take care of this if it wasn't there?

```
sage: fortran('fib1.f')
/Users/.../sage/local/lib/python2.7/site-packages/sage/misc/inline_fortran.py:23: DeprecationWarning: Calling fortran() with a filename is deprecated, use fortran(open(f).read) instead
See http://trac.sagemath.org/2891 for details.
  return self.eval(*args, **kwds)
sage: import numpy
sage: a = numpy.array(range(10), dtype=float)
sage: fib(a,10)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-5-a86fea2d23a9> in <module>()
----> 1 fib(a,Integer(10))

NameError: name 'fib' is not defined
sage: 
```


But it did find the right file, if I do something else it complains a few lines later because it can't load the file, which makes sense.  If I use `globals` (wasn't that the deprecated part? maybe only elsewhere) I get

```

sage: fortran('./fib1.f',globals())
sage: fib(a,10)  # so now it exists, anyway!
sage: a = numpy.array(range(10), dtype=float)
sage: a
array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
```

I'm not saying 'needs work', but I am saying 'reviewer doesn't understand'.



---

archive/issue_comments_019887.json:
```json
{
    "body": "But if I write the file in the other test\n\n```\nsage: fortran('./hello.f',globals())\n/Users/.../sage/local/lib/python2.7/site-packages/sage/misc/inline_fortran.py:23: DeprecationWarning: Calling fortran() with a filename is deprecated, use fortran(open(f).read) instead\nSee http://trac.sagemath.org/2891 for details.\n  return self.eval(*args, **kwds)\nsage: hello\n<fortran object>\nsage: hello()\n Hello World!\n```\n",
    "created_at": "2014-12-12T16:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19887",
    "user": "kcrisman"
}
```

But if I write the file in the other test

```
sage: fortran('./hello.f',globals())
/Users/.../sage/local/lib/python2.7/site-packages/sage/misc/inline_fortran.py:23: DeprecationWarning: Calling fortran() with a filename is deprecated, use fortran(open(f).read) instead
See http://trac.sagemath.org/2891 for details.
  return self.eval(*args, **kwds)
sage: hello
<fortran object>
sage: hello()
 Hello World!
```




---

archive/issue_comments_019888.json:
```json
{
    "body": "Replying to [comment:22 kcrisman]:\n> If I use `globals`\nYes, that's what you should do.\n\n> wasn't that the deprecated part? maybe only elsewhere\nIndeed, elsewhere. The idea of this ticket is that the `globals` parameter was moved from `InlineFortran.__init__()` to `InlineFortran.__call__()`.",
    "created_at": "2014-12-12T18:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19888",
    "user": "jdemeyer"
}
```

Replying to [comment:22 kcrisman]:
> If I use `globals`
Yes, that's what you should do.

> wasn't that the deprecated part? maybe only elsewhere
Indeed, elsewhere. The idea of this ticket is that the `globals` parameter was moved from `InlineFortran.__init__()` to `InlineFortran.__call__()`.



---

archive/issue_comments_019889.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-12-12T19:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19889",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_019890.json:
```json
{
    "body": "Got it, I also see what I was messing up earlier.\n\nSo this is fine other than the import stuff in comment:21, though one way to deal with that is to *not* remove those for now and deal with it when updating sagenb, e.g. #10057.",
    "created_at": "2014-12-12T19:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19890",
    "user": "kcrisman"
}
```

Got it, I also see what I was messing up earlier.

So this is fine other than the import stuff in comment:21, though one way to deal with that is to *not* remove those for now and deal with it when updating sagenb, e.g. #10057.



---

archive/issue_comments_019891.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-12-13T07:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19891",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_019892.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-12-13T07:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19892",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_019893.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-13T17:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19893",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_019894.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-12-15T17:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19894",
    "user": "vbraun"
}
```

Resolution: fixed
