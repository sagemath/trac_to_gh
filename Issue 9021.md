# Issue 9021: gdmodule not building on OpenSolaris x64.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-23 17:27:24

Assignee: drkirkby

## Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.4.2
 * gcc 4.4.4

## How gcc 4.4.4 was configured
Since the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. 


```
drkirkby`@`hawk:~/sage-4.4.2$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
```


gcc 4.3.4 was failing to build iconv. 

## How the Sage build was attempted
 * 64-bit build. SAGE64 was set to "yes"
 * #9008 update zlib to latest upstream release to allow a 64-bit library to be built. 
 * #9009 update mercurial spkg to build 64-bit.
 * #7982 update sage_fortran so it can build 64-bit binaries.

## The problem


```
_gdmodule.c: In function ‘image_stringup’:
_gdmodule.c:1022: warning: pointer targets in passing argument 5 of ‘gdImageStringUp’ differ in signedness
/export/home/drkirkby/sage-4.4.2/local/include/gd.h:365: note: expected ‘unsigned char *’ but argument is of type ‘char *’
_gdmodule.c: In function ‘image_stringup16’:
_gdmodule.c:1037: warning: passing argument 5 of ‘gdImageStringUp16’ from incompatible pointer type
/export/home/drkirkby/sage-4.4.2/local/include/gd.h:369: note: expected ‘short unsigned int *’ but argument is of type ‘Py_UNICODE *’
error: command 'gcc' failed with exit status 1
Failure to build gdmodule

real	0m0.134s
user	0m0.098s
sys	0m0.032s
sage: An error occurred while installing gdmodule-0.56.p7
```


## Likely Reason
It looks like a 32-bit build is being used, but it's not so obvious how to fix this - it is not the normal SAGE64/OS X issue.


---

Comment by leif created at 2010-05-23 22:54:07

If you're willing to accept a short informal "inline" patch, try adding something like

```
extra_args = ["-m64"] if os.environ.get("SAGE64", "no")=="yes" else []
```

right after the Cygwin patch (at top level in `patches/Setup.py`, and add

```
            extra_compile_args=extra_args, extra_link_args=extra_args,
```

to the `Extension` constructor call below.

-Leif


Sorry for the inconvenience, but I'm currently unable to create a patch...


---

Comment by leif created at 2010-05-23 23:14:27

Oh, the "usual" method of setting/modifying `CFLAGS` et al. in `spkg-install` _should_ work, too.


---

Attachment

Modifies `patches/Setup.py` to honor `$SAGE64`. Testing is up to you!


---

Comment by leif created at 2010-05-24 18:06:52

I've uploaded a Mercurial patch that modifies `patches/Setup.py` as suggested above.

Note that `patches/Setup.py.patch` isn't used by `spkg-install`, so I haven't updated that.

The patch has to be tested before bumping to p8 (and updating `SPKG.txt`, which already lacks some modification history).


---

Comment by drkirkby created at 2010-05-24 18:25:02

For other OpenSolaris issues, see #9026


---

Comment by drkirkby created at 2010-06-05 22:18:09

Replying to [comment:3 leif]:
> I've uploaded a Mercurial patch that modifies `patches/Setup.py` as suggested above.
> 
> Note that `patches/Setup.py.patch` isn't used by `spkg-install`, so I haven't updated that.
> 
> The patch has to be tested before bumping to p8 (and updating `SPKG.txt`, which already lacks some modification history).

Thank you, I'll try this. 

Dave


---

Comment by drkirkby created at 2011-04-02 13:33:24

This can be closed as fixed. 

I don't have a clue where it was fixed. Despite this was reported against gdmodule-0.56.p7, the current version in Sage is still gdmodule-0.56.p7. The latest entry in SPKG.txt shows gdmodule-0.56.p5, so at least two updates have not been documented properly. 

Dave


---

Comment by jdemeyer created at 2011-04-05 15:49:34

Resolution: worksforme
