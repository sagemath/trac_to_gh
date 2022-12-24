# Issue 9807: Upgrade numpy to 1.5b and scipy to 0.8

archive/issues_009807.json:
```json
{
    "body": "Assignee: maldun\n\nKeywords: numpy, scipy\n\nSince I really, really need them for my work, I will try to manage it to upgrade the scipy and numpy packages to the latest versions\n\nIssue created by migration from https://trac.sagemath.org/ticket/9808\n\n",
    "created_at": "2010-08-26T19:10:38Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Upgrade numpy to 1.5b and scipy to 0.8",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9807",
    "user": "maldun"
}
```
Assignee: maldun

Keywords: numpy, scipy

Since I really, really need them for my work, I will try to manage it to upgrade the scipy and numpy packages to the latest versions

Issue created by migration from https://trac.sagemath.org/ticket/9808





---

archive/issue_comments_096420.json:
```json
{
    "body": "I have now workable spkg files for the both packages.\nScipy worked well.\nNumpy need some work, but it's functioning.\n\nI host the files at megaupload, at:\nNumpy: http://www.megaupload.com/?d=6GCFZD65 \nScipy: http://www.megaupload.com/?d=JORT40DK\n\nI think the problem is the same as described in Trac # 7791 (http://trac.sagemath.org/sage_trac/ticket/7791 )\n\nI get the following errors:\n\n\n```\n/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/plot/all.py:22: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility\n  from complex_plot import complex_plot\n/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/plot/all.py:22: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility\n  from complex_plot import complex_plot\n/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_plot3d.py:5: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility\n  from implicit_surface import ImplicitSurface\n/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_plot3d.py:5: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility\n  from implicit_surface import ImplicitSurface\n/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/calculus/all.py:17: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility\n  from riemann import Riemann_Map\n/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/calculus/all.py:17: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility\n  from riemann import Riemann_Map\n/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/calculus/all.py:19: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility\n  from interpolators import polygon_spline, complex_cubic_spline\n/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/calculus/all.py:19: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility\n  from interpolators import polygon_spline, complex_cubic_spline\n/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/stats/hmm/all.py:8: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility\n  from hmm  import DiscreteHiddenMarkovModel\n/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/stats/hmm/all.py:8: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility\n  from hmm  import DiscreteHiddenMarkovModel\n```\n\n\nWhat's this? \nHas someone hardcoded the sizes of the routines?",
    "created_at": "2010-08-26T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96420",
    "user": "maldun"
}
```

I have now workable spkg files for the both packages.
Scipy worked well.
Numpy need some work, but it's functioning.

I host the files at megaupload, at:
Numpy: http://www.megaupload.com/?d=6GCFZD65 
Scipy: http://www.megaupload.com/?d=JORT40DK

I think the problem is the same as described in Trac # 7791 (http://trac.sagemath.org/sage_trac/ticket/7791 )

I get the following errors:


```
/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/plot/all.py:22: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from complex_plot import complex_plot
/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/plot/all.py:22: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from complex_plot import complex_plot
/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_plot3d.py:5: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from implicit_surface import ImplicitSurface
/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_plot3d.py:5: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from implicit_surface import ImplicitSurface
/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/calculus/all.py:17: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from riemann import Riemann_Map
/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/calculus/all.py:17: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from riemann import Riemann_Map
/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/calculus/all.py:19: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from interpolators import polygon_spline, complex_cubic_spline
/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/calculus/all.py:19: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from interpolators import polygon_spline, complex_cubic_spline
/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/stats/hmm/all.py:8: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from hmm  import DiscreteHiddenMarkovModel
/home/maldun/sage/sage-4.5.2/local/lib/python2.6/site-packages/sage/stats/hmm/all.py:8: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from hmm  import DiscreteHiddenMarkovModel
```


What's this? 
Has someone hardcoded the sizes of the routines?



---

archive/issue_comments_096421.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-26T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96421",
    "user": "maldun"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_096422.json:
```json
{
    "body": "numpy 1.5.0rc1: http://www.megaupload.com/?d=KK31RSZV",
    "created_at": "2010-08-26T23:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96422",
    "user": "maldun"
}
```

numpy 1.5.0rc1: http://www.megaupload.com/?d=KK31RSZV



---

archive/issue_comments_096423.json:
```json
{
    "body": "I don't think that we should upgrade to 1.5.0rc1 -- we should do 1.4.1 for now and wait until 1.5 is released.",
    "created_at": "2010-08-27T03:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96423",
    "user": "@mwhansen"
}
```

I don't think that we should upgrade to 1.5.0rc1 -- we should do 1.4.1 for now and wait until 1.5 is released.



---

archive/issue_comments_096424.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> I don't think that we should upgrade to 1.5.0rc1 -- we should do 1.4.1 for now and wait until 1.5 is released.\n\nThat has to be double checked but maldun says he needs features in 1.5.\nIt may be that the features he wants are 1.4.x and he doesn't know.\nDo we know roughly when 1.5 will be released? They are at 1.5rc1 9 days after beta2\nso it could very well be upon us in a very short time.",
    "created_at": "2010-08-27T04:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96424",
    "user": "@kiwifb"
}
```

Replying to [comment:3 mhansen]:
> I don't think that we should upgrade to 1.5.0rc1 -- we should do 1.4.1 for now and wait until 1.5 is released.

That has to be double checked but maldun says he needs features in 1.5.
It may be that the features he wants are 1.4.x and he doesn't know.
Do we know roughly when 1.5 will be released? They are at 1.5rc1 9 days after beta2
so it could very well be upon us in a very short time.



---

archive/issue_comments_096425.json:
```json
{
    "body": "The warnings go away after rebuilding the source.\nAnd the doctests only throw warnings but there don't seem to be errors, and the output is\ncorrect\n\n`@`mhansen, fbissey\nI think numpy has the same issues since version 1.4.\nand I'm quite sure that resolving it in 1.5.0rc1 would, solve the problem\nwith 1.4.1. too. (and perhaps also with 1.5. later)\nSo I suggest the following procedure:\nI solve the issues with the latest. Dobule check if 1.4.1 also works, and we decide then\nwhich of the versions we keep, or for example keep 1.4.1 in standard and 1.5.0rc1 as experimental",
    "created_at": "2010-08-27T07:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96425",
    "user": "maldun"
}
```

The warnings go away after rebuilding the source.
And the doctests only throw warnings but there don't seem to be errors, and the output is
correct

`@`mhansen, fbissey
I think numpy has the same issues since version 1.4.
and I'm quite sure that resolving it in 1.5.0rc1 would, solve the problem
with 1.4.1. too. (and perhaps also with 1.5. later)
So I suggest the following procedure:
I solve the issues with the latest. Dobule check if 1.4.1 also works, and we decide then
which of the versions we keep, or for example keep 1.4.1 in standard and 1.5.0rc1 as experimental



---

archive/issue_comments_096426.json:
```json
{
    "body": "If 1.5.0rc1 is merged, #7166 can be closed. I don't know about 1.4.1, but in any case that is not a critical bug. \n\nSome time back I made a Solaris-specific change to Numpy, as I wanted to get it reviewed with the least hassle - that generally means making it Solaris specific, as reviewers are easier to please if it only effects a rarer platform. \n\nBut I think the change should be implemented on OS X too. Currently there's a really nasty hack on OS X to build Numpy, that involves a script called `fake_gcc`, copying that to `$SAGE/LOCAL/bin/gcc`, then using the fake gcc to build Numpy. Finally this fake gcc file gets deleted. \n\nThe far neater option is the way I did it on Solaris. I suggest the changes I made for Solaris are implemented whenever `SAGE64` is set to \"yes\", irrespective of whatever platform it may be. Then all this fake gcc rubbish can be removed. \n\nIf you want, I can create a patch.",
    "created_at": "2010-08-27T11:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96426",
    "user": "drkirkby"
}
```

If 1.5.0rc1 is merged, #7166 can be closed. I don't know about 1.4.1, but in any case that is not a critical bug. 

Some time back I made a Solaris-specific change to Numpy, as I wanted to get it reviewed with the least hassle - that generally means making it Solaris specific, as reviewers are easier to please if it only effects a rarer platform. 

But I think the change should be implemented on OS X too. Currently there's a really nasty hack on OS X to build Numpy, that involves a script called `fake_gcc`, copying that to `$SAGE/LOCAL/bin/gcc`, then using the fake gcc to build Numpy. Finally this fake gcc file gets deleted. 

The far neater option is the way I did it on Solaris. I suggest the changes I made for Solaris are implemented whenever `SAGE64` is set to "yes", irrespective of whatever platform it may be. Then all this fake gcc rubbish can be removed. 

If you want, I can create a patch.



---

archive/issue_comments_096427.json:
```json
{
    "body": "Replying to [comment:6 drkirkby]:\n \n> \n> If you want, I can create a patch. \n\nwould be nice! But first I have to sort some things out, I hope it will get ready soon...",
    "created_at": "2010-08-27T15:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96427",
    "user": "maldun"
}
```

Replying to [comment:6 drkirkby]:
 
> 
> If you want, I can create a patch. 

would be nice! But first I have to sort some things out, I hope it will get ready soon...



---

archive/issue_comments_096428.json:
```json
{
    "body": "Looking at all that stuff in the spkg and comparing to Gentoo. Not very pretty.\nDo we really still need to use sage_fortran? On most platform we now use a native\nfortran compiler rather than a sage shipped one - I don't know if we still do that\nfor OS X.\nIn the patch to gnu.py there is:\n\n```\n+        # Note that sse flags and so on lead to gfortran code that segfaults, so disable arch flags\n+        return opt\n+\n```\n\nAn extract of the Gentoo set up:\n\n```\n\texport NUMPY_FCONFIG=\"config_fc --noopt --noarch\"\n```\n\nActually  here is the full set up that you might find interesting:\n\n```\n\t# See progress in http://projects.scipy.org/scipy/numpy/ticket/573\n\t# with the subtle difference that we don't want to break Darwin where\n\t# -shared is not a valid linker argument\n\tif [[ ${CHOST} != *-darwin* ]] ; then\n\t\tappend-ldflags -shared\n\tfi\n\n\t# only one fortran to link with:\n\t# linking with cblas and lapack library will force\n\t# autodetecting and linking to all available fortran compilers\n\tuse lapack || return\n\t[[ -z ${FC} ]] && FC=$(tc-getFC)\n\t# when fortran flags are set, pic is removed.\n\tFFLAGS=\"${FFLAGS} -fPIC\"\n\texport NUMPY_FCONFIG=\"config_fc --noopt --noarch\"\n```\n\nThe other patches we have are relatively minor, a fix to the f2py man page,\na patch for freebsd - that may be usefull, a patch for interix(!).\nI cannot comment on the cygwin patches but they look very small.\nWe are are a bit more anal with site.cfg, I don't think it is useful in the \ncontext of sage - we just have more complex possible combinations of blas/lapack.\n\nThe NUMPY_FCONFIG is passed to distutils as an argument of \n\n```\npython setup.py install\n```\n\ni.e. in the end what we do boils down to \"python setup.py install ${NUMPY_FCONFIG}\".\n\nCan you point me to your solaris fix Dave?\nI'd like to see if I can tidy all that up in something that requires less patching\nand is more based on FLAGS settings.",
    "created_at": "2010-08-29T11:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96428",
    "user": "@kiwifb"
}
```

Looking at all that stuff in the spkg and comparing to Gentoo. Not very pretty.
Do we really still need to use sage_fortran? On most platform we now use a native
fortran compiler rather than a sage shipped one - I don't know if we still do that
for OS X.
In the patch to gnu.py there is:

```
+        # Note that sse flags and so on lead to gfortran code that segfaults, so disable arch flags
+        return opt
+
```

An extract of the Gentoo set up:

```
	export NUMPY_FCONFIG="config_fc --noopt --noarch"
```

Actually  here is the full set up that you might find interesting:

```
	# See progress in http://projects.scipy.org/scipy/numpy/ticket/573
	# with the subtle difference that we don't want to break Darwin where
	# -shared is not a valid linker argument
	if [[ ${CHOST} != *-darwin* ]] ; then
		append-ldflags -shared
	fi

	# only one fortran to link with:
	# linking with cblas and lapack library will force
	# autodetecting and linking to all available fortran compilers
	use lapack || return
	[[ -z ${FC} ]] && FC=$(tc-getFC)
	# when fortran flags are set, pic is removed.
	FFLAGS="${FFLAGS} -fPIC"
	export NUMPY_FCONFIG="config_fc --noopt --noarch"
```

The other patches we have are relatively minor, a fix to the f2py man page,
a patch for freebsd - that may be usefull, a patch for interix(!).
I cannot comment on the cygwin patches but they look very small.
We are are a bit more anal with site.cfg, I don't think it is useful in the 
context of sage - we just have more complex possible combinations of blas/lapack.

The NUMPY_FCONFIG is passed to distutils as an argument of 

```
python setup.py install
```

i.e. in the end what we do boils down to "python setup.py install ${NUMPY_FCONFIG}".

Can you point me to your solaris fix Dave?
I'd like to see if I can tidy all that up in something that requires less patching
and is more based on FLAGS settings.



---

archive/issue_comments_096429.json:
```json
{
    "body": "Replying to [comment:8 fbissey]:\n> Looking at all that stuff in the spkg and comparing to Gentoo. Not very pretty.\n\nWhat a surprise. \n\n> Do we really still need to use sage_fortran? On most platform we now use a native\n> fortran compiler rather than a sage shipped one - I don't know if we still do that\n> for OS X.\n\nI've never understood the need for this `SAGE_FORTRAN`. I've tried arguing for it to be removed and use `FC` instead, but I had no luck. \n\nA Fortran compiler is still shipped on OS X, but I don't see why the variable `FC` can't be made to point to that, rather than have the variable `SAGE_FORTRAN`. \n\n> Can you point me to your solaris fix Dave?\n> I'd like to see if I can tidy all that up in something that requires less patching\n> and is more based on FLAGS settings.\n\nOn Solaris, and some OS X versions, if you want a 64-bit build, you must add the compiler flag `-m64` with gcc. Usually, putting that in `CFLAGS` is enough. However, for Numpy that does not work. \n\nSomeone came up with a fix for this which was implemented only on OS X, that involved creating a wrapper script called `gcc_fake` which basically calls gcc with the `-m64` option. You can see the script yourself in the top level directory. \n\nSince they had done this only on OS X, it did not work on Solaris. So I came up with a solution for Solaris, but I avoided the wrapper script. Instead I set the variable to `CC=gcc -m64`\n\nI'm attaching a patch, which basically uses the Solaris on any system, including OS X. I think this is the sensible way to do it, not have a wrapper script. \n\n**I've not tested the attached patch** - not even on Solaris!! But I think you can see what I am trying to do. I was going to try to explain it in words, but a bit of code, even if untested, should be more sensible.",
    "created_at": "2010-08-29T13:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96429",
    "user": "drkirkby"
}
```

Replying to [comment:8 fbissey]:
> Looking at all that stuff in the spkg and comparing to Gentoo. Not very pretty.

What a surprise. 

> Do we really still need to use sage_fortran? On most platform we now use a native
> fortran compiler rather than a sage shipped one - I don't know if we still do that
> for OS X.

I've never understood the need for this `SAGE_FORTRAN`. I've tried arguing for it to be removed and use `FC` instead, but I had no luck. 

A Fortran compiler is still shipped on OS X, but I don't see why the variable `FC` can't be made to point to that, rather than have the variable `SAGE_FORTRAN`. 

> Can you point me to your solaris fix Dave?
> I'd like to see if I can tidy all that up in something that requires less patching
> and is more based on FLAGS settings.

On Solaris, and some OS X versions, if you want a 64-bit build, you must add the compiler flag `-m64` with gcc. Usually, putting that in `CFLAGS` is enough. However, for Numpy that does not work. 

Someone came up with a fix for this which was implemented only on OS X, that involved creating a wrapper script called `gcc_fake` which basically calls gcc with the `-m64` option. You can see the script yourself in the top level directory. 

Since they had done this only on OS X, it did not work on Solaris. So I came up with a solution for Solaris, but I avoided the wrapper script. Instead I set the variable to `CC=gcc -m64`

I'm attaching a patch, which basically uses the Solaris on any system, including OS X. I think this is the sensible way to do it, not have a wrapper script. 

**I've not tested the attached patch** - not even on Solaris!! But I think you can see what I am trying to do. I was going to try to explain it in words, but a bit of code, even if untested, should be more sensible.



---

archive/issue_comments_096430.json:
```json
{
    "body": "An untested patch, which makes Numpy build the same was on OS X as it does on Solaris or other platforms where SAGE64=yes. It removes the stupid wrapper script.",
    "created_at": "2010-08-29T13:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96430",
    "user": "drkirkby"
}
```

An untested patch, which makes Numpy build the same was on OS X as it does on Solaris or other platforms where SAGE64=yes. It removes the stupid wrapper script.



---

archive/issue_comments_096431.json:
```json
{
    "body": "Attachment [9808-remove-gcc_fake.patch](tarball://root/attachments/some-uuid/ticket9808/9808-remove-gcc_fake.patch) by @kiwifb created at 2010-08-30 11:56:18\n\nOk - so we still use g95 on some targets. So we need to keep some patches\njust for these - bother.",
    "created_at": "2010-08-30T11:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96431",
    "user": "@kiwifb"
}
```

Attachment [9808-remove-gcc_fake.patch](tarball://root/attachments/some-uuid/ticket9808/9808-remove-gcc_fake.patch) by @kiwifb created at 2010-08-30 11:56:18

Ok - so we still use g95 on some targets. So we need to keep some patches
just for these - bother.



---

archive/issue_comments_096432.json:
```json
{
    "body": "Replying to [comment:10 fbissey]:\n> Ok - so we still use g95 on some targets. So we need to keep some patches\n> just for these - bother.\nI don't believe g95 is used anywhere. There are g95 binaries in the Fortran package in Sage, but William said they can be removed. There is a gfortran binary. So as far as I'm aware, all g95 stuff can be removed, but `SAGE_FORTRAN` can't be removed. \n\nDave",
    "created_at": "2010-08-30T12:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96432",
    "user": "drkirkby"
}
```

Replying to [comment:10 fbissey]:
> Ok - so we still use g95 on some targets. So we need to keep some patches
> just for these - bother.
I don't believe g95 is used anywhere. There are g95 binaries in the Fortran package in Sage, but William said they can be removed. There is a gfortran binary. So as far as I'm aware, all g95 stuff can be removed, but `SAGE_FORTRAN` can't be removed. 

Dave



---

archive/issue_comments_096433.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n> Replying to [comment:10 fbissey]:\n> > Ok - so we still use g95 on some targets. So we need to keep some patches\n> > just for these - bother.\n> I don't believe g95 is used anywhere. There are g95 binaries in the Fortran package in Sage, but William said they can be removed. There is a gfortran binary. So as far as I'm aware, all g95 stuff can be removed, but `SAGE_FORTRAN` can't be removed. \n> \nThat's good! That means we probably can give the shove to the gnu.py and __init__.py\npatches. I wouldn't be sorry to see the back of these.\n\nThere is a comment in SPKG.txt:\n\n```\nSpecial Update/Build Instructions:\n  * The file $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi comes from this file and must be updated if/when \n    the file src/numpy/doc/cython/numpy.pxi is updated.\n```\n\nI cannot find the file in question in that location. There is however a numpy.pxi under src/numpy/random/mtrand but I am not sure that's the file in question.\nFurthermore I don't appear to have a numpy.pxi in $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi .\nDoes anyone know if these instructions are obsolete?",
    "created_at": "2010-08-31T10:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96433",
    "user": "@kiwifb"
}
```

Replying to [comment:11 drkirkby]:
> Replying to [comment:10 fbissey]:
> > Ok - so we still use g95 on some targets. So we need to keep some patches
> > just for these - bother.
> I don't believe g95 is used anywhere. There are g95 binaries in the Fortran package in Sage, but William said they can be removed. There is a gfortran binary. So as far as I'm aware, all g95 stuff can be removed, but `SAGE_FORTRAN` can't be removed. 
> 
That's good! That means we probably can give the shove to the gnu.py and __init__.py
patches. I wouldn't be sorry to see the back of these.

There is a comment in SPKG.txt:

```
Special Update/Build Instructions:
  * The file $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi comes from this file and must be updated if/when 
    the file src/numpy/doc/cython/numpy.pxi is updated.
```

I cannot find the file in question in that location. There is however a numpy.pxi under src/numpy/random/mtrand but I am not sure that's the file in question.
Furthermore I don't appear to have a numpy.pxi in $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi .
Does anyone know if these instructions are obsolete?



---

archive/issue_comments_096434.json:
```json
{
    "body": "FYI: Numpy 1.5 has been officially released now.",
    "created_at": "2010-08-31T16:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96434",
    "user": "@jasongrout"
}
```

FYI: Numpy 1.5 has been officially released now.



---

archive/issue_comments_096435.json:
```json
{
    "body": "Replying to [comment:12 fbissey]:\n> Replying to [comment:11 drkirkby]:\n> > Replying to [comment:10 fbissey]:\n> > > Ok - so we still use g95 on some targets. So we need to keep some patches\n> > > just for these - bother.\n> > I don't believe g95 is used anywhere. There are g95 binaries in the Fortran package in Sage, but William said they can be removed. There is a gfortran binary. So as far as I'm aware, all g95 stuff can be removed, but `SAGE_FORTRAN` can't be removed. \n> > \n> That's good! That means we probably can give the shove to the gnu.py and __init__.py\n> patches. I wouldn't be sorry to see the back of these.\n> \n> There is a comment in SPKG.txt:\n> {{{\n> Special Update/Build Instructions:\n>   * The file $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi comes from this file and must be updated if/when \n>     the file src/numpy/doc/cython/numpy.pxi is updated.\n> }}}\n> I cannot find the file in question in that location. There is however a numpy.pxi under src/numpy/random/mtrand but I am not sure that's the file in question.\n> Furthermore I don't appear to have a numpy.pxi in $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi .\n> Does anyone know if these instructions are obsolete?\n\nI think I was the one that added those instructions, and I'm pretty sure they're obsolete instructions now.  I believe we took care of merging the differences between the two numpy.pxi/pxd files a while ago.",
    "created_at": "2010-08-31T16:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96435",
    "user": "@jasongrout"
}
```

Replying to [comment:12 fbissey]:
> Replying to [comment:11 drkirkby]:
> > Replying to [comment:10 fbissey]:
> > > Ok - so we still use g95 on some targets. So we need to keep some patches
> > > just for these - bother.
> > I don't believe g95 is used anywhere. There are g95 binaries in the Fortran package in Sage, but William said they can be removed. There is a gfortran binary. So as far as I'm aware, all g95 stuff can be removed, but `SAGE_FORTRAN` can't be removed. 
> > 
> That's good! That means we probably can give the shove to the gnu.py and __init__.py
> patches. I wouldn't be sorry to see the back of these.
> 
> There is a comment in SPKG.txt:
> {{{
> Special Update/Build Instructions:
>   * The file $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi comes from this file and must be updated if/when 
>     the file src/numpy/doc/cython/numpy.pxi is updated.
> }}}
> I cannot find the file in question in that location. There is however a numpy.pxi under src/numpy/random/mtrand but I am not sure that's the file in question.
> Furthermore I don't appear to have a numpy.pxi in $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi .
> Does anyone know if these instructions are obsolete?

I think I was the one that added those instructions, and I'm pretty sure they're obsolete instructions now.  I believe we took care of merging the differences between the two numpy.pxi/pxd files a while ago.



---

archive/issue_comments_096436.json:
```json
{
    "body": "Replying to [comment:14 jason]:\n> I think I was the one that added those instructions, and I'm pretty sure they're obsolete instructions now.  I believe we took care of merging the differences between the two numpy.pxi/pxd files a while ago.\n\nThank you for the confirmation. I have done some cleaning to numpy's spkg-install and it seems to work as intended on my machine. I guess we'll update to 1.5 and give it a spin.",
    "created_at": "2010-08-31T23:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96436",
    "user": "@kiwifb"
}
```

Replying to [comment:14 jason]:
> I think I was the one that added those instructions, and I'm pretty sure they're obsolete instructions now.  I believe we took care of merging the differences between the two numpy.pxi/pxd files a while ago.

Thank you for the confirmation. I have done some cleaning to numpy's spkg-install and it seems to work as intended on my machine. I guess we'll update to 1.5 and give it a spin.



---

archive/issue_comments_096437.json:
```json
{
    "body": "Replying to [comment:4 fbissey]:\n> Replying to [comment:3 mhansen]:\n> > I don't think that we should upgrade to 1.5.0rc1 -- we should do 1.4.1 for now and wait until 1.5 is released.\n> \n> That has to be double checked but maldun says he needs features in 1.5.\n> It may be that the features he wants are 1.4.x and he doesn't know.\n> Do we know roughly when 1.5 will be released? They are at 1.5rc1 9 days after beta2\n> so it could very well be upon us in a very short time.\n\nIn general though, we should not be upgrading to pre-release versions just because one person needs a feature that's only available in a pre-release. Everyone should not have to suffer the extra risks a pre-release gives unless there are compelling arguments for it. \n\nI realise in this case 1.5 has since been released, so it's immaterial now. \n\nDave",
    "created_at": "2010-08-31T23:46:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96437",
    "user": "drkirkby"
}
```

Replying to [comment:4 fbissey]:
> Replying to [comment:3 mhansen]:
> > I don't think that we should upgrade to 1.5.0rc1 -- we should do 1.4.1 for now and wait until 1.5 is released.
> 
> That has to be double checked but maldun says he needs features in 1.5.
> It may be that the features he wants are 1.4.x and he doesn't know.
> Do we know roughly when 1.5 will be released? They are at 1.5rc1 9 days after beta2
> so it could very well be upon us in a very short time.

In general though, we should not be upgrading to pre-release versions just because one person needs a feature that's only available in a pre-release. Everyone should not have to suffer the extra risks a pre-release gives unless there are compelling arguments for it. 

I realise in this case 1.5 has since been released, so it's immaterial now. 

Dave



---

archive/issue_comments_096438.json:
```json
{
    "body": "Replying to [comment:16 drkirkby]:\n\n> In general though, we should not be upgrading to pre-release versions just because one person needs a feature that's only available in a pre-release. Everyone should not have to suffer the extra risks a pre-release gives unless there are compelling arguments for it. \n\n\n+1",
    "created_at": "2010-09-01T01:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96438",
    "user": "@jasongrout"
}
```

Replying to [comment:16 drkirkby]:

> In general though, we should not be upgrading to pre-release versions just because one person needs a feature that's only available in a pre-release. Everyone should not have to suffer the extra risks a pre-release gives unless there are compelling arguments for it. 


+1



---

archive/issue_comments_096439.json:
```json
{
    "body": "Replying to [comment:16 drkirkby]:\n> In general though, we should not be upgrading to pre-release versions just because one person needs a feature that's only available in a pre-release. Everyone should not have to suffer the extra risks a pre-release gives unless there are compelling arguments for it. \n> \n> I realise in this case 1.5 has since been released, so it's immaterial now. \n> \nYes, I didn't think it would be worth working on that particular version if it wasn't\nfor the real proximity of the release (curses pari svn upgrade). I would probably\nhave put pressure for 1.4.1 otherwise (very keen to see numpy upgraded).",
    "created_at": "2010-09-01T10:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96439",
    "user": "@kiwifb"
}
```

Replying to [comment:16 drkirkby]:
> In general though, we should not be upgrading to pre-release versions just because one person needs a feature that's only available in a pre-release. Everyone should not have to suffer the extra risks a pre-release gives unless there are compelling arguments for it. 
> 
> I realise in this case 1.5 has since been released, so it's immaterial now. 
> 
Yes, I didn't think it would be worth working on that particular version if it wasn't
for the real proximity of the release (curses pari svn upgrade). I would probably
have put pressure for 1.4.1 otherwise (very keen to see numpy upgraded).



---

archive/issue_comments_096440.json:
```json
{
    "body": "Replying to [comment:13 jason]:\n> FYI: Numpy 1.5 has been officially released now.\n\nSo I was right =) Til I'm done with 1.5.0rc1 1.5 is out...\n\nSo changed so far:\n\nThe following doctest had to be rewritten:\n\n```\nFile \"/home/maldun/sage/sage-4.5.2/devel/sage/doc/en/faq/faq-usage.rst\", line 341:\n    sage: stats.ttest_ind(list([1,2,3,4,5]),list([2,3,4,5,.6]))\nExpected:\n    doctest...DeprecationWarning...\n    (0.076752955645333687, 0.94070490247380478)\nGot:\n    (0.076752955645333687, 0.94070490247380478)\n```\n\nThat was easy =)\n\nThe next prob was:\n\n```\nFile \"/home/maldun/sage/sage-4.5.2/devel/sage/sage/graphs/graph.py\", line 615:\n    sage: Graph(A)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/maldun/sage/sage-4.5.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/maldun/sage/sage-4.5.2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/maldun/sage/sage-4.5.2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[22]>\", line 1, in <module>\n        Graph(A)###line 615:\n    sage: Graph(A)\n      File \"/home/maldun/sage/sage-4.5.2/local/lib/python/site-packages/sage/graphs/graph.py\", line 846, in __init__\n        data = networkx.MultiGraph(data)\n      File \"/home/maldun/sage/sage-4.5.2/local/lib/python2.6/networkx/classes/graph.py\", line 220, in __init__\n        convert.from_whatever(data,create_using=self)\n      File \"/home/maldun/sage/sage-4.5.2/local/lib/python2.6/networkx/convert.py\", line 157, in from_whatever\n        if isinstance(thing,numpy.core.defmatrix.matrix) or \\\n    AttributeError: 'module' object has no attribute 'defmatrix'\n```\n\n\nthat was also easy. defmatrix just changed from numpy.core to numpy.matrix to numpy.matrixlib\nOnly changed that line in /local/lib/python2.6/networkx/classes/graph.py\n\nHere comes now a trickier one: \n\n\n```\n       sage -t -valgrind \"devel/sage/sage/rings/polynomial/polynomial_element.pyx\"\nTotal time for all tests: 716.4 seconds\nmaldun@zauberbuch:~/sage/sage-4.5.2$ sage -t  -valgrind \"devel/sage/sage/rings/polynomial/real_roots.pyx\n> \"\nERROR: File ./devel/sage/sage/rings/polynomial/real_roots.pyx\n is missing\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        ./devel/sage/sage/rings/polynomial/real_roots.pyx\n # File not found\nTotal time for all tests: 0.0 seconds\nmaldun@zauberbuch:~/sage/sage-4.5.2$ sage -t  -valgrind \"devel/sage/sage/rings/polynomial/real_roots.pyx\"\nsage -t -valgrind \"devel/sage/sage/rings/polynomial/real_roots.pyx\"\n**********************************************************************\nFile \"/home/maldun/sage/sage-4.5.2/devel/sage/sage/rings/polynomial/real_roots.pyx\", line 1819, in __main__.example_76\nFailed example:\n    oc.find_roots()###line 3064:_sage_    >>> oc.find_roots()\nExpected nothing\nGot:\n    doctest:1: RuntimeWarning: tp_compare didn't return -1 or -2 for exception\n**********************************************************************\nFile \"/home/maldun/sage/sage-4.5.2/devel/sage/sage/rings/polynomial/real_roots.pyx\", line 1840, in __main__.example_77\nFailed example:\n    oc.find_roots()###line 3085:_sage_    >>> oc.find_roots()\nExpected nothing\nGot:\n    doctest:1: RuntimeWarning: tp_compare didn't return -1 or -2 for exception\n**********************************************************************\nFile \"/home/maldun/sage/sage-4.5.2/devel/sage/sage/rings/polynomial/real_roots.pyx\", line 1934, in __main__.example_80\nFailed example:\n    oc.find_roots()###line 3157:_sage_    >>> oc.find_roots()\nExpected nothing\nGot:\n    doctest:1: RuntimeWarning: tp_compare didn't return -1 or -2 for exception\n**********************************************************************\nFile \"/home/maldun/sage/sage-4.5.2/devel/sage/sage/rings/polynomial/real_roots.pyx\", line 2320, in __main__.example_98\nFailed example:\n    real_roots(x**Integer(5) * (x**Integer(2) - Integer(9999))**Integer(2) - Integer(1))###line 3870:_sage_    >>> real_roots(x^5 * (x^2 - 9999)^2 - 1)\nExpected:\n    [((-29274496381311/9007199254740992, 419601125186091/2251799813685248), 1), ((2126658450145849453951061654415153249597/21267647932558653966460912964485513216, 4253316902721330018853696359533061621799/42535295865117307932921825928971026432), 1), ((1063329226287740282451317352558954186101/10633823966279326983230456482242756608, 531664614358685696701445201630854654353/5316911983139663491615228241121378304), 1)]\nGot:\n    doctest:1: RuntimeWarning: tp_compare didn't return -1 or -2 for exception\n    [((-29274496381311/9007199254740992, 419601125186091/2251799813685248), 1), ((2126658450145849453951061654415153249597/21267647932558653966460912964485513216, 4253316902721330018853696359533061621799/42535295865117307932921825928971026432), 1), ((1063329226287740282451317352558954186101/10633823966279326983230456482242756608, 531664614358685696701445201630854654353/5316911983139663491615228241121378304), 1)]\n**********************************************************************\n4 items had failures:\n   1 of  10 in __main__.example_76\n   1 of   9 in __main__.example_77\n   1 of  10 in __main__.example_80\n   1 of  44 in __main__.example_98\n***Test Failed*** 4 failures.\n         [227.6 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -valgrind \"devel/sage/sage/rings/polynomial/real_roots.pyx\"\nTotal time for all tests: 227.6 seconds\n```\n\n\nThis is not the only one, but the root  of evil seems to be in real_roots (how ironic...)\nmore precisly: I tracked it down, with help of valgrind, to the class ocean. Has anyone an Idea??",
    "created_at": "2010-09-01T18:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96440",
    "user": "maldun"
}
```

Replying to [comment:13 jason]:
> FYI: Numpy 1.5 has been officially released now.

So I was right =) Til I'm done with 1.5.0rc1 1.5 is out...

So changed so far:

The following doctest had to be rewritten:

```
File "/home/maldun/sage/sage-4.5.2/devel/sage/doc/en/faq/faq-usage.rst", line 341:
    sage: stats.ttest_ind(list([1,2,3,4,5]),list([2,3,4,5,.6]))
Expected:
    doctest...DeprecationWarning...
    (0.076752955645333687, 0.94070490247380478)
Got:
    (0.076752955645333687, 0.94070490247380478)
```

That was easy =)

The next prob was:

```
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/graphs/graph.py", line 615:
    sage: Graph(A)
Exception raised:
    Traceback (most recent call last):
      File "/home/maldun/sage/sage-4.5.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/maldun/sage/sage-4.5.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/maldun/sage/sage-4.5.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[22]>", line 1, in <module>
        Graph(A)###line 615:
    sage: Graph(A)
      File "/home/maldun/sage/sage-4.5.2/local/lib/python/site-packages/sage/graphs/graph.py", line 846, in __init__
        data = networkx.MultiGraph(data)
      File "/home/maldun/sage/sage-4.5.2/local/lib/python2.6/networkx/classes/graph.py", line 220, in __init__
        convert.from_whatever(data,create_using=self)
      File "/home/maldun/sage/sage-4.5.2/local/lib/python2.6/networkx/convert.py", line 157, in from_whatever
        if isinstance(thing,numpy.core.defmatrix.matrix) or \
    AttributeError: 'module' object has no attribute 'defmatrix'
```


that was also easy. defmatrix just changed from numpy.core to numpy.matrix to numpy.matrixlib
Only changed that line in /local/lib/python2.6/networkx/classes/graph.py

Here comes now a trickier one: 


```
       sage -t -valgrind "devel/sage/sage/rings/polynomial/polynomial_element.pyx"
Total time for all tests: 716.4 seconds
maldun@zauberbuch:~/sage/sage-4.5.2$ sage -t  -valgrind "devel/sage/sage/rings/polynomial/real_roots.pyx
> "
ERROR: File ./devel/sage/sage/rings/polynomial/real_roots.pyx
 is missing
 
----------------------------------------------------------------------
The following tests failed:


        ./devel/sage/sage/rings/polynomial/real_roots.pyx
 # File not found
Total time for all tests: 0.0 seconds
maldun@zauberbuch:~/sage/sage-4.5.2$ sage -t  -valgrind "devel/sage/sage/rings/polynomial/real_roots.pyx"
sage -t -valgrind "devel/sage/sage/rings/polynomial/real_roots.pyx"
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/rings/polynomial/real_roots.pyx", line 1819, in __main__.example_76
Failed example:
    oc.find_roots()###line 3064:_sage_    >>> oc.find_roots()
Expected nothing
Got:
    doctest:1: RuntimeWarning: tp_compare didn't return -1 or -2 for exception
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/rings/polynomial/real_roots.pyx", line 1840, in __main__.example_77
Failed example:
    oc.find_roots()###line 3085:_sage_    >>> oc.find_roots()
Expected nothing
Got:
    doctest:1: RuntimeWarning: tp_compare didn't return -1 or -2 for exception
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/rings/polynomial/real_roots.pyx", line 1934, in __main__.example_80
Failed example:
    oc.find_roots()###line 3157:_sage_    >>> oc.find_roots()
Expected nothing
Got:
    doctest:1: RuntimeWarning: tp_compare didn't return -1 or -2 for exception
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/rings/polynomial/real_roots.pyx", line 2320, in __main__.example_98
Failed example:
    real_roots(x**Integer(5) * (x**Integer(2) - Integer(9999))**Integer(2) - Integer(1))###line 3870:_sage_    >>> real_roots(x^5 * (x^2 - 9999)^2 - 1)
Expected:
    [((-29274496381311/9007199254740992, 419601125186091/2251799813685248), 1), ((2126658450145849453951061654415153249597/21267647932558653966460912964485513216, 4253316902721330018853696359533061621799/42535295865117307932921825928971026432), 1), ((1063329226287740282451317352558954186101/10633823966279326983230456482242756608, 531664614358685696701445201630854654353/5316911983139663491615228241121378304), 1)]
Got:
    doctest:1: RuntimeWarning: tp_compare didn't return -1 or -2 for exception
    [((-29274496381311/9007199254740992, 419601125186091/2251799813685248), 1), ((2126658450145849453951061654415153249597/21267647932558653966460912964485513216, 4253316902721330018853696359533061621799/42535295865117307932921825928971026432), 1), ((1063329226287740282451317352558954186101/10633823966279326983230456482242756608, 531664614358685696701445201630854654353/5316911983139663491615228241121378304), 1)]
**********************************************************************
4 items had failures:
   1 of  10 in __main__.example_76
   1 of   9 in __main__.example_77
   1 of  10 in __main__.example_80
   1 of  44 in __main__.example_98
***Test Failed*** 4 failures.
         [227.6 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -valgrind "devel/sage/sage/rings/polynomial/real_roots.pyx"
Total time for all tests: 227.6 seconds
```


This is not the only one, but the root  of evil seems to be in real_roots (how ironic...)
more precisly: I tracked it down, with help of valgrind, to the class ocean. Has anyone an Idea??



---

archive/issue_comments_096441.json:
```json
{
    "body": "Update: Found the problem. see: http://groups.google.com/group/cython-users/browse_thread/thread/624c696293b7fe44\n\nIt seems that all versions 1.5.x hold this bug....\nTried downgrading to 1.4.1. and all corrections I have done so far worked.\n\nI will now apply the patch from drkirkby, pack it again, test it overnight and hopefully we are done with 1.4.1, and hopefully they get it right in the next time. perhaps I should send the numpy/scipy guys the doctests I've done so far\n\nscipy 0.8. don't seem to make any problems so far",
    "created_at": "2010-09-01T20:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96441",
    "user": "maldun"
}
```

Update: Found the problem. see: http://groups.google.com/group/cython-users/browse_thread/thread/624c696293b7fe44

It seems that all versions 1.5.x hold this bug....
Tried downgrading to 1.4.1. and all corrections I have done so far worked.

I will now apply the patch from drkirkby, pack it again, test it overnight and hopefully we are done with 1.4.1, and hopefully they get it right in the next time. perhaps I should send the numpy/scipy guys the doctests I've done so far

scipy 0.8. don't seem to make any problems so far



---

archive/issue_comments_096442.json:
```json
{
    "body": "an doctest I oversaw:\n\n\n```\nType ``numpy.typecodes`` for a list of the possible\n        typecodes::\n\n            sage: import numpy\n            sage: sorted(numpy.typecodes.items())\n            [('All', '?bhilqpBHILQPfdgFDGSUVOMm'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Datetime', 'Mm'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]\n```\n\n\nThe output is now:\n\n```\n[('All', '?bhilqpBHILQPfdgFDGSUVOMm'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Datetime', 'Mm'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]\n```\n\n\nBut since it's an extension, and no downgrade it is also no prob",
    "created_at": "2010-09-01T21:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96442",
    "user": "maldun"
}
```

an doctest I oversaw:


```
Type ``numpy.typecodes`` for a list of the possible
        typecodes::

            sage: import numpy
            sage: sorted(numpy.typecodes.items())
            [('All', '?bhilqpBHILQPfdgFDGSUVOMm'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Datetime', 'Mm'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]
```


The output is now:

```
[('All', '?bhilqpBHILQPfdgFDGSUVOMm'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Datetime', 'Mm'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]
```


But since it's an extension, and no downgrade it is also no prob



---

archive/issue_comments_096443.json:
```json
{
    "body": "Replying to [comment:23 maldun]:\n> an doctest I oversaw:\n> \n> {{{\n> Type ``numpy.typecodes`` for a list of the possible\n>         typecodes::\n> \n>             sage: import numpy\n>             sage: sorted(numpy.typecodes.items())\n>             [('All', '?bhilqpBHILQPfdgFDGSUVOMm'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Datetime', 'Mm'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]\n> }}}\n> \n> The output is now:\n> {{{\n> [('All', '?bhilqpBHILQPfdgFDGSUVOMm'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Datetime', 'Mm'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]\n> }}}\n> \n> But since it's an extension, and no downgrade it is also no prob\nthe doctest should be fixed as well. I have attached a new version of spkg-install\nfor numpy if you cared to give it a spin. It completely drop the non-cygwin patches.\nIt may need a little bit of work as I haven't looked yet at how you included \nDave's fix.",
    "created_at": "2010-09-01T22:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96443",
    "user": "@kiwifb"
}
```

Replying to [comment:23 maldun]:
> an doctest I oversaw:
> 
> {{{
> Type ``numpy.typecodes`` for a list of the possible
>         typecodes::
> 
>             sage: import numpy
>             sage: sorted(numpy.typecodes.items())
>             [('All', '?bhilqpBHILQPfdgFDGSUVOMm'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Datetime', 'Mm'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]
> }}}
> 
> The output is now:
> {{{
> [('All', '?bhilqpBHILQPfdgFDGSUVOMm'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Datetime', 'Mm'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]
> }}}
> 
> But since it's an extension, and no downgrade it is also no prob
the doctest should be fixed as well. I have attached a new version of spkg-install
for numpy if you cared to give it a spin. It completely drop the non-cygwin patches.
It may need a little bit of work as I haven't looked yet at how you included 
Dave's fix.



---

archive/issue_comments_096444.json:
```json
{
    "body": "Replying to [comment:24 fbissey]:\n\n> the doctest should be fixed as well. I have attached a new version of spkg-install\n> for numpy if you cared to give it a spin. It completely drop the non-cygwin patches.\n> It may need a little bit of work as I haven't looked yet at how you included \n> Dave's fix.\n\nYour install file worked well for me. I have merged it, such that the patches are getting applied.\nAll doctests work now. You can download the packages now at:\nhttp://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.4.1.spkg\nand\nhttp://code.google.com/p/spkg-upload/downloads/detail?name=scipy-0.8.spkg\n\nbut you also have to install a modified version of networkx. I have opened a ticket for this, and this also includes a package: http://trac.sagemath.org/sage_trac/ticket/9854\n\nnext I will add a patch which includes the changed doctests",
    "created_at": "2010-09-04T00:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96444",
    "user": "maldun"
}
```

Replying to [comment:24 fbissey]:

> the doctest should be fixed as well. I have attached a new version of spkg-install
> for numpy if you cared to give it a spin. It completely drop the non-cygwin patches.
> It may need a little bit of work as I haven't looked yet at how you included 
> Dave's fix.

Your install file worked well for me. I have merged it, such that the patches are getting applied.
All doctests work now. You can download the packages now at:
http://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.4.1.spkg
and
http://code.google.com/p/spkg-upload/downloads/detail?name=scipy-0.8.spkg

but you also have to install a modified version of networkx. I have opened a ticket for this, and this also includes a package: http://trac.sagemath.org/sage_trac/ticket/9854

next I will add a patch which includes the changed doctests



---

archive/issue_comments_096445.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-04T00:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96445",
    "user": "maldun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096446.json:
```json
{
    "body": "One important note: after updating numpy one has to rebuild the source with sage -ba, or else you get runtime warnings.\n\nThe reason is the size change in some of the numpy functions, and then the .pyx files have to be rebuild",
    "created_at": "2010-09-04T00:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96446",
    "user": "maldun"
}
```

One important note: after updating numpy one has to rebuild the source with sage -ba, or else you get runtime warnings.

The reason is the size change in some of the numpy functions, and then the .pyx files have to be rebuild



---

archive/issue_comments_096447.json:
```json
{
    "body": "Attachment [networkx-1.0.1.p0.spkg](tarball://root/attachments/some-uuid/ticket9808/networkx-1.0.1.p0.spkg) by maldun created at 2010-09-04 01:32:43\n\nmodified networkx package (test version)",
    "created_at": "2010-09-04T01:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96447",
    "user": "maldun"
}
```

Attachment [networkx-1.0.1.p0.spkg](tarball://root/attachments/some-uuid/ticket9808/networkx-1.0.1.p0.spkg) by maldun created at 2010-09-04 01:32:43

modified networkx package (test version)



---

archive/issue_comments_096448.json:
```json
{
    "body": "Attachment [convert.py.diff](tarball://root/attachments/some-uuid/ticket9808/convert.py.diff) by maldun created at 2010-09-04 01:33:14\n\nchanges to networkx, which have to be applied",
    "created_at": "2010-09-04T01:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96448",
    "user": "maldun"
}
```

Attachment [convert.py.diff](tarball://root/attachments/some-uuid/ticket9808/convert.py.diff) by maldun created at 2010-09-04 01:33:14

changes to networkx, which have to be applied



---

archive/issue_comments_096449.json:
```json
{
    "body": "Thanks for the patches. I will probably introduce these in sage-on-gentoo in short order. About networkx, you realize that sage-4.5.3 will use networkx-1.2?\nsee ticket #9567 \nSo have you tried to see if networkx-1.2 needs patching (my guess is no, otherwise\nI would know by now from gentoo).",
    "created_at": "2010-09-04T08:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96449",
    "user": "@kiwifb"
}
```

Thanks for the patches. I will probably introduce these in sage-on-gentoo in short order. About networkx, you realize that sage-4.5.3 will use networkx-1.2?
see ticket #9567 
So have you tried to see if networkx-1.2 needs patching (my guess is no, otherwise
I would know by now from gentoo).



---

archive/issue_comments_096450.json:
```json
{
    "body": "Replying to [comment:27 fbissey]:\n> Thanks for the patches. I will probably introduce these in sage-on-gentoo in short order. About networkx, you realize that sage-4.5.3 will use networkx-1.2?\n> see ticket #9567 \n> So have you tried to see if networkx-1.2 needs patching (my guess is no, otherwise\n> I would know by now from gentoo).\n\nI've seen that networkx 1.2. is out but it doesn't seem to work with my sage-4.2 with numpy 1.4.1 nor with my sage-4.1 with the old numpy\nso I created this spkg in order that it can be used with old versions of sage too\n\nBut it seems the line where the problems come from doesn't exist in the new version of networkx anymore.\nCould you give the numpy packages a spin with the new versions of numpy/scipy? It is very time consuming for me to rebuild every time the source. Thanx in advance!",
    "created_at": "2010-09-04T10:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96450",
    "user": "maldun"
}
```

Replying to [comment:27 fbissey]:
> Thanks for the patches. I will probably introduce these in sage-on-gentoo in short order. About networkx, you realize that sage-4.5.3 will use networkx-1.2?
> see ticket #9567 
> So have you tried to see if networkx-1.2 needs patching (my guess is no, otherwise
> I would know by now from gentoo).

I've seen that networkx 1.2. is out but it doesn't seem to work with my sage-4.2 with numpy 1.4.1 nor with my sage-4.1 with the old numpy
so I created this spkg in order that it can be used with old versions of sage too

But it seems the line where the problems come from doesn't exist in the new version of networkx anymore.
Could you give the numpy packages a spin with the new versions of numpy/scipy? It is very time consuming for me to rebuild every time the source. Thanx in advance!



---

archive/issue_comments_096451.json:
```json
{
    "body": "ith the new versions of numpy/scipy? It is very time consuming for me to rebuild every time the source. Thanx in advance!\n\nsorry I meant new versions of networkx...",
    "created_at": "2010-09-04T10:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96451",
    "user": "maldun"
}
```

ith the new versions of numpy/scipy? It is very time consuming for me to rebuild every time the source. Thanx in advance!

sorry I meant new versions of networkx...



---

archive/issue_comments_096452.json:
```json
{
    "body": "Understood. We already ship networkx-1.2 with sage-4.5.2 on sage-on-gentoo [because\nnetworkx-1.0.1 has been removed from Gentoo] so I can test your patches along with networkx. It may take 1 or 2 days for me to fit it in my schedule.",
    "created_at": "2010-09-04T10:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96452",
    "user": "@kiwifb"
}
```

Understood. We already ship networkx-1.2 with sage-4.5.2 on sage-on-gentoo [because
networkx-1.0.1 has been removed from Gentoo] so I can test your patches along with networkx. It may take 1 or 2 days for me to fit it in my schedule.



---

archive/issue_comments_096453.json:
```json
{
    "body": "ok. Since I had some time this afternoon I build a version of sage-1.4.3.alpha1 (which also has networkx-1.2.) on my machine, applied the packages, the patch, rebuild the source with sage -ba and everything worked fine!\n\n\n```\n./sage -tp 4 -long devel/sage-numpy\n....\nsage -t -long devel/sage-numpy/doc/en/a_tour_of_sage/index.rst\n         [23.1 s]\nsage -t -long devel/sage-numpy/doc/en/thematic_tutorials/group_theory.rst\n         [247.1 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTimings have been updated.\nTotal time for all tests: 7320.5 seconds\n```\n\n\nSo networkx-1.2 works!\n\nFor Info: I use Ubuntu 10.04 on my machine.\nSo I think it would still be good if someone else would test it",
    "created_at": "2010-09-04T20:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96453",
    "user": "maldun"
}
```

ok. Since I had some time this afternoon I build a version of sage-1.4.3.alpha1 (which also has networkx-1.2.) on my machine, applied the packages, the patch, rebuild the source with sage -ba and everything worked fine!


```
./sage -tp 4 -long devel/sage-numpy
....
sage -t -long devel/sage-numpy/doc/en/a_tour_of_sage/index.rst
         [23.1 s]
sage -t -long devel/sage-numpy/doc/en/thematic_tutorials/group_theory.rst
         [247.1 s]
 
----------------------------------------------------------------------
All tests passed!
Timings have been updated.
Total time for all tests: 7320.5 seconds
```


So networkx-1.2 works!

For Info: I use Ubuntu 10.04 on my machine.
So I think it would still be good if someone else would test it



---

archive/issue_comments_096454.json:
```json
{
    "body": "It all works in sage-on-gentoo.\n\nHowever I think there are a few points that should be taken into consideration for both numpy and scipy.\nJust before posting my spkg-install I edited it to remove a change that I now think is probably necessary. I had set FC to SAGE_FORTRAN...\nWhy? Because numpy tries to autodetect a fortran compiler and will take a gnu compiler first. Unless you set FC. Which means if Dave tries to compile sage with sunstudio on a machine that has also gfortran he is in for a world of hurt.\nSo I think we should either set FC to SAGE_FORTRAN in numpy and possibly scipy. \nThe other option is to set it globally but that may cause problems on OSX.\n\nThoughts? Francois",
    "created_at": "2010-09-06T09:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96454",
    "user": "@kiwifb"
}
```

It all works in sage-on-gentoo.

However I think there are a few points that should be taken into consideration for both numpy and scipy.
Just before posting my spkg-install I edited it to remove a change that I now think is probably necessary. I had set FC to SAGE_FORTRAN...
Why? Because numpy tries to autodetect a fortran compiler and will take a gnu compiler first. Unless you set FC. Which means if Dave tries to compile sage with sunstudio on a machine that has also gfortran he is in for a world of hurt.
So I think we should either set FC to SAGE_FORTRAN in numpy and possibly scipy. 
The other option is to set it globally but that may cause problems on OSX.

Thoughts? Francois



---

archive/issue_comments_096455.json:
```json
{
    "body": "Replying to [comment:33 fbissey]:\n> It all works in sage-on-gentoo.\n> \n> However I think there are a few points that should be taken into consideration for both numpy and scipy.\n> Just before posting my spkg-install I edited it to remove a change that I now think is probably necessary. I had set FC to SAGE_FORTRAN...\n> Why? Because numpy tries to autodetect a fortran compiler and will take a gnu compiler first. Unless you set FC. Which means if Dave tries to compile sage with sunstudio on a machine that has also gfortran he is in for a world of hurt.\n> So I think we should either set FC to SAGE_FORTRAN in numpy and possibly scipy. \n> The other option is to set it globally but that may cause problems on OSX.\n> \n> Thoughts? Francois\n\nA very pragmatic thougt: If it doesn\"t hurt to set FC to SAGE_FORTRAN, why not? But I think it\"s better not to do it globally. Because then we could cause more problems then we solve.\nCan you give a modified spkg-install? I can try it out over night then.\n\nBut I think it would also be good to get some feedback for Solaris and OSX for the current versions. Then we could decide to keep the current, or to take the other.",
    "created_at": "2010-09-06T10:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96455",
    "user": "maldun"
}
```

Replying to [comment:33 fbissey]:
> It all works in sage-on-gentoo.
> 
> However I think there are a few points that should be taken into consideration for both numpy and scipy.
> Just before posting my spkg-install I edited it to remove a change that I now think is probably necessary. I had set FC to SAGE_FORTRAN...
> Why? Because numpy tries to autodetect a fortran compiler and will take a gnu compiler first. Unless you set FC. Which means if Dave tries to compile sage with sunstudio on a machine that has also gfortran he is in for a world of hurt.
> So I think we should either set FC to SAGE_FORTRAN in numpy and possibly scipy. 
> The other option is to set it globally but that may cause problems on OSX.
> 
> Thoughts? Francois

A very pragmatic thougt: If it doesn"t hurt to set FC to SAGE_FORTRAN, why not? But I think it"s better not to do it globally. Because then we could cause more problems then we solve.
Can you give a modified spkg-install? I can try it out over night then.

But I think it would also be good to get some feedback for Solaris and OSX for the current versions. Then we could decide to keep the current, or to take the other.



---

archive/issue_comments_096456.json:
```json
{
    "body": "Good news: It seems that the problem from numpy-1.5.0 has been resolved http://projects.scipy.org/numpy/ticket/1605\nI don't think it's a big deal. Shall I give it a try, or should we stick to 1.4.1 for now?",
    "created_at": "2010-09-06T11:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96456",
    "user": "maldun"
}
```

Good news: It seems that the problem from numpy-1.5.0 has been resolved http://projects.scipy.org/numpy/ticket/1605
I don't think it's a big deal. Shall I give it a try, or should we stick to 1.4.1 for now?



---

archive/issue_comments_096457.json:
```json
{
    "body": "Replying to [comment:35 maldun]:\n> Good news: It seems that the problem from numpy-1.5.0 has been resolved http://projects.scipy.org/numpy/ticket/1605\n> I don't think it's a big deal. Shall I give it a try, or should we stick to 1.4.1 for now?\n...or wait til 1.5.1 is out?",
    "created_at": "2010-09-06T11:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96457",
    "user": "maldun"
}
```

Replying to [comment:35 maldun]:
> Good news: It seems that the problem from numpy-1.5.0 has been resolved http://projects.scipy.org/numpy/ticket/1605
> I don't think it's a big deal. Shall I give it a try, or should we stick to 1.4.1 for now?
...or wait til 1.5.1 is out?



---

archive/issue_comments_096458.json:
```json
{
    "body": "May be wait until numpy-1.5.1. it is not a big deal right now I guess.\nMay be we should discuss it on sage-devel. At the moment we don't really\nhave much testing apart from the fact I unleashed the upgrade to numpy-1.4.1/scipy-0.8\non sage-on-gentoo users. I am not sure we can believably merge this in 4.5.3 unless\nit takes more than one week before it is released. If we target 4.5.3 I say we stay with what we have now, if we target 4.6 which should be a little further down the track we go for 1.5.x.",
    "created_at": "2010-09-06T11:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96458",
    "user": "@kiwifb"
}
```

May be wait until numpy-1.5.1. it is not a big deal right now I guess.
May be we should discuss it on sage-devel. At the moment we don't really
have much testing apart from the fact I unleashed the upgrade to numpy-1.4.1/scipy-0.8
on sage-on-gentoo users. I am not sure we can believably merge this in 4.5.3 unless
it takes more than one week before it is released. If we target 4.5.3 I say we stay with what we have now, if we target 4.6 which should be a little further down the track we go for 1.5.x.



---

archive/issue_comments_096459.json:
```json
{
    "body": "Attachment [spkg-install](tarball://root/attachments/some-uuid/ticket9808/spkg-install) by @kiwifb created at 2010-09-06 11:40:36\n\nnewer spkg_install setting FC",
    "created_at": "2010-09-06T11:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96459",
    "user": "@kiwifb"
}
```

Attachment [spkg-install](tarball://root/attachments/some-uuid/ticket9808/spkg-install) by @kiwifb created at 2010-09-06 11:40:36

newer spkg_install setting FC



---

archive/issue_comments_096460.json:
```json
{
    "body": "I updated my spkg_install as you requested. The other thing about using sage_fortran,\nthat I had forgotten to change back when I removed it, is that it includes \"-fPIC\".\nI didn't check the fortran spkg but hopefully the work done by Dave to set the correct\npic flag is picked up in sage_fortran.\n\nIf we don't adopt this, FFLAG=\"-fPIC\" (or whatever mechanism Dave came up with) should be added in my previous version.",
    "created_at": "2010-09-06T11:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96460",
    "user": "@kiwifb"
}
```

I updated my spkg_install as you requested. The other thing about using sage_fortran,
that I had forgotten to change back when I removed it, is that it includes "-fPIC".
I didn't check the fortran spkg but hopefully the work done by Dave to set the correct
pic flag is picked up in sage_fortran.

If we don't adopt this, FFLAG="-fPIC" (or whatever mechanism Dave came up with) should be added in my previous version.



---

archive/issue_comments_096461.json:
```json
{
    "body": "Replying to [comment:37 fbissey]:\n> May be wait until numpy-1.5.1. it is not a big deal right now I guess.\n> May be we should discuss it on sage-devel. At the moment we don't really\n> have much testing apart from the fact I unleashed the upgrade to numpy-1.4.1/scipy-0.8\n> on sage-on-gentoo users. I am not sure we can believably merge this in 4.5.3 unless\n> it takes more than one week before it is released. If we target 4.5.3 I say we stay with what we have now, if we target 4.6 which should be a little further down the track we go for 1.5.x.\n\nOk I think we should do the following: Let's stick to 1.4.1 since it is necessary for scipy 0.8. and quite well tested yet, in contrary to 1.5.x and it seems to work. Especially since the update from scipy 0.7 to 0.8 holds a lot of changes, and we don't know if they build some more bugs into numpy 1.5.1...\nIf it turns out that updating from 1.4.1 to 1.5.1 is no problem, then well... packing a new package would'nt be the prob I think.  \n\n`@`new spkg: Ok I will give it a try tonight!",
    "created_at": "2010-09-06T11:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96461",
    "user": "maldun"
}
```

Replying to [comment:37 fbissey]:
> May be wait until numpy-1.5.1. it is not a big deal right now I guess.
> May be we should discuss it on sage-devel. At the moment we don't really
> have much testing apart from the fact I unleashed the upgrade to numpy-1.4.1/scipy-0.8
> on sage-on-gentoo users. I am not sure we can believably merge this in 4.5.3 unless
> it takes more than one week before it is released. If we target 4.5.3 I say we stay with what we have now, if we target 4.6 which should be a little further down the track we go for 1.5.x.

Ok I think we should do the following: Let's stick to 1.4.1 since it is necessary for scipy 0.8. and quite well tested yet, in contrary to 1.5.x and it seems to work. Especially since the update from scipy 0.7 to 0.8 holds a lot of changes, and we don't know if they build some more bugs into numpy 1.5.1...
If it turns out that updating from 1.4.1 to 1.5.1 is no problem, then well... packing a new package would'nt be the prob I think.  

`@`new spkg: Ok I will give it a try tonight!



---

archive/issue_comments_096462.json:
```json
{
    "body": "There's a lot of packages etc. on this ticket.  Can someone provide a concise list of what would be needed to apply on a given platform?  (For instance, in a very cursory glance, the networkx package being here mystifies.)",
    "created_at": "2010-09-06T12:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96462",
    "user": "@kcrisman"
}
```

There's a lot of packages etc. on this ticket.  Can someone provide a concise list of what would be needed to apply on a given platform?  (For instance, in a very cursory glance, the networkx package being here mystifies.)



---

archive/issue_comments_096463.json:
```json
{
    "body": "Replying to [comment:40 kcrisman]:\n> There's a lot of packages etc. on this ticket.  Can someone provide a concise list of what would be needed to apply on a given platform?  (For instance, in a very cursory glance, the networkx package being here mystifies.) \n\nNeeded are:\nhttp://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.4.1.spkg   http://code.google.com/p/spkg-upload/downloads/detail?name=scipy-0.8.spkg\n\nafter installing numpy, one needs so execute sage -ba, or else one get's runtime warnings.\n\nYou also need networkx-1.2. (the other networkx is just a small hack for testing, because 1.2. didn't build correctly on my machine, but this is obsolete now, since networkx-1.2 is merged into sage 4.3.alpha1)",
    "created_at": "2010-09-06T13:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96463",
    "user": "maldun"
}
```

Replying to [comment:40 kcrisman]:
> There's a lot of packages etc. on this ticket.  Can someone provide a concise list of what would be needed to apply on a given platform?  (For instance, in a very cursory glance, the networkx package being here mystifies.) 

Needed are:
http://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.4.1.spkg   http://code.google.com/p/spkg-upload/downloads/detail?name=scipy-0.8.spkg

after installing numpy, one needs so execute sage -ba, or else one get's runtime warnings.

You also need networkx-1.2. (the other networkx is just a small hack for testing, because 1.2. didn't build correctly on my machine, but this is obsolete now, since networkx-1.2 is merged into sage 4.3.alpha1)



---

archive/issue_comments_096464.json:
```json
{
    "body": "I gave the links and (current) build instructions into the discription, so that people can find the latest versions more quickly",
    "created_at": "2010-09-06T13:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96464",
    "user": "maldun"
}
```

I gave the links and (current) build instructions into the discription, so that people can find the latest versions more quickly



---

archive/issue_comments_096465.json:
```json
{
    "body": "Included direct links to files in description.",
    "created_at": "2010-09-06T13:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96465",
    "user": "@kcrisman"
}
```

Included direct links to files in description.



---

archive/issue_comments_096466.json:
```json
{
    "body": "This seems to work fine on Mac OS X 10.6.4 Intel.  I will try to test it tomorrow on a PowerPC machine.  Note: I haven't looked at the spkg installs or anything, this is just a data point with regard to whether it works, not a review.",
    "created_at": "2010-09-06T16:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96466",
    "user": "@kcrisman"
}
```

This seems to work fine on Mac OS X 10.6.4 Intel.  I will try to test it tomorrow on a PowerPC machine.  Note: I haven't looked at the spkg installs or anything, this is just a data point with regard to whether it works, not a review.



---

archive/issue_comments_096467.json:
```json
{
    "body": "This fails very early on in Cygwin with\n\n\n```\nbuilding library \"npymath\" sources\ncreating build/src.cygwin-1.7.5-i686-2.6/src\nconv_template:> build/src.cygwin-1.7.5-i686-2.6/src/npy_math.c\nerror: src/npy_math.c.src: No such file or directory\nError building numpy.\n```\n",
    "created_at": "2010-09-06T16:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96467",
    "user": "@mwhansen"
}
```

This fails very early on in Cygwin with


```
building library "npymath" sources
creating build/src.cygwin-1.7.5-i686-2.6/src
conv_template:> build/src.cygwin-1.7.5-i686-2.6/src/npy_math.c
error: src/npy_math.c.src: No such file or directory
Error building numpy.
```




---

archive/issue_comments_096468.json:
```json
{
    "body": "Replying to [comment:50 mhansen]:\n> This fails very early on in Cygwin with\n> \n> {{{\n> building library \"npymath\" sources\n> creating build/src.cygwin-1.7.5-i686-2.6/src\n> conv_template:> build/src.cygwin-1.7.5-i686-2.6/src/npy_math.c\n> error: src/npy_math.c.src: No such file or directory\n> Error building numpy.\n> }}}\n\nOk I think I have the picture: some files from /src/numpy/core/src moved to subfolders\nthis have to be changed in the cygwin-core-setup.py\n\nI'm installing already cygwin on my laptop and look if I get it up and running, but if anyone could help out I would be thankful!",
    "created_at": "2010-09-06T18:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96468",
    "user": "maldun"
}
```

Replying to [comment:50 mhansen]:
> This fails very early on in Cygwin with
> 
> {{{
> building library "npymath" sources
> creating build/src.cygwin-1.7.5-i686-2.6/src
> conv_template:> build/src.cygwin-1.7.5-i686-2.6/src/npy_math.c
> error: src/npy_math.c.src: No such file or directory
> Error building numpy.
> }}}

Ok I think I have the picture: some files from /src/numpy/core/src moved to subfolders
this have to be changed in the cygwin-core-setup.py

I'm installing already cygwin on my laptop and look if I get it up and running, but if anyone could help out I would be thankful!



---

archive/issue_comments_096469.json:
```json
{
    "body": "I've tested it out, and everything works if you just remove the cygwin-core-setup.py patch.",
    "created_at": "2010-09-06T19:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96469",
    "user": "@mwhansen"
}
```

I've tested it out, and everything works if you just remove the cygwin-core-setup.py patch.



---

archive/issue_comments_096470.json:
```json
{
    "body": "Replying to [comment:52 mhansen]:\n> I've tested it out, and everything works if you just remove the cygwin-core-setup.py patch.\n\nI was just about to upload a patch...\nBut great this is even better than my solution! (and simpler)\nThe reason why it fails is just that cygwin-core-setup.py is outdated.\n\none question: (because I'm quite the noob...)\nIf I want to upload a modified version of numpy-1.4.1 do I have to overwrite the old version, or shall I rename it with numpy-1.4.1.p0.spkg?",
    "created_at": "2010-09-06T19:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96470",
    "user": "maldun"
}
```

Replying to [comment:52 mhansen]:
> I've tested it out, and everything works if you just remove the cygwin-core-setup.py patch.

I was just about to upload a patch...
But great this is even better than my solution! (and simpler)
The reason why it fails is just that cygwin-core-setup.py is outdated.

one question: (because I'm quite the noob...)
If I want to upload a modified version of numpy-1.4.1 do I have to overwrite the old version, or shall I rename it with numpy-1.4.1.p0.spkg?



---

archive/issue_comments_096471.json:
```json
{
    "body": "Replying to [comment:53 maldun]:\n\n> one question: (because I'm quite the noob...)\n> If I want to upload a modified version of numpy-1.4.1 do I have to overwrite the old version, or shall I rename it with numpy-1.4.1.p0.spkg?\n\nOverwrite the old one.",
    "created_at": "2010-09-06T19:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96471",
    "user": "drkirkby"
}
```

Replying to [comment:53 maldun]:

> one question: (because I'm quite the noob...)
> If I want to upload a modified version of numpy-1.4.1 do I have to overwrite the old version, or shall I rename it with numpy-1.4.1.p0.spkg?

Overwrite the old one.



---

archive/issue_comments_096472.json:
```json
{
    "body": "Thanx!\nNumpy is now updated with \n* changes from fbissey to the installer (it worked for me)\n* removed the cygwin-core-setup.py patch",
    "created_at": "2010-09-06T19:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96472",
    "user": "maldun"
}
```

Thanx!
Numpy is now updated with 
* changes from fbissey to the installer (it worked for me)
* removed the cygwin-core-setup.py patch



---

archive/issue_comments_096473.json:
```json
{
    "body": "The SciPy spkg works fine in Cygwin.",
    "created_at": "2010-09-06T20:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96473",
    "user": "@mwhansen"
}
```

The SciPy spkg works fine in Cygwin.



---

archive/issue_comments_096474.json:
```json
{
    "body": "I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?",
    "created_at": "2010-09-07T14:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96474",
    "user": "@kcrisman"
}
```

I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?



---

archive/issue_comments_096475.json:
```json
{
    "body": "Replying to [comment:57 kcrisman]:\n> I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?\n\nYes we did some changes to the spkg-install. But I downloaded and installed the package right now again. So I don't know wehre the problem is lying?",
    "created_at": "2010-09-07T14:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96475",
    "user": "maldun"
}
```

Replying to [comment:57 kcrisman]:
> I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?

Yes we did some changes to the spkg-install. But I downloaded and installed the package right now again. So I don't know wehre the problem is lying?



---

archive/issue_comments_096476.json:
```json
{
    "body": "Replying to [comment:58 maldun]:\n> Replying to [comment:57 kcrisman]:\n> > I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?\n> \n> Yes we did some changes to the spkg-install. But I downloaded and installed the package right now again. So I don't know wehre the problem is lying?\n> \n\nDid you use `sage -pkg` to create it or just do some kind of compression?  I get a message about `tar: this does not look like a file archive` and `tar: Archive contains obsolescent base-64 headers`.  I just installed the optional biopython package on this machine to test things, so the machine shouldn't be the problem (and it built Sage 4.5.2 just fine).",
    "created_at": "2010-09-07T14:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96476",
    "user": "@kcrisman"
}
```

Replying to [comment:58 maldun]:
> Replying to [comment:57 kcrisman]:
> > I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?
> 
> Yes we did some changes to the spkg-install. But I downloaded and installed the package right now again. So I don't know wehre the problem is lying?
> 

Did you use `sage -pkg` to create it or just do some kind of compression?  I get a message about `tar: this does not look like a file archive` and `tar: Archive contains obsolescent base-64 headers`.  I just installed the optional biopython package on this machine to test things, so the machine shouldn't be the problem (and it built Sage 4.5.2 just fine).



---

archive/issue_comments_096477.json:
```json
{
    "body": "Replying to [comment:59 kcrisman]:\n> Replying to [comment:58 maldun]:\n> > Replying to [comment:57 kcrisman]:\n> > > I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?\n> > \n> > Yes we did some changes to the spkg-install. But I downloaded and installed the package right now again. So I don't know wehre the problem is lying?\n> > \n> \n> Did you use `sage -pkg` to create it or just do some kind of compression?  I get a message about `tar: this does not look like a file archive` and `tar: Archive contains obsolescent base-64 headers`.  I just installed the optional biopython package on this machine to test things, so the machine shouldn't be the problem (and it built Sage 4.5.2 just fine).\n\nOk I repacked it now with -pkg and uploaded it. Does it work now?\nAnd sorry for the newby question: what is the difference between -pkg and just compress it?\nIs sage using a different version of tar? Because in fact a spkg is noting else then a tar.gz with different ending.",
    "created_at": "2010-09-07T15:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96477",
    "user": "maldun"
}
```

Replying to [comment:59 kcrisman]:
> Replying to [comment:58 maldun]:
> > Replying to [comment:57 kcrisman]:
> > > I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?
> > 
> > Yes we did some changes to the spkg-install. But I downloaded and installed the package right now again. So I don't know wehre the problem is lying?
> > 
> 
> Did you use `sage -pkg` to create it or just do some kind of compression?  I get a message about `tar: this does not look like a file archive` and `tar: Archive contains obsolescent base-64 headers`.  I just installed the optional biopython package on this machine to test things, so the machine shouldn't be the problem (and it built Sage 4.5.2 just fine).

Ok I repacked it now with -pkg and uploaded it. Does it work now?
And sorry for the newby question: what is the difference between -pkg and just compress it?
Is sage using a different version of tar? Because in fact a spkg is noting else then a tar.gz with different ending.



---

archive/issue_comments_096478.json:
```json
{
    "body": "> Ok I repacked it now with -pkg and uploaded it. Does it work now?\n> And sorry for the newby question: what is the difference between -pkg and just compress it?\n> Is sage using a different version of tar? Because in fact a spkg is noting else then a tar.gz with different ending.\n\nNo, it's a little more than that - it has an SPKG.txt, it has Mercurial repositories, etc.  True that the file type is the same.  But sage -pkg tests several things, and a successful review would check all that.  See [here](http://www.sagemath.org/doc/developer/producing_spkgs.html) for more info.",
    "created_at": "2010-09-07T15:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96478",
    "user": "@kcrisman"
}
```

> Ok I repacked it now with -pkg and uploaded it. Does it work now?
> And sorry for the newby question: what is the difference between -pkg and just compress it?
> Is sage using a different version of tar? Because in fact a spkg is noting else then a tar.gz with different ending.

No, it's a little more than that - it has an SPKG.txt, it has Mercurial repositories, etc.  True that the file type is the same.  But sage -pkg tests several things, and a successful review would check all that.  See [here](http://www.sagemath.org/doc/developer/producing_spkgs.html) for more info.



---

archive/issue_comments_096479.json:
```json
{
    "body": "Hmm, when I open it manually it seems fine.  Though when I run `sage -pkg` on that new folder, I get \n\n```\nHG REPO: Unchecked in changes\n```\n\nSo you'll need to fix that.   Putting myself as a reviewer now.\n\nCalling `sage -f` on this new spkg I made *does* seem to work, for whatever reason.  This doesn't make sense to me - why is `tar` complaining about yours?  Hopefully someone who knows about file systems will test this soon and explain why this causes a problem on Mac OS X 10.4 Tiger.",
    "created_at": "2010-09-07T15:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96479",
    "user": "@kcrisman"
}
```

Hmm, when I open it manually it seems fine.  Though when I run `sage -pkg` on that new folder, I get 

```
HG REPO: Unchecked in changes
```

So you'll need to fix that.   Putting myself as a reviewer now.

Calling `sage -f` on this new spkg I made *does* seem to work, for whatever reason.  This doesn't make sense to me - why is `tar` complaining about yours?  Hopefully someone who knows about file systems will test this soon and explain why this causes a problem on Mac OS X 10.4 Tiger.



---

archive/issue_comments_096480.json:
```json
{
    "body": "Okay, that worked.  Scipy seems to be installing fine directly from the website, I'm not sure why this happened.",
    "created_at": "2010-09-07T15:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96480",
    "user": "@kcrisman"
}
```

Okay, that worked.  Scipy seems to be installing fine directly from the website, I'm not sure why this happened.



---

archive/issue_comments_096481.json:
```json
{
    "body": "Thanx for the hints!\nI updated the mercurial entries now to the latest version.\nUploaded changed packages.\nEverything should be fine now",
    "created_at": "2010-09-07T17:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96481",
    "user": "maldun"
}
```

Thanx for the hints!
I updated the mercurial entries now to the latest version.
Uploaded changed packages.
Everything should be fine now



---

archive/issue_comments_096482.json:
```json
{
    "body": "Replying to [comment:63 kcrisman]:\n> Okay, that worked.  Scipy seems to be installing fine directly from the website, I'm not sure why this happened.\n\nI have an Idea: different versions of .tar may cause problems (so far as I know) If you look at the file sizes only it seems that sage does a different kind of compression.",
    "created_at": "2010-09-07T17:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96482",
    "user": "maldun"
}
```

Replying to [comment:63 kcrisman]:
> Okay, that worked.  Scipy seems to be installing fine directly from the website, I'm not sure why this happened.

I have an Idea: different versions of .tar may cause problems (so far as I know) If you look at the file sizes only it seems that sage does a different kind of compression.



---

archive/issue_comments_096483.json:
```json
{
    "body": "I get the following error with the Scipy for some reason.\n\n```\ncreating build/temp.macosx-10.4-ppc-2.6/scipy/special\ncreating build/temp.macosx-10.4-ppc-2.6/scipy/special/c_misc\ncompile options: '-I/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include -c'\ngcc: scipy/special/c_misc/fsolve.c\nscipy/special/c_misc/fsolve.c: In function 'false_position':\nscipy/special/c_misc/fsolve.c:58: warning: 'f3' may be used uninitialized in this function\nscipy/special/c_misc/fsolve.c:58: warning: 'x3' may be used uninitialized in this function\ngcc: scipy/special/c_misc/gammaincinv.c\nscipy/special/c_misc/gammaincinv.c:1:20: error: Python.h: No such file or directory\nIn file included from /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_math.h:5,\n                 from scipy/special/c_misc/gammaincinv.c:2:\n/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_common.h:79:2: error: #error Must use Python with unicode enabled.\nscipy/special/c_misc/gammaincinv.c:1:20: error: Python.h: No such file or directory\nIn file included from /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_math.h:5,\n                 from scipy/special/c_misc/gammaincinv.c:2:\n/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_common.h:79:2: error: #error Must use Python with unicode enabled.\nerror: Command \"gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include -c scipy/special/c_misc/gammaincinv.c -o build/temp.macosx-10.4-ppc-2.6/scipy/special/c_misc/gammaincinv.o\" failed with exit status 1\nError building scipy.\n```\n\nDid you use some special encoding for some of your stuff?",
    "created_at": "2010-09-07T17:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96483",
    "user": "@kcrisman"
}
```

I get the following error with the Scipy for some reason.

```
creating build/temp.macosx-10.4-ppc-2.6/scipy/special
creating build/temp.macosx-10.4-ppc-2.6/scipy/special/c_misc
compile options: '-I/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include -c'
gcc: scipy/special/c_misc/fsolve.c
scipy/special/c_misc/fsolve.c: In function 'false_position':
scipy/special/c_misc/fsolve.c:58: warning: 'f3' may be used uninitialized in this function
scipy/special/c_misc/fsolve.c:58: warning: 'x3' may be used uninitialized in this function
gcc: scipy/special/c_misc/gammaincinv.c
scipy/special/c_misc/gammaincinv.c:1:20: error: Python.h: No such file or directory
In file included from /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_math.h:5,
                 from scipy/special/c_misc/gammaincinv.c:2:
/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_common.h:79:2: error: #error Must use Python with unicode enabled.
scipy/special/c_misc/gammaincinv.c:1:20: error: Python.h: No such file or directory
In file included from /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_math.h:5,
                 from scipy/special/c_misc/gammaincinv.c:2:
/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_common.h:79:2: error: #error Must use Python with unicode enabled.
error: Command "gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include -c scipy/special/c_misc/gammaincinv.c -o build/temp.macosx-10.4-ppc-2.6/scipy/special/c_misc/gammaincinv.o" failed with exit status 1
Error building scipy.
```

Did you use some special encoding for some of your stuff?



---

archive/issue_comments_096484.json:
```json
{
    "body": "Replying to [comment:66 kcrisman]:\n> I get the following error with the Scipy for some reason.\n {{{\n creating build/temp.macosx-10.4-ppc-2.6/scipy/special\n creating build/temp.macosx-10.4-ppc-2.6/scipy/special/c_misc\n compile options: '-I/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include -c'\n gcc: scipy/special/c_misc/fsolve.c\n scipy/special/c_misc/fsolve.c: In function 'false_position':\n scipy/special/c_misc/fsolve.c:58: warning: 'f3' may be used uninitialized in this function\n scipy/special/c_misc/fsolve.c:58: warning: 'x3' may be used uninitialized in this function\n gcc: scipy/special/c_misc/gammaincinv.c\n scipy/special/c_misc/gammaincinv.c:1:20: error: Python.h: No such file or directory\n In file included from /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy core/include/numpy/npy_math.h:5,\n                  from scipy/special/c_misc/gammaincinv.c:2:\n /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_common.h:79:2: error: #error Must use Python with unicode enabled.\n scipy/special/c_misc/gammaincinv.c:1:20: error: Python.h: No such file or directory\n In file included from /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_math.h:5,\n                  from scipy/special/c_misc/gammaincinv.c:2:\n /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_common.h:79:2: error: #error Must use Python with unicode enabled.\n error: Command \"gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include -c scipy/special/c_misc/gammaincinv.c -o build/temp.macosx-10.4-ppc-2.6/scipy/special/c_misc/gammaincinv.o\" failed with exit status 1\n Error building scipy.\n }}}\n> Did you use some special encoding for some of your stuff?  \n\nNope. Perhaps something else did go wrong. I repacked it now on a different machine with a newer version of ubuntu and uploaded it.\nHope this works. The first install worked for me.",
    "created_at": "2010-09-07T18:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96484",
    "user": "maldun"
}
```

Replying to [comment:66 kcrisman]:
> I get the following error with the Scipy for some reason.
 {{{
 creating build/temp.macosx-10.4-ppc-2.6/scipy/special
 creating build/temp.macosx-10.4-ppc-2.6/scipy/special/c_misc
 compile options: '-I/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include -c'
 gcc: scipy/special/c_misc/fsolve.c
 scipy/special/c_misc/fsolve.c: In function 'false_position':
 scipy/special/c_misc/fsolve.c:58: warning: 'f3' may be used uninitialized in this function
 scipy/special/c_misc/fsolve.c:58: warning: 'x3' may be used uninitialized in this function
 gcc: scipy/special/c_misc/gammaincinv.c
 scipy/special/c_misc/gammaincinv.c:1:20: error: Python.h: No such file or directory
 In file included from /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy core/include/numpy/npy_math.h:5,
                  from scipy/special/c_misc/gammaincinv.c:2:
 /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_common.h:79:2: error: #error Must use Python with unicode enabled.
 scipy/special/c_misc/gammaincinv.c:1:20: error: Python.h: No such file or directory
 In file included from /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_math.h:5,
                  from scipy/special/c_misc/gammaincinv.c:2:
 /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/npy_common.h:79:2: error: #error Must use Python with unicode enabled.
 error: Command "gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include -c scipy/special/c_misc/gammaincinv.c -o build/temp.macosx-10.4-ppc-2.6/scipy/special/c_misc/gammaincinv.o" failed with exit status 1
 Error building scipy.
 }}}
> Did you use some special encoding for some of your stuff?  

Nope. Perhaps something else did go wrong. I repacked it now on a different machine with a newer version of ubuntu and uploaded it.
Hope this works. The first install worked for me.



---

archive/issue_comments_096485.json:
```json
{
    "body": "Sadly, same error.  This is probably on my end, but this is a supported architecture so it's important to know what went wrong.  I don't think that the `./sage -ba` would have anything to do with it.\n\nSo I suspect that the \"missing: `Python.h` is the problem, as I've seen a few other things about this online (including ones like this one, where /include/Python.h definitely exists, here it's within the `$SAGE_ROOT` directory).  I wonder why it's not finding it this time?",
    "created_at": "2010-09-07T19:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96485",
    "user": "@kcrisman"
}
```

Sadly, same error.  This is probably on my end, but this is a supported architecture so it's important to know what went wrong.  I don't think that the `./sage -ba` would have anything to do with it.

So I suspect that the "missing: `Python.h` is the problem, as I've seen a few other things about this online (including ones like this one, where /include/Python.h definitely exists, here it's within the `$SAGE_ROOT` directory).  I wonder why it's not finding it this time?



---

archive/issue_comments_096486.json:
```json
{
    "body": "Replying to [comment:68 kcrisman]:\n> Sadly, same error.  This is probably on my end, but this is a supported architecture so it's important to know what went wrong.  I don't think that the `./sage -ba` would have anything to do with it.\n> \n> So I suspect that the \"missing: `Python.h` is the problem, as I've seen a few other things about this online (including ones like this one, where /include/Python.h definitely exists, here it's within the `$SAGE_ROOT` directory).  I wonder why it's not finding it this time?\n\nQuestion: Have you tried to give the direct path to the compiler?\nAnd does in OS X gcc points to /include/Python.h because in sage it's /include/python2.6/Python.h ?",
    "created_at": "2010-09-07T20:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96486",
    "user": "maldun"
}
```

Replying to [comment:68 kcrisman]:
> Sadly, same error.  This is probably on my end, but this is a supported architecture so it's important to know what went wrong.  I don't think that the `./sage -ba` would have anything to do with it.
> 
> So I suspect that the "missing: `Python.h` is the problem, as I've seen a few other things about this online (including ones like this one, where /include/Python.h definitely exists, here it's within the `$SAGE_ROOT` directory).  I wonder why it's not finding it this time?

Question: Have you tried to give the direct path to the compiler?
And does in OS X gcc points to /include/Python.h because in sage it's /include/python2.6/Python.h ?



---

archive/issue_comments_096487.json:
```json
{
    "body": "Replying to [comment:69 maldun]:\n> Replying to [comment:68 kcrisman]:\n> > Sadly, same error.  This is probably on my end, but this is a supported architecture so it's important to know what went wrong.  I don't think that the `./sage -ba` would have anything to do with it.\n> > \n> > So I suspect that the \"missing: `Python.h` is the problem, as I've seen a few other things about this online (including ones like this one, where /include/Python.h definitely exists, here it's within the `$SAGE_ROOT` directory).  I wonder why it's not finding it this time?\n> \n> Question: Have you tried to give the direct path to the compiler?\nNo - how would I do that?\n> And does in OS X gcc points to /include/Python.h because in sage it's /include/python2.6/Python.h ?\nI find that very unlikely, since everything else works fine and in general Sage builds fine on OS X 10.4-10.6.  But sometimes things get mixed up, I'm sure.  There aren't any weird env variables that would do that here, though, I don't think.",
    "created_at": "2010-09-08T00:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96487",
    "user": "@kcrisman"
}
```

Replying to [comment:69 maldun]:
> Replying to [comment:68 kcrisman]:
> > Sadly, same error.  This is probably on my end, but this is a supported architecture so it's important to know what went wrong.  I don't think that the `./sage -ba` would have anything to do with it.
> > 
> > So I suspect that the "missing: `Python.h` is the problem, as I've seen a few other things about this online (including ones like this one, where /include/Python.h definitely exists, here it's within the `$SAGE_ROOT` directory).  I wonder why it's not finding it this time?
> 
> Question: Have you tried to give the direct path to the compiler?
No - how would I do that?
> And does in OS X gcc points to /include/Python.h because in sage it's /include/python2.6/Python.h ?
I find that very unlikely, since everything else works fine and in general Sage builds fine on OS X 10.4-10.6.  But sometimes things get mixed up, I'm sure.  There aren't any weird env variables that would do that here, though, I don't think.



---

archive/issue_comments_096488.json:
```json
{
    "body": "A question: do we impose python to be built with or without unicode support? If\nnot, is the support enabled by default depending on the platform?\nTo me it looks like numpy ships headers that are encoded with unicode and that \nyour sage's python chock on them, that's the first and foremost error.\ndistutils seem to be unable to work things properly after that.\n\nTwo things could be tried:\n1) have python built with unicode support on OSX.\n2) \"vet\" numpy to convert the headers in /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/ to plain text.\nActually you probably can do that easily and manually right now on the installed\nheaders.\n\nGive it a spin and see if it works. If it does we'll have to do something about\nthat piece of unicode one way or another.",
    "created_at": "2010-09-08T01:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96488",
    "user": "@kiwifb"
}
```

A question: do we impose python to be built with or without unicode support? If
not, is the support enabled by default depending on the platform?
To me it looks like numpy ships headers that are encoded with unicode and that 
your sage's python chock on them, that's the first and foremost error.
distutils seem to be unable to work things properly after that.

Two things could be tried:
1) have python built with unicode support on OSX.
2) "vet" numpy to convert the headers in /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/ to plain text.
Actually you probably can do that easily and manually right now on the installed
headers.

Give it a spin and see if it works. If it does we'll have to do something about
that piece of unicode one way or another.



---

archive/issue_comments_096489.json:
```json
{
    "body": "Replying to [comment:71 fbissey]:\n> A question: do we impose python to be built with or without unicode support? If\n> not, is the support enabled by default depending on the platform?\n> To me it looks like numpy ships headers that are encoded with unicode and that \n> your sage's python chock on them, that's the first and foremost error.\n> distutils seem to be unable to work things properly after that.\n> \n> Two things could be tried:\n> 1) have python built with unicode support on OSX.\n> 2) \"vet\" numpy to convert the headers in /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/ to plain text.\n> Actually you probably can do that easily and manually right now on the installed\n> headers.\nUmm... except that I have no idea how I might do that.  What exact changes would I need to make to Python.h (and/or something else)?   It seems unwise to make yet another python spkg change to deal with this; did numpy only recently (between whatever Sage has now and 1.4.1) start making its headers unicode?  I am not exactly a C expert.\n\nThat said, 1) seems to be more canonical, though I guess if it makes it work, 2) could be an option.  This is the sort of thing Leif and/or drkirkby usually have an informed opinion on...\n> Give it a spin and see if it works. If it does we'll have to do something about\n> that piece of unicode one way or another.",
    "created_at": "2010-09-08T03:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96489",
    "user": "@kcrisman"
}
```

Replying to [comment:71 fbissey]:
> A question: do we impose python to be built with or without unicode support? If
> not, is the support enabled by default depending on the platform?
> To me it looks like numpy ships headers that are encoded with unicode and that 
> your sage's python chock on them, that's the first and foremost error.
> distutils seem to be unable to work things properly after that.
> 
> Two things could be tried:
> 1) have python built with unicode support on OSX.
> 2) "vet" numpy to convert the headers in /Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include/numpy/ to plain text.
> Actually you probably can do that easily and manually right now on the installed
> headers.
Umm... except that I have no idea how I might do that.  What exact changes would I need to make to Python.h (and/or something else)?   It seems unwise to make yet another python spkg change to deal with this; did numpy only recently (between whatever Sage has now and 1.4.1) start making its headers unicode?  I am not exactly a C expert.

That said, 1) seems to be more canonical, though I guess if it makes it work, 2) could be an option.  This is the sort of thing Leif and/or drkirkby usually have an informed opinion on...
> Give it a spin and see if it works. If it does we'll have to do something about
> that piece of unicode one way or another.



---

archive/issue_comments_096490.json:
```json
{
    "body": "2) would be good to find if this is indeed the problem.\nDoing it is another story. Do you have iconv on OSX?\nI would think so as it is needed by R amongst other.\n\nso go into the right folder and try:\n\n```\niconv -f UTF-8 -t ISO-8859-1 *.h\n```\n",
    "created_at": "2010-09-08T09:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96490",
    "user": "@kiwifb"
}
```

2) would be good to find if this is indeed the problem.
Doing it is another story. Do you have iconv on OSX?
I would think so as it is needed by R amongst other.

so go into the right folder and try:

```
iconv -f UTF-8 -t ISO-8859-1 *.h
```




---

archive/issue_comments_096491.json:
```json
{
    "body": "Same error.",
    "created_at": "2010-09-08T16:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96491",
    "user": "@kcrisman"
}
```

Same error.



---

archive/issue_comments_096492.json:
```json
{
    "body": "In the spkg-install, there is the line\n\n\n```\nunset CFLAGS LDFLAGS CXXFLAGS SHAREDFLAGS\n```\n\n\ncould this be somehow connected to our problem, because if we unset the flags, gcc doesn't point at Python.h in OS X?",
    "created_at": "2010-09-08T18:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96492",
    "user": "maldun"
}
```

In the spkg-install, there is the line


```
unset CFLAGS LDFLAGS CXXFLAGS SHAREDFLAGS
```


could this be somehow connected to our problem, because if we unset the flags, gcc doesn't point at Python.h in OS X?



---

archive/issue_comments_096493.json:
```json
{
    "body": "Replying to [comment:75 maldun]:\n> In the spkg-install, there is the line\n> \n> {{{\n> unset CFLAGS LDFLAGS CXXFLAGS SHAREDFLAGS\n> }}}\n> \n> could this be somehow connected to our problem, because if we unset the flags, gcc doesn't point at Python.h in OS X?\nOk I reformulate it: Can we use the CFLAGS and LDFLAGS to give to tell gcc to link Python.h directly?",
    "created_at": "2010-09-08T18:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96493",
    "user": "maldun"
}
```

Replying to [comment:75 maldun]:
> In the spkg-install, there is the line
> 
> {{{
> unset CFLAGS LDFLAGS CXXFLAGS SHAREDFLAGS
> }}}
> 
> could this be somehow connected to our problem, because if we unset the flags, gcc doesn't point at Python.h in OS X?
Ok I reformulate it: Can we use the CFLAGS and LDFLAGS to give to tell gcc to link Python.h directly?



---

archive/issue_comments_096494.json:
```json
{
    "body": "Replying to [comment:75 maldun]:\n> In the spkg-install, there is the line\n> \n> {{{\n> unset CFLAGS LDFLAGS CXXFLAGS SHAREDFLAGS\n> }}}\n> \n> could this be somehow connected to our problem, because if we unset the flags, gcc doesn't point at Python.h in OS X?\n\nBut this is not a change in the spkg-install script.  Sage has built fine on this computer in the very recent past.  The new spkg also works fine on other (newer) Macs.\n\nFrom the numpy website\n\n```\nReusing npymath\n\nIn 1.3.0, we started putting portable C math routines in npymath library, so that people can use those to write portable extensions. Unfortunately, it was not possible to easily link against this library: in 1.4.0, support has been added to numpy.distutils so that 3rd party can reuse this library. See coremath documentation for more information.\n```\n\nThis seems quite possibly relevant (given the error message).  After all, if `Python.h` isn't imported, then maybe the first error seen is that `PY_UNICODE_DEF` or whatever it's called wouldn't be set... maybe?  \n\nI'm just trying to throw out an idea here, I am woefully uniformed when it comes to headers and things like that.  But I feel like it has to be a change in Scipy or Numpy, since the previous Sage built fine on this machine.",
    "created_at": "2010-09-08T19:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96494",
    "user": "@kcrisman"
}
```

Replying to [comment:75 maldun]:
> In the spkg-install, there is the line
> 
> {{{
> unset CFLAGS LDFLAGS CXXFLAGS SHAREDFLAGS
> }}}
> 
> could this be somehow connected to our problem, because if we unset the flags, gcc doesn't point at Python.h in OS X?

But this is not a change in the spkg-install script.  Sage has built fine on this computer in the very recent past.  The new spkg also works fine on other (newer) Macs.

From the numpy website

```
Reusing npymath

In 1.3.0, we started putting portable C math routines in npymath library, so that people can use those to write portable extensions. Unfortunately, it was not possible to easily link against this library: in 1.4.0, support has been added to numpy.distutils so that 3rd party can reuse this library. See coremath documentation for more information.
```

This seems quite possibly relevant (given the error message).  After all, if `Python.h` isn't imported, then maybe the first error seen is that `PY_UNICODE_DEF` or whatever it's called wouldn't be set... maybe?  

I'm just trying to throw out an idea here, I am woefully uniformed when it comes to headers and things like that.  But I feel like it has to be a change in Scipy or Numpy, since the previous Sage built fine on this machine.



---

archive/issue_comments_096495.json:
```json
{
    "body": "I have another wild theory: \nHaven't you said, that the package build one time? And then not. Is this correct?\n\nThe only thing I changed was updating the mercurial files, and then commiting. Therefore I had to write the commit messages, and I do this in kate. kate's standard encoding is utf-8. ( My computer's language is german, so everything is utf-8)\nThis  (or just packing it, because the encoding on my machine is not unicode) did change something to the encoding.\nWhat happens if you untar the package use the iconv from up there, and repack it on your machine?",
    "created_at": "2010-09-08T22:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96495",
    "user": "maldun"
}
```

I have another wild theory: 
Haven't you said, that the package build one time? And then not. Is this correct?

The only thing I changed was updating the mercurial files, and then commiting. Therefore I had to write the commit messages, and I do this in kate. kate's standard encoding is utf-8. ( My computer's language is german, so everything is utf-8)
This  (or just packing it, because the encoding on my machine is not unicode) did change something to the encoding.
What happens if you untar the package use the iconv from up there, and repack it on your machine?



---

archive/issue_comments_096496.json:
```json
{
    "body": "Replying to [comment:78 maldun]:\n> I have another wild theory: \n> Haven't you said, that the package build one time? And then not. Is this correct?\n> \n> The only thing I changed was updating the mercurial files, and then commiting. Therefore I had to write the commit messages, and I do this in kate. kate's standard encoding is utf-8. ( My computer's language is german, so everything is utf-8)\n> This  (or just packing it, because the encoding on my machine is not unicode) did change something to the encoding.\n> What happens if you untar the package use the iconv from up there, and repack it on your machine?\n\nI don't think so but it can be tested I guess. I think Karl is on something,\nI am having a look at scipy's spkg-install to see if there is something that should be done there.\n\n\nI have an endianess problem with numpy-1.4.1 on linux ppc, funny it works on\nppc OSX: [http://projects.scipy.org/numpy/ticket/1403](http://projects.scipy.org/numpy/ticket/1403) and [http://bugs.gentoo.org/show_bug.cgi?id=306237](http://bugs.gentoo.org/show_bug.cgi?id=306237) on the other hand numpy-1.5.0\nbuilt on my test machine. I am trying to find the changeset that made it possible to see if it is worth backporting.",
    "created_at": "2010-09-09T00:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96496",
    "user": "@kiwifb"
}
```

Replying to [comment:78 maldun]:
> I have another wild theory: 
> Haven't you said, that the package build one time? And then not. Is this correct?
> 
> The only thing I changed was updating the mercurial files, and then commiting. Therefore I had to write the commit messages, and I do this in kate. kate's standard encoding is utf-8. ( My computer's language is german, so everything is utf-8)
> This  (or just packing it, because the encoding on my machine is not unicode) did change something to the encoding.
> What happens if you untar the package use the iconv from up there, and repack it on your machine?

I don't think so but it can be tested I guess. I think Karl is on something,
I am having a look at scipy's spkg-install to see if there is something that should be done there.


I have an endianess problem with numpy-1.4.1 on linux ppc, funny it works on
ppc OSX: [http://projects.scipy.org/numpy/ticket/1403](http://projects.scipy.org/numpy/ticket/1403) and [http://bugs.gentoo.org/show_bug.cgi?id=306237](http://bugs.gentoo.org/show_bug.cgi?id=306237) on the other hand numpy-1.5.0
built on my test machine. I am trying to find the changeset that made it possible to see if it is worth backporting.



---

archive/issue_comments_096497.json:
```json
{
    "body": "Replying to [comment:74 kcrisman]:\n> Same error.\nIt may sound unrelated but what fortran compiler are you using in your\nsage install? g95 or gfortran?\n\nIn any case I think some of the patches in scipy would need rebasing.\nBut the fact of the matter is that they are g95 dependent and we dropped\ng95 - I already did so in numpy so we should do it as well in scipy.",
    "created_at": "2010-09-09T02:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96497",
    "user": "@kiwifb"
}
```

Replying to [comment:74 kcrisman]:
> Same error.
It may sound unrelated but what fortran compiler are you using in your
sage install? g95 or gfortran?

In any case I think some of the patches in scipy would need rebasing.
But the fact of the matter is that they are g95 dependent and we dropped
g95 - I already did so in numpy so we should do it as well in scipy.



---

archive/issue_comments_096498.json:
```json
{
    "body": "I don't know exactly, but recall that Sage still includes Fortran compilers for Mac (see [here](http://www.sagemath.org/doc/installation/source.html)).  This is an spkg (sage-fortran...).   From the spkg readme:\n\n\n```\n# gFortran\n\n## Description\n\nG95 is a stable, production Fortran 95 compiler available for multiple\nCPU architectures and operating systems.\n\n## Upstream contacts\n\nURL: http://ftp.g95.org\n     http://www.g95.org\n\n```\n\nSo I don't know how to answer your question - apparently it's both gfortran and g95 :)  The spkg-install has more details on this, but it apparently depends on the version (there are different .bz2 files for different Macs); my old PPC Mac would have used g95, I think.  Is there some technical reason we should drop this?\n\nResponding to the other comment, sadly, although I thought Scipy installed correctly at first, my machine is REALLY slow, so eventually it turned out that it didn't.  I succeeded on a newer Intel Mac, but that is unrelated.",
    "created_at": "2010-09-09T02:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96498",
    "user": "@kcrisman"
}
```

I don't know exactly, but recall that Sage still includes Fortran compilers for Mac (see [here](http://www.sagemath.org/doc/installation/source.html)).  This is an spkg (sage-fortran...).   From the spkg readme:


```
# gFortran

## Description

G95 is a stable, production Fortran 95 compiler available for multiple
CPU architectures and operating systems.

## Upstream contacts

URL: http://ftp.g95.org
     http://www.g95.org

```

So I don't know how to answer your question - apparently it's both gfortran and g95 :)  The spkg-install has more details on this, but it apparently depends on the version (there are different .bz2 files for different Macs); my old PPC Mac would have used g95, I think.  Is there some technical reason we should drop this?

Responding to the other comment, sadly, although I thought Scipy installed correctly at first, my machine is REALLY slow, so eventually it turned out that it didn't.  I succeeded on a newer Intel Mac, but that is unrelated.



---

archive/issue_comments_096499.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-09T04:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96499",
    "user": "@kiwifb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096500.json:
```json
{
    "body": "See comment 10 by Dave. g95 can be removed. Unless they forgot about\nOSX ppc. For my question, what does \n\n```\n$SAGE_LOCAL/bin/sage_fortran --version\n```\n\nsays? I am guessing we have gfortran binaries for all platforms. \nDropping g95 means that we can remove some (ugly) patches for numpy/scipy\nthere are probably other valid reasons to do so but generally speaking that's less work. \n\nI removed all patches that were applied for g95 in numpy, so if you have g95 the problems may come from there.\n\nI share your pain about building on ppc (although I dropped OS X sometimes\nago, this is now linux only and gentoo so everything or almost install from sources. openoffice-3.1 clocks in at 27 hours to build). Did you mean that numpy failed or restating that scipy failed in your latest comment?\n\nIf numpy fails for you as well on OSX ppc we may have a strong motivation to move to 1.5.0 again.\n\nI am changing this to need_works until we work out what's wrong in your case.",
    "created_at": "2010-09-09T04:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96500",
    "user": "@kiwifb"
}
```

See comment 10 by Dave. g95 can be removed. Unless they forgot about
OSX ppc. For my question, what does 

```
$SAGE_LOCAL/bin/sage_fortran --version
```

says? I am guessing we have gfortran binaries for all platforms. 
Dropping g95 means that we can remove some (ugly) patches for numpy/scipy
there are probably other valid reasons to do so but generally speaking that's less work. 

I removed all patches that were applied for g95 in numpy, so if you have g95 the problems may come from there.

I share your pain about building on ppc (although I dropped OS X sometimes
ago, this is now linux only and gentoo so everything or almost install from sources. openoffice-3.1 clocks in at 27 hours to build). Did you mean that numpy failed or restating that scipy failed in your latest comment?

If numpy fails for you as well on OSX ppc we may have a strong motivation to move to 1.5.0 again.

I am changing this to need_works until we work out what's wrong in your case.



---

archive/issue_comments_096501.json:
```json
{
    "body": "Replying to [comment:82 fbissey]:\n\n> If numpy fails for you as well on OSX ppc we may have a strong motivation to move to 1.5.0 again.\n> \n\nIf you want I can prepare a package for 1.5.0 with the patch from the numpy trac, and run the doctests, in the evening.",
    "created_at": "2010-09-09T08:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96501",
    "user": "maldun"
}
```

Replying to [comment:82 fbissey]:

> If numpy fails for you as well on OSX ppc we may have a strong motivation to move to 1.5.0 again.
> 

If you want I can prepare a package for 1.5.0 with the patch from the numpy trac, and run the doctests, in the evening.



---

archive/issue_comments_096502.json:
```json
{
    "body": "Numpy was fine in all cases; Scipy was what didn't build. drkirkby's comment \"There are g95 binaries in the Fortran package in Sage, but William said they can be removed.\" may not be true.\n\nThe command that supposedly checks which version I have returns with an error:\n\n```\nlocal/bin/sage_fortran: line 3: sage_fortran.bin: command not found\n```\n\nThis also happens on my (successful) build of 4.6.prealpha4, so maybe the command is wrong?\n\nIncidentally, does this ticket do anything with respect to #7831 and #8010?  Just curious.",
    "created_at": "2010-09-09T12:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96502",
    "user": "@kcrisman"
}
```

Numpy was fine in all cases; Scipy was what didn't build. drkirkby's comment "There are g95 binaries in the Fortran package in Sage, but William said they can be removed." may not be true.

The command that supposedly checks which version I have returns with an error:

```
local/bin/sage_fortran: line 3: sage_fortran.bin: command not found
```

This also happens on my (successful) build of 4.6.prealpha4, so maybe the command is wrong?

Incidentally, does this ticket do anything with respect to #7831 and #8010?  Just curious.



---

archive/issue_comments_096503.json:
```json
{
    "body": "Okay, I finally figured out how to check this - I had to run the binary directly, the scripts didn't work.\n\n```\nG95 (GCC 4.0.3 (g95 0.91!) Jun 4 2007)\n```\n\netcetera.  On my Macintel, I get\n\n```\nGNU Fortran (GCC) 4.2.3\nCopyright (C) 2007 Free Software Foundation, Inc.\n```\n\nSo yes, it is using G95 on Tiger.",
    "created_at": "2010-09-09T15:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96503",
    "user": "@kcrisman"
}
```

Okay, I finally figured out how to check this - I had to run the binary directly, the scripts didn't work.

```
G95 (GCC 4.0.3 (g95 0.91!) Jun 4 2007)
```

etcetera.  On my Macintel, I get

```
GNU Fortran (GCC) 4.2.3
Copyright (C) 2007 Free Software Foundation, Inc.
```

So yes, it is using G95 on Tiger.



---

archive/issue_comments_096504.json:
```json
{
    "body": "It would be great if this is the problem and it can somehow be solved!\n\nAnother thing: I builded numpy-1.5.0 with the new patch now. There only failed some doctests because numpy is throwing some new warnings.\nWant to give it a try? Perhaps the problem is then obsolete with scipy 0.8. also?\nI personally would prefer to stick to 1.4.1, but well it is like it is...",
    "created_at": "2010-09-09T21:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96504",
    "user": "maldun"
}
```

It would be great if this is the problem and it can somehow be solved!

Another thing: I builded numpy-1.5.0 with the new patch now. There only failed some doctests because numpy is throwing some new warnings.
Want to give it a try? Perhaps the problem is then obsolete with scipy 0.8. also?
I personally would prefer to stick to 1.4.1, but well it is like it is...



---

archive/issue_comments_096505.json:
```json
{
    "body": "If you post it, I can try it - though it might be after the weekend, depending on my physical access to that particular box.\n\nfbissey - can you explain (in layman's terms) how having the wrong fortran compiler might affect things?  It does confuse me :)",
    "created_at": "2010-09-09T22:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96505",
    "user": "@kcrisman"
}
```

If you post it, I can try it - though it might be after the weekend, depending on my physical access to that particular box.

fbissey - can you explain (in layman's terms) how having the wrong fortran compiler might affect things?  It does confuse me :)



---

archive/issue_comments_096506.json:
```json
{
    "body": "Replying to [comment:87 kcrisman]:\n> If you post it, I can try it - though it might be after the weekend, depending on my physical access to that particular box.\n> \n> fbissey - can you explain (in layman's terms) how having the wrong fortran compiler might affect things?  It does confuse me :)\n\nUp and ready!\n\nYes this would be interesting! I don't really get it either because it looks more like a C problem to me?",
    "created_at": "2010-09-09T23:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96506",
    "user": "maldun"
}
```

Replying to [comment:87 kcrisman]:
> If you post it, I can try it - though it might be after the weekend, depending on my physical access to that particular box.
> 
> fbissey - can you explain (in layman's terms) how having the wrong fortran compiler might affect things?  It does confuse me :)

Up and ready!

Yes this would be interesting! I don't really get it either because it looks more like a C problem to me?



---

archive/issue_comments_096507.json:
```json
{
    "body": "http://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.5.0.spkg&can=2&q=#makechanges",
    "created_at": "2010-09-09T23:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96507",
    "user": "maldun"
}
```

http://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.5.0.spkg&can=2&q=#makechanges



---

archive/issue_comments_096508.json:
```json
{
    "body": "It's more of a hunch than anything special I'll admit to that. The numpy/scipy connection seems to be fragile so I am not discounting it. In actual fact the fortran compiler is used only to compile one file in the whole of numpy (lapack_lite.so). I am more worried that it mixes up the toolchain it prepares for scipy.\n\n\nOne thing I'd like to see however is a complete build log for scipy not just the failing bit. There may be clues earlier in the process.",
    "created_at": "2010-09-09T23:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96508",
    "user": "@kiwifb"
}
```

It's more of a hunch than anything special I'll admit to that. The numpy/scipy connection seems to be fragile so I am not discounting it. In actual fact the fortran compiler is used only to compile one file in the whole of numpy (lapack_lite.so). I am more worried that it mixes up the toolchain it prepares for scipy.


One thing I'd like to see however is a complete build log for scipy not just the failing bit. There may be clues earlier in the process.



---

archive/issue_comments_096509.json:
```json
{
    "body": "Replying to [comment:88 maldun]:\n> Replying to [comment:87 kcrisman]:\n> > If you post it, I can try it - though it might be after the weekend, depending on my physical access to that particular box.\n> > \n> > fbissey - can you explain (in layman's terms) how having the wrong fortran compiler might affect things?  It does confuse me :)\n> \n> Up and ready!\n\nSorry, fails with exactly the same error (on a different box with similar specs, same G95 in its Sage).  So for now probably stick with the better-tested 1.4.1 for numpy.  Hopefully we can figure out what's going on here.\n\nThe logs for the numpy (1.5.0) and scipy are in [this](http://sage.math.washington.edu/home/kcrisman/) directory, from the second computer.  Happy hunting!  By the way, Python.h is clearly working fine elsewhere in these logs, and sage_fortran compiles all kinds of neat stuff up to that point.",
    "created_at": "2010-09-10T00:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96509",
    "user": "@kcrisman"
}
```

Replying to [comment:88 maldun]:
> Replying to [comment:87 kcrisman]:
> > If you post it, I can try it - though it might be after the weekend, depending on my physical access to that particular box.
> > 
> > fbissey - can you explain (in layman's terms) how having the wrong fortran compiler might affect things?  It does confuse me :)
> 
> Up and ready!

Sorry, fails with exactly the same error (on a different box with similar specs, same G95 in its Sage).  So for now probably stick with the better-tested 1.4.1 for numpy.  Hopefully we can figure out what's going on here.

The logs for the numpy (1.5.0) and scipy are in [this](http://sage.math.washington.edu/home/kcrisman/) directory, from the second computer.  Happy hunting!  By the way, Python.h is clearly working fine elsewhere in these logs, and sage_fortran compiles all kinds of neat stuff up to that point.



---

archive/issue_comments_096510.json:
```json
{
    "body": "Replying to [comment:91 kcrisman]:\n> Replying to [comment:88 maldun]:\n> > Replying to [comment:87 kcrisman]:\n> > > If you post it, I can try it - though it might be after the weekend, depending on my physical access to that particular box.\n> > > \n> > > fbissey - can you explain (in layman's terms) how having the wrong fortran compiler might affect things?  It does confuse me :)\n> > \n> > Up and ready!\n> \n> Sorry, fails with exactly the same error (on a different box with similar specs, same G95 in its Sage).  So for now probably stick with the better-tested 1.4.1 for numpy.  Hopefully we can figure out what's going on here.\n> \n> The logs for the numpy (1.5.0) and scipy are in [this](http://sage.math.washington.edu/home/kcrisman/) directory, from the second computer.  Happy hunting!  By the way, Python.h is clearly working fine elsewhere in these logs, and sage_fortran compiles all kinds of neat stuff up to that point. \n\n\nThanks for the logs. Sorry to be a bother but would you have old build logs for scipy-0.7 as well? Since I don't have a ppc OSX setup that would be very useful to \nhave a successful log even from an older version of scipy.",
    "created_at": "2010-09-10T00:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96510",
    "user": "@kiwifb"
}
```

Replying to [comment:91 kcrisman]:
> Replying to [comment:88 maldun]:
> > Replying to [comment:87 kcrisman]:
> > > If you post it, I can try it - though it might be after the weekend, depending on my physical access to that particular box.
> > > 
> > > fbissey - can you explain (in layman's terms) how having the wrong fortran compiler might affect things?  It does confuse me :)
> > 
> > Up and ready!
> 
> Sorry, fails with exactly the same error (on a different box with similar specs, same G95 in its Sage).  So for now probably stick with the better-tested 1.4.1 for numpy.  Hopefully we can figure out what's going on here.
> 
> The logs for the numpy (1.5.0) and scipy are in [this](http://sage.math.washington.edu/home/kcrisman/) directory, from the second computer.  Happy hunting!  By the way, Python.h is clearly working fine elsewhere in these logs, and sage_fortran compiles all kinds of neat stuff up to that point. 


Thanks for the logs. Sorry to be a bother but would you have old build logs for scipy-0.7 as well? Since I don't have a ppc OSX setup that would be very useful to 
have a successful log even from an older version of scipy.



---

archive/issue_comments_096511.json:
```json
{
    "body": "> > Sorry, fails with exactly the same error (on a different box with similar specs, same G95 in its Sage).  So for now probably stick with the better-tested 1.4.1 for numpy.  Hopefully we can figure out what's going on here.\n> > \n> > The logs for the numpy (1.5.0) and scipy are in [this](http://sage.math.washington.edu/home/kcrisman/) directory, from the second computer.  Happy hunting!  By the way, Python.h is clearly working fine elsewhere in these logs, and sage_fortran compiles all kinds of neat stuff up to that point. \n> \n> \n> Thanks for the logs. Sorry to be a bother but would you have old build logs for scipy-0.7 as well? Since I don't have a ppc OSX setup that would be very useful to \n> have a successful log even from an older version of scipy.\nLook in the same place, just posted it.  So nice to be operating at 1.25 GHz instead of 700 MHz... \n\nAlso, interestingly, I now have a \"mixed\" installation on this computer:\n\n```\nsage: import numpy\nsage: numpy.version.version\n'1.5.0'\nsage: import scipy\nsage: scipy.version.version\n'0.7.0'\n```\n\nAt least some of the relevant tests seem to pass with this, though of course I get the RunTimeErrors mentioned above and did `Inf`  and `inf` change places?  I know little about numpy and scipy, though.  Anyway, that's better than on the other box, whose issues with bad tarballs seem to not exist on this box.",
    "created_at": "2010-09-10T00:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96511",
    "user": "@kcrisman"
}
```

> > Sorry, fails with exactly the same error (on a different box with similar specs, same G95 in its Sage).  So for now probably stick with the better-tested 1.4.1 for numpy.  Hopefully we can figure out what's going on here.
> > 
> > The logs for the numpy (1.5.0) and scipy are in [this](http://sage.math.washington.edu/home/kcrisman/) directory, from the second computer.  Happy hunting!  By the way, Python.h is clearly working fine elsewhere in these logs, and sage_fortran compiles all kinds of neat stuff up to that point. 
> 
> 
> Thanks for the logs. Sorry to be a bother but would you have old build logs for scipy-0.7 as well? Since I don't have a ppc OSX setup that would be very useful to 
> have a successful log even from an older version of scipy.
Look in the same place, just posted it.  So nice to be operating at 1.25 GHz instead of 700 MHz... 

Also, interestingly, I now have a "mixed" installation on this computer:

```
sage: import numpy
sage: numpy.version.version
'1.5.0'
sage: import scipy
sage: scipy.version.version
'0.7.0'
```

At least some of the relevant tests seem to pass with this, though of course I get the RunTimeErrors mentioned above and did `Inf`  and `inf` change places?  I know little about numpy and scipy, though.  Anyway, that's better than on the other box, whose issues with bad tarballs seem to not exist on this box.



---

archive/issue_comments_096512.json:
```json
{
    "body": "Replying to [comment:93 kcrisman]:\n> Look in the same place, just posted it.  So nice to be operating at 1.25 GHz instead of 700 MHz... \n> \n> Also, interestingly, I now have a \"mixed\" installation on this computer:\n> {{{\n> sage: import numpy\n> sage: numpy.version.version\n> '1.5.0'\n> sage: import scipy\n> sage: scipy.version.version\n> '0.7.0'\n> }}}\n> At least some of the relevant tests seem to pass with this, though of course I get the RunTimeErrors mentioned above and did `Inf`  and `inf` change places?  I know little about numpy and scipy, though.  Anyway, that's better than on the other box, whose issues with bad tarballs seem to not exist on this box.\n\nFound the logs, I may have a theory and the logs may help to (in)validate it.\nNot sure about Inf/inf either. scipy should work fine with numpy-1.5 - once rebuilt,\nand sage needs rebuilding too. That may get rid of some of these runtime errors.\nscipy-0.8 needs numpy-1.4 minimum on the other hand.",
    "created_at": "2010-09-10T00:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96512",
    "user": "@kiwifb"
}
```

Replying to [comment:93 kcrisman]:
> Look in the same place, just posted it.  So nice to be operating at 1.25 GHz instead of 700 MHz... 
> 
> Also, interestingly, I now have a "mixed" installation on this computer:
> {{{
> sage: import numpy
> sage: numpy.version.version
> '1.5.0'
> sage: import scipy
> sage: scipy.version.version
> '0.7.0'
> }}}
> At least some of the relevant tests seem to pass with this, though of course I get the RunTimeErrors mentioned above and did `Inf`  and `inf` change places?  I know little about numpy and scipy, though.  Anyway, that's better than on the other box, whose issues with bad tarballs seem to not exist on this box.

Found the logs, I may have a theory and the logs may help to (in)validate it.
Not sure about Inf/inf either. scipy should work fine with numpy-1.5 - once rebuilt,
and sage needs rebuilding too. That may get rid of some of these runtime errors.
scipy-0.8 needs numpy-1.4 minimum on the other hand.



---

archive/issue_comments_096513.json:
```json
{
    "body": "> > Also, interestingly, I now have a \"mixed\" installation on this computer:\n> > {{{\n> > sage: import numpy\n> > sage: numpy.version.version\n> > '1.5.0'\n> > sage: import scipy\n> > sage: scipy.version.version\n> > '0.7.0'\n> > }}}\n> > At least some of the relevant tests seem to pass with this, though of course I get the RunTimeErrors mentioned above and did `Inf`  and `inf` change places?  I know little about numpy and scipy, though.  Anyway, that's better than on the other box, whose issues with bad tarballs seem to not exist on this box.\n> \n> Found the logs, I may have a theory and the logs may help to (in)validate it.\n> Not sure about Inf/inf either. scipy should work fine with numpy-1.5 - once rebuilt,\n> and sage needs rebuilding too. That may get rid of some of these runtime errors.\n> scipy-0.8 needs numpy-1.4 minimum on the other hand. \n\nYup, tests in relevant modules are passing, with only the `RuntimeWarning`s (not errors, sorry for that) in general marring things (as noted, one or two other very minor things).  Anyway, none of this not compiling nonsense, so something must have changed in Scipy 0.8 from 0.7 - maybe something that used that change mentioned above about reusing `npymath`.  There were indeed a couple changes to the `gammaincinv` function in Scipy, if you look at their changesets, but as a non-expert how those could have resulted in this Python.h/unicode error is totally beyond me.",
    "created_at": "2010-09-10T01:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96513",
    "user": "@kcrisman"
}
```

> > Also, interestingly, I now have a "mixed" installation on this computer:
> > {{{
> > sage: import numpy
> > sage: numpy.version.version
> > '1.5.0'
> > sage: import scipy
> > sage: scipy.version.version
> > '0.7.0'
> > }}}
> > At least some of the relevant tests seem to pass with this, though of course I get the RunTimeErrors mentioned above and did `Inf`  and `inf` change places?  I know little about numpy and scipy, though.  Anyway, that's better than on the other box, whose issues with bad tarballs seem to not exist on this box.
> 
> Found the logs, I may have a theory and the logs may help to (in)validate it.
> Not sure about Inf/inf either. scipy should work fine with numpy-1.5 - once rebuilt,
> and sage needs rebuilding too. That may get rid of some of these runtime errors.
> scipy-0.8 needs numpy-1.4 minimum on the other hand. 

Yup, tests in relevant modules are passing, with only the `RuntimeWarning`s (not errors, sorry for that) in general marring things (as noted, one or two other very minor things).  Anyway, none of this not compiling nonsense, so something must have changed in Scipy 0.8 from 0.7 - maybe something that used that change mentioned above about reusing `npymath`.  There were indeed a couple changes to the `gammaincinv` function in Scipy, if you look at their changesets, but as a non-expert how those could have resulted in this Python.h/unicode error is totally beyond me.



---

archive/issue_comments_096514.json:
```json
{
    "body": "Interestingly enough on Gentoo we have -I/usr/include/python2.6 added to the compilation flags everywhere. I wonder if just finding a way of adding -I${SAGE_LOCAL}/include/python2.6 in sage would help at all. The mystery then\nwould be \"how did it work before?\" Furthermore why is it not needed for the earlier\nC compilations.... or on other platforms? May be we are using system python headers without knowing it?\n\nI will work on that over the week end. Hopefully by Monday I will have something you can test.",
    "created_at": "2010-09-10T01:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96514",
    "user": "@kiwifb"
}
```

Interestingly enough on Gentoo we have -I/usr/include/python2.6 added to the compilation flags everywhere. I wonder if just finding a way of adding -I${SAGE_LOCAL}/include/python2.6 in sage would help at all. The mystery then
would be "how did it work before?" Furthermore why is it not needed for the earlier
C compilations.... or on other platforms? May be we are using system python headers without knowing it?

I will work on that over the week end. Hopefully by Monday I will have something you can test.



---

archive/issue_comments_096515.json:
```json
{
    "body": "It turns out to be more subtle than I thought and I don't know yet why.\n\nIt is not easy to add -I${SAGE_LOCAL}/include/python2.6 to compile options, in any case many other compilation lines actually have it already. After careful checking, I found that this particular option is not used in any scipy-0.7.x log I had on sage or Gentoo for these particular objects.\nBut I see it in scipy-0.8.0 in Gentoo. \n\nI am messing up with some of my system at the moment so I cannot generate a successful build log of scipy-0.8.0 from sage at the moment. But it would be interesting to know if this particular compilation option has been added in the successful builds.",
    "created_at": "2010-09-12T22:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96515",
    "user": "@kiwifb"
}
```

It turns out to be more subtle than I thought and I don't know yet why.

It is not easy to add -I${SAGE_LOCAL}/include/python2.6 to compile options, in any case many other compilation lines actually have it already. After careful checking, I found that this particular option is not used in any scipy-0.7.x log I had on sage or Gentoo for these particular objects.
But I see it in scipy-0.8.0 in Gentoo. 

I am messing up with some of my system at the moment so I cannot generate a successful build log of scipy-0.8.0 from sage at the moment. But it would be interesting to know if this particular compilation option has been added in the successful builds.



---

archive/issue_comments_096516.json:
```json
{
    "body": "OK - so there is a fair difference on that file between 0.7.2 and 0.8.0.\n\nheaders in gammaincinv.c in 0.7.2\n\n```\n#include <stdio.h>\n#include <math.h>\n#include \"../cephes.h\"\n#undef fabs\n#include \"misc.h\"\n```\n\nin 0.8.0\n\n```\n#include <Python.h>\n#include <numpy/npy_math.h>\n\n#include <stdio.h>\n#include <math.h>\n\n#include \"../cephes.h\"\n#undef fabs\n#include \"misc.h\"\n```\n\nSo it will be very interesting to get a successful build log of scipy-0.8.0\nin sage for inspection. A quick and dirty fix would be to change <Python.h>\nto <python2.6/Python.h> and I am not completely sure it would  work either.\n\nThere are a few more Python.h header in that folder so just fixing that one may not work:\n\n```\ngrep -r \"Python\\.h\" *\namos_wrappers.h:#include \"Python.h\"\ncdf_wrappers.h:#include \"Python.h\"\ncephes/sici.c:#include <Python.h>\ncephes/mconf.h:#include <Python.h>\n_cephesmodule.c:#include \"Python.h\"\nc_misc/gammaincinv.c:#include <Python.h>\nlambertw.c:#include \"Python.h\"\northogonal_eval.c:#include \"Python.h\"\nspecfun_wrappers.h:#include \"Python.h\"\ntoms_wrappers.h:#include \"Python.h\"\nufunc_extras.h:#include \"Python.h\"\n```\n\nconsidering the SConscript the files in the cephes subfolder will probably be trouble too.",
    "created_at": "2010-09-13T01:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96516",
    "user": "@kiwifb"
}
```

OK - so there is a fair difference on that file between 0.7.2 and 0.8.0.

headers in gammaincinv.c in 0.7.2

```
#include <stdio.h>
#include <math.h>
#include "../cephes.h"
#undef fabs
#include "misc.h"
```

in 0.8.0

```
#include <Python.h>
#include <numpy/npy_math.h>

#include <stdio.h>
#include <math.h>

#include "../cephes.h"
#undef fabs
#include "misc.h"
```

So it will be very interesting to get a successful build log of scipy-0.8.0
in sage for inspection. A quick and dirty fix would be to change <Python.h>
to <python2.6/Python.h> and I am not completely sure it would  work either.

There are a few more Python.h header in that folder so just fixing that one may not work:

```
grep -r "Python\.h" *
amos_wrappers.h:#include "Python.h"
cdf_wrappers.h:#include "Python.h"
cephes/sici.c:#include <Python.h>
cephes/mconf.h:#include <Python.h>
_cephesmodule.c:#include "Python.h"
c_misc/gammaincinv.c:#include <Python.h>
lambertw.c:#include "Python.h"
orthogonal_eval.c:#include "Python.h"
specfun_wrappers.h:#include "Python.h"
toms_wrappers.h:#include "Python.h"
ufunc_extras.h:#include "Python.h"
```

considering the SConscript the files in the cephes subfolder will probably be trouble too.



---

archive/issue_comments_096517.json:
```json
{
    "body": "But it would nice to know anyway. If it doesn't work with gammaincinv.c, at least the  error message would change. Providing a patch would then be easy for me.\n\nIronically I already had asked if this had could been the problem...\nThe only thing what me disturbs is the this entry in the error log of kcrisman:  \n\n```\n...y/npy_common.h:79:2: error: #error Must use Python with unicode enabled.\n```\n\nThis sounds more like that unicode isn't enabled, and perhaps this is related to native python installation on the system, and the gcc uses this header instead that from sage.\nI think to be absolutely sure, we should try also to set the path really to Python.h in the sage install in the header, if setting to <python2.6/Python.h> doesn't work.\n\n`@`fbissey Another question: would it help you, if you see my install log from ubuntu?",
    "created_at": "2010-09-13T08:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96517",
    "user": "maldun"
}
```

But it would nice to know anyway. If it doesn't work with gammaincinv.c, at least the  error message would change. Providing a patch would then be easy for me.

Ironically I already had asked if this had could been the problem...
The only thing what me disturbs is the this entry in the error log of kcrisman:  

```
...y/npy_common.h:79:2: error: #error Must use Python with unicode enabled.
```

This sounds more like that unicode isn't enabled, and perhaps this is related to native python installation on the system, and the gcc uses this header instead that from sage.
I think to be absolutely sure, we should try also to set the path really to Python.h in the sage install in the header, if setting to <python2.6/Python.h> doesn't work.

`@`fbissey Another question: would it help you, if you see my install log from ubuntu?



---

archive/issue_comments_096518.json:
```json
{
    "body": "No need for extra logs. I found the culprit and why it affects only Karl's ppc\nmachine. I point the finger to g95! or rather the fact that the patches that\nare installed if g95 is found should have been rebased. \n\nBasically the file special/setup.py is replaced by a version from scipy-0.7.0\nwhich doesn't need the python header. Could you please use spkg-install.2 attached \nin scipy-0.8.0 it doesn't use the patches for g95. It should work without special\npatch in my opinion anyway.",
    "created_at": "2010-09-13T08:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96518",
    "user": "@kiwifb"
}
```

No need for extra logs. I found the culprit and why it affects only Karl's ppc
machine. I point the finger to g95! or rather the fact that the patches that
are installed if g95 is found should have been rebased. 

Basically the file special/setup.py is replaced by a version from scipy-0.7.0
which doesn't need the python header. Could you please use spkg-install.2 attached 
in scipy-0.8.0 it doesn't use the patches for g95. It should work without special
patch in my opinion anyway.



---

archive/issue_comments_096519.json:
```json
{
    "body": "So I've packed the scipy with your spkg-install, but this time it doesn't work for me. I get this error:\n\n\n```\nHost system\nuname -a:\nLinux math181 2.6.31-22-generic #63-Ubuntu SMP Thu Aug 19 00:23:50 UTC 2010 x86_64 GNU/Linux\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: x86_64-linux-gnu\nConfigured with: ../src/configure -v --with-pkgversion='Ubuntu 4.4.1-4ubuntu9' --with-bugurl=file:///usr/share/doc/gcc-4.4/README.Bugs --enable-languages=c,c++,fortran,objc,obj-c++ --prefix=/usr --enable-shared --enable-multiarch --enable-linker-build-id --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.4 --program-suffix=-4.4 --enable-nls --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --disable-werror --with-arch-32=i486 --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu\nThread model: posix\ngcc version 4.4.1 (Ubuntu 4.4.1-4ubuntu9)\n****************************************************\ninvalid command name 'config_fc --noopt --noarch'\nError building scipy.\n\nreal    0m2.296s\n\n```\n",
    "created_at": "2010-09-13T10:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96519",
    "user": "maldun"
}
```

So I've packed the scipy with your spkg-install, but this time it doesn't work for me. I get this error:


```
Host system
uname -a:
Linux math181 2.6.31-22-generic #63-Ubuntu SMP Thu Aug 19 00:23:50 UTC 2010 x86_64 GNU/Linux
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 4.4.1-4ubuntu9' --with-bugurl=file:///usr/share/doc/gcc-4.4/README.Bugs --enable-languages=c,c++,fortran,objc,obj-c++ --prefix=/usr --enable-shared --enable-multiarch --enable-linker-build-id --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.4 --program-suffix=-4.4 --enable-nls --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --disable-werror --with-arch-32=i486 --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.4.1 (Ubuntu 4.4.1-4ubuntu9)
****************************************************
invalid command name 'config_fc --noopt --noarch'
Error building scipy.

real    0m2.296s

```




---

archive/issue_comments_096520.json:
```json
{
    "body": "I think I have gone overboard with double quotes, attaching a new version shortly.",
    "created_at": "2010-09-13T10:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96520",
    "user": "@kiwifb"
}
```

I think I have gone overboard with double quotes, attaching a new version shortly.



---

archive/issue_comments_096521.json:
```json
{
    "body": "Ok. I deleted all outdated patches like you suggested (initially I let them in, because they didn't any harm, and since I didn't know much about every detail of the patches, I first tried out if it works, but of course it's better to throw them out) and it builds without problem. But with the old spkg.\nthe spkg-install.2 you attached still, with the same error, because my machine doesn't know the command\nconfig_fc --noopt --noarch:\n\n```\ninvalid command name 'config_fc --noopt --noarch'\n```\n\n\ncould it be that I have to install something on my system? Or should we solve this with an If clause?",
    "created_at": "2010-09-13T11:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96521",
    "user": "maldun"
}
```

Ok. I deleted all outdated patches like you suggested (initially I let them in, because they didn't any harm, and since I didn't know much about every detail of the patches, I first tried out if it works, but of course it's better to throw them out) and it builds without problem. But with the old spkg.
the spkg-install.2 you attached still, with the same error, because my machine doesn't know the command
config_fc --noopt --noarch:

```
invalid command name 'config_fc --noopt --noarch'
```


could it be that I have to install something on my system? Or should we solve this with an If clause?



---

archive/issue_comments_096522.json:
```json
{
    "body": "ok I solved it: You forgot the \"-\" before the config =)",
    "created_at": "2010-09-13T11:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96522",
    "user": "maldun"
}
```

ok I solved it: You forgot the "-" before the config =)



---

archive/issue_comments_096523.json:
```json
{
    "body": "Attachment [spkg-install.2](tarball://root/attachments/some-uuid/ticket9808/spkg-install.2) by @kiwifb created at 2010-09-13 11:29:32\n\nnew replacement for scipy",
    "created_at": "2010-09-13T11:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96523",
    "user": "@kiwifb"
}
```

Attachment [spkg-install.2](tarball://root/attachments/some-uuid/ticket9808/spkg-install.2) by @kiwifb created at 2010-09-13 11:29:32

new replacement for scipy



---

archive/issue_comments_096524.json:
```json
{
    "body": "I think I found the problem, I think the shell was not set up properly.\n\nI mean, these are options passed to setup.py not separate commands.\nThey shouldn't be interpreted as such and aren't in the numpy spkg-install,\nso there are no reason why they should be in scipy.\nBut the shells for the two spkg-install were different so I think that may be \na point of bash/shell semantic. In which case I am curious to find out what I\nam supposed to do in sh. There is a new spkg-install.2 for you to try.",
    "created_at": "2010-09-13T11:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96524",
    "user": "@kiwifb"
}
```

I think I found the problem, I think the shell was not set up properly.

I mean, these are options passed to setup.py not separate commands.
They shouldn't be interpreted as such and aren't in the numpy spkg-install,
so there are no reason why they should be in scipy.
But the shells for the two spkg-install were different so I think that may be 
a point of bash/shell semantic. In which case I am curious to find out what I
am supposed to do in sh. There is a new spkg-install.2 for you to try.



---

archive/issue_comments_096525.json:
```json
{
    "body": "Replying to [comment:104 maldun]:\n> ok I solved it: You forgot the \"-\" before the config =)\n\nOk you posted while I was answering. That may pass but I am not sure that\ndoes what it's supposed to do. There shouldn't be a \"-\" in front. I suspect\nit is now just ignored.",
    "created_at": "2010-09-13T11:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96525",
    "user": "@kiwifb"
}
```

Replying to [comment:104 maldun]:
> ok I solved it: You forgot the "-" before the config =)

Ok you posted while I was answering. That may pass but I am not sure that
does what it's supposed to do. There shouldn't be a "-" in front. I suspect
it is now just ignored.



---

archive/issue_comments_096526.json:
```json
{
    "body": "ok I was to quick... indeed it builded, but not for too long: it took it a -c\"onfig_fc\"... so it didn't ignore, but missinterpreted it.\n\nBut the error remains. I don't really get it is there something different with ubuntu's gcc?",
    "created_at": "2010-09-13T11:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96526",
    "user": "maldun"
}
```

ok I was to quick... indeed it builded, but not for too long: it took it a -c"onfig_fc"... so it didn't ignore, but missinterpreted it.

But the error remains. I don't really get it is there something different with ubuntu's gcc?



---

archive/issue_comments_096527.json:
```json
{
    "body": "Ah okay: I looked into the scipy docu: This option seems to be for numpy, not for scipy.\nhttp://projects.scipy.org/numpy/wiki/DistutilsDoc#specifing-config-fc-options-for-libraries-in-setup-py-script\n\nBecause numpy builded with that command. Does it build on your system?",
    "created_at": "2010-09-13T11:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96527",
    "user": "maldun"
}
```

Ah okay: I looked into the scipy docu: This option seems to be for numpy, not for scipy.
http://projects.scipy.org/numpy/wiki/DistutilsDoc#specifing-config-fc-options-for-libraries-in-setup-py-script

Because numpy builded with that command. Does it build on your system?



---

archive/issue_comments_096528.json:
```json
{
    "body": "OK. I thought it was used in scipy as well. There seems to be 2 files with it, and it shouldn't have an impact. You can remove it then. Strange it doesn't generate errors in Gentoo.",
    "created_at": "2010-09-13T12:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96528",
    "user": "@kiwifb"
}
```

OK. I thought it was used in scipy as well. There seems to be 2 files with it, and it shouldn't have an impact. You can remove it then. Strange it doesn't generate errors in Gentoo.



---

archive/issue_comments_096529.json:
```json
{
    "body": "Ok updatet scipy package, with deleted patches",
    "created_at": "2010-09-13T13:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96529",
    "user": "maldun"
}
```

Ok updatet scipy package, with deleted patches



---

archive/issue_comments_096530.json:
```json
{
    "body": "Help!  I couldn't work on this over the weekend, and now I'm not quite sure what I should do to test :)  Should I just try installing the new Scipy 0.8, or what?  I am very glad that it seems you've figured out what G95 didn't like, though.     It would also be nice to see a diff between the `spkg-install` scripts.",
    "created_at": "2010-09-13T14:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96530",
    "user": "@kcrisman"
}
```

Help!  I couldn't work on this over the weekend, and now I'm not quite sure what I should do to test :)  Should I just try installing the new Scipy 0.8, or what?  I am very glad that it seems you've figured out what G95 didn't like, though.     It would also be nice to see a diff between the `spkg-install` scripts.



---

archive/issue_comments_096531.json:
```json
{
    "body": "Ok short summary: 1) Try the new scipy 2) If this doesn't work try to change the header in gammaincinv.c in the scipy sources from <Python.h> to <python2.6/Python.h> 3) If this results in no change, rewrite the header that it takes the sage header directly means change <Python.h> to \"whateverpathitmaybe/python2.6/Python.h\" and look if the error message changes. (because there are other files affected, but this should be no prob to patch)\n\nIf it's really only the location of the header patching wouldn't be a problem.\nAnd Thanx for all the trouble!\n\n\nI have the diffs made for on my other machine, I can post them tomorrow!",
    "created_at": "2010-09-13T19:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96531",
    "user": "maldun"
}
```

Ok short summary: 1) Try the new scipy 2) If this doesn't work try to change the header in gammaincinv.c in the scipy sources from <Python.h> to <python2.6/Python.h> 3) If this results in no change, rewrite the header that it takes the sage header directly means change <Python.h> to "whateverpathitmaybe/python2.6/Python.h" and look if the error message changes. (because there are other files affected, but this should be no prob to patch)

If it's really only the location of the header patching wouldn't be a problem.
And Thanx for all the trouble!


I have the diffs made for on my other machine, I can post them tomorrow!



---

archive/issue_comments_096532.json:
```json
{
    "body": "Diff of the spkg installs; The lines wich concern config fc are removed due problems in ubuntu",
    "created_at": "2010-09-14T12:14:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96532",
    "user": "maldun"
}
```

Diff of the spkg installs; The lines wich concern config fc are removed due problems in ubuntu



---

archive/issue_comments_096533.json:
```json
{
    "body": "Attachment [spkg.diff](tarball://root/attachments/some-uuid/ticket9808/spkg.diff) by @kcrisman created at 2010-09-14 13:07:25\n\nWell, that seems to have helped...\n\n```\ngcc: scipy/special/c_misc/gammaincinv.c\n```\n\nand it keeps going!\n\nSo it was the patches for G95 that were the problem.  Which one in particular (which command/line) caused the header confusion, do you think?  I'm just curious, and don't know enough about this to say.\n\nBy the way, I'm seeing things like \n\n```\ncompile options: '-I/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include -I/Users/student/Desktop/sage-4.5.2/local/include/python2.6 -c'\n```\n\nso hopefully that is also a positive sign.",
    "created_at": "2010-09-14T13:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96533",
    "user": "@kcrisman"
}
```

Attachment [spkg.diff](tarball://root/attachments/some-uuid/ticket9808/spkg.diff) by @kcrisman created at 2010-09-14 13:07:25

Well, that seems to have helped...

```
gcc: scipy/special/c_misc/gammaincinv.c
```

and it keeps going!

So it was the patches for G95 that were the problem.  Which one in particular (which command/line) caused the header confusion, do you think?  I'm just curious, and don't know enough about this to say.

By the way, I'm seeing things like 

```
compile options: '-I/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/site-packages/numpy/core/include -I/Users/student/Desktop/sage-4.5.2/local/include/python2.6 -c'
```

so hopefully that is also a positive sign.



---

archive/issue_comments_096534.json:
```json
{
    "body": "Success!  Now I'll set `SAGE_CHECK=yes`, retry numpy, do `./sage -ba`, retry scipy, and test the Sage library.  It will take a LONG time but hopefully tomorrow I'll have a report for you.",
    "created_at": "2010-09-14T13:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96534",
    "user": "@kcrisman"
}
```

Success!  Now I'll set `SAGE_CHECK=yes`, retry numpy, do `./sage -ba`, retry scipy, and test the Sage library.  It will take a LONG time but hopefully tomorrow I'll have a report for you.



---

archive/issue_comments_096535.json:
```json
{
    "body": "That are great news! Hopefully everything works!",
    "created_at": "2010-09-14T13:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96535",
    "user": "maldun"
}
```

That are great news! Hopefully everything works!



---

archive/issue_comments_096536.json:
```json
{
    "body": "Ah and don't forget the patch for the doctests in the attachement. Else there would 2 doctests fail due to output changes in numpy.",
    "created_at": "2010-09-14T13:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96536",
    "user": "maldun"
}
```

Ah and don't forget the patch for the doctests in the attachement. Else there would 2 doctests fail due to output changes in numpy.



---

archive/issue_comments_096537.json:
```json
{
    "body": "I'm not worried about that, but I'll do it when I get there.  Numpy just finished installing successfully.\n\nQuestion:  \n\n```\n# Program around a bug in SciPY's distutils.\nunset CFLAGS\n\npython setup.py install ${NUMPY_FCONFIG}\n\n```\n\nI assume this is still needed in the numpy `spkg-install`.  Just checking.\n\nQuestion:\nI know drkirkby is cc:ed on this ticket.  Numpy seems to have a very easy to run test suite - see [here](http://projects.scipy.org/numpy/wiki/TestingGuidelines).  However, it requires the Nose package.  Maybe this should be a separate ticket, but it would seem reasonable to include Nose, which is about 250 KB, so that we can run the numpy tests.  I am curious as to how we run the scipy tests without it!",
    "created_at": "2010-09-14T14:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96537",
    "user": "@kcrisman"
}
```

I'm not worried about that, but I'll do it when I get there.  Numpy just finished installing successfully.

Question:  

```
# Program around a bug in SciPY's distutils.
unset CFLAGS

python setup.py install ${NUMPY_FCONFIG}

```

I assume this is still needed in the numpy `spkg-install`.  Just checking.

Question:
I know drkirkby is cc:ed on this ticket.  Numpy seems to have a very easy to run test suite - see [here](http://projects.scipy.org/numpy/wiki/TestingGuidelines).  However, it requires the Nose package.  Maybe this should be a separate ticket, but it would seem reasonable to include Nose, which is about 250 KB, so that we can run the numpy tests.  I am curious as to how we run the scipy tests without it!



---

archive/issue_comments_096538.json:
```json
{
    "body": "Replying to [comment:113 kcrisman]:\n> Well, that seems to have helped...\n> {{{\n> gcc: scipy/special/c_misc/gammaincinv.c\n> }}}\n> and it keeps going!\n> \n> So it was the patches for G95 that were the problem.  Which one in particular (which command/line) caused the header confusion, do you think?  I'm just curious, and don't know enough about this to say.\n> \n\nWell, there are 4 patches that were applied in case g95 was found as the fortran compiler. The faulty one is special.setup.py (or possibly setup.py.special) which\nreplaces the file setup.py in the folder scipy/special.\n\nThis setup.py file has changed quite a lot between version 0.7.0 and 0.8.0.\nThe lines at fault:\n\n```\n    # C libraries\n    config.add_library('sc_c_misc',sources=[join('c_misc','*.c')])\n    config.add_library('sc_cephes',sources=[join('cephes','*.c')],\n                       include_dirs=[get_python_inc(), get_numpy_include_dirs()],\n                       macros=define_macros)\n```\n\nin version 0.7.0 and this is the code found in the \"patch\" file and\n\n```\n    # C libraries\n    config.add_library('sc_c_misc',sources=[join('c_misc','*.c')],\n                       include_dirs=[get_python_inc(), get_numpy_include_dirs()],\n                       macros=define_macros)\n    config.add_library('sc_cephes',sources=[join('cephes','*.c')],\n                       include_dirs=[get_python_inc(), get_numpy_include_dirs()],\n                       macros=define_macros)\n```\n\nin version 0.8.0. This is a case were using patches rather copying files wholesale would have prevented the problem. Either the patch wouldn't have worked with the newer version and we would have known straight away or it would have applied with some fuzz without dommaging this particular section.",
    "created_at": "2010-09-15T04:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96538",
    "user": "@kiwifb"
}
```

Replying to [comment:113 kcrisman]:
> Well, that seems to have helped...
> {{{
> gcc: scipy/special/c_misc/gammaincinv.c
> }}}
> and it keeps going!
> 
> So it was the patches for G95 that were the problem.  Which one in particular (which command/line) caused the header confusion, do you think?  I'm just curious, and don't know enough about this to say.
> 

Well, there are 4 patches that were applied in case g95 was found as the fortran compiler. The faulty one is special.setup.py (or possibly setup.py.special) which
replaces the file setup.py in the folder scipy/special.

This setup.py file has changed quite a lot between version 0.7.0 and 0.8.0.
The lines at fault:

```
    # C libraries
    config.add_library('sc_c_misc',sources=[join('c_misc','*.c')])
    config.add_library('sc_cephes',sources=[join('cephes','*.c')],
                       include_dirs=[get_python_inc(), get_numpy_include_dirs()],
                       macros=define_macros)
```

in version 0.7.0 and this is the code found in the "patch" file and

```
    # C libraries
    config.add_library('sc_c_misc',sources=[join('c_misc','*.c')],
                       include_dirs=[get_python_inc(), get_numpy_include_dirs()],
                       macros=define_macros)
    config.add_library('sc_cephes',sources=[join('cephes','*.c')],
                       include_dirs=[get_python_inc(), get_numpy_include_dirs()],
                       macros=define_macros)
```

in version 0.8.0. This is a case were using patches rather copying files wholesale would have prevented the problem. Either the patch wouldn't have worked with the newer version and we would have known straight away or it would have applied with some fuzz without dommaging this particular section.



---

archive/issue_comments_096539.json:
```json
{
    "body": "Replying to [comment:117 kcrisman]:\n> I'm not worried about that, but I'll do it when I get there.  Numpy just finished installing successfully.\n> \n> Question:  \n> {{{\n> # Program around a bug in SciPY's distutils.\n> unset CFLAGS\n> \n> python setup.py install ${NUMPY_FCONFIG}\n> \n> }}}\n> I assume this is still needed in the numpy `spkg-install`.  Just checking.\n> \n> Question:\n> I know drkirkby is cc:ed on this ticket.  Numpy seems to have a very easy to run test suite - see [here](http://projects.scipy.org/numpy/wiki/TestingGuidelines).  However, it requires the Nose package.  Maybe this should be a separate ticket, but it would seem reasonable to include Nose, which is about 250 KB, so that we can run the numpy tests.  I am curious as to how we run the scipy tests without it! \n\nActually Dave has started a thread about this a few weeks ago on the mailing list,\nyou are welcome to add your opinion and revive the thread.",
    "created_at": "2010-09-15T04:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96539",
    "user": "@kiwifb"
}
```

Replying to [comment:117 kcrisman]:
> I'm not worried about that, but I'll do it when I get there.  Numpy just finished installing successfully.
> 
> Question:  
> {{{
> # Program around a bug in SciPY's distutils.
> unset CFLAGS
> 
> python setup.py install ${NUMPY_FCONFIG}
> 
> }}}
> I assume this is still needed in the numpy `spkg-install`.  Just checking.
> 
> Question:
> I know drkirkby is cc:ed on this ticket.  Numpy seems to have a very easy to run test suite - see [here](http://projects.scipy.org/numpy/wiki/TestingGuidelines).  However, it requires the Nose package.  Maybe this should be a separate ticket, but it would seem reasonable to include Nose, which is about 250 KB, so that we can run the numpy tests.  I am curious as to how we run the scipy tests without it! 

Actually Dave has started a thread about this a few weeks ago on the mailing list,
you are welcome to add your opinion and revive the thread.



---

archive/issue_comments_096540.json:
```json
{
    "body": "Replying to [comment:117 kcrisman]:\n> I'm not worried about that, but I'll do it when I get there.  Numpy just finished installing successfully.\n> \n> Question:  \n> {{{\n> # Program around a bug in SciPY's distutils.\n> unset CFLAGS\n> \n> python setup.py install ${NUMPY_FCONFIG}\n> \n> }}}\n> I assume this is still needed in the numpy `spkg-install`.  Just checking.\nI thought I had asked maldun to remove this. It's working fine on Gentoo as it is,\nI am assuming this has been fixed upstream (possibly a while ago).",
    "created_at": "2010-09-15T04:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96540",
    "user": "@kiwifb"
}
```

Replying to [comment:117 kcrisman]:
> I'm not worried about that, but I'll do it when I get there.  Numpy just finished installing successfully.
> 
> Question:  
> {{{
> # Program around a bug in SciPY's distutils.
> unset CFLAGS
> 
> python setup.py install ${NUMPY_FCONFIG}
> 
> }}}
> I assume this is still needed in the numpy `spkg-install`.  Just checking.
I thought I had asked maldun to remove this. It's working fine on Gentoo as it is,
I am assuming this has been fixed upstream (possibly a while ago).



---

archive/issue_comments_096541.json:
```json
{
    "body": "I added the \n\n```\n# Program around a bug in SciPY's distutils.\nunset CFLAGS\n```\n\n\ninto the numpy spkg-install from the old one, just to be sure that we don't run into troubles, and actually it doesn't do any harm... but if you want I can remove it as well.\n\nBut didn't we agree that the\n`setup.py install ${NUMPY_FCONFIG`} \nis necessary in numpy? I had to delete it from scipy or else it doesn't build anymore, but in numpy it's correct.",
    "created_at": "2010-09-15T08:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96541",
    "user": "maldun"
}
```

I added the 

```
# Program around a bug in SciPY's distutils.
unset CFLAGS
```


into the numpy spkg-install from the old one, just to be sure that we don't run into troubles, and actually it doesn't do any harm... but if you want I can remove it as well.

But didn't we agree that the
`setup.py install ${NUMPY_FCONFIG`} 
is necessary in numpy? I had to delete it from scipy or else it doesn't build anymore, but in numpy it's correct.



---

archive/issue_comments_096542.json:
```json
{
    "body": "Replying to [comment:121 maldun]:\n> I added the \n> {{{\n> # Program around a bug in SciPY's distutils.\n> unset CFLAGS\n> }}}\n> \n> into the numpy spkg-install from the old one, just to be sure that we don't run into troubles, and actually it doesn't do any harm... but if you want I can remove it as well.\n> \nWe should remove it. If there is a problem - which I doubt, we can put it back.\n\n> But didn't we agree that the\n> `setup.py install ${NUMPY_FCONFIG`} \n> is necessary in numpy? I had to delete it from scipy or else it doesn't build anymore, but in numpy it's correct.\n> \n\nYes! Leave it here.",
    "created_at": "2010-09-15T09:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96542",
    "user": "@kiwifb"
}
```

Replying to [comment:121 maldun]:
> I added the 
> {{{
> # Program around a bug in SciPY's distutils.
> unset CFLAGS
> }}}
> 
> into the numpy spkg-install from the old one, just to be sure that we don't run into troubles, and actually it doesn't do any harm... but if you want I can remove it as well.
> 
We should remove it. If there is a problem - which I doubt, we can put it back.

> But didn't we agree that the
> `setup.py install ${NUMPY_FCONFIG`} 
> is necessary in numpy? I had to delete it from scipy or else it doesn't build anymore, but in numpy it's correct.
> 

Yes! Leave it here.



---

archive/issue_comments_096543.json:
```json
{
    "body": "Ok I removed the line. \n\nI also thougth before posting I should check if there are some old rests in there, and I removed some patches that are possible(?) outdated. I think this could affect the cygwin installation, so it would be important to see if it still builds on all machines, or else I have to carefully merge the changed lines, from the old patches with the new versions of the files.\n\nIt works for me, so I hope I didn't cause some new problems",
    "created_at": "2010-09-15T10:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96543",
    "user": "maldun"
}
```

Ok I removed the line. 

I also thougth before posting I should check if there are some old rests in there, and I removed some patches that are possible(?) outdated. I think this could affect the cygwin installation, so it would be important to see if it still builds on all machines, or else I have to carefully merge the changed lines, from the old patches with the new versions of the files.

It works for me, so I hope I didn't cause some new problems



---

archive/issue_comments_096544.json:
```json
{
    "body": "I have a different problem: When I upload the new Version, and try to download it I get the old one. Is there some confusion on the server?",
    "created_at": "2010-09-15T10:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96544",
    "user": "maldun"
}
```

I have a different problem: When I upload the new Version, and try to download it I get the old one. Is there some confusion on the server?



---

archive/issue_comments_096545.json:
```json
{
    "body": "Ok worked. Don't ask why...",
    "created_at": "2010-09-15T10:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96545",
    "user": "maldun"
}
```

Ok worked. Don't ask why...



---

archive/issue_comments_096546.json:
```json
{
    "body": "Ok - now this needs review!\n\nI looked at the cygwin-lapack_lite-setup.py patch. The file patched hasn't changed between numpy-1.3.x and 1.4.1, so it can still be applied safely if needed.\n\nIn summary the only problems overall are:\n* numpy 1.4.1 is broken on linux ppc (on the official list of supported OS - so bad) and alpha (not on the supported list - so OK).\n* numpy-1.5.0 has an issues with cython that will be solved in 1.5.1 - shame because it also fixes linux ppc and alpha.\n\nAnything to add?",
    "created_at": "2010-09-15T11:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96546",
    "user": "@kiwifb"
}
```

Ok - now this needs review!

I looked at the cygwin-lapack_lite-setup.py patch. The file patched hasn't changed between numpy-1.3.x and 1.4.1, so it can still be applied safely if needed.

In summary the only problems overall are:
* numpy 1.4.1 is broken on linux ppc (on the official list of supported OS - so bad) and alpha (not on the supported list - so OK).
* numpy-1.5.0 has an issues with cython that will be solved in 1.5.1 - shame because it also fixes linux ppc and alpha.

Anything to add?



---

archive/issue_comments_096547.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-15T11:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96547",
    "user": "@kiwifb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096548.json:
```json
{
    "body": "Replying to [comment:126 fbissey]:\n\n> Anything to add?\n\nas mentioned above: The version of numpy-1.5.0 with the patch applied is ok. The only trouble I have are some doctests, which fails because numpy throws a \"Division by zero encountered!\" Exception, which makes them fail, although the results are correct. But I still don't know how to catch the exceptions.",
    "created_at": "2010-09-15T11:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96548",
    "user": "maldun"
}
```

Replying to [comment:126 fbissey]:

> Anything to add?

as mentioned above: The version of numpy-1.5.0 with the patch applied is ok. The only trouble I have are some doctests, which fails because numpy throws a "Division by zero encountered!" Exception, which makes them fail, although the results are correct. But I still don't know how to catch the exceptions.



---

archive/issue_comments_096549.json:
```json
{
    "body": "I should say that while breaking on linux ppc is not good, I only know of one other person building sage on that platform. So it could take the backseat while problems\nwith the 1.5 series are ironed out.",
    "created_at": "2010-09-15T11:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96549",
    "user": "@kiwifb"
}
```

I should say that while breaking on linux ppc is not good, I only know of one other person building sage on that platform. So it could take the backseat while problems
with the 1.5 series are ironed out.



---

archive/issue_comments_096550.json:
```json
{
    "body": "> * numpy-1.5.0 has an issues with cython that will be solved in 1.5.1 - shame because it also fixes linux ppc and alpha.\n\nHmm, dropping an official thing is not so good.  I think that one would want to post to the list about this - more likely wait for 1.5.1?  Or is the fix for this easily backported?  \n\nAlso, although I've been going for over 24 hours now on the tests (and several timeouts! so I'll have to run those with `SAGE_TIMEOUT_LONG>3600`), I have only seen two errors, both like this:\n\n```\nsage -t -long \"devel/sage/sage/graphs/digraph.py\"           \n**********************************************************************\nFile \"/Users/student/Desktop/sage-4.5.2/devel/sage/sage/graphs/digraph.py\", line 204:\n    sage: DiGraph(A)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/student/Desktop/sage-4.5.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/student/Desktop/sage-4.5.2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/student/Desktop/sage-4.5.2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[17]>\", line 1, in <module>\n        DiGraph(A)###line 204:\n    sage: DiGraph(A)\n      File \"/Users/student/Desktop/sage-4.5.2/local/lib/python/site-packages/sage/graphs/digraph.py\", line 364, in __init__\n        data = networkx.MultiDiGraph(data)\n      File \"/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/networkx/classes/digraph.py\", line 217, in __init__\n        convert.from_whatever(data,create_using=self)\n      File \"/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/networkx/convert.py\", line 157, in from_whatever\n        if isinstance(thing,numpy.core.defmatrix.matrix) or \\\n    AttributeError: 'module' object has no attribute 'defmatrix'\n**********************************************************************\n```\n\nHave you seen this?  Clearly it's something to do with numpy, from the end - but it's not clear to me why it would be asking whether a module has defmatrix attribute.",
    "created_at": "2010-09-15T17:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96550",
    "user": "@kcrisman"
}
```

> * numpy-1.5.0 has an issues with cython that will be solved in 1.5.1 - shame because it also fixes linux ppc and alpha.

Hmm, dropping an official thing is not so good.  I think that one would want to post to the list about this - more likely wait for 1.5.1?  Or is the fix for this easily backported?  

Also, although I've been going for over 24 hours now on the tests (and several timeouts! so I'll have to run those with `SAGE_TIMEOUT_LONG>3600`), I have only seen two errors, both like this:

```
sage -t -long "devel/sage/sage/graphs/digraph.py"           
**********************************************************************
File "/Users/student/Desktop/sage-4.5.2/devel/sage/sage/graphs/digraph.py", line 204:
    sage: DiGraph(A)
Exception raised:
    Traceback (most recent call last):
      File "/Users/student/Desktop/sage-4.5.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.5.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.5.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[17]>", line 1, in <module>
        DiGraph(A)###line 204:
    sage: DiGraph(A)
      File "/Users/student/Desktop/sage-4.5.2/local/lib/python/site-packages/sage/graphs/digraph.py", line 364, in __init__
        data = networkx.MultiDiGraph(data)
      File "/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/networkx/classes/digraph.py", line 217, in __init__
        convert.from_whatever(data,create_using=self)
      File "/Users/student/Desktop/sage-4.5.2/local/lib/python2.6/networkx/convert.py", line 157, in from_whatever
        if isinstance(thing,numpy.core.defmatrix.matrix) or \
    AttributeError: 'module' object has no attribute 'defmatrix'
**********************************************************************
```

Have you seen this?  Clearly it's something to do with numpy, from the end - but it's not clear to me why it would be asking whether a module has defmatrix attribute.



---

archive/issue_comments_096551.json:
```json
{
    "body": "I know this error. Since you use sage 4.5.2 you will also use networkx-1.0.1. See comments 24 and following or ticket #9854.\n\nYou have to either use Sage 4.5.3 which holds networkx-1.2, upgrade networkx-1.0.1 in your current version, or apply the networkx-1.0.1.p0.spkg in the attachement, which holds a simple patch.\n\nThe reason is that numpy.core.defmatrix moved to numpy.matrixlib.defmatrix.",
    "created_at": "2010-09-15T21:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96551",
    "user": "maldun"
}
```

I know this error. Since you use sage 4.5.2 you will also use networkx-1.0.1. See comments 24 and following or ticket #9854.

You have to either use Sage 4.5.3 which holds networkx-1.2, upgrade networkx-1.0.1 in your current version, or apply the networkx-1.0.1.p0.spkg in the attachement, which holds a simple patch.

The reason is that numpy.core.defmatrix moved to numpy.matrixlib.defmatrix.



---

archive/issue_comments_096552.json:
```json
{
    "body": "`@`linux ppc I could work over the weekend the solve the failed doctests in numpy-1.5.0, because with the patch from the numpy developers the biggest problem i.e. the cython problem is solved. The only thing remains are some \"Division by Zero Warnings\" as mentioned above.",
    "created_at": "2010-09-15T21:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96552",
    "user": "maldun"
}
```

`@`linux ppc I could work over the weekend the solve the failed doctests in numpy-1.5.0, because with the patch from the numpy developers the biggest problem i.e. the cython problem is solved. The only thing remains are some "Division by Zero Warnings" as mentioned above.



---

archive/issue_comments_096553.json:
```json
{
    "body": "And another thing: If we aren't able to merge numpy and scipy to 4.6. in time, why don't we provide the packages as optional or experimental? Because they work on most systems, and it would be a waste to just throw them away.",
    "created_at": "2010-09-15T21:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96553",
    "user": "maldun"
}
```

And another thing: If we aren't able to merge numpy and scipy to 4.6. in time, why don't we provide the packages as optional or experimental? Because they work on most systems, and it would be a waste to just throw them away.



---

archive/issue_comments_096554.json:
```json
{
    "body": "Replying to [comment:129 kcrisman]:\n> > * numpy-1.5.0 has an issues with cython that will be solved in 1.5.1 - shame because it also fixes linux ppc and alpha.\n> \n> Hmm, dropping an official thing is not so good.  I think that one would want to post to the list about this - more likely wait for 1.5.1?  Or is the fix for this easily backported?  \n\nDepending on what list you read, Linux on PPC may or may not be supported. I've tried to get an agreement before on what we do support and what we don't, but never got anywhere. \n\nI'm personally in favor of keeping Sage building on less regular systems, as it often indicates problems. The Solaris port has found endless bugs in Sage - some of which have even according to William been serious. \n\nI have an old IBM RS/6000 7025 F50 (Power PC) which I was setting up AIX on the other day. I contemlated  whether I should put Linux on it too for testing Sage. But when I read Sage's README.txt, PowerPC was only supported on OS X, not Linux. So I did not bother. But the machine has space for 18 disk drives, so I could always add it!! \n\nDave",
    "created_at": "2010-09-15T22:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96554",
    "user": "drkirkby"
}
```

Replying to [comment:129 kcrisman]:
> > * numpy-1.5.0 has an issues with cython that will be solved in 1.5.1 - shame because it also fixes linux ppc and alpha.
> 
> Hmm, dropping an official thing is not so good.  I think that one would want to post to the list about this - more likely wait for 1.5.1?  Or is the fix for this easily backported?  

Depending on what list you read, Linux on PPC may or may not be supported. I've tried to get an agreement before on what we do support and what we don't, but never got anywhere. 

I'm personally in favor of keeping Sage building on less regular systems, as it often indicates problems. The Solaris port has found endless bugs in Sage - some of which have even according to William been serious. 

I have an old IBM RS/6000 7025 F50 (Power PC) which I was setting up AIX on the other day. I contemlated  whether I should put Linux on it too for testing Sage. But when I read Sage's README.txt, PowerPC was only supported on OS X, not Linux. So I did not bother. But the machine has space for 18 disk drives, so I could always add it!! 

Dave



---

archive/issue_comments_096555.json:
```json
{
    "body": "I forgot about the networkx change, thanks for the reminder.\n> > > * numpy-1.5.0 has an issues with cython that will be solved in 1.5.1 - shame because it also fixes linux ppc and alpha.\n> > \n> > Hmm, dropping an official thing is not so good.  I think that one would want to post to the list about this - more likely wait for 1.5.1?  Or is the fix for this easily backported?  \n> I'm personally in favor of keeping Sage building on less regular systems, as it often indicates problems. The Solaris port has found endless bugs in Sage - some of which have even according to William been serious. \n> \n> I have an old IBM RS/6000 7025 F50 (Power PC) which I was setting up AIX on the other day. I contemlated  whether I should put Linux on it too for testing Sage. But when I read Sage's README.txt, PowerPC was only supported on OS X, not Linux. So I did not bother. But the machine has space for 18 disk drives, so I could always add it!! \n\nWhy not?  I've been trying to figure out how to get a thumb drive to boot my PPC machine on Ubuntu (and possibly other distros) but it turns out it's devilishly hard to get that to work, and I haven't had time to do it.  I can't find an easy virtualization option either (neither xen nor anything else seem to really be particularly easy, if they even still work with such an old machine...)\n\n> And another thing: If we aren't able to merge numpy and scipy to 4.6. in time, why don't we provide the packages as optional or experimental? Because they work on most systems, and it would be a waste to just throw them away.\nCertainly one could do this, but even that would require a positive review from someone.  You might have to ask on the list about this - I've never heard of having an upgrade to a normal package as only optional.",
    "created_at": "2010-09-16T01:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96555",
    "user": "@kcrisman"
}
```

I forgot about the networkx change, thanks for the reminder.
> > > * numpy-1.5.0 has an issues with cython that will be solved in 1.5.1 - shame because it also fixes linux ppc and alpha.
> > 
> > Hmm, dropping an official thing is not so good.  I think that one would want to post to the list about this - more likely wait for 1.5.1?  Or is the fix for this easily backported?  
> I'm personally in favor of keeping Sage building on less regular systems, as it often indicates problems. The Solaris port has found endless bugs in Sage - some of which have even according to William been serious. 
> 
> I have an old IBM RS/6000 7025 F50 (Power PC) which I was setting up AIX on the other day. I contemlated  whether I should put Linux on it too for testing Sage. But when I read Sage's README.txt, PowerPC was only supported on OS X, not Linux. So I did not bother. But the machine has space for 18 disk drives, so I could always add it!! 

Why not?  I've been trying to figure out how to get a thumb drive to boot my PPC machine on Ubuntu (and possibly other distros) but it turns out it's devilishly hard to get that to work, and I haven't had time to do it.  I can't find an easy virtualization option either (neither xen nor anything else seem to really be particularly easy, if they even still work with such an old machine...)

> And another thing: If we aren't able to merge numpy and scipy to 4.6. in time, why don't we provide the packages as optional or experimental? Because they work on most systems, and it would be a waste to just throw them away.
Certainly one could do this, but even that would require a positive review from someone.  You might have to ask on the list about this - I've never heard of having an upgrade to a normal package as only optional.



---

archive/issue_comments_096556.json:
```json
{
    "body": "> You have to either use Sage 4.5.3 which holds networkx-1.2, upgrade networkx-1.0.1 in your current version, or apply the networkx-1.0.1.p0.spkg in the attachement, which holds a simple patch.\n\nIncidentally, I also had to repackage that spkg, because you didn't use `./sage -pkg` for it either :) and it had unchecked in changes :)  But clearly that is irrelevant for testing, since the upgrade is already in a later Sage.\n\nOkay, with this upgrade those two tests pass.  I am currently testing the other four failures, all of which were timeouts, all of which are in files I personally know to have VERY long `-long` doctests, and all but one of which hopefully will pass with `SAGE_TIMEOUT_LONG=10000` (there is one in `interfaces/maxima.py` which always fails on OS X 10.4, as far as I know, which is due to tab-completion testing of Maxima never finishing, totally unrelated to this).  I'll let you know if something *doesn't* work.\n\nSo I think that my job is done here (pointing out that I was testing the version from before the weekend.  fbissey or drkirkby should comment on the spkg itself.",
    "created_at": "2010-09-16T12:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96556",
    "user": "@kcrisman"
}
```

> You have to either use Sage 4.5.3 which holds networkx-1.2, upgrade networkx-1.0.1 in your current version, or apply the networkx-1.0.1.p0.spkg in the attachement, which holds a simple patch.

Incidentally, I also had to repackage that spkg, because you didn't use `./sage -pkg` for it either :) and it had unchecked in changes :)  But clearly that is irrelevant for testing, since the upgrade is already in a later Sage.

Okay, with this upgrade those two tests pass.  I am currently testing the other four failures, all of which were timeouts, all of which are in files I personally know to have VERY long `-long` doctests, and all but one of which hopefully will pass with `SAGE_TIMEOUT_LONG=10000` (there is one in `interfaces/maxima.py` which always fails on OS X 10.4, as far as I know, which is due to tab-completion testing of Maxima never finishing, totally unrelated to this).  I'll let you know if something *doesn't* work.

So I think that my job is done here (pointing out that I was testing the version from before the weekend.  fbissey or drkirkby should comment on the spkg itself.



---

archive/issue_comments_096557.json:
```json
{
    "body": "Well thanks Karl! Your testing was very useful. Since I have contributed to bits and pieces\nI think I should had myself as an author. But most of the heavy lifting as been done by maldun.\n\nSo what's left is the question of whether we go for numpy-1.4.1 and leave minor archs unsupported\nfor a little bit. Or we wait for 1.5.1, which works on the minor archs in question and will play\nwell with cython.\n\nAs an aside I have already pushed the upgrade in sage-on-gentoo (to avoid tree rote, we already\nhave to keep two old packages that are otherwise removed from Gentoo) and we want to avoid that\nkind of stuff as much as possible. So the current code is out there and used by a few people.\n\nAfter that there are question of details. In spkg-install I have set FC to ${SAGE_LOCAL}/bin/sage_fortran, with the idea that it was basically calling \"gfortran -fpic\" or the g95 equivalent. We have been talking about that very subject on sage-devel recently. Is it the best way to go? If one uses sunstudio (and I am planning to give a go) the correct flag would be -Kpic but would it be set up properly in sage_fortran? I doubt it. \n\nSo what would be the best course of action? Using the variable SAGE_FORTRAN for now and ask it\nto be set with the proper pic flag and hopefully drop it later on when FC is the mainstay?",
    "created_at": "2010-09-17T01:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96557",
    "user": "@kiwifb"
}
```

Well thanks Karl! Your testing was very useful. Since I have contributed to bits and pieces
I think I should had myself as an author. But most of the heavy lifting as been done by maldun.

So what's left is the question of whether we go for numpy-1.4.1 and leave minor archs unsupported
for a little bit. Or we wait for 1.5.1, which works on the minor archs in question and will play
well with cython.

As an aside I have already pushed the upgrade in sage-on-gentoo (to avoid tree rote, we already
have to keep two old packages that are otherwise removed from Gentoo) and we want to avoid that
kind of stuff as much as possible. So the current code is out there and used by a few people.

After that there are question of details. In spkg-install I have set FC to ${SAGE_LOCAL}/bin/sage_fortran, with the idea that it was basically calling "gfortran -fpic" or the g95 equivalent. We have been talking about that very subject on sage-devel recently. Is it the best way to go? If one uses sunstudio (and I am planning to give a go) the correct flag would be -Kpic but would it be set up properly in sage_fortran? I doubt it. 

So what would be the best course of action? Using the variable SAGE_FORTRAN for now and ask it
to be set with the proper pic flag and hopefully drop it later on when FC is the mainstay?



---

archive/issue_comments_096558.json:
```json
{
    "body": "Replying to [comment:136 fbissey]:\n> Well thanks Karl! Your testing was very useful. Since I have contributed to bits and pieces\n> I think I should had myself as an author. But most of the heavy lifting as been done by maldun.\n> \nI think you are right. So I allowed myself to set you as co-author, since this whole thing wouldn't work without your help =)\n\n> So what's left is the question of whether we go for numpy-1.4.1 and leave minor archs unsupported\n> for a little bit. Or we wait for 1.5.1, which works on the minor archs in question and will play\n> well with cython.\n> \nI would suggest the following: If numpy 1.5.1 doesn't come out before Sage 4.6. let's take 1.4.1 (since ppc linux is not on the current supported list; see readme.tex of sage)\nI will start this weekend with correcting things of 1.5.0, since the current errors are new warnings, and I'm quite sure numpy 1.5.1 will throw those as well.\nWhen numpy 1.5.1 is out before 4.6. I will try to pack it, and then hopefully it is done in no time, since it shared the same probs.\n\n> As an aside I have already pushed the upgrade in sage-on-gentoo (to avoid tree rote, we already\n> have to keep two old packages that are otherwise removed from Gentoo) and we want to avoid that\n> kind of stuff as much as possible. So the current code is out there and used by a few people.\n> \n> After that there are question of details. In spkg-install I have set FC to ${SAGE_LOCAL}/bin/sage_fortran, with the idea that it was basically calling \"gfortran -fpic\" or the g95 equivalent. We have been talking about that very subject on sage-devel recently. Is it the best way to go? If one uses sunstudio (and I am planning to give a go) the correct flag would be -Kpic but would it be set up properly in sage_fortran? I doubt it. \n> \n> So what would be the best course of action? Using the variable SAGE_FORTRAN for now and ask it\n> to be set with the proper pic flag and hopefully drop it later on when FC is the mainstay? \n\nThe question is how fast this change with the fortran compiler is done. I think we should wait a little bit now.\n\nMy question is: should this given a positive review, or is something still missing?",
    "created_at": "2010-09-17T09:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96558",
    "user": "maldun"
}
```

Replying to [comment:136 fbissey]:
> Well thanks Karl! Your testing was very useful. Since I have contributed to bits and pieces
> I think I should had myself as an author. But most of the heavy lifting as been done by maldun.
> 
I think you are right. So I allowed myself to set you as co-author, since this whole thing wouldn't work without your help =)

> So what's left is the question of whether we go for numpy-1.4.1 and leave minor archs unsupported
> for a little bit. Or we wait for 1.5.1, which works on the minor archs in question and will play
> well with cython.
> 
I would suggest the following: If numpy 1.5.1 doesn't come out before Sage 4.6. let's take 1.4.1 (since ppc linux is not on the current supported list; see readme.tex of sage)
I will start this weekend with correcting things of 1.5.0, since the current errors are new warnings, and I'm quite sure numpy 1.5.1 will throw those as well.
When numpy 1.5.1 is out before 4.6. I will try to pack it, and then hopefully it is done in no time, since it shared the same probs.

> As an aside I have already pushed the upgrade in sage-on-gentoo (to avoid tree rote, we already
> have to keep two old packages that are otherwise removed from Gentoo) and we want to avoid that
> kind of stuff as much as possible. So the current code is out there and used by a few people.
> 
> After that there are question of details. In spkg-install I have set FC to ${SAGE_LOCAL}/bin/sage_fortran, with the idea that it was basically calling "gfortran -fpic" or the g95 equivalent. We have been talking about that very subject on sage-devel recently. Is it the best way to go? If one uses sunstudio (and I am planning to give a go) the correct flag would be -Kpic but would it be set up properly in sage_fortran? I doubt it. 
> 
> So what would be the best course of action? Using the variable SAGE_FORTRAN for now and ask it
> to be set with the proper pic flag and hopefully drop it later on when FC is the mainstay? 

The question is how fast this change with the fortran compiler is done. I think we should wait a little bit now.

My question is: should this given a positive review, or is something still missing?



---

archive/issue_comments_096559.json:
```json
{
    "body": "I'd like to check this out on sage-4.6.alpha1, but its unclear to me exactly what to do.  Can someone summarize the current procedure for incorporating this ticket?",
    "created_at": "2010-09-20T20:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96559",
    "user": "mhampton"
}
```

I'd like to check this out on sage-4.6.alpha1, but its unclear to me exactly what to do.  Can someone summarize the current procedure for incorporating this ticket?



---

archive/issue_comments_096560.json:
```json
{
    "body": "Replying to [comment:138 mhampton]:\n> I'd like to check this out on sage-4.6.alpha1, but its unclear to me exactly what to do.  Can someone summarize the current procedure for incorporating this ticket?\n\nInstall notes and links to the packages are in the discription of this ticket!\n\nQuick and dirty: Install the packagages, do sage -ba to compile the whole source, apply the patch in the attachment for the doctests.\n\ngreez maldun",
    "created_at": "2010-09-20T20:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96560",
    "user": "maldun"
}
```

Replying to [comment:138 mhampton]:
> I'd like to check this out on sage-4.6.alpha1, but its unclear to me exactly what to do.  Can someone summarize the current procedure for incorporating this ticket?

Install notes and links to the packages are in the discription of this ticket!

Quick and dirty: Install the packagages, do sage -ba to compile the whole source, apply the patch in the attachment for the doctests.

greez maldun



---

archive/issue_comments_096561.json:
```json
{
    "body": "Just a quick note that I used this package in sage-4.6alpha1 and it didn't break any tests on linux-x86, I haven't heard of any problems on linux-amd64 from a friend who was also testing this. So it applies cleanly on 4.6alpha1.",
    "created_at": "2010-09-28T17:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96561",
    "user": "@kiwifb"
}
```

Just a quick note that I used this package in sage-4.6alpha1 and it didn't break any tests on linux-x86, I haven't heard of any problems on linux-amd64 from a friend who was also testing this. So it applies cleanly on 4.6alpha1.



---

archive/issue_comments_096562.json:
```json
{
    "body": "Dave pointed me to this ticket the day before yesterday (and I read it from the beginning). ;-)\n\nDespite that, it's unclear to me which diffs are currrent, and the description should IMHO be updated wrt. what's to be done to review this.\n\n`./sage -ba` is also in my opinion not a solution to get dependent extension modules updated, i.e. if `./sage -b` isn't sufficient, dependencies should be added to `module_list.py`.",
    "created_at": "2010-09-29T13:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96562",
    "user": "@nexttime"
}
```

Dave pointed me to this ticket the day before yesterday (and I read it from the beginning). ;-)

Despite that, it's unclear to me which diffs are currrent, and the description should IMHO be updated wrt. what's to be done to review this.

`./sage -ba` is also in my opinion not a solution to get dependent extension modules updated, i.e. if `./sage -b` isn't sufficient, dependencies should be added to `module_list.py`.



---

archive/issue_comments_096563.json:
```json
{
    "body": "Replying to [comment:141 leif]:\n> Dave pointed me to this ticket the day before yesterday (and I read it from the beginning). ;-)\n> \n> Despite that, it's unclear to me which diffs are currrent, and the description should IMHO be updated wrt. what's to be done to review this.\n> \n> `./sage -ba` is also in my opinion not a solution to get dependent extension modules updated, i.e. if `./sage -b` isn't sufficient, dependencies should be added to `module_list.py`.\n> \n\nI cleaned up the discription a little bit, and deleted the obsolete remark about networkx-1.2\n\nI don't know if this is a good Idea because this is a whole bunch of files we are talking about, which have to be added. Perhaps you won't save much time either when compiling. I first tried this too, but after about 2 hours searching, I got somehow tired of this... And after merging numpy > 1.3.x into Sage this has not to be done anymore. All versions of 1.5.x builded without problems, and didn't need -ba anymore.\nYou only have to do this when big changes are happening, and this is rather occassionally.\n\npackage with a linux ppc patch is out: http://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.4.1.p0.spkg\nhope it works this time!",
    "created_at": "2010-09-29T18:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96563",
    "user": "maldun"
}
```

Replying to [comment:141 leif]:
> Dave pointed me to this ticket the day before yesterday (and I read it from the beginning). ;-)
> 
> Despite that, it's unclear to me which diffs are currrent, and the description should IMHO be updated wrt. what's to be done to review this.
> 
> `./sage -ba` is also in my opinion not a solution to get dependent extension modules updated, i.e. if `./sage -b` isn't sufficient, dependencies should be added to `module_list.py`.
> 

I cleaned up the discription a little bit, and deleted the obsolete remark about networkx-1.2

I don't know if this is a good Idea because this is a whole bunch of files we are talking about, which have to be added. Perhaps you won't save much time either when compiling. I first tried this too, but after about 2 hours searching, I got somehow tired of this... And after merging numpy > 1.3.x into Sage this has not to be done anymore. All versions of 1.5.x builded without problems, and didn't need -ba anymore.
You only have to do this when big changes are happening, and this is rather occassionally.

package with a linux ppc patch is out: http://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.4.1.p0.spkg
hope it works this time!



---

archive/issue_comments_096564.json:
```json
{
    "body": "Ah before I forget it, and you think I'm just lazy: I just looked up again in an non compiled version which files are concerned, and I remembered again what was really the problem\nMost of them are already in the module_list.py.\n\nHowever the problem is, that there are actually no changes to that files, so sage -b won't do nothing, because it does'nt recognice any changes!\n\nonly -ba force sage to do that and link the whole c files to the new version of numpy.\n\nYou would have to change the behavior of -b, not add something to the module_list.py",
    "created_at": "2010-09-29T19:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96564",
    "user": "maldun"
}
```

Ah before I forget it, and you think I'm just lazy: I just looked up again in an non compiled version which files are concerned, and I remembered again what was really the problem
Most of them are already in the module_list.py.

However the problem is, that there are actually no changes to that files, so sage -b won't do nothing, because it does'nt recognice any changes!

only -ba force sage to do that and link the whole c files to the new version of numpy.

You would have to change the behavior of -b, not add something to the module_list.py



---

archive/issue_comments_096565.json:
```json
{
    "body": "Just for the record, `gcc` has the following option:\n\n  `-mabi=ieeelongdouble`\n  \n    Change the current ABI to use IEEE extended precision long double. This is a PowerPC 32-bit Linux ABI option.\n\nI don't know if this requires a different (or differently built) `libc` however.",
    "created_at": "2010-09-29T19:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96565",
    "user": "@nexttime"
}
```

Just for the record, `gcc` has the following option:

  `-mabi=ieeelongdouble`
  
    Change the current ABI to use IEEE extended precision long double. This is a PowerPC 32-bit Linux ABI option.

I don't know if this requires a different (or differently built) `libc` however.



---

archive/issue_comments_096566.json:
```json
{
    "body": "Replying to [comment:143 maldun]:\n> Ah before I forget it, and you think I'm just lazy: I just looked up again in an non compiled version which files are concerned, and I remembered again what was really the problem\n> Most of them are already in the module_list.py.\n> \n> However the problem is, that there are actually no changes to that files, so sage -b won't do nothing, because it does'nt recognice any changes!\n\nSo we have to add (at least some of) those files to `depends` that actually *have* changed.\n\n> only -ba force sage to do that and link the whole c files to the new version of numpy.\n> \n> You would have to change the behavior of -b, not add something to the module_list.py\n\nThat's IMHO not an option, since missing dependencies will break any Sage upgrade anyway.\n\nP.S.: The attached diffs are still confusing. (One should at least change/update their descriptions.) For review, complete diffs between the old and new spkgs (of course excluding `src/`) would be helpful.",
    "created_at": "2010-09-29T19:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96566",
    "user": "@nexttime"
}
```

Replying to [comment:143 maldun]:
> Ah before I forget it, and you think I'm just lazy: I just looked up again in an non compiled version which files are concerned, and I remembered again what was really the problem
> Most of them are already in the module_list.py.
> 
> However the problem is, that there are actually no changes to that files, so sage -b won't do nothing, because it does'nt recognice any changes!

So we have to add (at least some of) those files to `depends` that actually *have* changed.

> only -ba force sage to do that and link the whole c files to the new version of numpy.
> 
> You would have to change the behavior of -b, not add something to the module_list.py

That's IMHO not an option, since missing dependencies will break any Sage upgrade anyway.

P.S.: The attached diffs are still confusing. (One should at least change/update their descriptions.) For review, complete diffs between the old and new spkgs (of course excluding `src/`) would be helpful.



---

archive/issue_comments_096567.json:
```json
{
    "body": "Replying to [comment:145 leif]:\n\n>\n> So we have to add (at least some of) those files to `depends` that actually *have* changed.\n> \n\nAnd that's the problem: There are NO files which would have changed! Not within sage/devel/sage-whateverbranch. And that's also the reason for the warnings: numpy wonders why still the old size of flatiter is in the .c files. \nThe only changes are in local/LIB/python/site-packages/numpy, and -b don't care about those.\nThe only way to trick -b was to put in a comment to the certain files, delete them again and save it, that sage -b recognices the changes.\n\nI when kcrisman gives me feedback if numpy works now on ppc, I will put a complete changelog here on trac. Perhaps over the weekend I find some time for that.",
    "created_at": "2010-09-29T19:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96567",
    "user": "maldun"
}
```

Replying to [comment:145 leif]:

>
> So we have to add (at least some of) those files to `depends` that actually *have* changed.
> 

And that's the problem: There are NO files which would have changed! Not within sage/devel/sage-whateverbranch. And that's also the reason for the warnings: numpy wonders why still the old size of flatiter is in the .c files. 
The only changes are in local/LIB/python/site-packages/numpy, and -b don't care about those.
The only way to trick -b was to put in a comment to the certain files, delete them again and save it, that sage -b recognices the changes.

I when kcrisman gives me feedback if numpy works now on ppc, I will put a complete changelog here on trac. Perhaps over the weekend I find some time for that.



---

archive/issue_comments_096568.json:
```json
{
    "body": "> I when kcrisman gives me feedback if numpy works now on ppc, I will put a complete changelog here on trac. Perhaps over the weekend I find some time for that.\n\nYou mean on OS X, not Linux, right?\n\nNumpy installed fine, and Scipy got past the bad spot fine, so I don't anticipate any problems.  Then I'll run tests.\n\nLeif, is this really a problem? (Asked as a query, not a complaint.)  Presumably someone will only use these packages via sage-upgrade, and then the whole library rebuilds (because sage-x.y.z is new), right?  Or is that not how sage-upgrade works?  \n\nI'm adding a few reviewers based on how things have gone over these ~150 comments.",
    "created_at": "2010-09-29T20:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96568",
    "user": "@kcrisman"
}
```

> I when kcrisman gives me feedback if numpy works now on ppc, I will put a complete changelog here on trac. Perhaps over the weekend I find some time for that.

You mean on OS X, not Linux, right?

Numpy installed fine, and Scipy got past the bad spot fine, so I don't anticipate any problems.  Then I'll run tests.

Leif, is this really a problem? (Asked as a query, not a complaint.)  Presumably someone will only use these packages via sage-upgrade, and then the whole library rebuilds (because sage-x.y.z is new), right?  Or is that not how sage-upgrade works?  

I'm adding a few reviewers based on how things have gone over these ~150 comments.



---

archive/issue_comments_096569.json:
```json
{
    "body": "Replying to [comment:146 maldun]:\n> Replying to [comment:145 leif]:\n> \n> >\n> > So we have to add (at least some of) those files to `depends` that actually *have* changed.\n> > \n> \n> And that's the problem: There are NO files which would have changed! Not within sage/devel/sage-whateverbranch. And that's also the reason for the warnings: numpy wonders why still the old size of flatiter is in the .c files.\n\nSo what? Then just make them also depend on e.g. `$SAGE_LOCAL/lib/python/site-packages/numpy/core/include/numpy/numpyconfig.h` (if *that* has changed).",
    "created_at": "2010-09-29T20:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96569",
    "user": "@nexttime"
}
```

Replying to [comment:146 maldun]:
> Replying to [comment:145 leif]:
> 
> >
> > So we have to add (at least some of) those files to `depends` that actually *have* changed.
> > 
> 
> And that's the problem: There are NO files which would have changed! Not within sage/devel/sage-whateverbranch. And that's also the reason for the warnings: numpy wonders why still the old size of flatiter is in the .c files.

So what? Then just make them also depend on e.g. `$SAGE_LOCAL/lib/python/site-packages/numpy/core/include/numpy/numpyconfig.h` (if *that* has changed).



---

archive/issue_comments_096570.json:
```json
{
    "body": "Replying to [comment:147 kcrisman]:\n> Leif, is this really a problem? (Asked as a query, not a complaint.)  Presumably someone will only use these packages via sage-upgrade, and then the whole library rebuilds (because sage-x.y.z is new), right?  Or is that not how sage-upgrade works?\n\nThe Sage library is \"new\" in every Sage version (even if there were no real changes to it), but does **not** get rebuilt *from scratch* (since there's no reason to do so if the dependencies are correct [or at least close to complete].)",
    "created_at": "2010-09-29T20:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96570",
    "user": "@nexttime"
}
```

Replying to [comment:147 kcrisman]:
> Leif, is this really a problem? (Asked as a query, not a complaint.)  Presumably someone will only use these packages via sage-upgrade, and then the whole library rebuilds (because sage-x.y.z is new), right?  Or is that not how sage-upgrade works?

The Sage library is "new" in every Sage version (even if there were no real changes to it), but does **not** get rebuilt *from scratch* (since there's no reason to do so if the dependencies are correct [or at least close to complete].)



---

archive/issue_comments_096571.json:
```json
{
    "body": "P.S.: `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could be an option, too.",
    "created_at": "2010-09-29T20:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96571",
    "user": "@nexttime"
}
```

P.S.: `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could be an option, too.



---

archive/issue_comments_096572.json:
```json
{
    "body": "I can do that, but this still won't solve the problem. Perhaps you misunderstand me, so I explain it again in more detail.\n\nAfter installing numpy the only thing that has to be done is to recompile the .pyx files (which don't have changed), so that the old .c files (which haven't changed either) have be builded with the new version of numpy, that actually the change happens. I'm not a pro to sage, but as far I understood that is, that -b only recompile changed files. No changes, no compilation. Even if I add now the changed files (the package) sage only would recompile those, and leaves out a whole lot of files which also have to be recompiled. The only way to get now sage to recompile those .pyx which is to change the files after installation for example by putting a comment into them, or force sage to recompile them, that is that what -ba does. since there is no option that I know to force recompilation, I don't have an Idea how else I could get it working.\n\nIf you have a better way please let me know. I will apply a patch as soon as possible!\n\n`@`kcrisman: didn't we talk about linux ppc? You said it builds on OS X ppc, or am I wrong?",
    "created_at": "2010-09-29T20:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96572",
    "user": "maldun"
}
```

I can do that, but this still won't solve the problem. Perhaps you misunderstand me, so I explain it again in more detail.

After installing numpy the only thing that has to be done is to recompile the .pyx files (which don't have changed), so that the old .c files (which haven't changed either) have be builded with the new version of numpy, that actually the change happens. I'm not a pro to sage, but as far I understood that is, that -b only recompile changed files. No changes, no compilation. Even if I add now the changed files (the package) sage only would recompile those, and leaves out a whole lot of files which also have to be recompiled. The only way to get now sage to recompile those .pyx which is to change the files after installation for example by putting a comment into them, or force sage to recompile them, that is that what -ba does. since there is no option that I know to force recompilation, I don't have an Idea how else I could get it working.

If you have a better way please let me know. I will apply a patch as soon as possible!

`@`kcrisman: didn't we talk about linux ppc? You said it builds on OS X ppc, or am I wrong?



---

archive/issue_comments_096573.json:
```json
{
    "body": "No, I'm sorry if you misread my post about that.  I would *like* to do so but there are still a number of technical hurdles to me running Linux PPC on my box (I think this should be clear in my sage-devel post).  I am testing whether the change you made to support Linux PPC doesn't break anything.  Sorry if this is not useful :( and I wish I did have access to Linux PPC more easily; unfortunately, this requires either having access to an already existing Linux PPC machine OR trying to run an image of Linux on a CD even with so little RAM there is no point OR using a portable hard drive, which is a more significant expense.",
    "created_at": "2010-09-29T20:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96573",
    "user": "@kcrisman"
}
```

No, I'm sorry if you misread my post about that.  I would *like* to do so but there are still a number of technical hurdles to me running Linux PPC on my box (I think this should be clear in my sage-devel post).  I am testing whether the change you made to support Linux PPC doesn't break anything.  Sorry if this is not useful :( and I wish I did have access to Linux PPC more easily; unfortunately, this requires either having access to an already existing Linux PPC machine OR trying to run an image of Linux on a CD even with so little RAM there is no point OR using a portable hard drive, which is a more significant expense.



---

archive/issue_comments_096574.json:
```json
{
    "body": "Apparently we have to add Carl Friedrich Gauss to the authors... ;-)",
    "created_at": "2010-09-29T20:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96574",
    "user": "@nexttime"
}
```

Apparently we have to add Carl Friedrich Gauss to the authors... ;-)



---

archive/issue_comments_096575.json:
```json
{
    "body": "As I feared: Making them dependent didn't force compilation either.",
    "created_at": "2010-09-29T21:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96575",
    "user": "maldun"
}
```

As I feared: Making them dependent didn't force compilation either.



---

archive/issue_comments_096576.json:
```json
{
    "body": "Update: If you are changing the numpy.pxd file (for example insert a blank line and delete it) sage -b compile the dependent sources, but this file is in cython not in numpy.\n\nmanual changes on the numpy header files didn't do anything. \n\n`@`Leif I know what you are trying to tell me. I would have expected that making a header dependent would get sage to resolve the dependencies and recompile the .pyx files also.\n\nBut even little changes to the header files do nothing even if they are dependent, or I forced dependency.\n\nI didn't meant this as offense or something, I just told you what I had experienced in the\nearly stages of this ticket.\nIf you have a solution for example a diff with an entry that forces dependency, (plot3d for example) I could write the others in no time.\n\n\n\nPerhaps I do something wrong. If you know what the trouble is please tell me.",
    "created_at": "2010-09-29T22:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96576",
    "user": "maldun"
}
```

Update: If you are changing the numpy.pxd file (for example insert a blank line and delete it) sage -b compile the dependent sources, but this file is in cython not in numpy.

manual changes on the numpy header files didn't do anything. 

`@`Leif I know what you are trying to tell me. I would have expected that making a header dependent would get sage to resolve the dependencies and recompile the .pyx files also.

But even little changes to the header files do nothing even if they are dependent, or I forced dependency.

I didn't meant this as offense or something, I just told you what I had experienced in the
early stages of this ticket.
If you have a solution for example a diff with an entry that forces dependency, (plot3d for example) I could write the others in no time.



Perhaps I do something wrong. If you know what the trouble is please tell me.



---

archive/issue_comments_096577.json:
```json
{
    "body": "There are only a few headers that actually have been updated, e.g. `_numpyconfig.h`.\n\nA trivial solution is to just `touch` one header file after installation in `spkg-install`, and make the relevant extension modules (also) depend on that one.\n\nTouching `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could also help.",
    "created_at": "2010-09-29T22:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96577",
    "user": "@nexttime"
}
```

There are only a few headers that actually have been updated, e.g. `_numpyconfig.h`.

A trivial solution is to just `touch` one header file after installation in `spkg-install`, and make the relevant extension modules (also) depend on that one.

Touching `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could also help.



---

archive/issue_comments_096578.json:
```json
{
    "body": "Replying to [comment:156 leif]:\n> Touching `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could also help.\n\nDoing so triggers at least recompilation of the 13 extension modules that add the numpy include dir to their `include_dirs`.",
    "created_at": "2010-09-29T22:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96578",
    "user": "@nexttime"
}
```

Replying to [comment:156 leif]:
> Touching `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could also help.

Doing so triggers at least recompilation of the 13 extension modules that add the numpy include dir to their `include_dirs`.



---

archive/issue_comments_096579.json:
```json
{
    "body": "Lots happens when I am asleep and lecturing first thing in the morning :)\n\nI cannot comment on the sage-release thread from work. I am one of the few\npeople running sage on linux ppc - more as hobby to check that it works than real\nproduction. The problem for numpy on ppc is fixed in numpy-1.5.\n\ncannot comment on the rest right now I have a truckload of exams to prepare.",
    "created_at": "2010-09-29T22:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96579",
    "user": "@kiwifb"
}
```

Lots happens when I am asleep and lecturing first thing in the morning :)

I cannot comment on the sage-release thread from work. I am one of the few
people running sage on linux ppc - more as hobby to check that it works than real
production. The problem for numpy on ppc is fixed in numpy-1.5.

cannot comment on the rest right now I have a truckload of exams to prepare.



---

archive/issue_comments_096580.json:
```json
{
    "body": "Replying to [comment:157 leif]:\n> Replying to [comment:156 leif]:\n> > Touching `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could also help.\n> \n> Doing so triggers at least recompilation of the 13 extension modules that add the numpy include dir to their `include_dirs`.\n\n... and caused `ptestlong` to pass without any errors. So touching just that file in numpy's `spkg-install` should fix all dependency issues, without touching `module_list.py` at all (which is advantageous, too).\n\nI just wonder that (or if) that file is still compatible with the new numpy.\n\n----\n\nRegarding the discussion on sage-release, who prepares a numpy 1.5.0 (or later) spkg? ;-)\n\nThe 1.4.1 seems obsolete now...",
    "created_at": "2010-09-30T00:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96580",
    "user": "@nexttime"
}
```

Replying to [comment:157 leif]:
> Replying to [comment:156 leif]:
> > Touching `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could also help.
> 
> Doing so triggers at least recompilation of the 13 extension modules that add the numpy include dir to their `include_dirs`.

... and caused `ptestlong` to pass without any errors. So touching just that file in numpy's `spkg-install` should fix all dependency issues, without touching `module_list.py` at all (which is advantageous, too).

I just wonder that (or if) that file is still compatible with the new numpy.

----

Regarding the discussion on sage-release, who prepares a numpy 1.5.0 (or later) spkg? ;-)

The 1.4.1 seems obsolete now...



---

archive/issue_comments_096581.json:
```json
{
    "body": "Replying to [comment:159 leif]:\n> So touching just that file in numpy's `spkg-install` should fix all dependency issues, without touching `module_list.py` at all (which is advantageous, too).\n\nUnfortunately this will only work if Cython is not updated/rebuilt (after numpy has been installed), since none of these packages depends on the other, and Cython might still ship one with an old time stamp (which is preserved on installation).",
    "created_at": "2010-09-30T00:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96581",
    "user": "@nexttime"
}
```

Replying to [comment:159 leif]:
> So touching just that file in numpy's `spkg-install` should fix all dependency issues, without touching `module_list.py` at all (which is advantageous, too).

Unfortunately this will only work if Cython is not updated/rebuilt (after numpy has been installed), since none of these packages depends on the other, and Cython might still ship one with an old time stamp (which is preserved on installation).



---

archive/issue_comments_096582.json:
```json
{
    "body": ">Regarding the discussion on sage-release, who prepares a numpy 1.5.0 (or later) spkg? ;-)\n>\n>The 1.4.1 seems obsolete now... \n\nI do. There are only 2 doctests that fails, due to output changes inf -> Inf\nI hope I can complete it over the weekend.\n\nActually there is another problem with the headers: You would have to make ALL haeaders dependent on the concerning entries in the module_list.py, because in every version of numpy there can be an other headers that changes... and of course that is a matter of taste, but wouldn't get this the module_list.py a little bit messy, with dependencies that actually aren't needed?\n\njust my 2 cents",
    "created_at": "2010-09-30T08:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96582",
    "user": "maldun"
}
```

>Regarding the discussion on sage-release, who prepares a numpy 1.5.0 (or later) spkg? ;-)
>
>The 1.4.1 seems obsolete now... 

I do. There are only 2 doctests that fails, due to output changes inf -> Inf
I hope I can complete it over the weekend.

Actually there is another problem with the headers: You would have to make ALL haeaders dependent on the concerning entries in the module_list.py, because in every version of numpy there can be an other headers that changes... and of course that is a matter of taste, but wouldn't get this the module_list.py a little bit messy, with dependencies that actually aren't needed?

just my 2 cents



---

archive/issue_comments_096583.json:
```json
{
    "body": "Replying to [comment:142 maldun]:\n> Replying to [comment:141 leif]:\n> > Dave pointed me to this ticket the day before yesterday (and I read it from the beginning). ;-)\n> > \n> > Despite that, it's unclear to me which diffs are currrent, and the description should IMHO be updated wrt. what's to be done to review this.\n> > \n> > `./sage -ba` is also in my opinion not a solution to get dependent extension modules updated, i.e. if `./sage -b` isn't sufficient, dependencies should be added to `module_list.py`.\n> > \n> \n> I cleaned up the discription a little bit, and deleted the obsolete remark about networkx-1.2\n> \n> I don't know if this is a good Idea because this is a whole bunch of files we are talking about, which have to be added. Perhaps you won't save much time either when compiling. I first tried this too, but after about 2 hours searching, I got somehow tired of this... And after merging numpy > 1.3.x into Sage this has not to be done anymore. All versions of 1.5.x builded without problems, and didn't need -ba anymore.\n> You only have to do this when big changes are happening, and this is rather occassionally.\n> \n> package with a linux ppc patch is out: http://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.4.1.p0.spkg\n> hope it works this time!\n\nOk so I tried to build numpy-1.4.1 with our patch on ppc. Didn't work.\nIt may be a good start but it fails in the same way it did before:\n\n```\n\ufffd[39mcompile options: '-Inumpy/core/src/private -Inumpy/core/src -Inumpy/core -Inumpy/core/src/npymath -Inumpy/core/src/multiarray -Inumpy/core/src/umath -Inumpy/core/include -I/usr/include/python2.6 -c'\ufffd[0m\n\ufffd[39mpowerpc-unknown-linux-gnu-gcc: _configtest.c\ufffd[0m\n\ufffd[39mremoving: _configtest.c _configtest.o\ufffd[0m\nTraceback (most recent call last):\n  File \"setup.py\", line 187, in <module>\n    setup_package()\n  File \"setup.py\", line 180, in setup_package\n    configuration=configuration )\n  File \"/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/core.py\", line 186, in setup\n    return old_setup(**new_attr)\n  File \"/usr/lib/python2.6/distutils/core.py\", line 152, in setup\n    dist.run_commands()\n  File \"/usr/lib/python2.6/distutils/dist.py\", line 975, in run_commands\n    self.run_command(cmd)\n  File \"/usr/lib/python2.6/distutils/dist.py\", line 995, in run_command\n    cmd_obj.run()\n  File \"/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/command/build.py\", line 37, in run\n    old_build.run(self)\n  File \"/usr/lib/python2.6/distutils/command/build.py\", line 134, in run\n    self.run_command(cmd_name)\n  File \"/usr/lib/python2.6/distutils/cmd.py\", line 333, in run_command\n    self.distribution.run_command(command)\n  File \"/usr/lib/python2.6/distutils/dist.py\", line 995, in run_command\n    cmd_obj.run()\n  File \"/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/command/build_src.py\", line 152, in run\n    self.build_sources()\n  File \"/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/command/build_src.py\", line 169, in build_sources\n    self.build_extension_sources(ext)\n  File \"/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/command/build_src.py\", line 328, in build_extension_sources\n    sources = self.generate_sources(sources, ext)\n  File \"/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/command/build_src.py\", line 385, in generate_sources\n    source = func(extension, build_dir)\n  File \"numpy/core/setup.py\", line 416, in generate_config_h\n    rep = check_long_double_representation(config_cmd)\n  File \"numpy/core/setup_common.py\", line 136, in check_long_double_representation\n    type = long_double_representation(pyod(object))\n  File \"numpy/core/setup_common.py\", line 244, in long_double_representation\n    raise ValueError(\"Unrecognized format (%s)\" % saw)\nValueError: Unrecognized format (['001', '043', '105', '147', '211', '253', '315', '357', '301', '235', '157', '064', '124', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '376', '334', '272', '230', '166', '124', '062', '020'])\n \ufffd[31;01m*\ufffd[0m ERROR: dev-python/numpy-1.4.1 failed:\n```\n\nThe expectation from numpy/core/setup_common.py is:\n\n```\nLONG_DOUBLE_REPRESENTATION_SRC = r\"\"\"\n/* \"before\" is 16 bytes to ensure there's no padding between it and \"x\".\n *    We're not expecting any \"long double\" bigger than 16 bytes or with\n *       alignment requirements stricter than 16 bytes.  */\ntypedef %(type)s test_type;\n\nstruct {\n        char         before[16];\n        test_type    x;\n        char         after[8];\n} foo = {\n        { '\\0', '\\0', '\\0', '\\0', '\\0', '\\0', '\\0', '\\0',\n          '\\001', '\\043', '\\105', '\\147', '\\211', '\\253', '\\315', '\\357' },\n        -123456789.0,\n        { '\\376', '\\334', '\\272', '\\230', '\\166', '\\124', '\\062', '\\020' }\n};\n\"\"\"\n```\n\nAnd when you compare the two you can see that it is an endianess problem.",
    "created_at": "2010-10-01T00:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96583",
    "user": "@kiwifb"
}
```

Replying to [comment:142 maldun]:
> Replying to [comment:141 leif]:
> > Dave pointed me to this ticket the day before yesterday (and I read it from the beginning). ;-)
> > 
> > Despite that, it's unclear to me which diffs are currrent, and the description should IMHO be updated wrt. what's to be done to review this.
> > 
> > `./sage -ba` is also in my opinion not a solution to get dependent extension modules updated, i.e. if `./sage -b` isn't sufficient, dependencies should be added to `module_list.py`.
> > 
> 
> I cleaned up the discription a little bit, and deleted the obsolete remark about networkx-1.2
> 
> I don't know if this is a good Idea because this is a whole bunch of files we are talking about, which have to be added. Perhaps you won't save much time either when compiling. I first tried this too, but after about 2 hours searching, I got somehow tired of this... And after merging numpy > 1.3.x into Sage this has not to be done anymore. All versions of 1.5.x builded without problems, and didn't need -ba anymore.
> You only have to do this when big changes are happening, and this is rather occassionally.
> 
> package with a linux ppc patch is out: http://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.4.1.p0.spkg
> hope it works this time!

Ok so I tried to build numpy-1.4.1 with our patch on ppc. Didn't work.
It may be a good start but it fails in the same way it did before:

```
�[39mcompile options: '-Inumpy/core/src/private -Inumpy/core/src -Inumpy/core -Inumpy/core/src/npymath -Inumpy/core/src/multiarray -Inumpy/core/src/umath -Inumpy/core/include -I/usr/include/python2.6 -c'�[0m
�[39mpowerpc-unknown-linux-gnu-gcc: _configtest.c�[0m
�[39mremoving: _configtest.c _configtest.o�[0m
Traceback (most recent call last):
  File "setup.py", line 187, in <module>
    setup_package()
  File "setup.py", line 180, in setup_package
    configuration=configuration )
  File "/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/core.py", line 186, in setup
    return old_setup(**new_attr)
  File "/usr/lib/python2.6/distutils/core.py", line 152, in setup
    dist.run_commands()
  File "/usr/lib/python2.6/distutils/dist.py", line 975, in run_commands
    self.run_command(cmd)
  File "/usr/lib/python2.6/distutils/dist.py", line 995, in run_command
    cmd_obj.run()
  File "/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/command/build.py", line 37, in run
    old_build.run(self)
  File "/usr/lib/python2.6/distutils/command/build.py", line 134, in run
    self.run_command(cmd_name)
  File "/usr/lib/python2.6/distutils/cmd.py", line 333, in run_command
    self.distribution.run_command(command)
  File "/usr/lib/python2.6/distutils/dist.py", line 995, in run_command
    cmd_obj.run()
  File "/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/command/build_src.py", line 152, in run
    self.build_sources()
  File "/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/command/build_src.py", line 169, in build_sources
    self.build_extension_sources(ext)
  File "/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/command/build_src.py", line 328, in build_extension_sources
    sources = self.generate_sources(sources, ext)
  File "/scratch/portage/portage/dev-python/numpy-1.4.1/work/numpy-1.4.1/numpy/distutils/command/build_src.py", line 385, in generate_sources
    source = func(extension, build_dir)
  File "numpy/core/setup.py", line 416, in generate_config_h
    rep = check_long_double_representation(config_cmd)
  File "numpy/core/setup_common.py", line 136, in check_long_double_representation
    type = long_double_representation(pyod(object))
  File "numpy/core/setup_common.py", line 244, in long_double_representation
    raise ValueError("Unrecognized format (%s)" % saw)
ValueError: Unrecognized format (['001', '043', '105', '147', '211', '253', '315', '357', '301', '235', '157', '064', '124', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '376', '334', '272', '230', '166', '124', '062', '020'])
 �[31;01m*�[0m ERROR: dev-python/numpy-1.4.1 failed:
```

The expectation from numpy/core/setup_common.py is:

```
LONG_DOUBLE_REPRESENTATION_SRC = r"""
/* "before" is 16 bytes to ensure there's no padding between it and "x".
 *    We're not expecting any "long double" bigger than 16 bytes or with
 *       alignment requirements stricter than 16 bytes.  */
typedef %(type)s test_type;

struct {
        char         before[16];
        test_type    x;
        char         after[8];
} foo = {
        { '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0',
          '\001', '\043', '\105', '\147', '\211', '\253', '\315', '\357' },
        -123456789.0,
        { '\376', '\334', '\272', '\230', '\166', '\124', '\062', '\020' }
};
"""
```

And when you compare the two you can see that it is an endianess problem.



---

archive/issue_comments_096584.json:
```json
{
    "body": "Attachment [numpy-spkg-install.diff](tarball://root/attachments/some-uuid/ticket9808/numpy-spkg-install.diff) by maldun created at 2010-10-02 18:58:44\n\nChanges of the spkg-install from the upgrade to 1.3.x to 1.5.0 (changes that were applied to 1.4.1 are also contained)",
    "created_at": "2010-10-02T18:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96584",
    "user": "maldun"
}
```

Attachment [numpy-spkg-install.diff](tarball://root/attachments/some-uuid/ticket9808/numpy-spkg-install.diff) by maldun created at 2010-10-02 18:58:44

Changes of the spkg-install from the upgrade to 1.3.x to 1.5.0 (changes that were applied to 1.4.1 are also contained)



---

archive/issue_comments_096585.json:
```json
{
    "body": "Attachment [scipy-spkg-install.diff](tarball://root/attachments/some-uuid/ticket9808/scipy-spkg-install.diff) by maldun created at 2010-10-02 18:59:54\n\ndiff of the spkg-install of scipy from 0.7.p5 to 0.8",
    "created_at": "2010-10-02T18:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96585",
    "user": "maldun"
}
```

Attachment [scipy-spkg-install.diff](tarball://root/attachments/some-uuid/ticket9808/scipy-spkg-install.diff) by maldun created at 2010-10-02 18:59:54

diff of the spkg-install of scipy from 0.7.p5 to 0.8



---

archive/issue_comments_096586.json:
```json
{
    "body": "I am incorporating that in my 4.6alpha2 branch on Gentoo right now.\n\nI will unfortunately be unable to test it on linux ppc before Wednesday 6th \nbecause of limited access to the hardware. So it may be too short for me to do\na comprehensive review for the alpha3 deadline. I already know for sure that\nnumpy-1.5.0/scipy-0.8.0 will build it's just the testing that will be lacking.",
    "created_at": "2010-10-02T23:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96586",
    "user": "@kiwifb"
}
```

I am incorporating that in my 4.6alpha2 branch on Gentoo right now.

I will unfortunately be unable to test it on linux ppc before Wednesday 6th 
because of limited access to the hardware. So it may be too short for me to do
a comprehensive review for the alpha3 deadline. I already know for sure that
numpy-1.5.0/scipy-0.8.0 will build it's just the testing that will be lacking.



---

archive/issue_comments_096587.json:
```json
{
    "body": "Build on linux x86 and tests pass here on 4.6alpha2.",
    "created_at": "2010-10-03T07:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96587",
    "user": "@kiwifb"
}
```

Build on linux x86 and tests pass here on 4.6alpha2.



---

archive/issue_comments_096588.json:
```json
{
    "body": "What do I need to do to install these?  I did this: unpacked a sage-4.6.alpha2 tarball, downloaded the new numpy and scipy spkg files, applied the file \"trac_9808_numpy_doctest_change.patch\" to the main Sage library spkg, and built Sage from scratch (with SAGE_CHECK=yes, except when installing the python spkg, which always fails self-tests).  On taurus (a skynet linux machine, x86_64-Linux-nehalem-fc), I'm getting doctest failures:\n\n```\nThe following tests failed:\n\n        sage -t  -long devel/sage/sage/plot/plot.py # 12 doctests failed\n        sage -t  -long devel/sage/sage/misc/citation.pyx # 2 doctests failed\n        sage -t  -long devel/sage/sage/plot/misc.py # 4 doctests failed\n```\n\nFor example:\n\n```\nsage -t  -long devel/sage/sage/misc/citation.pyx\n**********************************************************************\nFile \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/devel/sage-main/sage/misc/citation.pyx\", line 60\\\n:\n    sage: get_systems('integrate(x^2, x)')\nExpected:\n    ['ginac', 'Maxima']\nGot:\n    ['numpy', 'ginac', 'Maxima']\n**********************************************************************\n```\n\nand\n\n```\nsage -t  -long devel/sage/sage/plot/plot.py\n**********************************************************************\nFile \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/devel/sage-main/sage/plot/plot.py\", line 207:\n    sage: (g1+g2).show(ticks=pi/6, tick_formatter=pi)  # show their sum, nicely formatted\nException raised:\n    Traceback (most recent call last):\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[49]>\", line 1, in <module>\n        (g1+g2).show(ticks=pi/Integer(6), tick_formatter=pi)  # show their sum, nicely formatted###line 207:\n    sage: (g1+g2).show(ticks=pi/6, tick_formatter=pi)  # show their sum, nicely formatted\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/sage/plot/plot.py\", line 1546, in show\n        self.save(DOCTEST_MODE_FILE, **options)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/sage/plot/plot.py\", line 2202, in save\n        figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/figure.py\", line 1032, in savefig\n        self.canvas.print_figure(*args, **kwargs)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/backend_bases.py\", line 1455, in print_figure\n        **kwargs)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/backends/backend_agg.py\", line 358, in print_png\n        FigureCanvasAgg.draw(self)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/backends/backend_agg.py\", line 314, in draw\n        self.figure.draw(self.renderer)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/artist.py\", line 46, in draw_wrapper\n        draw(artist, renderer, *args, **kwargs)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/figure.py\", line 773, in draw\n        for a in self.axes: a.draw(renderer)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/artist.py\", line 46, in draw_wrapper\n        draw(artist, renderer, *args, **kwargs)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/axes.py\", line 1735, in draw\n        a.draw(renderer)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/artist.py\", line 46, in draw_wrapper\n        draw(artist, renderer, *args, **kwargs)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/axis.py\", line 742, in draw\n        tick.draw(renderer)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/artist.py\", line 46, in draw_wrapper\n        draw(artist, renderer, *args, **kwargs)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/axis.py\", line 196, in draw\n        self.label1.draw(renderer)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/text.py\", line 518, in draw\n        bbox, info = self._get_layout(renderer)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/text.py\", line 280, in _get_layout\n        clean_line, self._fontproperties, ismath=ismath)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/backends/backend_agg.py\", line 156, in get_text_width_height_descent\n        self.mathtext_parser.parse(s, self.dpi, prop)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/mathtext.py\", line 2797, in parse\n        font_output = fontset_class(prop, backend)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/mathtext.py\", line 658, in __init__\n        self._stix_fallback = StixFonts(*args, **kwargs)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/mathtext.py\", line 900, in __init__\n        fullpath = findfont(name)\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/font_manager.py\", line 1306, in findfont\n        if not os.path.exists(font):\n      File \"/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python2.6/genericpath.py\", line 18, in exists\n        st = os.stat(path)\n    TypeError: coercing to Unicode: need string or buffer, dict found\n```\n",
    "created_at": "2010-10-05T00:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96588",
    "user": "@jhpalmieri"
}
```

What do I need to do to install these?  I did this: unpacked a sage-4.6.alpha2 tarball, downloaded the new numpy and scipy spkg files, applied the file "trac_9808_numpy_doctest_change.patch" to the main Sage library spkg, and built Sage from scratch (with SAGE_CHECK=yes, except when installing the python spkg, which always fails self-tests).  On taurus (a skynet linux machine, x86_64-Linux-nehalem-fc), I'm getting doctest failures:

```
The following tests failed:

        sage -t  -long devel/sage/sage/plot/plot.py # 12 doctests failed
        sage -t  -long devel/sage/sage/misc/citation.pyx # 2 doctests failed
        sage -t  -long devel/sage/sage/plot/misc.py # 4 doctests failed
```

For example:

```
sage -t  -long devel/sage/sage/misc/citation.pyx
**********************************************************************
File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/devel/sage-main/sage/misc/citation.pyx", line 60\
:
    sage: get_systems('integrate(x^2, x)')
Expected:
    ['ginac', 'Maxima']
Got:
    ['numpy', 'ginac', 'Maxima']
**********************************************************************
```

and

```
sage -t  -long devel/sage/sage/plot/plot.py
**********************************************************************
File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/devel/sage-main/sage/plot/plot.py", line 207:
    sage: (g1+g2).show(ticks=pi/6, tick_formatter=pi)  # show their sum, nicely formatted
Exception raised:
    Traceback (most recent call last):
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[49]>", line 1, in <module>
        (g1+g2).show(ticks=pi/Integer(6), tick_formatter=pi)  # show their sum, nicely formatted###line 207:
    sage: (g1+g2).show(ticks=pi/6, tick_formatter=pi)  # show their sum, nicely formatted
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/sage/plot/plot.py", line 1546, in show
        self.save(DOCTEST_MODE_FILE, **options)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/sage/plot/plot.py", line 2202, in save
        figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/figure.py", line 1032, in savefig
        self.canvas.print_figure(*args, **kwargs)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/backend_bases.py", line 1455, in print_figure
        **kwargs)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 358, in print_png
        FigureCanvasAgg.draw(self)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 314, in draw
        self.figure.draw(self.renderer)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/artist.py", line 46, in draw_wrapper
        draw(artist, renderer, *args, **kwargs)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/figure.py", line 773, in draw
        for a in self.axes: a.draw(renderer)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/artist.py", line 46, in draw_wrapper
        draw(artist, renderer, *args, **kwargs)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/axes.py", line 1735, in draw
        a.draw(renderer)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/artist.py", line 46, in draw_wrapper
        draw(artist, renderer, *args, **kwargs)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/axis.py", line 742, in draw
        tick.draw(renderer)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/artist.py", line 46, in draw_wrapper
        draw(artist, renderer, *args, **kwargs)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/axis.py", line 196, in draw
        self.label1.draw(renderer)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/text.py", line 518, in draw
        bbox, info = self._get_layout(renderer)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/text.py", line 280, in _get_layout
        clean_line, self._fontproperties, ismath=ismath)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 156, in get_text_width_height_descent
        self.mathtext_parser.parse(s, self.dpi, prop)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/mathtext.py", line 2797, in parse
        font_output = fontset_class(prop, backend)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/mathtext.py", line 658, in __init__
        self._stix_fallback = StixFonts(*args, **kwargs)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/mathtext.py", line 900, in __init__
        fullpath = findfont(name)
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python/site-packages/matplotlib/font_manager.py", line 1306, in findfont
        if not os.path.exists(font):
      File "/home/palmieri/taurus/numpy/sage-4.6.alpha2/local/lib/python2.6/genericpath.py", line 18, in exists
        st = os.stat(path)
    TypeError: coercing to Unicode: need string or buffer, dict found
```




---

archive/issue_comments_096589.json:
```json
{
    "body": "Another report: on the skynet machine fulvia (Solaris on x86), matplotlib fails to find numpy, so it doesn't install:\n\n```\n============================================================================\nBUILDING MATPLOTLIB\n            matplotlib: 0.99.3\n                python: 2.6.4 (r264:75706, Oct  4 2010, 18:22:25)  [GCC\n                        4.5.1]\n              platform: sunos5\n\nREQUIRED DEPENDENCIES\n                 numpy: no\n                        * You must install numpy 1.1 or later to build\n                        * matplotlib.\nError building matplotlib package.\n\nreal    0m1.344s\nuser    0m0.062s\nsys     0m0.093s\nsage: An error occurred while installing matplotlib-0.99.3\n```\n\nThe new numpy package has already been installed at this point in the build, so I don't know what's going on here.  On the same machine, scipy fails to install:\n\n```\ngcc version 4.5.1 (GCC)\n****************************************************\n./spkg-install: LDFLAGS=-shared: is not an identifier\n```\n\nPerhaps you need something like `LDFLAGS=\"-shared\"`?  I'm not really sure.",
    "created_at": "2010-10-05T00:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96589",
    "user": "@jhpalmieri"
}
```

Another report: on the skynet machine fulvia (Solaris on x86), matplotlib fails to find numpy, so it doesn't install:

```
============================================================================
BUILDING MATPLOTLIB
            matplotlib: 0.99.3
                python: 2.6.4 (r264:75706, Oct  4 2010, 18:22:25)  [GCC
                        4.5.1]
              platform: sunos5

REQUIRED DEPENDENCIES
                 numpy: no
                        * You must install numpy 1.1 or later to build
                        * matplotlib.
Error building matplotlib package.

real    0m1.344s
user    0m0.062s
sys     0m0.093s
sage: An error occurred while installing matplotlib-0.99.3
```

The new numpy package has already been installed at this point in the build, so I don't know what's going on here.  On the same machine, scipy fails to install:

```
gcc version 4.5.1 (GCC)
****************************************************
./spkg-install: LDFLAGS=-shared: is not an identifier
```

Perhaps you need something like `LDFLAGS="-shared"`?  I'm not really sure.



---

archive/issue_comments_096590.json:
```json
{
    "body": "Can you try the new matplotlib spkg on #9221, if you think it is a matplotlib problem?",
    "created_at": "2010-10-05T00:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96590",
    "user": "@jasongrout"
}
```

Can you try the new matplotlib spkg on #9221, if you think it is a matplotlib problem?



---

archive/issue_comments_096591.json:
```json
{
    "body": "Replying to [comment:169 jason]:\n> Can you try the new matplotlib spkg on #9221, if you think it is a matplotlib problem?\n\nFor fulvia, it doesn't help: I still get the same error about numpy not being installed.  If I run `./sage -python` and then `import numpy`, I get an error, so although the numpy spkg claims to install correctly, there is some kind of problem:\n\n```\nImportError: ld.so.1: python: fatal: relocation error: file /home/palmieri/fulvia/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/multiarray.so: symbol isfinite: referenced symbol not found\n```\n\n\nFor taurus, using the new matplotlib spkg (and applying the patch from #9221) does seem to fix most of the problems: \n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t  -long devel/sage/sage/misc/citation.pyx # 2 doctests failed\n----------------------------------------------------------------------\n```\n",
    "created_at": "2010-10-05T02:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96591",
    "user": "@jhpalmieri"
}
```

Replying to [comment:169 jason]:
> Can you try the new matplotlib spkg on #9221, if you think it is a matplotlib problem?

For fulvia, it doesn't help: I still get the same error about numpy not being installed.  If I run `./sage -python` and then `import numpy`, I get an error, so although the numpy spkg claims to install correctly, there is some kind of problem:

```
ImportError: ld.so.1: python: fatal: relocation error: file /home/palmieri/fulvia/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/multiarray.so: symbol isfinite: referenced symbol not found
```


For taurus, using the new matplotlib spkg (and applying the patch from #9221) does seem to fix most of the problems: 

```
----------------------------------------------------------------------

The following tests failed:

        sage -t  -long devel/sage/sage/misc/citation.pyx # 2 doctests failed
----------------------------------------------------------------------
```




---

archive/issue_comments_096592.json:
```json
{
    "body": "Dear me!\n\nAnd I was going to report numpy-1.5/scipy-0.8 build on ppc (should be running testall now, I'd do -long but on that hardware we would still be there next week).\n\nOK there are several issues to be solved: first  \"-shared\" is a good idea. That\ncould be it.\n\nFailing to build matplotlib with an installed numpy :) where did I see something like that... Why, I reported a bug on that on gentoo bugzilla a while ago:\n[http://bugs.gentoo.org/show_bug.cgi?id=320669](http://bugs.gentoo.org/show_bug.cgi?id=320669).\n\nLong story short: that means your lapack (and possibly ATLAS) install is hosed. \nProbably related to problems producing .so libraries.\n\nI don't get any of the failures you report. A quick package check on Gentoo\nshows that: matplotlib and rpy depend on numpy and it would be a good idea to rebuild\nthem.\n\nI am a bit worried about the unicode mention in plot.py, that may mean a mismatch between various packages configuration regarding unicode (python/numpy/matplotlib).",
    "created_at": "2010-10-05T03:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96592",
    "user": "@kiwifb"
}
```

Dear me!

And I was going to report numpy-1.5/scipy-0.8 build on ppc (should be running testall now, I'd do -long but on that hardware we would still be there next week).

OK there are several issues to be solved: first  "-shared" is a good idea. That
could be it.

Failing to build matplotlib with an installed numpy :) where did I see something like that... Why, I reported a bug on that on gentoo bugzilla a while ago:
[http://bugs.gentoo.org/show_bug.cgi?id=320669](http://bugs.gentoo.org/show_bug.cgi?id=320669).

Long story short: that means your lapack (and possibly ATLAS) install is hosed. 
Probably related to problems producing .so libraries.

I don't get any of the failures you report. A quick package check on Gentoo
shows that: matplotlib and rpy depend on numpy and it would be a good idea to rebuild
them.

I am a bit worried about the unicode mention in plot.py, that may mean a mismatch between various packages configuration regarding unicode (python/numpy/matplotlib).



---

archive/issue_comments_096593.json:
```json
{
    "body": "Replying to [comment:171 fbissey]:\n> Dear me!\n> \n> And I was going to report numpy-1.5/scipy-0.8 build on ppc (should be running testall now, I'd do -long but on that hardware we would still be there next week).\n> \n> OK there are several issues to be solved: first  \"-shared\" is a good idea. That\n> could be it.\n\nOops, it looks like it's already quoted in the spkg-install file.  I changed the first line from\n\n```/bin/sh\n```\n\nto\n\n```/usr/bin/env bash \n```\n\nI don't know if this was a good idea, but it did get past that error, only to run into the same import error as when trying to install matplotlib.\n\n> Failing to build matplotlib with an installed numpy :) where did I see something like that... Why, I reported a bug on that on gentoo bugzilla a while ago:\n> [http://bugs.gentoo.org/show_bug.cgi?id=320669](http://bugs.gentoo.org/show_bug.cgi?id=320669).\n> \n> Long story short: that means your lapack (and possibly ATLAS) install is hosed. \n> Probably related to problems producing .so libraries.\n\nHmm.  We've had problems with shared libraries with ATLAS before on Solaris machines, among others, but it's interesting that this particular problem wouldn't have shown up before this.\n\n> I don't get any of the failures you report. A quick package check on Gentoo\n> shows that: matplotlib and rpy depend on numpy and it would be a good idea to rebuild\n> them.\n\nSince I'm building from scratch, all of the dependencies should work themselves out.\n\n> I am a bit worried about the unicode mention in plot.py, that may mean a mismatch between various packages configuration regarding unicode (python/numpy/matplotlib).\n\nAs Jason suggested, the new matplotlib spkg seems to fix this, at least on taurus.  Since that package has been merged as of 4.6.alpha3, it should be taken care of.",
    "created_at": "2010-10-05T03:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96593",
    "user": "@jhpalmieri"
}
```

Replying to [comment:171 fbissey]:
> Dear me!
> 
> And I was going to report numpy-1.5/scipy-0.8 build on ppc (should be running testall now, I'd do -long but on that hardware we would still be there next week).
> 
> OK there are several issues to be solved: first  "-shared" is a good idea. That
> could be it.

Oops, it looks like it's already quoted in the spkg-install file.  I changed the first line from

```/bin/sh
```

to

```/usr/bin/env bash 
```

I don't know if this was a good idea, but it did get past that error, only to run into the same import error as when trying to install matplotlib.

> Failing to build matplotlib with an installed numpy :) where did I see something like that... Why, I reported a bug on that on gentoo bugzilla a while ago:
> [http://bugs.gentoo.org/show_bug.cgi?id=320669](http://bugs.gentoo.org/show_bug.cgi?id=320669).
> 
> Long story short: that means your lapack (and possibly ATLAS) install is hosed. 
> Probably related to problems producing .so libraries.

Hmm.  We've had problems with shared libraries with ATLAS before on Solaris machines, among others, but it's interesting that this particular problem wouldn't have shown up before this.

> I don't get any of the failures you report. A quick package check on Gentoo
> shows that: matplotlib and rpy depend on numpy and it would be a good idea to rebuild
> them.

Since I'm building from scratch, all of the dependencies should work themselves out.

> I am a bit worried about the unicode mention in plot.py, that may mean a mismatch between various packages configuration regarding unicode (python/numpy/matplotlib).

As Jason suggested, the new matplotlib spkg seems to fix this, at least on taurus.  Since that package has been merged as of 4.6.alpha3, it should be taken care of.



---

archive/issue_comments_096594.json:
```json
{
    "body": "Replying to [comment:172 jhpalmieri]:\n> Replying to [comment:171 fbissey]:\n> > Dear me!\n> > \n> > And I was going to report numpy-1.5/scipy-0.8 build on ppc (should be running testall now, I'd do -long but on that hardware we would still be there next week).\n> > \n> > OK there are several issues to be solved: first  \"-shared\" is a good idea. That\n> > could be it.\n> \n> Oops, it looks like it's already quoted in the spkg-install file.  I changed the first line from\n> {{{\n> #!/bin/sh\n> }}}\n> to\n> {{{\n> #!/usr/bin/env bash \n> }}}\n> I don't know if this was a good idea, but it did get past that error, only to run into the same import error as when trying to install matplotlib.\n\nThe old version of the spkg was doing that as well. I don't think we should have\ndropped it. There may be a more elegant solution but in the meantime that should do.\n\n> \n> > Failing to build matplotlib with an installed numpy :) where did I see something like that... Why, I reported a bug on that on gentoo bugzilla a while ago:\n> > [http://bugs.gentoo.org/show_bug.cgi?id=320669](http://bugs.gentoo.org/show_bug.cgi?id=320669).\n> > \n> > Long story short: that means your lapack (and possibly ATLAS) install is hosed. \n> > Probably related to problems producing .so libraries.\n> \n> Hmm.  We've had problems with shared libraries with ATLAS before on Solaris machines, among others, but it's interesting that this particular problem wouldn't have shown up before this.\n\nI cannot comment on that, I don't know the package history of that machine. But \nsearching for numpy in the closed bugs from gentoo's bugzilla show that I haven't been the only victim of that and the answer is always the same: for a reason or another lapack or blas/cblas is foobar.\n\n> \n> > I don't get any of the failures you report. A quick package check on Gentoo\n> > shows that: matplotlib and rpy depend on numpy and it would be a good idea to rebuild\n> > them.\n> \n> Since I'm building from scratch, all of the dependencies should work themselves out.\n> \n> > I am a bit worried about the unicode mention in plot.py, that may mean a mismatch between various packages configuration regarding unicode (python/numpy/matplotlib).\n> \n> As Jason suggested, the new matplotlib spkg seems to fix this, at least on taurus.  Since that package has been merged as of 4.6.alpha3, it should be taken care of.\n\nAh! I already have matplotlib-1.0 here that's probably why I never saw any of that.",
    "created_at": "2010-10-05T06:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96594",
    "user": "@kiwifb"
}
```

Replying to [comment:172 jhpalmieri]:
> Replying to [comment:171 fbissey]:
> > Dear me!
> > 
> > And I was going to report numpy-1.5/scipy-0.8 build on ppc (should be running testall now, I'd do -long but on that hardware we would still be there next week).
> > 
> > OK there are several issues to be solved: first  "-shared" is a good idea. That
> > could be it.
> 
> Oops, it looks like it's already quoted in the spkg-install file.  I changed the first line from
> {{{
> #!/bin/sh
> }}}
> to
> {{{
> #!/usr/bin/env bash 
> }}}
> I don't know if this was a good idea, but it did get past that error, only to run into the same import error as when trying to install matplotlib.

The old version of the spkg was doing that as well. I don't think we should have
dropped it. There may be a more elegant solution but in the meantime that should do.

> 
> > Failing to build matplotlib with an installed numpy :) where did I see something like that... Why, I reported a bug on that on gentoo bugzilla a while ago:
> > [http://bugs.gentoo.org/show_bug.cgi?id=320669](http://bugs.gentoo.org/show_bug.cgi?id=320669).
> > 
> > Long story short: that means your lapack (and possibly ATLAS) install is hosed. 
> > Probably related to problems producing .so libraries.
> 
> Hmm.  We've had problems with shared libraries with ATLAS before on Solaris machines, among others, but it's interesting that this particular problem wouldn't have shown up before this.

I cannot comment on that, I don't know the package history of that machine. But 
searching for numpy in the closed bugs from gentoo's bugzilla show that I haven't been the only victim of that and the answer is always the same: for a reason or another lapack or blas/cblas is foobar.

> 
> > I don't get any of the failures you report. A quick package check on Gentoo
> > shows that: matplotlib and rpy depend on numpy and it would be a good idea to rebuild
> > them.
> 
> Since I'm building from scratch, all of the dependencies should work themselves out.
> 
> > I am a bit worried about the unicode mention in plot.py, that may mean a mismatch between various packages configuration regarding unicode (python/numpy/matplotlib).
> 
> As Jason suggested, the new matplotlib spkg seems to fix this, at least on taurus.  Since that package has been merged as of 4.6.alpha3, it should be taken care of.

Ah! I already have matplotlib-1.0 here that's probably why I never saw any of that.



---

archive/issue_comments_096595.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-05T07:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96595",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096596.json:
```json
{
    "body": "Replying to [comment:172 jhpalmieri]:\n> Replying to [comment:171 fbissey]:\n> > Long story short: that means your lapack (and possibly ATLAS) install is hosed. \n> > Probably related to problems producing .so libraries.\n> \n> Hmm.  We've had problems with shared libraries with ATLAS before on Solaris machines, among others, but it's interesting that this particular problem wouldn't have shown up before this.\n\nThe upstream ATLAS program never builds shared libraries. Mathematica only ships with static libraries for ATLAS. It's not entirely clear to me why we bother building shared libraries for ATLAS, given they have tended to cause problems on several systems. \n\nHowever, I'm not convinced that's the problem here. The ATLAS package has remained unchanged for a long time. \n\nDave",
    "created_at": "2010-10-05T07:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96596",
    "user": "drkirkby"
}
```

Replying to [comment:172 jhpalmieri]:
> Replying to [comment:171 fbissey]:
> > Long story short: that means your lapack (and possibly ATLAS) install is hosed. 
> > Probably related to problems producing .so libraries.
> 
> Hmm.  We've had problems with shared libraries with ATLAS before on Solaris machines, among others, but it's interesting that this particular problem wouldn't have shown up before this.

The upstream ATLAS program never builds shared libraries. Mathematica only ships with static libraries for ATLAS. It's not entirely clear to me why we bother building shared libraries for ATLAS, given they have tended to cause problems on several systems. 

However, I'm not convinced that's the problem here. The ATLAS package has remained unchanged for a long time. 

Dave



---

archive/issue_comments_096597.json:
```json
{
    "body": "I don't have time to look at this now, but is this being built as C99? If not, that would explain it, since `isfinite` was not defined until the C99 standard. \n\nDave",
    "created_at": "2010-10-05T08:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96597",
    "user": "drkirkby"
}
```

I don't have time to look at this now, but is this being built as C99? If not, that would explain it, since `isfinite` was not defined until the C99 standard. 

Dave



---

archive/issue_comments_096598.json:
```json
{
    "body": "Replying to [comment:175 drkirkby]:\n> I don't have time to look at this now, but is this being built as C99? If not, that would explain it, since `isfinite` was not defined until the C99 standard. \n> \nWhy would fluvia not compile stuff in C99 by default? Compared to the other platforms?\nAs for ATLAS it was a suggestion. I just know that the problem is linked to something broken in lapack and because of linking to libf77blas/libcblas it can come down to\na problem with ATLAS.\nI don't know what exactly is happening with that particular machine.",
    "created_at": "2010-10-05T08:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96598",
    "user": "@kiwifb"
}
```

Replying to [comment:175 drkirkby]:
> I don't have time to look at this now, but is this being built as C99? If not, that would explain it, since `isfinite` was not defined until the C99 standard. 
> 
Why would fluvia not compile stuff in C99 by default? Compared to the other platforms?
As for ATLAS it was a suggestion. I just know that the problem is linked to something broken in lapack and because of linking to libf77blas/libcblas it can come down to
a problem with ATLAS.
I don't know what exactly is happening with that particular machine.



---

archive/issue_comments_096599.json:
```json
{
    "body": "Replying to [comment:176 fbissey]:\n> Replying to [comment:175 drkirkby]:\n> > I don't have time to look at this now, but is this being built as C99? If not, that would explain it, since `isfinite` was not defined until the C99 standard. \n> > \n> Why would fluvia not compile stuff in C99 by default? Compared to the other platforms?\n> As for ATLAS it was a suggestion. I just know that the problem is linked to something broken in lapack and because of linking to libf77blas/libcblas it can come down to\n> a problem with ATLAS.\n> I don't know what exactly is happening with that particular machine.\n\ngcc does not compile C99 by default. \n\nhttp://gcc.gnu.org/onlinedocs/gcc-4.5.1/gcc/C-Dialect-Options.html#C-Dialect-Options\n\nsays:\n\n\n```\nstd=\n    Determine the language standard.\n\n<snip>\n\n`gnu89'\n    GNU dialect of ISO C90 (including some C99 features). This is the default for C code. \n```\n\n\nBut `isfinite` was not introduced until C99. The Sun headers tend not to define everything under the sun. \n\nI'm not saying that's the issue. But it could be. I've seen a similar issue before. \n\nDave",
    "created_at": "2010-10-05T14:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96599",
    "user": "drkirkby"
}
```

Replying to [comment:176 fbissey]:
> Replying to [comment:175 drkirkby]:
> > I don't have time to look at this now, but is this being built as C99? If not, that would explain it, since `isfinite` was not defined until the C99 standard. 
> > 
> Why would fluvia not compile stuff in C99 by default? Compared to the other platforms?
> As for ATLAS it was a suggestion. I just know that the problem is linked to something broken in lapack and because of linking to libf77blas/libcblas it can come down to
> a problem with ATLAS.
> I don't know what exactly is happening with that particular machine.

gcc does not compile C99 by default. 

http://gcc.gnu.org/onlinedocs/gcc-4.5.1/gcc/C-Dialect-Options.html#C-Dialect-Options

says:


```
std=
    Determine the language standard.

<snip>

`gnu89'
    GNU dialect of ISO C90 (including some C99 features). This is the default for C code. 
```


But `isfinite` was not introduced until C99. The Sun headers tend not to define everything under the sun. 

I'm not saying that's the issue. But it could be. I've seen a similar issue before. 

Dave



---

archive/issue_comments_096600.json:
```json
{
    "body": "For what it's worth, I redid the build on fulvia with SAGE_CHECK=yes, and ATLAS passed its self-tests.  The matplotlib package still fails to install, with the import error from numpy.",
    "created_at": "2010-10-05T14:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96600",
    "user": "@jhpalmieri"
}
```

For what it's worth, I redid the build on fulvia with SAGE_CHECK=yes, and ATLAS passed its self-tests.  The matplotlib package still fails to install, with the import error from numpy.



---

archive/issue_comments_096601.json:
```json
{
    "body": "Does matplotlib generate any sort of config.log or similar? That might indicate what the problem is. \n\nI know at one point I had issues on 64-bit builds, when Numpy thought the static library was 32-bit. \n\nhttp://projects.scipy.org/numpy/ticket/1525\nhttp://trac.sagemath.org/sage_trac/ticket/8086",
    "created_at": "2010-10-05T14:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96601",
    "user": "drkirkby"
}
```

Does matplotlib generate any sort of config.log or similar? That might indicate what the problem is. 

I know at one point I had issues on 64-bit builds, when Numpy thought the static library was 32-bit. 

http://projects.scipy.org/numpy/ticket/1525
http://trac.sagemath.org/sage_trac/ticket/8086



---

archive/issue_comments_096602.json:
```json
{
    "body": "By the way, I'm getting the same error on mark2 (Solaris on sparc) as on fulvia (Solaris on x86).  Cicero (another linux box) doesn't have this problem with building matplotlib: it's built successfully and is now doctesting.\n\nReplying to [comment:179 drkirkby]:\n> Does matplotlib generate any sort of config.log or similar? That might indicate what the problem is. \n\nI don't see any log file in spkg/build/matplotlib on the machines where this is failing.  I think the problem is what I indicated above (comment:170): matplotlib tests whether numpy is installed by running python and trying \"import numpy\".  In this case, that import fails, so matplotlib deduces that numpy is not installed.\n\nHere's the relevant code (from setupext.py):\n\n```\ndef check_for_numpy():\n    try:\n        import numpy\n    except ImportError:\n\tprint_status(\"numpy\", \"no\")\n        print_message(\"You must install numpy 1.1 or later to build matplotlib.\")\n        return False\n```\n",
    "created_at": "2010-10-05T15:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96602",
    "user": "@jhpalmieri"
}
```

By the way, I'm getting the same error on mark2 (Solaris on sparc) as on fulvia (Solaris on x86).  Cicero (another linux box) doesn't have this problem with building matplotlib: it's built successfully and is now doctesting.

Replying to [comment:179 drkirkby]:
> Does matplotlib generate any sort of config.log or similar? That might indicate what the problem is. 

I don't see any log file in spkg/build/matplotlib on the machines where this is failing.  I think the problem is what I indicated above (comment:170): matplotlib tests whether numpy is installed by running python and trying "import numpy".  In this case, that import fails, so matplotlib deduces that numpy is not installed.

Here's the relevant code (from setupext.py):

```
def check_for_numpy():
    try:
        import numpy
    except ImportError:
	print_status("numpy", "no")
        print_message("You must install numpy 1.1 or later to build matplotlib.")
        return False
```




---

archive/issue_comments_096603.json:
```json
{
    "body": "Here's a recursive grep for `isfinite` in `/usr/include` on my OpenSolaris machine. I've not tested the package on my OpenSolaris machine, but given the results on Solaris 10, I doubt it would build. \n\n\n```\ndrkirkby@hawk:~$ ggrep -R isfinite /usr/include\n/usr/include/python2.6/pyconfig.h:/* Define to 1 if you have the declaration of `isfinite', and to 0 if you\n/usr/include/python2.6/pymath.h:#define Py_IS_FINITE(X) isfinite(X)\nggrep: warning: /usr/include/gphoto2/gphoto2: recursive directory loop\n\n/usr/include/iso/math_c99.h:#undef\tisfinite\n/usr/include/iso/math_c99.h:#define\tisfinite(x)\t__extension__( \\\n/usr/include/iso/math_c99.h:\t\t\t{ __typeof(x) __x_r = (x); isfinite(__x_r) && \\\n/usr/include/iso/math_c99.h:#undef\tisfinite\n/usr/include/iso/math_c99.h:#define\tisfinite(x)\t__builtin_isfinite(x)\n```\n\n\nNote, there's no reference at all in `math.h` to `isfinite`. But when the conditions are right, the contents of `/usr/include/iso/math_c99.h` will get included, and so the macro `isfinite` will be defined. \n\nIMHO, the error message John got:\n\n\n```\nImportError: ld.so.1: python: fatal: relocation error: file /home/palmieri/fulvia/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/multiarray.so: symbol isfinite: referenced symbol not found\n```\n\n\nis related to the fact that for whatever reason, the C99 headers are not being included properly. \n\nUnless this is compiled with `-std=c99`, I doubt this will work. \n\nThis contrasts to a Linux box (sage.math) where it looks to me that `isfinite` will be defined whenever `math.h` is included. That is just an error in my opinion, as `isfinite` was not defined until the C99 standard. So Linux is wrong to define it, but some software is assuming it's defined, and so fails when it is not. \n\nIMHO, the bug is in unlikely to be LAPACK or ATLAS.",
    "created_at": "2010-10-05T17:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96603",
    "user": "drkirkby"
}
```

Here's a recursive grep for `isfinite` in `/usr/include` on my OpenSolaris machine. I've not tested the package on my OpenSolaris machine, but given the results on Solaris 10, I doubt it would build. 


```
drkirkby@hawk:~$ ggrep -R isfinite /usr/include
/usr/include/python2.6/pyconfig.h:/* Define to 1 if you have the declaration of `isfinite', and to 0 if you
/usr/include/python2.6/pymath.h:#define Py_IS_FINITE(X) isfinite(X)
ggrep: warning: /usr/include/gphoto2/gphoto2: recursive directory loop

/usr/include/iso/math_c99.h:#undef	isfinite
/usr/include/iso/math_c99.h:#define	isfinite(x)	__extension__( \
/usr/include/iso/math_c99.h:			{ __typeof(x) __x_r = (x); isfinite(__x_r) && \
/usr/include/iso/math_c99.h:#undef	isfinite
/usr/include/iso/math_c99.h:#define	isfinite(x)	__builtin_isfinite(x)
```


Note, there's no reference at all in `math.h` to `isfinite`. But when the conditions are right, the contents of `/usr/include/iso/math_c99.h` will get included, and so the macro `isfinite` will be defined. 

IMHO, the error message John got:


```
ImportError: ld.so.1: python: fatal: relocation error: file /home/palmieri/fulvia/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/multiarray.so: symbol isfinite: referenced symbol not found
```


is related to the fact that for whatever reason, the C99 headers are not being included properly. 

Unless this is compiled with `-std=c99`, I doubt this will work. 

This contrasts to a Linux box (sage.math) where it looks to me that `isfinite` will be defined whenever `math.h` is included. That is just an error in my opinion, as `isfinite` was not defined until the C99 standard. So Linux is wrong to define it, but some software is assuming it's defined, and so fails when it is not. 

IMHO, the bug is in unlikely to be LAPACK or ATLAS.



---

archive/issue_comments_096604.json:
```json
{
    "body": "The more I look at this, the more I think it's a Numpy bug. \n\nPython is not built with C99 on my machine. The `config.log` of Python shows:\n\n\n\n```\nac_cv_have_decl_isfinite=no\n```\n\n\nwhich is to be expected since its not built C99. So Numpy is at fault here I think, since that's making a reference to `isfinite` despite Python is not built with C99, so it's not defined, as evidenced by Python's `config.log`\n\nBTW John, do you want an account on my OpenSolaris machine? It can build Sage in under an hour, so is a bit quicker than fulvia. \n\nDave",
    "created_at": "2010-10-05T17:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96604",
    "user": "drkirkby"
}
```

The more I look at this, the more I think it's a Numpy bug. 

Python is not built with C99 on my machine. The `config.log` of Python shows:



```
ac_cv_have_decl_isfinite=no
```


which is to be expected since its not built C99. So Numpy is at fault here I think, since that's making a reference to `isfinite` despite Python is not built with C99, so it's not defined, as evidenced by Python's `config.log`

BTW John, do you want an account on my OpenSolaris machine? It can build Sage in under an hour, so is a bit quicker than fulvia. 

Dave



---

archive/issue_comments_096605.json:
```json
{
    "body": "IMHO, we need to see if we can reproduce this with the latest cvs/svn/whatever snapshot of Numpy, and if so, report it as a bug to \n\nhttp://projects.scipy.org/numpy\n\nIf it's been fixed, then perhaps we can add a patch to the stable version, to just correct this bug. \n\nDave",
    "created_at": "2010-10-05T17:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96605",
    "user": "drkirkby"
}
```

IMHO, we need to see if we can reproduce this with the latest cvs/svn/whatever snapshot of Numpy, and if so, report it as a bug to 

http://projects.scipy.org/numpy

If it's been fixed, then perhaps we can add a patch to the stable version, to just correct this bug. 

Dave



---

archive/issue_comments_096606.json:
```json
{
    "body": "I just downloaded the latest code (as listed [here](http://new.scipy.org/download.html#bleeding-edge-repository-access)), replaced the \"src\" directory with it, and installed it.  Running \"./sage -python\" and then \"import numpy\" results in the same error about isfinite.",
    "created_at": "2010-10-05T18:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96606",
    "user": "@jhpalmieri"
}
```

I just downloaded the latest code (as listed [here](http://new.scipy.org/download.html#bleeding-edge-repository-access)), replaced the "src" directory with it, and installed it.  Running "./sage -python" and then "import numpy" results in the same error about isfinite.



---

archive/issue_comments_096607.json:
```json
{
    "body": "I reported this as a Numpy bug: \n\nhttp://projects.scipy.org/numpy/ticket/1625",
    "created_at": "2010-10-05T19:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96607",
    "user": "drkirkby"
}
```

I reported this as a Numpy bug: 

http://projects.scipy.org/numpy/ticket/1625



---

archive/issue_comments_096608.json:
```json
{
    "body": "I see this problem on my OpenSolaris machine too, which I expected would be the case.\n\nOn my OpenSolaris machine, Python's header file pyconfig.h has in it: \n\n\n```\n/* Define to 1 if you have the declaration of `isfinite', and to 0 if you\n   don't. */\n#define HAVE_DECL_ISFINITE 0\n```\n\n\nbut Numpy's config.h has in it:\n\n\n```\n#define HAVE_DECL_ISFINITE\n```\n\n\nSomeone by the usename of 'pv' has said on the Numpy bug report http://projects.scipy.org/numpy/ticket/1625\n\n\n```\nHowever, the code at numpy/core/setup.py:218 is wrong, since it checks for #ifdef and not #if for Python's HAVE_DECL_ISFINITE. \n```\n\n\nSo it seems this is a bug, and one which should be easy to fix. Note the fix does not need to be Solaris-specific, as the code is basically wrong on any platform - you just happen to get away with it on systems where the header file defines `isfinite` even though the code is not built C99. \n\nIt's gone midnight here, I'm tired and have a lot to do all this week. But if nobody else patches this, I'll be able to do it in the next day or two. \n\nDave",
    "created_at": "2010-10-05T23:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96608",
    "user": "drkirkby"
}
```

I see this problem on my OpenSolaris machine too, which I expected would be the case.

On my OpenSolaris machine, Python's header file pyconfig.h has in it: 


```
/* Define to 1 if you have the declaration of `isfinite', and to 0 if you
   don't. */
#define HAVE_DECL_ISFINITE 0
```


but Numpy's config.h has in it:


```
#define HAVE_DECL_ISFINITE
```


Someone by the usename of 'pv' has said on the Numpy bug report http://projects.scipy.org/numpy/ticket/1625


```
However, the code at numpy/core/setup.py:218 is wrong, since it checks for #ifdef and not #if for Python's HAVE_DECL_ISFINITE. 
```


So it seems this is a bug, and one which should be easy to fix. Note the fix does not need to be Solaris-specific, as the code is basically wrong on any platform - you just happen to get away with it on systems where the header file defines `isfinite` even though the code is not built C99. 

It's gone midnight here, I'm tired and have a lot to do all this week. But if nobody else patches this, I'll be able to do it in the next day or two. 

Dave



---

archive/issue_comments_096609.json:
```json
{
    "body": "Actually a bigger fix is being proposed on the numpy list. See there - I'm going to bed!\n\ndave",
    "created_at": "2010-10-05T23:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96609",
    "user": "drkirkby"
}
```

Actually a bigger fix is being proposed on the numpy list. See there - I'm going to bed!

dave



---

archive/issue_comments_096610.json:
```json
{
    "body": "Dave, thanks a lot for working on this with the numpy people.  I prepared a new spkg and so far, the new numpy builds on fulvia, and after \"./sage -python\", \"import numpy\" works.  Matplotlib and scipy have now successfully built.  It will be a while before the build is complete, but things look good to me.\n\nI'm putting the spkg up at [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg).\n\nThis is from a current svn snapshot based on 1.5.0.  I don't know if we have a policy about names for such spkg's, so I just used the date.  I also don't know if we have a policy about whether to include the repository information, so I've kept it.  This makes the spkg much bigger than the old version...\n\nShould we mark this as \"needs review\" again?  It seems to depend on #9221.",
    "created_at": "2010-10-06T00:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96610",
    "user": "@jhpalmieri"
}
```

Dave, thanks a lot for working on this with the numpy people.  I prepared a new spkg and so far, the new numpy builds on fulvia, and after "./sage -python", "import numpy" works.  Matplotlib and scipy have now successfully built.  It will be a while before the build is complete, but things look good to me.

I'm putting the spkg up at [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg).

This is from a current svn snapshot based on 1.5.0.  I don't know if we have a policy about names for such spkg's, so I just used the date.  I also don't know if we have a policy about whether to include the repository information, so I've kept it.  This makes the spkg much bigger than the old version...

Should we mark this as "needs review" again?  It seems to depend on #9221.



---

archive/issue_comments_096611.json:
```json
{
    "body": "> Should we mark this as \"needs review\" again?\n\nOr should we wait until the patch is positively reviewed on the numpy trac server?",
    "created_at": "2010-10-06T00:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96611",
    "user": "@jhpalmieri"
}
```

> Should we mark this as "needs review" again?

Or should we wait until the patch is positively reviewed on the numpy trac server?



---

archive/issue_comments_096612.json:
```json
{
    "body": "Replying to [comment:188 jhpalmieri]:\n> Dave, thanks a lot for working on this with the numpy people.  I prepared a new spkg and so far, the new numpy builds on fulvia, and after \"./sage -python\", \"import numpy\" works.  Matplotlib and scipy have now successfully built.  It will be a while before the build is complete, but things look good to me.\n> \n> I'm putting the spkg up at [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg).\n> \n> This is from a current svn snapshot based on 1.5.0.  I don't know if we have a policy about names for such spkg's, so I just used the date.  I also don't know if we have a policy about whether to include the repository information, so I've kept it.  This makes the spkg much bigger than the old version...\n\nYou don't need to keep the svn repository history, but you do need to put the revision number in the spkg name (numpy-1.5.0.svnXXXX).\n\nHowever, I think it would be better to just include the one patch on top of 1.5.0, rather than pull an unstable release from subversion.  See the comments at the top of this trac ticket about using an unstable release (like 1.5.0RC2).",
    "created_at": "2010-10-06T00:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96612",
    "user": "@jasongrout"
}
```

Replying to [comment:188 jhpalmieri]:
> Dave, thanks a lot for working on this with the numpy people.  I prepared a new spkg and so far, the new numpy builds on fulvia, and after "./sage -python", "import numpy" works.  Matplotlib and scipy have now successfully built.  It will be a while before the build is complete, but things look good to me.
> 
> I'm putting the spkg up at [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg).
> 
> This is from a current svn snapshot based on 1.5.0.  I don't know if we have a policy about names for such spkg's, so I just used the date.  I also don't know if we have a policy about whether to include the repository information, so I've kept it.  This makes the spkg much bigger than the old version...

You don't need to keep the svn repository history, but you do need to put the revision number in the spkg name (numpy-1.5.0.svnXXXX).

However, I think it would be better to just include the one patch on top of 1.5.0, rather than pull an unstable release from subversion.  See the comments at the top of this trac ticket about using an unstable release (like 1.5.0RC2).



---

archive/issue_comments_096613.json:
```json
{
    "body": "> However, I think it would be better to just include the one patch on top of 1.5.0, rather than pull an unstable release from subversion.  See the comments at the top of this trac ticket about using an unstable release (like 1.5.0RC2).\n\nI agree on this point, for what it's worth (since I will just be doing `./sage -i` and testing).",
    "created_at": "2010-10-06T01:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96613",
    "user": "@kcrisman"
}
```

> However, I think it would be better to just include the one patch on top of 1.5.0, rather than pull an unstable release from subversion.  See the comments at the top of this trac ticket about using an unstable release (like 1.5.0RC2).

I agree on this point, for what it's worth (since I will just be doing `./sage -i` and testing).



---

archive/issue_comments_096614.json:
```json
{
    "body": "Yes, but the patch was based on the svn code, not vanilla 1.5.0.",
    "created_at": "2010-10-06T01:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96614",
    "user": "@jhpalmieri"
}
```

Yes, but the patch was based on the svn code, not vanilla 1.5.0.



---

archive/issue_comments_096615.json:
```json
{
    "body": "Replying to [comment:192 jhpalmieri]:\n> Yes, but the patch was based on the svn code, not vanilla 1.5.0.\n\nAre you saying that the patch does not apply to 1.5.0 directly?",
    "created_at": "2010-10-06T01:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96615",
    "user": "@jasongrout"
}
```

Replying to [comment:192 jhpalmieri]:
> Yes, but the patch was based on the svn code, not vanilla 1.5.0.

Are you saying that the patch does not apply to 1.5.0 directly?



---

archive/issue_comments_096616.json:
```json
{
    "body": "The patch affects two files.  One part of the patch is this:\n\n```diff\ndiff --git a/numpy/core/setup.py b/numpy/core/setup.py\nindex ad8d5cb..f71ec10 100644\n--- a/numpy/core/setup.py\n+++ b/numpy/core/setup.py\n@@ -215,10 +215,13 @@ def check_ieee_macros(config):\n     _macros = [\"isnan\", \"isinf\", \"signbit\", \"isfinite\"]\n     if sys.version_info[:2] >= (2, 6):\n         for f in _macros:\n-            already_declared = config.check_decl(fname2def(\"decl_%s\" % f),\n+            py_symbol = fname2def(\"decl_%s\" % f)\n+            already_declared = config.check_decl(py_symbol,\n                     headers=[\"Python.h\", \"math.h\"])\n             if already_declared:\n-                pub.append('NPY_%s' % fname2def(\"decl_%s\" % f))\n+                if config.check_macro_true(py_symbol,\n+                        headers=[\"Python.h\", \"math.h\"]):\n+                    pub.append('NPY_%s' % fname2def(\"decl_%s\" % f))\n             else:\n                 macros.append(f)\n     else:\n```\n\nand for example the line \"`already_declared = config.check_decl(fname2def(\"decl_%s\" % f),`\" is not present in the 1.5.0 version.\n\nMaybe you can modify it (and maybe easily) to apply to 1.5.0, but the diff, as written, does not.",
    "created_at": "2010-10-06T01:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96616",
    "user": "@jhpalmieri"
}
```

The patch affects two files.  One part of the patch is this:

```diff
diff --git a/numpy/core/setup.py b/numpy/core/setup.py
index ad8d5cb..f71ec10 100644
--- a/numpy/core/setup.py
+++ b/numpy/core/setup.py
@@ -215,10 +215,13 @@ def check_ieee_macros(config):
     _macros = ["isnan", "isinf", "signbit", "isfinite"]
     if sys.version_info[:2] >= (2, 6):
         for f in _macros:
-            already_declared = config.check_decl(fname2def("decl_%s" % f),
+            py_symbol = fname2def("decl_%s" % f)
+            already_declared = config.check_decl(py_symbol,
                     headers=["Python.h", "math.h"])
             if already_declared:
-                pub.append('NPY_%s' % fname2def("decl_%s" % f))
+                if config.check_macro_true(py_symbol,
+                        headers=["Python.h", "math.h"]):
+                    pub.append('NPY_%s' % fname2def("decl_%s" % f))
             else:
                 macros.append(f)
     else:
```

and for example the line "`already_declared = config.check_decl(fname2def("decl_%s" % f),`" is not present in the 1.5.0 version.

Maybe you can modify it (and maybe easily) to apply to 1.5.0, but the diff, as written, does not.



---

archive/issue_comments_096617.json:
```json
{
    "body": "Okay, I have a new version of the spkg, based on vanilla 1.5.0. I haven't tested it because I just lost my internet connection to fulvia.  See [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.spkg](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.spkg).  I'm also attaching the file displaying the differences between this spkg and the old 1.5.0 spkg posted here, except for two things: the new spkg includes modified copies of numpy/core/setup.py and numpy/distutils/command/config.py (in the patches directory -- the src directory is unmodified), and I didn't see any reason to include them in the posted patch file.  They are of course included in the repository, but to keep the patch file small, I edited them out before posting it.\n\nOh, the internet connection is back again.  I'm rebuilding on fulvia from scratch, which will take a while, but I just rebuilt the numpy package on mark2 successfully: \"import numpy\" works.",
    "created_at": "2010-10-06T02:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96617",
    "user": "@jhpalmieri"
}
```

Okay, I have a new version of the spkg, based on vanilla 1.5.0. I haven't tested it because I just lost my internet connection to fulvia.  See [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.spkg](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.spkg).  I'm also attaching the file displaying the differences between this spkg and the old 1.5.0 spkg posted here, except for two things: the new spkg includes modified copies of numpy/core/setup.py and numpy/distutils/command/config.py (in the patches directory -- the src directory is unmodified), and I didn't see any reason to include them in the posted patch file.  They are of course included in the repository, but to keep the patch file small, I edited them out before posting it.

Oh, the internet connection is back again.  I'm rebuilding on fulvia from scratch, which will take a while, but I just rebuilt the numpy package on mark2 successfully: "import numpy" works.



---

archive/issue_comments_096618.json:
```json
{
    "body": "Ah I'm only a few days away and everyones busy. Sometimes I think this ticket is cursed...\nHow high are the bets that this will work one day before 1.5.1 is released? =D\n\n`@`jhpalmiere, drkirkby, fbissey: Thanks for all the trouble!\n\nIf you want I build the package with the new patches and upload it on google code for testing. (Or do you want to upload it?)\nI will test it out on Ubuntu tonight for sure.\n\ngrettings,\nmaldun",
    "created_at": "2010-10-06T10:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96618",
    "user": "maldun"
}
```

Ah I'm only a few days away and everyones busy. Sometimes I think this ticket is cursed...
How high are the bets that this will work one day before 1.5.1 is released? =D

`@`jhpalmiere, drkirkby, fbissey: Thanks for all the trouble!

If you want I build the package with the new patches and upload it on google code for testing. (Or do you want to upload it?)
I will test it out on Ubuntu tonight for sure.

grettings,
maldun



---

archive/issue_comments_096619.json:
```json
{
    "body": "Ok I oversaw the link in the post...\nI changed the old link in the discription to your new one.\nThe new package is doing fine on ubuntu. \nreport for doctests will come soon!",
    "created_at": "2010-10-06T10:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96619",
    "user": "maldun"
}
```

Ok I oversaw the link in the post...
I changed the old link in the discription to your new one.
The new package is doing fine on ubuntu. 
report for doctests will come soon!



---

archive/issue_comments_096620.json:
```json
{
    "body": "Replying to [comment:196 maldun]:\n> Sometimes I think this ticket is cursed...\n> How high are the bets that this will work one day before 1.5.1 is released? =D\n\nWell the Numpy now works, but Scipy is presenting a problem on OpenSolaris due to the fact that the wrong compiler is being used. The variable `SAGE_FORTRAN` should specify the compiler:\n\n\n```\ndrkirkby@hawk:~$ echo $SAGE_FORTRAN\n/usr/local/gcc-4.5.0-delayed/bin/gfortran\n```\n\n\nused for all Fortran bits in Sage. But this version of Scipy has now decided to go off and use `/usr/bin/f90` which is the Sun Fortran compiler. \n\nI note that Francois has added this line:\n\n\n```\nexport FC=\"${SAGE_LOCAL}/bin/sage_fortran\"\n```\n\n\nbut it is not sufficient to get Scipy to use the right compiler. \n\n\n```\n f90: Internal Error, code=fw-interface-cexp-277, last src=scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f:673\nerror: Command \"/usr/bin/f90 -ftrap=%none -f77 -xcode=pic32 -Iscipy/sparse/linalg/eigen/arpack/ARPACK/SRC -I/export/home/drkirkby/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include -c -c scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f -o build/temp.solaris-2.11-i86pc-2.6/scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.o\" failed with exit status 1\nError building scipy.\n\nreal\t2m40.038s\nuser\t1m13.094s\nsys\t0m12.185s\nsage: An error occurred while installing scipy-0.8\n```\n\n\nI then set `F90`, but found Scipy was then using the Fortran 77 compiler `/usr/bin/f77`. So I had to set `F77` too. I decided to set `F95` just in case, there is, or the developers add some Fortran 95 code. So with all these set:\n\n\n```\nexport FC=\"$SAGE_LOCAL/bin/sage_fortran\"\nexport F77=\"$SAGE_LOCAL/bin/sage_fortran\"\nexport F90=\"$SAGE_LOCAL/bin/sage_fortran\"\nexport F95=\"$SAGE_LOCAL/bin/sage_fortran\"\n```\n\n\nScipy does build on OpenSolaris OK. \n\nBut I looked at the SPKG.txt and found there are many things missing, which should be there. I will try to improve that and post a Scipy package. \n\nDave",
    "created_at": "2010-10-06T14:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96620",
    "user": "drkirkby"
}
```

Replying to [comment:196 maldun]:
> Sometimes I think this ticket is cursed...
> How high are the bets that this will work one day before 1.5.1 is released? =D

Well the Numpy now works, but Scipy is presenting a problem on OpenSolaris due to the fact that the wrong compiler is being used. The variable `SAGE_FORTRAN` should specify the compiler:


```
drkirkby@hawk:~$ echo $SAGE_FORTRAN
/usr/local/gcc-4.5.0-delayed/bin/gfortran
```


used for all Fortran bits in Sage. But this version of Scipy has now decided to go off and use `/usr/bin/f90` which is the Sun Fortran compiler. 

I note that Francois has added this line:


```
export FC="${SAGE_LOCAL}/bin/sage_fortran"
```


but it is not sufficient to get Scipy to use the right compiler. 


```
 f90: Internal Error, code=fw-interface-cexp-277, last src=scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f:673
error: Command "/usr/bin/f90 -ftrap=%none -f77 -xcode=pic32 -Iscipy/sparse/linalg/eigen/arpack/ARPACK/SRC -I/export/home/drkirkby/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include -c -c scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f -o build/temp.solaris-2.11-i86pc-2.6/scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.o" failed with exit status 1
Error building scipy.

real	2m40.038s
user	1m13.094s
sys	0m12.185s
sage: An error occurred while installing scipy-0.8
```


I then set `F90`, but found Scipy was then using the Fortran 77 compiler `/usr/bin/f77`. So I had to set `F77` too. I decided to set `F95` just in case, there is, or the developers add some Fortran 95 code. So with all these set:


```
export FC="$SAGE_LOCAL/bin/sage_fortran"
export F77="$SAGE_LOCAL/bin/sage_fortran"
export F90="$SAGE_LOCAL/bin/sage_fortran"
export F95="$SAGE_LOCAL/bin/sage_fortran"
```


Scipy does build on OpenSolaris OK. 

But I looked at the SPKG.txt and found there are many things missing, which should be there. I will try to improve that and post a Scipy package. 

Dave



---

archive/issue_comments_096621.json:
```json
{
    "body": "Attachment [9808-Fortran-issues-in-SciPy.patch](tarball://root/attachments/some-uuid/ticket9808/9808-Fortran-issues-in-SciPy.patch) by drkirkby created at 2010-10-06 14:43:53\n\nSets F77, F90 and F95 so SciPy really does use the Fortran compiler we want. Setting FC alone is insufficient.",
    "created_at": "2010-10-06T14:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96621",
    "user": "drkirkby"
}
```

Attachment [9808-Fortran-issues-in-SciPy.patch](tarball://root/attachments/some-uuid/ticket9808/9808-Fortran-issues-in-SciPy.patch) by drkirkby created at 2010-10-06 14:43:53

Sets F77, F90 and F95 so SciPy really does use the Fortran compiler we want. Setting FC alone is insufficient.



---

archive/issue_comments_096622.json:
```json
{
    "body": "Can I still test this by upgrading the packages, doing `./sage -ba`, and adding the doctest patch?  By the way, with the Pynac upgrade now in 4.6.alpha3 (see #9901), it's conceivable that the functions/hyperbolic.py piece of that will have to be rebased.",
    "created_at": "2010-10-06T14:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96622",
    "user": "@kcrisman"
}
```

Can I still test this by upgrading the packages, doing `./sage -ba`, and adding the doctest patch?  By the way, with the Pynac upgrade now in 4.6.alpha3 (see #9901), it's conceivable that the functions/hyperbolic.py piece of that will have to be rebased.



---

archive/issue_comments_096623.json:
```json
{
    "body": "Replying to [comment:200 kcrisman]:\n> Can I still test this by upgrading the packages, doing `./sage -ba`, and adding the doctest patch?  By the way, with the Pynac upgrade now in 4.6.alpha3 (see #9901), it's conceivable that the functions/hyperbolic.py piece of that will have to be rebased.\n\nI don't know enough about what needs to be done to test this. I've not even applied the patch myself yet. But the packages are at least building now, which is a start! \n\nI really need to be doing other things today, so are going to leave this ticket for the rest of the day - at least I will not be adding any code. \n\nDave",
    "created_at": "2010-10-06T14:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96623",
    "user": "drkirkby"
}
```

Replying to [comment:200 kcrisman]:
> Can I still test this by upgrading the packages, doing `./sage -ba`, and adding the doctest patch?  By the way, with the Pynac upgrade now in 4.6.alpha3 (see #9901), it's conceivable that the functions/hyperbolic.py piece of that will have to be rebased.

I don't know enough about what needs to be done to test this. I've not even applied the patch myself yet. But the packages are at least building now, which is a start! 

I really need to be doing other things today, so are going to leave this ticket for the rest of the day - at least I will not be adding any code. 

Dave



---

archive/issue_comments_096624.json:
```json
{
    "body": "I've not applied the patches, so have not checked this fully, so I am not marking for review. But the two packages do now both build on OpenSolaris 06/2009 and I assume will do on Solaris 10 both SPARC and x86. **However, I have not tested these on Solaris, or any other system** \n\nI also added a lot of information which was missing from SPKG.txt\n\nThe new SciPy package is here. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/scipy-0.8.spkg\n\nI don't have time to sort out how to apply the patches, fully build and doctest this. Sorry. \n\nDave",
    "created_at": "2010-10-06T15:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96624",
    "user": "drkirkby"
}
```

I've not applied the patches, so have not checked this fully, so I am not marking for review. But the two packages do now both build on OpenSolaris 06/2009 and I assume will do on Solaris 10 both SPARC and x86. **However, I have not tested these on Solaris, or any other system** 

I also added a lot of information which was missing from SPKG.txt

The new SciPy package is here. 

http://boxen.math.washington.edu/home/kirkby/patches/scipy-0.8.spkg

I don't have time to sort out how to apply the patches, fully build and doctest this. Sorry. 

Dave



---

archive/issue_comments_096625.json:
```json
{
    "body": "Replying to [comment:202 drkirkby]:\n> I've not applied the patches, so have not checked this fully, so I am not marking for review. But the two packages do now both build on OpenSolaris 06/2009 and I assume will do on Solaris 10 both SPARC and x86. **However, I have not tested these on Solaris, or any other system** \n> \n> I also added a lot of information which was missing from SPKG.txt\n> \n> The new SciPy package is here. \n> \n> http://boxen.math.washington.edu/home/kirkby/patches/scipy-0.8.spkg\n> \n> I don't have time to sort out how to apply the patches, fully build and doctest this. Sorry. \n> \n> Dave \n\nThanks for doing this!\nI already applied your package on my machine, it builded fine!\nI hope I find some time to make the tests soon.",
    "created_at": "2010-10-06T17:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96625",
    "user": "maldun"
}
```

Replying to [comment:202 drkirkby]:
> I've not applied the patches, so have not checked this fully, so I am not marking for review. But the two packages do now both build on OpenSolaris 06/2009 and I assume will do on Solaris 10 both SPARC and x86. **However, I have not tested these on Solaris, or any other system** 
> 
> I also added a lot of information which was missing from SPKG.txt
> 
> The new SciPy package is here. 
> 
> http://boxen.math.washington.edu/home/kirkby/patches/scipy-0.8.spkg
> 
> I don't have time to sort out how to apply the patches, fully build and doctest this. Sorry. 
> 
> Dave 

Thanks for doing this!
I already applied your package on my machine, it builded fine!
I hope I find some time to make the tests soon.



---

archive/issue_comments_096626.json:
```json
{
    "body": "Replying to [comment:200 kcrisman]:\n> Can I still test this by upgrading the packages, doing `./sage -ba`, and adding the doctest patch?  By the way, with the Pynac upgrade now in 4.6.alpha3 (see #9901), it's conceivable that the functions/hyperbolic.py piece of that will have to be rebased.\n\nNormally it should do. If you want save some time, write something in the numpy.pxd delete it again and save the file, so that the timestamp gets refreshed. After that sage -b should also do the trick.",
    "created_at": "2010-10-06T17:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96626",
    "user": "maldun"
}
```

Replying to [comment:200 kcrisman]:
> Can I still test this by upgrading the packages, doing `./sage -ba`, and adding the doctest patch?  By the way, with the Pynac upgrade now in 4.6.alpha3 (see #9901), it's conceivable that the functions/hyperbolic.py piece of that will have to be rebased.

Normally it should do. If you want save some time, write something in the numpy.pxd delete it again and save the file, so that the timestamp gets refreshed. After that sage -b should also do the trick.



---

archive/issue_comments_096627.json:
```json
{
    "body": "`@`changed doctests: Since this ticket won't be ready before the deadline, I wait till the release comes out and change it then.",
    "created_at": "2010-10-06T17:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96627",
    "user": "maldun"
}
```

`@`changed doctests: Since this ticket won't be ready before the deadline, I wait till the release comes out and change it then.



---

archive/issue_comments_096628.json:
```json
{
    "body": "I've built and tested this, and get the following test failures on my OpenSolaris machine:\n\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t  -long devel/sage/doc/en/bordeaux_2008/introduction.rst # 1 doctests failed\n\tsage -t  -long devel/sage/sage/numerical/test.py # 3 doctests failed\n\tsage -t  -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed\n\tsage -t  -long devel/sage/sage/tensor/differential_forms.py # 1 doctests failed\n\tsage -t  -long devel/sage/sage/plot/plot3d/list_plot3d.py # 8 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1815.6 seconds\n```\n\n\nPrior to upgrading Numpy and !Scipy, I had only two failures, which were:\n\n`devel/sage/sage/rings/polynomial/polynomial_element.pyx` #10042\n\nand \n\n`devel/sage/sage/tensor/differential_forms.py` #10041\n\nSo that is three new failures after the upgrade of these two packages. \n\n```\n\tsage -t  -long devel/sage/doc/en/bordeaux_2008/introduction.rst # 1 doctests failed\n\tsage -t  -long devel/sage/sage/numerical/test.py # 3 doctests failed\n\tsage -t  -long devel/sage/sage/plot/plot3d/list_plot3d.py # 8 doctests failed\n```\n\n\nI've attached a log showing just the failed tests. At least some of the problems are related to:\n\n* `ImportError: No module named delaunay`\n* `ImportError: No module named arpack`\n\nDave",
    "created_at": "2010-10-06T17:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96628",
    "user": "drkirkby"
}
```

I've built and tested this, and get the following test failures on my OpenSolaris machine:


```
----------------------------------------------------------------------

The following tests failed:

	sage -t  -long devel/sage/doc/en/bordeaux_2008/introduction.rst # 1 doctests failed
	sage -t  -long devel/sage/sage/numerical/test.py # 3 doctests failed
	sage -t  -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed
	sage -t  -long devel/sage/sage/tensor/differential_forms.py # 1 doctests failed
	sage -t  -long devel/sage/sage/plot/plot3d/list_plot3d.py # 8 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1815.6 seconds
```


Prior to upgrading Numpy and !Scipy, I had only two failures, which were:

`devel/sage/sage/rings/polynomial/polynomial_element.pyx` #10042

and 

`devel/sage/sage/tensor/differential_forms.py` #10041

So that is three new failures after the upgrade of these two packages. 

```
	sage -t  -long devel/sage/doc/en/bordeaux_2008/introduction.rst # 1 doctests failed
	sage -t  -long devel/sage/sage/numerical/test.py # 3 doctests failed
	sage -t  -long devel/sage/sage/plot/plot3d/list_plot3d.py # 8 doctests failed
```


I've attached a log showing just the failed tests. At least some of the problems are related to:

* `ImportError: No module named delaunay`
* `ImportError: No module named arpack`

Dave



---

archive/issue_comments_096629.json:
```json
{
    "body": "Attachment [probable-Numpy-SciPy-issues-on-OpenSolaris.txt](tarball://root/attachments/some-uuid/ticket9808/probable-Numpy-SciPy-issues-on-OpenSolaris.txt) by drkirkby created at 2010-10-06 17:45:43\n\nThe three new doctest failures which are almost certainly a result of upgrading Numpy and Scipy",
    "created_at": "2010-10-06T17:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96629",
    "user": "drkirkby"
}
```

Attachment [probable-Numpy-SciPy-issues-on-OpenSolaris.txt](tarball://root/attachments/some-uuid/ticket9808/probable-Numpy-SciPy-issues-on-OpenSolaris.txt) by drkirkby created at 2010-10-06 17:45:43

The three new doctest failures which are almost certainly a result of upgrading Numpy and Scipy



---

archive/issue_comments_096630.json:
```json
{
    "body": "In a build from scratch on fulvia (with the previous version of the scipy package), I see these failures:\n\n```\nThe following tests failed:\n\n        sage -t  -long devel/sage/sage/tensor/differential_forms.py # 1 doctests failed\n        sage -t  -long devel/sage/sage/misc/citation.pyx # 2 doctests failed\n        sage -t  -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed\n```\n\nThe first of these is covered by #10041.  The second of these I mentioned before:\n\n```\nsage -t  -long devel/sage/sage/misc/citation.pyx\n**********************************************************************\nFile \"/home/palmieri/fulvia/numpy/sage-4.6.alpha2/devel/sage-main/sage/misc/citation.pyx\", line 60:\n    sage: get_systems('integrate(x^2, x)')\nExpected:\n    ['ginac', 'Maxima']\nGot:\n    ['numpy', 'ginac', 'Maxima']\n**********************************************************************\nFile \"/home/palmieri/fulvia/numpy/sage-4.6.alpha2/devel/sage-main/sage/misc/citation.pyx\", line 64:\n    sage: get_systems('I.primary_decomposition()')\nExpected:\n    ['Singular']\nGot:\n    ['Singular', 'numpy']\n**********************************************************************\n1 items had failures:\n   2 of   8 in __main__.example_0\n***Test Failed*** 2 failures.\n```\n\nThe third of these is mostly covered by #10042, except for the first line, which somewhat concerns me:\n\n```\nsage -t  -long devel/sage/sage/rings/polynomial/polynomial_element.pyx\nWarning: invalid value encountered in isfinite\n**********************************************************************\nFile \"/home/palmieri/fulvia/numpy/sage-4.6.alpha2/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\", line 4316:\n    sage: f.roots(algorithm='numpy')\n```\n\nDave, do you see this?",
    "created_at": "2010-10-06T20:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96630",
    "user": "@jhpalmieri"
}
```

In a build from scratch on fulvia (with the previous version of the scipy package), I see these failures:

```
The following tests failed:

        sage -t  -long devel/sage/sage/tensor/differential_forms.py # 1 doctests failed
        sage -t  -long devel/sage/sage/misc/citation.pyx # 2 doctests failed
        sage -t  -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed
```

The first of these is covered by #10041.  The second of these I mentioned before:

```
sage -t  -long devel/sage/sage/misc/citation.pyx
**********************************************************************
File "/home/palmieri/fulvia/numpy/sage-4.6.alpha2/devel/sage-main/sage/misc/citation.pyx", line 60:
    sage: get_systems('integrate(x^2, x)')
Expected:
    ['ginac', 'Maxima']
Got:
    ['numpy', 'ginac', 'Maxima']
**********************************************************************
File "/home/palmieri/fulvia/numpy/sage-4.6.alpha2/devel/sage-main/sage/misc/citation.pyx", line 64:
    sage: get_systems('I.primary_decomposition()')
Expected:
    ['Singular']
Got:
    ['Singular', 'numpy']
**********************************************************************
1 items had failures:
   2 of   8 in __main__.example_0
***Test Failed*** 2 failures.
```

The third of these is mostly covered by #10042, except for the first line, which somewhat concerns me:

```
sage -t  -long devel/sage/sage/rings/polynomial/polynomial_element.pyx
Warning: invalid value encountered in isfinite
**********************************************************************
File "/home/palmieri/fulvia/numpy/sage-4.6.alpha2/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 4316:
    sage: f.roots(algorithm='numpy')
```

Dave, do you see this?



---

archive/issue_comments_096631.json:
```json
{
    "body": "> Normally it should do. If you want save some time, write something in the numpy.pxd delete it again and save the file, so that the timestamp gets refreshed. After that sage -b should also do the trick.\nI think that just the command\n\n```\ntouch .../numpy.pxd\n```\n\nshould work, as leif pointed out.  Maybe this isn't a universal command?  Anyway, it did the trick on my computer - MUCH less time to build ~12 files than all the Cython files!  It's still doing this, so I won't have a chance to test yet, but I hope I won't get the failures drkirkby gets.",
    "created_at": "2010-10-06T20:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96631",
    "user": "@kcrisman"
}
```

> Normally it should do. If you want save some time, write something in the numpy.pxd delete it again and save the file, so that the timestamp gets refreshed. After that sage -b should also do the trick.
I think that just the command

```
touch .../numpy.pxd
```

should work, as leif pointed out.  Maybe this isn't a universal command?  Anyway, it did the trick on my computer - MUCH less time to build ~12 files than all the Cython files!  It's still doing this, so I won't have a chance to test yet, but I hope I won't get the failures drkirkby gets.



---

archive/issue_comments_096632.json:
```json
{
    "body": "Replying to [comment:207 jhpalmieri]:\n> In a build from scratch on fulvia (with the previous version of the scipy package), I see these failures:\n\n<snip>\n\n> Dave, do you see this?\n\nIIRC, the old Scipy would not build at all once Numpy had been upgraded. \n\nI originally thought it was a bit silly to create a ticket which upgraded two packages, but then I came to the conclusion one could not be done without the other. Perhaps I was mistaken. \n\nSo the short answer is no I do not see what you got, but I was unable to build the old SciPy. \n\nI will start another fresh build. I'll report in an hour or so. \n\nDave",
    "created_at": "2010-10-06T20:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96632",
    "user": "drkirkby"
}
```

Replying to [comment:207 jhpalmieri]:
> In a build from scratch on fulvia (with the previous version of the scipy package), I see these failures:

<snip>

> Dave, do you see this?

IIRC, the old Scipy would not build at all once Numpy had been upgraded. 

I originally thought it was a bit silly to create a ticket which upgraded two packages, but then I came to the conclusion one could not be done without the other. Perhaps I was mistaken. 

So the short answer is no I do not see what you got, but I was unable to build the old SciPy. 

I will start another fresh build. I'll report in an hour or so. 

Dave



---

archive/issue_comments_096633.json:
```json
{
    "body": "Not, since the patch to resolve the `isfinite` problem on http://projects.scipy.org/numpy/ticket/1625 worked, I commented on that fact on the ticket. That patch has now been committed to the Numpy source code, so will be in the next release, which is expected to be 1.5.1 but may be 2.0.0. \n\nSo we have that one solved! \n\nDave",
    "created_at": "2010-10-06T20:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96633",
    "user": "drkirkby"
}
```

Not, since the patch to resolve the `isfinite` problem on http://projects.scipy.org/numpy/ticket/1625 worked, I commented on that fact on the ticket. That patch has now been committed to the Numpy source code, so will be in the next release, which is expected to be 1.5.1 but may be 2.0.0. 

So we have that one solved! 

Dave



---

archive/issue_comments_096634.json:
```json
{
    "body": "Replying to [comment:209 drkirkby]:\n> Dave, do you see this?\n> \n> IIRC, the old Scipy would not build at all once Numpy had been upgraded. \n> \n> I originally thought it was a bit silly to create a ticket which upgraded two packages, but then I came to the conclusion one could not be done without the other. Perhaps I was mistaken. \n> \n> So the short answer is no I do not see what you got, but I was unable to build the old SciPy. \n> \n> I will start another fresh build. I'll report in an hour or so. \n> \n> Dave \n\nWell, I started another build, and whilst the new Numpy built, the old Scipy failed:\n\n\n```\n f90: Internal Error, code=fw-interface-cexp-277, last src=scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f:673\nf90: Warning: The option -xcode=pic32 has no effect on x86\nscipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f:\n\tzneupd:\n f90: Internal Error, code=fw-interface-cexp-277, last src=scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f:673\nerror: Command \"/usr/bin/f90 -ftrap=%none -f77 -xcode=pic32 -Iscipy/sparse/linalg/eigen/arpack/ARPACK/SRC -I/export/home/drkirkby/half/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include -c -c scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f -o build/temp.solaris-2.11-i86pc-2.6/scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.o\" failed with exit status 1\nError building scipy.\n\nreal\t1m52.484s\nuser\t1m6.919s\nsys\t0m8.931s\nsage: An error occurred while installing scipy-0.7.p5\n```\n\n\nNote this is picking up the Sun compilers, not the gcc one. \n\nThat was the problem I had with the new Scipy, but never the old one. Perhaps something in the new Numpy has changed so that the old Scipy is finding the wrong compiler. I've no idea!\n\nMaybe the Sun compilers are not in your path on fulvia. \n\nDave",
    "created_at": "2010-10-06T20:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96634",
    "user": "drkirkby"
}
```

Replying to [comment:209 drkirkby]:
> Dave, do you see this?
> 
> IIRC, the old Scipy would not build at all once Numpy had been upgraded. 
> 
> I originally thought it was a bit silly to create a ticket which upgraded two packages, but then I came to the conclusion one could not be done without the other. Perhaps I was mistaken. 
> 
> So the short answer is no I do not see what you got, but I was unable to build the old SciPy. 
> 
> I will start another fresh build. I'll report in an hour or so. 
> 
> Dave 

Well, I started another build, and whilst the new Numpy built, the old Scipy failed:


```
 f90: Internal Error, code=fw-interface-cexp-277, last src=scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f:673
f90: Warning: The option -xcode=pic32 has no effect on x86
scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f:
	zneupd:
 f90: Internal Error, code=fw-interface-cexp-277, last src=scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f:673
error: Command "/usr/bin/f90 -ftrap=%none -f77 -xcode=pic32 -Iscipy/sparse/linalg/eigen/arpack/ARPACK/SRC -I/export/home/drkirkby/half/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include -c -c scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.f -o build/temp.solaris-2.11-i86pc-2.6/scipy/sparse/linalg/eigen/arpack/ARPACK/SRC/zneupd.o" failed with exit status 1
Error building scipy.

real	1m52.484s
user	1m6.919s
sys	0m8.931s
sage: An error occurred while installing scipy-0.7.p5
```


Note this is picking up the Sun compilers, not the gcc one. 

That was the problem I had with the new Scipy, but never the old one. Perhaps something in the new Numpy has changed so that the old Scipy is finding the wrong compiler. I've no idea!

Maybe the Sun compilers are not in your path on fulvia. 

Dave



---

archive/issue_comments_096635.json:
```json
{
    "body": "I just started a fresh build with the new Numpy and the new SciPy. I assume once it builds, I need to apply the patch, rebuild the library and doctest again. I've done this once today, but I'll try again just to make sure I did not make an error. \n\ndave",
    "created_at": "2010-10-06T20:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96635",
    "user": "drkirkby"
}
```

I just started a fresh build with the new Numpy and the new SciPy. I assume once it builds, I need to apply the patch, rebuild the library and doctest again. I've done this once today, but I'll try again just to make sure I did not make an error. 

dave



---

archive/issue_comments_096636.json:
```json
{
    "body": "I don't know what's happening with me today. Things which did work no longer do!\n\nI'm getting a failure of `scipy_sandbox-20071020.p5` to build now. It has the same issue SciPy had - using the wrong compiler. \n\nI'm wondering if Numpy should in some way indicate the compiler so programs which depend on Numpy (SciPy and I assume scipy_sandbox), use the same compiler? \n\nThis is what I just see:\n\n\n```\n f90: Internal Error, code=fw-interface-cexp-277, last src=./ARPACK/SRC/zneupd.f:673\nerror: Command \"/usr/bin/f90 -ftrap=%none -f77 -xcode=pic32 -I./ARPACK/SRC -I/export/home/drkirkby/new/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include -c -c ./ARPACK/SRC/zneupd.f -o build/temp.solaris-2.11-i86pc-2.6/ARPACK/SRC/zneupd.o\" failed with exit status 1\nError building arpack \n\n\nreal\t0m11.229s\nuser\t0m4.239s\nsys\t0m1.659s\nsage: An error occurred while installing scipy_sandbox-20071020.p5\n```\n\n\nI could easily patch scipy_sandbox-20071020.p5 so it uses the right compiler, but I'm wondering if Numpy should tell it the compiler to use, and this version is failing to do that. \n\n\n**Has anyone changed anything connected with the Fortran compiler in Numpy?** \n\nDave",
    "created_at": "2010-10-06T21:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96636",
    "user": "drkirkby"
}
```

I don't know what's happening with me today. Things which did work no longer do!

I'm getting a failure of `scipy_sandbox-20071020.p5` to build now. It has the same issue SciPy had - using the wrong compiler. 

I'm wondering if Numpy should in some way indicate the compiler so programs which depend on Numpy (SciPy and I assume scipy_sandbox), use the same compiler? 

This is what I just see:


```
 f90: Internal Error, code=fw-interface-cexp-277, last src=./ARPACK/SRC/zneupd.f:673
error: Command "/usr/bin/f90 -ftrap=%none -f77 -xcode=pic32 -I./ARPACK/SRC -I/export/home/drkirkby/new/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include -c -c ./ARPACK/SRC/zneupd.f -o build/temp.solaris-2.11-i86pc-2.6/ARPACK/SRC/zneupd.o" failed with exit status 1
Error building arpack 


real	0m11.229s
user	0m4.239s
sys	0m1.659s
sage: An error occurred while installing scipy_sandbox-20071020.p5
```


I could easily patch scipy_sandbox-20071020.p5 so it uses the right compiler, but I'm wondering if Numpy should tell it the compiler to use, and this version is failing to do that. 


**Has anyone changed anything connected with the Fortran compiler in Numpy?** 

Dave



---

archive/issue_comments_096637.json:
```json
{
    "body": "Replying to [comment:213 drkirkby]:\n\n> **Has anyone changed anything connected with the Fortran compiler in Numpy?** \n> \n> Dave \n\nI've just checked, and see someone (I think Francois) made some changes to how Fortran is handled in Numpy. He has exported FC, but not F77, F90 or F95. I think that's having a knock-on effect on anything that depends on Numpy, such as !Scipy and scipy-sandbox. \n\nI'll change the Numpy package so it exports FC, F77, F90 & F95. I suspect that will fix the problem. \n\nThe doctest failures I got before, can easily be explained by this Fortran mix-up. \n\nDave",
    "created_at": "2010-10-06T21:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96637",
    "user": "drkirkby"
}
```

Replying to [comment:213 drkirkby]:

> **Has anyone changed anything connected with the Fortran compiler in Numpy?** 
> 
> Dave 

I've just checked, and see someone (I think Francois) made some changes to how Fortran is handled in Numpy. He has exported FC, but not F77, F90 or F95. I think that's having a knock-on effect on anything that depends on Numpy, such as !Scipy and scipy-sandbox. 

I'll change the Numpy package so it exports FC, F77, F90 & F95. I suspect that will fix the problem. 

The doctest failures I got before, can easily be explained by this Fortran mix-up. 

Dave



---

archive/issue_comments_096638.json:
```json
{
    "body": "Replying to [comment:212 drkirkby]:\n> I just started a fresh build with the new Numpy and the new SciPy. I assume once it builds, I need to apply the patch, rebuild the library and doctest again.\n\nInstead, before building, you can cd into spkg/standard, type \"tar jxf sage-4.6.alpha2.spkg\", cd into the newly created directory \"sage-4.6.alpha2\", and apply the patches (\"hg import ...\").  Then cd back to spkg/standard and type \"sage -pkg sage-4.6.alpha2\" to recreate the spkg file for the Sage library, but with the patches included.  Then you can \"make ptestlong\".\n\nBy the way, I just noticed these lines in the new scipy spkg-install file:\n\n```\nif [ `uname` = \"Darwin\" ]; then\n    unset ATLAS\n    unset BLAS\n    unset LAPACK\n    export FC=\"sage_fortran\"\nelse\n    export LDFLAGS=\"${LDFLAGS} -shared\"\nfi\nexport FC=\"${SAGE_LOCAL}/bin/sage_fortran\"\n```\n\nIt seems to me that the last line will override the similar line in the \"if\" block.  Could you fix that, too?",
    "created_at": "2010-10-06T21:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96638",
    "user": "@jhpalmieri"
}
```

Replying to [comment:212 drkirkby]:
> I just started a fresh build with the new Numpy and the new SciPy. I assume once it builds, I need to apply the patch, rebuild the library and doctest again.

Instead, before building, you can cd into spkg/standard, type "tar jxf sage-4.6.alpha2.spkg", cd into the newly created directory "sage-4.6.alpha2", and apply the patches ("hg import ...").  Then cd back to spkg/standard and type "sage -pkg sage-4.6.alpha2" to recreate the spkg file for the Sage library, but with the patches included.  Then you can "make ptestlong".

By the way, I just noticed these lines in the new scipy spkg-install file:

```
if [ `uname` = "Darwin" ]; then
    unset ATLAS
    unset BLAS
    unset LAPACK
    export FC="sage_fortran"
else
    export LDFLAGS="${LDFLAGS} -shared"
fi
export FC="${SAGE_LOCAL}/bin/sage_fortran"
```

It seems to me that the last line will override the similar line in the "if" block.  Could you fix that, too?



---

archive/issue_comments_096639.json:
```json
{
    "body": "> By the way, I just noticed these lines in the new scipy spkg-install file:\n\nSorry, I meant the **numpy** spkg-install file.",
    "created_at": "2010-10-06T21:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96639",
    "user": "@jhpalmieri"
}
```

> By the way, I just noticed these lines in the new scipy spkg-install file:

Sorry, I meant the **numpy** spkg-install file.



---

archive/issue_comments_096640.json:
```json
{
    "body": "Dave: Is this the sort of change you had in mind?\n\n```diff\n\ndiff -r 1c2a7c8515fc spkg-install\n--- a/spkg-install\tTue Oct 05 22:35:34 2010 -0400\n+++ b/spkg-install\tWed Oct 06 15:07:58 2010 -0700\n@@ -37,11 +37,13 @@\n     unset ATLAS\n     unset BLAS\n     unset LAPACK\n-    export FC=\"sage_fortran\"\n else\n     export LDFLAGS=\"${LDFLAGS} -shared\"\n fi\n export FC=\"${SAGE_LOCAL}/bin/sage_fortran\"\n+export F77=\"${SAGE_LOCAL}/bin/sage_fortran\"\n+export F90=\"${SAGE_LOCAL}/bin/sage_fortran\"\n+export F95=\"${SAGE_LOCAL}/bin/sage_fortran\"\n export NUMPY_FCONFIG=\"config_fc --noopt --noarch\"\n \n ################################################\n```\n\nI've prepared a new spkg in [http://sage.math.washington.edu/home/palmieri/SPKG/numpy-1.5.0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/numpy-1.5.0.spkg).  (This is not the same place as the previous one.  I'm updating the ticket description with this new version.)",
    "created_at": "2010-10-06T22:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96640",
    "user": "@jhpalmieri"
}
```

Dave: Is this the sort of change you had in mind?

```diff

diff -r 1c2a7c8515fc spkg-install
--- a/spkg-install	Tue Oct 05 22:35:34 2010 -0400
+++ b/spkg-install	Wed Oct 06 15:07:58 2010 -0700
@@ -37,11 +37,13 @@
     unset ATLAS
     unset BLAS
     unset LAPACK
-    export FC="sage_fortran"
 else
     export LDFLAGS="${LDFLAGS} -shared"
 fi
 export FC="${SAGE_LOCAL}/bin/sage_fortran"
+export F77="${SAGE_LOCAL}/bin/sage_fortran"
+export F90="${SAGE_LOCAL}/bin/sage_fortran"
+export F95="${SAGE_LOCAL}/bin/sage_fortran"
 export NUMPY_FCONFIG="config_fc --noopt --noarch"
 
 ################################################
```

I've prepared a new spkg in [http://sage.math.washington.edu/home/palmieri/SPKG/numpy-1.5.0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/numpy-1.5.0.spkg).  (This is not the same place as the previous one.  I'm updating the ticket description with this new version.)



---

archive/issue_comments_096641.json:
```json
{
    "body": "Attachment [trac_9808-numpy.patch](tarball://root/attachments/some-uuid/ticket9808/trac_9808-numpy.patch) by @jhpalmieri created at 2010-10-06 22:19:59\n\nfor reference only: diff between old numpy 1.5.0 spkg and new one",
    "created_at": "2010-10-06T22:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96641",
    "user": "@jhpalmieri"
}
```

Attachment [trac_9808-numpy.patch](tarball://root/attachments/some-uuid/ticket9808/trac_9808-numpy.patch) by @jhpalmieri created at 2010-10-06 22:19:59

for reference only: diff between old numpy 1.5.0 spkg and new one



---

archive/issue_comments_096642.json:
```json
{
    "body": "Replying to [comment:217 jhpalmieri]:\n> Dave: Is this the sort of change you had in mind?\n\nYes. I personally only ever use () and not {} in scripts, but I assume the latter is ok. \n\nThat **probably** means that SciPy and scipy_sandbox do not need similar - I suspect they pick these up from Numpy. But we will see. It might be necessary to add  it to scipy_sandbox too. \n\nDave",
    "created_at": "2010-10-06T22:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96642",
    "user": "drkirkby"
}
```

Replying to [comment:217 jhpalmieri]:
> Dave: Is this the sort of change you had in mind?

Yes. I personally only ever use () and not {} in scripts, but I assume the latter is ok. 

That **probably** means that SciPy and scipy_sandbox do not need similar - I suspect they pick these up from Numpy. But we will see. It might be necessary to add  it to scipy_sandbox too. 

Dave



---

archive/issue_comments_096643.json:
```json
{
    "body": "Back from snooze-land via morning teaching.\n\nI would have expected that the fortran settings in scipy and numpy would have to match. I am completely astonished that you had problems with scipy and not numpy. In fact on Gentoo we currently have a bug open because numpy picks up the intel fortran compiler when it shouldn't.\n\nOther than that I haven't tested the new spkg on linux ppc, but I don't think anything that has been touched that would affect compilation . Most of the test suite passed, a lot of time out on this hardware but since we are not in a hurry anymore I will do a run of the long test suite once I have checked the latest spkg.\n\nI am not seeing the failure on citation.pyx or polynomial_element.pyx on that hardware, I just checked specifically.\n\nFrancois",
    "created_at": "2010-10-06T22:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96643",
    "user": "@kiwifb"
}
```

Back from snooze-land via morning teaching.

I would have expected that the fortran settings in scipy and numpy would have to match. I am completely astonished that you had problems with scipy and not numpy. In fact on Gentoo we currently have a bug open because numpy picks up the intel fortran compiler when it shouldn't.

Other than that I haven't tested the new spkg on linux ppc, but I don't think anything that has been touched that would affect compilation . Most of the test suite passed, a lot of time out on this hardware but since we are not in a hurry anymore I will do a run of the long test suite once I have checked the latest spkg.

I am not seeing the failure on citation.pyx or polynomial_element.pyx on that hardware, I just checked specifically.

Francois



---

archive/issue_comments_096644.json:
```json
{
    "body": "I hit the same issue with `scipy_sandbox`. I've put that on another ticket, with a patch that needs review. \n\nDave",
    "created_at": "2010-10-06T23:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96644",
    "user": "drkirkby"
}
```

I hit the same issue with `scipy_sandbox`. I've put that on another ticket, with a patch that needs review. 

Dave



---

archive/issue_comments_096645.json:
```json
{
    "body": "Oops, I forgot to say, the other ticket is #10092. Perhaps someone can review that - it should be very easy. \n\ndave",
    "created_at": "2010-10-06T23:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96645",
    "user": "drkirkby"
}
```

Oops, I forgot to say, the other ticket is #10092. Perhaps someone can review that - it should be very easy. 

dave



---

archive/issue_comments_096646.json:
```json
{
    "body": "I'm having problems with scipy on Mac OS X (Intel, 10.6):\n\n```\ncompiling Fortran sources\nFortran f77 compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -ffixed-form -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops\nFortran f90 compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops\nFortran fix compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -ffixed-form -fno-second-underscore -Wall -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops\ncreating build/temp.macosx-10.6-i386-2.6\ncreating build/temp.macosx-10.6-i386-2.6/scipy\ncreating build/temp.macosx-10.6-i386-2.6/scipy/fftpack\ncreating build/temp.macosx-10.6-i386-2.6/scipy/fftpack/src\ncreating build/temp.macosx-10.6-i386-2.6/scipy/fftpack/src/dfftpack\ncompile options: '-I/Applications/sage_builds/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include -c'\nsage_fortran:f77: scipy/fftpack/src/dfftpack/dcosqb.f\nlipo: /var/folders/ks/ksTkDzjXF7KfYo6uWLAQHk+++TM/-Tmp-//ccMIVvsm.out and /var/folders/ks/ksTkDzjXF7KfYo6uWLAQHk+++TM/-Tmp-//ccmhVCg6.out have the same architectures (ppc64) and can't be in the same fat output file\nlipo: /var/folders/ks/ksTkDzjXF7KfYo6uWLAQHk+++TM/-Tmp-//ccMIVvsm.out and /var/folders/ks/ksTkDzjXF7KfYo6uWLAQHk+++TM/-Tmp-//ccmhVCg6.out have the same architectures (ppc64) and can't be in the same fat output file\nerror: Command \"/Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -ffixed-form -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops -I/Applications/sage_builds/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include -c\n -c scipy/fftpack/src/dfftpack/dcosqb.f -o build/temp.macosx-10.6-i386-2.6/scipy/fftpack/src/dfftpack/dcosqb.o\" failed with exit status 1\nError building scipy.\n```\n",
    "created_at": "2010-10-07T00:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96646",
    "user": "@jhpalmieri"
}
```

I'm having problems with scipy on Mac OS X (Intel, 10.6):

```
compiling Fortran sources
Fortran f77 compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -ffixed-form -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops
Fortran f90 compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops
Fortran fix compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -ffixed-form -fno-second-underscore -Wall -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops
creating build/temp.macosx-10.6-i386-2.6
creating build/temp.macosx-10.6-i386-2.6/scipy
creating build/temp.macosx-10.6-i386-2.6/scipy/fftpack
creating build/temp.macosx-10.6-i386-2.6/scipy/fftpack/src
creating build/temp.macosx-10.6-i386-2.6/scipy/fftpack/src/dfftpack
compile options: '-I/Applications/sage_builds/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include -c'
sage_fortran:f77: scipy/fftpack/src/dfftpack/dcosqb.f
lipo: /var/folders/ks/ksTkDzjXF7KfYo6uWLAQHk+++TM/-Tmp-//ccMIVvsm.out and /var/folders/ks/ksTkDzjXF7KfYo6uWLAQHk+++TM/-Tmp-//ccmhVCg6.out have the same architectures (ppc64) and can't be in the same fat output file
lipo: /var/folders/ks/ksTkDzjXF7KfYo6uWLAQHk+++TM/-Tmp-//ccMIVvsm.out and /var/folders/ks/ksTkDzjXF7KfYo6uWLAQHk+++TM/-Tmp-//ccmhVCg6.out have the same architectures (ppc64) and can't be in the same fat output file
error: Command "/Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -ffixed-form -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops -I/Applications/sage_builds/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include -c
 -c scipy/fftpack/src/dfftpack/dcosqb.f -o build/temp.macosx-10.6-i386-2.6/scipy/fftpack/src/dfftpack/dcosqb.o" failed with exit status 1
Error building scipy.
```




---

archive/issue_comments_096647.json:
```json
{
    "body": "OK, things are a lot better now on OpenSolaris, though seem to be a problem for John on OS X!!\n\nUsing:\n\n* The updated Numpy on this ticket\n* The updated Scipy which John made to export FC, F77, F90 and F95\n* An upated scipy_sandbox on #10092 which I made to export FC, F77, F90 and F95\n\nthen the three additional test failures caused by the Numpy/Scipy changes have all been resolved. This is on a Sun Ultra 27 running OpenSolaris 06/2009. \n\n\n```\ndrkirkby@hawk:~/new/sage-4.6.alpha2$ ./sage -t  -long devel/sage/doc/en/bordeaux_2008/introduction.rst\nsage -t -long \"devel/sage/doc/en/bordeaux_2008/introduction.rst\"\n\t [3.1 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 3.1 seconds\ndrkirkby@hawk:~/new/sage-4.6.alpha2$ ./sage -t  -long devel/sage/sage/numerical/test.py\nsage -t -long \"devel/sage/sage/numerical/test.py\"           \n\t [4.5 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.5 seconds\ndrkirkby@hawk:~/new/sage-4.6.alpha2$ ./sage -t  -long devel/sage/sage/plot/plot3d/list_plot3d.py\nsage -t -long \"devel/sage/sage/plot/plot3d/list_plot3d.py\"  \n\t [3.1 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 3.1 seconds\n```\n\n\nI suspect these will work on the Solaris x86 and Solaris SPARC machines, but since:\n\n* Skynet is down for maintenance. \n* t2 is down and will remain so until William is less rude towards me. \n* Everything except my slowest SPARC is powered off. \n\nI'm not able to check this on Solaris 10, either SPARC or x86. \n\nI will run a 'ptestlong' which will take half an hour. \n\nWe will have to look at the OS X issues now!\n\nWill this ticket ever get closed? \n\nDave",
    "created_at": "2010-10-07T00:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96647",
    "user": "drkirkby"
}
```

OK, things are a lot better now on OpenSolaris, though seem to be a problem for John on OS X!!

Using:

* The updated Numpy on this ticket
* The updated Scipy which John made to export FC, F77, F90 and F95
* An upated scipy_sandbox on #10092 which I made to export FC, F77, F90 and F95

then the three additional test failures caused by the Numpy/Scipy changes have all been resolved. This is on a Sun Ultra 27 running OpenSolaris 06/2009. 


```
drkirkby@hawk:~/new/sage-4.6.alpha2$ ./sage -t  -long devel/sage/doc/en/bordeaux_2008/introduction.rst
sage -t -long "devel/sage/doc/en/bordeaux_2008/introduction.rst"
	 [3.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.1 seconds
drkirkby@hawk:~/new/sage-4.6.alpha2$ ./sage -t  -long devel/sage/sage/numerical/test.py
sage -t -long "devel/sage/sage/numerical/test.py"           
	 [4.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.5 seconds
drkirkby@hawk:~/new/sage-4.6.alpha2$ ./sage -t  -long devel/sage/sage/plot/plot3d/list_plot3d.py
sage -t -long "devel/sage/sage/plot/plot3d/list_plot3d.py"  
	 [3.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.1 seconds
```


I suspect these will work on the Solaris x86 and Solaris SPARC machines, but since:

* Skynet is down for maintenance. 
* t2 is down and will remain so until William is less rude towards me. 
* Everything except my slowest SPARC is powered off. 

I'm not able to check this on Solaris 10, either SPARC or x86. 

I will run a 'ptestlong' which will take half an hour. 

We will have to look at the OS X issues now!

Will this ticket ever get closed? 

Dave



---

archive/issue_comments_096648.json:
```json
{
    "body": "I've got no idea if this will solve it, but the sage_fortran script has in it:\n\n\n```\n/usr/local/gcc-4.5.0-delayed/bin/gfortran -fPIC $@\n```\n\n\nbut the bit at the end should be quoted:\n\n\n```\n/usr/local/gcc-4.5.0-delayed/bin/gfortran -fPIC \"$@\"\n```\n\n\nI've never found that an issue with any package in Sage, but when I tried to use an identical script for gcc and g++, I found problems which got resolved when I quoted the end of the line. You could try manually editing the script, putting a couple of quotation marks and seeing if that helps. \n\nThis is very puzzling, but it is 1:25 AM here, and time I hit the bed. \n\nJohn, do you think the changing of the Fortran settings in these packages has caused the problem on OS X? \n\nDave",
    "created_at": "2010-10-07T00:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96648",
    "user": "drkirkby"
}
```

I've got no idea if this will solve it, but the sage_fortran script has in it:


```
/usr/local/gcc-4.5.0-delayed/bin/gfortran -fPIC $@
```


but the bit at the end should be quoted:


```
/usr/local/gcc-4.5.0-delayed/bin/gfortran -fPIC "$@"
```


I've never found that an issue with any package in Sage, but when I tried to use an identical script for gcc and g++, I found problems which got resolved when I quoted the end of the line. You could try manually editing the script, putting a couple of quotation marks and seeing if that helps. 

This is very puzzling, but it is 1:25 AM here, and time I hit the bed. 

John, do you think the changing of the Fortran settings in these packages has caused the problem on OS X? 

Dave



---

archive/issue_comments_096649.json:
```json
{
    "body": "Is it supposed to have all of these:  -arch ppc -arch x86_64 -arch ppc64\non OSX? Are making a fat build that could be used on all these archs somehow?",
    "created_at": "2010-10-07T00:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96649",
    "user": "@kiwifb"
}
```

Is it supposed to have all of these:  -arch ppc -arch x86_64 -arch ppc64
on OSX? Are making a fat build that could be used on all these archs somehow?



---

archive/issue_comments_096650.json:
```json
{
    "body": "> John, do you think the changing of the Fortran settings in these packages has caused the problem on OS X?\n\nWhen I saw the problem, I tried rebuilding with older versions, or with versions modified to undo those changes.  I had the same problem, so assuming I didn't screw anything up, it wasn't caused by changing the Fortran settings.\n\n> You could try manually editing the script, putting a couple of quotation marks and seeing if that helps.\n\nI'll try it.",
    "created_at": "2010-10-07T01:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96650",
    "user": "@jhpalmieri"
}
```

> John, do you think the changing of the Fortran settings in these packages has caused the problem on OS X?

When I saw the problem, I tried rebuilding with older versions, or with versions modified to undo those changes.  I had the same problem, so assuming I didn't screw anything up, it wasn't caused by changing the Fortran settings.

> You could try manually editing the script, putting a couple of quotation marks and seeing if that helps.

I'll try it.



---

archive/issue_comments_096651.json:
```json
{
    "body": "Replying to [comment:224 drkirkby]:\n> I've got no idea if this will solve it, but the sage_fortran script has in it:\n> \n\n```\n/usr/local/gcc-4.5.0-delayed/bin/gfortran -fPIC $@\n```\n\n\nOn my Mac, it actually looks like this:\n\n```/usr/bin/env bash\n$SAGE_LOCAL/bin/gfortran-64  -m64 \"$@\"\n```\n\nSo I don't need to add quotes -- they're already there.  And so this is not the cause of the problem.",
    "created_at": "2010-10-07T03:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96651",
    "user": "@jhpalmieri"
}
```

Replying to [comment:224 drkirkby]:
> I've got no idea if this will solve it, but the sage_fortran script has in it:
> 

```
/usr/local/gcc-4.5.0-delayed/bin/gfortran -fPIC $@
```


On my Mac, it actually looks like this:

```/usr/bin/env bash
$SAGE_LOCAL/bin/gfortran-64  -m64 "$@"
```

So I don't need to add quotes -- they're already there.  And so this is not the cause of the problem.



---

archive/issue_comments_096652.json:
```json
{
    "body": "I run ptestlong after sorting out the Fortran issues, and get:\n\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t  -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed\n\tsage -t  -long devel/sage/sage/tensor/differential_forms.py # 1 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1868.7 seconds\n```\n\n\nwhich is two failures I was aware of, which are being worked on at #10041 and #10042. \n\nHowever, to have only these 2 failures, and not 5, it's essential to use an updated package at #10092, which just adds exports FC, F77, F90 and F95 from scipy_sandbox. \n\nOf course, that still does not resolve the OS X issues which John has. If they are new to these updated packages, then we still have a problem.",
    "created_at": "2010-10-07T08:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96652",
    "user": "drkirkby"
}
```

I run ptestlong after sorting out the Fortran issues, and get:


```
----------------------------------------------------------------------

The following tests failed:

	sage -t  -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed
	sage -t  -long devel/sage/sage/tensor/differential_forms.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1868.7 seconds
```


which is two failures I was aware of, which are being worked on at #10041 and #10042. 

However, to have only these 2 failures, and not 5, it's essential to use an updated package at #10092, which just adds exports FC, F77, F90 and F95 from scipy_sandbox. 

Of course, that still does not resolve the OS X issues which John has. If they are new to these updated packages, then we still have a problem.



---

archive/issue_comments_096653.json:
```json
{
    "body": "A summary of changes to help reviewers - this ticket has got a bit complex, as 3 packages and a patch all need to be applied.",
    "created_at": "2010-10-07T08:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96653",
    "user": "drkirkby"
}
```

A summary of changes to help reviewers - this ticket has got a bit complex, as 3 packages and a patch all need to be applied.



---

archive/issue_comments_096654.json:
```json
{
    "body": "Attachment [changes.txt](tarball://root/attachments/some-uuid/ticket9808/changes.txt) by drkirkby created at 2010-10-07 09:18:16\n\nReplying to [comment:219 fbissey]:\n> Back from snooze-land via morning teaching.\n> \n> I would have expected that the fortran settings in scipy and numpy would have to match. \n\nThat seems not to the be case. It's probably a good idea if they do, but it looks like setting FC in Numpy is enough. I've just verified with grep by looking at the Numpy log that it only ever uses the GNU compiler when compiling F90 code and does not attempt to use `/usr/bin/f90`\n\n\n```\ndrkirkby@hawk:~/new/sage-4.6.alpha2/spkg/logs$ grep  f90 numpy-1.5.0.log | grep bin\ndrkirkby@hawk:~/new/sage-4.6.alpha2/spkg/logs$ grep  f95 numpy-1.5.0.log | grep bin\ndrkirkby@hawk:~/new/sage-4.6.alpha2/spkg/logs$ \n```\n\n\nIt does not appear to have anything that's obviously using a Fortran 90 target, though it does compile files with the extension .f90. \n\n> I am completely astonished that you had problems with scipy and not numpy. In fact on Gentoo we currently have a bug open because numpy picks up the intel fortran compiler when it shouldn't.\n\nHave you reported that bug upstream to the Numpy developers? If so, do you have the link handy? Do you have a link to the Gentoo bug? You could try exporting F77, F90 and F95 in addition to FC and see if that fixes it. It would be worth opening a bug report in Sage if this is affecting Sage too, which I expect it will. I could try creating a file 'icc' on my Sun and seeing if Numpy uses that, though since the Intel compiler does not run on Solaris, there's less chance of that being an issue. Perhaps someone with Linux can create a file `icc` that simply exits with 1. \n\n\n```/bin/sh\nexit 1\n```\n\n\nand see if that screws up building Numpy. If so, it's a bug. \n\nIn fact, given the issues with Scipy and scipy_sandbox, it might be wise we export all these variables in Numpy. \n\nWhat puzzles me most is why it is now necessary do this in scipy_sandbox, despite there have been no changes to the scipy_sandbox code at all! But checking in the sage-4.6.1.alpha1 code, I see the f90 target is using `sage_fortran` and not `/usr/bin/f90`.\n\n\n```\ndrkirkby@hawk:~/sage-4.6.alpha1/spkg/logs$ grep f90 scipy_sandbox-20071020.p5.log\nFortran f90 compiler: sage_fortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops\nFortran f90 compiler: sage_fortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops\n```\n\n\nHence this Numpy or SciPy upgrade has needed some rather surprising changes to be made to scipy_sandbox. \n\nI know when you build gmp, mpfr will be build with the same compiler, as the location of the compiler is actually stored in the gmp header files. I thought Numpy/ScipPy might use some similar technique, but it appears not.",
    "created_at": "2010-10-07T09:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96654",
    "user": "drkirkby"
}
```

Attachment [changes.txt](tarball://root/attachments/some-uuid/ticket9808/changes.txt) by drkirkby created at 2010-10-07 09:18:16

Replying to [comment:219 fbissey]:
> Back from snooze-land via morning teaching.
> 
> I would have expected that the fortran settings in scipy and numpy would have to match. 

That seems not to the be case. It's probably a good idea if they do, but it looks like setting FC in Numpy is enough. I've just verified with grep by looking at the Numpy log that it only ever uses the GNU compiler when compiling F90 code and does not attempt to use `/usr/bin/f90`


```
drkirkby@hawk:~/new/sage-4.6.alpha2/spkg/logs$ grep  f90 numpy-1.5.0.log | grep bin
drkirkby@hawk:~/new/sage-4.6.alpha2/spkg/logs$ grep  f95 numpy-1.5.0.log | grep bin
drkirkby@hawk:~/new/sage-4.6.alpha2/spkg/logs$ 
```


It does not appear to have anything that's obviously using a Fortran 90 target, though it does compile files with the extension .f90. 

> I am completely astonished that you had problems with scipy and not numpy. In fact on Gentoo we currently have a bug open because numpy picks up the intel fortran compiler when it shouldn't.

Have you reported that bug upstream to the Numpy developers? If so, do you have the link handy? Do you have a link to the Gentoo bug? You could try exporting F77, F90 and F95 in addition to FC and see if that fixes it. It would be worth opening a bug report in Sage if this is affecting Sage too, which I expect it will. I could try creating a file 'icc' on my Sun and seeing if Numpy uses that, though since the Intel compiler does not run on Solaris, there's less chance of that being an issue. Perhaps someone with Linux can create a file `icc` that simply exits with 1. 


```/bin/sh
exit 1
```


and see if that screws up building Numpy. If so, it's a bug. 

In fact, given the issues with Scipy and scipy_sandbox, it might be wise we export all these variables in Numpy. 

What puzzles me most is why it is now necessary do this in scipy_sandbox, despite there have been no changes to the scipy_sandbox code at all! But checking in the sage-4.6.1.alpha1 code, I see the f90 target is using `sage_fortran` and not `/usr/bin/f90`.


```
drkirkby@hawk:~/sage-4.6.alpha1/spkg/logs$ grep f90 scipy_sandbox-20071020.p5.log
Fortran f90 compiler: sage_fortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops
Fortran f90 compiler: sage_fortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops
```


Hence this Numpy or SciPy upgrade has needed some rather surprising changes to be made to scipy_sandbox. 

I know when you build gmp, mpfr will be build with the same compiler, as the location of the compiler is actually stored in the gmp header files. I thought Numpy/ScipPy might use some similar technique, but it appears not.



---

archive/issue_comments_096655.json:
```json
{
    "body": "The problem with ifc is actually more subtle than that [http://bugs.gentoo.org/show_bug.cgi?id=336077](http://bugs.gentoo.org/show_bug.cgi?id=336077) . someone has ifc installed but no license for whatever reason. Even so FC is set to gfortran, ifc will be tested if found. Without a license ifc wants to create a number of folders in the system, because the build system is sandboxed (so that no live files are touched will we are building the software) ifc throws an error with stops the build.\n\nWhile sage doesn't use a sandbox the build could stop if ifc has been installed as root and a regular user is building numpy.\n\nThat's something to remember, even if a fortran compiler is selected, numpy/scipy will test for all the compilers they know off and try the one they found.\n\nAs for scipy, there were notes in the old spkg that scipy uses numpy distutils to build, that may have changed slightly in scipy-0.8.0 as it wasn't necessary to set all these compilers before at least in sage. A quick look at the corresponding Gentoo ebuilds show that we have been setting FC, F77 and F90 (but not F95) for some time in scipy (OK I didn't go in the CVS attic to checkout 0.7.0 in particular, just 0.8.0 and 0.7.2).",
    "created_at": "2010-10-07T09:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96655",
    "user": "@kiwifb"
}
```

The problem with ifc is actually more subtle than that [http://bugs.gentoo.org/show_bug.cgi?id=336077](http://bugs.gentoo.org/show_bug.cgi?id=336077) . someone has ifc installed but no license for whatever reason. Even so FC is set to gfortran, ifc will be tested if found. Without a license ifc wants to create a number of folders in the system, because the build system is sandboxed (so that no live files are touched will we are building the software) ifc throws an error with stops the build.

While sage doesn't use a sandbox the build could stop if ifc has been installed as root and a regular user is building numpy.

That's something to remember, even if a fortran compiler is selected, numpy/scipy will test for all the compilers they know off and try the one they found.

As for scipy, there were notes in the old spkg that scipy uses numpy distutils to build, that may have changed slightly in scipy-0.8.0 as it wasn't necessary to set all these compilers before at least in sage. A quick look at the corresponding Gentoo ebuilds show that we have been setting FC, F77 and F90 (but not F95) for some time in scipy (OK I didn't go in the CVS attic to checkout 0.7.0 in particular, just 0.8.0 and 0.7.2).



---

archive/issue_comments_096656.json:
```json
{
    "body": "Replying to [comment:230 fbissey]:\n> The problem with ifc is actually more subtle than that [http://bugs.gentoo.org/show_bug.cgi?id=336077](http://bugs.gentoo.org/show_bug.cgi?id=336077) . someone has ifc installed but no license for whatever reason. \n\nProbably a trial which has run out. I've had a few of them!\n\n> Even so FC is set to gfortran, ifc will be tested if found. Without a license ifc wants to create a number of folders in the system, because the build system is sandboxed (so that no live files are touched will we are building the software) ifc throws an error with stops the build.\n> \n> While sage doesn't use a sandbox the build could stop if ifc has been installed as root and a regular user is building numpy.\n\nOK, thank you. I think we need to check that. If Numpy is not using the compiler we specify, that must be a bug IMHO. \n \n> That's something to remember, even if a fortran compiler is selected, numpy/scipy will test for all the compilers they know off and try the one they found.\n\nIt seems a bit odd, given we have specified one. \n \n> As for scipy, there were notes in the old spkg that scipy uses numpy distutils to build, that may have changed slightly in scipy-0.8.0 as it wasn't necessary to set all these compilers before at least in sage. A quick look at the corresponding Gentoo ebuilds show that we have been setting FC, F77 and F90 (but not F95) for some time in scipy (OK I didn't go in the CVS attic to checkout 0.7.0 in particular, just 0.8.0 and 0.7.2).\n\nSetting F95 was a precaution. \n\nAny chance of you taking a look at #10092, which sets these Fortran variable in scipy_sandbox? That should be quite easy to review and would be one step closer to getting this more complex ticket reviewed. \n\nDave",
    "created_at": "2010-10-07T12:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96656",
    "user": "drkirkby"
}
```

Replying to [comment:230 fbissey]:
> The problem with ifc is actually more subtle than that [http://bugs.gentoo.org/show_bug.cgi?id=336077](http://bugs.gentoo.org/show_bug.cgi?id=336077) . someone has ifc installed but no license for whatever reason. 

Probably a trial which has run out. I've had a few of them!

> Even so FC is set to gfortran, ifc will be tested if found. Without a license ifc wants to create a number of folders in the system, because the build system is sandboxed (so that no live files are touched will we are building the software) ifc throws an error with stops the build.
> 
> While sage doesn't use a sandbox the build could stop if ifc has been installed as root and a regular user is building numpy.

OK, thank you. I think we need to check that. If Numpy is not using the compiler we specify, that must be a bug IMHO. 
 
> That's something to remember, even if a fortran compiler is selected, numpy/scipy will test for all the compilers they know off and try the one they found.

It seems a bit odd, given we have specified one. 
 
> As for scipy, there were notes in the old spkg that scipy uses numpy distutils to build, that may have changed slightly in scipy-0.8.0 as it wasn't necessary to set all these compilers before at least in sage. A quick look at the corresponding Gentoo ebuilds show that we have been setting FC, F77 and F90 (but not F95) for some time in scipy (OK I didn't go in the CVS attic to checkout 0.7.0 in particular, just 0.8.0 and 0.7.2).

Setting F95 was a precaution. 

Any chance of you taking a look at #10092, which sets these Fortran variable in scipy_sandbox? That should be quite easy to review and would be one step closer to getting this more complex ticket reviewed. 

Dave



---

archive/issue_comments_096657.json:
```json
{
    "body": "I've upgraded to the new ones on the Mac PPC, and the only problem I get in sage/matrix and sage/functions (other than the ones the patch fixes) is\n\n```\nsage -t -long \"devel/sage/sage/functions/hyperbolic.py\"     \nWarning: divide by zero encountered in divide\nWarning: divide by zero encountered in divide\n```\n\nAny ideas?  Looks like some other stuff reported here. I don't know that it would show up in doctesting.",
    "created_at": "2010-10-07T20:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96657",
    "user": "@kcrisman"
}
```

I've upgraded to the new ones on the Mac PPC, and the only problem I get in sage/matrix and sage/functions (other than the ones the patch fixes) is

```
sage -t -long "devel/sage/sage/functions/hyperbolic.py"     
Warning: divide by zero encountered in divide
Warning: divide by zero encountered in divide
```

Any ideas?  Looks like some other stuff reported here. I don't know that it would show up in doctesting.



---

archive/issue_comments_096658.json:
```json
{
    "body": "Replying to [comment:232 kcrisman]:\n> I've upgraded to the new ones on the Mac PPC, and the only problem I get in sage/matrix and sage/functions (other than the ones the patch fixes) is\n> {{{\n> sage -t -long \"devel/sage/sage/functions/hyperbolic.py\"     \n> Warning: divide by zero encountered in divide\n> Warning: divide by zero encountered in divide\n> }}}\n> Any ideas?  Looks like some other stuff reported here. I don't know that it would show up in doctesting.\n\nI don't get that on linux ppc, although I had a similar warning in sage/calculus/interpolators.pyx on one of my x86 box with sage-on-gentoo, I don't remember it showing on any other box, and the test in question has had a failure with sage-on-gentoo on that box only for a long time. A bit of a mistery [http://github.com/cschwan/sage-on-gentoo/issues#issue/6](http://github.com/cschwan/sage-on-gentoo/issues#issue/6) .\n\nI will review #10092 shortly, should be quick.",
    "created_at": "2010-10-07T21:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96658",
    "user": "@kiwifb"
}
```

Replying to [comment:232 kcrisman]:
> I've upgraded to the new ones on the Mac PPC, and the only problem I get in sage/matrix and sage/functions (other than the ones the patch fixes) is
> {{{
> sage -t -long "devel/sage/sage/functions/hyperbolic.py"     
> Warning: divide by zero encountered in divide
> Warning: divide by zero encountered in divide
> }}}
> Any ideas?  Looks like some other stuff reported here. I don't know that it would show up in doctesting.

I don't get that on linux ppc, although I had a similar warning in sage/calculus/interpolators.pyx on one of my x86 box with sage-on-gentoo, I don't remember it showing on any other box, and the test in question has had a failure with sage-on-gentoo on that box only for a long time. A bit of a mistery [http://github.com/cschwan/sage-on-gentoo/issues#issue/6](http://github.com/cschwan/sage-on-gentoo/issues#issue/6) .

I will review #10092 shortly, should be quick.



---

archive/issue_comments_096659.json:
```json
{
    "body": "How close is this ticket being to positively reviewed?  I have a trial 4.6.alpha3 that's ready to release, except for #10097, which I expect we'll fix within a day.  I'll release 4.6.alpha3 after that and put 4.6 in feature freeze.",
    "created_at": "2010-10-07T22:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96659",
    "user": "@qed777"
}
```

How close is this ticket being to positively reviewed?  I have a trial 4.6.alpha3 that's ready to release, except for #10097, which I expect we'll fix within a day.  I'll release 4.6.alpha3 after that and put 4.6 in feature freeze.



---

archive/issue_comments_096660.json:
```json
{
    "body": "Replying to [comment:234 mpatel]:\n> How close is this ticket being to positively reviewed?  I have a trial 4.6.alpha3 that's ready to release, except for #10097, which I expect we'll fix within a day.  I'll release 4.6.alpha3 after that and put 4.6 in feature freeze.\n\nI must say that with all that's happened to the ticket in the last few days, I and possibly maldun had lost hope of it making the deadline for the feature freeze.\n\nI am about to review positively #10092 which would need merging at the same time. I am happy with\nthe spkg-es as they are for linux-ppc, so it is positive for me on that platform. I don't know about the other.",
    "created_at": "2010-10-07T22:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96660",
    "user": "@kiwifb"
}
```

Replying to [comment:234 mpatel]:
> How close is this ticket being to positively reviewed?  I have a trial 4.6.alpha3 that's ready to release, except for #10097, which I expect we'll fix within a day.  I'll release 4.6.alpha3 after that and put 4.6 in feature freeze.

I must say that with all that's happened to the ticket in the last few days, I and possibly maldun had lost hope of it making the deadline for the feature freeze.

I am about to review positively #10092 which would need merging at the same time. I am happy with
the spkg-es as they are for linux-ppc, so it is positive for me on that platform. I don't know about the other.



---

archive/issue_comments_096661.json:
```json
{
    "body": "Replying to [comment:234 mpatel]:\n> How close is this ticket being to positively reviewed?  I have a trial 4.6.alpha3 that's ready to release, except for #10097, which I expect we'll fix within a day.  I'll release 4.6.alpha3 after that and put 4.6 in feature freeze.\n\n\n#10092 has been positively reviewed. That has no dependencies, so that can go in now. \n\nThese SciPy and Numpy patches look ok to me, but John had an issue on OS X. \n\nI think this must be very close to a positive review. \n\nDave",
    "created_at": "2010-10-07T23:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96661",
    "user": "drkirkby"
}
```

Replying to [comment:234 mpatel]:
> How close is this ticket being to positively reviewed?  I have a trial 4.6.alpha3 that's ready to release, except for #10097, which I expect we'll fix within a day.  I'll release 4.6.alpha3 after that and put 4.6 in feature freeze.


#10092 has been positively reviewed. That has no dependencies, so that can go in now. 

These SciPy and Numpy patches look ok to me, but John had an issue on OS X. 

I think this must be very close to a positive review. 

Dave



---

archive/issue_comments_096662.json:
```json
{
    "body": "I get the same error as John on OS X 10.6.",
    "created_at": "2010-10-08T00:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96662",
    "user": "@kcrisman"
}
```

I get the same error as John on OS X 10.6.



---

archive/issue_comments_096663.json:
```json
{
    "body": "Replying to [comment:237 kcrisman]:\n> I get the same error as John on OS X 10.6.\n\nIn which case I think we can forget this going into this release. Numpy 1.5.1 should be released by the end of the month, so I guess we will have to wait for that. \n\n#10092 will be needed for sure, and that is **very** safe and has positive review, so it would seem sensible to merge that if possible. \n\nDave",
    "created_at": "2010-10-08T00:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96663",
    "user": "drkirkby"
}
```

Replying to [comment:237 kcrisman]:
> I get the same error as John on OS X 10.6.

In which case I think we can forget this going into this release. Numpy 1.5.1 should be released by the end of the month, so I guess we will have to wait for that. 

#10092 will be needed for sure, and that is **very** safe and has positive review, so it would seem sensible to merge that if possible. 

Dave



---

archive/issue_comments_096664.json:
```json
{
    "body": "This seems related to `-m 64` and `-arch ppc64` - see for instance [here](https://trac.macports.org/ticket/21408) for something like this in Boost (which it seems they solved by just removing that option! maybe no one is building Sage on PPC in 64-bit mode anyway?).  [This discussion](http://omgili.com/mailinglist/boost-users/lists/boost/org/2E4E2E72-3D6F-41B3-BB5B-0D81145DEA59orchidseedorg.html) also seems to have relevant information about those two options; see especially 'On Mon, 7 Sep 2009'.  \n\nAnother unrelated thread says 'the fact that the gcc compiler now creates `x86_64` code by default so we are likely missing some instances of `-m32` which weren't required' in a similar context, though obviously that's not exactly what's going on here given the error messages - just that 32/64 bit and intel/ppc has something to do with it.  Maybe we are missing some Mac flags in the new Scipy?",
    "created_at": "2010-10-08T00:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96664",
    "user": "@kcrisman"
}
```

This seems related to `-m 64` and `-arch ppc64` - see for instance [here](https://trac.macports.org/ticket/21408) for something like this in Boost (which it seems they solved by just removing that option! maybe no one is building Sage on PPC in 64-bit mode anyway?).  [This discussion](http://omgili.com/mailinglist/boost-users/lists/boost/org/2E4E2E72-3D6F-41B3-BB5B-0D81145DEA59orchidseedorg.html) also seems to have relevant information about those two options; see especially 'On Mon, 7 Sep 2009'.  

Another unrelated thread says 'the fact that the gcc compiler now creates `x86_64` code by default so we are likely missing some instances of `-m32` which weren't required' in a similar context, though obviously that's not exactly what's going on here given the error messages - just that 32/64 bit and intel/ppc has something to do with it.  Maybe we are missing some Mac flags in the new Scipy?



---

archive/issue_comments_096665.json:
```json
{
    "body": "Replying to [comment:240 kcrisman]:\n> This seems related to `-m 64` and `-arch ppc64` - see for instance [here](https://trac.macports.org/ticket/21408) for something like this in Boost (which it seems they solved by just removing that option! maybe no one is building Sage on PPC in 64-bit mode anyway?).  [This discussion](http://omgili.com/mailinglist/boost-users/lists/boost/org/2E4E2E72-3D6F-41B3-BB5B-0D81145DEA59orchidseedorg.html) also seems to have relevant information about those two options; see especially 'On Mon, 7 Sep 2009'.  \n> \n> Another unrelated thread says 'the fact that the gcc compiler now creates `x86_64` code by default so we are likely missing some instances of `-m32` which weren't required' in a similar context, though obviously that's not exactly what's going on here given the error messages - just that 32/64 bit and intel/ppc has something to do with it.  Maybe we are missing some Mac flags in the new Scipy?\n\n\nMay be. Could we have a little bit more of the log of the failure please? It could help to know what succeeded before the failure.",
    "created_at": "2010-10-08T01:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96665",
    "user": "@kiwifb"
}
```

Replying to [comment:240 kcrisman]:
> This seems related to `-m 64` and `-arch ppc64` - see for instance [here](https://trac.macports.org/ticket/21408) for something like this in Boost (which it seems they solved by just removing that option! maybe no one is building Sage on PPC in 64-bit mode anyway?).  [This discussion](http://omgili.com/mailinglist/boost-users/lists/boost/org/2E4E2E72-3D6F-41B3-BB5B-0D81145DEA59orchidseedorg.html) also seems to have relevant information about those two options; see especially 'On Mon, 7 Sep 2009'.  
> 
> Another unrelated thread says 'the fact that the gcc compiler now creates `x86_64` code by default so we are likely missing some instances of `-m32` which weren't required' in a similar context, though obviously that's not exactly what's going on here given the error messages - just that 32/64 bit and intel/ppc has something to do with it.  Maybe we are missing some Mac flags in the new Scipy?


May be. Could we have a little bit more of the log of the failure please? It could help to know what succeeded before the failure.



---

archive/issue_comments_096666.json:
```json
{
    "body": "> \n> May be. Could we have a little bit more of the log of the failure please? It could help to know what succeeded before the failure.\n\nSorry, that terminal is now gone.  Everything looks like jhpalmieri's - once Scipy is doing\n\n```\ncompiling Fortran sources\n```\n\nthe problem starts precisely there, so everything up to wherever that starts for dfftpack works.",
    "created_at": "2010-10-08T01:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96666",
    "user": "@kcrisman"
}
```

> 
> May be. Could we have a little bit more of the log of the failure please? It could help to know what succeeded before the failure.

Sorry, that terminal is now gone.  Everything looks like jhpalmieri's - once Scipy is doing

```
compiling Fortran sources
```

the problem starts precisely there, so everything up to wherever that starts for dfftpack works.



---

archive/issue_comments_096667.json:
```json
{
    "body": "> May be. Could we have a little bit more of the log of the failure please? It could help to know what succeeded before the failure.\n\nI've had the failure on two different OS X machines.  I've posted the full scipy log [here](http://sage.math.washington.edu/home/palmieri/misc/scipy-0.8.log).",
    "created_at": "2010-10-08T01:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96667",
    "user": "@jhpalmieri"
}
```

> May be. Could we have a little bit more of the log of the failure please? It could help to know what succeeded before the failure.

I've had the failure on two different OS X machines.  I've posted the full scipy log [here](http://sage.math.washington.edu/home/palmieri/misc/scipy-0.8.log).



---

archive/issue_comments_096668.json:
```json
{
    "body": "Just to check, I also built the older packages -- the ones uploaded by maldun to code.google.com -- and got the same error with  scipy.  So it doesn't seem to be because of the recent changes to those packages.",
    "created_at": "2010-10-08T01:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96668",
    "user": "@jhpalmieri"
}
```

Just to check, I also built the older packages -- the ones uploaded by maldun to code.google.com -- and got the same error with  scipy.  So it doesn't seem to be because of the recent changes to those packages.



---

archive/issue_comments_096669.json:
```json
{
    "body": "Here is something relevant in the latest Scipy - is it in previous version (in INSTALL.TXT)?  This might obviate the need to specify all those fortran compiler options...\n\n```\n\nYou can specify which Fortran compiler to use by using the following\ninstall command::\n\n  python setup.py config_fc --fcompiler=<Vendor> install\n\nTo see a valid list of <Vendor> names, run::\n\n  python setup.py config_fc --help-fcompiler\n```\n\nIs there somewhere in Scipy's makefile (or whatever) that specifies the architecture stuff for the super-universal binary?  I don't think that other Sage spkgs have the ppc64 arch, and I don't see anything in `spkg-install` that would do this.    Anyway, the thing about not finding certain fortran compilers in John's log looks suspicious, perhaps.",
    "created_at": "2010-10-08T15:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96669",
    "user": "@kcrisman"
}
```

Here is something relevant in the latest Scipy - is it in previous version (in INSTALL.TXT)?  This might obviate the need to specify all those fortran compiler options...

```

You can specify which Fortran compiler to use by using the following
install command::

  python setup.py config_fc --fcompiler=<Vendor> install

To see a valid list of <Vendor> names, run::

  python setup.py config_fc --help-fcompiler
```

Is there somewhere in Scipy's makefile (or whatever) that specifies the architecture stuff for the super-universal binary?  I don't think that other Sage spkgs have the ppc64 arch, and I don't see anything in `spkg-install` that would do this.    Anyway, the thing about not finding certain fortran compilers in John's log looks suspicious, perhaps.



---

archive/issue_comments_096670.json:
```json
{
    "body": "I don't know the significance of this, but from the scipy-0.7.5.log (the old version, which builds just fine):\n\n```\ncopying scipy/weave/weave_version.py -> build/lib.macosx-10.6-i386-2.6/scipy/weave\nrunning build_clib\ncustomize UnixCCompiler\ncustomize UnixCCompiler using build_clib\ncustomize Sage_FCompiler_1\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'\ni686-apple-darwin8-gfortran-4.2: no input files\ncustomize Sage_FCompiler_1\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'\ni686-apple-darwin8-gfortran-4.2: no input files\ncustomize Sage_FCompiler_1 using build_clib\nbuilding 'dfftpack' library\ncompiling Fortran sources\nFortran f77 compiler: sage_fortran -Wall -ffixed-form -fno-second-underscore -fPIC -O3 -funroll-loops\nFortran f90 compiler: sage_fortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops\nFortran fix compiler: sage_fortran -Wall -ffixed-form -fno-second-underscore -Wall -fno-second-underscore -fPIC -O3 -funroll-loops\n```\n\nFrom the failed scipy-0.8.log:\n\n```\ncopying scipy/weave/weave_version.py -> build/lib.macosx-10.6-i386-2.6/scipy/weave\nrunning build_clib\ncustomize UnixCCompiler\ncustomize UnixCCompiler using build_clib\ncustomize NAGFCompiler\nFound executable /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran\nFound executable /usr/bin/ar\nFound executable /usr/bin/ranlib\ncustomize AbsoftFCompiler\ncustomize IBMFCompiler\nCould not locate executable xlf95\ncustomize IntelFCompiler\ncustomize GnuFCompiler\ngnu: no Fortran 90 compiler found\nFound executable /usr/bin/ld\ngnu: no Fortran 90 compiler found\ncustomize Gnu95FCompiler\ncustomize Gnu95FCompiler\ncustomize Gnu95FCompiler using build_clib\nbuilding 'dfftpack' library\ncompiling Fortran sources\nFortran f77 compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -ffixed-form -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops\nFortran f90 compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops\nFortran fix compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -ffixed-form -fno-second-underscore -Wall -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops\n```\n\nNote that there are now lots of extra arguments to the fortran compiler.",
    "created_at": "2010-10-08T15:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96670",
    "user": "@jhpalmieri"
}
```

I don't know the significance of this, but from the scipy-0.7.5.log (the old version, which builds just fine):

```
copying scipy/weave/weave_version.py -> build/lib.macosx-10.6-i386-2.6/scipy/weave
running build_clib
customize UnixCCompiler
customize UnixCCompiler using build_clib
customize Sage_FCompiler_1
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
customize Sage_FCompiler_1
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
customize Sage_FCompiler_1 using build_clib
building 'dfftpack' library
compiling Fortran sources
Fortran f77 compiler: sage_fortran -Wall -ffixed-form -fno-second-underscore -fPIC -O3 -funroll-loops
Fortran f90 compiler: sage_fortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops
Fortran fix compiler: sage_fortran -Wall -ffixed-form -fno-second-underscore -Wall -fno-second-underscore -fPIC -O3 -funroll-loops
```

From the failed scipy-0.8.log:

```
copying scipy/weave/weave_version.py -> build/lib.macosx-10.6-i386-2.6/scipy/weave
running build_clib
customize UnixCCompiler
customize UnixCCompiler using build_clib
customize NAGFCompiler
Found executable /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran
Found executable /usr/bin/ar
Found executable /usr/bin/ranlib
customize AbsoftFCompiler
customize IBMFCompiler
Could not locate executable xlf95
customize IntelFCompiler
customize GnuFCompiler
gnu: no Fortran 90 compiler found
Found executable /usr/bin/ld
gnu: no Fortran 90 compiler found
customize Gnu95FCompiler
customize Gnu95FCompiler
customize Gnu95FCompiler using build_clib
building 'dfftpack' library
compiling Fortran sources
Fortran f77 compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -ffixed-form -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops
Fortran f90 compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops
Fortran fix compiler: /Applications/sage_builds/numpy/sage-4.6.alpha2/local/bin/sage_fortran -Wall -ffixed-form -fno-second-underscore -Wall -fno-second-underscore -arch ppc -arch x86_64 -arch ppc64 -fPIC -O3 -funroll-loops
```

Note that there are now lots of extra arguments to the fortran compiler.



---

archive/issue_comments_096671.json:
```json
{
    "body": "This is what I was alluding to - they are now trying to build a universal binary for Mac, 32 and 64 bit, Intel and PPC.  Notice that they also got rid of the shared option and probably replaced it by the dynamic lookup option or whatever works for Mac.   Somehow our fortran compiler thing is not doing it right - maybe because we got rid of the whole `Sage_F_compiler` thingie?\n\nBut I have no idea where this would be in the Scipy source; I'm learning on the job.  I do think that getting rid of wherever the `-arch ppc64` is in there has a high probability of clearing up the issue, though in a hackish way (and this is what Boost did in the threads I link to in Comment 240).",
    "created_at": "2010-10-08T17:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96671",
    "user": "@kcrisman"
}
```

This is what I was alluding to - they are now trying to build a universal binary for Mac, 32 and 64 bit, Intel and PPC.  Notice that they also got rid of the shared option and probably replaced it by the dynamic lookup option or whatever works for Mac.   Somehow our fortran compiler thing is not doing it right - maybe because we got rid of the whole `Sage_F_compiler` thingie?

But I have no idea where this would be in the Scipy source; I'm learning on the job.  I do think that getting rid of wherever the `-arch ppc64` is in there has a high probability of clearing up the issue, though in a hackish way (and this is what Boost did in the threads I link to in Comment 240).



---

archive/issue_comments_096672.json:
```json
{
    "body": "I think the best thing is we ask on the SciPy mailing list. I assume there is one - there is one for Numpy. None of us appear to know how to fix this properly, \n\nI've got no idea if is related to getting rid of the Sage_F_compiler thingie, but that sure is a possibility. \n\nI'm going to try to find a suitable list, subscribe to it, then ask. \n\nDave",
    "created_at": "2010-10-08T17:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96672",
    "user": "drkirkby"
}
```

I think the best thing is we ask on the SciPy mailing list. I assume there is one - there is one for Numpy. None of us appear to know how to fix this properly, 

I've got no idea if is related to getting rid of the Sage_F_compiler thingie, but that sure is a possibility. 

I'm going to try to find a suitable list, subscribe to it, then ask. 

Dave



---

archive/issue_comments_096673.json:
```json
{
    "body": "Replying to [comment:249 drkirkby]:\n> I think the best thing is we ask on the SciPy mailing list. I assume there is one - there is one for Numpy. None of us appear to know how to fix this properly, \n> \n> I've got no idea if is related to getting rid of the Sage_F_compiler thingie, but that sure is a possibility. \n> \n> I'm going to try to find a suitable list, subscribe to it, then ask. \n> \n\nSee http://scipy.org/Mailing_Lists",
    "created_at": "2010-10-08T17:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96673",
    "user": "@jasongrout"
}
```

Replying to [comment:249 drkirkby]:
> I think the best thing is we ask on the SciPy mailing list. I assume there is one - there is one for Numpy. None of us appear to know how to fix this properly, 
> 
> I've got no idea if is related to getting rid of the Sage_F_compiler thingie, but that sure is a possibility. 
> 
> I'm going to try to find a suitable list, subscribe to it, then ask. 
> 

See http://scipy.org/Mailing_Lists



---

archive/issue_comments_096674.json:
```json
{
    "body": "Possibly related?\n\n- [http://projects.scipy.org/numpy/ticket/1399](http://projects.scipy.org/numpy/ticket/1399)\n- [http://article.gmane.org/gmane.comp.python.scientific.devel/14564](http://article.gmane.org/gmane.comp.python.scientific.devel/14564)\n- [http://article.gmane.org/gmane.comp.python.scientific.user/26314](http://article.gmane.org/gmane.comp.python.scientific.user/26314)",
    "created_at": "2010-10-08T17:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96674",
    "user": "@jhpalmieri"
}
```

Possibly related?

- [http://projects.scipy.org/numpy/ticket/1399](http://projects.scipy.org/numpy/ticket/1399)
- [http://article.gmane.org/gmane.comp.python.scientific.devel/14564](http://article.gmane.org/gmane.comp.python.scientific.devel/14564)
- [http://article.gmane.org/gmane.comp.python.scientific.user/26314](http://article.gmane.org/gmane.comp.python.scientific.user/26314)



---

archive/issue_comments_096675.json:
```json
{
    "body": "Almost certainly so.",
    "created_at": "2010-10-08T18:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96675",
    "user": "@kcrisman"
}
```

Almost certainly so.



---

archive/issue_comments_096676.json:
```json
{
    "body": "Replying to [comment:250 jason]:\n> Replying to [comment:249 drkirkby]:\n> > I think the best thing is we ask on the SciPy mailing list. I assume there is one - there is one for Numpy. None of us appear to know how to fix this properly, \n> > \n> > I've got no idea if is related to getting rid of the Sage_F_compiler thingie, but that sure is a possibility. \n> > \n> > I'm going to try to find a suitable list, subscribe to it, then ask. \n> > \n> \n> See http://scipy.org/Mailing_Lists\n> \n\nI've subscribed to scipy-user----AT----scipy.org and made a post with the title *Problems building SciPy on OS X due to ppc64 issues* I posted a link to John's build log. \n\nRobert Kern has replied to my post:\n\n```\nAre the multiple \"-c\" options causing issues? From the build log, it\nlooks like \"-c\" is being added explicitly somewhere.\n\ncompile options:\n'-I/Applications/sage_builds/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include\n-c'\n\nExactly where did the gfortran compiler come from? What version is it?\nWhat architecture is the machine doing the build?\n```\n\n\nIt would help if someone who is experiencing the problem could subscribe to scipy-user, as otherwise I'm just a middle-man! \n\nDave",
    "created_at": "2010-10-08T20:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96676",
    "user": "drkirkby"
}
```

Replying to [comment:250 jason]:
> Replying to [comment:249 drkirkby]:
> > I think the best thing is we ask on the SciPy mailing list. I assume there is one - there is one for Numpy. None of us appear to know how to fix this properly, 
> > 
> > I've got no idea if is related to getting rid of the Sage_F_compiler thingie, but that sure is a possibility. 
> > 
> > I'm going to try to find a suitable list, subscribe to it, then ask. 
> > 
> 
> See http://scipy.org/Mailing_Lists
> 

I've subscribed to scipy-user----AT----scipy.org and made a post with the title *Problems building SciPy on OS X due to ppc64 issues* I posted a link to John's build log. 

Robert Kern has replied to my post:

```
Are the multiple "-c" options causing issues? From the build log, it
looks like "-c" is being added explicitly somewhere.

compile options:
'-I/Applications/sage_builds/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include
-c'

Exactly where did the gfortran compiler come from? What version is it?
What architecture is the machine doing the build?
```


It would help if someone who is experiencing the problem could subscribe to scipy-user, as otherwise I'm just a middle-man! 

Dave



---

archive/issue_comments_096677.json:
```json
{
    "body": "There's a potentially helpful comment on the SciPy list from Ralf Gommers. It concerns *boost* again. It suggests we are trying to build ppc on a system which does not support PPC. In which case, removing that option for ppc is a necessarily and not a hack. \n\nI'm puzzled how this option gets added now though - where does it come from? \n\n*Some googling turns up this which seems related to your issue:*\n\nhttp://omgili.com/mailinglist/boost-users/lists/boost/org/2E4E2E72-3D6F-41B3-BB5B-0D81145DEA59orchidseedorg.html\n\n''You are using the 10.6 SDK and gcc 4.2. In the 10.6 SDK the ppc64\narchitecture is not supported anymore, you want to use 10.4 or 10.5 SDK.\nSince Python is built with gcc 4.0 you want to do the same if you want C++\nsupport for ppc64 (which you'll need for scipy.sparsetools).''\n\n''The above may be irrelevant for you though, since Sage is distributing\nbinaries for each OS X version separately, right? 10.6 doesn't install on\nppc64 machines, so no need to build that arch at all.''\n\nDave",
    "created_at": "2010-10-09T01:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96677",
    "user": "drkirkby"
}
```

There's a potentially helpful comment on the SciPy list from Ralf Gommers. It concerns *boost* again. It suggests we are trying to build ppc on a system which does not support PPC. In which case, removing that option for ppc is a necessarily and not a hack. 

I'm puzzled how this option gets added now though - where does it come from? 

*Some googling turns up this which seems related to your issue:*

http://omgili.com/mailinglist/boost-users/lists/boost/org/2E4E2E72-3D6F-41B3-BB5B-0D81145DEA59orchidseedorg.html

''You are using the 10.6 SDK and gcc 4.2. In the 10.6 SDK the ppc64
architecture is not supported anymore, you want to use 10.4 or 10.5 SDK.
Since Python is built with gcc 4.0 you want to do the same if you want C++
support for ppc64 (which you'll need for scipy.sparsetools).''

''The above may be irrelevant for you though, since Sage is distributing
binaries for each OS X version separately, right? 10.6 doesn't install on
ppc64 machines, so no need to build that arch at all.''

Dave



---

archive/issue_comments_096678.json:
```json
{
    "body": "Replying to [comment:254 drkirkby]:\n> There's a potentially helpful comment on the SciPy list from Ralf Gommers. It concerns *boost* again. It suggests we are trying to build ppc on a system which does not support PPC. In which case, removing that option for ppc is a necessarily and not a hack. \n> \n> I'm puzzled how this option gets added now though - where does it come from? \n\nThat's what I'm trying to figure out.  Usually it gets added in the spkg-install, but apparently that's not the case here - it's coming from Scipy itself, [here](http://projects.scipy.org/numpy/ticket/1399) (first noted by John).\n\n> ''You are using the 10.6 SDK and gcc 4.2. In the 10.6 SDK the ppc64\n> architecture is not supported anymore, you want to use 10.4 or 10.5 SDK.\n> Since Python is built with gcc 4.0 you want to do the same if you want C++\n> support for ppc64 (which you'll need for scipy.sparsetools).''\n\nWell, not exactly.  However, we always tell people that Mac Sage versions shouldn't be expected to work on older versions of Mac than they are created on.  So what's going on here is that we'll have to likely add something to the skpg-install or to the numpy distutils (whatever that is) that removes the ppc64 option (perhaps both ppc options?) from the `-arch` flags in order to get around this *only* in the case that we in fact have OS X 10.6\n\n```\nsage: os.uname()\n('Darwin', 'new-host-2.home', '10.4.0', 'Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386', 'i386')\n```\n\nwhere in particular `os.uname()[2][:2]==10` might be the thing to look at (this is OS X 10.6, confusingly) for checking for this, otherwise allowing a multiple architecture build. \n\n> ''The above may be irrelevant for you though, since Sage is distributing\n> binaries for each OS X version separately, right? 10.6 doesn't install on\n> ppc64 machines, so no need to build that arch at all.''\n\nYeah, but apparently we have to ask Scipy specifically not to build on it, or perhaps ask Numpy not to - otherwise it's already asked for by Numpy/Scipy, which seems confusing.\n\nIncidentally, this exact boost thread is one of the ones I pointed out earlier, I think ;)",
    "created_at": "2010-10-09T03:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96678",
    "user": "@kcrisman"
}
```

Replying to [comment:254 drkirkby]:
> There's a potentially helpful comment on the SciPy list from Ralf Gommers. It concerns *boost* again. It suggests we are trying to build ppc on a system which does not support PPC. In which case, removing that option for ppc is a necessarily and not a hack. 
> 
> I'm puzzled how this option gets added now though - where does it come from? 

That's what I'm trying to figure out.  Usually it gets added in the spkg-install, but apparently that's not the case here - it's coming from Scipy itself, [here](http://projects.scipy.org/numpy/ticket/1399) (first noted by John).

> ''You are using the 10.6 SDK and gcc 4.2. In the 10.6 SDK the ppc64
> architecture is not supported anymore, you want to use 10.4 or 10.5 SDK.
> Since Python is built with gcc 4.0 you want to do the same if you want C++
> support for ppc64 (which you'll need for scipy.sparsetools).''

Well, not exactly.  However, we always tell people that Mac Sage versions shouldn't be expected to work on older versions of Mac than they are created on.  So what's going on here is that we'll have to likely add something to the skpg-install or to the numpy distutils (whatever that is) that removes the ppc64 option (perhaps both ppc options?) from the `-arch` flags in order to get around this *only* in the case that we in fact have OS X 10.6

```
sage: os.uname()
('Darwin', 'new-host-2.home', '10.4.0', 'Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386', 'i386')
```

where in particular `os.uname()[2][:2]==10` might be the thing to look at (this is OS X 10.6, confusingly) for checking for this, otherwise allowing a multiple architecture build. 

> ''The above may be irrelevant for you though, since Sage is distributing
> binaries for each OS X version separately, right? 10.6 doesn't install on
> ppc64 machines, so no need to build that arch at all.''

Yeah, but apparently we have to ask Scipy specifically not to build on it, or perhaps ask Numpy not to - otherwise it's already asked for by Numpy/Scipy, which seems confusing.

Incidentally, this exact boost thread is one of the ones I pointed out earlier, I think ;)



---

archive/issue_comments_096679.json:
```json
{
    "body": "Replying to [comment:255 kcrisman]:\n> Replying to [comment:254 drkirkby]:\n> > There's a potentially helpful comment on the SciPy list from Ralf Gommers. It concerns *boost* again. It suggests we are trying to build ppc on a system which does not support PPC. In which case, removing that option for ppc is a necessarily and not a hack. \n> > \n> > I'm puzzled how this option gets added now though - where does it come from? \n> \n> That's what I'm trying to figure out.  Usually it gets added in the spkg-install, but apparently that's not the case here - it's coming from Scipy itself, [here](http://projects.scipy.org/numpy/ticket/1399) (first noted by John).\n\nIf you grep through the scipy directory, I don't think you'll find \"ppc64\" anywhere.  I think it's coming from numpy, and in particular the file src/numpy/distutils/fcompiler/gnu.py.  If you make the change\n\n```diff\n--- gnu.py.old\t2010-08-21 22:08:35.000000000 -0700\n+++ gnu.py\t2010-10-08 20:59:29.000000000 -0700\n@@ -254,7 +254,7 @@\n         if not sys.platform == 'darwin':\n             return []\n         arch_flags = []\n-        for arch in [\"ppc\", \"i686\", \"x86_64\", \"ppc64\"]:\n+        for arch in [\"ppc\", \"i686\", \"x86_64\"]:\n             if _can_target(cmd, arch):\n                 arch_flags.extend([\"-arch\", arch])\n         return arch_flags\n```\n\nto numpy and install it, then afterwards scipy seems to install correctly.  I don't have time this weekend to create a new spkg which incorporates this patch, or even to figure out under what circumstances to do it (do we have to detect DARWIN + x86?  should we get rid of \"ppc\" also?).  If someone else wants to make a new spkg, that would be fine with me.",
    "created_at": "2010-10-09T04:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96679",
    "user": "@jhpalmieri"
}
```

Replying to [comment:255 kcrisman]:
> Replying to [comment:254 drkirkby]:
> > There's a potentially helpful comment on the SciPy list from Ralf Gommers. It concerns *boost* again. It suggests we are trying to build ppc on a system which does not support PPC. In which case, removing that option for ppc is a necessarily and not a hack. 
> > 
> > I'm puzzled how this option gets added now though - where does it come from? 
> 
> That's what I'm trying to figure out.  Usually it gets added in the spkg-install, but apparently that's not the case here - it's coming from Scipy itself, [here](http://projects.scipy.org/numpy/ticket/1399) (first noted by John).

If you grep through the scipy directory, I don't think you'll find "ppc64" anywhere.  I think it's coming from numpy, and in particular the file src/numpy/distutils/fcompiler/gnu.py.  If you make the change

```diff
--- gnu.py.old	2010-08-21 22:08:35.000000000 -0700
+++ gnu.py	2010-10-08 20:59:29.000000000 -0700
@@ -254,7 +254,7 @@
         if not sys.platform == 'darwin':
             return []
         arch_flags = []
-        for arch in ["ppc", "i686", "x86_64", "ppc64"]:
+        for arch in ["ppc", "i686", "x86_64"]:
             if _can_target(cmd, arch):
                 arch_flags.extend(["-arch", arch])
         return arch_flags
```

to numpy and install it, then afterwards scipy seems to install correctly.  I don't have time this weekend to create a new spkg which incorporates this patch, or even to figure out under what circumstances to do it (do we have to detect DARWIN + x86?  should we get rid of "ppc" also?).  If someone else wants to make a new spkg, that would be fine with me.



---

archive/issue_comments_096680.json:
```json
{
    "body": "> > That's what I'm trying to figure out.  Usually it gets added in the spkg-install, but apparently that's not the case here - it's coming from Scipy itself, [here](http://projects.scipy.org/numpy/ticket/1399) (first noted by John).\n> \n> If you grep through the scipy directory, I don't think you'll find \"ppc64\" anywhere.  I think it's coming from numpy, and in particular the file src/numpy/distutils/fcompiler/gnu.py.  If you make the change\nYes, you're right - I realized that later last night, but had been confused by the scipy.org address.  And this is exactly the change mentioned in all these links being bandied about.\n> {{{\n> #!diff\n> --- gnu.py.old\t2010-08-21 22:08:35.000000000 -0700\n> +++ gnu.py\t2010-10-08 20:59:29.000000000 -0700\n> `@``@` -254,7 +254,7 `@``@`\n>          if not sys.platform == 'darwin':\n>              return []\n>          arch_flags = []\n> -        for arch in [\"ppc\", \"i686\", \"x86_64\", \"ppc64\"]:\n> +        for arch in [\"ppc\", \"i686\", \"x86_64\"]:\n>              if _can_target(cmd, arch):\n>                  arch_flags.extend([\"-arch\", arch])\n>          return arch_flags\n> }}}\n> to numpy and install it, then afterwards scipy seems to install correctly.  I don't have time this weekend to create a new spkg which incorporates this patch, or even to figure out under what circumstances to do it (do we have to detect DARWIN + x86?  should we get rid of \"ppc\" also?).  If someone else wants to make a new spkg, that would be fine with me.\nI can't do that this weekend, but might be able to next week.  I think that detecting `os.uname()[2][:2]==10` (or however that works in shell script) would be sufficient, since it seems to be a 10.6 problem with Python (namely, that the Python we use wouldn't support ppc64 or whatever with 10.6 - which makes sense, since 10.6 doesn't work on ppc).  It probably wouldn't hurt to remove ppc as well in that situation, but I think that Python/Apple haven't removed that as much yet since they still want to support universal binaries on PPC Leopard (10.5).",
    "created_at": "2010-10-09T12:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96680",
    "user": "@kcrisman"
}
```

> > That's what I'm trying to figure out.  Usually it gets added in the spkg-install, but apparently that's not the case here - it's coming from Scipy itself, [here](http://projects.scipy.org/numpy/ticket/1399) (first noted by John).
> 
> If you grep through the scipy directory, I don't think you'll find "ppc64" anywhere.  I think it's coming from numpy, and in particular the file src/numpy/distutils/fcompiler/gnu.py.  If you make the change
Yes, you're right - I realized that later last night, but had been confused by the scipy.org address.  And this is exactly the change mentioned in all these links being bandied about.
> {{{
> #!diff
> --- gnu.py.old	2010-08-21 22:08:35.000000000 -0700
> +++ gnu.py	2010-10-08 20:59:29.000000000 -0700
> `@``@` -254,7 +254,7 `@``@`
>          if not sys.platform == 'darwin':
>              return []
>          arch_flags = []
> -        for arch in ["ppc", "i686", "x86_64", "ppc64"]:
> +        for arch in ["ppc", "i686", "x86_64"]:
>              if _can_target(cmd, arch):
>                  arch_flags.extend(["-arch", arch])
>          return arch_flags
> }}}
> to numpy and install it, then afterwards scipy seems to install correctly.  I don't have time this weekend to create a new spkg which incorporates this patch, or even to figure out under what circumstances to do it (do we have to detect DARWIN + x86?  should we get rid of "ppc" also?).  If someone else wants to make a new spkg, that would be fine with me.
I can't do that this weekend, but might be able to next week.  I think that detecting `os.uname()[2][:2]==10` (or however that works in shell script) would be sufficient, since it seems to be a 10.6 problem with Python (namely, that the Python we use wouldn't support ppc64 or whatever with 10.6 - which makes sense, since 10.6 doesn't work on ppc).  It probably wouldn't hurt to remove ppc as well in that situation, but I think that Python/Apple haven't removed that as much yet since they still want to support universal binaries on PPC Leopard (10.5).



---

archive/issue_comments_096681.json:
```json
{
    "body": "As requested I updated the doctest changes in the patch.\n\nI tested all recent numpy and scipy versions on ubuntu 10.04, and they built without problems on sage-4.6.alpha3 and all doctests passed with the updated patch.\n\nHope that all bugs in numpy are killed soon. I think the whole ticket here contributed quite a bit to numpy and scipy.",
    "created_at": "2010-10-11T06:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96681",
    "user": "maldun"
}
```

As requested I updated the doctest changes in the patch.

I tested all recent numpy and scipy versions on ubuntu 10.04, and they built without problems on sage-4.6.alpha3 and all doctests passed with the updated patch.

Hope that all bugs in numpy are killed soon. I think the whole ticket here contributed quite a bit to numpy and scipy.



---

archive/issue_comments_096682.json:
```json
{
    "body": "Okay, I'm trying to look at this numpy package, and have some questions. \n\nFirst, there are all these special instructions in the SPKG.txt that seem to be totally irrelevant now about the `sage_fcompiler` etc. for gfortran and so forth.  Is all that unnecessary now that we exported F*, or not?  I assume drkirkby would be the most knowledgeable about this.  I know we tested this a lot, but it still worries me, since I know little about such things.\n\nSecond, I think that jhpalmieri's spkg should be 1.5.0.p0, correct?  And that should also be in SPKG.txt.\n\nNext, toward the end it should be `SciPy` not `SciPY`.\n\nAlso, 11 hours ago someone pointed on on the Numpy trac that [this](http://github.com/matthew-brett/numpy/compare/numpy:master...farchs-from-c) might solve our issue more appropriately.  I was going to try to make a numpy spkg based on the other fix, but this might be better - I have to look at it and test it.  Anyway, an update.",
    "created_at": "2010-10-13T02:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96682",
    "user": "@kcrisman"
}
```

Okay, I'm trying to look at this numpy package, and have some questions. 

First, there are all these special instructions in the SPKG.txt that seem to be totally irrelevant now about the `sage_fcompiler` etc. for gfortran and so forth.  Is all that unnecessary now that we exported F*, or not?  I assume drkirkby would be the most knowledgeable about this.  I know we tested this a lot, but it still worries me, since I know little about such things.

Second, I think that jhpalmieri's spkg should be 1.5.0.p0, correct?  And that should also be in SPKG.txt.

Next, toward the end it should be `SciPy` not `SciPY`.

Also, 11 hours ago someone pointed on on the Numpy trac that [this](http://github.com/matthew-brett/numpy/compare/numpy:master...farchs-from-c) might solve our issue more appropriately.  I was going to try to make a numpy spkg based on the other fix, but this might be better - I have to look at it and test it.  Anyway, an update.



---

archive/issue_comments_096683.json:
```json
{
    "body": "> First, there are all these special instructions ...\n\nI don't know about this.  I hope Dave does.\n\n> Second, I think that jhpalmieri's spkg should be 1.5.0.p0, correct? And that should also be in SPKG.txt.\n\nI think that since it's not a vanilla 1.5.0, making it p0 is fine.  Or because I patched someone else's (already patched) 1.5.0, it could be p0.  Anyway, it's fine with me.  (I seem to remember seeing someone express the opinion that if it's the first time we've released a package for that particular version, then we don't need a patch number, but I don't really care one way or the other.)\n\n> Next, toward the end it should be SciPy not SciPY.\n\nOkay.\n\nFinally, if you want to try a different fix, I'm happy to test it out.  Thanks for paying attention to the Numpy trac ticket; that's more than I was doing...",
    "created_at": "2010-10-13T03:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96683",
    "user": "@jhpalmieri"
}
```

> First, there are all these special instructions ...

I don't know about this.  I hope Dave does.

> Second, I think that jhpalmieri's spkg should be 1.5.0.p0, correct? And that should also be in SPKG.txt.

I think that since it's not a vanilla 1.5.0, making it p0 is fine.  Or because I patched someone else's (already patched) 1.5.0, it could be p0.  Anyway, it's fine with me.  (I seem to remember seeing someone express the opinion that if it's the first time we've released a package for that particular version, then we don't need a patch number, but I don't really care one way or the other.)

> Next, toward the end it should be SciPy not SciPY.

Okay.

Finally, if you want to try a different fix, I'm happy to test it out.  Thanks for paying attention to the Numpy trac ticket; that's more than I was doing...



---

archive/issue_comments_096684.json:
```json
{
    "body": "Replying to [comment:260 jhpalmieri]:\n> > First, there are all these special instructions ...\n> \n> I don't know about this.  I hope Dave does.\n> \nI think I know about them, they should be mostly removed. My fault for pushing\nsome of the changes obsoleting these to maldun without updating the instructions\nat the same time.",
    "created_at": "2010-10-13T03:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96684",
    "user": "@kiwifb"
}
```

Replying to [comment:260 jhpalmieri]:
> > First, there are all these special instructions ...
> 
> I don't know about this.  I hope Dave does.
> 
I think I know about them, they should be mostly removed. My fault for pushing
some of the changes obsoleting these to maldun without updating the instructions
at the same time.



---

archive/issue_comments_096685.json:
```json
{
    "body": "> Finally, if you want to try a different fix, I'm happy to test it out.  Thanks for paying attention to the Numpy trac ticket; that's more than I was doing...\n\nI'm trying it right now, but it's slow going because I know nothing about shell.  For instance, I just learned that `diff` has three different possible options, and the third one was the one that Sage patches look like - this took a half hour :(\n\nI am trying to use `uname -r` to check for the Darwin version, but I don't know what would happen on (say) Solaris with this command.  David, portability ideas?  According to [this](http://www.unixtutorial.org/commands/uname/) it seems okay.",
    "created_at": "2010-10-13T03:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96685",
    "user": "@kcrisman"
}
```

> Finally, if you want to try a different fix, I'm happy to test it out.  Thanks for paying attention to the Numpy trac ticket; that's more than I was doing...

I'm trying it right now, but it's slow going because I know nothing about shell.  For instance, I just learned that `diff` has three different possible options, and the third one was the one that Sage patches look like - this took a half hour :(

I am trying to use `uname -r` to check for the Darwin version, but I don't know what would happen on (say) Solaris with this command.  David, portability ideas?  According to [this](http://www.unixtutorial.org/commands/uname/) it seems okay.



---

archive/issue_comments_096686.json:
```json
{
    "body": "Also, because unix tutorials are bad for true beginners, I have no idea how to do something that in pseudo-Python would be\n\n```\noutput = `uname =r`\nif output[:2] == 10:\n    do ...\n```\n\nin shell script.  How do I take the output of `uname -r` and just get the first two characters (which would be 10 for OS X 10.6)?  Maddening - and of course it's impossible to figure out how to get this from the tutorials online without reading for hours.  Sorry - hopefully tomorrow I'll be able to get that figured out and test that patch, which depends on checking the `CFLAGS` passed to the fcompiler/gnu.py script.",
    "created_at": "2010-10-13T03:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96686",
    "user": "@kcrisman"
}
```

Also, because unix tutorials are bad for true beginners, I have no idea how to do something that in pseudo-Python would be

```
output = `uname =r`
if output[:2] == 10:
    do ...
```

in shell script.  How do I take the output of `uname -r` and just get the first two characters (which would be 10 for OS X 10.6)?  Maddening - and of course it's impossible to figure out how to get this from the tutorials online without reading for hours.  Sorry - hopefully tomorrow I'll be able to get that figured out and test that patch, which depends on checking the `CFLAGS` passed to the fcompiler/gnu.py script.



---

archive/issue_comments_096687.json:
```json
{
    "body": "Better use plain 'uname' as it should return Darwin for you if I am not mistaken.\nI am hoping that plain uname is portable. [http://www.opengroup.org/onlinepubs/009695399/utilities/uname.html](http://www.opengroup.org/onlinepubs/009695399/utilities/uname.html)\nIt would be much easier. There is already a bunch of line for OSX:\n\n```\nif [ `uname` = \"Darwin\" ]; then\n    unset ATLAS\n    unset BLAS\n    unset LAPACK\nelse\n    export LDFLAGS=\"${LDFLAGS} -shared\"\nfi\n```\n",
    "created_at": "2010-10-13T03:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96687",
    "user": "@kiwifb"
}
```

Better use plain 'uname' as it should return Darwin for you if I am not mistaken.
I am hoping that plain uname is portable. [http://www.opengroup.org/onlinepubs/009695399/utilities/uname.html](http://www.opengroup.org/onlinepubs/009695399/utilities/uname.html)
It would be much easier. There is already a bunch of line for OSX:

```
if [ `uname` = "Darwin" ]; then
    unset ATLAS
    unset BLAS
    unset LAPACK
else
    export LDFLAGS="${LDFLAGS} -shared"
fi
```




---

archive/issue_comments_096688.json:
```json
{
    "body": "So I looked at the special build instructions and right now they should be amended to\n\n```\nSpecial Update/Build Instructions:\n  * Scipy uses numpy's distutils to control its compilation of fortran code.\n    Whenever numpy is updated it is necessary to make sure that scipy still builds ok. \n```\n\nAnd that's it. The rest is obsolete. I should review what we have done to make sure there are no other - new instructions that should be given.",
    "created_at": "2010-10-13T03:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96688",
    "user": "@kiwifb"
}
```

So I looked at the special build instructions and right now they should be amended to

```
Special Update/Build Instructions:
  * Scipy uses numpy's distutils to control its compilation of fortran code.
    Whenever numpy is updated it is necessary to make sure that scipy still builds ok. 
```

And that's it. The rest is obsolete. I should review what we have done to make sure there are no other - new instructions that should be given.



---

archive/issue_comments_096689.json:
```json
{
    "body": "Replying to [comment:264 fbissey]:\n> Better use plain 'uname' as it should return Darwin for you if I am not mistaken.\n\nNo, the point is you want to test not only for Darwin, but for Darwin version 10.6, as opposed to 10.5 or 10.4.  `uname -r` should return strings like 10.4.0, 9.3.1, and 8.8.0, respectively, for these (I think).  (The last parts of the string, like 4.0 or 3.1 or 8.0, are the minor version numbers, which I don't think we care about.)\n\nThis seems to work for me, but I'm not a sed expert:\n\n```\nVER=`uname -r | sed 's/\\([0-9]*\\)\\..*/\\1/'`\n```\n\n(This takes the output from uname -r, sends it to sed, which does a regular expression match to return the digits found before the first period.)  Then you do something like\n\n```\nif [ $VER -ge 10 ]; then\n   ...\nfi\n```\n\n(Might as well test whether VER is at least 10, rather than equal to 10 on the nose.)\n\nActually, do we know if their patch needs us to test for the Darwin version?  Do you have access to a 10.4 machine to test on?",
    "created_at": "2010-10-13T04:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96689",
    "user": "@jhpalmieri"
}
```

Replying to [comment:264 fbissey]:
> Better use plain 'uname' as it should return Darwin for you if I am not mistaken.

No, the point is you want to test not only for Darwin, but for Darwin version 10.6, as opposed to 10.5 or 10.4.  `uname -r` should return strings like 10.4.0, 9.3.1, and 8.8.0, respectively, for these (I think).  (The last parts of the string, like 4.0 or 3.1 or 8.0, are the minor version numbers, which I don't think we care about.)

This seems to work for me, but I'm not a sed expert:

```
VER=`uname -r | sed 's/\([0-9]*\)\..*/\1/'`
```

(This takes the output from uname -r, sends it to sed, which does a regular expression match to return the digits found before the first period.)  Then you do something like

```
if [ $VER -ge 10 ]; then
   ...
fi
```

(Might as well test whether VER is at least 10, rather than equal to 10 on the nose.)

Actually, do we know if their patch needs us to test for the Darwin version?  Do you have access to a 10.4 machine to test on?



---

archive/issue_comments_096690.json:
```json
{
    "body": "A few points. \n* I'm going to be very busy over the next week, and particularly today, so I don't have a lot of time to put into this. \n* I believe the pacakge should be called 1.5.0 and not 1.5.0.p0 - this was discussed some time ago on sage-devel. \n* I'm not sure that 'sed' command is doing what John wants. Instead of using 'uname' for test purposes, use 'echo'. \n\n\n```\ndrkirkby@hawk:~$ echo 10.1.4  | sed 's/\\([0-9]*\\)\\..*/\\1/'\n10\ndrkirkby@hawk:~$ echo 10.6.0  | sed 's/\\([0-9]*\\)\\..*/\\1/'\n10\ndrkirkby@hawk:~$ echo 10.6.0  | sed 's/\\([0-9]*\\)\\..*/\\1/'\n10\ndrkirkby@hawk:~$ echo 10.5.1  | sed 's/\\([0-9]*\\)\\..*/\\1/'\n10\ndrkirkby@hawk:~$ echo 9.5.1  | sed 's/\\([0-9]*\\)\\..*/\\1/'\n9\ndrkirkby@hawk:~$ echo 10.4.1  | sed 's/\\([0-9]*\\)\\..*/\\1/'\n10\n```\n\n\nThat looks to be taking only the major part, and so can't distinguish from 10.5 or 10.6, which I think is what is said is needed. If that's what's needed, my approach would be \n* Simulate the output of 'uname -r' (which is portable, so can be used on any platform, not just OS X), using 'echo'. That way you don't need to find different systems to test on. \n* Make sure the OS is OS X. My HP C3600 runs HP-UX 11.11 and I expect (though it's off so I can't check), that 'uname -r' might print 11.11 which would not be any use here. So put this all in 'if' statemant that checks for OS X first. \n* If you consider the output version to be x.y.z, then I'd do something like this, where I split the x.y.z into individual parts, by first replacing the dots with a space, then printing the 1st, 2nd or 3rd part of the expressions using 'awk'. \n\n\n```\ndrkirkby@hawk:~$ echo 10.4.1\n10.4.1\ndrkirkby@hawk:~$ echo 10.4.1  | sed 's/\\./ /g' \n10 4 1\ndrkirkby@hawk:~$ echo 10.4.1  | sed 's/\\./ /g' | awk '{print $1}'\n10\ndrkirkby@hawk:~$ echo 10.4.1  | sed 's/\\./ /g' | awk '{print $2}'\n4\ndrkirkby@hawk:~$ echo 10.4.1  | sed 's/\\./ /g' | awk '{print $3}'\n1\ndrkirkby@hawk:~$ \n```\n",
    "created_at": "2010-10-13T11:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96690",
    "user": "drkirkby"
}
```

A few points. 
* I'm going to be very busy over the next week, and particularly today, so I don't have a lot of time to put into this. 
* I believe the pacakge should be called 1.5.0 and not 1.5.0.p0 - this was discussed some time ago on sage-devel. 
* I'm not sure that 'sed' command is doing what John wants. Instead of using 'uname' for test purposes, use 'echo'. 


```
drkirkby@hawk:~$ echo 10.1.4  | sed 's/\([0-9]*\)\..*/\1/'
10
drkirkby@hawk:~$ echo 10.6.0  | sed 's/\([0-9]*\)\..*/\1/'
10
drkirkby@hawk:~$ echo 10.6.0  | sed 's/\([0-9]*\)\..*/\1/'
10
drkirkby@hawk:~$ echo 10.5.1  | sed 's/\([0-9]*\)\..*/\1/'
10
drkirkby@hawk:~$ echo 9.5.1  | sed 's/\([0-9]*\)\..*/\1/'
9
drkirkby@hawk:~$ echo 10.4.1  | sed 's/\([0-9]*\)\..*/\1/'
10
```


That looks to be taking only the major part, and so can't distinguish from 10.5 or 10.6, which I think is what is said is needed. If that's what's needed, my approach would be 
* Simulate the output of 'uname -r' (which is portable, so can be used on any platform, not just OS X), using 'echo'. That way you don't need to find different systems to test on. 
* Make sure the OS is OS X. My HP C3600 runs HP-UX 11.11 and I expect (though it's off so I can't check), that 'uname -r' might print 11.11 which would not be any use here. So put this all in 'if' statemant that checks for OS X first. 
* If you consider the output version to be x.y.z, then I'd do something like this, where I split the x.y.z into individual parts, by first replacing the dots with a space, then printing the 1st, 2nd or 3rd part of the expressions using 'awk'. 


```
drkirkby@hawk:~$ echo 10.4.1
10.4.1
drkirkby@hawk:~$ echo 10.4.1  | sed 's/\./ /g' 
10 4 1
drkirkby@hawk:~$ echo 10.4.1  | sed 's/\./ /g' | awk '{print $1}'
10
drkirkby@hawk:~$ echo 10.4.1  | sed 's/\./ /g' | awk '{print $2}'
4
drkirkby@hawk:~$ echo 10.4.1  | sed 's/\./ /g' | awk '{print $3}'
1
drkirkby@hawk:~$ 
```




---

archive/issue_comments_096691.json:
```json
{
    "body": "Great, all this should hopefully work out fine.   Most of what is said above I already had been checking anyway, but having the syntax is nice. \n\n```\nif [ `uname` = \"Darwin\"]; then\n    VER=`uname -r | sed 's/\\([0-9]*\\)\\..*/\\1/'`\n    if [ $VER -ge 10 ]; then\n        cp ../patches/gnu-changes.py numpy/distutils/fcompiler/gnu.py\nfi\n```\n\nbecause `uname -r` being 10.x.y means OS X 10.6.  It is VERY confusing, but that's how it is (as John points out).  So John's sed command should work.\n\nI also updated the SPKG.txt as Francois indicated.  I should have an spkg ready to test sometime today with all this changed - assuming it works, that is.\n\nThe patch doesn't require us to test for the Darwin version, and I do have a 10.4 machine to test it on (though it takes ages to build Scipy).  I guess I could just patch it completely.  I just would rather only apply the patch if absolutely necessary, since although the code makes sense, I don't know what will happen until I try it (which, as said, will happen later today).  What they do is get the `-arch` flags from the ambient `CFLAGS` and I don't actually know what the ambient `CFLAGS` will be - presumably from elsewhere in Python or whatever, but who knows?    \n\nAnyway, if we only apply it on Mac Snow Leopard, that will also make it maximally easy to review that part of the change; I haven't made any other changes to spkg-install. \n\nWell, now it's time to sage-pkg it up, and hope for the best.",
    "created_at": "2010-10-13T12:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96691",
    "user": "@kcrisman"
}
```

Great, all this should hopefully work out fine.   Most of what is said above I already had been checking anyway, but having the syntax is nice. 

```
if [ `uname` = "Darwin"]; then
    VER=`uname -r | sed 's/\([0-9]*\)\..*/\1/'`
    if [ $VER -ge 10 ]; then
        cp ../patches/gnu-changes.py numpy/distutils/fcompiler/gnu.py
fi
```

because `uname -r` being 10.x.y means OS X 10.6.  It is VERY confusing, but that's how it is (as John points out).  So John's sed command should work.

I also updated the SPKG.txt as Francois indicated.  I should have an spkg ready to test sometime today with all this changed - assuming it works, that is.

The patch doesn't require us to test for the Darwin version, and I do have a 10.4 machine to test it on (though it takes ages to build Scipy).  I guess I could just patch it completely.  I just would rather only apply the patch if absolutely necessary, since although the code makes sense, I don't know what will happen until I try it (which, as said, will happen later today).  What they do is get the `-arch` flags from the ambient `CFLAGS` and I don't actually know what the ambient `CFLAGS` will be - presumably from elsewhere in Python or whatever, but who knows?    

Anyway, if we only apply it on Mac Snow Leopard, that will also make it maximally easy to review that part of the change; I haven't made any other changes to spkg-install. 

Well, now it's time to sage-pkg it up, and hope for the best.



---

archive/issue_comments_096692.json:
```json
{
    "body": "Replying to [comment:265 fbissey]:\n> So I looked at the special build instructions and right now they should be amended to\n> {{{\n> Special Update/Build Instructions:\n>   * Scipy uses numpy's distutils to control its compilation of fortran code.\n>     Whenever numpy is updated it is necessary to make sure that scipy still builds ok. \n> }}}\n> And that's it. The rest is obsolete. I should review what we have done to make sure there are no other - new instructions that should be given.\n\nThat includes the business about\n\n```\nThe file $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi comes from this file\n```\n\nand so on? I just want to confirm this is also obsolete.",
    "created_at": "2010-10-13T12:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96692",
    "user": "@kcrisman"
}
```

Replying to [comment:265 fbissey]:
> So I looked at the special build instructions and right now they should be amended to
> {{{
> Special Update/Build Instructions:
>   * Scipy uses numpy's distutils to control its compilation of fortran code.
>     Whenever numpy is updated it is necessary to make sure that scipy still builds ok. 
> }}}
> And that's it. The rest is obsolete. I should review what we have done to make sure there are no other - new instructions that should be given.

That includes the business about

```
The file $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi comes from this file
```

and so on? I just want to confirm this is also obsolete.



---

archive/issue_comments_096693.json:
```json
{
    "body": "Doesn't work, same error.  That doesn't mean it wouldn't be worth keeping, because of the other things mentioned in this thread and the scipy/boost lists, so I am keeping this in my current attempt at an spkg. \n\nBut I think that this means the only other possible problem is the \n\n```\nAre the multiple \"-c\" options causing issues? From the build log, it\nlooks like \"-c\" is being added explicitly somewhere.\n```\n\nissue.   From the gcc docs:\n\n```\n-c\nCompile or assemble the source files, but do not link. The linking stage simply is not done. The ultimate output is in the form of an object file for each source file.\n```\n\nSo I guess doing that twice WOULD cause the exact error message we are seeing.  Maybe once we fix that, we would still have to fix the ppc64 issue, so (as I say above) I'll keep that in for now. \n\n```\ncompile options:\n'-I/Applications/sage_builds/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include\n-c'\n```\n\nAnd then the usual `-c` is added.  So where does this one come from?  In the Numpy install I see\n\n```\nC compiler: gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes\n\ncompile options: '-Inumpy/core/src/private -Inumpy/core/src -Inumpy/core -Inumpy/core/src/npymath -Inumpy/core/src/multiarray -Inumpy/core/src/umath -Inumpy/core/include -I/Users/karl-dietercrisman/Downloads/sage-4.6.alpha3/local/include/python2.6 -c'\n```\n\nso at least sometimes it's okay to have `-c` in the compile options.  But I haven't got a clue where that string is set.\n\nAlso, there were two syntax errors in my initial change - here is the corrected one:\n\n```\nif [ `uname` = \"Darwin\" ]; then\n    VER=`uname -r | sed 's/\\([0-9]*\\)\\..*/\\1/'`\n    if [ $VER -ge 10 ]; then\n        cp ../patches/gnu-changes.py numpy/distutils/fcompiler/gnu.py\n    fi\nfi\n```\n",
    "created_at": "2010-10-13T14:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96693",
    "user": "@kcrisman"
}
```

Doesn't work, same error.  That doesn't mean it wouldn't be worth keeping, because of the other things mentioned in this thread and the scipy/boost lists, so I am keeping this in my current attempt at an spkg. 

But I think that this means the only other possible problem is the 

```
Are the multiple "-c" options causing issues? From the build log, it
looks like "-c" is being added explicitly somewhere.
```

issue.   From the gcc docs:

```
-c
Compile or assemble the source files, but do not link. The linking stage simply is not done. The ultimate output is in the form of an object file for each source file.
```

So I guess doing that twice WOULD cause the exact error message we are seeing.  Maybe once we fix that, we would still have to fix the ppc64 issue, so (as I say above) I'll keep that in for now. 

```
compile options:
'-I/Applications/sage_builds/numpy/sage-4.6.alpha2/local/lib/python2.6/site-packages/numpy/core/include
-c'
```

And then the usual `-c` is added.  So where does this one come from?  In the Numpy install I see

```
C compiler: gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes

compile options: '-Inumpy/core/src/private -Inumpy/core/src -Inumpy/core -Inumpy/core/src/npymath -Inumpy/core/src/multiarray -Inumpy/core/src/umath -Inumpy/core/include -I/Users/karl-dietercrisman/Downloads/sage-4.6.alpha3/local/include/python2.6 -c'
```

so at least sometimes it's okay to have `-c` in the compile options.  But I haven't got a clue where that string is set.

Also, there were two syntax errors in my initial change - here is the corrected one:

```
if [ `uname` = "Darwin" ]; then
    VER=`uname -r | sed 's/\([0-9]*\)\..*/\1/'`
    if [ $VER -ge 10 ]; then
        cp ../patches/gnu-changes.py numpy/distutils/fcompiler/gnu.py
    fi
fi
```




---

archive/issue_comments_096694.json:
```json
{
    "body": "Replying to [comment:269 kcrisman]:\n> Replying to [comment:265 fbissey]:\n> > So I looked at the special build instructions and right now they should be amended to\n> > {{{\n> > Special Update/Build Instructions:\n> >   * Scipy uses numpy's distutils to control its compilation of fortran code.\n> >     Whenever numpy is updated it is necessary to make sure that scipy still builds ok. \n> > }}}\n> > And that's it. The rest is obsolete. I should review what we have done to make sure there are no other - new instructions that should be given.\n> \n> That includes the business about\n> {{{\n> The file $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi comes from this file\n> }}}\n> and so on? I just want to confirm this is also obsolete.\nIt was obsolete before we started working with the spkg. It should have been removed\nin 1.3.1 if not before.",
    "created_at": "2010-10-13T17:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96694",
    "user": "@kiwifb"
}
```

Replying to [comment:269 kcrisman]:
> Replying to [comment:265 fbissey]:
> > So I looked at the special build instructions and right now they should be amended to
> > {{{
> > Special Update/Build Instructions:
> >   * Scipy uses numpy's distutils to control its compilation of fortran code.
> >     Whenever numpy is updated it is necessary to make sure that scipy still builds ok. 
> > }}}
> > And that's it. The rest is obsolete. I should review what we have done to make sure there are no other - new instructions that should be given.
> 
> That includes the business about
> {{{
> The file $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi comes from this file
> }}}
> and so on? I just want to confirm this is also obsolete.
It was obsolete before we started working with the spkg. It should have been removed
in 1.3.1 if not before.



---

archive/issue_comments_096695.json:
```json
{
    "body": "You are OK with the bash shell, but it is **very** unportable to have no space before the left bracket. That will break with many shells, so is not a good habit to get into. \n\nSee example below:\n\n\n```\n-bash-3.00$ cat bad\n#!/bin/sh\nif [ `uname` = \"Darwin\"]; then\n  echo \"This is OS X\"\nfi\n-bash-3.00$ ./bad\n./bad: test: ] missing\n```\n\n\nNow just add a space:\n\n\n```\n-bash-3.00$ cat good\n#!/bin/sh\nif [ `uname` = \"Darwin\" ]; then\n  echo \"This is OS X\"\nfi\n-bash-3.00$ ./good\n-bash-3.00$ \n```\n\n\nSince this was a Solaris system, not OS X, `good` did **not** print it was OS X. \n\n\n```\n-bash-3.00$ uname\nSunOS\n```\n\n\nJust like Python, different people have different styles, and some are more portable than others. But that lack of a space is particular troublesome.\n\nDave",
    "created_at": "2010-10-13T18:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96695",
    "user": "drkirkby"
}
```

You are OK with the bash shell, but it is **very** unportable to have no space before the left bracket. That will break with many shells, so is not a good habit to get into. 

See example below:


```
-bash-3.00$ cat bad
#!/bin/sh
if [ `uname` = "Darwin"]; then
  echo "This is OS X"
fi
-bash-3.00$ ./bad
./bad: test: ] missing
```


Now just add a space:


```
-bash-3.00$ cat good
#!/bin/sh
if [ `uname` = "Darwin" ]; then
  echo "This is OS X"
fi
-bash-3.00$ ./good
-bash-3.00$ 
```


Since this was a Solaris system, not OS X, `good` did **not** print it was OS X. 


```
-bash-3.00$ uname
SunOS
```


Just like Python, different people have different styles, and some are more portable than others. But that lack of a space is particular troublesome.

Dave



---

archive/issue_comments_096696.json:
```json
{
    "body": "Oops, I see you had realised this. Also I note it fails with bash too. \n\nOh well, I'll shut up!!!\n\ndave",
    "created_at": "2010-10-13T18:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96696",
    "user": "drkirkby"
}
```

Oops, I see you had realised this. Also I note it fails with bash too. 

Oh well, I'll shut up!!!

dave



---

archive/issue_comments_096697.json:
```json
{
    "body": "No problem :)  \n\nBut if you know where that extra \"-c\" comes from, please pipe up!  I'm stumped, but then again I know nothing of where such things are originated - presumably there is a typical file where they come from.",
    "created_at": "2010-10-13T19:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96697",
    "user": "@kcrisman"
}
```

No problem :)  

But if you know where that extra "-c" comes from, please pipe up!  I'm stumped, but then again I know nothing of where such things are originated - presumably there is a typical file where they come from.



---

archive/issue_comments_096698.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-14T02:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96698",
    "user": "@kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096699.json:
```json
{
    "body": "Okay, I went back to John's initial idea and just removed the ppc64 option. I'm still totally mystified as to why that would solve it per se, if the double `-c` option is really a problem, but oh well - ppc64 is the problem.  \n\nSo I have now changed the description yet again to point us to a numpy spkg at my sage account.  Try it out.  I will now also attach diffs for reference about this.  Notice that I only attach the changed gnu.py file on Snow Leopard, so this should presumably only change anything on there.",
    "created_at": "2010-10-14T02:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96699",
    "user": "@kcrisman"
}
```

Okay, I went back to John's initial idea and just removed the ppc64 option. I'm still totally mystified as to why that would solve it per se, if the double `-c` option is really a problem, but oh well - ppc64 is the problem.  

So I have now changed the description yet again to point us to a numpy spkg at my sage account.  Try it out.  I will now also attach diffs for reference about this.  Notice that I only attach the changed gnu.py file on Snow Leopard, so this should presumably only change anything on there.



---

archive/issue_comments_096700.json:
```json
{
    "body": "Patch to src/numpy/distutils/fcompiler/gnu.py",
    "created_at": "2010-10-14T02:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96700",
    "user": "@kcrisman"
}
```

Patch to src/numpy/distutils/fcompiler/gnu.py



---

archive/issue_comments_096701.json:
```json
{
    "body": "Attachment [gnu-changes.patch](tarball://root/attachments/some-uuid/ticket9808/gnu-changes.patch) by drkirkby created at 2010-10-14 09:49:00\n\nReplying to [comment:275 kcrisman]:\n> Okay, I went back to John's initial idea and just removed the ppc64 option. I'm still totally mystified as to why that would solve it per se, if the double `-c` option is really a problem, but oh well - ppc64 is the problem.  \n\n\nThere's no reason a double -c should be a problem. There are numerous options that get passed to gcc multiple times. Here's a simple session where I list the files in my directory, and look for the most recent one. \n\n\n```\ndrkirkby@hawk:~$ touch foobar\ndrkirkby@hawk:~$ ls -lrt | tail -1\n-rw-r--r--   1 drkirkby other          8 Oct 14 10:37 foobar\ndrkirkby@hawk:~$ gcc -lm  test.c\ndrkirkby@hawk:~$ ls -lrt | tail -1\n-rwxr-xr-x   1 drkirkby staff       8316 Oct 14 10:38 a.out\ndrkirkby@hawk:~$ gcc -lm -c -c test.c\ndrkirkby@hawk:~$ ls -lrt | tail -1\n-rw-r--r--   1 drkirkby staff       1012 Oct 14 10:38 test.o\ndrkirkby@hawk:~$ \n```\n\n\nWe can see that calling \n\n\n```\ngcc -lm -c -c test.c\n```\n\n\nresulted in the most recent file being an object file (.o) and not an executable a.out. \n\nThe patch you attached is not a Mercurial patch, so could not easily be integrated.",
    "created_at": "2010-10-14T09:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96701",
    "user": "drkirkby"
}
```

Attachment [gnu-changes.patch](tarball://root/attachments/some-uuid/ticket9808/gnu-changes.patch) by drkirkby created at 2010-10-14 09:49:00

Replying to [comment:275 kcrisman]:
> Okay, I went back to John's initial idea and just removed the ppc64 option. I'm still totally mystified as to why that would solve it per se, if the double `-c` option is really a problem, but oh well - ppc64 is the problem.  


There's no reason a double -c should be a problem. There are numerous options that get passed to gcc multiple times. Here's a simple session where I list the files in my directory, and look for the most recent one. 


```
drkirkby@hawk:~$ touch foobar
drkirkby@hawk:~$ ls -lrt | tail -1
-rw-r--r--   1 drkirkby other          8 Oct 14 10:37 foobar
drkirkby@hawk:~$ gcc -lm  test.c
drkirkby@hawk:~$ ls -lrt | tail -1
-rwxr-xr-x   1 drkirkby staff       8316 Oct 14 10:38 a.out
drkirkby@hawk:~$ gcc -lm -c -c test.c
drkirkby@hawk:~$ ls -lrt | tail -1
-rw-r--r--   1 drkirkby staff       1012 Oct 14 10:38 test.o
drkirkby@hawk:~$ 
```


We can see that calling 


```
gcc -lm -c -c test.c
```


resulted in the most recent file being an object file (.o) and not an executable a.out. 

The patch you attached is not a Mercurial patch, so could not easily be integrated.



---

archive/issue_comments_096702.json:
```json
{
    "body": "> There's no reason a double -c should be a problem. There are numerous options that get passed to gcc multiple times. Here's a simple session where I list the files in my directory, and look for the most recent one. \nThis example just shows I am totally clueless.   So that couldn't have caused the problem?\n\n> The patch you attached is not a Mercurial patch, so could not easily be integrated. \nIt wasn't intended to be integrated - it was just intended to be viewed.  It is already part of the (correctly integrated, I think) patch in the actual spkg in the description, which is [here](http://sage.math.washington.edu/home/kcrisman/numpy-1.5.0.spkg).\n\nAnyway, all long doctests pass with this on my 10.6 Snow Leopard computer.  And the change to spkg-install are exactly the same, so in theory this is the only platform it should affect, meaning all other review should work.   As I said, though, I don't feel comfortable giving it final positive review.\n\nWill this ticket reach 300 comments?",
    "created_at": "2010-10-14T12:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96702",
    "user": "@kcrisman"
}
```

> There's no reason a double -c should be a problem. There are numerous options that get passed to gcc multiple times. Here's a simple session where I list the files in my directory, and look for the most recent one. 
This example just shows I am totally clueless.   So that couldn't have caused the problem?

> The patch you attached is not a Mercurial patch, so could not easily be integrated. 
It wasn't intended to be integrated - it was just intended to be viewed.  It is already part of the (correctly integrated, I think) patch in the actual spkg in the description, which is [here](http://sage.math.washington.edu/home/kcrisman/numpy-1.5.0.spkg).

Anyway, all long doctests pass with this on my 10.6 Snow Leopard computer.  And the change to spkg-install are exactly the same, so in theory this is the only platform it should affect, meaning all other review should work.   As I said, though, I don't feel comfortable giving it final positive review.

Will this ticket reach 300 comments?



---

archive/issue_comments_096703.json:
```json
{
    "body": "Attachment [last-spkg-install-changes.patch](tarball://root/attachments/some-uuid/ticket9808/last-spkg-install-changes.patch) by @kcrisman created at 2010-10-14 12:19:38\n\nFor reference only - OS X 10.6 fix in spkg-install",
    "created_at": "2010-10-14T12:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96703",
    "user": "@kcrisman"
}
```

Attachment [last-spkg-install-changes.patch](tarball://root/attachments/some-uuid/ticket9808/last-spkg-install-changes.patch) by @kcrisman created at 2010-10-14 12:19:38

For reference only - OS X 10.6 fix in spkg-install



---

archive/issue_comments_096704.json:
```json
{
    "body": "Replying to [comment:271 fbissey]:\n> Replying to [comment:269 kcrisman]:\n> > Replying to [comment:265 fbissey]:\n> > > So I looked at the special build instructions and right now they should be amended to\n> > > {{{\n> > > Special Update/Build Instructions:\n> > >   * Scipy uses numpy's distutils to control its compilation of fortran code.\n> > >     Whenever numpy is updated it is necessary to make sure that scipy still builds ok. \n> > > }}}\n> > > And that's it. The rest is obsolete. I should review what we have done to make sure there are no other - new instructions that should be given.\n> > \n> > That includes the business about\n> > {{{\n> > The file $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi comes from this file\n> > }}}\n> > and so on? I just want to confirm this is also obsolete.\n> It was obsolete before we started working with the spkg. It should have been removed\n> in 1.3.1 if not before.\n\nSorry that's my fault. I had realized it, but then forgot to remove it...",
    "created_at": "2010-10-14T13:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96704",
    "user": "maldun"
}
```

Replying to [comment:271 fbissey]:
> Replying to [comment:269 kcrisman]:
> > Replying to [comment:265 fbissey]:
> > > So I looked at the special build instructions and right now they should be amended to
> > > {{{
> > > Special Update/Build Instructions:
> > >   * Scipy uses numpy's distutils to control its compilation of fortran code.
> > >     Whenever numpy is updated it is necessary to make sure that scipy still builds ok. 
> > > }}}
> > > And that's it. The rest is obsolete. I should review what we have done to make sure there are no other - new instructions that should be given.
> > 
> > That includes the business about
> > {{{
> > The file $SAGE_ROOT/devel/sage/sage/ext/numpy.pxi comes from this file
> > }}}
> > and so on? I just want to confirm this is also obsolete.
> It was obsolete before we started working with the spkg. It should have been removed
> in 1.3.1 if not before.

Sorry that's my fault. I had realized it, but then forgot to remove it...



---

archive/issue_comments_096705.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-14T14:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96705",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096706.json:
```json
{
    "body": "I built this on a unix box (eno), an OS X 10.6 box, an OpenSolaris box (hawk), and a Solaris on x86 box (fulvia).  (By \"built\", I mean I built from scratch based on Sage 4.6.alpha3, replacing the numpy and scipy packages with the ones on this ticket, and I also applied the doctest patch.)\n\n- On some machines, the doctest patch didn't apply cleanly: the patch to doc/en/faq/faq-usage.rst didn't apply, because it seems to already have been applied.  Maybe the tar file for 4.6.alpha3 changed?  The patch didn't apply cleanly on the machines where I downloaded it more recently.\n- On linux, all tests passed.\n- On Mac and OpenSolaris, two doctest failures:\n\n```\nsage -t  -long -force_lib devel/sage/sage/matrix/matrix1.pyx\n**********************************************************************\nFile \"/Applications/sage_builds/numpy/sage-4.6.alpha3/devel/sage-main/sage/matrix/matrix1.pyx\", line 448:\n    sage: sorted(numpy.typecodes.items())\nExpected:\n    [('All', '?bhilqpBHILQPfdgFDGSUVOMm'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Datetime', 'Mm'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]\nGot:\n    [('All', '?bhilqpBHILQPfdgFDGSUVO'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]\n**********************************************************************\n```\n\n and\n\n```\nsage -t  -long -force_lib devel/sage/sage/misc/citation.pyx\n**********************************************************************\nFile \"/Applications/sage_builds/numpy/sage-4.6.alpha3/devel/sage-main/sage/misc/citation.pyx\", line 60:\n    sage: get_systems('integrate(x^2, x)')\nExpected:\n    ['ginac', 'Maxima']\nGot:\n    ['numpy', 'ginac', 'Maxima']\n**********************************************************************\nFile \"/Applications/sage_builds/numpy/sage-4.6.alpha3/devel/sage-main/sage/misc/citation.pyx\", line 64:\n    sage: get_systems('I.primary_decomposition()')\nExpected:\n    ['Singular']\nGot:\n    ['Singular', 'numpy']\n**********************************************************************\n```\n\n- the bad news: scipy doesn't build on fulvia. After listing all of the files extracted, this is basically all of the log file:\n\n```\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nCOLLECT_GCC=gcc\nCOLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.1/x86_64-SunOS-core2-sun-ld/libexec/gcc/i386-pc-solaris2.10\\\n/4.5.1/lto-wrapper\nTarget: i386-pc-solaris2.10\nConfigured with: /usr/local/gcc-4.5.1/src/gcc-4.5.1/configure --enable-languages=c,c++,fortran --w\\\nith-gnu-as --with-as=/usr/local/binutils-2.20.1/x86_64-SunOS-core2-gcc-4.4.3/bin/as --with-ld=/usr\\\n/ccs/bin/ld --with-gmp=/usr/local/gmp-5.0.1/x86_64-SunOS-core2-gcc-4.5.0-abi32 --with-mpfr=/usr/lo\\\ncal/mpfr-3.0.0/x86_64-SunOS-core2-gmp-5.0.1-gcc-4.5.0-abi32 --with-mpc=/usr/local/mpc-0.8.2/x86_64\\\n-SunOS-core2-mpfr-3.0.0-gmp-5.0.1-gcc-4.5.0-abi32 --prefix=/usr/local/gcc-4.5.1/x86_64-SunOS-core2\\\n-sun-ld\nThread model: posix\ngcc version 4.5.1 (GCC)\n****************************************************\n./spkg-install: LDFLAGS=-shared: is not an identifier\n```\n",
    "created_at": "2010-10-14T14:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96706",
    "user": "@jhpalmieri"
}
```

I built this on a unix box (eno), an OS X 10.6 box, an OpenSolaris box (hawk), and a Solaris on x86 box (fulvia).  (By "built", I mean I built from scratch based on Sage 4.6.alpha3, replacing the numpy and scipy packages with the ones on this ticket, and I also applied the doctest patch.)

- On some machines, the doctest patch didn't apply cleanly: the patch to doc/en/faq/faq-usage.rst didn't apply, because it seems to already have been applied.  Maybe the tar file for 4.6.alpha3 changed?  The patch didn't apply cleanly on the machines where I downloaded it more recently.
- On linux, all tests passed.
- On Mac and OpenSolaris, two doctest failures:

```
sage -t  -long -force_lib devel/sage/sage/matrix/matrix1.pyx
**********************************************************************
File "/Applications/sage_builds/numpy/sage-4.6.alpha3/devel/sage-main/sage/matrix/matrix1.pyx", line 448:
    sage: sorted(numpy.typecodes.items())
Expected:
    [('All', '?bhilqpBHILQPfdgFDGSUVOMm'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Datetime', 'Mm'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]
Got:
    [('All', '?bhilqpBHILQPfdgFDGSUVO'), ('AllFloat', 'fdgFDG'), ('AllInteger', 'bBhHiIlLqQpP'), ('Character', 'c'), ('Complex', 'FDG'), ('Float', 'fdg'), ('Integer', 'bhilqp'), ('UnsignedInteger', 'BHILQP')]
**********************************************************************
```

 and

```
sage -t  -long -force_lib devel/sage/sage/misc/citation.pyx
**********************************************************************
File "/Applications/sage_builds/numpy/sage-4.6.alpha3/devel/sage-main/sage/misc/citation.pyx", line 60:
    sage: get_systems('integrate(x^2, x)')
Expected:
    ['ginac', 'Maxima']
Got:
    ['numpy', 'ginac', 'Maxima']
**********************************************************************
File "/Applications/sage_builds/numpy/sage-4.6.alpha3/devel/sage-main/sage/misc/citation.pyx", line 64:
    sage: get_systems('I.primary_decomposition()')
Expected:
    ['Singular']
Got:
    ['Singular', 'numpy']
**********************************************************************
```

- the bad news: scipy doesn't build on fulvia. After listing all of the files extracted, this is basically all of the log file:

```
Finished extraction
****************************************************
Host system
uname -a:
SunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.1/x86_64-SunOS-core2-sun-ld/libexec/gcc/i386-pc-solaris2.10\
/4.5.1/lto-wrapper
Target: i386-pc-solaris2.10
Configured with: /usr/local/gcc-4.5.1/src/gcc-4.5.1/configure --enable-languages=c,c++,fortran --w\
ith-gnu-as --with-as=/usr/local/binutils-2.20.1/x86_64-SunOS-core2-gcc-4.4.3/bin/as --with-ld=/usr\
/ccs/bin/ld --with-gmp=/usr/local/gmp-5.0.1/x86_64-SunOS-core2-gcc-4.5.0-abi32 --with-mpfr=/usr/lo\
cal/mpfr-3.0.0/x86_64-SunOS-core2-gmp-5.0.1-gcc-4.5.0-abi32 --with-mpc=/usr/local/mpc-0.8.2/x86_64\
-SunOS-core2-mpfr-3.0.0-gmp-5.0.1-gcc-4.5.0-abi32 --prefix=/usr/local/gcc-4.5.1/x86_64-SunOS-core2\
-sun-ld
Thread model: posix
gcc version 4.5.1 (GCC)
****************************************************
./spkg-install: LDFLAGS=-shared: is not an identifier
```




---

archive/issue_comments_096707.json:
```json
{
    "body": ">  - On some machines, the doctest patch didn't apply cleanly: the patch to doc/en/faq/faq-usage.rst didn't apply, because it seems to already have been applied.  Maybe the tar file for 4.6.alpha3 changed?  The patch didn't apply cleanly on the machines where I downloaded it more recently.\nYeah, I had that problem too at times.\n\n>  - On Mac and OpenSolaris, two doctest failures:\nDid those errors go away upon testing 'by hand'?  Incidentally, I don't think I got these errors on my Mac (Snow Leopard, like yours). \n\n>  - the bad news: scipy doesn't build on fulvia. After listing all of the files extracted, this is basically all of the log file:\n> {{{\n> Finished extraction\n> ****************************************************\n> Host system\n> uname -a:\n> SunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc\n> ****************************************************\n> ****************************************************\n> CC Version\n> gcc -v\n> Using built-in specs.\n> COLLECT_GCC=gcc\n> COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.1/x86_64-SunOS-core2-sun-ld/libexec/gcc/i386-pc-solaris2.10\\\n> /4.5.1/lto-wrapper\n> Target: i386-pc-solaris2.10\n> Configured with: /usr/local/gcc-4.5.1/src/gcc-4.5.1/configure --enable-languages=c,c++,fortran --w\\\n> ith-gnu-as --with-as=/usr/local/binutils-2.20.1/x86_64-SunOS-core2-gcc-4.4.3/bin/as --with-ld=/usr\\\n> /ccs/bin/ld --with-gmp=/usr/local/gmp-5.0.1/x86_64-SunOS-core2-gcc-4.5.0-abi32 --with-mpfr=/usr/lo\\\n> cal/mpfr-3.0.0/x86_64-SunOS-core2-gmp-5.0.1-gcc-4.5.0-abi32 --with-mpc=/usr/local/mpc-0.8.2/x86_64\\\n> -SunOS-core2-mpfr-3.0.0-gmp-5.0.1-gcc-4.5.0-abi32 --prefix=/usr/local/gcc-4.5.1/x86_64-SunOS-core2\\\n> -sun-ld\n> Thread model: posix\n> gcc version 4.5.1 (GCC)\n> ****************************************************\n> ./spkg-install: LDFLAGS=-shared: is not an identifier\n> }}}\nIsn't this basically the same error that fulvia had before with this Scipy?  So nothing has changed there.  You suggested something about \n\n```\n    export LDFLAGS=\"-shared\"\n```\n\nbefore, but this is now quoted in the spkg-install already, assuming you used the one on kirkby's account.\n\nI assume fulvia is a machine which already has \"official\" support?",
    "created_at": "2010-10-14T14:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96707",
    "user": "@kcrisman"
}
```

>  - On some machines, the doctest patch didn't apply cleanly: the patch to doc/en/faq/faq-usage.rst didn't apply, because it seems to already have been applied.  Maybe the tar file for 4.6.alpha3 changed?  The patch didn't apply cleanly on the machines where I downloaded it more recently.
Yeah, I had that problem too at times.

>  - On Mac and OpenSolaris, two doctest failures:
Did those errors go away upon testing 'by hand'?  Incidentally, I don't think I got these errors on my Mac (Snow Leopard, like yours). 

>  - the bad news: scipy doesn't build on fulvia. After listing all of the files extracted, this is basically all of the log file:
> {{{
> Finished extraction
> ****************************************************
> Host system
> uname -a:
> SunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc
> ****************************************************
> ****************************************************
> CC Version
> gcc -v
> Using built-in specs.
> COLLECT_GCC=gcc
> COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.1/x86_64-SunOS-core2-sun-ld/libexec/gcc/i386-pc-solaris2.10\
> /4.5.1/lto-wrapper
> Target: i386-pc-solaris2.10
> Configured with: /usr/local/gcc-4.5.1/src/gcc-4.5.1/configure --enable-languages=c,c++,fortran --w\
> ith-gnu-as --with-as=/usr/local/binutils-2.20.1/x86_64-SunOS-core2-gcc-4.4.3/bin/as --with-ld=/usr\
> /ccs/bin/ld --with-gmp=/usr/local/gmp-5.0.1/x86_64-SunOS-core2-gcc-4.5.0-abi32 --with-mpfr=/usr/lo\
> cal/mpfr-3.0.0/x86_64-SunOS-core2-gmp-5.0.1-gcc-4.5.0-abi32 --with-mpc=/usr/local/mpc-0.8.2/x86_64\
> -SunOS-core2-mpfr-3.0.0-gmp-5.0.1-gcc-4.5.0-abi32 --prefix=/usr/local/gcc-4.5.1/x86_64-SunOS-core2\
> -sun-ld
> Thread model: posix
> gcc version 4.5.1 (GCC)
> ****************************************************
> ./spkg-install: LDFLAGS=-shared: is not an identifier
> }}}
Isn't this basically the same error that fulvia had before with this Scipy?  So nothing has changed there.  You suggested something about 

```
    export LDFLAGS="-shared"
```

before, but this is now quoted in the spkg-install already, assuming you used the one on kirkby's account.

I assume fulvia is a machine which already has "official" support?



---

archive/issue_comments_096708.json:
```json
{
    "body": "Replying to [comment:280 kcrisman]:\n \n> >  - On Mac and OpenSolaris, two doctest failures:\n> Did those errors go away upon testing 'by hand'?  Incidentally, I don't think I got these errors on my Mac (Snow Leopard, like yours). \n\nOn the Mac, the citation.pyx failure went away when done by hand, but not the matrix1.pyx failure.  On OpenSolaris, both are repeatable by hand.\n\n> >  - the bad news: scipy doesn't build on fulvia. After listing all of the files extracted, this is basically all of the log file:\n\n> Isn't this basically the same error that fulvia had before with this Scipy?  So nothing has changed there.  You suggested something about \n> {{{\n>     export LDFLAGS=\"-shared\"\n> }}}\n> before, but this is now quoted in the spkg-install already, assuming you used the one on kirkby's account.\n\nIn fact, it was already there before I made the suggestion.  I think the suggestion [above](http://trac.sagemath.org/sage_trac/ticket/9808?replyto=280#comment:172) about changing the first line of spkg-install from \"/bin/sh\" to \"/usr/bin/env bash\" might work, and I hope it won't break on any other platforms.  I'll prepare a new spkg later today.\n\n> I assume fulvia is a machine which already has \"official\" support?  \n\nTo the extent that this concept is defined, I would say yes.  Sage should build on all of the skynet machines, and fulvia is one of those.",
    "created_at": "2010-10-14T15:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96708",
    "user": "@jhpalmieri"
}
```

Replying to [comment:280 kcrisman]:
 
> >  - On Mac and OpenSolaris, two doctest failures:
> Did those errors go away upon testing 'by hand'?  Incidentally, I don't think I got these errors on my Mac (Snow Leopard, like yours). 

On the Mac, the citation.pyx failure went away when done by hand, but not the matrix1.pyx failure.  On OpenSolaris, both are repeatable by hand.

> >  - the bad news: scipy doesn't build on fulvia. After listing all of the files extracted, this is basically all of the log file:

> Isn't this basically the same error that fulvia had before with this Scipy?  So nothing has changed there.  You suggested something about 
> {{{
>     export LDFLAGS="-shared"
> }}}
> before, but this is now quoted in the spkg-install already, assuming you used the one on kirkby's account.

In fact, it was already there before I made the suggestion.  I think the suggestion [above](http://trac.sagemath.org/sage_trac/ticket/9808?replyto=280#comment:172) about changing the first line of spkg-install from "/bin/sh" to "/usr/bin/env bash" might work, and I hope it won't break on any other platforms.  I'll prepare a new spkg later today.

> I assume fulvia is a machine which already has "official" support?  

To the extent that this concept is defined, I would say yes.  Sage should build on all of the skynet machines, and fulvia is one of those.



---

archive/issue_comments_096709.json:
```json
{
    "body": "Replying to [comment:279 jhpalmieri]:\n> I built this on a unix box (eno), an OS X 10.6 box, an OpenSolaris box (hawk), and a Solaris on x86 box (fulvia).  (By \"built\", I mean I built from scratch based on Sage 4.6.alpha3, replacing the numpy and scipy packages with the ones on this ticket, and I also applied the doctest patch.)\n> \n>  - On some machines, the doctest patch didn't apply cleanly: the patch to doc/en/faq/faq-usage.rst didn't apply, because it seems to already have been applied.  Maybe the tar file for 4.6.alpha3 changed?  The patch didn't apply cleanly on the machines where I downloaded it more recently.\n\nStrange I tested the patch out, and it really didn't work. Then I made a new patch and it worked. So perhaps the file was corrupt. I upload a new version right now. Hope nothing gets corrupted again...\n\n-maldun",
    "created_at": "2010-10-14T18:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96709",
    "user": "maldun"
}
```

Replying to [comment:279 jhpalmieri]:
> I built this on a unix box (eno), an OS X 10.6 box, an OpenSolaris box (hawk), and a Solaris on x86 box (fulvia).  (By "built", I mean I built from scratch based on Sage 4.6.alpha3, replacing the numpy and scipy packages with the ones on this ticket, and I also applied the doctest patch.)
> 
>  - On some machines, the doctest patch didn't apply cleanly: the patch to doc/en/faq/faq-usage.rst didn't apply, because it seems to already have been applied.  Maybe the tar file for 4.6.alpha3 changed?  The patch didn't apply cleanly on the machines where I downloaded it more recently.

Strange I tested the patch out, and it really didn't work. Then I made a new patch and it worked. So perhaps the file was corrupt. I upload a new version right now. Hope nothing gets corrupted again...

-maldun



---

archive/issue_comments_096710.json:
```json
{
    "body": "Attachment [trac_9808_numpy_doctest_change.patch](tarball://root/attachments/some-uuid/ticket9808/trac_9808_numpy_doctest_change.patch) by maldun created at 2010-10-14 18:08:16\n\nChanged doctests for numpy-1.5.0 due to output changes in numpy",
    "created_at": "2010-10-14T18:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96710",
    "user": "maldun"
}
```

Attachment [trac_9808_numpy_doctest_change.patch](tarball://root/attachments/some-uuid/ticket9808/trac_9808_numpy_doctest_change.patch) by maldun created at 2010-10-14 18:08:16

Changed doctests for numpy-1.5.0 due to output changes in numpy



---

archive/issue_comments_096711.json:
```json
{
    "body": "Ok if I download it again I have the same problem. It's really strange. If you look at the file sizes, the uploaded version has 2.7 kb (which the file what works also has), while the downloaded has 4.3 kb.\nSomething strange happens here...",
    "created_at": "2010-10-14T18:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96711",
    "user": "maldun"
}
```

Ok if I download it again I have the same problem. It's really strange. If you look at the file sizes, the uploaded version has 2.7 kb (which the file what works also has), while the downloaded has 4.3 kb.
Something strange happens here...



---

archive/issue_comments_096712.json:
```json
{
    "body": "Did you download the raw or the html version of the patch?",
    "created_at": "2010-10-14T18:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96712",
    "user": "@jasongrout"
}
```

Did you download the raw or the html version of the patch?



---

archive/issue_comments_096713.json:
```json
{
    "body": "The raw, and I'm already suspecting what's going on here: When I download from the wiki trac I get the old version for sage 4.5.3 instead of the new one... I had this problem frequently on several wikis now and it is starting to get on my nerves...\n\ntry this link out: http://computational-sage.googlecode.com/files/trac_9808_numpy_doctest_change.patch\n\nIt's my googlecode repository. Downloading from there works fine.\n\n-maldun",
    "created_at": "2010-10-14T18:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96713",
    "user": "maldun"
}
```

The raw, and I'm already suspecting what's going on here: When I download from the wiki trac I get the old version for sage 4.5.3 instead of the new one... I had this problem frequently on several wikis now and it is starting to get on my nerves...

try this link out: http://computational-sage.googlecode.com/files/trac_9808_numpy_doctest_change.patch

It's my googlecode repository. Downloading from there works fine.

-maldun



---

archive/issue_comments_096714.json:
```json
{
    "body": "New upload of the doctest changes for sage 4.6",
    "created_at": "2010-10-14T18:40:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96714",
    "user": "maldun"
}
```

New upload of the doctest changes for sage 4.6



---

archive/issue_comments_096715.json:
```json
{
    "body": "Attachment [trac_9808_changed_doctests.patch](tarball://root/attachments/some-uuid/ticket9808/trac_9808_changed_doctests.patch) by maldun created at 2010-10-14 18:40:57\n\nOk better solution: new name no probs anymore =)",
    "created_at": "2010-10-14T18:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96715",
    "user": "maldun"
}
```

Attachment [trac_9808_changed_doctests.patch](tarball://root/attachments/some-uuid/ticket9808/trac_9808_changed_doctests.patch) by maldun created at 2010-10-14 18:40:57

Ok better solution: new name no probs anymore =)



---

archive/issue_comments_096716.json:
```json
{
    "body": "Updates: my doctest failure in citation.pyx is a \"red herring\".  In particular, it's not because of the patches here; it's because of a flaw in how the function get_systems works.  Often when I've been testing the packages and patches on this ticket, I've created a new version of sage in a directory called \"numpy\", and get_systems sees that string in the path name and adds \"numpy\" to the systems used by the particular command.  If I rename the directory to something else, then the doctest passes.  So let's not worry about this; at some point, someone can fix get_systems so it ignores the initial chunk of the path name (ignore the parent of SAGE_ROOT, for example).\n\nMy doctest failure in matrix1.pyx is still there.  For some reason, the \"Datetime\" type codes are not there on some systems.  Any ideas why?  I glanced at the install log for numpy, but I didn't see anything suspicious, not that I really know what to look for.  Here's the log from my OS X 10.6 machine, which is one place I see this problem: [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.log](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.log).\n\nFinally, I have a new version of the scipy spkg, which works for me on all of the machines I've tested on: linux, OpenSolaris, Solaris on x86, Mac OS X 10.6.  I'm putting the link in the ticket description, and I'm posting the Mercurial patch -- it's very small.\n\nI'm leaving this as \"needs work\" because of the matrix1.pyx issue, but I think that's the only remaining problem.  Please test the new scipy spkg on other systems to make sure, though.",
    "created_at": "2010-10-14T20:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96716",
    "user": "@jhpalmieri"
}
```

Updates: my doctest failure in citation.pyx is a "red herring".  In particular, it's not because of the patches here; it's because of a flaw in how the function get_systems works.  Often when I've been testing the packages and patches on this ticket, I've created a new version of sage in a directory called "numpy", and get_systems sees that string in the path name and adds "numpy" to the systems used by the particular command.  If I rename the directory to something else, then the doctest passes.  So let's not worry about this; at some point, someone can fix get_systems so it ignores the initial chunk of the path name (ignore the parent of SAGE_ROOT, for example).

My doctest failure in matrix1.pyx is still there.  For some reason, the "Datetime" type codes are not there on some systems.  Any ideas why?  I glanced at the install log for numpy, but I didn't see anything suspicious, not that I really know what to look for.  Here's the log from my OS X 10.6 machine, which is one place I see this problem: [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.log](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.log).

Finally, I have a new version of the scipy spkg, which works for me on all of the machines I've tested on: linux, OpenSolaris, Solaris on x86, Mac OS X 10.6.  I'm putting the link in the ticket description, and I'm posting the Mercurial patch -- it's very small.

I'm leaving this as "needs work" because of the matrix1.pyx issue, but I think that's the only remaining problem.  Please test the new scipy spkg on other systems to make sure, though.



---

archive/issue_comments_096717.json:
```json
{
    "body": "Attachment [trac_9808-scipy.patch](tarball://root/attachments/some-uuid/ticket9808/trac_9808-scipy.patch) by @jhpalmieri created at 2010-10-14 20:24:36\n\nfor reference only: diff between old scipy 0.8 spkg and new one",
    "created_at": "2010-10-14T20:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96717",
    "user": "@jhpalmieri"
}
```

Attachment [trac_9808-scipy.patch](tarball://root/attachments/some-uuid/ticket9808/trac_9808-scipy.patch) by @jhpalmieri created at 2010-10-14 20:24:36

for reference only: diff between old scipy 0.8 spkg and new one



---

archive/issue_comments_096718.json:
```json
{
    "body": "See #10129 for the citation.pyx issue.",
    "created_at": "2010-10-14T20:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96718",
    "user": "@jhpalmieri"
}
```

See #10129 for the citation.pyx issue.



---

archive/issue_comments_096719.json:
```json
{
    "body": "`@`jhpalmieri I looked again on your matrix1.pyx problem, and this really interesting if you look on comment #23 (  http://trac.sagemath.org/sage_trac/ticket/9808#comment:23 ) we already had this change in linux also, but in numpy-1.4.1 and it vanished for numpy-1.5.0 again.\n\nSo whatever happen in Mac OS X it appears like an old numpy output comes up again, and if you look at it carefully it actually isn't really an error, more like that more keywords are available.\n\nSo perhaps it has something to do with the numpy installation of numpy itself on OS X. (perhaps another bug of numpy)",
    "created_at": "2010-10-14T20:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96719",
    "user": "maldun"
}
```

`@`jhpalmieri I looked again on your matrix1.pyx problem, and this really interesting if you look on comment #23 (  http://trac.sagemath.org/sage_trac/ticket/9808#comment:23 ) we already had this change in linux also, but in numpy-1.4.1 and it vanished for numpy-1.5.0 again.

So whatever happen in Mac OS X it appears like an old numpy output comes up again, and if you look at it carefully it actually isn't really an error, more like that more keywords are available.

So perhaps it has something to do with the numpy installation of numpy itself on OS X. (perhaps another bug of numpy)



---

archive/issue_comments_096720.json:
```json
{
    "body": "Replying to [comment:289 maldun]:\n> So whatever happen in Mac OS X it appears like an old numpy output comes up again, and if you look at it carefully it actually isn't really an error, more like that more keywords are available.\n\nIt looked to me like the \"Datetime\" keywords were missing, rather than more being available, but I might be wrong.\n\n> So perhaps it has something to do with the numpy installation of numpy itself on OS X. (perhaps another bug of numpy)\n\nI also see this on OpenSolaris, for what that's worth.\n\nIn any case, it's not a big deal, is it?  Can we just change the doctest somehow?",
    "created_at": "2010-10-14T21:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96720",
    "user": "@jhpalmieri"
}
```

Replying to [comment:289 maldun]:
> So whatever happen in Mac OS X it appears like an old numpy output comes up again, and if you look at it carefully it actually isn't really an error, more like that more keywords are available.

It looked to me like the "Datetime" keywords were missing, rather than more being available, but I might be wrong.

> So perhaps it has something to do with the numpy installation of numpy itself on OS X. (perhaps another bug of numpy)

I also see this on OpenSolaris, for what that's worth.

In any case, it's not a big deal, is it?  Can we just change the doctest somehow?



---

archive/issue_comments_096721.json:
```json
{
    "body": "*lol* I have the picture now: it seemed you installed my old patch which inherits the datetime change which was left  from numpy-1.4.1\n\nIf you try the new patch trac_9808_changed_doctests.patch in the attachement instead of \ntrac_9808_changed_doctests.patch it will work. (look in the patch)\n\nThe one which is at fault here is the wiki: I overrided the file, but the wiki let you download the old patch.\nTry it out: Download both patches, and look at them. The old one has the false filesize and inherits this change what had to be applied to numpy 1.4.1, in the new one this is left out",
    "created_at": "2010-10-14T21:15:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96721",
    "user": "maldun"
}
```

*lol* I have the picture now: it seemed you installed my old patch which inherits the datetime change which was left  from numpy-1.4.1

If you try the new patch trac_9808_changed_doctests.patch in the attachement instead of 
trac_9808_changed_doctests.patch it will work. (look in the patch)

The one which is at fault here is the wiki: I overrided the file, but the wiki let you download the old patch.
Try it out: Download both patches, and look at them. The old one has the false filesize and inherits this change what had to be applied to numpy 1.4.1, in the new one this is left out



---

archive/issue_comments_096722.json:
```json
{
    "body": "Okay, I understand.  I don't know if it's the wiki's fault or mine: I may have just been using an old copy of the patch file which I had on my computer.  Anyway, I'm trying again now.  I've marked this \"needs review\", but things are looking pretty good now.",
    "created_at": "2010-10-14T21:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96722",
    "user": "@jhpalmieri"
}
```

Okay, I understand.  I don't know if it's the wiki's fault or mine: I may have just been using an old copy of the patch file which I had on my computer.  Anyway, I'm trying again now.  I've marked this "needs review", but things are looking pretty good now.



---

archive/issue_comments_096723.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-14T21:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96723",
    "user": "@jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096724.json:
```json
{
    "body": "With the new spkgs and the new patch, all tests pass for me (except for known unrelated failures) on skynet machines eno (linux), lena (linux), and fulvia (Solaris on x86).  The build on mark (Solaris on sparc) is ongoing; it's a very slow machine.  All tests also pass on my OS X 10.6 box and on Dave Kirkby's OpenSolaris machine hawk, as well as on sage.math.\n\nIs this enough for a positive review?  I guess not quite: since I prepared the most recent scipy spkg, someone else should definitely review the changes (given in attachment:trac_9808-scipy.patch) and test it out.",
    "created_at": "2010-10-15T04:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96724",
    "user": "@jhpalmieri"
}
```

With the new spkgs and the new patch, all tests pass for me (except for known unrelated failures) on skynet machines eno (linux), lena (linux), and fulvia (Solaris on x86).  The build on mark (Solaris on sparc) is ongoing; it's a very slow machine.  All tests also pass on my OS X 10.6 box and on Dave Kirkby's OpenSolaris machine hawk, as well as on sage.math.

Is this enough for a positive review?  I guess not quite: since I prepared the most recent scipy spkg, someone else should definitely review the changes (given in attachment:trac_9808-scipy.patch) and test it out.



---

archive/issue_comments_096725.json:
```json
{
    "body": "I was able to successfully install both packages on my slowest PPC OS X system; doing ./sage -b after touching the include will take a while, and I would have to wait until Monday to do all tests.  But I will at least test devel/sage/sage/matrix/, devel/sage/sage/functions/, devel/sage/sage/finance/, and devel/sage/sage/numerical, because those use Scipy and Numpy a lot and are NOT eons to test.  \n\nCertainly the patch makes sense.  I can't check now whether the spkg was correctly created and whether it has any changes not checked in, but assuming all is well, this should be considered a successful, if long, process.   And I hope 1.5.1 won't come out the day after - though it looks like the Enthought folks are already looking to 2.0 as well.",
    "created_at": "2010-10-15T15:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96725",
    "user": "@kcrisman"
}
```

I was able to successfully install both packages on my slowest PPC OS X system; doing ./sage -b after touching the include will take a while, and I would have to wait until Monday to do all tests.  But I will at least test devel/sage/sage/matrix/, devel/sage/sage/functions/, devel/sage/sage/finance/, and devel/sage/sage/numerical, because those use Scipy and Numpy a lot and are NOT eons to test.  

Certainly the patch makes sense.  I can't check now whether the spkg was correctly created and whether it has any changes not checked in, but assuming all is well, this should be considered a successful, if long, process.   And I hope 1.5.1 won't come out the day after - though it looks like the Enthought folks are already looking to 2.0 as well.



---

archive/issue_comments_096726.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-15T16:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96726",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096727.json:
```json
{
    "body": "Okay, these tests (which are most of the numpy/scipy ones in Sage, though not all) are passing fine, with the expected errors (I didn't apply the patch, but am seeing precisely what is in the patch).  Great!\n\nI also checked this now\n\n```\nCreating Sage package scipy-0.8/\n\nCreated package scipy-0.8.spkg.\n\n    NAME: scipy\n VERSION: 0.8\n    SIZE: 4.6M\n HG REPO: Good\nSPKG.txt: Good\n```\n\nfrom the latest package John posted.  Positive review!",
    "created_at": "2010-10-15T16:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96727",
    "user": "@kcrisman"
}
```

Okay, these tests (which are most of the numpy/scipy ones in Sage, though not all) are passing fine, with the expected errors (I didn't apply the patch, but am seeing precisely what is in the patch).  Great!

I also checked this now

```
Creating Sage package scipy-0.8/

Created package scipy-0.8.spkg.

    NAME: scipy
 VERSION: 0.8
    SIZE: 4.6M
 HG REPO: Good
SPKG.txt: Good
```

from the latest package John posted.  Positive review!



---

archive/issue_comments_096728.json:
```json
{
    "body": "Replying to [comment:296 kcrisman]:\n\n> from the latest package John posted.  Positive review!\n\nI've never thought I will read those words... I think I need a beer now 8)\n\nThe patch also works on Sage-4.6.alpha3 on Ubuntu. (Which was expected, but it is better to check too often then one time too less)\n\nThanks to everyone who worked on this ticket! I'm quite the beginner, but I think I learned a lot by helping upgrading numpy and can finally going back working on #9706 which should be a lot easier, but I needed the update to complete this task, because the new scipy holds a lot new features for orthogonal polynomials.\nHope I didn't cause too much grey hairs!\n\nKind regards,\nStefan aka maldun",
    "created_at": "2010-10-15T17:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96728",
    "user": "maldun"
}
```

Replying to [comment:296 kcrisman]:

> from the latest package John posted.  Positive review!

I've never thought I will read those words... I think I need a beer now 8)

The patch also works on Sage-4.6.alpha3 on Ubuntu. (Which was expected, but it is better to check too often then one time too less)

Thanks to everyone who worked on this ticket! I'm quite the beginner, but I think I learned a lot by helping upgrading numpy and can finally going back working on #9706 which should be a lot easier, but I needed the update to complete this task, because the new scipy holds a lot new features for orthogonal polynomials.
Hope I didn't cause too much grey hairs!

Kind regards,
Stefan aka maldun



---

archive/issue_comments_096729.json:
```json
{
    "body": "Kudos to you guys!  \n\n(and 3 more comments to reach 300!)",
    "created_at": "2010-10-15T17:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96729",
    "user": "@jasongrout"
}
```

Kudos to you guys!  

(and 3 more comments to reach 300!)



---

archive/issue_comments_096730.json:
```json
{
    "body": "Congratulations, I got exhausted just trying to follow this!",
    "created_at": "2010-10-23T14:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96730",
    "user": "mhampton"
}
```

Congratulations, I got exhausted just trying to follow this!



---

archive/issue_comments_096731.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96731",
    "user": "@jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_096732.json:
```json
{
    "body": "Replying to [comment:266 jhpalmieri]:\n> Replying to [comment:264 fbissey]:\n> > Better use plain 'uname' as it should return Darwin for you if I am not mistaken.\n> \n> No, the point is you want to test not only for Darwin, but for Darwin version 10.6, as opposed to 10.5 or 10.4.  `uname -r` should return strings like 10.4.0, 9.3.1, and 8.8.0, respectively, for these (I think).  (The last parts of the string, like 4.0 or 3.1 or 8.0, are the minor version numbers, which I don't think we care about.)\n> \n> This seems to work for me, but I'm not a sed expert:\n\n```\nVER=`uname -r | sed 's/\\([0-9]*\\)\\..*/\\1/'`\n```\n\n> (This takes the output from uname -r, sends it to sed, which does a regular expression match to return the digits found before the first period.)  Then you do something like\n\n```\nif [ $VER -ge 10 ]; then\n   ...\nfi\n```\n\n> (Might as well test whether VER is at least 10, rather than equal to 10 on the nose.)\n\nJust for the record:\n\nThe easiest (and by the way more efficient and less error-prone) way to test for e.g. Darwin 8 / MacOS X 10.4 / Tiger is to use the (Bourne) shell's built-in pattern matching:\n\n```sh\ncase \"$UNAME\" in # set in sage-env\n    Darwin)\n        case \"`uname -r`\" in # quotes not mandatory\n            8*) # Tiger / 10.4\n                ...\n                ;;\n            9*) # Leopard / 10.5\n                ...\n                ;;\n            10*) # Snow Leopard / 10.6\n                ...\n                ;;\n            *)  # other, \"default\"\n                ...\n        esac\n    # add other OSs like Linux here if appropriate\nesac\n```\n\nOr, if you want to use `sed` or `tr`, something like:\n\n```sh\nos_with_ver=`uname -sr | sed -e 's/ /-/g'` # order of options to 'uname' doesn't matter\n\nos_with_ver_and_arch=`uname -srm | tr ' ' '-'` # using the simpler 'tr'(anslate) command\n\ncase $os_with_ver in\n    Darwin-8*) # Tiger / Darwin 8 / MacOS X 10.4\n        ...\n        ;;\n    ...\nesac\n\n# More specific:\ncase $os_with_ver_and_arch in\n    Darwin-8*-ppc) # Tiger / Darwin 8 / MacOS X 10.4 on PPC (32-bit)\n        ...\n        ;;\n    Darwin-9*-ppc64) # Leopard / Darwin 9 / MacOS X 10.5 on PPC (64-bit)\n        ...\n        ;;\n    Linux-*-x86_64|Linux-*-ia64) # Any 64-bit Linux version on Intel\n        ...\n        ;;\n    Linux-*-i[3456]86) # Any 32-bit Linux version on Intel\n        ...\n        ;;\n    ...\nesac\n```\n",
    "created_at": "2010-11-02T00:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9807#issuecomment-96732",
    "user": "@nexttime"
}
```

Replying to [comment:266 jhpalmieri]:
> Replying to [comment:264 fbissey]:
> > Better use plain 'uname' as it should return Darwin for you if I am not mistaken.
> 
> No, the point is you want to test not only for Darwin, but for Darwin version 10.6, as opposed to 10.5 or 10.4.  `uname -r` should return strings like 10.4.0, 9.3.1, and 8.8.0, respectively, for these (I think).  (The last parts of the string, like 4.0 or 3.1 or 8.0, are the minor version numbers, which I don't think we care about.)
> 
> This seems to work for me, but I'm not a sed expert:

```
VER=`uname -r | sed 's/\([0-9]*\)\..*/\1/'`
```

> (This takes the output from uname -r, sends it to sed, which does a regular expression match to return the digits found before the first period.)  Then you do something like

```
if [ $VER -ge 10 ]; then
   ...
fi
```

> (Might as well test whether VER is at least 10, rather than equal to 10 on the nose.)

Just for the record:

The easiest (and by the way more efficient and less error-prone) way to test for e.g. Darwin 8 / MacOS X 10.4 / Tiger is to use the (Bourne) shell's built-in pattern matching:

```sh
case "$UNAME" in # set in sage-env
    Darwin)
        case "`uname -r`" in # quotes not mandatory
            8*) # Tiger / 10.4
                ...
                ;;
            9*) # Leopard / 10.5
                ...
                ;;
            10*) # Snow Leopard / 10.6
                ...
                ;;
            *)  # other, "default"
                ...
        esac
    # add other OSs like Linux here if appropriate
esac
```

Or, if you want to use `sed` or `tr`, something like:

```sh
os_with_ver=`uname -sr | sed -e 's/ /-/g'` # order of options to 'uname' doesn't matter

os_with_ver_and_arch=`uname -srm | tr ' ' '-'` # using the simpler 'tr'(anslate) command

case $os_with_ver in
    Darwin-8*) # Tiger / Darwin 8 / MacOS X 10.4
        ...
        ;;
    ...
esac

# More specific:
case $os_with_ver_and_arch in
    Darwin-8*-ppc) # Tiger / Darwin 8 / MacOS X 10.4 on PPC (32-bit)
        ...
        ;;
    Darwin-9*-ppc64) # Leopard / Darwin 9 / MacOS X 10.5 on PPC (64-bit)
        ...
        ;;
    Linux-*-x86_64|Linux-*-ia64) # Any 64-bit Linux version on Intel
        ...
        ;;
    Linux-*-i[3456]86) # Any 32-bit Linux version on Intel
        ...
        ;;
    ...
esac
```

