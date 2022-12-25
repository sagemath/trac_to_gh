# Issue 8488: Add support for @interact to the Sage library and module for a library of interacts

archive/issues_008488.json:
```json
{
    "body": "Assignee: @jasongrout\n\nCC:  mhampton\n\nSee http://groups.google.com/group/sage-devel/browse_frm/thread/240592d465bd4f84#\n\nIssue created by migration from https://trac.sagemath.org/ticket/8488\n\n",
    "closed_at": "2010-04-19T05:22:30Z",
    "created_at": "2010-03-10T13:16:54Z",
    "labels": [
        "component: interact"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Add support for @interact to the Sage library and module for a library of interacts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8488",
    "user": "https://github.com/williamstein"
}
```
Assignee: @jasongrout

CC:  mhampton

See http://groups.google.com/group/sage-devel/browse_frm/thread/240592d465bd4f84#

Issue created by migration from https://trac.sagemath.org/ticket/8488





---

archive/issue_comments_076378.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T13:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76378",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076379.json:
```json
{
    "body": "Attachment [trac_8488.patch](tarball://root/attachments/some-uuid/ticket8488/trac_8488.patch) by @williamstein created at 2010-03-10 13:22:48",
    "created_at": "2010-03-10T13:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76379",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8488.patch](tarball://root/attachments/some-uuid/ticket8488/trac_8488.patch) by @williamstein created at 2010-03-10 13:22:48



---

archive/issue_comments_076380.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-10T18:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76380",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076381.json:
```json
{
    "body": "I think it would be better to use the `@`wraps decorator in python, which automatically copies the documentation, etc.  Also, the source inspection probably won't work here (I haven't checked, though).  We should spruce up this decorator to follow the pattern in sage/plot/misc.py (see the `@`options or `@`suboptions decorator classes).",
    "created_at": "2010-03-10T18:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76381",
    "user": "https://github.com/jasongrout"
}
```

I think it would be better to use the `@`wraps decorator in python, which automatically copies the documentation, etc.  Also, the source inspection probably won't work here (I haven't checked, though).  We should spruce up this decorator to follow the pattern in sage/plot/misc.py (see the `@`options or `@`suboptions decorator classes).



---

archive/issue_comments_076382.json:
```json
{
    "body": "or even better, we should make a `@`wrap_sage decorator which does the same thing as `@`wraps and additionally does:\n\n```\n        from sage.misc.sageinspect import sage_getsource\n        wrapper._sage_src_ = lambda: sage_getsource(func)\n```\n\nlike in the sage/plot/misc.py files.",
    "created_at": "2010-03-10T18:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76382",
    "user": "https://github.com/jasongrout"
}
```

or even better, we should make a `@`wrap_sage decorator which does the same thing as `@`wraps and additionally does:

```
        from sage.misc.sageinspect import sage_getsource
        wrapper._sage_src_ = lambda: sage_getsource(func)
```

like in the sage/plot/misc.py files.



---

archive/issue_comments_076383.json:
```json
{
    "body": "I just attached a patch which implements a \"sage_wraps\" decorator which mirrors the functools wraps decorator, but also adds the sage-specific _sage_src_ attribute, so that `interacts.demo??` works.\n\nThis is still \"needs work\", since the sage_wraps function needs some doctests.\n\nWe can now simplify the code in sage/plot/misc.py and a few other places that call the `@`wraps decorator using `@`sage_wraps.",
    "created_at": "2010-03-10T20:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76383",
    "user": "https://github.com/jasongrout"
}
```

I just attached a patch which implements a "sage_wraps" decorator which mirrors the functools wraps decorator, but also adds the sage-specific _sage_src_ attribute, so that `interacts.demo??` works.

This is still "needs work", since the sage_wraps function needs some doctests.

We can now simplify the code in sage/plot/misc.py and a few other places that call the `@`wraps decorator using `@`sage_wraps.



---

archive/issue_comments_076384.json:
```json
{
    "body": "Note that there is a bug in the ReST formatting.  After applying both patches above, `interacts.demo??` gives output that is all messed up since apparently the formatting engine doesn't deal well with the single newlines that _sage_src_() returns.  I've run out of time to try to track this down and see if it is a bug in the introspection or in the file or what.",
    "created_at": "2010-03-10T20:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76384",
    "user": "https://github.com/jasongrout"
}
```

Note that there is a bug in the ReST formatting.  After applying both patches above, `interacts.demo??` gives output that is all messed up since apparently the formatting engine doesn't deal well with the single newlines that _sage_src_() returns.  I've run out of time to try to track this down and see if it is a bug in the introspection or in the file or what.



---

archive/issue_comments_076385.json:
```json
{
    "body": "Also, I don't think we should import library_interact into the interacts namespace.  I think interacts.<tab> should just give a list of interacts (in fact, I think it should be broken down a bit further, so that interacts.calculus.<tab> gives calculus interacts, etc.)  Note that because of wonderful namespaces, the same interact could be imported into interacts.calculus and interacts.linear_algebra, for example.",
    "created_at": "2010-03-10T20:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76385",
    "user": "https://github.com/jasongrout"
}
```

Also, I don't think we should import library_interact into the interacts namespace.  I think interacts.<tab> should just give a list of interacts (in fact, I think it should be broken down a bit further, so that interacts.calculus.<tab> gives calculus interacts, etc.)  Note that because of wonderful namespaces, the same interact could be imported into interacts.calculus and interacts.linear_algebra, for example.



---

archive/issue_comments_076386.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-11T01:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76386",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_020389.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2010-03-11T01:50:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "milestone": "sage-4.3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8488#event-20389"
}
```



