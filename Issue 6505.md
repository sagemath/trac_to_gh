# Issue 6505: [with patch, needs review] Sage banner: include warning if a prerelease

archive/issues_006505.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nCC:  drkirby\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/b3e57f934ee83c79):\n\n```\nI just noticed an old thread, where a user had problems on squite, \nmaking his own version of some packages with an alpha, heta or rc \nrelease of Sage. \n\nIt would be good if alpha/beta/rc releases always showed a message that \nthey were pre-release versions for developers and not considered stable. \nIf there was some automatic way of making this happen, it would avoid \nthe risk of someone forgetting to add or delete a file. \n```\n\nThis patch should do this.  To fully test, make a source distribution of Sage using sage-sdist.  To partially test, in Sage, do\n\n```\nsage: sage.version.version\n'4.1.rc1'\nsage: print sage.misc.banner.banner_text()\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage.version.version = '4.1'\nsage: print sage.misc.banner.banner_text()\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n```\n\nI believe that when a Sage distribution is created, the string from `banner_text()` is printed into the file SAGE_ROOT/local/bin/sage-banner (see SAGE_ROOT/local/bin/sage-sdist).  So I think this patch will do what was requested.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6505\n\n",
    "created_at": "2009-07-10T02:39:31Z",
    "labels": [
        "misc",
        "trivial",
        "enhancement"
    ],
    "title": "[with patch, needs review] Sage banner: include warning if a prerelease",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6505",
    "user": "jhpalmieri"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/6505





---

archive/issue_comments_052994.json:
```json
{
    "body": "The change of tiny to some sort of float value seems kind of odd, could this be avoided somehow? \n\n119\t \t    {'major': 3, 'minor': 2, 'tiny': 1.2, 'prerelease': False}. \n \t125\t    {'major': 3, 'minor': 2, 'tiny': 1.200..., 'prerelease': False}.",
    "created_at": "2009-07-10T04:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6505#issuecomment-52994",
    "user": "mhampton"
}
```

The change of tiny to some sort of float value seems kind of odd, could this be avoided somehow? 

119	 	    {'major': 3, 'minor': 2, 'tiny': 1.2, 'prerelease': False}. 
 	125	    {'major': 3, 'minor': 2, 'tiny': 1.200..., 'prerelease': False}.



---

archive/issue_comments_052995.json:
```json
{
    "body": "Replying to [comment:4 mhampton]:\n> \n> The change of tiny to some sort of float value seems kind of odd, could this be avoided somehow? \n> \n> 119\t \t    {'major': 3, 'minor': 2, 'tiny': 1.2, 'prerelease': False}. \n>  \t125\t    {'major': 3, 'minor': 2, 'tiny': 1.200..., 'prerelease': False}. \n\nI agree that's a bit weird, but when we do really 'use' the value of `tiny`? If we just print it, it should be fine; even when there's some actual comparisons being done, I think there won't be any trouble with the floating point numbers. I'll think about this some more, but it seems okay to me.\n\nBTW, I'm working on reviewing this.",
    "created_at": "2009-07-16T06:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6505#issuecomment-52995",
    "user": "ddrake"
}
```

Replying to [comment:4 mhampton]:
> 
> The change of tiny to some sort of float value seems kind of odd, could this be avoided somehow? 
> 
> 119	 	    {'major': 3, 'minor': 2, 'tiny': 1.2, 'prerelease': False}. 
>  	125	    {'major': 3, 'minor': 2, 'tiny': 1.200..., 'prerelease': False}. 

I agree that's a bit weird, but when we do really 'use' the value of `tiny`? If we just print it, it should be fine; even when there's some actual comparisons being done, I think there won't be any trouble with the floating point numbers. I'll think about this some more, but it seems okay to me.

BTW, I'm working on reviewing this.



---

