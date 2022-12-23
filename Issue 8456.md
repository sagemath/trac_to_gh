# Issue 8456: lazy import improvements

archive/issues_008456.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  rishi jason rlm\n\n1) Cythonize for speed.\n2) Insert original object into namespace on resolution\n3) Support import *\n\nIssue created by migration from https://trac.sagemath.org/ticket/8456\n\n",
    "created_at": "2010-03-06T08:52:13Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "lazy import improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8456",
    "user": "robertwb"
}
```
Assignee: tbd

CC:  rishi jason rlm

1) Cythonize for speed.
2) Insert original object into namespace on resolution
3) Support import *

Issue created by migration from https://trac.sagemath.org/ticket/8456





---

archive/issue_comments_076082.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-06T09:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76082",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_076083.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-06T09:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76083",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076084.json:
```json
{
    "body": "I split it up into two patches for easier refereeing. The first simply moves lazy_import.py to lazy_import.pyx.",
    "created_at": "2010-03-06T09:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76084",
    "user": "robertwb"
}
```

I split it up into two patches for easier refereeing. The first simply moves lazy_import.py to lazy_import.pyx.



---

archive/issue_comments_076085.json:
```json
{
    "body": "I started with importing the first patch only. I tried to lazy-import ZZ, but it did not properly work:\n\n\n```\nsage: from sage.misc.lazy_import import lazy_import\nsage: lazy_import('sage.rings.all', 'ZZ')\nsage: type(ZZ)\n<type 'sage.rings.integer_ring.IntegerRing_class'>\n```\n\nAccording to the doc tests, the result should be different.\n\nI then imported the second patch. When starting sage, I got\n\n\n```\n---------------------------------------------------------------------------\nOSError                                   Traceback (most recent call last)\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67\n     68\n\n/home/king/SAGE/sage-4.3.1/local/bin/ipy_profile_sage.py in <module>()\n      5     preparser(True)\n      6\n----> 7     import sage.all_cmdline\n      8     sage.all_cmdline._init_cmdline(globals())\n      9\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()\n     12 try:\n     13\n---> 14     from sage.all import *\n     15     from sage.calculus.predefined import x\n     16     preparser(on=True)\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/all.py in <module>()\n    323 # Cache the contents of star imports.\n\n    324 import sage.misc.lazy_import\n--> 325 sage.misc.lazy_import.save_cache_file()\n    326\n    327\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/lazy_import.so in sage.misc.lazy_import.save_cache_file (sage/misc/lazy_import.c:1977)()\n\nOSError: [Errno 18] Invalid cross-device link\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\nNo idea what this means. But I think it is \"needs work\".\n\nCheers, Simon",
    "created_at": "2010-03-19T10:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76085",
    "user": "SimonKing"
}
```

I started with importing the first patch only. I tried to lazy-import ZZ, but it did not properly work:


```
sage: from sage.misc.lazy_import import lazy_import
sage: lazy_import('sage.rings.all', 'ZZ')
sage: type(ZZ)
<type 'sage.rings.integer_ring.IntegerRing_class'>
```

According to the doc tests, the result should be different.

I then imported the second patch. When starting sage, I got


```
---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67
     68

/home/king/SAGE/sage-4.3.1/local/bin/ipy_profile_sage.py in <module>()
      5     preparser(True)
      6
----> 7     import sage.all_cmdline
      8     sage.all_cmdline._init_cmdline(globals())
      9

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/all.py in <module>()
    323 # Cache the contents of star imports.

    324 import sage.misc.lazy_import
--> 325 sage.misc.lazy_import.save_cache_file()
    326
    327

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/lazy_import.so in sage.misc.lazy_import.save_cache_file (sage/misc/lazy_import.c:1977)()

