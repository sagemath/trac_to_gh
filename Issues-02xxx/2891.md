# Issue 2891: Don't use globals() to initialize InlineFortran

archive/issues_002891.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @jdemeyer\n\nThe `InlineFortran` stuff in `src/sage/misc/inline_fortran.py` is bad.  That `globals` variable should be explicitly passed into the `eval` and `__call__` methods, and should *not* be set on creation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2891\n\n",
    "closed_at": "2014-12-15T17:50:57Z",
    "created_at": "2008-04-12T03:14:41Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.5",
    "title": "Don't use globals() to initialize InlineFortran",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2891",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

CC:  @jdemeyer

The `InlineFortran` stuff in `src/sage/misc/inline_fortran.py` is bad.  That `globals` variable should be explicitly passed into the `eval` and `__call__` methods, and should *not* be set on creation.

Issue created by migration from https://trac.sagemath.org/ticket/2891





---

archive/issue_comments_019831.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-04-12T03:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19831",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_019832.json:
```json
{
    "body": "Attachment [inline_fortran.py](tarball://root/attachments/some-uuid/ticket2891/inline_fortran.py) by @williamstein created at 2008-04-12 03:17:57",
    "created_at": "2008-04-12T03:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19832",
    "user": "https://github.com/williamstein"
}
```

Attachment [inline_fortran.py](tarball://root/attachments/some-uuid/ticket2891/inline_fortran.py) by @williamstein created at 2008-04-12 03:17:57



---

archive/issue_events_006612.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2891#event-6612"
}
```



---

archive/issue_events_006613.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2891#event-6613"
}
```



---

archive/issue_events_006614.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2891#event-6614"
}
```



---

archive/issue_events_006615.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2891#event-6615"
}
```



---

archive/issue_events_006616.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2891#event-6616"
}
```



---

archive/issue_events_006617.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2891#event-6617"
}
```



---

archive/issue_events_006618.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2891#event-6618"
}
```



---

archive/issue_comments_019833.json:
```json
{
    "body": "Hey Jeroen, you worked on several related tickets like #13992 and #13887 - is this ticket even needed at this point?  \n\n~~(Also, I can't figure out how exactly `src/sage/misc/inline_fortran.py` gets used, as it doesn't seem to ever be imported, and is only mentioned a comment in the scripts...)~~ The notebook is the only place this is used in any case (maybe also SMC?).  See also #8427.",
    "created_at": "2014-12-09T16:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19833",
    "user": "https://github.com/kcrisman"
}
```

Hey Jeroen, you worked on several related tickets like #13992 and #13887 - is this ticket even needed at this point?  

~~(Also, I can't figure out how exactly `src/sage/misc/inline_fortran.py` gets used, as it doesn't seem to ever be imported, and is only mentioned a comment in the scripts...)~~ The notebook is the only place this is used in any case (maybe also SMC?).  See also #8427.



---

archive/issue_comments_019834.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n> Hey Jeroen, you worked on several related tickets like #13992 and #13887 - is this ticket even needed at this point?\n\nFor sure, the issue that this ticket talks about (the `globals` variable) hasn't been changed.",
    "created_at": "2014-12-09T17:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19834",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:8 kcrisman]:
> Hey Jeroen, you worked on several related tickets like #13992 and #13887 - is this ticket even needed at this point?

For sure, the issue that this ticket talks about (the `globals` variable) hasn't been changed.



---

archive/issue_comments_019835.json:
```json
{
    "body": "The problem is also that there isn't a single example using this `globals` argument, so it's hard to even know what the code *should* do.",
    "created_at": "2014-12-09T17:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19835",
    "user": "https://github.com/jdemeyer"
}
```

The problem is also that there isn't a single example using this `globals` argument, so it's hard to even know what the code *should* do.



---

archive/issue_comments_019836.json:
```json
{
    "body": "We could probably remove this whole `inline_fortran` thing without anybody noticing...",
    "created_at": "2014-12-09T17:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19836",
    "user": "https://github.com/jdemeyer"
}
```

We could probably remove this whole `inline_fortran` thing without anybody noticing...



---

archive/issue_comments_019837.json:
```json
{
    "body": "If you care, the `inline_fortran` stuff was added in Sage by\n\n```\ncommit d46359f9384268204bd687e2a7aaded15938399d\nAuthor: William Stein <wstein@gmail.com>\nDate:   Tue Jun 26 16:37:36 2007 -0700\n\n    (Josh Kantor and W Stein) Add support for %fortran in the notebook.\n\n```",
    "created_at": "2014-12-09T17:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19837",
    "user": "https://github.com/jdemeyer"
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

archive/issue_comments_019838.json:
```json
{
    "body": "> We could probably remove this whole `inline_fortran` thing without anybody noticing...\n\nI thought so too, but I figured out where it is used - in sagenb for `%fortran`.  As it says in the thing you quote, in fact.",
    "created_at": "2014-12-09T18:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19838",
    "user": "https://github.com/kcrisman"
}
```

> We could probably remove this whole `inline_fortran` thing without anybody noticing...

I thought so too, but I figured out where it is used - in sagenb for `%fortran`.  As it says in the thing you quote, in fact.



---

archive/issue_events_006619.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-12-09T19:46:19Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2891#event-6619"
}
```



---

archive/issue_events_006620.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-12-09T19:46:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "milestone": "sage-6.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2891#event-6620"
}
```



---