archive/issue_comments_052996.json:
```json
{
    "body": "This patch looks good, but I did try to use `-sdist` and am having some problems. I'm not sure if the problem is with the patch or with my use of -sdist. (Almost certainly the latter!)\n\nI compiled a source tarball (4.1.rc1), applied the patch (with mq), did a qfinish to get the patch into the regular history, and then tried `./sage -sdist 4.1.rc2` to try and make a fictional rc2 to see if, after compiling, I got the correct banner.\n\nThe sdist script spit out some strange errors, but did create a tarball. I'm compiling that tarball now, but local/bin/sage-banner is an empty file!\n\nAlso, doing an sdist leaves behind a zombie tree: it looks like it's there, but if you try to run Sage, it doesn't work. This is because of #1065 (!) but even if I do a `sage -b`, when I rerun Sage, I don't get a banner...which is worrisome since that's what this ticket is about.\n\nI do notice that when I try to emulate the `sage-sdist` script and run the line that sets the banner, this happens. This is from a \"`sage -sh`\" shell:\n\n```\nrake@sage.math:/scratch/drake/sage-4.1.rc1/local/bin$ echo \"import sage.misc.banner; sage.misc.banner.banner()\" | ./python\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/misc/banner.py\", line 95, in banner\n    print banner_text() \n  File \"/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/misc/banner.py\", line 68, in banner_text\n    pre = version_dict()['prerelease']\n  File \"/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/misc/banner.py\", line 136, in version_dict\n    from sage.rings.integer import Integer\n  File \"integer.pyx\", line 156, in sage.rings.integer (sage/rings/integer.c:31017)\n  File \"/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/rings/infinity.py\", line 200, in <module>\n    import sage.rings.rational\n  File \"rational.pyx\", line 70, in sage.rings.rational (sage/rings/rational.c:23686)\n  File \"real_mpfr.pyx\", line 1, in sage.rings.real_mpfr (sage/rings/real_mpfr.c:29109)\n  File \"complex_number.pxd\", line 8, in sage.libs.mpmath.utils (sage/libs/mpmath/utils.c:5273)\n  File \"complex_double.pxd\", line 13, in sage.rings.complex_number (sage/rings/complex_number.c:14050)\n  File \"complex_double.pyx\", line 88, in sage.rings.complex_double (sage/rings/complex_double.c:13486)\n  File \"/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/rings/complex_field.py\", line 86, in ComplexField\n    C = ComplexField_class(prec)\n  File \"/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/rings/complex_field.py\", line 175, in __init__\n    ParentWithGens.__init__(self, self._real_field(), ('I',), False)\n  File \"/scratch/drake/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/rings/complex_field.py\", line 228, in _real_field\n    self.__real_field = real_mpfr.RealField_constructor(self._prec)\n  File \"real_mpfr.pyx\", line 244, in sage.rings.real_mpfr.RealField_constructor (sage/rings/real_mpfr.c:3853)\nTypeError: 'NoneType' object is unsubscriptable\n```\n\nLooks like something fishy in the bit of code that makes the version dictionary. I'll look at this more later, if no one beats to me. BTW, this did pass doctests, so either something is really goofy about the environment above, or we a fix and a new doctest.",
    "created_at": "2009-07-16T11:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6505#issuecomment-52996",
    "user": "ddrake"
}
```

This patch looks good, but I did try to use `-sdist` and am having some problems. I'm not sure if the problem is with the patch or with my use of -sdist. (Almost certainly the latter!)

I compiled a source tarball (4.1.rc1), applied the patch (with mq), did a qfinish to get the patch into the regular history, and then tried `./sage -sdist 4.1.rc2` to try and make a fictional rc2 to see if, after compiling, I got the correct banner.

The sdist script spit out some strange errors, but did create a tarball. I'm compiling that tarball now, but local/bin/sage-banner is an empty file!

Also, doing an sdist leaves behind a zombie tree: it looks like it's there, but if you try to run Sage, it doesn't work. This is because of #1065 (!) but even if I do a `sage -b`, when I rerun Sage, I don't get a banner...which is worrisome since that's what this ticket is about.

I do notice that when I try to emulate the `sage-sdist` script and run the line that sets the banner, this happens. This is from a "`sage -sh`" shell:

```
rake@sage.math:/scratch/drake/sage-4.1.rc1/local/bin$ echo "import sage.misc.banner; sage.misc.banner.banner()" | ./python
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

archive/issue_comments_052997.json:
```json
{
    "body": "Okay, I took a 4.1.rc1 source tarball, compiled it, make a little change, then sdisted it...and it appears to work fine. No significant error messages, and I think the resulting sage-banner file works. So there's something going on with this patch.\n\nBTW, above I meant to end with \"or we *need* a fix and a new doctest.\"",
    "created_at": "2009-07-17T11:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6505#issuecomment-52997",
    "user": "ddrake"
}
```

Okay, I took a 4.1.rc1 source tarball, compiled it, make a little change, then sdisted it...and it appears to work fine. No significant error messages, and I think the resulting sage-banner file works. So there's something going on with this patch.

BTW, above I meant to end with "or we *need* a fix and a new doctest."



---

archive/issue_comments_052998.json:
```json
{
    "body": "Here is a new version of the patch which doesn't give me this error message.",
    "created_at": "2009-07-19T17:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6505#issuecomment-52998",
    "user": "jhpalmieri"
}
```

Here is a new version of the patch which doesn't give me this error message.



---

archive/issue_comments_052999.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-07-19T17:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6505#issuecomment-52999",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_053000.json:
```json
{
    "body": "Replying to [comment:5 ddrake]:\n> Replying to [comment:4 mhampton]:\n> > \n> > The change of tiny to some sort of float value seems kind of odd, could this be avoided somehow? \n> > \n> > 119\t \t    {'major': 3, 'minor': 2, 'tiny': 1.2, 'prerelease': False}. \n> >  \t125\t    {'major': 3, 'minor': 2, 'tiny': 1.200..., 'prerelease': False}. \n> \n> I agree that's a bit weird, but when we do really 'use' the value of `tiny`? If we just print it, it should be fine; even when there's some actual comparisons being done, I think there won't be any trouble with the floating point numbers. I'll think about this some more, but it seems okay to me.\n\nRight: I think in recent history, `tiny` has been an integer, and in this case it prints like an integer.  Allowing it to have digits beyond the decimal point is \"just in case\".  If it is a float, we can print it when needed with as many decimal places as we want.",
    "created_at": "2009-07-19T17:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6505#issuecomment-53000",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_053001.json:
```json
{
    "body": "I'll try to look at the new patch soon. I'm now at a conference and may not have a lot of time, but at the end of this week, the conference will transmogrify into \"*-combinat\" (http://wiki.sagemath.org/combinat/FPSAC09) so I'll definitely be able to devote time to reviewing by then.",
    "created_at": "2009-07-20T05:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6505#issuecomment-53001",
    "user": "ddrake"
}
```

I'll try to look at the new patch soon. I'm now at a conference and may not have a lot of time, but at the end of this week, the conference will transmogrify into "*-combinat" (http://wiki.sagemath.org/combinat/FPSAC09) so I'll definitely be able to devote time to reviewing by then.



---

archive/issue_comments_053002.json:
```json
{
    "body": "Positive review. This took me a while, since I didn't really know how to use -sdist, but it does work as advertised.",
    "created_at": "2009-07-26T09:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6505#issuecomment-53002",
    "user": "ddrake"
}
```

Positive review. This took me a while, since I didn't really know how to use -sdist, but it does work as advertised.



---

archive/issue_comments_053003.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-27T08:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6505#issuecomment-53003",
    "user": "mvngu"
}
```

Resolution: fixed