OSError: [Errno 18] Invalid cross-device link
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```

No idea what this means. But I think it is "needs work".

Cheers, Simon



---

archive/issue_comments_076086.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-19T10:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76086",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076087.json:
```json
{
    "body": "PS:\n\nWhen quitting sage after the unsuccessful start, I got\n\n\n```\nsage: quit\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/king/SAGE/sage-4.3.1/local/bin/<ipython console> in <module>()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/IPython/iplib.pyc in ipmagic(self, arg_s)\n    951         else:\n    952             magic_args = self.var_expand(magic_args,1)\n--> 953             return fn(magic_args)\n    954\n    955     def ipalias(self,arg_s):\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/IPython/Magic.pyc in magic_quit(self, parameter_s)\n   2478         \"\"\"Exit IPython, confirming if configured to do so (like %exit)\"\"\"\n   2479\n-> 2480         self.shell.exit()\n   2481\n   2482     def magic_Exit(self, parameter_s=''):\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/all.py in _quit_sage_(self)\n    292         self.exit_now = True\n    293     if self.exit_now:\n--> 294         quit_sage()\n    295         self.exit_now = True\n    296\n\nTypeError: 'NoneType' object is not callable\n```\n\nEven worse, hg_sage does not work. So, it is more difficult now to repair my sage installation...",
    "created_at": "2010-03-19T10:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76087",
    "user": "SimonKing"
}
```

PS:

When quitting sage after the unsuccessful start, I got


```
sage: quit
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/SAGE/sage-4.3.1/local/bin/<ipython console> in <module>()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/IPython/iplib.pyc in ipmagic(self, arg_s)
    951         else:
    952             magic_args = self.var_expand(magic_args,1)
--> 953             return fn(magic_args)
    954
    955     def ipalias(self,arg_s):

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/IPython/Magic.pyc in magic_quit(self, parameter_s)
   2478         """Exit IPython, confirming if configured to do so (like %exit)"""
   2479
-> 2480         self.shell.exit()
   2481
   2482     def magic_Exit(self, parameter_s=''):

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/all.py in _quit_sage_(self)
    292         self.exit_now = True
    293     if self.exit_now:
--> 294         quit_sage()
    295         self.exit_now = True
    296

