# Issue 455: scipy picks /usr/local/lib/libfftw3.a instead of $SAGE_LIB/libfftw3.a

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-19 08:56:19

Assignee: was

CC:  jason mvngu

Reported by JMD:

system : AMD64 X2 4200
             Slamd64  (Slackware 11.0 for x86-64)
             gcc 3.4.6

Here it seems that /usr/local/lib/libfftw3.a on my system is used,
maybe instead of something inside sage-2.8/

log :   gcc: build/src.linux-x86_64-2.5/Lib/fftpack/_fftpackmodule.c
sage_fortran -shared -shared build/temp.linux-x86_64-2.5/build/
src.linux-x86_64-2.5/Lib/fftpack/_fftpackmodule.o build/temp.linux-
x86_64-2.5/Lib/fftpack/src/zfft.o build/temp.linux-x86_64-2.5/Lib/
fftpack/src/drfft.o build/temp.linux-x86_64-2.5/Lib/fftpack/src/
zrfft.o build/temp.linux-x86_64-2.5/Lib/fftpack/src/zfftnd.o build/
temp.linux-x86_64-2.5/build/src.linux-x86_64-2.5/fortranobject.o -L/
usr/local/lib -Lbuild/temp.linux-x86_64-2.5 -ldfftpack -lfftw3 -o
build/lib.linux-x86_64-2.5/scipy/fftpack/_fftpack.so
ld: /usr/local/lib/libfftw3.a(mapflags.o): relocation R_X86_64_32
against `a local symbol' can not be used when making a shared object;
recompile with -fPIC
/usr/local/lib/libfftw3.a: ne peut lire les symboles: Mauvaise valeur
ld: /usr/local/lib/libfftw3.a(mapflags.o): relocation R_X86_64_32
against `a local symbol' can not be used when making a shared object;
recompile with -fPIC
/usr/local/lib/libfftw3.a: ne peut lire les symboles: Mauvaise valeur
error: Command "sage_fortran -shared -shared build/temp.linux-
x86_64-2.5/build/src.linux-x86_64-2.5/Lib/fftpack/_fftpackmodule.o
build/temp.linux-x86_64-2.5/Lib/fftpack/src/zfft.o build/temp.linux-
x86_64-2.5/Lib/fftpack/src/drfft.o build/temp.linux-x86_64-2.5/Lib/
fftpack/src/zrfft.o build/temp.linux-x86_64-2.5/Lib/fftpack/src/
zfftnd.o build/temp.linux-x86_64-2.5/build/src.linux-x86_64-2.5/
fortranobject.o -L/usr/local/lib -Lbuild/temp.linux-x86_64-2.5 -
ldfftpack -lfftw3 -o build/lib.linux-x86_64-2.5/scipy/fftpack/
_fftpack.so" failed with exit status 1
Error building scipy. 

The problem goes away when /usr/local/lib/libfftw3.a is moved.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-12 08:57:05

This problem can be fixed by patching the default locations the build system looks for libraries. We should disallow /usr and /usr/local and on OSX the various places for Fink and MacPorts since more than likely some random crap will be pulled in that way.

Cheers,

Michael


---

Comment by jason created at 2009-02-12 10:02:19

IIRC, fftw is stripped out of the scipy 0.7 release, so this problem may go away, right?

On the other hand, we'll probably miss fftw, since I understand that in at least some cases, it is faster than the default scipy fftpack.


---

Comment by mabshoff created at 2009-02-12 10:10:58

Replying to [comment:4 jason]:
> IIRC, fftw is stripped out of the scipy 0.7 release, so this problem may go away, right?

IIRC there is still some fft support, but the point is that we should not pick up random crap. 

> On the other hand, we'll probably miss fftw, since I understand that in at least some cases, it is faster than the default scipy fftpack.

Yes, we need to figure out what to do about that. 

I have changed the ticket summary to reflect the intention. I know how to do this, so we can do it during the scipy 0.7 update.

Cheers,

Michael


---

Comment by kcrisman created at 2009-12-30 04:39:34

Scipy is now in version 0.7.0 in Sage.  Has this been done elsewhere in the meantime?  (Perhaps not, since I still need to remove /sw from my own PATH on Mac).


---

Comment by jason created at 2010-06-11 06:39:20

I wonder if #9208 and #9210 make it so that you don't need to remove /sw from your path anymore.

I don't believe that fftw3 is used anymore in scipy:


```
~/sage% grep "lfftw3" install.log
~/sage%  
```


So I think this ticket can safely be closed.


---

Comment by jason created at 2010-06-11 06:40:34

(there might be other /usr/local/ libs that are picked up, but fftw won't be since it's not used)


---

Comment by kcrisman created at 2012-07-07 04:12:37

> I wonder if #9208 and #9210 make it so that you don't need to remove /sw from your path anymore.
That might be dangerous.
> So I think this ticket can safely be closed.
So... positive review, sage-invalid?  I'll let you make the call.


---

Comment by mhansen created at 2013-07-22 15:37:47

Resolution: invalid


---

Comment by mhansen created at 2013-07-22 15:37:47

I think we should mark it as invalid.