---

archive/issue_comments_076387.json:
```json
{
    "body": "Changing assignee from @itolkov to @jasongrout.",
    "created_at": "2010-03-11T01:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76387",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @itolkov to @jasongrout.



---

archive/issue_comments_076388.json:
```json
{
    "body": "Oops, I deleted the title, instead of adding a comment, apparently.\n\nOkay, William or Marshall, the ball's back in your court to review my patch.",
    "created_at": "2010-03-11T01:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76388",
    "user": "https://github.com/jasongrout"
}
```

Oops, I deleted the title, instead of adding a comment, apparently.

Okay, William or Marshall, the ball's back in your court to review my patch.



---

archive/issue_comments_076389.json:
```json
{
    "body": "REVIEW:\n\n* very nice using the python wrapping stuff, and making source code introspection work, in theory!\n\n* In practice, source code introspection does not work, though this is due to a lazy assumption *I* made I think when implementing interact in the notebook, namely I think when the notebook server sees \"`@`interact\" in the output, it does something funny with formatting.  Anyway, if you try:\n\n```\ninteracts.calculus.taylor_polynomial??\n```\nin a cell then shift-enter, you'll see the source is all on one long line, which isn't good.  That said, fixing this shouldn't be part of this patch, since it's a very different issue in the sage notebook itself, and maybe quite tricky to deal with.\n\n* Important. Try this in an input cell:\n\n```\ninteracts.calculus.[tab]\n```\nInstead of getting *one* thing, you get 15.  This *has* to be fixed. \n\n* Otherwise, I'm happy with this patch.",
    "created_at": "2010-03-11T04:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76389",
    "user": "https://github.com/williamstein"
}
```

REVIEW:

* very nice using the python wrapping stuff, and making source code introspection work, in theory!

* In practice, source code introspection does not work, though this is due to a lazy assumption *I* made I think when implementing interact in the notebook, namely I think when the notebook server sees "`@`interact" in the output, it does something funny with formatting.  Anyway, if you try:

```
interacts.calculus.taylor_polynomial??
```
in a cell then shift-enter, you'll see the source is all on one long line, which isn't good.  That said, fixing this shouldn't be part of this patch, since it's a very different issue in the sage notebook itself, and maybe quite tricky to deal with.

* Important. Try this in an input cell:

```
interacts.calculus.[tab]
```
Instead of getting *one* thing, you get 15.  This *has* to be fixed. 

* Otherwise, I'm happy with this patch.



---

archive/issue_comments_076390.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-11T04:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76390",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076391.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-11T05:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76391",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076392.json:
```json
{
    "body": "Replying to [comment:11 was]:\n\n> REVIEW: * very nice using the python wrapping stuff, and making source code introspection work, in theory! * In practice, source code introspection does not work, though this is due to a lazy assumption *I* made I think when implementing interact in the notebook, namely I think when the notebook server sees \"`@`interact\" in the output, it does something funny with formatting.  Anyway, if you try: ` interacts.calculus.taylor_polynomial?? ` in a cell then shift-enter, you'll see the source is all on one long line, which isn't good.  That said, fixing this shouldn't be part of this patch, since it's a very different issue in the sage notebook itself, and maybe quite tricky to deal with.\n\n\nAh, that makes sense.  I saw this, and even started writing a ticket for it, but I couldn't reproduce it with anything besides the interact stuff (see my comment above about ReST formatting), and then I ran out of time.\n\nI'm attaching a new patch which takes care of the namespace issue you mentioned.\u00a0 Basically, I lump everything into a library file, and then just import into calculus.py the actual interact. I'm sure there's a fancy object we could make that would nicely categorize everything, but this quick solution takes advantage of the nice namespace framework we already have.",
    "created_at": "2010-03-11T05:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76392",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:11 was]:

> REVIEW: * very nice using the python wrapping stuff, and making source code introspection work, in theory! * In practice, source code introspection does not work, though this is due to a lazy assumption *I* made I think when implementing interact in the notebook, namely I think when the notebook server sees "`@`interact" in the output, it does something funny with formatting.  Anyway, if you try: ` interacts.calculus.taylor_polynomial?? ` in a cell then shift-enter, you'll see the source is all on one long line, which isn't good.  That said, fixing this shouldn't be part of this patch, since it's a very different issue in the sage notebook itself, and maybe quite tricky to deal with.


Ah, that makes sense.  I saw this, and even started writing a ticket for it, but I couldn't reproduce it with anything besides the interact stuff (see my comment above about ReST formatting), and then I ran out of time.

I'm attaching a new patch which takes care of the namespace issue you mentioned.  Basically, I lump everything into a library file, and then just import into calculus.py the actual interact. I'm sure there's a fancy object we could make that would nicely categorize everything, but this quick solution takes advantage of the nice namespace framework we already have.



---

archive/issue_comments_076393.json:
```json
{
    "body": "Attachment [trac-8488-sage_wrap_decorator.patch](tarball://root/attachments/some-uuid/ticket8488/trac-8488-sage_wrap_decorator.patch) by @jasongrout created at 2010-03-11 05:31:43\n\napply on top of previous patch",
    "created_at": "2010-03-11T05:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76393",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8488-sage_wrap_decorator.patch](tarball://root/attachments/some-uuid/ticket8488/trac-8488-sage_wrap_decorator.patch) by @jasongrout created at 2010-03-11 05:31:43

apply on top of previous patch



---

archive/issue_comments_076394.json:
```json
{
    "body": "Replying to [comment:11 was]:\n\n>    * Otherwise, I'm happy with this patch. \n\n\nFYI, I'm leaving it to you to set \"positive review\" after my last patch, if you're still happy.",
    "created_at": "2010-03-11T15:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76394",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:11 was]:

>    * Otherwise, I'm happy with this patch. 


FYI, I'm leaving it to you to set "positive review" after my last patch, if you're still happy.



---

archive/issue_comments_076395.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-27T17:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76395",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076396.json:
```json
{
    "body": "I applied both patches to 4.3.5 and I'm getting doctest failures:\n\n```\nsage -t  devel/sage/sage/interacts/library.py\n**********************************************************************\nFile \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage-new/sage/interacts/library.py\", line 18:\n    sage: @interacts.decorator.library_interact\n    def f(n=Integer(5)): print n\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[2]>\", line 1, in <module>\n        @interacts.decorator.library_interact###line 18:\n    sage: @interacts.decorator.library_interact\n    AttributeError: 'module' object has no attribute 'decorator'\n**********************************************************************\nFile \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage-new/sage/interacts/library.py\", line 21:\n    sage: f()  # an interact appears\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[3]>\", line 1, in <module>\n        f()  # an interact appears###line 21:\n    sage: f()  # an interact appears\n    NameError: name 'f' is not defined\n**********************************************************************\nFile \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage-new/sage/interacts/library.py\", line 45:\n    sage: interacts.decorator.demo()\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[2]>\", line 1, in <module>\n        interacts.decorator.demo()###line 45:\n    sage: interacts.decorator.demo()\n    AttributeError: 'module' object has no attribute 'decorator'\n**********************************************************************\n2 items had failures:\n   2 of   4 in __main__.example_1\n   1 of   3 in __main__.example_2\n***Test Failed*** 3 failures.\n```",
    "created_at": "2010-04-16T19:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76396",
    "user": "https://github.com/jhpalmieri"
}
```

I applied both patches to 4.3.5 and I'm getting doctest failures:

```
sage -t  devel/sage/sage/interacts/library.py
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage-new/sage/interacts/library.py", line 18:
    sage: @interacts.decorator.library_interact
    def f(n=Integer(5)): print n
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        @interacts.decorator.library_interact###line 18:
    sage: @interacts.decorator.library_interact
    AttributeError: 'module' object has no attribute 'decorator'
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage-new/sage/interacts/library.py", line 21:
    sage: f()  # an interact appears
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[3]>", line 1, in <module>
        f()  # an interact appears###line 21:
    sage: f()  # an interact appears
    NameError: name 'f' is not defined
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage-new/sage/interacts/library.py", line 45:
    sage: interacts.decorator.demo()
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        interacts.decorator.demo()###line 45:
    sage: interacts.decorator.demo()
    AttributeError: 'module' object has no attribute 'decorator'
**********************************************************************
2 items had failures:
   2 of   4 in __main__.example_1
   1 of   3 in __main__.example_2
