# Issue 9807: Upgrade numpy to 1.5b and scipy to 0.8

Issue created by migration from Trac.

Original creator: maldun

Original creation time: 2010-08-26 19:10:38

Assignee: maldun

Keywords: numpy, scipy

Since I really, really need them for my work, I will try to manage it to upgrade the scipy and numpy packages to the latest versions


---

Comment by maldun created at 2010-08-26 22:23:40

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

Comment by maldun created at 2010-08-26 22:23:40

Changing status from new to needs_work.


---

Comment by maldun created at 2010-08-26 23:26:22

numpy 1.5.0rc1: http://www.megaupload.com/?d=KK31RSZV


---

Comment by mhansen created at 2010-08-27 03:48:14

I don't think that we should upgrade to 1.5.0rc1 -- we should do 1.4.1 for now and wait until 1.5 is released.


---

Comment by fbissey created at 2010-08-27 04:59:26

Replying to [comment:3 mhansen]:
> I don't think that we should upgrade to 1.5.0rc1 -- we should do 1.4.1 for now and wait until 1.5 is released.

That has to be double checked but maldun says he needs features in 1.5.
It may be that the features he wants are 1.4.x and he doesn't know.
Do we know roughly when 1.5 will be released? They are at 1.5rc1 9 days after beta2
so it could very well be upon us in a very short time.


---

Comment by maldun created at 2010-08-27 07:11:59

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

Comment by drkirkby created at 2010-08-27 11:24:07

If 1.5.0rc1 is merged, #7166 can be closed. I don't know about 1.4.1, but in any case that is not a critical bug. 

Some time back I made a Solaris-specific change to Numpy, as I wanted to get it reviewed with the least hassle - that generally means making it Solaris specific, as reviewers are easier to please if it only effects a rarer platform. 

But I think the change should be implemented on OS X too. Currently there's a really nasty hack on OS X to build Numpy, that involves a script called `fake_gcc`, copying that to `$SAGE/LOCAL/bin/gcc`, then using the fake gcc to build Numpy. Finally this fake gcc file gets deleted. 

The far neater option is the way I did it on Solaris. I suggest the changes I made for Solaris are implemented whenever `SAGE64` is set to "yes", irrespective of whatever platform it may be. Then all this fake gcc rubbish can be removed. 

If you want, I can create a patch.


---

Comment by maldun created at 2010-08-27 15:24:06

Replying to [comment:6 drkirkby]:
 
> 
> If you want, I can create a patch. 

would be nice! But first I have to sort some things out, I hope it will get ready soon...


---

