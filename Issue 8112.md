# Issue 8112: flint fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-01-28 16:02:28

Assignee: drkirkby

flint-1.5.0.p3 fails to build if SAGE64=yes and no CFLAGS and CFLAG64 are set globally due to a 32/64 bit issue.

A patch is on it's way.

Jaap


---

Comment by jsp created at 2010-01-28 16:24:56

Here is an spkg:
[http://boxen.math.washington.edu/home/jsp/ports/flint-1.5.0.p4.spkg](http://boxen.math.washington.edu/home/jsp/ports/flint-1.5.0.p4.spkg)



```
jaap`@`opensolaris:~/Downloads/sage-4.3.2.alpha0$ file local/lib/libflint.so 
local/lib/libflint.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available

```


Jaap


---

Comment by jsp created at 2010-01-28 16:24:56

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-29 18:22:45

It's not clear to me what is intended here. 

 * There is no such thing as CXXFLAG. Did you mean CXXFLAGS? 
 * The point of CFLAG64 is that it would be set to whatever flag is needed to build 64 bit executables with a C compiler, which -m64 in most, but not all cases. 
 * The point of CXXFLAG64 is that it would be set to whatever flag is needed to build 64 bit executables with a C++ compiler, which -m64 in most, but not all cases. 


If Flint will build by setting the environment variables CFLAG64 and CXXFLAG64 to -m64, then I would not bother patching Flint at all. Just set those two environments variables. They will not mess up the build process in any way, and since they are variables, they could be set to something else. Setting CFLAGS is known to cause problems, but setting CFLAG64 or CXXFLAG64 will not cause any problems. 

If you do need to patch this again, then you can remove this code:


```
./test_gcc_version.sh
if [ $? -ne 0 ]; then
   echo "GCC version less than 3.4.0"
   echo "Flint will not be able to compile successfully"
   exit 1
fi
```


since 'prereq' will ensure that gcc is at least 4.0.1. That also means the file test_gcc_version.sh can be removed, as it is now redundant. 

Thinking about this 64-bit patching process in general, it is better to simply use CFLAG64 and CXXFLAG64 rather than -m64, and simply document the user must type


```
$ CFLAG64=-m64
$ export CFLAG64
$ CXXFLAG64=-m64
$ export CXXFLAG64
```


until such time as sage-env is updated. At which point, that will be unnecessary to do. That will avoid -m64 ever having to be hard-coded again, which is a good thing, as not all compilers accept that flag. 

I suspect this ticket can be closed as 'wontfix' as no fixes are needed, but I may be wrong. 

Dave


---

Comment by drkirkby created at 2010-01-29 18:22:45

Changing status from needs_review to needs_work.


---

Comment by jsp created at 2010-01-29 19:43:06

Replying to [comment:2 drkirkby]:
> It's not clear to me what is intended here. 
> 
>  * There is no such thing as CXXFLAG. Did you mean CXXFLAGS? 

I don't see anything alike in the patch file!?

>  * The point of CFLAG64 is that it would be set to whatever flag is needed to build 64 bit executables with a C compiler, which -m64 in most, but not all cases. 
>  * The point of CXXFLAG64 is that it would be set to whatever flag is needed to build 64 bit executables with a C++ compiler, which -m64 in most, but not all cases. 
> 
> 
> If Flint will build by setting the environment variables CFLAG64 and CXXFLAG64 to -m64, then I would not bother patching Flint at all. Just set those two environments variables. They will not mess up the build process in any way, and since they are variables, they could be set to something else. Setting CFLAGS is known to cause problems, but setting CFLAG64 or CXXFLAG64 will not cause any problems. 
> 

Are you shure flint will build that way?


> If you do need to patch this again, then you can remove this code:
> 
> {{{
> ./test_gcc_version.sh
> if [ $? -ne 0 ]; then
>    echo "GCC version less than 3.4.0"
>    echo "Flint will not be able to compile successfully"
>    exit 1
> fi
> }}}
> 
> since 'prereq' will ensure that gcc is at least 4.0.1. That also means the file test_gcc_version.sh can be removed, as it is now redundant. 
> 
> Thinking about this 64-bit patching process in general, it is better to simply use CFLAG64 and CXXFLAG64 rather than -m64, and simply document the user must type
> 
> {{{
> $ CFLAG64=-m64
> $ export CFLAG64
> $ CXXFLAG64=-m64
> $ export CXXFLAG64
> }}}
> 
> until such time as sage-env is updated. At which point, that will be unnecessary to do. That will avoid -m64 ever having to be hard-coded again, which is a good thing, as not all compilers accept that flag. 
> 
> I suspect this ticket can be closed as 'wontfix' as no fixes are needed, but I may be wrong. 
> 

We'll see.


> Dave 
>


---

Comment by jsp created at 2010-01-31 16:54:45

Changing status from needs_work to needs_review.


---

Comment by jsp created at 2010-01-31 16:54:45

Maybe the description was somewhat misleading or I was unclear over the meaning of this.

What I propose is:


```
if [ "x$SAGE64" = xyes ]; then
   FLINT_TUNE=" -fPIC -m64 -funroll-loops"
   export CFLAGS="$CFLAGS -m64"
   export CXXFLAGS="$CXXFLAGS -m64"
   export CFLAG64="$CFLAG64 -m64"
   export CXXFLAG64="$CXXFLAG -m64"
fi

```


Now if CFLAGS is empty the -m64 gets in.

See the patch.

Jaap


---

Comment by drkirkby created at 2010-02-21 00:44:52

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-02-21 00:44:52

This has been a bit messed up by me, as I made some changes which assumed we could set CFLAGS globally, but we can't. 

I'd proposed using CFLAG64 to be the C compiler flag(s) needed to build a 64-bit binary, which are usually -m64, but might not be. That could be set globally, but lets assume for now it is not. 

How would something like this seem:

If [ -z "$CFLAG64" ] ; then 
  CFLAG64=-m64
fi

(see how I did this in #8191) 

http://trac.sagemath.org/sage_trac/attachment/ticket/8191/R.patch

Then simply append $CFLAG64 to FLINT_TUNE. But remove the -m64, as we don't need both. 

Since CFLAGS and CXXFLAGS are not set in spkg-install, there is no point exporting them. Neither is there any point in exporting CFLAG64 or CXXFLAG64 as again they are not used by Flint. 

I think *all* that needs to be done is to set CFLAG64 to be -m64 unless it is set to something else, then ensure that for a 64-bit build, FLINT_TUNE gets $CFLAG64 included. 

Dave


---

Comment by jsp created at 2010-02-23 16:06:56

Changing status from needs_work to needs_review.


---

Comment by jsp created at 2010-02-23 16:06:56

Done as you suggested. We pass $CFLAG64 to FLINT_TUNE if SAGE64=yes.
But export CXXFLAG64 appropriate. See makefile.


```
# Since this code uses the C++ compiler as a linker to produce
# a library, the -m64 (or equivalent) option must be provided, as it
# it is in the line above where the target is libflint.dylib64

libflint.so: $(FLINTOBJ)
        $(CPP) $(CXXFLAG64) -fPIC -shared -o libflint.so $(FLINTOBJ) $(LIBS)
```




```
Found gcc 4 or later
g++  -m64 -fPIC -shared -o libflint.so zn_mod.o misc.o mul_ks.o pack.o mul.o mulmid.o mulmid_ks.o ks_support.o mpn_mulmid.o nuss.o pmf.o pmfvec_fft.o tuning.o mul_fft.o mul_fft_dft.o array.o invert.o mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o zmod_poly.o theta.o zmod_mat.o F_mpz.o tinyQS.o factor_base.o poly.o sieve.o linear_algebra.o block_lanczos.o NTL-interface.o -L/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib/ -L/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib/  -lgmp -lpthread -lntl -lm 
Deleting old FLINT
Installing new library file

```



New spkg with the same name:
[http://boxen.math.washington.edu/home/jsp/ports/flint-1.5.0.p4.spkg](http://boxen.math.washington.edu/home/jsp/ports/flint-1.5.0.p4.spkg)


Jaap


---

Attachment


---

Comment by drkirkby created at 2010-03-03 18:30:46

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-03-03 18:30:46

Your fix resolves the issues we have, and is unlikely to break anything (see below for a possible exception). I do have a few comments that are worth documenting. 

 * I was a bit concerned that -funroll-loops will be enabled when SAGE64 is set to yes, despite the fact that it supposed to crash on an UltraSPARC III+ processor. (Previously -funroll-loops was disabled on Solaris SPARC). However, testing showed this will *not* build on Solaris 10 in 64-bit mode on SPARC, irrespective of whether -funroll-loops is set or not. Therefore the inclusion of -funroll-loops is not causing any extra problems on SPARC, and might actually improve performance when the issues are resolved on 64-bit SPARC. 

 * There was no need to export CXXFLAG64, as Flint will not use it, but it can do no harm whatsoever.

 * I'm changing the title slightly, from CFLAGS to FLINT_TUNE, as CFLAGS is not used directly in the spkg-install. It is FLINT_TUNE that gets set


```
drkirkby`@`redstart:~/fresh/sage-4.3.3/spkg/standard/flint-1.5.0.p4$ grep CFLAGS spkg-install
drkirkby`@`redstart:~/fresh/sage-4.3.3/spkg/standard/flint-1.5.0.p4$ 
```


Positive review.


---

Comment by mhansen created at 2010-03-06 08:39:31

Resolution: fixed