TypeError: 'NoneType' object is not callable
```

Even worse, hg_sage does not work. So, it is more difficult now to repair my sage installation...



---

archive/issue_comments_076088.json:
```json
{
    "body": "Hmm... is this on top of an alpha? Worked fine for me. \n\nAs for backing out, you can do \"sage -hg rollback\"",
    "created_at": "2010-03-19T17:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76088",
    "user": "robertwb"
}
```

Hmm... is this on top of an alpha? Worked fine for me. 

As for backing out, you can do "sage -hg rollback"



---

archive/issue_comments_076089.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-22T20:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76089",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_076090.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-22T20:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76090",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076091.json:
```json
{
    "body": "OK, the problem was I was using os.rename rather than, say, shutil.move, which caused errors when the DOT_SAGE file was not on the same filesystem as temp files. Glad you caught that, ready for another review.",
    "created_at": "2010-06-22T20:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76091",
    "user": "robertwb"
}
```

OK, the problem was I was using os.rename rather than, say, shutil.move, which caused errors when the DOT_SAGE file was not on the same filesystem as temp files. Glad you caught that, ready for another review.



---

archive/issue_comments_076092.json:
```json
{
    "body": "Simon, could you look at this again, when it's convenient?  I can try to review this, but I'm not sure that I'm sufficiently familiar with Cython.\n\nFor me, all three patches apply cleanly to 4.5.3.alpha1 (using a Mercurial queue).",
    "created_at": "2010-08-20T01:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76092",
    "user": "mpatel"
}
```

Simon, could you look at this again, when it's convenient?  I can try to review this, but I'm not sure that I'm sufficiently familiar with Cython.

For me, all three patches apply cleanly to 4.5.3.alpha1 (using a Mercurial queue).



---

archive/issue_comments_076093.json:
```json
{
    "body": "Lots of people want to see a faster Sage startup; is anyone willing to review this?",
    "created_at": "2010-10-20T05:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76093",
    "user": "robertwb"
}
```

Lots of people want to see a faster Sage startup; is anyone willing to review this?



---

archive/issue_comments_076094.json:
```json
{
    "body": "rebase 8456-lazy-import-cython.patch to sage 4.6\n\npatches apply and doctest pass. The code looks ok, but I do not know (yet) cython nor python introspection to give a positive review.",
    "created_at": "2010-11-04T12:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76094",
    "user": "lftabera"
}
```

rebase 8456-lazy-import-cython.patch to sage 4.6

patches apply and doctest pass. The code looks ok, but I do not know (yet) cython nor python introspection to give a positive review.



---

archive/issue_comments_076095.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-11-04T15:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76095",
    "user": "lftabera"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_076096.json:
```json
{
    "body": "As a user, I would be puzzled if I found at the begining of the session:\n\n\n```\nsage: InfinityRing\n<sage.misc.lazy_import.LazyImport object at 0x7f51dca0e290>\nsage: InfinityRing()\nZero\nsage: InfinityRing\nThe Infinity Ring\n```\n\n\nSo I think that LazyImport should have a __repr__ method that inserts the real object in the namespace.\n\nThe problem is that once you start with this kind of things you do not know where to stop...\n\n\n```\nsage: infinity in InfinityRing\nTypeError: argument of type 'sage.misc.lazy_import.LazyImport' is not iterable\n```\n\n\nSo, what about __repr__, __contains__, _latex_, __cmp__ ? Is it worth to add them to the class? Should this be in another ticket?",
    "created_at": "2010-11-04T15:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76096",
    "user": "lftabera"
}
```

As a user, I would be puzzled if I found at the begining of the session:


```
sage: InfinityRing
<sage.misc.lazy_import.LazyImport object at 0x7f51dca0e290>
sage: InfinityRing()
Zero
sage: InfinityRing
The Infinity Ring
```


So I think that LazyImport should have a __repr__ method that inserts the real object in the namespace.

The problem is that once you start with this kind of things you do not know where to stop...


```
sage: infinity in InfinityRing
TypeError: argument of type 'sage.misc.lazy_import.LazyImport' is not iterable
```


So, what about __repr__, __contains__, _latex_, __cmp__ ? Is it worth to add them to the class? Should this be in another ticket?



---

archive/issue_comments_076097.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-11-04T17:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76097",
    "user": "robertwb"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_076098.json:
```json
{
    "body": "Hmm... it looks like I need to manually add the typeslot methods, as they don't get forwarded with getattr. Thanks for catching this, I'll post another patch.",
    "created_at": "2010-11-04T17:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76098",
    "user": "robertwb"
}
```

Hmm... it looks like I need to manually add the typeslot methods, as they don't get forwarded with getattr. Thanks for catching this, I'll post another patch.



---

archive/issue_comments_076099.json:
```json
{
    "body": "Apply only 8456-lazy-import-cython-rebase-4.6.patch and 8456-lazy-import-enhancements-4.6.patch. This fixes the issue with `__repr__` and all the other special methods.",
    "created_at": "2010-11-07T06:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76099",
    "user": "robertwb"
}
```

Apply only 8456-lazy-import-cython-rebase-4.6.patch and 8456-lazy-import-enhancements-4.6.patch. This fixes the issue with `__repr__` and all the other special methods.



---

archive/issue_comments_076100.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-07T06:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76100",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076101.json:
```json
{
    "body": "Replying to [comment:14 robertwb]:\n> Apply only 8456-lazy-import-cython-rebase-4.6.patch and 8456-lazy-import-enhancements-4.6.patch. This fixes the issue with `__repr__` and all the other special methods. \n\nAre you sure that's right?\n\n\n```\nrlmill@fermat:~/sage-4.6.1.alpha2/devel/sage-main$ hg qpush\napplying 8456-lazy-import-cython-rebase-4.6.patch\nunable to find 'sage/misc/lazy_import.pyx' for patching\n8 out of 8 hunks FAILED -- saving rejects to file sage/misc/lazy_import.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh 8456-lazy-import-cython-rebase-4.6.patch\n```\n",
    "created_at": "2010-11-26T13:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76101",
    "user": "rlm"
}
```

Replying to [comment:14 robertwb]:
> Apply only 8456-lazy-import-cython-rebase-4.6.patch and 8456-lazy-import-enhancements-4.6.patch. This fixes the issue with `__repr__` and all the other special methods. 

Are you sure that's right?


```
rlmill@fermat:~/sage-4.6.1.alpha2/devel/sage-main$ hg qpush
applying 8456-lazy-import-cython-rebase-4.6.patch
unable to find 'sage/misc/lazy_import.pyx' for patching
8 out of 8 hunks FAILED -- saving rejects to file sage/misc/lazy_import.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 8456-lazy-import-cython-rebase-4.6.patch
```




---

archive/issue_comments_076102.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-26T13:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76102",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076103.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-26T16:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76103",
    "user": "rlm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076104.json:
```json
{
    "body": "Sorry, I missed the dependency... :/",
    "created_at": "2010-11-26T16:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76104",
    "user": "rlm"
}
```

Sorry, I missed the dependency... :/



---

archive/issue_comments_076105.json:
```json
{
    "body": "Attachment\n\napply instead of 8456-lazy-import-cython.patch",
    "created_at": "2010-12-02T06:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76105",
    "user": "robertwb"
}
```

Attachment

apply instead of 8456-lazy-import-cython.patch



---

archive/issue_comments_076106.json:
```json
{
    "body": "The code looks good. Is there a reason why _cmp_ does not have a test?",
    "created_at": "2010-12-04T17:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76106",
    "user": "lftabera"
}
```

The code looks good. Is there a reason why _cmp_ does not have a test?



---

archive/issue_comments_076107.json:
```json
{
    "body": "{{__cmp__}} does have a test. \n\nThe buildbot needs to know to apply 8456-lazy-import-cython-rebase-4.6.patch and 8456-lazy-import-enhancements-4.6.patch",
    "created_at": "2010-12-04T19:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76107",
    "user": "robertwb"
}
```

{{__cmp__}} does have a test. 

The buildbot needs to know to apply 8456-lazy-import-cython-rebase-4.6.patch and 8456-lazy-import-enhancements-4.6.patch



---

archive/issue_comments_076108.json:
```json
{
    "body": "I may be misunderstanding, since ther is also a __richcmp__ method and __cmp__ method is not used, but I see the following code:\n\n\n```\n    def __cmp__(left, right):\n        \"\"\"\n        TESTS::\n        \n            sage: lazy_import('sage.all', 'ZZ'); lazy_ZZ = ZZ\n        \"\"\"\n        return binop(cmp, left, right)\n```\n",
    "created_at": "2010-12-05T12:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76108",
    "user": "lftabera"
}
```

I may be misunderstanding, since ther is also a __richcmp__ method and __cmp__ method is not used, but I see the following code:


```
    def __cmp__(left, right):
        """
        TESTS::
        
            sage: lazy_import('sage.all', 'ZZ'); lazy_ZZ = ZZ
        """
        return binop(cmp, left, right)
