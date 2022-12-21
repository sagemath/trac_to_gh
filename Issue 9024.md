# Issue 9024: tachyon is buiding 32-bit on OpenSolaris x64 even when SAGE64 is set to "yes"

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-23 22:05:30

Assignee: drkirkby

'tachyon' has a script called 'Make-arch' which has various architectures. But there was not one for 64-bit Solaris on x86. The code in Sage currently uses the target 'solaris-pthreads-gcc' - see below


```
if [ $UNAME = "SunOS" ]; then
    make solaris-pthreads-gcc
    finished
fi
```


That target consists of the lines:


```
solaris-pthreads-gcc:
        $(MAKE) all \
        "ARCH = solaris-pthreads-gcc" \
        "CC = gcc" \
        "CFLAGS = -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS $(MISCFLAGS) -DTHR -DUSEPOSIXTHREADS" \
        "AR = ar" \
        "ARFLAGS = r" \
        "STRIP = strip" \
        "LIBS = -L. -ltachyon $(MISCLIB) -lm -lpthread"
```


Note there are two problems with this. 

 * '-O6' is not an option for gcc. 
 * There is no option to make this build 64-bit objects. 

These problems should be easily solved. 





---

Comment by drkirkby created at 2010-05-23 22:26:31

The attached patch has a new target which I called 'solaris-pthreads-gcc-64-bit'


```
solaris-pthreads-gcc-64-bit:
        $(MAKE) all \
        "ARCH = solaris-pthreads-gcc" \
        "CC = gcc" \
        "CFLAGS = -Wall -O4 -m64 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS $(MISCFLAGS) -DTHR -DUSEPOSIXTHREADS" \
        "AR = ar" \
        "ARFLAGS = r" \
        "STRIP = strip" \
        "LIBS = -L. -ltachyon $(MISCLIB) -lm -lpthread"

```


Note the '-O6' has been changed to '-O4' and a -m64 added. The revised spkg-install then builds tachyon differently for 32 and 64-bit builds. 


```
if [ $UNAME = "SunOS" ]; then
    if [ "x$SAGE64" = xyes ] ; then
       # There was nothing suitable for 64-bit mode with 
       # gcc, so I made a new target. David Kirkby, May 2010. 
       make solaris-pthreads-gcc-64-bit
    else
       make solaris-pthreads-gcc
    fi
    finished
fi
```


The new package can be found at:

http://boxen.math.washington.edu/home/kirkby/patches/tachyon-0.98beta.p11.spkg

Note:

The file patches/Make-arch.patch was a bit out of date - someone had obviously updated patches/Make-arch without changing patches/Make-arch.patch. This has now been resolved too. 

Dave


---

Comment by drkirkby created at 2010-05-23 22:26:31

Changing status from new to needs_review.


---

Attachment

Mercurial patch to allow to build 64-bit on Solaris (both SPARC and x64)


---

Comment by drkirkby created at 2010-05-24 18:23:41

For other OpenSolaris issues, see #9026


---

Comment by jsp created at 2010-06-10 15:59:07

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-06-10 15:59:07

Looks ok to me on Open Solaris:



```
Successfully installed tachyon-0.98beta.p11
You can safely delete the temporary build directory
/export/home/jaap/sage_port/sage-4.4.3/spkg/build/tachyon-0.98beta.p11
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing tachyon-0.98beta.p11.spkg
-bash-4.0$ file local/bin/tachyon 
local/bin/tachyon:      ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, stripped
-bash-4.0$ 

```


Also tested on other platforms (Fedora 32 bit and 64 bit)

Positive review.

Jaap


---

Comment by mhansen created at 2010-06-11 18:31:54

Merged http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p11.spkg which just adds a description to the entry in SPKG.txt


---

Comment by mhansen created at 2010-06-11 18:31:54

Resolution: fixed
