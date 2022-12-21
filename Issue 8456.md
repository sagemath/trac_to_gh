# Issue 8456: lazy import improvements

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-03-06 08:52:13

Assignee: tbd

CC:  rishi jason rlm

1) Cythonize for speed.
2) Insert original object into namespace on resolution
3) Support import *


---

Attachment


---

Comment by robertwb created at 2010-03-06 09:39:48

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-03-06 09:39:48

I split it up into two patches for easier refereeing. The first simply moves lazy_import.py to lazy_import.pyx.


---

Comment by SimonKing created at 2010-03-19 10:48:41

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

Comment by SimonKing created at 2010-03-19 10:48:41

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-03-19 10:50:47

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

Comment by robertwb created at 2010-03-19 17:31:58

Hmm... is this on top of an alpha? Worked fine for me. 

As for backing out, you can do "sage -hg rollback"


---

Attachment


---

Comment by robertwb created at 2010-06-22 20:46:37

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-06-22 20:46:37

OK, the problem was I was using os.rename rather than, say, shutil.move, which caused errors when the DOT_SAGE file was not on the same filesystem as temp files. Glad you caught that, ready for another review.


---

Comment by mpatel created at 2010-08-20 01:26:55

Simon, could you look at this again, when it's convenient?  I can try to review this, but I'm not sure that I'm sufficiently familiar with Cython.

For me, all three patches apply cleanly to 4.5.3.alpha1 (using a Mercurial queue).


---

Comment by robertwb created at 2010-10-20 05:27:52

Lots of people want to see a faster Sage startup; is anyone willing to review this?


---

Comment by lftabera created at 2010-11-04 12:33:56

rebase 8456-lazy-import-cython.patch to sage 4.6

patches apply and doctest pass. The code looks ok, but I do not know (yet) cython nor python introspection to give a positive review.


---

Comment by lftabera created at 2010-11-04 15:01:32

Changing status from needs_review to needs_info.


---

Comment by lftabera created at 2010-11-04 15:01:32

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

Comment by robertwb created at 2010-11-04 17:57:32

Changing status from needs_info to needs_work.


---

Comment by robertwb created at 2010-11-04 17:57:32

Hmm... it looks like I need to manually add the typeslot methods, as they don't get forwarded with getattr. Thanks for catching this, I'll post another patch.


---

Comment by robertwb created at 2010-11-07 06:13:53

Apply only 8456-lazy-import-cython-rebase-4.6.patch and 8456-lazy-import-enhancements-4.6.patch. This fixes the issue with `__repr__` and all the other special methods.


---

Comment by robertwb created at 2010-11-07 06:13:53

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-11-26 13:29:03

Replying to [comment:14 robertwb]:
> Apply only 8456-lazy-import-cython-rebase-4.6.patch and 8456-lazy-import-enhancements-4.6.patch. This fixes the issue with `__repr__` and all the other special methods. 

Are you sure that's right?


```
rlmill`@`fermat:~/sage-4.6.1.alpha2/devel/sage-main$ hg qpush
applying 8456-lazy-import-cython-rebase-4.6.patch
unable to find 'sage/misc/lazy_import.pyx' for patching
8 out of 8 hunks FAILED -- saving rejects to file sage/misc/lazy_import.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 8456-lazy-import-cython-rebase-4.6.patch
```



---

Comment by rlm created at 2010-11-26 13:29:03

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-11-26 16:45:34

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-11-26 16:45:34

Sorry, I missed the dependency... :/


---

Attachment

apply instead of 8456-lazy-import-cython.patch


---

Comment by lftabera created at 2010-12-04 17:00:44

The code looks good. Is there a reason why _cmp_ does not have a test?


---

Comment by robertwb created at 2010-12-04 19:08:56

{{__cmp__}} does have a test. 

The buildbot needs to know to apply 8456-lazy-import-cython-rebase-4.6.patch and 8456-lazy-import-enhancements-4.6.patch


---

Comment by lftabera created at 2010-12-05 12:35:23

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

Comment by robertwb created at 2010-12-05 12:44:17

No, you're absolutely right, that (half) doctest is an oversight on my part.


---

Attachment


---

Comment by robertwb created at 2010-12-07 10:22:34

I've updated the patch.


---

Comment by lftabera created at 2010-12-16 20:53:33

The code looks right so I give it a positive review.

However, I upload a patch to add some minor documentation explaining the parameters of lazy_import. 
Robert, could you please review and check that I did not make a mistake?


---

Comment by robertwb created at 2010-12-17 22:39:06

Your documentation is correct, thanks.


---

Comment by robertwb created at 2010-12-17 22:39:06

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-24 16:45:02

Please check Sphinx syntax

```
docstring of sage.misc.lazy_import.get_star_imports:1: (WARNING/2) Inline emphasis start-string without end-string.
```



---

Comment by jdemeyer created at 2011-01-24 16:45:02

Changing status from positive_review to needs_work.


---

Comment by robertwb created at 2011-01-25 07:00:59

Changing status from needs_work to needs_review.


---

Attachment

I've refreshed the documentation patch to escape this asterisk.


---

Comment by robertwb created at 2011-01-25 18:24:31

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2011-01-25 18:24:31

I'm re-instating the positive review, as adding the asterisk escape was a superficial change.


---

Comment by jdemeyer created at 2011-01-26 22:26:28

Resolution: fixed