```




---

archive/issue_comments_076109.json:
```json
{
    "body": "No, you're absolutely right, that (half) doctest is an oversight on my part.",
    "created_at": "2010-12-05T12:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76109",
    "user": "robertwb"
}
```

No, you're absolutely right, that (half) doctest is an oversight on my part.



---

archive/issue_comments_076110.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-12-07T10:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76110",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_076111.json:
```json
{
    "body": "I've updated the patch.",
    "created_at": "2010-12-07T10:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76111",
    "user": "robertwb"
}
```

I've updated the patch.



---

archive/issue_comments_076112.json:
```json
{
    "body": "The code looks right so I give it a positive review.\n\nHowever, I upload a patch to add some minor documentation explaining the parameters of lazy_import. \nRobert, could you please review and check that I did not make a mistake?",
    "created_at": "2010-12-16T20:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76112",
    "user": "lftabera"
}
```

The code looks right so I give it a positive review.

However, I upload a patch to add some minor documentation explaining the parameters of lazy_import. 
Robert, could you please review and check that I did not make a mistake?



---

archive/issue_comments_076113.json:
```json
{
    "body": "Your documentation is correct, thanks.",
    "created_at": "2010-12-17T22:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76113",
    "user": "robertwb"
}
```

Your documentation is correct, thanks.



---

archive/issue_comments_076114.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-17T22:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76114",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076115.json:
```json
{
    "body": "Please check Sphinx syntax\n\n```\ndocstring of sage.misc.lazy_import.get_star_imports:1: (WARNING/2) Inline emphasis start-string without end-string.\n```\n",
    "created_at": "2011-01-24T16:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76115",
    "user": "jdemeyer"
}
```

Please check Sphinx syntax

```
docstring of sage.misc.lazy_import.get_star_imports:1: (WARNING/2) Inline emphasis start-string without end-string.
```




---

archive/issue_comments_076116.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-24T16:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76116",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076117.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-25T07:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76117",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076118.json:
```json
{
    "body": "Attachment\n\nI've refreshed the documentation patch to escape this asterisk.",
    "created_at": "2011-01-25T07:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76118",
    "user": "robertwb"
}
```

Attachment

I've refreshed the documentation patch to escape this asterisk.



---

archive/issue_comments_076119.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-25T18:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76119",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076120.json:
```json
{
    "body": "I'm re-instating the positive review, as adding the asterisk escape was a superficial change.",
    "created_at": "2011-01-25T18:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76120",
    "user": "robertwb"
}
```

I'm re-instating the positive review, as adding the asterisk escape was a superficial change.



---

archive/issue_comments_076121.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-26T22:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8456#issuecomment-76121",
    "user": "jdemeyer"
}
```

Resolution: fixed