Comment by fbissey created at 2010-08-29 11:21:20

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
	if [This is the Trac macro *${CHOST} != *-darwin* * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#${CHOST} != *-darwin* -macro) ; then
		append-ldflags -shared
	fi

	# only one fortran to link with:
	# linking with cblas and lapack library will force
	# autodetecting and linking to all available fortran compilers
	use lapack || return
	[This is the Trac macro *-z ${FC} * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-z ${FC} -macro) && FC=$(tc-getFC)
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

Comment by drkirkby created at 2010-08-29 13:18:08

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

*I've not tested the attached patch* - not even on Solaris!! But I think you can see what I am trying to do. I was going to try to explain it in words, but a bit of code, even if untested, should be more sensible.


---

Comment by drkirkby created at 2010-08-29 13:19:26

An untested patch, which makes Numpy build the same was on OS X as it does on Solaris or other platforms where SAGE64=yes. It removes the stupid wrapper script.


---

Attachment

Ok - so we still use g95 on some targets. So we need to keep some patches
just for these - bother.


---

Comment by drkirkby created at 2010-08-30 12:34:07

Replying to [comment:10 fbissey]:
> Ok - so we still use g95 on some targets. So we need to keep some patches
> just for these - bother.
I don't believe g95 is used anywhere. There are g95 binaries in the Fortran package in Sage, but William said they can be removed. There is a gfortran binary. So as far as I'm aware, all g95 stuff can be removed, but `SAGE_FORTRAN` can't be removed. 

Dave


---

Comment by fbissey created at 2010-08-31 10:17:35

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

Comment by jason created at 2010-08-31 16:55:02

FYI: Numpy 1.5 has been officially released now.


---

Comment by jason created at 2010-08-31 16:57:00

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

Comment by fbissey created at 2010-08-31 23:42:19

Replying to [comment:14 jason]:
> I think I was the one that added those instructions, and I'm pretty sure they're obsolete instructions now.  I believe we took care of merging the differences between the two numpy.pxi/pxd files a while ago.

Thank you for the confirmation. I have done some cleaning to numpy's spkg-install and it seems to work as intended on my machine. I guess we'll update to 1.5 and give it a spin.


---

Comment by drkirkby created at 2010-08-31 23:46:35

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

Comment by jason created at 2010-09-01 01:47:56

Replying to [comment:16 drkirkby]:

> In general though, we should not be upgrading to pre-release versions just because one person needs a feature that's only available in a pre-release. Everyone should not have to suffer the extra risks a pre-release gives unless there are compelling arguments for it. 


+1


---

Comment by fbissey created at 2010-09-01 10:01:22

Replying to [comment:16 drkirkby]:
> In general though, we should not be upgrading to pre-release versions just because one person needs a feature that's only available in a pre-release. Everyone should not have to suffer the extra risks a pre-release gives unless there are compelling arguments for it. 
> 
> I realise in this case 1.5 has since been released, so it's immaterial now. 
> 
Yes, I didn't think it would be worth working on that particular version if it wasn't
for the real proximity of the release (curses pari svn upgrade). I would probably
have put pressure for 1.4.1 otherwise (very keen to see numpy upgraded).


---

Comment by maldun created at 2010-09-01 18:39:02

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
maldun`@`zauberbuch:~/sage/sage-4.5.2$ sage -t  -valgrind "devel/sage/sage/rings/polynomial/real_roots.pyx
> "
ERROR: File ./devel/sage/sage/rings/polynomial/real_roots.pyx
 is missing
 
----------------------------------------------------------------------
The following tests failed:


        ./devel/sage/sage/rings/polynomial/real_roots.pyx
 # File not found
Total time for all tests: 0.0 seconds
maldun`@`zauberbuch:~/sage/sage-4.5.2$ sage -t  -valgrind "devel/sage/sage/rings/polynomial/real_roots.pyx"
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

Comment by maldun created at 2010-09-01 20:31:46

Update: Found the problem. see: http://groups.google.com/group/cython-users/browse_thread/thread/624c696293b7fe44

It seems that all versions 1.5.x hold this bug....
Tried downgrading to 1.4.1. and all corrections I have done so far worked.

I will now apply the patch from drkirkby, pack it again, test it overnight and hopefully we are done with 1.4.1, and hopefully they get it right in the next time. perhaps I should send the numpy/scipy guys the doctests I've done so far

scipy 0.8. don't seem to make any problems so far


---

Comment by maldun created at 2010-09-01 21:55:12

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

Comment by fbissey created at 2010-09-01 22:41:23

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

Comment by maldun created at 2010-09-04 00:23:45

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

Comment by maldun created at 2010-09-04 00:23:45

Changing status from needs_work to needs_review.


---

Comment by maldun created at 2010-09-04 00:38:04

One important note: after updating numpy one has to rebuild the source with sage -ba, or else you get runtime warnings.

The reason is the size change in some of the numpy functions, and then the .pyx files have to be rebuild


---

Attachment

modified networkx package (test version)


---

Attachment

changes to networkx, which have to be applied


---

Comment by fbissey created at 2010-09-04 08:43:30

Thanks for the patches. I will probably introduce these in sage-on-gentoo in short order. About networkx, you realize that sage-4.5.3 will use networkx-1.2?
see ticket #9567 
So have you tried to see if networkx-1.2 needs patching (my guess is no, otherwise
I would know by now from gentoo).


---

Comment by maldun created at 2010-09-04 10:05:52

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

Comment by maldun created at 2010-09-04 10:07:08

ith the new versions of numpy/scipy? It is very time consuming for me to rebuild every time the source. Thanx in advance!

sorry I meant new versions of networkx...


---

Comment by fbissey created at 2010-09-04 10:13:48

Understood. We already ship networkx-1.2 with sage-4.5.2 on sage-on-gentoo [because
networkx-1.0.1 has been removed from Gentoo] so I can test your patches along with networkx. It may take 1 or 2 days for me to fit it in my schedule.


---

Comment by maldun created at 2010-09-04 20:15:10

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

Comment by fbissey created at 2010-09-06 09:37:12

It all works in sage-on-gentoo.

However I think there are a few points that should be taken into consideration for both numpy and scipy.
Just before posting my spkg-install I edited it to remove a change that I now think is probably necessary. I had set FC to SAGE_FORTRAN...
Why? Because numpy tries to autodetect a fortran compiler and will take a gnu compiler first. Unless you set FC. Which means if Dave tries to compile sage with sunstudio on a machine that has also gfortran he is in for a world of hurt.
So I think we should either set FC to SAGE_FORTRAN in numpy and possibly scipy. 
The other option is to set it globally but that may cause problems on OSX.

Thoughts? Francois


---

Comment by maldun created at 2010-09-06 10:12:34

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

Comment by maldun created at 2010-09-06 11:18:42

Good news: It seems that the problem from numpy-1.5.0 has been resolved http://projects.scipy.org/numpy/ticket/1605
I don't think it's a big deal. Shall I give it a try, or should we stick to 1.4.1 for now?


---

Comment by maldun created at 2010-09-06 11:24:18

Replying to [comment:35 maldun]:
> Good news: It seems that the problem from numpy-1.5.0 has been resolved http://projects.scipy.org/numpy/ticket/1605
> I don't think it's a big deal. Shall I give it a try, or should we stick to 1.4.1 for now?
...or wait til 1.5.1 is out?


---

Comment by fbissey created at 2010-09-06 11:31:40

May be wait until numpy-1.5.1. it is not a big deal right now I guess.
May be we should discuss it on sage-devel. At the moment we don't really
have much testing apart from the fact I unleashed the upgrade to numpy-1.4.1/scipy-0.8
on sage-on-gentoo users. I am not sure we can believably merge this in 4.5.3 unless
it takes more than one week before it is released. If we target 4.5.3 I say we stay with what we have now, if we target 4.6 which should be a little further down the track we go for 1.5.x.


---

Attachment

newer spkg_install setting FC


---

Comment by fbissey created at 2010-09-06 11:46:08

I updated my spkg_install as you requested. The other thing about using sage_fortran,
that I had forgotten to change back when I removed it, is that it includes "-fPIC".
I didn't check the fortran spkg but hopefully the work done by Dave to set the correct
pic flag is picked up in sage_fortran.

If we don't adopt this, FFLAG="-fPIC" (or whatever mechanism Dave came up with) should be added in my previous version.


---

Comment by maldun created at 2010-09-06 11:51:14

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

Comment by kcrisman created at 2010-09-06 12:56:41

There's a lot of packages etc. on this ticket.  Can someone provide a concise list of what would be needed to apply on a given platform?  (For instance, in a very cursory glance, the networkx package being here mystifies.)


---

Comment by maldun created at 2010-09-06 13:41:20

Replying to [comment:40 kcrisman]:
> There's a lot of packages etc. on this ticket.  Can someone provide a concise list of what would be needed to apply on a given platform?  (For instance, in a very cursory glance, the networkx package being here mystifies.) 

Needed are:
http://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.4.1.spkg   http://code.google.com/p/spkg-upload/downloads/detail?name=scipy-0.8.spkg

after installing numpy, one needs so execute sage -ba, or else one get's runtime warnings.

You also need networkx-1.2. (the other networkx is just a small hack for testing, because 1.2. didn't build correctly on my machine, but this is obsolete now, since networkx-1.2 is merged into sage 4.3.alpha1)


---

Comment by maldun created at 2010-09-06 13:47:18

I gave the links and (current) build instructions into the discription, so that people can find the latest versions more quickly


---

Comment by kcrisman created at 2010-09-06 13:55:00

Included direct links to files in description.


---

Comment by kcrisman created at 2010-09-06 16:08:34

This seems to work fine on Mac OS X 10.6.4 Intel.  I will try to test it tomorrow on a PowerPC machine.  Note: I haven't looked at the spkg installs or anything, this is just a data point with regard to whether it works, not a review.


---

Comment by mhansen created at 2010-09-06 16:59:05

This fails very early on in Cygwin with


```
building library "npymath" sources
creating build/src.cygwin-1.7.5-i686-2.6/src
conv_template:> build/src.cygwin-1.7.5-i686-2.6/src/npy_math.c
error: src/npy_math.c.src: No such file or directory
Error building numpy.
```



---

Comment by maldun created at 2010-09-06 18:38:56

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

Comment by mhansen created at 2010-09-06 19:19:04

I've tested it out, and everything works if you just remove the cygwin-core-setup.py patch.


---

Comment by maldun created at 2010-09-06 19:25:10

Replying to [comment:52 mhansen]:
> I've tested it out, and everything works if you just remove the cygwin-core-setup.py patch.

I was just about to upload a patch...
But great this is even better than my solution! (and simpler)
The reason why it fails is just that cygwin-core-setup.py is outdated.

one question: (because I'm quite the noob...)
If I want to upload a modified version of numpy-1.4.1 do I have to overwrite the old version, or shall I rename it with numpy-1.4.1.p0.spkg?


---

Comment by drkirkby created at 2010-09-06 19:27:06

Replying to [comment:53 maldun]:

> one question: (because I'm quite the noob...)
> If I want to upload a modified version of numpy-1.4.1 do I have to overwrite the old version, or shall I rename it with numpy-1.4.1.p0.spkg?

Overwrite the old one.


---

Comment by maldun created at 2010-09-06 19:41:16

Thanx!
Numpy is now updated with 
 * changes from fbissey to the installer (it worked for me)
 * removed the cygwin-core-setup.py patch


---

Comment by mhansen created at 2010-09-06 20:07:51

The SciPy spkg works fine in Cygwin.


---

Comment by kcrisman created at 2010-09-07 14:05:45

I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?


---

Comment by maldun created at 2010-09-07 14:30:01

Replying to [comment:57 kcrisman]:
> I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?

Yes we did some changes to the spkg-install. But I downloaded and installed the package right now again. So I don't know wehre the problem is lying?


---

Comment by kcrisman created at 2010-09-07 14:54:21

Replying to [comment:58 maldun]:
> Replying to [comment:57 kcrisman]:
> > I'm getting a corrupted package message with the packages right now while trying it on a different system.  Did something get changed with respect to the file with this latest update?
> 
> Yes we did some changes to the spkg-install. But I downloaded and installed the package right now again. So I don't know wehre the problem is lying?
> 

Did you use `sage -pkg` to create it or just do some kind of compression?  I get a message about `tar: this does not look like a file archive` and `tar: Archive contains obsolescent base-64 headers`.  I just installed the optional biopython package on this machine to test things, so the machine shouldn't be the problem (and it built Sage 4.5.2 just fine).


---

Comment by maldun created at 2010-09-07 15:11:04

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

Comment by kcrisman created at 2010-09-07 15:25:25

> Ok I repacked it now with -pkg and uploaded it. Does it work now?
> And sorry for the newby question: what is the difference between -pkg and just compress it?
> Is sage using a different version of tar? Because in fact a spkg is noting else then a tar.gz with different ending.

No, it's a little more than that - it has an SPKG.txt, it has Mercurial repositories, etc.  True that the file type is the same.  But sage -pkg tests several things, and a successful review would check all that.  See [here](http://www.sagemath.org/doc/developer/producing_spkgs.html) for more info.


---

Comment by kcrisman created at 2010-09-07 15:34:43

Hmm, when I open it manually it seems fine.  Though when I run `sage -pkg` on that new folder, I get 

```
HG REPO: Unchecked in changes
```

So you'll need to fix that.   Putting myself as a reviewer now.

Calling `sage -f` on this new spkg I made *does* seem to work, for whatever reason.  This doesn't make sense to me - why is `tar` complaining about yours?  Hopefully someone who knows about file systems will test this soon and explain why this causes a problem on Mac OS X 10.4 Tiger.


---

Comment by kcrisman created at 2010-09-07 15:59:55

Okay, that worked.  Scipy seems to be installing fine directly from the website, I'm not sure why this happened.


---

Comment by maldun created at 2010-09-07 17:07:02

Thanx for the hints!
I updated the mercurial entries now to the latest version.
Uploaded changed packages.
Everything should be fine now


---

Comment by maldun created at 2010-09-07 17:09:28

Replying to [comment:63 kcrisman]:
> Okay, that worked.  Scipy seems to be installing fine directly from the website, I'm not sure why this happened.

I have an Idea: different versions of .tar may cause problems (so far as I know) If you look at the file sizes only it seems that sage does a different kind of compression.


---

Comment by kcrisman created at 2010-09-07 17:21:37

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

Comment by maldun created at 2010-09-07 18:33:56

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

Comment by kcrisman created at 2010-09-07 19:50:27

Sadly, same error.  This is probably on my end, but this is a supported architecture so it's important to know what went wrong.  I don't think that the `./sage -ba` would have anything to do with it.

So I suspect that the "missing: `Python.h` is the problem, as I've seen a few other things about this online (including ones like this one, where /include/Python.h definitely exists, here it's within the `$SAGE_ROOT` directory).  I wonder why it's not finding it this time?


---

Comment by maldun created at 2010-09-07 20:55:54

Replying to [comment:68 kcrisman]:
> Sadly, same error.  This is probably on my end, but this is a supported architecture so it's important to know what went wrong.  I don't think that the `./sage -ba` would have anything to do with it.
> 
> So I suspect that the "missing: `Python.h` is the problem, as I've seen a few other things about this online (including ones like this one, where /include/Python.h definitely exists, here it's within the `$SAGE_ROOT` directory).  I wonder why it's not finding it this time?

Question: Have you tried to give the direct path to the compiler?
And does in OS X gcc points to /include/Python.h because in sage it's /include/python2.6/Python.h ?


---

Comment by kcrisman created at 2010-09-08 00:57:38

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

Comment by fbissey created at 2010-09-08 01:26:50

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

Comment by kcrisman created at 2010-09-08 03:56:05

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

Comment by fbissey created at 2010-09-08 09:40:44

2) would be good to find if this is indeed the problem.
Doing it is another story. Do you have iconv on OSX?
I would think so as it is needed by R amongst other.

so go into the right folder and try:

```
iconv -f UTF-8 -t ISO-8859-1 *.h
```



---

Comment by kcrisman created at 2010-09-08 16:41:06

Same error.


---

Comment by maldun created at 2010-09-08 18:05:26

In the spkg-install, there is the line


```
unset CFLAGS LDFLAGS CXXFLAGS SHAREDFLAGS
```


could this be somehow connected to our problem, because if we unset the flags, gcc doesn't point at Python.h in OS X?


---

Comment by maldun created at 2010-09-08 18:49:26

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

Comment by kcrisman created at 2010-09-08 19:50:57

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

Comment by maldun created at 2010-09-08 22:07:51

I have another wild theory: 
Haven't you said, that the package build one time? And then not. Is this correct?

The only thing I changed was updating the mercurial files, and then commiting. Therefore I had to write the commit messages, and I do this in kate. kate's standard encoding is utf-8. ( My computer's language is german, so everything is utf-8)
This  (or just packing it, because the encoding on my machine is not unicode) did change something to the encoding.
What happens if you untar the package use the iconv from up there, and repack it on your machine?


---

Comment by fbissey created at 2010-09-09 00:50:24

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

Comment by fbissey created at 2010-09-09 02:07:23

Replying to [comment:74 kcrisman]:
> Same error.
It may sound unrelated but what fortran compiler are you using in your
sage install? g95 or gfortran?

In any case I think some of the patches in scipy would need rebasing.
But the fact of the matter is that they are g95 dependent and we dropped
g95 - I already did so in numpy so we should do it as well in scipy.


---

Comment by kcrisman created at 2010-09-09 02:55:00

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

Comment by fbissey created at 2010-09-09 04:13:27

Changing status from needs_review to needs_work.


---

Comment by fbissey created at 2010-09-09 04:13:27

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

Comment by maldun created at 2010-09-09 08:31:45

Replying to [comment:82 fbissey]:

> If numpy fails for you as well on OSX ppc we may have a strong motivation to move to 1.5.0 again.
> 

If you want I can prepare a package for 1.5.0 with the patch from the numpy trac, and run the doctests, in the evening.


---

Comment by kcrisman created at 2010-09-09 12:59:50

Numpy was fine in all cases; Scipy was what didn't build. drkirkby's comment "There are g95 binaries in the Fortran package in Sage, but William said they can be removed." may not be true.

The command that supposedly checks which version I have returns with an error:

```
local/bin/sage_fortran: line 3: sage_fortran.bin: command not found
```

This also happens on my (successful) build of 4.6.prealpha4, so maybe the command is wrong?

Incidentally, does this ticket do anything with respect to #7831 and #8010?  Just curious.


---

Comment by kcrisman created at 2010-09-09 15:04:40

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

Comment by maldun created at 2010-09-09 21:21:41

It would be great if this is the problem and it can somehow be solved!

Another thing: I builded numpy-1.5.0 with the new patch now. There only failed some doctests because numpy is throwing some new warnings.
Want to give it a try? Perhaps the problem is then obsolete with scipy 0.8. also?
I personally would prefer to stick to 1.4.1, but well it is like it is...


---

Comment by kcrisman created at 2010-09-09 22:54:27

If you post it, I can try it - though it might be after the weekend, depending on my physical access to that particular box.

fbissey - can you explain (in layman's terms) how having the wrong fortran compiler might affect things?  It does confuse me :)


---

Comment by maldun created at 2010-09-09 23:23:52

Replying to [comment:87 kcrisman]:
> If you post it, I can try it - though it might be after the weekend, depending on my physical access to that particular box.
> 
> fbissey - can you explain (in layman's terms) how having the wrong fortran compiler might affect things?  It does confuse me :)

Up and ready!

Yes this would be interesting! I don't really get it either because it looks more like a C problem to me?


---

Comment by maldun created at 2010-09-09 23:24:54

http://code.google.com/p/spkg-upload/downloads/detail?name=numpy-1.5.0.spkg&can=2&q=#makechanges


---

Comment by fbissey created at 2010-09-09 23:49:02

It's more of a hunch than anything special I'll admit to that. The numpy/scipy connection seems to be fragile so I am not discounting it. In actual fact the fortran compiler is used only to compile one file in the whole of numpy (lapack_lite.so). I am more worried that it mixes up the toolchain it prepares for scipy.


One thing I'd like to see however is a complete build log for scipy not just the failing bit. There may be clues earlier in the process.


---

Comment by kcrisman created at 2010-09-10 00:21:34

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

Comment by fbissey created at 2010-09-10 00:37:12

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

Comment by kcrisman created at 2010-09-10 00:48:21

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

Comment by fbissey created at 2010-09-10 00:59:12

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

Comment by kcrisman created at 2010-09-10 01:11:41

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

Comment by fbissey created at 2010-09-10 01:24:20

Interestingly enough on Gentoo we have -I/usr/include/python2.6 added to the compilation flags everywhere. I wonder if just finding a way of adding -I${SAGE_LOCAL}/include/python2.6 in sage would help at all. The mystery then
would be "how did it work before?" Furthermore why is it not needed for the earlier
C compilations.... or on other platforms? May be we are using system python headers without knowing it?

I will work on that over the week end. Hopefully by Monday I will have something you can test.


---

Comment by fbissey created at 2010-09-12 22:08:39

It turns out to be more subtle than I thought and I don't know yet why.

It is not easy to add -I${SAGE_LOCAL}/include/python2.6 to compile options, in any case many other compilation lines actually have it already. After careful checking, I found that this particular option is not used in any scipy-0.7.x log I had on sage or Gentoo for these particular objects.
But I see it in scipy-0.8.0 in Gentoo. 

I am messing up with some of my system at the moment so I cannot generate a successful build log of scipy-0.8.0 from sage at the moment. But it would be interesting to know if this particular compilation option has been added in the successful builds.


---

Comment by fbissey created at 2010-09-13 01:35:39

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

Comment by maldun created at 2010-09-13 08:26:36

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

Comment by fbissey created at 2010-09-13 08:55:54

No need for extra logs. I found the culprit and why it affects only Karl's ppc
machine. I point the finger to g95! or rather the fact that the patches that
are installed if g95 is found should have been rebased. 

Basically the file special/setup.py is replaced by a version from scipy-0.7.0
which doesn't need the python header. Could you please use spkg-install.2 attached 
in scipy-0.8.0 it doesn't use the patches for g95. It should work without special
patch in my opinion anyway.


---

Comment by maldun created at 2010-09-13 10:34:27

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

Comment by fbissey created at 2010-09-13 10:55:53

I think I have gone overboard with double quotes, attaching a new version shortly.


---

Comment by maldun created at 2010-09-13 11:16:06

Ok. I deleted all outdated patches like you suggested (initially I let them in, because they didn't any harm, and since I didn't know much about every detail of the patches, I first tried out if it works, but of course it's better to throw them out) and it builds without problem. But with the old spkg.
the spkg-install.2 you attached still, with the same error, because my machine doesn't know the command
config_fc --noopt --noarch:

```
invalid command name 'config_fc --noopt --noarch'
```


could it be that I have to install something on my system? Or should we solve this with an If clause?


---

Comment by maldun created at 2010-09-13 11:28:45

ok I solved it: You forgot the "-" before the config =)


---

Attachment

new replacement for scipy


---

Comment by fbissey created at 2010-09-13 11:35:08

I think I found the problem, I think the shell was not set up properly.

I mean, these are options passed to setup.py not separate commands.
They shouldn't be interpreted as such and aren't in the numpy spkg-install,
so there are no reason why they should be in scipy.
But the shells for the two spkg-install were different so I think that may be 
a point of bash/shell semantic. In which case I am curious to find out what I
am supposed to do in sh. There is a new spkg-install.2 for you to try.


---

Comment by fbissey created at 2010-09-13 11:37:55

Replying to [comment:104 maldun]:
> ok I solved it: You forgot the "-" before the config =)

Ok you posted while I was answering. That may pass but I am not sure that
does what it's supposed to do. There shouldn't be a "-" in front. I suspect
it is now just ignored.


---

Comment by maldun created at 2010-09-13 11:45:14

ok I was to quick... indeed it builded, but not for too long: it took it a -c"onfig_fc"... so it didn't ignore, but missinterpreted it.

But the error remains. I don't really get it is there something different with ubuntu's gcc?


---

Comment by maldun created at 2010-09-13 11:55:18

Ah okay: I looked into the scipy docu: This option seems to be for numpy, not for scipy.
http://projects.scipy.org/numpy/wiki/DistutilsDoc#specifing-config-fc-options-for-libraries-in-setup-py-script

Because numpy builded with that command. Does it build on your system?


---

Comment by fbissey created at 2010-09-13 12:05:10

OK. I thought it was used in scipy as well. There seems to be 2 files with it, and it shouldn't have an impact. You can remove it then. Strange it doesn't generate errors in Gentoo.


---

Comment by maldun created at 2010-09-13 13:43:28

Ok updatet scipy package, with deleted patches


---

Comment by kcrisman created at 2010-09-13 14:59:17

Help!  I couldn't work on this over the weekend, and now I'm not quite sure what I should do to test :)  Should I just try installing the new Scipy 0.8, or what?  I am very glad that it seems you've figured out what G95 didn't like, though.     It would also be nice to see a diff between the `spkg-install` scripts.


---

Comment by maldun created at 2010-09-13 19:25:34

Ok short summary: 1) Try the new scipy 2) If this doesn't work try to change the header in gammaincinv.c in the scipy sources from <Python.h> to <python2.6/Python.h> 3) If this results in no change, rewrite the header that it takes the sage header directly means change <Python.h> to "whateverpathitmaybe/python2.6/Python.h" and look if the error message changes. (because there are other files affected, but this should be no prob to patch)