archive/issue_comments_019839.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-12-09T20:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19839",
    "user": "https://github.com/jdemeyer"
}
```

New commits:



---

archive/issue_comments_019840.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-12-09T20:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19840",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_019841.json:
```json
{
    "body": "Overall looks good to me, but I would have to take some time to look at the details in a few instances, especially the \n\n```\n# Note that f2py() doesn't raise an exception if it fails.\n```\nbit and checking that the deprecations work.  The reorganization, importing, and removal of much of server/support.py is just fine.",
    "created_at": "2014-12-09T20:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19841",
    "user": "https://github.com/kcrisman"
}
```

Overall looks good to me, but I would have to take some time to look at the details in a few instances, especially the 

```
# Note that f2py() doesn't raise an exception if it fails.
```
bit and checking that the deprecations work.  The reorganization, importing, and removal of much of server/support.py is just fine.



---

archive/issue_comments_019842.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-12-09T21:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19842",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_019843.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-12-12T10:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19843",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_019844.json:
```json
{
    "body": "I'm not sure why you removed the doctest file, since after you remove `sage/server/misc.py` there are no doctests left in that directory :-) but surely it can't hurt.\n\nHowever, this needs a slight bit of work to be compatible with https://github.com/sagemath/sagenb/pull/291 now in upstream.  Before:\n\n```\nsage: from sage.server.support import save_session\nsage: save_session()\nDeprecationWarning: \nImporting save_session from here is deprecated. If you need to use it, please import it directly from sagenb.misc.support\nSee http://trac.sagemath.org/2891 for details.\n\n```\nafter:\n\n```\nsage: from sage.server.support import save_session\nsage: save_session()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\nAttributeError: 'module' object has no attribute 'save_session'\n```\nand likewise for `load_session` and `variables`, I believe.",
    "created_at": "2014-12-12T16:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19844",
    "user": "https://github.com/kcrisman"
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

archive/issue_comments_019845.json:
```json
{
    "body": "Glad the deprecation works, but I don't know why this failed - and shouldn't your exception `imp` code take care of this if it wasn't there?\n\n```\nsage: fortran('fib1.f')\n/Users/.../sage/local/lib/python2.7/site-packages/sage/misc/inline_fortran.py:23: DeprecationWarning: Calling fortran() with a filename is deprecated, use fortran(open(f).read) instead\nSee http://trac.sagemath.org/2891 for details.\n  return self.eval(*args, **kwds)\nsage: import numpy\nsage: a = numpy.array(range(10), dtype=float)\nsage: fib(a,10)\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n<ipython-input-5-a86fea2d23a9> in <module>()\n----> 1 fib(a,Integer(10))\n\nNameError: name 'fib' is not defined\nsage: \n```\n\nBut it did find the right file, if I do something else it complains a few lines later because it can't load the file, which makes sense.  If I use `globals` (wasn't that the deprecated part? maybe only elsewhere) I get\n\n```\n\nsage: fortran('./fib1.f',globals())\nsage: fib(a,10)  # so now it exists, anyway!\nsage: a = numpy.array(range(10), dtype=float)\nsage: a\narray([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])\n```\nI'm not saying 'needs work', but I am saying 'reviewer doesn't understand'.",
    "created_at": "2014-12-12T16:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19845",
    "user": "https://github.com/kcrisman"
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

archive/issue_comments_019846.json:
```json
{
    "body": "But if I write the file in the other test\n\n```\nsage: fortran('./hello.f',globals())\n/Users/.../sage/local/lib/python2.7/site-packages/sage/misc/inline_fortran.py:23: DeprecationWarning: Calling fortran() with a filename is deprecated, use fortran(open(f).read) instead\nSee http://trac.sagemath.org/2891 for details.\n  return self.eval(*args, **kwds)\nsage: hello\n<fortran object>\nsage: hello()\n Hello World!\n```",
    "created_at": "2014-12-12T16:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19846",
    "user": "https://github.com/kcrisman"
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

archive/issue_comments_019847.json:
```json
{
    "body": "Replying to [comment:22 kcrisman]:\n> If I use `globals`\n\nYes, that's what you should do.\n\n> wasn't that the deprecated part? maybe only elsewhere\n\nIndeed, elsewhere. The idea of this ticket is that the `globals` parameter was moved from `InlineFortran.__init__()` to `InlineFortran.__call__()`.",
    "created_at": "2014-12-12T18:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19847",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:22 kcrisman]:
> If I use `globals`

Yes, that's what you should do.

> wasn't that the deprecated part? maybe only elsewhere

Indeed, elsewhere. The idea of this ticket is that the `globals` parameter was moved from `InlineFortran.__init__()` to `InlineFortran.__call__()`.



---

archive/issue_comments_019848.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-12-12T19:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19848",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_019849.json:
```json
{
    "body": "Got it, I also see what I was messing up earlier.\n\nSo this is fine other than the import stuff in comment:21, though one way to deal with that is to *not* remove those for now and deal with it when updating sagenb, e.g. #10057.",
    "created_at": "2014-12-12T19:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19849",
    "user": "https://github.com/kcrisman"
}
```

Got it, I also see what I was messing up earlier.

So this is fine other than the import stuff in comment:21, though one way to deal with that is to *not* remove those for now and deal with it when updating sagenb, e.g. #10057.



---

archive/issue_comments_019850.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-12-13T07:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19850",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_019851.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-12-13T07:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19851",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_019852.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-13T17:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19852",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_019853.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-12-15T17:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2891#issuecomment-19853",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_006621.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-12-15T17:50:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2891",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2891#event-6621"
}
```
