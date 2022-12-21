# Issue 9356: make SAGE_ATLAS_LIB work on Solaris

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-06-28 01:26:33

Assignee: drkirkby

CC:  drkirkby fbissey

SAGE_ATLAS_LIB is supposed to allow the use of an external ATLAS installation rather than have Sage build it.  I think if Sage builds ATLAS once, then you ought to be able to copy the relevant files from that build to another directory and then use that directory as SAGE_ATLAS_LIB the next time you build Sage.  But this doesn't work on Solaris: on Solaris, when Sage builds ATLAS, it explicitly deletes the file liblapack.so, installing liblapack.a instead.  But when it tests SAGE_ATLAS_LIB, it tests for the existence of liblapack.so.

The new spkg just tests for the existence of liblapack.a on Solaris.


---

Comment by jhpalmieri created at 2010-06-28 01:30:46

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-06-28 01:30:46

Changing priority from major to minor.


---

Attachment

output of "hg diff" in atlas directory


---

Comment by drkirkby created at 2010-06-28 02:52:18

It looks OK, so positive review. 

I'm a bit suspicious of whether deleting the shared libraries was the right thing to do. #5024 deleted them as they were not working, but it would appear the GNU linker was used to convert from static to dynamic libraries. Given the GNU linker never has worked that well on Solaris, I'm not totally surprised they did not work. 

I obviously looked at this at some point in the past to get the shared libraries to be created: 

http://groups.google.co.uk/group/comp.unix.solaris/browse_thread/thread/963996de0269c17a/

It seems I wasted my time, as they are later deleted anyway, which I did not realise. 