If it's really only the location of the header patching wouldn't be a problem.
And Thanx for all the trouble!


I have the diffs made for on my other machine, I can post them tomorrow!


---

Comment by maldun created at 2010-09-14 12:14:29

Diff of the spkg installs; The lines wich concern config fc are removed due problems in ubuntu


---

Attachment

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

Comment by kcrisman created at 2010-09-14 13:39:13

Success!  Now I'll set `SAGE_CHECK=yes`, retry numpy, do `./sage -ba`, retry scipy, and test the Sage library.  It will take a LONG time but hopefully tomorrow I'll have a report for you.


---

Comment by maldun created at 2010-09-14 13:43:24

That are great news! Hopefully everything works!


---

Comment by maldun created at 2010-09-14 13:45:19

Ah and don't forget the patch for the doctests in the attachement. Else there would 2 doctests fail due to output changes in numpy.


---

Comment by kcrisman created at 2010-09-14 14:00:30

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

Comment by fbissey created at 2010-09-15 04:21:24

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

Comment by fbissey created at 2010-09-15 04:23:22

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

Comment by fbissey created at 2010-09-15 04:28:21

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

Comment by maldun created at 2010-09-15 08:45:03

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

Comment by fbissey created at 2010-09-15 09:24:50

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

Comment by maldun created at 2010-09-15 10:25:11

Ok I removed the line. 

I also thougth before posting I should check if there are some old rests in there, and I removed some patches that are possible(?) outdated. I think this could affect the cygwin installation, so it would be important to see if it still builds on all machines, or else I have to carefully merge the changed lines, from the old patches with the new versions of the files.

It works for me, so I hope I didn't cause some new problems


---

Comment by maldun created at 2010-09-15 10:39:45

I have a different problem: When I upload the new Version, and try to download it I get the old one. Is there some confusion on the server?


---

Comment by maldun created at 2010-09-15 10:43:50

Ok worked. Don't ask why...


---

Comment by fbissey created at 2010-09-15 11:11:18

Ok - now this needs review!

I looked at the cygwin-lapack_lite-setup.py patch. The file patched hasn't changed between numpy-1.3.x and 1.4.1, so it can still be applied safely if needed.

In summary the only problems overall are:
* numpy 1.4.1 is broken on linux ppc (on the official list of supported OS - so bad) and alpha (not on the supported list - so OK).
* numpy-1.5.0 has an issues with cython that will be solved in 1.5.1 - shame because it also fixes linux ppc and alpha.

Anything to add?


---

Comment by fbissey created at 2010-09-15 11:11:18

Changing status from needs_work to needs_review.


---

Comment by maldun created at 2010-09-15 11:40:18

Replying to [comment:126 fbissey]:

> Anything to add?

as mentioned above: The version of numpy-1.5.0 with the patch applied is ok. The only trouble I have are some doctests, which fails because numpy throws a "Division by zero encountered!" Exception, which makes them fail, although the results are correct. But I still don't know how to catch the exceptions.


---

Comment by fbissey created at 2010-09-15 11:44:54

I should say that while breaking on linux ppc is not good, I only know of one other person building sage on that platform. So it could take the backseat while problems
with the 1.5 series are ironed out.


---

Comment by kcrisman created at 2010-09-15 17:30:03

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

Comment by maldun created at 2010-09-15 21:32:12

I know this error. Since you use sage 4.5.2 you will also use networkx-1.0.1. See comments 24 and following or ticket #9854.

You have to either use Sage 4.5.3 which holds networkx-1.2, upgrade networkx-1.0.1 in your current version, or apply the networkx-1.0.1.p0.spkg in the attachement, which holds a simple patch.

The reason is that numpy.core.defmatrix moved to numpy.matrixlib.defmatrix.


---

Comment by maldun created at 2010-09-15 21:52:05

`@`linux ppc I could work over the weekend the solve the failed doctests in numpy-1.5.0, because with the patch from the numpy developers the biggest problem i.e. the cython problem is solved. The only thing remains are some "Division by Zero Warnings" as mentioned above.


---

Comment by maldun created at 2010-09-15 21:54:16

And another thing: If we aren't able to merge numpy and scipy to 4.6. in time, why don't we provide the packages as optional or experimental? Because they work on most systems, and it would be a waste to just throw them away.


---

Comment by drkirkby created at 2010-09-15 22:10:41

Replying to [comment:129 kcrisman]:
> > * numpy-1.5.0 has an issues with cython that will be solved in 1.5.1 - shame because it also fixes linux ppc and alpha.
> 
> Hmm, dropping an official thing is not so good.  I think that one would want to post to the list about this - more likely wait for 1.5.1?  Or is the fix for this easily backported?  

Depending on what list you read, Linux on PPC may or may not be supported. I've tried to get an agreement before on what we do support and what we don't, but never got anywhere. 

I'm personally in favor of keeping Sage building on less regular systems, as it often indicates problems. The Solaris port has found endless bugs in Sage - some of which have even according to William been serious. 

I have an old IBM RS/6000 7025 F50 (Power PC) which I was setting up AIX on the other day. I contemlated  whether I should put Linux on it too for testing Sage. But when I read Sage's README.txt, PowerPC was only supported on OS X, not Linux. So I did not bother. But the machine has space for 18 disk drives, so I could always add it!! 

Dave


---

Comment by kcrisman created at 2010-09-16 01:12:59

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

Comment by kcrisman created at 2010-09-16 12:58:25

> You have to either use Sage 4.5.3 which holds networkx-1.2, upgrade networkx-1.0.1 in your current version, or apply the networkx-1.0.1.p0.spkg in the attachement, which holds a simple patch.

Incidentally, I also had to repackage that spkg, because you didn't use `./sage -pkg` for it either :) and it had unchecked in changes :)  But clearly that is irrelevant for testing, since the upgrade is already in a later Sage.

Okay, with this upgrade those two tests pass.  I am currently testing the other four failures, all of which were timeouts, all of which are in files I personally know to have VERY long `-long` doctests, and all but one of which hopefully will pass with `SAGE_TIMEOUT_LONG=10000` (there is one in `interfaces/maxima.py` which always fails on OS X 10.4, as far as I know, which is due to tab-completion testing of Maxima never finishing, totally unrelated to this).  I'll let you know if something *doesn't* work.

So I think that my job is done here (pointing out that I was testing the version from before the weekend.  fbissey or drkirkby should comment on the spkg itself.


---

Comment by fbissey created at 2010-09-17 01:58:46

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

Comment by maldun created at 2010-09-17 09:18:38

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

Comment by mhampton created at 2010-09-20 20:16:04

I'd like to check this out on sage-4.6.alpha1, but its unclear to me exactly what to do.  Can someone summarize the current procedure for incorporating this ticket?


---

Comment by maldun created at 2010-09-20 20:33:50

Replying to [comment:138 mhampton]:
> I'd like to check this out on sage-4.6.alpha1, but its unclear to me exactly what to do.  Can someone summarize the current procedure for incorporating this ticket?

Install notes and links to the packages are in the discription of this ticket!

Quick and dirty: Install the packagages, do sage -ba to compile the whole source, apply the patch in the attachment for the doctests.

greez maldun


---

Comment by fbissey created at 2010-09-28 17:54:27

Just a quick note that I used this package in sage-4.6alpha1 and it didn't break any tests on linux-x86, I haven't heard of any problems on linux-amd64 from a friend who was also testing this. So it applies cleanly on 4.6alpha1.


---

Comment by leif created at 2010-09-29 13:04:30

Dave pointed me to this ticket the day before yesterday (and I read it from the beginning). ;-)

Despite that, it's unclear to me which diffs are currrent, and the description should IMHO be updated wrt. what's to be done to review this.

`./sage -ba` is also in my opinion not a solution to get dependent extension modules updated, i.e. if `./sage -b` isn't sufficient, dependencies should be added to `module_list.py`.


---

Comment by maldun created at 2010-09-29 18:29:40

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

Comment by maldun created at 2010-09-29 19:04:57

Ah before I forget it, and you think I'm just lazy: I just looked up again in an non compiled version which files are concerned, and I remembered again what was really the problem
Most of them are already in the module_list.py.

However the problem is, that there are actually no changes to that files, so sage -b won't do nothing, because it does'nt recognice any changes!

only -ba force sage to do that and link the whole c files to the new version of numpy.

You would have to change the behavior of -b, not add something to the module_list.py


---

Comment by leif created at 2010-09-29 19:23:28

Just for the record, `gcc` has the following option:

  `-mabi=ieeelongdouble`
  
    Change the current ABI to use IEEE extended precision long double. This is a PowerPC 32-bit Linux ABI option.

I don't know if this requires a different (or differently built) `libc` however.


---

Comment by leif created at 2010-09-29 19:36:30