***Test Failed*** 3 failures.
```



---

archive/issue_comments_076397.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-16T19:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76397",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076398.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-18T00:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76398",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076399.json:
```json
{
    "body": "Attachment [trac_8488-part3.patch](tarball://root/attachments/some-uuid/ticket8488/trac_8488-part3.patch) by @williamstein created at 2010-04-18 00:33:15",
    "created_at": "2010-04-18T00:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76399",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8488-part3.patch](tarball://root/attachments/some-uuid/ticket8488/trac_8488-part3.patch) by @williamstein created at 2010-04-18 00:33:15



---

archive/issue_comments_076400.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-18T00:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76400",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076401.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-18T18:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76401",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076402.json:
```json
{
    "body": "When I apply this, I get a new doctest failure:\n\n```\n**********************************************************************\nFile \"/Applications/sage_builds/sage-4.4.alpha0/devel/sage-new/sage/symbolic/ring.pyx\", line 443:\n    sage: SR.symbol() # temporary variable\nExpected:\n    symbol160\nGot:\n    symbol162\n**********************************************************************\n```\nI don't know why these patches cause this file to file.  Can we just change \"160\" to \"162\"?",
    "created_at": "2010-04-18T18:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76402",
    "user": "https://github.com/jhpalmieri"
}
```

When I apply this, I get a new doctest failure:

```
**********************************************************************
File "/Applications/sage_builds/sage-4.4.alpha0/devel/sage-new/sage/symbolic/ring.pyx", line 443:
    sage: SR.symbol() # temporary variable
Expected:
    symbol160
Got:
    symbol162
**********************************************************************
```
I don't know why these patches cause this file to file.  Can we just change "160" to "162"?



---

archive/issue_comments_076403.json:
```json
{
    "body": "Replying to [comment:18 jhpalmieri]:\n> When I apply this, I get a new doctest failure:\n> \n> ```\n> **********************************************************************\n> File \"/Applications/sage_builds/sage-4.4.alpha0/devel/sage-new/sage/symbolic/ring.pyx\", line 443:\n>     sage: SR.symbol() # temporary variable\n> Expected:\n>     symbol160\n> Got:\n>     symbol162\n> **********************************************************************\n> ```\n> I don't know why these patches cause this file to file.  Can we just change \"160\" to \"162\"?\n\n\nYes.  It's just some internal counter.   That's a stupid doctest though, since an unrelated change anywhere else in Sage could break it.  Can you change the output to\n\n   symbol...\n\n?\n\nWilliam",
    "created_at": "2010-04-18T22:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76403",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:18 jhpalmieri]:
> When I apply this, I get a new doctest failure:
> 
> ```
> **********************************************************************
> File "/Applications/sage_builds/sage-4.4.alpha0/devel/sage-new/sage/symbolic/ring.pyx", line 443:
>     sage: SR.symbol() # temporary variable
> Expected:
>     symbol160
> Got:
>     symbol162
> **********************************************************************
> ```
> I don't know why these patches cause this file to file.  Can we just change "160" to "162"?


Yes.  It's just some internal counter.   That's a stupid doctest though, since an unrelated change anywhere else in Sage could break it.  Can you change the output to

   symbol...

?

William



---

archive/issue_comments_076404.json:
```json
{
    "body": "Okay, here's a patch.",
    "created_at": "2010-04-19T00:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76404",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, here's a patch.



---

archive/issue_comments_076405.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-19T00:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76405",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076406.json:
```json
{
    "body": "Attachment [trac_8488-part4.patch](tarball://root/attachments/some-uuid/ticket8488/trac_8488-part4.patch) by @jhpalmieri created at 2010-04-19 00:07:17",
    "created_at": "2010-04-19T00:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76406",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8488-part4.patch](tarball://root/attachments/some-uuid/ticket8488/trac_8488-part4.patch) by @jhpalmieri created at 2010-04-19 00:07:17



---

archive/issue_comments_076407.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-19T05:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76407",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076408.json:
```json
{
    "body": "(I just got around now to applying the patch and running doctests.)",
    "created_at": "2010-04-19T05:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76408",
    "user": "https://github.com/jhpalmieri"
}
```

(I just got around now to applying the patch and running doctests.)



---

archive/issue_comments_076409.json:
```json
{
    "body": "Merged into 4.4.alpha1:\n- trac_8488.patch\n- trac-8488-sage_wrap_decorator.patch\n- trac_8488-part3.patch\n- trac_8488-part4.patch",
    "created_at": "2010-04-19T05:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76409",
    "user": "https://github.com/jhpalmieri"
}
```

Merged into 4.4.alpha1:
- trac_8488.patch
- trac-8488-sage_wrap_decorator.patch
- trac_8488-part3.patch
- trac_8488-part4.patch



---

archive/issue_events_020390.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-19T05:22:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8488#event-20390"
}
```



---

archive/issue_comments_076410.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8488#issuecomment-76410",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
