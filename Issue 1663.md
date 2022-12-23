# Issue 1663: scipy build fails in tr_TR locale

Issue created by migration from https://trac.sagemath.org/ticket/1663

Original creator: burcin

Original creation time: 2008-01-03 09:59:57

Assignee: mabshoff

CC:  jason jkantor timdumol rlm

Scipy build fails with the following error when locale is set to `tr_TR.UTF-8`.


```
building 'odepack' library
compiling Fortran sources
Fortran f77 compiler: sage_fortran -ffixed-form -fno-second-underscore
-O
Fortran f90 compiler: sage_fortran -fno-second-underscore -O
Fortran fix compiler: sage_fortran -ffixed-form -fno-second-underscore
-O
creating build/temp.linux-i686-2.5/scipy/integrate/odepack
compile options: '-c'
sage_fortran:f77: scipy/integrate/odepack/lsoda.f
sage_fortran:f77: scipy/integrate/odepack/mdp.f
sage_fortran:f77: scipy/integrate/odepack/vnorm.f
sage_fortran:f77: scipy/integrate/odepack/xerrwv.f
In file scipy/integrate/odepack/xerrwv.f:103

 20   format(6x,'in above message,  i1 =',i10)
                                          1
Error: Unexpected element in format string at (1)
In file scipy/integrate/odepack/xerrwv.f:105

 30   format(6x,'in above message,  i1 =',i10,3x,'i2 =',i10)
                                          1
Error: Unexpected element in format string at (1)
In file scipy/integrate/odepack/xerrwv.f:103

 20   format(6x,'in above message,  i1 =',i10)
                                          1
Error: Unexpected element in format string at (1)
In file scipy/integrate/odepack/xerrwv.f:105

 30   format(6x,'in above message,  i1 =',i10,3x,'i2 =',i10)
                                          1
Error: Unexpected element in format string at (1)
error: Command "sage_fortran -ffixed-form -fno-second-underscore -O -c
-c scipy/integrate/odepack/xerrwv.f -o build/temp.linux-i686-2.5/scipy/
integrate/odepack/xerrwv.o" failed with exit status 1
```


In the tr_TR locale, lowercase of `I` is `ı`, and uppercase of `i` is `İ`. This might cause unexpected results for auto generated files.

A simple workaround is to clear the locale environment variables:


```
unset LANG LC_ALL LC_CTYPE
```



---

Comment by mabshoff created at 2008-01-03 11:57:33

This sounds fine as a temporary workaround, but we need to do the following things:

 * figure out if it happens with an unmodified python and numpy/scipy
 * if not figure out what we did wrong
 * alternatively report this upstream to the scipy people

Cheers,

Michael


---

Comment by cartman created at 2008-01-03 14:41:03

scipy standalone build works fine on Pardus, I suspect this is due to our Python changes,

we build with following configure options added: --enable-unicode=ucs4 --with-wctype-functions

and we apply http://svn.uludag.org.tr/pardus/devel/system/base/python/files/default-utf8.patch

Regards,
ismail


---

Comment by mabshoff created at 2008-01-03 14:55:06

The ticket to switch to ucs4 is #551. The 2.10 release should be a good point in time to do the conversion since we will update a boat load of spkgs.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-03 15:26:37

We should also check Pardus's svn repo for fixes at.

http://svn.uludag.org.tr/pardus/devel/system/base/python/files

Cheers,

Michael


---

Comment by burcin created at 2008-01-17 16:28:41

The problem remains, after the switch to ucs4, using a python built with the changes mentioned in comment:2. 

Looking at the error message again, I don't see how this can be related to python. I can't find any other changes in the Pardus repository which might effect the scipy build. Ismail, any ideas?

I suggest clearing the LANG, LC_ALL and LC_CTYPE variables in the scipy spkg-install for now, as a work around.


---

Comment by cartman created at 2008-01-21 13:59:43

Setting LC_ALL to C should workaround all this problems, weird thing is how it compiles here. I will dig a bit more and let you know. Sorry for the late reply, trac somehow does not e-mail me new messages :-/


---

Comment by mabshoff created at 2008-03-01 22:44:30

The SciPy people have actually fixed this bug, so once we update it should be resolved.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-11 12:16:30

Since the Scipy people have not done a release in an eternity we should really add the workaround to our scipy.spkg for now to close the issue. I will take care of this in the short term.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-11 12:16:30

Changing status from new to assigned.


---

Comment by burcin created at 2009-06-15 09:39:17

scipy was upgraded with #3391, but this problem still remains. Error message is the same.

To reproduce the error, 


```
export LC_CTYPE=tr_TR.UTF-8
```


and build Sage as usual.


---

Comment by burcin created at 2010-01-19 12:46:14

Resolution: fixed


---

Comment by burcin created at 2010-01-19 12:46:14

Sage-4.3.1.rc1 just built with `LC_CTYPE=tr_TR.UTF-8` on my laptop. This seems to be fixed by the latest scipy update.


---

Comment by timdumol created at 2010-01-21 10:40:55

The SciPy 0.7.1 package included in Sage was done by Jason Grout, not by me. The setup.py packages of his package were more up-to-date, so his was included (also, he made his much earlier).