Replying to [comment:143 maldun]:
> Ah before I forget it, and you think I'm just lazy: I just looked up again in an non compiled version which files are concerned, and I remembered again what was really the problem
> Most of them are already in the module_list.py.
> 
> However the problem is, that there are actually no changes to that files, so sage -b won't do nothing, because it does'nt recognice any changes!

So we have to add (at least some of) those files to `depends` that actually _have_ changed.

> only -ba force sage to do that and link the whole c files to the new version of numpy.
> 
> You would have to change the behavior of -b, not add something to the module_list.py

That's IMHO not an option, since missing dependencies will break any Sage upgrade anyway.

P.S.: The attached diffs are still confusing. (One should at least change/update their descriptions.) For review, complete diffs between the old and new spkgs (of course excluding `src/`) would be helpful.


---

Comment by maldun created at 2010-09-29 19:57:05

Replying to [comment:145 leif]:

>
> So we have to add (at least some of) those files to `depends` that actually _have_ changed.
> 

And that's the problem: There are NO files which would have changed! Not within sage/devel/sage-whateverbranch. And that's also the reason for the warnings: numpy wonders why still the old size of flatiter is in the .c files. 
The only changes are in local/LIB/python/site-packages/numpy, and -b don't care about those.
The only way to trick -b was to put in a comment to the certain files, delete them again and save it, that sage -b recognices the changes.

I when kcrisman gives me feedback if numpy works now on ppc, I will put a complete changelog here on trac. Perhaps over the weekend I find some time for that.


---

Comment by kcrisman created at 2010-09-29 20:02:48

> I when kcrisman gives me feedback if numpy works now on ppc, I will put a complete changelog here on trac. Perhaps over the weekend I find some time for that.

You mean on OS X, not Linux, right?

Numpy installed fine, and Scipy got past the bad spot fine, so I don't anticipate any problems.  Then I'll run tests.

Leif, is this really a problem? (Asked as a query, not a complaint.)  Presumably someone will only use these packages via sage-upgrade, and then the whole library rebuilds (because sage-x.y.z is new), right?  Or is that not how sage-upgrade works?  

I'm adding a few reviewers based on how things have gone over these ~150 comments.


---

Comment by leif created at 2010-09-29 20:06:26

Replying to [comment:146 maldun]:
> Replying to [comment:145 leif]:
> 
> >
> > So we have to add (at least some of) those files to `depends` that actually _have_ changed.
> > 
> 
> And that's the problem: There are NO files which would have changed! Not within sage/devel/sage-whateverbranch. And that's also the reason for the warnings: numpy wonders why still the old size of flatiter is in the .c files.

So what? Then just make them also depend on e.g. `$SAGE_LOCAL/lib/python/site-packages/numpy/core/include/numpy/numpyconfig.h` (if _that_ has changed).


---

Comment by leif created at 2010-09-29 20:13:19

Replying to [comment:147 kcrisman]:
> Leif, is this really a problem? (Asked as a query, not a complaint.)  Presumably someone will only use these packages via sage-upgrade, and then the whole library rebuilds (because sage-x.y.z is new), right?  Or is that not how sage-upgrade works?

The Sage library is "new" in every Sage version (even if there were no real changes to it), but does *not* get rebuilt _from scratch_ (since there's no reason to do so if the dependencies are correct [or at least close to complete].)


---

Comment by leif created at 2010-09-29 20:23:12

P.S.: `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could be an option, too.


---

Comment by maldun created at 2010-09-29 20:27:18

I can do that, but this still won't solve the problem. Perhaps you misunderstand me, so I explain it again in more detail.

After installing numpy the only thing that has to be done is to recompile the .pyx files (which don't have changed), so that the old .c files (which haven't changed either) have be builded with the new version of numpy, that actually the change happens. I'm not a pro to sage, but as far I understood that is, that -b only recompile changed files. No changes, no compilation. Even if I add now the changed files (the package) sage only would recompile those, and leaves out a whole lot of files which also have to be recompiled. The only way to get now sage to recompile those .pyx which is to change the files after installation for example by putting a comment into them, or force sage to recompile them, that is that what -ba does. since there is no option that I know to force recompilation, I don't have an Idea how else I could get it working.

If you have a better way please let me know. I will apply a patch as soon as possible!

`@`kcrisman: didn't we talk about linux ppc? You said it builds on OS X ppc, or am I wrong?


---

Comment by kcrisman created at 2010-09-29 20:31:11

No, I'm sorry if you misread my post about that.  I would *like* to do so but there are still a number of technical hurdles to me running Linux PPC on my box (I think this should be clear in my sage-devel post).  I am testing whether the change you made to support Linux PPC doesn't break anything.  Sorry if this is not useful :( and I wish I did have access to Linux PPC more easily; unfortunately, this requires either having access to an already existing Linux PPC machine OR trying to run an image of Linux on a CD even with so little RAM there is no point OR using a portable hard drive, which is a more significant expense.


---

Comment by leif created at 2010-09-29 20:45:42

Apparently we have to add Carl Friedrich Gauss to the authors... ;-)


---

Comment by maldun created at 2010-09-29 21:09:57

As I feared: Making them dependent didn't force compilation either.


---

Comment by maldun created at 2010-09-29 22:04:13

Update: If you are changing the numpy.pxd file (for example insert a blank line and delete it) sage -b compile the dependent sources, but this file is in cython not in numpy.

manual changes on the numpy header files didn't do anything. 

`@`Leif I know what you are trying to tell me. I would have expected that making a header dependent would get sage to resolve the dependencies and recompile the .pyx files also.

But even little changes to the header files do nothing even if they are dependent, or I forced dependency.

I didn't meant this as offense or something, I just told you what I had experienced in the
early stages of this ticket.
If you have a solution for example a diff with an entry that forces dependency, (plot3d for example) I could write the others in no time.



Perhaps I do something wrong. If you know what the trouble is please tell me.


---

Comment by leif created at 2010-09-29 22:13:27

There are only a few headers that actually have been updated, e.g. `_numpyconfig.h`.

A trivial solution is to just `touch` one header file after installation in `spkg-install`, and make the relevant extension modules (also) depend on that one.

Touching `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could also help.


---

Comment by leif created at 2010-09-29 22:17:55

Replying to [comment:156 leif]:
> Touching `$SAGE_LOCAL/lib/python/site-packages/Cython/Includes/numpy.pxd` could also help.

Doing so triggers at least recompilation of the 13 extension modules that add the numpy include dir to their `include_dirs`.


---

Comment by fbissey created at 2010-09-29 22:31:53

Lots happens when I am asleep and lecturing first thing in the morning :)

I cannot comment on the sage-release thread from work. I am one of the few
people running sage on linux ppc - more as hobby to check that it works than real
production. The problem for numpy on ppc is fixed in numpy-1.5.

cannot comment on the rest right now I have a truckload of exams to prepare.


---

Comment by leif created at 2010-09-30 00:01:36

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

Comment by leif created at 2010-09-30 00:26:47

Replying to [comment:159 leif]:
> So touching just that file in numpy's `spkg-install` should fix all dependency issues, without touching `module_list.py` at all (which is advantageous, too).

Unfortunately this will only work if Cython is not updated/rebuilt (after numpy has been installed), since none of these packages depends on the other, and Cython might still ship one with an old time stamp (which is preserved on installation).


---

Comment by maldun created at 2010-09-30 08:46:08

>Regarding the discussion on sage-release, who prepares a numpy 1.5.0 (or later) spkg? ;-)
>
>The 1.4.1 seems obsolete now... 

I do. There are only 2 doctests that fails, due to output changes inf -> Inf
I hope I can complete it over the weekend.

Actually there is another problem with the headers: You would have to make ALL haeaders dependent on the concerning entries in the module_list.py, because in every version of numpy there can be an other headers that changes... and of course that is a matter of taste, but wouldn't get this the module_list.py a little bit messy, with dependencies that actually aren't needed?

just my 2 cents


---

Comment by fbissey created at 2010-10-01 00:38:33

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

Attachment

Changes of the spkg-install from the upgrade to 1.3.x to 1.5.0 (changes that were applied to 1.4.1 are also contained)


---

Attachment

diff of the spkg-install of scipy from 0.7.p5 to 0.8


---

Comment by fbissey created at 2010-10-02 23:50:48

I am incorporating that in my 4.6alpha2 branch on Gentoo right now.

I will unfortunately be unable to test it on linux ppc before Wednesday 6th 
because of limited access to the hardware. So it may be too short for me to do
a comprehensive review for the alpha3 deadline. I already know for sure that
numpy-1.5.0/scipy-0.8.0 will build it's just the testing that will be lacking.


---

Comment by fbissey created at 2010-10-03 07:36:47

Build on linux x86 and tests pass here on 4.6alpha2.


---

Comment by jhpalmieri created at 2010-10-05 00:01:29

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

Comment by jhpalmieri created at 2010-10-05 00:20:14

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

Comment by jason created at 2010-10-05 00:47:04

Can you try the new matplotlib spkg on #9221, if you think it is a matplotlib problem?


---

Comment by jhpalmieri created at 2010-10-05 02:01:59

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

Comment by fbissey created at 2010-10-05 03:27:42

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

Comment by jhpalmieri created at 2010-10-05 03:41:54

