# Issue 9346: sage_fortran no longer works for 32-bit builds on Solaris.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-06-26 18:06:03

Assignee: drkirkby

CC:  mpatel jsp

A recent update to the sage_fortran package (#7982), was made to aid the creation of 64-bit object files when the environment variable SAGE64 was set to yes. The patch accomplished that task. 

Unfortunately, this was as the cost of 32-bit object files. 

Instead of the file sage_fortran being a small script to invoke the Fortran compiler, it is now a broken script.


```
$ cat local/bin/sage_fortran
#!/bin/sh 
```


Since a 64-bit port is not complete and this breaks a 32-bit build, it means Sage is totally broken on Solaris. 

Fortunately the required change is very small indeed. 




---

Comment by jhpalmieri created at 2010-06-26 22:41:15

I tried building on t2 and was wondering what the problem is; thanks for figuring it out.

Using mpatel's completely sensible suggestion at #7982, I created a new spkg, available at [http://sage.math.washington.edu/home/palmieri/SPKG/fortran-20100626.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/fortran-20100626.spkg).  I'm attaching the output from "hg -diff" as a patch file so you can see what changed.


---

Comment by jhpalmieri created at 2010-06-26 22:41:15

Changing status from new to needs_review.


---

Attachment

By the way, this spkg is not compressed, so if you want to manually extract it, type "tar xf ..." rather than "tar jxf ...".  (The uncompressed version ended up being a little smaller than the compressed one, and is faster to create and to uncompress.)


---

Comment by drkirkby created at 2010-06-27 11:57:23

Thanks John for fixing this. An interesting, but not surprising observation that this is smaller if left uncompressed. At some point we next update this, I believe it would be sensible to add that as a special build instruction, but its not important - it will work either way. 

This whole way Sage builds fortran source code seems a bit odd to me. Why we can't do it like other program do, I will never know. Even if we ship a fortran binary, the process could be simplified a lot.  

That aside, this updated package works well. I've checked this with both a 64-bit build, and a _simulated_ 32-bit build. Some care needs to be taken in swapping these, as this is more involved than simply setting or unsetting `SAGE64`. 

 == Testing in a simulated 32-bit build ==
 * The file `local/lib/sage-64.txt ` must be removed to simulate a 32-bit environment. This gets created automatically in the build process if SAGE64 is set to "yes" and is a safety feature to stop someone starting a 64-bit build then upgrading Sage, without setting SAGE64 to "yes", resulting in a mixture of binaries. 
 * The variable `SAGE_FORTRAN_LIB ` variable must be made to point to a 32-bit library (in my case `/usr/local/gcc-4.4.4-multilib/lib/libgfortran.so` This was not essential for testing fortran-20100626, but it is essential if one wishes to swap build environments fully. 
 * `SAGE64` must obviously be unset.  

Once that happens, 


```
Successfully installed fortran-20100626
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.5.alpha0/spkg/build/fortran-20100626
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing fortran-20100626.spkg

```

We can see that local/lib/libgfortran.so points to where my 32-bit libgfortran library will be. and that the sage_fortran script looks sensible (unlike before) and it does not have an -m64 flag. 


```
drkirkby`@`hawk:~/sage-4.5.alpha0$ ls -l local/lib/libgfortran.so
lrwxrwxrwx   1 drkirkby staff         48 Jun 27 12:18 local/lib/libgfortran.so -> /usr/local/gcc-4.4.4-multilib/lib/libgfortran.so
drkirkby`@`hawk:~/sage-4.5.alpha0$ cat local/bin/sage_fortran
#!/bin/sh 

/usr/local/gcc-4.4.4-multilib/bin/gfortran -fPIC $`@`
```


So I'm happy that will work in a 32-bit environment, but I also know you have tested it, and Metesh tested his code also. I don't have a 32-bit build system around at the minute to test it more vigorously. 

## Testing in a 64-bit environment
To restore back to a 64-bit environment:

```
drkirkby`@`hawk:~/sage-4.5.alpha0$ touch local/lib/sage-64.txt
drkirkby`@`hawk:~/sage-4.5.alpha0$ export SAGE_FORTRAN_LIB=/usr/local/gcc-4.4.4-multilib/lib/amd64/libgfortran.so
drkirkby`@`hawk:~/sage-4.5.alpha0$ export SAGE64=yes
```

Then I could test the package

```
drkirkby`@`hawk:~/sage-4.5.alpha0$ ./sage -f fortran-20100626
Force installing fortran-20100626
Calling sage-spkg on fortran-20100626
<SNIP>
fortran-20100626/src/gfortran/fortran-OSX64-20090120/spkg-install
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: /export/home/drkirkby/gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4-multilib --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.4.4-multilib --with-mpfr=/usr/local/gcc-4.4.4-multilib --disable-nls --enable-checking=release --enable-werror=no --enable-multilib --with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld
Thread model: posix
gcc version 4.4.4 (GCC) 
****************************************************
cd "/export/home/drkirkby/sage-4.5.alpha0/local/lib/"; ln -sf "/usr/local/gcc-4.4.4-multilib/lib/amd64/libgfortran.so" .

real	0m0.039s
user	0m0.015s
sys	0m0.022s
Successfully installed fortran-20100626
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.5.alpha0/spkg/build/fortran-20100626
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing fortran-20100626.spkg
```

With the package installed, I could check the library created by the package now points to a 64-bit library


```
drkirkby`@`hawk:~/sage-4.5.alpha0$ ls -l local/lib/libgfortran.so
lrwxrwxrwx   1 drkirkby staff         54 Jun 27 12:22 local/lib/libgfortran.so -> /usr/local/gcc-4.4.4-multilib/lib/amd64/libgfortran.so
drkirkby`@`hawk:~/sage-4.5.alpha0$ cat local/bin/sage_fortran
#!/bin/sh 

/usr/local/gcc-4.4.4-multilib/bin/gfortran -m64 -fPIC $`@`
```


The resulting sage_fortran script looks fine. I then started, but quickly stopped the installation of lapack-20071123.p1 and confirmed the object files created were 64-bit. 

So positive review. I put Mitesh Patel as an author too, as it was his code that solved this, though John made the package.


---

Comment by drkirkby created at 2010-06-27 11:57:23

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-06-27 16:18:45

Replying to [comment:3 drkirkby]:

> That aside, this updated package works well. I've checked this with both a 64-bit build, and a _simulated_ 32-bit build. 

It also works for me on t2 with SAGE64 not set and no file `local/lib/sage-64.txt` present.  At various points in the build process, it says that it's 32-bit.

> So positive review. I put Mitesh Patel as an author too, as it was his code that solved this, though John made the package. 

Right, I should have done that in the first place.


---

Comment by rlm created at 2010-06-28 16:58:56

Resolution: fixed


---

Comment by drkirkby created at 2010-06-28 23:33:08

This has an error in it. Ideally the error needs resolving before alpha1 is released. 

#9368 tracks this error. Basically the line text 


```
 OS == "sunos" and 
```


needs removing. 

Dave