I suspect the shared ones might actually work now. I think at a later date, when we have the test suites working, we should revisit whether deleting the shared libraries and using the much larger static ones is a good idea. (There's a comment in SPKG.txt about the shared one being 100 KB and the static one 8 MB.) 

But this looks good. It solves the problem. But long-term I think there might be a better solution. 

Dave


---

Comment by drkirkby created at 2010-06-28 02:52:18

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-10 02:37:25

On sage.math, `SAGE_LOCAL/lib` for a "standard" Sage 4.5.alpha4 build contains 

 * `libatlas.a, libatlas.so`
 * `libcblas.a, libcblas.so`
 * `libf77blas.a`
 * `liblapack.a`

After [converting the latter two to .so files](http://www.tipcache.com/tip/Convert_a_static_library_%28.a%29_to_a_shared_object_%28.so%29_12.html), I can use `SAGE_ATLAS_LIB` to build a separate copy of Sage without building ATLAS.  The new `SAGE_LOCAL/lib` contains `liblapack.a` and symlinks to the 4 shared libraries.  The long doctests pass.  Do we need the missing shared and/or static libraries?


---

Comment by jhpalmieri created at 2010-07-10 03:28:09

> Do we need the missing shared and/or static libraries?

I think this is an excellent question, and I have no idea what the answer is.  I hope that someone updates the ATLAS spkg soon and cleans up this question as well as others, like enabling parallel building so it doesn't take several decades to build on t2.math :)

The big cleanup belongs on another ticket, though.

Here's the end of the file spkg/logs/atlas... on sage.math, which I think explains why those files are missing:

```
ld -L/scratch/palmieri/sage-4.5.alpha4/local/lib -shared -soname liblapack.so -o liblapack.so --wh\
ole-archive liblapack.a --no-whole-archive -lc -lm -lgfortran
ld: cannot find -lgfortran
ld -L/scratch/palmieri/sage-4.5.alpha4/local/lib -shared -soname libf77blas.so -o libf77blas.so --\
whole-archive libf77blas.a --no-whole-archive -lc -lm -lgfortran
ld: cannot find -lgfortran
```

Is this a big deal?  Is it easy to fix?

Meanwhile, the Sage build for any system which has this problem will be missing liblapack.so and libf77blas.so.  (This includes not just sage.math but also the skynet machine lena.)  It would be best to fix it so these files are created properly, but meanwhile, should we change the ATLAS spkg so SAGE_ATLAS_LIB doesn't check for these?  Is the presence of the .a file always good enough?


---

Comment by drkirkby created at 2010-07-10 07:44:49

I can't see any logic for having both shared and static libraries, though it would never suprise me if one bit of Sage will not work with one type, so we need both.

If I understand correctly the static (.a) libraries are created and converted to shared libraries (.so), on all platforms except Solaris, since the conversion was not working in Solaris. I note that Mathematica ships with the shared library only on OpenSolaris on x64 - I don't have a Solaris 10 SPARC switched on with Mathematica on it, but I can check later. I suspect Wolfram Research only ship the shared library. The Solaris operating system does not ship with a single static library - their use is unpopular for their many disadvantages. 

The main advantage for the shared library would be a reduced memory footprint when multiple users make use of the same library. An ideal solution would be to create shared libraries properly on all platforms, and delete the static ones. 

I did look at updating ATLAS, but I had problems. I spent several hours on it, and got nowhere. Perhaps I was being too ambitions - trying to build ATLAS in parallel. If one looks at the ATLAS package, one can see that multiple threads are disabled, so the linear algebra will be solved more slowly than necessary. ATLAS is designed to be built in parallel - there are options to the Configure script for this. As are there options to control the number of threads used at runtime. 

I'd really like to resolve the issue with Sage building properly on OpenSolaris before devoting a lot of time to ATLAS. The OpenSolaris is annoying, as it builds, but does not run (segfault's at startup). I don't have much of a clue on how to debug it. I was hoping William would, but he has not looked at it despite I created him an account on my OpenSolaris machine with a built, but non-working version of Sage waiting to debugged. 

I think this ticket is a useful addition to Sage, but long term it would be better to have only the shared libraries, and so treat ATLAS the same ways as other platforms. 

I suspect, but have not confirmed, that the shared libraries will actually work properly on Solaris - they are certainly created, then deleted. I suspect that Micheal deleted them since he used the GNU linker (I know he used it), despite even the GCC docs telling you to use the Sun linker. (Of course, trying to build Sage with the GNU linker was easier, as one did not have to rid Sage of so many GNUisms. But ultimately, getting rid of the GNUisms and using the Sun linker was preferable.) Now Sage builds with the Sun linker, it would be worth investigating if the shared library work on Solaris, and we just delete the static libraries.

Dave


---

Comment by mpatel created at 2010-07-10 08:49:34

Let's definitely leave further changes for other tickets.

For the gfortran problem, I tried:

```sh
$ cd local/lib
$ ln -s libgfortran.so.2 libgfortran.so
$ rm -f libatlas.* libcblas.* libf77blas.* liblapack.*
$ cd ../../ 
$ ./sage -f spkg/standard/atlas-3.8.3.p12.spkg
[...]
ld -L/mnt/usb1/scratch/mpatel/apps/sage-4.5.a4/local/lib -shared -soname liblapack.so -o liblapack.so --whole-archive liblapack.a --no-whole-archive -lc -lm -lgfortran
ld -L/mnt/usb1/scratch/mpatel/apps/sage-4.5.a4/local/lib -shared -soname libf77blas.so -o libf77blas.so --whole-archive libf77blas.a --no-whole-archive -lc -lm -lgfortran
[...]
$ ls -ltr local/lib
[...]
   0 lrwxrwxrwx  1 mpatel mpatel   16 2010-07-10 00:05 libgfortran.so -> libgfortran.so.2
529k -rw-r--r--  1 mpatel mpatel 521k 2010-07-10 00:30 liblapack.a
570k -rw-r--r--  1 mpatel mpatel 565k 2010-07-10 00:30 libf77blas.a
472k -rw-r--r--  1 mpatel mpatel 467k 2010-07-10 00:30 libcblas.a
 12M -rw-r--r--  1 mpatel mpatel  12M 2010-07-10 00:30 libatlas.a
164k -rwxr-xr-x  1 mpatel mpatel 157k 2010-07-10 00:30 liblapack.so*
160k -rwxr-xr-x  1 mpatel mpatel 156k 2010-07-10 00:30 libf77blas.so*
156k -rw-r--r--  1 mpatel mpatel 151k 2010-07-10 00:30 libcblas.so
7.0M -rw-r--r--  1 mpatel mpatel 7.0M 2010-07-10 00:30 libatlas.so
```

(On sage.math, I use `SAGE_FORTRAN=/usr/bin/gfortran` and `SAGE_FORTRAN_LIB=/usr/lib/libgfortran.so.2`.)

But I can't take this further right now.


---

Comment by drkirkby created at 2010-07-10 09:54:46

Replying to [comment:7 mpatel]:
> Let's definitely leave further changes for other tickets.

I agree. This works. Long term a better solution no doubt exists, but this is step in the right direction. 

Dave


---

Comment by mpatel created at 2010-08-09 09:37:47

Resolution: fixed


---

Comment by mpatel created at 2010-08-21 07:17:58

I built 4.5.3.alpha1 on t2 with `SAGE_ATLAS_LIB` set to `SAGE_LOCAL` of an already built copy of alpha1.  (The latter I built without setting `SAGE_ATLAS_LIB` and without copying/linking any pre-existing ATLAS libraries.)  I get several doctest failures which appear to simplify to

```python
sage: from scipy.linalg import flapack
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/scratch/mpatel/tmp/sage-4.5.3.alpha1-sal/<ipython console> in <module>()

/scratch/mpatel/tmp/sage-4.5.3.alpha1-sal/local/lib/python2.6/site-packages/scipy/linalg/__init__.py in <module>()
      6 from linalg_version import linalg_version as __version__
      7
----> 8 from basic import *
      9 from decomp import *
     10 from matfuncs import *

/scratch/mpatel/tmp/sage-4.5.3.alpha1-sal/local/lib/python2.6/site-packages/scipy/linalg/basic.py in <module>()
     15 #from blas import get_blas_funcs
     16 from flinalg import get_flinalg_funcs
---> 17 from lapack import get_lapack_funcs
     18 from numpy import asarray,zeros,sum,newaxis,greater_equal,subtract,arange,\  
     19      conjugate,ravel,r_,mgrid,take,ones,dot,transpose,sqrt,add,real

/scratch/mpatel/tmp/sage-4.5.3.alpha1-sal/local/lib/python2.6/site-packages/scipy/linalg/lapack.py in <module>()
     16
     17 from scipy.linalg import flapack
---> 18 from scipy.linalg import clapack
     19 _use_force_clapack = 1
     20 if hasattr(clapack,'empty_module'):

ImportError: ld.so.1: python: fatal: relocation error: file /scratch/mpatel/tmp/sage-4.5.3.alpha1-sal/local/lib/python2.6/site-packages/scipy/linalg/clapack.so: symbol clapack_slauum: referenced symbol not found
sage: 
```

Has anyone seen this error before?  This `import` statement works in the "original" alpha1, which also passes the long doctests.


---

Comment by drkirkby created at 2010-08-21 12:06:19

Replying to [comment:10 mpatel]:
> Has anyone seen this error before?  This `import` statement works in the "original" alpha1, which also passes the long doctests.

I also had a failure setting SAGE_ATLAS_LIB, but I was not sure if it was something else I'd messed around with, so rebuilt Sage without setting it. 

I must admit, I reviewed this on the basis of "it looks logical" rather than "I have tested it". 

I think I can see what the problem might be too. `system_atlas.py` creates a load of symbolic links for shared libraries, but omits the static library. I suspect it needs another link put in. 


```
os.system(' ln -sf ' + ATLAS_LIB + '/lib/liblapack.a '  + SAGE_LOCAL_LIB+'/liblapack.a')
```


Could you try making that link symbolic link manually, and testing if that fixes the problem. 



Dave


---

Comment by mpatel created at 2010-08-22 05:35:50

Replying to [comment:11 drkirkby]:
> Could you try making that link symbolic link manually, and testing if that fixes the problem. 

I did this manually and reinstalled the NumPy and SciPy packages.  I'm not sure if it was necessary to recompile NumPy, but your suggestion works for me.  The long doctests now all pass.

John, have you had any problems with `SAGE_ATLAS_LIB`?


---

Comment by drkirkby created at 2010-08-22 07:57:48

Replying to [comment:12 mpatel]:
> Replying to [comment:11 drkirkby]:
> > Could you try making that link symbolic link manually, and testing if that fixes the problem. 
> 
> I did this manually and reinstalled the NumPy and SciPy packages.  I'm not sure if it was necessary to recompile NumPy, but your suggestion works for me.  The long doctests now all pass.

I think it would have been to recompile, as this is a *static* library, which means it should get bound into the executable. Had it been a shared library missing, then just adding the link would have been sufficient, but I doubt it would with a static library. 
 
> John, have you had any problems with `SAGE_ATLAS_LIB`?

I'm pretty sure John will do, as there's simply nothing in the code to make that static library available. John's fix was part of the solution, but not a complete solution. I'm sorry I did not make a better job of reviewing it, but it seemed so logical! 

Since I've already created a atlas-3.8.3.p14.spkg (#9508), which is merged into 4.5.3.alpha1, and #9508 includes this change, I think it is better to create another ticket to add the missing link, which I've since done. That is #9780. 

I'll implement that and test on OpenSolaris later today. If it fixes it on OpenSolaris then it will work for Solaris. The advantage of testing on OpenSolaris is simply speed. It takes a lot less time to build Sage on a 3.33 GHz Xeon than it does on `t2.math` or any SPARC I personally have access to. 

Dave


---

Comment by jhpalmieri created at 2010-08-22 14:48:31

Replying to [comment:12 mpatel]:
> Replying to [comment:11 drkirkby]:
> > Could you try making that link symbolic link manually, and testing if that fixes the problem. 
> 
> I did this manually and reinstalled the NumPy and SciPy packages.  I'm not sure if it was necessary to recompile NumPy, but your suggestion works for me.  The long doctests now all pass.
> 
> John, have you had any problems with `SAGE_ATLAS_LIB`?

I just tried using it, and it didn't work for me: same problem you had.  I thought that I had used it before successfully, but I don't know how this could be now.  I'm puzzled.

As far as making the link, do we need to link to all of the static libraries created by ATLAS?  It seems like it wouldn't hurt.  Also, it seems as though there is another liblapack.a, I think installed by the lapack spkg, which might need to be deleted before making the link.


---

Comment by drkirkby created at 2010-08-23 11:46:53

Replying to [comment:14 jhpalmieri]:
> Replying to [comment:12 mpatel]:
> > Replying to [comment:11 drkirkby]:
> > > Could you try making that link symbolic link manually, and testing if that fixes the problem. 
> > 
> > I did this manually and reinstalled the NumPy and SciPy packages.  I'm not sure if it was necessary to recompile NumPy, but your suggestion works for me.  The long doctests now all pass.
> > 
> > John, have you had any problems with `SAGE_ATLAS_LIB`?
> 
> I just tried using it, and it didn't work for me: same problem you had.  I thought that I had used it before successfully, but I don't know how this could be now.  I'm puzzled.

We all make mistakes. 

> As far as making the link, do we need to link to all of the static libraries created by ATLAS?  It seems like it wouldn't hurt.  Also, it seems as though there is another liblapack.a, I think installed by the lapack spkg, which might need to be deleted before making the link.

Yes, you are probably right. That's something I can address at #9780. In fact, I don't think there's any need to have the lapack package in Sage.


---

Comment by drkirkby created at 2010-08-27 12:11:37

I'm cc'in François Bissey on this, as he probably knows what Sage *really* need to include, and what we are wasting our time with. At the moment, `$SAGE_ROOT/spkg/deps` shows ATLAS depending on lapack. Then, in the ATLAS package, we create lapack.so from lapack.a. I'm not sure if ATLAS actually builds lapack.a itself. If so, I am not convinced we need lapack in Sage. 

I think François has said there's no need for us to include BLAS, as ATLAS is a BLAS library. Perhaps he can comment. The easy answer to solve this issue is to delete `liblapack.a` as you suggest. But that might not be the best long solution.

I don't understand the BLAS/LAPACK/ATLAS relationship. 

Dave


---

Comment by fbissey created at 2010-08-27 23:49:10

Not sure I like the smell of being cc to a can of worms first thing on Saturday morning.
I will need to see what the ATLAS spkg builds and install exactly. Glad that I 
have definitely dealt with that on sage-on-gentoo.
To summarize BLAS and LAPACK are technically a set of well defined linear algbra operations. There are standards on what they should be named and what they should do.
Which is why you can have a variety of implementation.
You may find some info here useful:
[http://www.gentoo.org/proj/en/science/blas-lapack.xml](http://www.gentoo.org/proj/en/science/blas-lapack.xml)
Anyway, BLAS is the reference implementation it produces libf77blas.{a,so} but
no cblas. lapack is lapack reference, it builds liblapack.{a,so} you can build
lapack-reference on top of most BLAS implementations.
ATLAS builds a tuned version of BLAS routines it build libcblas.{a,so} as well as
low level libraries in libatlas.{a,so}.
A wrapper for fortran77 code is then produced [another copy of libf77blas.{a,so}].
It is not compulsory to build these. There is a standard way documented upstream in ATLAS to include lapack-reference code in ATLAS and produce a set of lapack libraries. A lapack library produced by ATLAS in this way will also ship a clapack.h header - there is no standards for clapack.

I mentioned clapack because scipy looks for this. It will produce a different
set of low levels routines depending on whether it can find it or not. I think.
Your scipy will be slightly different depending on it. I could show the exact
differences if absolutely needed. 

If your lapack libraries has been compiled with atlas it will requires libatlas. 

ATLAS shouldn't depend on lapack. If anything it should be the other way around.
Unless we use the dependency to get access to the source code. 
I'll inspect the ATLAS spkg to see what is exactly done there.


---

Comment by fbissey created at 2010-08-28 04:32:13

So I have had a look at the ATLAS spkg and the ATLAS installation instructions


[http://math-atlas.sourceforge.net/atlas_install/atlas_install.html](http://math-atlas.sourceforge.net/atlas_install/atlas_install.html)

Of Particular interest are the section on lapack.
So you can build lapack first. I always thought that you needed to build a blas
first as lapack uses blas routines. Well that's what it says on lapack's homepage.[http://www.netlib.org/lapack/](http://www.netlib.org/lapack/)

So the ATLAS spkg does textbook application of section 3, and once we are done
we need to replace the old liblapck.a with the one provided by ATLAS which basically
replace a few routines with optimized one. That explain why ATLAS depends on lapack,
and possibly the whole chain blas->lapack->atlas.

I think it would be better to follow the scenario played out in section 8, but I have a feeling it relies on there being a blas somewhere in the system. There are ways 
I am sure. In gentoo we build lapack-atlas afterwards - it is somewhat involved.

The main problem in this kind of scenario is technically you may build lapack with 
2 different libf77blas. I am not sure what atlas does to ensure that doesn't lead 
to serious troubles.


---

Comment by fbissey created at 2010-08-28 09:36:22

Replying to [comment:15 drkirkby]:

> Yes, you are probably right. That's something I can address at #9780. In fact, I don't think there's any need to have the lapack package in Sage.

The sage spkg doesn't use it. However: 

 * numpy can use it. 
 * scipy *requires* it. 
 * linbox pretends to want it. - the reality is more subtle than that. Which is why even so liblinbox*.so are compiled against lapack sage components compiled against these do not need to be linked to lapack as well. 
 * R can use it.


---

Comment by drkirkby created at 2010-08-28 12:01:06

Replying to [comment:19 fbissey]:
> Replying to [comment:15 drkirkby]:
> 
> > Yes, you are probably right. That's something I can address at #9780. In fact, I don't think there's any need to have the lapack package in Sage.
> 
> The sage spkg doesn't use it. However: 
> 
>  * numpy can use it. 
>  * scipy *requires* it. 
>  * linbox pretends to want it. - the reality is more subtle than that. Which is why even so liblinbox*.so are compiled against lapack sage components compiled against these do not need to be linked to lapack as well. 
>  * R can use it.

What's confusing me is that in the ATLAS package, in the file `make_correct_shared.sh` there is this line:



```
	lapack_command="ld -L"$f95_dir" -L"$SAGE_LOCAL"/lib  -shared -soname liblapack.so -o liblapack.so  --whole-archive liblapack.a --no-whole-archive -lc -lm -lf95"
```


which makes a shared library `liblapack.so` from a static library `liblapack.a`. But the LAPACK package also creates `liblapack.a`

Since LAPACK is listed as a dependency of ATLAS, it would appear that LAPACK gets built first, creates `liblapack.a`, then ATLAS overwrites `liblapack.a`. (Overwriting files like this is not supposed to happen in Sage, but if ATLAS creates a more optimised version, I can see there may be the logical thing to do).

So it seems if you want to make use of a pre-existing `liblapack.a` from ATLAS, which means creating a symbolic link, would need to remove the `liblapack.a` created by LAPACK first, then create the link. (Otherwise, I think creating the link might fail, though I'm not sure.) I need to rush out, so dont have time to test that. 

Dave


---

Comment by drkirkby created at 2010-08-28 12:21:58

Replying to [comment:20 drkirkby]:

> So it seems if you want to make use of a pre-existing `liblapack.a` from ATLAS, which means creating a symbolic link, would need to remove the `liblapack.a` created by LAPACK first, then create the link. (Otherwise, I think creating the link might fail, though I'm not sure.) I need to rush out, so dont have time to test that. 
> 
> Dave 

On checking, just creating the link will overwrite the old file, so there's no need to delete anything first. But if I'm not mistaken, `liblapack.a` does get created twice - once by LAPACK and once by the script in ATLAS.  

Dave


---

Comment by fbissey created at 2010-08-28 21:56:47

Replying to [comment:21 drkirkby]:

> Replying to [comment:20 drkirkby]:
> > So it seems if you want to make use of a pre-existing `liblapack.a` from ATLAS, which means creating a symbolic link, would need to remove the `liblapack.a` created by LAPACK first, then create the link. (Otherwise, I think creating the link might fail, though I'm not sure.) I need to rush out, so dont have time to test that.  Dave
> On checking, just creating the link will overwrite the old file, so there's no need to delete anything first. But if I'm not mistaken, `liblapack.a` does get created twice - once by LAPACK and once by the script in ATLAS.   Dave

That is correct.

The lapack spkg produce liblapack.a, ATLAS takes it as an input, unbundles it
and then build some optimized routines to replace the original ones.
Finally it recreates a library liblapack.a which is meant to replace the original.

You should read the ATLAS installation guide it is very instructive. There is even
a section about solaris on sparc.

Francois


---

Comment by drkirkby created at 2010-08-28 22:29:58

Replying to [comment:22 fbissey]:
> That is correct.

> The lapack spkg produce liblapack.a, ATLAS takes it as an input, unbundles it
> and then build some optimized routines to replace the original ones.
> Finally it recreates a library liblapack.a which is meant to replace the original.
> 
> You should read the ATLAS installation guide it is very instructive. There is even
> a section about solaris on sparc.
> 
> Francois

Thank you. That makes more sense now. I will take a read of the ATLAS docs. I would like to update the ATLAS package, but it is is a bit of a mess - bash, perl, python scripts all over the place. Loads of patches. 

I've already opened #9780 to add the link we need. I'll create a patch. Thank you for your help 
Francois. 

Dave


---

Comment by fbissey created at 2010-08-28 22:56:27

The one thing I don't really understand is why we need the .a libraries.
It may point to the .so being made incorrectly. On my system - and it is used by
system wide sage that we make for Gentoo:

```
ldd /usr/lib/python2.6/site-packages/numpy/linalg/lapack_lite.so
        linux-gate.so.1 =>  (0xb78de000)
        liblapack.so.0 => /usr/lib/liblapack.so.0 (0xb738c000)
        libpython2.6.so.1.0 => /usr/lib/libpython2.6.so.1.0 (0xb7232000)
        libc.so.6 => /lib/libc.so.6 (0xb70c4000)
        libblas.so.0 => /usr/lib/blas/atlas/libblas.so.0 (0xb70a4000)
        libcblas.so.0 => /usr/lib/blas/atlas/libcblas.so.0 (0xb7081000)
        libatlas.so.0 => /usr/lib/libatlas.so.0 (0xb69c2000)
        libgfortran.so.3 => /usr/lib/gcc/i686-pc-linux-gnu/4.4.4/libgfortran.so.3 (0xb68fb000)
        libm.so.6 => /lib/libm.so.6 (0xb68d4000)
        libgcc_s.so.1 => /usr/lib/gcc/i686-pc-linux-gnu/4.4.4/libgcc_s.so.1 (0xb68b6000)
        libpthread.so.0 => /lib/libpthread.so.0 (0xb689b000)
        libdl.so.2 => /lib/libdl.so.2 (0xb6897000)
        libutil.so.1 => /lib/libutil.so.1 (0xb6893000)
        /lib/ld-linux.so.2 (0xb78df000)
```

Note that libblas.so is actually libf77blas.so (it is just renamed for
obscure Gentoo reasons). I can show the same kind of things for libraries
shipped with scipy. In contrast in a vanilla install of sage:

```
ldd local/lib/python2.6/site-packages/numpy/linalg/lapack_lite.so
        linux-gate.so.1 =>  (0xb78b0000)
        libcblas.so => /home/francois/Work/sandbox/install/sage-4.4.1/local/lib/libcblas.so (0xb7770000)
        libatlas.so => /home/francois/Work/sandbox/install/sage-4.4.1/local/lib/libatlas.so (0xb72db000)
        libgfortran.so.3 => /usr/lib/gcc/i686-pc-linux-gnu/4.4.4/libgfortran.so.3 (0xb71ea000)
        libm.so.6 => /lib/libm.so.6 (0xb71c3000)
        libgcc_s.so.1 => /usr/lib/gcc/i686-pc-linux-gnu/4.4.4/libgcc_s.so.1 (0xb71a4000)
        libc.so.6 => /lib/libc.so.6 (0xb7036000)
        /lib/ld-linux.so.2 (0xb78b1000)
```

While it says sage-4.4.1 it has been incrementally updated to 4.5.2.


---

Comment by drkirkby created at 2010-08-31 08:33:00

Replying to [comment:24 fbissey]:
> The one thing I don't really understand is why we need the .a libraries.

If you look above, you will see I made that same point. There does not seem to be any logical reason to distribute both static and dynamic libraries. 

However, #5024 shows liblapack.so was causing problems on "non-Linux" systems - which I assume means both OS X and Solaris, though there's little information there. 

I've certainly seen problems on Solaris with `liblapack.so`, so on Solaris at least, liblapack.so can't be built just now. 

I think long term, we need to look at updating ATLAS. I expect it should be able to create shared libraries that work. That said, on Solaris x86 at least, Mathematica ships with   and `libatlas.a`, `libf77blas.a`, `liblapack.a` and `libcblas.a` rather than shared libraries. Out of the 111 libraries included in Mathematica, only 6 are static - the other 105 are shared. 

I thought I'd posted a fix to this problem. Adding the link for `liblapack.a` works. I'll stick that on #9780. 

Dave


---

Comment by fbissey created at 2010-08-31 10:03:34

Replying to [comment:25 drkirkby]:
> Replying to [comment:24 fbissey]:
> > The one thing I don't really understand is why we need the .a libraries.
> 
> If you look above, you will see I made that same point. There does not seem to be any logical reason to distribute both static and dynamic libraries. 
> 
That would be nice too. My point was more to the fact that numpy uses the 
static library rather than the shared one. If I trust ldd output from my install
on linux sage's numpy is always linked to the static library.

Obviously there are cases were you need the static library on some platforms but
it should only link to the static library on those platforms. I will look
to see if that comes from the numpy spkg while working on #9808 

Francois


---

Comment by fbissey created at 2010-08-31 23:36:24

Well it appears that my sage installation lacks liblapack.so. This probably explain that. I am sure it should have been created. it is strange I seem to miss it.


---

Comment by jhpalmieri created at 2010-09-01 19:28:17

> Well it appears that my sage installation lacks liblapack.so. This probably explain that. I am sure it should have been created. it is strange I seem to miss it.

I've seen this before, for example on sage.math.  Toward the end of the atlas log file, I see

```
ld -L/mnt/usb1/scratch/palmieri/sage-4.5.3.alpha0/local/lib -shared -soname liblapack.so -o liblap\
ack.so --whole-archive liblapack.a --no-whole-archive -lc -lm -lgfortran
ld: cannot find -lgfortran
ld -L/mnt/usb1/scratch/palmieri/sage-4.5.3.alpha0/local/lib -shared -soname libf77blas.so -o libf7\
7blas.so --whole-archive libf77blas.a --no-whole-archive -lc -lm -lgfortran
ld: cannot find -lgfortran
```

I've never noticed that it caused problems, not that I would know exactly what to look for anyway.
