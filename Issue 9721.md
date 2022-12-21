# Issue 9721: Problem upgrading from 4.5.2 to 4.5.3.alpha0 on OS X 10.6

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-08-11 01:17:29

Assignee: tbd

CC:  kcrisman leif

Reported by Karl-Dieter Crisman on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/7abfbeedb07abb53/a487f3968757f7b4#a487f3968757f7b4):

```
4.5.3.alpha0 did NOT upgrade successfully for me on OS X 10.6 from
4.5.2.  See below - though note that Sage does start up properly, and
sage -i returns (among others)

libm4ri-20100221

however the

pycrypto-2.1.0 pynac-0.2.0.p5 sage-4.5.3.alpha0

packages did then not update either, presumably.

- kcrisman

Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5664)
****************************************************
Starting build...
Removing old PolyBoRi install...
Done removing old PolyBoRi install.
Running build_polybori...
scons: Reading SConscript files ...
Checking for C header file gd.h... yes
Checking for C library gd... no
Checking for C++ header file ext/hash_map... yes
Warning: No LaTeX to html converter found, Tutorial will not be installed
Checking for C library m4ri... no
Checking for C header file gd.h... yes
Checking for C library gd... no
Symlinking to M4RI/m4ri ...
OSError: [Errno 2] No such file or directory:
  File "/Users/.../sage-4.5.2/spkg/build/polybori-0.6.4.p2/src/polybori-0.6.4/SConstruct", line 421:
    os.symlink('.', m4ri_inc)
Error building PolyBoRi.

real    0m1.425s
user    0m0.860s
sys     0m0.473s
sage: An error occurred while installing polybori-0.6.4.p2
```

Leif Leonhardy [replied](http://groups.google.com/group/sage-release/browse_thread/thread/7abfbeedb07abb53/69df2817539da964#69df2817539da964):

```
That's apparently due to my new (stripped) PolyBoRi spkg (#9472).

I'm currently looking at this, but in principle SCons should find the
"external m4ri" (on MacOS X, too) and not try to use the (now obsolete)
copy of it that was included in previous PolyBoRi spkgs. 
```

Related: #9472.


---

Comment by leif created at 2010-08-11 02:18:01

Note that neither the M4RI library *nor the GD library* (in the second attempt) are found, so this is not directly (or exclusively) related to removing the M4RI source tree.

It seems some SCons parameters have gotten messed up during the upgrade process. I'm currently trying to reproduce this error on Linux (though frankly speaking I expect this to be Apple-specific once again...)

Can someone try to reproduce this on other MacOS X boxes?


---

Comment by leif created at 2010-08-11 04:17:20

Replying to [comment:1 leif]:
> I'm currently trying to reproduce this error on Linux (though frankly speaking I expect this to be Apple-specific once again...)

"Of course"<sup>TM</sup> this worked for me on Ubuntu 9.04 x86_64.
(I've built 4.5.2 from scratch, successfully run ptestlong, successfully upgraded to 4.5.3.alpha0, then again successfully run ptestlong.)

```
...
Starting build...
Removing old PolyBoRi install...
Done removing old PolyBoRi install.
Running build_polybori...
scons: Reading SConscript files ...
Checking for C header file gd.h... yes
Checking for C library gd... no
Checking for C++ header file unordered_map... no
Checking for C++ header file tr1/unordered_map... yes
Warning: No LaTeX to html converter found, Tutorial will not be installed
Checking for C library m4ri... yes
Checking for C header file gd.h... yes
Checking for C library gd... yes
no python extension
scons: done reading SConscript files.
scons: Building targets ...
...
```


I don't think disabling/bypassing the check for a system (or Sage) M4RI library will fix Karl-Dieter's issue, since the GD library wasn't found either.

So, again,

> Can someone try to reproduce this on other MacOS X boxes?

Perhaps just his base installation was somehow broken...


---

Comment by mpatel created at 2010-08-11 09:36:19

Replying to [comment:1 leif]:
> Can someone try to reproduce this on other MacOS X boxes?

I upgraded successfully from a scratch-built 4.5.2 to 4.5.3.alpha0 on bsd.math (OS X 10.6).


---

Comment by malb created at 2010-08-11 12:12:52

This might be relevant http://trac.sagemath.org/sage_trac/ticket/9717#comment:5


---

Comment by mpatel created at 2010-08-17 07:14:41

Is it possible that #9717, which we merged into 4.5.3.alpha1, has fixed this problem?


---

Comment by kcrisman created at 2010-08-17 10:13:23

Replying to [comment:5 mpatel]:
> Is it possible that #9717, which we merged into 4.5.3.alpha1, has fixed this problem?
I will try to check this out today.  It will depend on whether my wireless connection is useful - I won't have other access today.


---

Comment by kcrisman created at 2010-08-17 19:05:56

Well, I was able to upgrade from the (broken) 4.5.2 to 4.5.3.alpha1 with no problems and all tests seem to be passing.  Is that good enough?


---

Comment by mpatel created at 2010-08-17 22:02:53

Resolution: duplicate


---

Comment by mpatel created at 2010-08-17 22:02:53

Replying to [comment:3 mpatel]:
> Replying to [comment:1 leif]:
> > Can someone try to reproduce this on other MacOS X boxes?
> 
> I upgraded successfully from a scratch-built 4.5.2 to 4.5.3.alpha0 on bsd.math (OS X 10.6).

For what it's worth, a 4.5.2-to-4.5.3.alpha1 upgrade also works for me.  The long doctests pass.

I'm resolving this ticket as a "duplicate" of (possibly fixed by) #9717.  Of course, we can reopen it or open another ticket, if there are new reports.
