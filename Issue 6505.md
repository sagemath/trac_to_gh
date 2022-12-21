# Issue 6505: [with patch, needs review] Sage banner: include warning if a prerelease

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-07-10 02:39:31

Assignee: jhpalmieri

CC:  drkirby

From [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/b3e57f934ee83c79):

```
I just noticed an old thread, where a user had problems on squite, 
making his own version of some packages with an alpha, heta or rc 
release of Sage. 

It would be good if alpha/beta/rc releases always showed a message that 
they were pre-release versions for developers and not considered stable. 
If there was some automatic way of making this happen, it would avoid 
the risk of someone forgetting to add or delete a file. 
```

This patch should do this.  To fully test, make a source distribution of Sage using sage-sdist.  To partially test, in Sage, do

```
sage: sage.version.version
'4.1.rc1'
sage: print sage.misc.banner.banner_text()
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage.version.version = '4.1'
sage: print sage.misc.banner.banner_text()
----------------------------------------------------------------------
----------------------------------------------------------------------
```

I believe that when a Sage distribution is created, the string from `banner_text()` is printed into the file SAGE_ROOT/local/bin/sage-banner (see SAGE_ROOT/local/bin/sage-sdist).  So I think this patch will do what was requested.


---

Comment by mhampton created at 2009-07-10 04:26:17

The change of tiny to some sort of float value seems kind of odd, could this be avoided somehow? 

119	 	    {'major': 3, 'minor': 2, 'tiny': 1.2, 'prerelease': False}. 
 	125	    {'major': 3, 'minor': 2, 'tiny': 1.200..., 'prerelease': False}.


---

Comment by ddrake created at 2009-07-16 06:17:37

Replying to [comment:4 mhampton]:
> 
> The change of tiny to some sort of float value seems kind of odd, could this be avoided somehow? 
> 
> 119	 	    {'major': 3, 'minor': 2, 'tiny': 1.2, 'prerelease': False}. 
>  	125	    {'major': 3, 'minor': 2, 'tiny': 1.200..., 'prerelease': False}. 

I agree that's a bit weird, but when we do really 'use' the value of `tiny`? If we just print it, it should be fine; even when there's some actual comparisons being done, I think there won't be any trouble with the floating point numbers. I'll think about this some more, but it seems okay to me.

BTW, I'm working on reviewing this.


---

Comment by ddrake created at 2009-07-16 11:39:59

This patch looks good, but I did try to use `-sdist` and am having some problems. I'm not sure if the problem is with the patch or with my use of -sdist. (Almost certainly the latter!)

I compiled a source tarball (4.1.rc1), applied the patch (with mq), did a qfinish to get the patch into the regular history, and then tried `./sage -sdist 4.1.rc2` to try and make a fictional rc2 to see if, after compiling, I got the correct banner.

The sdist script spit out some strange errors, but did create a tarball. I'm compiling that tarball now, but local/bin/sage-banner is an empty file!

Also, doing an sdist leaves behind a zombie tree: it looks like it's there, but if you try to run Sage, it doesn't work. This is because of #1065 (!) but even if I do a `sage -b`, when I rerun Sage, I don't get a banner...which is worrisome since that's what this ticket is about.

I do notice that when I try to emulate the `sage-sdist` script and run the line that sets the banner, this happens. This is from a "`sage -sh`" shell:

```
rake`@`sage.math:/scratch/drake/sage-4.1.rc1/local/bin$ echo "import sage.misc.banner; sage.misc.banner.banner()" | ./python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/misc/banner.py", line 95, in banner
    print banner_text() 
  File "/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/misc/banner.py", line 68, in banner_text
    pre = version_dict()['prerelease']
  File "/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/misc/banner.py", line 136, in version_dict
    from sage.rings.integer import Integer
  File "integer.pyx", line 156, in sage.rings.integer (sage/rings/integer.c:31017)
  File "/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/rings/infinity.py", line 200, in <module>
    import sage.rings.rational
  File "rational.pyx", line 70, in sage.rings.rational (sage/rings/rational.c:23686)
  File "real_mpfr.pyx", line 1, in sage.rings.real_mpfr (sage/rings/real_mpfr.c:29109)
  File "complex_number.pxd", line 8, in sage.libs.mpmath.utils (sage/libs/mpmath/utils.c:5273)
  File "complex_double.pxd", line 13, in sage.rings.complex_number (sage/rings/complex_number.c:14050)
  File "complex_double.pyx", line 88, in sage.rings.complex_double (sage/rings/complex_double.c:13486)
  File "/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/rings/complex_field.py", line 86, in ComplexField
    C = ComplexField_class(prec)
  File "/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/rings/complex_field.py", line 175, in __init__
    ParentWithGens.__init__(self, self._real_field(), ('I',), False)
  File "/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/rings/complex_field.py", line 228, in _real_field
    self.__real_field = real_mpfr.RealField_constructor(self._prec)
  File "real_mpfr.pyx", line 244, in sage.rings.real_mpfr.RealField_constructor (sage/rings/real_mpfr.c:3853)
TypeError: 'NoneType' object is unsubscriptable
```

Looks like something fishy in the bit of code that makes the version dictionary. I'll look at this more later, if no one beats to me. BTW, this did pass doctests, so either something is really goofy about the environment above, or we a fix and a new doctest.


---

Comment by ddrake created at 2009-07-17 11:34:57

Okay, I took a 4.1.rc1 source tarball, compiled it, make a little change, then sdisted it...and it appears to work fine. No significant error messages, and I think the resulting sage-banner file works. So there's something going on with this patch.

BTW, above I meant to end with "or we _need_ a fix and a new doctest."


---

Comment by jhpalmieri created at 2009-07-19 17:43:00

Here is a new version of the patch which doesn't give me this error message.


---

Attachment


---

Comment by jhpalmieri created at 2009-07-19 17:49:13

Replying to [comment:5 ddrake]:
> Replying to [comment:4 mhampton]:
> > 
> > The change of tiny to some sort of float value seems kind of odd, could this be avoided somehow? 
> > 
> > 119	 	    {'major': 3, 'minor': 2, 'tiny': 1.2, 'prerelease': False}. 
> >  	125	    {'major': 3, 'minor': 2, 'tiny': 1.200..., 'prerelease': False}. 
> 
> I agree that's a bit weird, but when we do really 'use' the value of `tiny`? If we just print it, it should be fine; even when there's some actual comparisons being done, I think there won't be any trouble with the floating point numbers. I'll think about this some more, but it seems okay to me.

Right: I think in recent history, `tiny` has been an integer, and in this case it prints like an integer.  Allowing it to have digits beyond the decimal point is "just in case".  If it is a float, we can print it when needed with as many decimal places as we want.


---

Comment by ddrake created at 2009-07-20 05:15:44

I'll try to look at the new patch soon. I'm now at a conference and may not have a lot of time, but at the end of this week, the conference will transmogrify into "*-combinat" (http://wiki.sagemath.org/combinat/FPSAC09) so I'll definitely be able to devote time to reviewing by then.


---

Comment by ddrake created at 2009-07-26 09:43:04

Positive review. This took me a while, since I didn't really know how to use -sdist, but it does work as advertised.


---

Comment by mvngu created at 2009-07-27 08:11:36

Resolution: fixed