Replying to [comment:171 fbissey]:
> Dear me!
> 
> And I was going to report numpy-1.5/scipy-0.8 build on ppc (should be running testall now, I'd do -long but on that hardware we would still be there next week).
> 
> OK there are several issues to be solved: first  "-shared" is a good idea. That
> could be it.

Oops, it looks like it's already quoted in the spkg-install file.  I changed the first line from
{{{#!/bin/sh
```

to
{{{#!/usr/bin/env bash 
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

Comment by fbissey created at 2010-10-05 06:22:48

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

Comment by drkirkby created at 2010-10-05 07:03:45

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-10-05 07:03:45

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

Comment by drkirkby created at 2010-10-05 08:34:37

I don't have time to look at this now, but is this being built as C99? If not, that would explain it, since `isfinite` was not defined until the C99 standard. 

Dave


---

Comment by fbissey created at 2010-10-05 08:53:00

Replying to [comment:175 drkirkby]:
> I don't have time to look at this now, but is this being built as C99? If not, that would explain it, since `isfinite` was not defined until the C99 standard. 
> 
Why would fluvia not compile stuff in C99 by default? Compared to the other platforms?
As for ATLAS it was a suggestion. I just know that the problem is linked to something broken in lapack and because of linking to libf77blas/libcblas it can come down to
a problem with ATLAS.
I don't know what exactly is happening with that particular machine.


---

Comment by drkirkby created at 2010-10-05 14:18:34

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

Comment by jhpalmieri created at 2010-10-05 14:30:56

For what it's worth, I redid the build on fulvia with SAGE_CHECK=yes, and ATLAS passed its self-tests.  The matplotlib package still fails to install, with the import error from numpy.


---

Comment by drkirkby created at 2010-10-05 14:58:59

Does matplotlib generate any sort of config.log or similar? That might indicate what the problem is. 

I know at one point I had issues on 64-bit builds, when Numpy thought the static library was 32-bit. 

http://projects.scipy.org/numpy/ticket/1525
http://trac.sagemath.org/sage_trac/ticket/8086


---

Comment by jhpalmieri created at 2010-10-05 15:41:38

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

Comment by drkirkby created at 2010-10-05 17:11:59

Here's a recursive grep for `isfinite` in `/usr/include` on my OpenSolaris machine. I've not tested the package on my OpenSolaris machine, but given the results on Solaris 10, I doubt it would build. 


```
drkirkby`@`hawk:~$ ggrep -R isfinite /usr/include
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

Comment by drkirkby created at 2010-10-05 17:22:35

The more I look at this, the more I think it's a Numpy bug. 

Python is not built with C99 on my machine. The `config.log` of Python shows:



```
ac_cv_have_decl_isfinite=no
```


which is to be expected since its not built C99. So Numpy is at fault here I think, since that's making a reference to `isfinite` despite Python is not built with C99, so it's not defined, as evidenced by Python's `config.log`

BTW John, do you want an account on my OpenSolaris machine? It can build Sage in under an hour, so is a bit quicker than fulvia. 

Dave


---

Comment by drkirkby created at 2010-10-05 17:46:26

IMHO, we need to see if we can reproduce this with the latest cvs/svn/whatever snapshot of Numpy, and if so, report it as a bug to 

http://projects.scipy.org/numpy

If it's been fixed, then perhaps we can add a patch to the stable version, to just correct this bug. 

Dave


---

Comment by jhpalmieri created at 2010-10-05 18:58:36

I just downloaded the latest code (as listed [here](http://new.scipy.org/download.html#bleeding-edge-repository-access)), replaced the "src" directory with it, and installed it.  Running "./sage -python" and then "import numpy" results in the same error about isfinite.


---

Comment by drkirkby created at 2010-10-05 19:51:27

I reported this as a Numpy bug: 

http://projects.scipy.org/numpy/ticket/1625


---

Comment by drkirkby created at 2010-10-05 23:36:15

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

Comment by drkirkby created at 2010-10-05 23:47:26

Actually a bigger fix is being proposed on the numpy list. See there - I'm going to bed!

dave


---

Comment by jhpalmieri created at 2010-10-06 00:31:47

Dave, thanks a lot for working on this with the numpy people.  I prepared a new spkg and so far, the new numpy builds on fulvia, and after "./sage -python", "import numpy" works.  Matplotlib and scipy have now successfully built.  It will be a while before the build is complete, but things look good to me.

I'm putting the spkg up at [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg).

This is from a current svn snapshot based on 1.5.0.  I don't know if we have a policy about names for such spkg's, so I just used the date.  I also don't know if we have a policy about whether to include the repository information, so I've kept it.  This makes the spkg much bigger than the old version...

Should we mark this as "needs review" again?  It seems to depend on #9221.


---

Comment by jhpalmieri created at 2010-10-06 00:32:51

> Should we mark this as "needs review" again?

Or should we wait until the patch is positively reviewed on the numpy trac server?


---

Comment by jason created at 2010-10-06 00:56:07

Replying to [comment:188 jhpalmieri]:
> Dave, thanks a lot for working on this with the numpy people.  I prepared a new spkg and so far, the new numpy builds on fulvia, and after "./sage -python", "import numpy" works.  Matplotlib and scipy have now successfully built.  It will be a while before the build is complete, but things look good to me.
> 
> I'm putting the spkg up at [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.svn-20101005.spkg).
> 
> This is from a current svn snapshot based on 1.5.0.  I don't know if we have a policy about names for such spkg's, so I just used the date.  I also don't know if we have a policy about whether to include the repository information, so I've kept it.  This makes the spkg much bigger than the old version...

You don't need to keep the svn repository history, but you do need to put the revision number in the spkg name (numpy-1.5.0.svnXXXX).

However, I think it would be better to just include the one patch on top of 1.5.0, rather than pull an unstable release from subversion.  See the comments at the top of this trac ticket about using an unstable release (like 1.5.0RC2).


---

Comment by kcrisman created at 2010-10-06 01:20:25

> However, I think it would be better to just include the one patch on top of 1.5.0, rather than pull an unstable release from subversion.  See the comments at the top of this trac ticket about using an unstable release (like 1.5.0RC2).

I agree on this point, for what it's worth (since I will just be doing `./sage -i` and testing).


---

Comment by jhpalmieri created at 2010-10-06 01:22:10

Yes, but the patch was based on the svn code, not vanilla 1.5.0.


---

Comment by jason created at 2010-10-06 01:27:02

Replying to [comment:192 jhpalmieri]:
> Yes, but the patch was based on the svn code, not vanilla 1.5.0.

Are you saying that the patch does not apply to 1.5.0 directly?


---

Comment by jhpalmieri created at 2010-10-06 01:45:18

The patch affects two files.  One part of the patch is this:

```diff
diff --git a/numpy/core/setup.py b/numpy/core/setup.py
index ad8d5cb..f71ec10 100644
--- a/numpy/core/setup.py
+++ b/numpy/core/setup.py
`@``@` -215,10 +215,13 `@``@` def check_ieee_macros(config):
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

Comment by jhpalmieri created at 2010-10-06 02:55:40

Okay, I have a new version of the spkg, based on vanilla 1.5.0. I haven't tested it because I just lost my internet connection to fulvia.  See [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.spkg](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.spkg).  I'm also attaching the file displaying the differences between this spkg and the old 1.5.0 spkg posted here, except for two things: the new spkg includes modified copies of numpy/core/setup.py and numpy/distutils/command/config.py (in the patches directory -- the src directory is unmodified), and I didn't see any reason to include them in the posted patch file.  They are of course included in the repository, but to keep the patch file small, I edited them out before posting it.

Oh, the internet connection is back again.  I'm rebuilding on fulvia from scratch, which will take a while, but I just rebuilt the numpy package on mark2 successfully: "import numpy" works.


---

Comment by maldun created at 2010-10-06 10:33:07

Ah I'm only a few days away and everyones busy. Sometimes I think this ticket is cursed...
How high are the bets that this will work one day before 1.5.1 is released? =D

`@`jhpalmiere, drkirkby, fbissey: Thanks for all the trouble!

If you want I build the package with the new patches and upload it on google code for testing. (Or do you want to upload it?)
I will test it out on Ubuntu tonight for sure.

grettings,
maldun


---

Comment by maldun created at 2010-10-06 10:52:45

Ok I oversaw the link in the post...
I changed the old link in the discription to your new one.
The new package is doing fine on ubuntu. 
report for doctests will come soon!


---

Comment by drkirkby created at 2010-10-06 14:16:29

Replying to [comment:196 maldun]:
> Sometimes I think this ticket is cursed...
> How high are the bets that this will work one day before 1.5.1 is released? =D

Well the Numpy now works, but Scipy is presenting a problem on OpenSolaris due to the fact that the wrong compiler is being used. The variable `SAGE_FORTRAN` should specify the compiler:


```
drkirkby`@`hawk:~$ echo $SAGE_FORTRAN
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

Attachment

Sets F77, F90 and F95 so SciPy really does use the Fortran compiler we want. Setting FC alone is insufficient.


---

Comment by kcrisman created at 2010-10-06 14:51:51

Can I still test this by upgrading the packages, doing `./sage -ba`, and adding the doctest patch?  By the way, with the Pynac upgrade now in 4.6.alpha3 (see #9901), it's conceivable that the functions/hyperbolic.py piece of that will have to be rebased.


---

Comment by drkirkby created at 2010-10-06 14:55:56

Replying to [comment:200 kcrisman]:
> Can I still test this by upgrading the packages, doing `./sage -ba`, and adding the doctest patch?  By the way, with the Pynac upgrade now in 4.6.alpha3 (see #9901), it's conceivable that the functions/hyperbolic.py piece of that will have to be rebased.

I don't know enough about what needs to be done to test this. I've not even applied the patch myself yet. But the packages are at least building now, which is a start! 

I really need to be doing other things today, so are going to leave this ticket for the rest of the day - at least I will not be adding any code. 

Dave


---

Comment by drkirkby created at 2010-10-06 15:01:55

I've not applied the patches, so have not checked this fully, so I am not marking for review. But the two packages do now both build on OpenSolaris 06/2009 and I assume will do on Solaris 10 both SPARC and x86. *However, I have not tested these on Solaris, or any other system* 

I also added a lot of information which was missing from SPKG.txt

The new SciPy package is here. 

http://boxen.math.washington.edu/home/kirkby/patches/scipy-0.8.spkg

I don't have time to sort out how to apply the patches, fully build and doctest this. Sorry. 

Dave


---

Comment by maldun created at 2010-10-06 17:21:10

Replying to [comment:202 drkirkby]:
> I've not applied the patches, so have not checked this fully, so I am not marking for review. But the two packages do now both build on OpenSolaris 06/2009 and I assume will do on Solaris 10 both SPARC and x86. *However, I have not tested these on Solaris, or any other system* 
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

Comment by maldun created at 2010-10-06 17:28:59

Replying to [comment:200 kcrisman]:
> Can I still test this by upgrading the packages, doing `./sage -ba`, and adding the doctest patch?  By the way, with the Pynac upgrade now in 4.6.alpha3 (see #9901), it's conceivable that the functions/hyperbolic.py piece of that will have to be rebased.

Normally it should do. If you want save some time, write something in the numpy.pxd delete it again and save the file, so that the timestamp gets refreshed. After that sage -b should also do the trick.


---

Comment by maldun created at 2010-10-06 17:36:36

`@`changed doctests: Since this ticket won't be ready before the deadline, I wait till the release comes out and change it then.


---

Comment by drkirkby created at 2010-10-06 17:42:18

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

Attachment

The three new doctest failures which are almost certainly a result of upgrading Numpy and Scipy


---

Comment by jhpalmieri created at 2010-10-06 20:01:12

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

Comment by kcrisman created at 2010-10-06 20:21:51

> Normally it should do. If you want save some time, write something in the numpy.pxd delete it again and save the file, so that the timestamp gets refreshed. After that sage -b should also do the trick.
I think that just the command

```
touch .../numpy.pxd
```

should work, as leif pointed out.  Maybe this isn't a universal command?  Anyway, it did the trick on my computer - MUCH less time to build ~12 files than all the Cython files!  It's still doing this, so I won't have a chance to test yet, but I hope I won't get the failures drkirkby gets.


---

Comment by drkirkby created at 2010-10-06 20:31:41

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

Comment by drkirkby created at 2010-10-06 20:42:52

Not, since the patch to resolve the `isfinite` problem on http://projects.scipy.org/numpy/ticket/1625 worked, I commented on that fact on the ticket. That patch has now been committed to the Numpy source code, so will be in the next release, which is expected to be 1.5.1 but may be 2.0.0. 

So we have that one solved! 

Dave


---

Comment by drkirkby created at 2010-10-06 20:47:29

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

Comment by drkirkby created at 2010-10-06 20:56:42

I just started a fresh build with the new Numpy and the new SciPy. I assume once it builds, I need to apply the patch, rebuild the library and doctest again. I've done this once today, but I'll try again just to make sure I did not make an error. 

dave


---

Comment by drkirkby created at 2010-10-06 21:30:47

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


*Has anyone changed anything connected with the Fortran compiler in Numpy?* 

Dave


---

Comment by drkirkby created at 2010-10-06 21:44:27

Replying to [comment:213 drkirkby]:

> *Has anyone changed anything connected with the Fortran compiler in Numpy?* 
> 
> Dave 

I've just checked, and see someone (I think Francois) made some changes to how Fortran is handled in Numpy. He has exported FC, but not F77, F90 or F95. I think that's having a knock-on effect on anything that depends on Numpy, such as !Scipy and scipy-sandbox. 

I'll change the Numpy package so it exports FC, F77, F90 & F95. I suspect that will fix the problem. 

The doctest failures I got before, can easily be explained by this Fortran mix-up. 

Dave


---

Comment by jhpalmieri created at 2010-10-06 21:54:56

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

Comment by jhpalmieri created at 2010-10-06 21:55:45

> By the way, I just noticed these lines in the new scipy spkg-install file:

Sorry, I meant the *numpy* spkg-install file.


---

Comment by jhpalmieri created at 2010-10-06 22:16:12

Dave: Is this the sort of change you had in mind?

```diff

diff -r 1c2a7c8515fc spkg-install
--- a/spkg-install	Tue Oct 05 22:35:34 2010 -0400
+++ b/spkg-install	Wed Oct 06 15:07:58 2010 -0700
`@``@` -37,11 +37,13 `@``@`
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

Attachment

for reference only: diff between old numpy 1.5.0 spkg and new one


---

Comment by drkirkby created at 2010-10-06 22:20:43

Replying to [comment:217 jhpalmieri]:
> Dave: Is this the sort of change you had in mind?

Yes. I personally only ever use () and not {} in scripts, but I assume the latter is ok. 

That *probably* means that SciPy and scipy_sandbox do not need similar - I suspect they pick these up from Numpy. But we will see. It might be necessary to add  it to scipy_sandbox too. 

Dave


---

Comment by fbissey created at 2010-10-06 22:31:40

Back from snooze-land via morning teaching.

I would have expected that the fortran settings in scipy and numpy would have to match. I am completely astonished that you had problems with scipy and not numpy. In fact on Gentoo we currently have a bug open because numpy picks up the intel fortran compiler when it shouldn't.

Other than that I haven't tested the new spkg on linux ppc, but I don't think anything that has been touched that would affect compilation . Most of the test suite passed, a lot of time out on this hardware but since we are not in a hurry anymore I will do a run of the long test suite once I have checked the latest spkg.

I am not seeing the failure on citation.pyx or polynomial_element.pyx on that hardware, I just checked specifically.

Francois


---

Comment by drkirkby created at 2010-10-06 23:53:14

I hit the same issue with `scipy_sandbox`. I've put that on another ticket, with a patch that needs review. 

Dave


---

Comment by drkirkby created at 2010-10-06 23:53:59

Oops, I forgot to say, the other ticket is #10092. Perhaps someone can review that - it should be very easy. 

dave


---

Comment by jhpalmieri created at 2010-10-07 00:12:11

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

Comment by drkirkby created at 2010-10-07 00:18:22

OK, things are a lot better now on OpenSolaris, though seem to be a problem for John on OS X!!

Using:

 * The updated Numpy on this ticket
 * The updated Scipy which John made to export FC, F77, F90 and F95
 * An upated scipy_sandbox on #10092 which I made to export FC, F77, F90 and F95

then the three additional test failures caused by the Numpy/Scipy changes have all been resolved. This is on a Sun Ultra 27 running OpenSolaris 06/2009. 


```
drkirkby`@`hawk:~/new/sage-4.6.alpha2$ ./sage -t  -long devel/sage/doc/en/bordeaux_2008/introduction.rst
sage -t -long "devel/sage/doc/en/bordeaux_2008/introduction.rst"
	 [3.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.1 seconds
drkirkby`@`hawk:~/new/sage-4.6.alpha2$ ./sage -t  -long devel/sage/sage/numerical/test.py
sage -t -long "devel/sage/sage/numerical/test.py"           
	 [4.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.5 seconds
drkirkby`@`hawk:~/new/sage-4.6.alpha2$ ./sage -t  -long devel/sage/sage/plot/plot3d/list_plot3d.py
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

Comment by drkirkby created at 2010-10-07 00:27:51

I've got no idea if this will solve it, but the sage_fortran script has in it:


```
/usr/local/gcc-4.5.0-delayed/bin/gfortran -fPIC $`@`
```


but the bit at the end should be quoted:


```
/usr/local/gcc-4.5.0-delayed/bin/gfortran -fPIC "$`@`"
```


I've never found that an issue with any package in Sage, but when I tried to use an identical script for gcc and g++, I found problems which got resolved when I quoted the end of the line. You could try manually editing the script, putting a couple of quotation marks and seeing if that helps. 

This is very puzzling, but it is 1:25 AM here, and time I hit the bed. 

John, do you think the changing of the Fortran settings in these packages has caused the problem on OS X? 

Dave


---

Comment by fbissey created at 2010-10-07 00:42:10

Is it supposed to have all of these:  -arch ppc -arch x86_64 -arch ppc64
on OSX? Are making a fat build that could be used on all these archs somehow?


---

Comment by jhpalmieri created at 2010-10-07 01:31:00

> John, do you think the changing of the Fortran settings in these packages has caused the problem on OS X?

When I saw the problem, I tried rebuilding with older versions, or with versions modified to undo those changes.  I had the same problem, so assuming I didn't screw anything up, it wasn't caused by changing the Fortran settings.

> You could try manually editing the script, putting a couple of quotation marks and seeing if that helps.

I'll try it.


---

Comment by jhpalmieri created at 2010-10-07 03:09:23

Replying to [comment:224 drkirkby]:
> I've got no idea if this will solve it, but the sage_fortran script has in it:
> 

```
/usr/local/gcc-4.5.0-delayed/bin/gfortran -fPIC $`@`
```


On my Mac, it actually looks like this:
{{{#!/usr/bin/env bash
$SAGE_LOCAL/bin/gfortran-64  -m64 "$`@`"
```

So I don't need to add quotes -- they're already there.  And so this is not the cause of the problem.


---

Comment by drkirkby created at 2010-10-07 08:36:25

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

Comment by drkirkby created at 2010-10-07 08:43:30

A summary of changes to help reviewers - this ticket has got a bit complex, as 3 packages and a patch all need to be applied.


---

Attachment

Replying to [comment:219 fbissey]:
> Back from snooze-land via morning teaching.
> 
> I would have expected that the fortran settings in scipy and numpy would have to match. 

That seems not to the be case. It's probably a good idea if they do, but it looks like setting FC in Numpy is enough. I've just verified with grep by looking at the Numpy log that it only ever uses the GNU compiler when compiling F90 code and does not attempt to use `/usr/bin/f90`


```
drkirkby`@`hawk:~/new/sage-4.6.alpha2/spkg/logs$ grep  f90 numpy-1.5.0.log | grep bin
drkirkby`@`hawk:~/new/sage-4.6.alpha2/spkg/logs$ grep  f95 numpy-1.5.0.log | grep bin
drkirkby`@`hawk:~/new/sage-4.6.alpha2/spkg/logs$ 
```


It does not appear to have anything that's obviously using a Fortran 90 target, though it does compile files with the extension .f90. 

> I am completely astonished that you had problems with scipy and not numpy. In fact on Gentoo we currently have a bug open because numpy picks up the intel fortran compiler when it shouldn't.

Have you reported that bug upstream to the Numpy developers? If so, do you have the link handy? Do you have a link to the Gentoo bug? You could try exporting F77, F90 and F95 in addition to FC and see if that fixes it. It would be worth opening a bug report in Sage if this is affecting Sage too, which I expect it will. I could try creating a file 'icc' on my Sun and seeing if Numpy uses that, though since the Intel compiler does not run on Solaris, there's less chance of that being an issue. Perhaps someone with Linux can create a file `icc` that simply exits with 1. 

{{{#!/bin/sh
exit 1
```


and see if that screws up building Numpy. If so, it's a bug. 

In fact, given the issues with Scipy and scipy_sandbox, it might be wise we export all these variables in Numpy. 

What puzzles me most is why it is now necessary do this in scipy_sandbox, despite there have been no changes to the scipy_sandbox code at all! But checking in the sage-4.6.1.alpha1 code, I see the f90 target is using `sage_fortran` and not `/usr/bin/f90`.


```
drkirkby`@`hawk:~/sage-4.6.alpha1/spkg/logs$ grep f90 scipy_sandbox-20071020.p5.log
Fortran f90 compiler: sage_fortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops
Fortran f90 compiler: sage_fortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops
```


Hence this Numpy or SciPy upgrade has needed some rather surprising changes to be made to scipy_sandbox. 

I know when you build gmp, mpfr will be build with the same compiler, as the location of the compiler is actually stored in the gmp header files. I thought Numpy/ScipPy might use some similar technique, but it appears not.


---

Comment by fbissey created at 2010-10-07 09:56:21

The problem with ifc is actually more subtle than that [http://bugs.gentoo.org/show_bug.cgi?id=336077](http://bugs.gentoo.org/show_bug.cgi?id=336077) . someone has ifc installed but no license for whatever reason. Even so FC is set to gfortran, ifc will be tested if found. Without a license ifc wants to create a number of folders in the system, because the build system is sandboxed (so that no live files are touched will we are building the software) ifc throws an error with stops the build.

While sage doesn't use a sandbox the build could stop if ifc has been installed as root and a regular user is building numpy.

That's something to remember, even if a fortran compiler is selected, numpy/scipy will test for all the compilers they know off and try the one they found.

As for scipy, there were notes in the old spkg that scipy uses numpy distutils to build, that may have changed slightly in scipy-0.8.0 as it wasn't necessary to set all these compilers before at least in sage. A quick look at the corresponding Gentoo ebuilds show that we have been setting FC, F77 and F90 (but not F95) for some time in scipy (OK I didn't go in the CVS attic to checkout 0.7.0 in particular, just 0.8.0 and 0.7.2).


---

Comment by drkirkby created at 2010-10-07 12:28:33

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

Comment by kcrisman created at 2010-10-07 20:10:35

I've upgraded to the new ones on the Mac PPC, and the only problem I get in sage/matrix and sage/functions (other than the ones the patch fixes) is

```
sage -t -long "devel/sage/sage/functions/hyperbolic.py"     
Warning: divide by zero encountered in divide
Warning: divide by zero encountered in divide
```

Any ideas?  Looks like some other stuff reported here. I don't know that it would show up in doctesting.


---

Comment by fbissey created at 2010-10-07 21:53:25

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

Comment by mpatel created at 2010-10-07 22:40:38

How close is this ticket being to positively reviewed?  I have a trial 4.6.alpha3 that's ready to release, except for #10097, which I expect we'll fix within a day.  I'll release 4.6.alpha3 after that and put 4.6 in feature freeze.


---

Comment by fbissey created at 2010-10-07 22:45:30

Replying to [comment:234 mpatel]:
> How close is this ticket being to positively reviewed?  I have a trial 4.6.alpha3 that's ready to release, except for #10097, which I expect we'll fix within a day.  I'll release 4.6.alpha3 after that and put 4.6 in feature freeze.

I must say that with all that's happened to the ticket in the last few days, I and possibly maldun had lost hope of it making the deadline for the feature freeze.

I am about to review positively #10092 which would need merging at the same time. I am happy with
the spkg-es as they are for linux-ppc, so it is positive for me on that platform. I don't know about the other.


---

Comment by drkirkby created at 2010-10-07 23:09:19

Replying to [comment:234 mpatel]:
> How close is this ticket being to positively reviewed?  I have a trial 4.6.alpha3 that's ready to release, except for #10097, which I expect we'll fix within a day.  I'll release 4.6.alpha3 after that and put 4.6 in feature freeze.


#10092 has been positively reviewed. That has no dependencies, so that can go in now. 

These SciPy and Numpy patches look ok to me, but John had an issue on OS X. 

I think this must be very close to a positive review. 

Dave


---

Comment by kcrisman created at 2010-10-08 00:40:39

I get the same error as John on OS X 10.6.


---

Comment by drkirkby created at 2010-10-08 00:52:09

Replying to [comment:237 kcrisman]:
> I get the same error as John on OS X 10.6.

In which case I think we can forget this going into this release. Numpy 1.5.1 should be released by the end of the month, so I guess we will have to wait for that. 

#10092 will be needed for sure, and that is *very* safe and has positive review, so it would seem sensible to merge that if possible. 

Dave


---

Comment by kcrisman created at 2010-10-08 00:57:01

This seems related to `-m 64` and `-arch ppc64` - see for instance [here](https://trac.macports.org/ticket/21408) for something like this in Boost (which it seems they solved by just removing that option! maybe no one is building Sage on PPC in 64-bit mode anyway?).  [This discussion](http://omgili.com/mailinglist/boost-users/lists/boost/org/2E4E2E72-3D6F-41B3-BB5B-0D81145DEA59orchidseedorg.html) also seems to have relevant information about those two options; see especially 'On Mon, 7 Sep 2009'.  

Another unrelated thread says 'the fact that the gcc compiler now creates `x86_64` code by default so we are likely missing some instances of `-m32` which weren't required' in a similar context, though obviously that's not exactly what's going on here given the error messages - just that 32/64 bit and intel/ppc has something to do with it.  Maybe we are missing some Mac flags in the new Scipy?


---

Comment by fbissey created at 2010-10-08 01:05:58

Replying to [comment:240 kcrisman]:
> This seems related to `-m 64` and `-arch ppc64` - see for instance [here](https://trac.macports.org/ticket/21408) for something like this in Boost (which it seems they solved by just removing that option! maybe no one is building Sage on PPC in 64-bit mode anyway?).  [This discussion](http://omgili.com/mailinglist/boost-users/lists/boost/org/2E4E2E72-3D6F-41B3-BB5B-0D81145DEA59orchidseedorg.html) also seems to have relevant information about those two options; see especially 'On Mon, 7 Sep 2009'.  
> 
> Another unrelated thread says 'the fact that the gcc compiler now creates `x86_64` code by default so we are likely missing some instances of `-m32` which weren't required' in a similar context, though obviously that's not exactly what's going on here given the error messages - just that 32/64 bit and intel/ppc has something to do with it.  Maybe we are missing some Mac flags in the new Scipy?


May be. Could we have a little bit more of the log of the failure please? It could help to know what succeeded before the failure.


---

Comment by kcrisman created at 2010-10-08 01:18:07

> 
> May be. Could we have a little bit more of the log of the failure please? It could help to know what succeeded before the failure.

Sorry, that terminal is now gone.  Everything looks like jhpalmieri's - once Scipy is doing

```
compiling Fortran sources
```

the problem starts precisely there, so everything up to wherever that starts for dfftpack works.


---

Comment by jhpalmieri created at 2010-10-08 01:20:32

> May be. Could we have a little bit more of the log of the failure please? It could help to know what succeeded before the failure.

I've had the failure on two different OS X machines.  I've posted the full scipy log [here](http://sage.math.washington.edu/home/palmieri/misc/scipy-0.8.log).


---

Comment by jhpalmieri created at 2010-10-08 01:52:29

Just to check, I also built the older packages -- the ones uploaded by maldun to code.google.com -- and got the same error with  scipy.  So it doesn't seem to be because of the recent changes to those packages.


---

Comment by kcrisman created at 2010-10-08 15:16:35

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

Comment by jhpalmieri created at 2010-10-08 15:45:56

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

Comment by kcrisman created at 2010-10-08 17:13:24

This is what I was alluding to - they are now trying to build a universal binary for Mac, 32 and 64 bit, Intel and PPC.  Notice that they also got rid of the shared option and probably replaced it by the dynamic lookup option or whatever works for Mac.   Somehow our fortran compiler thing is not doing it right - maybe because we got rid of the whole `Sage_F_compiler` thingie?

But I have no idea where this would be in the Scipy source; I'm learning on the job.  I do think that getting rid of wherever the `-arch ppc64` is in there has a high probability of clearing up the issue, though in a hackish way (and this is what Boost did in the threads I link to in Comment 240).


---

Comment by drkirkby created at 2010-10-08 17:25:10

I think the best thing is we ask on the SciPy mailing list. I assume there is one - there is one for Numpy. None of us appear to know how to fix this properly, 

I've got no idea if is related to getting rid of the Sage_F_compiler thingie, but that sure is a possibility. 

I'm going to try to find a suitable list, subscribe to it, then ask. 

Dave


---

Comment by jason created at 2010-10-08 17:37:28

Replying to [comment:249 drkirkby]:
> I think the best thing is we ask on the SciPy mailing list. I assume there is one - there is one for Numpy. None of us appear to know how to fix this properly, 
> 
> I've got no idea if is related to getting rid of the Sage_F_compiler thingie, but that sure is a possibility. 
> 
> I'm going to try to find a suitable list, subscribe to it, then ask. 
> 

See http://scipy.org/Mailing_Lists


---

Comment by jhpalmieri created at 2010-10-08 17:52:13

Possibly related?

 - [http://projects.scipy.org/numpy/ticket/1399](http://projects.scipy.org/numpy/ticket/1399)
 - [http://article.gmane.org/gmane.comp.python.scientific.devel/14564](http://article.gmane.org/gmane.comp.python.scientific.devel/14564)
 - [http://article.gmane.org/gmane.comp.python.scientific.user/26314](http://article.gmane.org/gmane.comp.python.scientific.user/26314)


---

Comment by kcrisman created at 2010-10-08 18:05:19

Almost certainly so.


---

Comment by drkirkby created at 2010-10-08 20:20:25

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

I've subscribed to scipy-user----AT----scipy.org and made a post with the title _Problems building SciPy on OS X due to ppc64 issues_ I posted a link to John's build log. 

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

Comment by drkirkby created at 2010-10-09 01:23:07

There's a potentially helpful comment on the SciPy list from Ralf Gommers. It concerns _boost_ again. It suggests we are trying to build ppc on a system which does not support PPC. In which case, removing that option for ppc is a necessarily and not a hack. 

I'm puzzled how this option gets added now though - where does it come from? 

_Some googling turns up this which seems related to your issue:_

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

Comment by kcrisman created at 2010-10-09 03:31:23

Replying to [comment:254 drkirkby]:
> There's a potentially helpful comment on the SciPy list from Ralf Gommers. It concerns _boost_ again. It suggests we are trying to build ppc on a system which does not support PPC. In which case, removing that option for ppc is a necessarily and not a hack. 
> 
> I'm puzzled how this option gets added now though - where does it come from? 

That's what I'm trying to figure out.  Usually it gets added in the spkg-install, but apparently that's not the case here - it's coming from Scipy itself, [here](http://projects.scipy.org/numpy/ticket/1399) (first noted by John).

> ''You are using the 10.6 SDK and gcc 4.2. In the 10.6 SDK the ppc64
> architecture is not supported anymore, you want to use 10.4 or 10.5 SDK.
> Since Python is built with gcc 4.0 you want to do the same if you want C++
> support for ppc64 (which you'll need for scipy.sparsetools).''

Well, not exactly.  However, we always tell people that Mac Sage versions shouldn't be expected to work on older versions of Mac than they are created on.  So what's going on here is that we'll have to likely add something to the skpg-install or to the numpy distutils (whatever that is) that removes the ppc64 option (perhaps both ppc options?) from the `-arch` flags in order to get around this _only_ in the case that we in fact have OS X 10.6

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

Comment by jhpalmieri created at 2010-10-09 04:10:14

Replying to [comment:255 kcrisman]:
> Replying to [comment:254 drkirkby]:
> > There's a potentially helpful comment on the SciPy list from Ralf Gommers. It concerns _boost_ again. It suggests we are trying to build ppc on a system which does not support PPC. In which case, removing that option for ppc is a necessarily and not a hack. 
> > 
> > I'm puzzled how this option gets added now though - where does it come from? 
> 
> That's what I'm trying to figure out.  Usually it gets added in the spkg-install, but apparently that's not the case here - it's coming from Scipy itself, [here](http://projects.scipy.org/numpy/ticket/1399) (first noted by John).

If you grep through the scipy directory, I don't think you'll find "ppc64" anywhere.  I think it's coming from numpy, and in particular the file src/numpy/distutils/fcompiler/gnu.py.  If you make the change

```diff
--- gnu.py.old	2010-08-21 22:08:35.000000000 -0700
+++ gnu.py	2010-10-08 20:59:29.000000000 -0700
`@``@` -254,7 +254,7 `@``@`
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

Comment by kcrisman created at 2010-10-09 12:41:47

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

Comment by maldun created at 2010-10-11 06:44:37

As requested I updated the doctest changes in the patch.

I tested all recent numpy and scipy versions on ubuntu 10.04, and they built without problems on sage-4.6.alpha3 and all doctests passed with the updated patch.

Hope that all bugs in numpy are killed soon. I think the whole ticket here contributed quite a bit to numpy and scipy.


---

Comment by kcrisman created at 2010-10-13 02:21:20

Okay, I'm trying to look at this numpy package, and have some questions. 

First, there are all these special instructions in the SPKG.txt that seem to be totally irrelevant now about the `sage_fcompiler` etc. for gfortran and so forth.  Is all that unnecessary now that we exported F*, or not?  I assume drkirkby would be the most knowledgeable about this.  I know we tested this a lot, but it still worries me, since I know little about such things.

Second, I think that jhpalmieri's spkg should be 1.5.0.p0, correct?  And that should also be in SPKG.txt.

Next, toward the end it should be `SciPy` not `SciPY`.

Also, 11 hours ago someone pointed on on the Numpy trac that [this](http://github.com/matthew-brett/numpy/compare/numpy:master...farchs-from-c) might solve our issue more appropriately.  I was going to try to make a numpy spkg based on the other fix, but this might be better - I have to look at it and test it.  Anyway, an update.


---

Comment by jhpalmieri created at 2010-10-13 03:02:57

> First, there are all these special instructions ...

I don't know about this.  I hope Dave does.

> Second, I think that jhpalmieri's spkg should be 1.5.0.p0, correct? And that should also be in SPKG.txt.

I think that since it's not a vanilla 1.5.0, making it p0 is fine.  Or because I patched someone else's (already patched) 1.5.0, it could be p0.  Anyway, it's fine with me.  (I seem to remember seeing someone express the opinion that if it's the first time we've released a package for that particular version, then we don't need a patch number, but I don't really care one way or the other.)

> Next, toward the end it should be SciPy not SciPY.

Okay.

Finally, if you want to try a different fix, I'm happy to test it out.  Thanks for paying attention to the Numpy trac ticket; that's more than I was doing...


---

Comment by fbissey created at 2010-10-13 03:13:06

Replying to [comment:260 jhpalmieri]:
> > First, there are all these special instructions ...
> 
> I don't know about this.  I hope Dave does.
> 
I think I know about them, they should be mostly removed. My fault for pushing
some of the changes obsoleting these to maldun without updating the instructions
at the same time.


---

Comment by kcrisman created at 2010-10-13 03:19:22

> Finally, if you want to try a different fix, I'm happy to test it out.  Thanks for paying attention to the Numpy trac ticket; that's more than I was doing...

I'm trying it right now, but it's slow going because I know nothing about shell.  For instance, I just learned that `diff` has three different possible options, and the third one was the one that Sage patches look like - this took a half hour :(

I am trying to use `uname -r` to check for the Darwin version, but I don't know what would happen on (say) Solaris with this command.  David, portability ideas?  According to [this](http://www.unixtutorial.org/commands/uname/) it seems okay.


---

Comment by kcrisman created at 2010-10-13 03:22:19

Also, because unix tutorials are bad for true beginners, I have no idea how to do something that in pseudo-Python would be

```
output = `uname =r`
if output[:2] == 10:
    do ...
```

in shell script.  How do I take the output of `uname -r` and just get the first two characters (which would be 10 for OS X 10.6)?  Maddening - and of course it's impossible to figure out how to get this from the tutorials online without reading for hours.  Sorry - hopefully tomorrow I'll be able to get that figured out and test that patch, which depends on checking the `CFLAGS` passed to the fcompiler/gnu.py script.


---

Comment by fbissey created at 2010-10-13 03:30:33

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

Comment by fbissey created at 2010-10-13 03:37:40

So I looked at the special build instructions and right now they should be amended to

```
Special Update/Build Instructions:
  * Scipy uses numpy's distutils to control its compilation of fortran code.
    Whenever numpy is updated it is necessary to make sure that scipy still builds ok. 
```

And that's it. The rest is obsolete. I should review what we have done to make sure there are no other - new instructions that should be given.


---

Comment by jhpalmieri created at 2010-10-13 04:26:58

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

Comment by drkirkby created at 2010-10-13 11:10:00

A few points. 
 * I'm going to be very busy over the next week, and particularly today, so I don't have a lot of time to put into this. 
 * I believe the pacakge should be called 1.5.0 and not 1.5.0.p0 - this was discussed some time ago on sage-devel. 
 * I'm not sure that 'sed' command is doing what John wants. Instead of using 'uname' for test purposes, use 'echo'. 


```
drkirkby`@`hawk:~$ echo 10.1.4  | sed 's/\([0-9]*\)\..*/\1/'
10
drkirkby`@`hawk:~$ echo 10.6.0  | sed 's/\([0-9]*\)\..*/\1/'
10
drkirkby`@`hawk:~$ echo 10.6.0  | sed 's/\([0-9]*\)\..*/\1/'
10
drkirkby`@`hawk:~$ echo 10.5.1  | sed 's/\([0-9]*\)\..*/\1/'
10
drkirkby`@`hawk:~$ echo 9.5.1  | sed 's/\([0-9]*\)\..*/\1/'
9
drkirkby`@`hawk:~$ echo 10.4.1  | sed 's/\([0-9]*\)\..*/\1/'
10
```


That looks to be taking only the major part, and so can't distinguish from 10.5 or 10.6, which I think is what is said is needed. If that's what's needed, my approach would be 
 * Simulate the output of 'uname -r' (which is portable, so can be used on any platform, not just OS X), using 'echo'. That way you don't need to find different systems to test on. 
 * Make sure the OS is OS X. My HP C3600 runs HP-UX 11.11 and I expect (though it's off so I can't check), that 'uname -r' might print 11.11 which would not be any use here. So put this all in 'if' statemant that checks for OS X first. 
 * If you consider the output version to be x.y.z, then I'd do something like this, where I split the x.y.z into individual parts, by first replacing the dots with a space, then printing the 1st, 2nd or 3rd part of the expressions using 'awk'. 


```
drkirkby`@`hawk:~$ echo 10.4.1
10.4.1
drkirkby`@`hawk:~$ echo 10.4.1  | sed 's/\./ /g' 
10 4 1
drkirkby`@`hawk:~$ echo 10.4.1  | sed 's/\./ /g' | awk '{print $1}'
10
drkirkby`@`hawk:~$ echo 10.4.1  | sed 's/\./ /g' | awk '{print $2}'
4
drkirkby`@`hawk:~$ echo 10.4.1  | sed 's/\./ /g' | awk '{print $3}'
1
drkirkby`@`hawk:~$ 
```



---

Comment by kcrisman created at 2010-10-13 12:14:16

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

Comment by kcrisman created at 2010-10-13 12:48:43

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

Comment by kcrisman created at 2010-10-13 14:54:35

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

Comment by fbissey created at 2010-10-13 17:30:52

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

Comment by drkirkby created at 2010-10-13 18:10:10

You are OK with the bash shell, but it is *very* unportable to have no space before the left bracket. That will break with many shells, so is not a good habit to get into. 

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


Since this was a Solaris system, not OS X, `good` did *not* print it was OS X. 


```
-bash-3.00$ uname
SunOS
```


Just like Python, different people have different styles, and some are more portable than others. But that lack of a space is particular troublesome.

Dave


---

Comment by drkirkby created at 2010-10-13 18:11:45

Oops, I see you had realised this. Also I note it fails with bash too. 

Oh well, I'll shut up!!!

dave


---

Comment by kcrisman created at 2010-10-13 19:19:50

No problem :)  

But if you know where that extra "-c" comes from, please pipe up!  I'm stumped, but then again I know nothing of where such things are originated - presumably there is a typical file where they come from.


---

Comment by kcrisman created at 2010-10-14 02:20:05

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-10-14 02:20:05

Okay, I went back to John's initial idea and just removed the ppc64 option. I'm still totally mystified as to why that would solve it per se, if the double `-c` option is really a problem, but oh well - ppc64 is the problem.  

So I have now changed the description yet again to point us to a numpy spkg at my sage account.  Try it out.  I will now also attach diffs for reference about this.  Notice that I only attach the changed gnu.py file on Snow Leopard, so this should presumably only change anything on there.


---

Comment by kcrisman created at 2010-10-14 02:28:06

Patch to src/numpy/distutils/fcompiler/gnu.py


---

Attachment

Replying to [comment:275 kcrisman]:
> Okay, I went back to John's initial idea and just removed the ppc64 option. I'm still totally mystified as to why that would solve it per se, if the double `-c` option is really a problem, but oh well - ppc64 is the problem.  


There's no reason a double -c should be a problem. There are numerous options that get passed to gcc multiple times. Here's a simple session where I list the files in my directory, and look for the most recent one. 


```
drkirkby`@`hawk:~$ touch foobar
drkirkby`@`hawk:~$ ls -lrt | tail -1
-rw-r--r--   1 drkirkby other          8 Oct 14 10:37 foobar
drkirkby`@`hawk:~$ gcc -lm  test.c
drkirkby`@`hawk:~$ ls -lrt | tail -1
-rwxr-xr-x   1 drkirkby staff       8316 Oct 14 10:38 a.out
drkirkby`@`hawk:~$ gcc -lm -c -c test.c
drkirkby`@`hawk:~$ ls -lrt | tail -1
-rw-r--r--   1 drkirkby staff       1012 Oct 14 10:38 test.o
drkirkby`@`hawk:~$ 
```


We can see that calling 


```
gcc -lm -c -c test.c
```


resulted in the most recent file being an object file (.o) and not an executable a.out. 

The patch you attached is not a Mercurial patch, so could not easily be integrated.


---

Comment by kcrisman created at 2010-10-14 12:17:48

> There's no reason a double -c should be a problem. There are numerous options that get passed to gcc multiple times. Here's a simple session where I list the files in my directory, and look for the most recent one. 
This example just shows I am totally clueless.   So that couldn't have caused the problem?

> The patch you attached is not a Mercurial patch, so could not easily be integrated. 
It wasn't intended to be integrated - it was just intended to be viewed.  It is already part of the (correctly integrated, I think) patch in the actual spkg in the description, which is [here](http://sage.math.washington.edu/home/kcrisman/numpy-1.5.0.spkg).

Anyway, all long doctests pass with this on my 10.6 Snow Leopard computer.  And the change to spkg-install are exactly the same, so in theory this is the only platform it should affect, meaning all other review should work.   As I said, though, I don't feel comfortable giving it final positive review.

Will this ticket reach 300 comments?


---

Attachment

For reference only - OS X 10.6 fix in spkg-install


---

Comment by maldun created at 2010-10-14 13:13:59

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

Comment by jhpalmieri created at 2010-10-14 14:41:15

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-10-14 14:41:15

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

Comment by kcrisman created at 2010-10-14 14:54:36

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

Comment by jhpalmieri created at 2010-10-14 15:25:49

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

Comment by maldun created at 2010-10-14 18:06:55

Replying to [comment:279 jhpalmieri]:
> I built this on a unix box (eno), an OS X 10.6 box, an OpenSolaris box (hawk), and a Solaris on x86 box (fulvia).  (By "built", I mean I built from scratch based on Sage 4.6.alpha3, replacing the numpy and scipy packages with the ones on this ticket, and I also applied the doctest patch.)
> 
>  - On some machines, the doctest patch didn't apply cleanly: the patch to doc/en/faq/faq-usage.rst didn't apply, because it seems to already have been applied.  Maybe the tar file for 4.6.alpha3 changed?  The patch didn't apply cleanly on the machines where I downloaded it more recently.

Strange I tested the patch out, and it really didn't work. Then I made a new patch and it worked. So perhaps the file was corrupt. I upload a new version right now. Hope nothing gets corrupted again...

-maldun


---

Attachment

Changed doctests for numpy-1.5.0 due to output changes in numpy


---

Comment by maldun created at 2010-10-14 18:17:58

Ok if I download it again I have the same problem. It's really strange. If you look at the file sizes, the uploaded version has 2.7 kb (which the file what works also has), while the downloaded has 4.3 kb.
Something strange happens here...


---

Comment by jason created at 2010-10-14 18:20:31

Did you download the raw or the html version of the patch?


---

Comment by maldun created at 2010-10-14 18:36:06

The raw, and I'm already suspecting what's going on here: When I download from the wiki trac I get the old version for sage 4.5.3 instead of the new one... I had this problem frequently on several wikis now and it is starting to get on my nerves...

try this link out: http://computational-sage.googlecode.com/files/trac_9808_numpy_doctest_change.patch

It's my googlecode repository. Downloading from there works fine.

-maldun


---

Comment by maldun created at 2010-10-14 18:40:13

New upload of the doctest changes for sage 4.6


---

Attachment

Ok better solution: new name no probs anymore =)


---

Comment by jhpalmieri created at 2010-10-14 20:23:20

Updates: my doctest failure in citation.pyx is a "red herring".  In particular, it's not because of the patches here; it's because of a flaw in how the function get_systems works.  Often when I've been testing the packages and patches on this ticket, I've created a new version of sage in a directory called "numpy", and get_systems sees that string in the path name and adds "numpy" to the systems used by the particular command.  If I rename the directory to something else, then the doctest passes.  So let's not worry about this; at some point, someone can fix get_systems so it ignores the initial chunk of the path name (ignore the parent of SAGE_ROOT, for example).

My doctest failure in matrix1.pyx is still there.  For some reason, the "Datetime" type codes are not there on some systems.  Any ideas why?  I glanced at the install log for numpy, but I didn't see anything suspicious, not that I really know what to look for.  Here's the log from my OS X 10.6 machine, which is one place I see this problem: [http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.log](http://sage.math.washington.edu/home/palmieri/misc/numpy-1.5.0.log).

Finally, I have a new version of the scipy spkg, which works for me on all of the machines I've tested on: linux, OpenSolaris, Solaris on x86, Mac OS X 10.6.  I'm putting the link in the ticket description, and I'm posting the Mercurial patch -- it's very small.

I'm leaving this as "needs work" because of the matrix1.pyx issue, but I think that's the only remaining problem.  Please test the new scipy spkg on other systems to make sure, though.


---

Attachment

for reference only: diff between old scipy 0.8 spkg and new one


---

Comment by jhpalmieri created at 2010-10-14 20:49:14

See #10129 for the citation.pyx issue.


---

Comment by maldun created at 2010-10-14 20:51:05

`@`jhpalmieri I looked again on your matrix1.pyx problem, and this really interesting if you look on comment #23 (  http://trac.sagemath.org/sage_trac/ticket/9808#comment:23 ) we already had this change in linux also, but in numpy-1.4.1 and it vanished for numpy-1.5.0 again.

So whatever happen in Mac OS X it appears like an old numpy output comes up again, and if you look at it carefully it actually isn't really an error, more like that more keywords are available.

So perhaps it has something to do with the numpy installation of numpy itself on OS X. (perhaps another bug of numpy)


---

Comment by jhpalmieri created at 2010-10-14 21:05:43

Replying to [comment:289 maldun]:
> So whatever happen in Mac OS X it appears like an old numpy output comes up again, and if you look at it carefully it actually isn't really an error, more like that more keywords are available.

It looked to me like the "Datetime" keywords were missing, rather than more being available, but I might be wrong.

> So perhaps it has something to do with the numpy installation of numpy itself on OS X. (perhaps another bug of numpy)

I also see this on OpenSolaris, for what that's worth.

In any case, it's not a big deal, is it?  Can we just change the doctest somehow?


---

Comment by maldun created at 2010-10-14 21:15:36

*lol* I have the picture now: it seemed you installed my old patch which inherits the datetime change which was left  from numpy-1.4.1

If you try the new patch trac_9808_changed_doctests.patch in the attachement instead of 
trac_9808_changed_doctests.patch it will work. (look in the patch)

The one which is at fault here is the wiki: I overrided the file, but the wiki let you download the old patch.
Try it out: Download both patches, and look at them. The old one has the false filesize and inherits this change what had to be applied to numpy 1.4.1, in the new one this is left out


---

Comment by jhpalmieri created at 2010-10-14 21:45:35

Okay, I understand.  I don't know if it's the wiki's fault or mine: I may have just been using an old copy of the patch file which I had on my computer.  Anyway, I'm trying again now.  I've marked this "needs review", but things are looking pretty good now.


---

Comment by jhpalmieri created at 2010-10-14 21:45:35

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-10-15 04:17:18

With the new spkgs and the new patch, all tests pass for me (except for known unrelated failures) on skynet machines eno (linux), lena (linux), and fulvia (Solaris on x86).  The build on mark (Solaris on sparc) is ongoing; it's a very slow machine.  All tests also pass on my OS X 10.6 box and on Dave Kirkby's OpenSolaris machine hawk, as well as on sage.math.

Is this enough for a positive review?  I guess not quite: since I prepared the most recent scipy spkg, someone else should definitely review the changes (given in attachment:trac_9808-scipy.patch) and test it out.


---

Comment by kcrisman created at 2010-10-15 15:56:48

I was able to successfully install both packages on my slowest PPC OS X system; doing ./sage -b after touching the include will take a while, and I would have to wait until Monday to do all tests.  But I will at least test devel/sage/sage/matrix/, devel/sage/sage/functions/, devel/sage/sage/finance/, and devel/sage/sage/numerical, because those use Scipy and Numpy a lot and are NOT eons to test.  

Certainly the patch makes sense.  I can't check now whether the spkg was correctly created and whether it has any changes not checked in, but assuming all is well, this should be considered a successful, if long, process.   And I hope 1.5.1 won't come out the day after - though it looks like the Enthought folks are already looking to 2.0 as well.


---

Comment by kcrisman created at 2010-10-15 16:54:36

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-10-15 16:54:36

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

Comment by maldun created at 2010-10-15 17:31:04

Replying to [comment:296 kcrisman]:

> from the latest package John posted.  Positive review!

I've never thought I will read those words... I think I need a beer now 8)

The patch also works on Sage-4.6.alpha3 on Ubuntu. (Which was expected, but it is better to check too often then one time too less)

Thanks to everyone who worked on this ticket! I'm quite the beginner, but I think I learned a lot by helping upgrading numpy and can finally going back working on #9706 which should be a lot easier, but I needed the update to complete this task, because the new scipy holds a lot new features for orthogonal polynomials.
Hope I didn't cause too much grey hairs!

Kind regards,
Stefan aka maldun


---

Comment by jason created at 2010-10-15 17:33:01

Kudos to you guys!  

(and 3 more comments to reach 300!)


---

Comment by mhampton created at 2010-10-23 14:55:34

Congratulations, I got exhausted just trying to follow this!


---

Comment by jdemeyer created at 2010-11-01 10:10:59

Resolution: fixed


---

Comment by leif created at 2010-11-02 00:46:24

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

