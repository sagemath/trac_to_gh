# Issue 4959: r's install_packages is broken in many variants of sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-09 16:36:50

Assignee: mabshoff

CC:  jason mvngu

See, e.g., this from sage-devel

```
I had a similar failure today, trying to:

r.install_packages("adapt")

after some fussing, runing ./sage as root, and using the notebook
interface I could get through the download phase, but same sorts of
failures in just as the gcc kicks in.  Seems several of the key R
scripts have "/home/wstein/..."  hard wired in to R_HOME_XXX, which
obviously will fail.  I tried editing the R startup scripts (among
others) but couldn't get it to work.

BTW, I installed from the latest Debian tarball into a Debian/VMWARE
machine just today.  So installing R packages is still an issue.
```


Since most of the value of R is the huge list of third party packages, it's very important that this get fixed. 


---

Comment by kcrisman created at 2009-12-11 20:07:01

See also #5246, which reports an extremely similar problem.  

Incidentally, I have not had this problem at all in downloading a number of packages, and others have reported success lately, so it is possible this was specific to a certain release because of weird hard coding of links environment variables.  This should be tested on a few different machines with packages that do not rely on the 'recommended' packages (see #2198 and #6532 for why).


---

Comment by kcrisman created at 2009-12-14 16:05:05

Incidentally, the R package above has been removed from R, it seems.   It also seems this person was using the Debian install, which is now of course woefully out of date.


---

Comment by kcrisman created at 2009-12-14 16:48:49

On sage.math, after picking the mirror, I get one error message for trying to install 'abind' from the r console:

```
Warning message:
In doTryCatch(return(expr), name, parentenv, handler) :
  unable to load shared library '/home/.../sage-4.3.r0-sage.math.washington.edu-x86_64-Linux/local/lib/R//modules//R_X11.so':
  /scratch/mhansen/release/4.3/rc0/sage-4.3.rc0/local/lib/gcc-lib/x86_64-unknown-linux-gnu/4.0.3/libgcc_s.so.1: version `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6)
Segmentation fault
```

but a different one when trying to use the r.install_packages() interface, which I unfortunately deleted.


---

Comment by kcrisman created at 2009-12-14 18:31:54

Here is the error message from that:

```
Warning messages:
1: In file.create(f.tg) :
  cannot create file '/scratch/mhansen/release/4.3/rc0/sage-4.3.rc0/local/lib/R/doc/html/packages.html', reason 'Permission denied'
2: In tools:::unix.packages.html(.Library) :
  cannot create HTML package index
> 
```

So again there seem to be problems with hard links in the R installation, since my binary wasn't in /scratch and certainly not in mhansen's scratch.


---

Comment by kcrisman created at 2009-12-27 03:39:44

And see [here](http://groups.google.com/group/sage-devel/browse_thread/thread/7f81537bf81cc05c/dd5d592c0e27966c?q=)  for reports on several other platforms.


---

Comment by kcrisman created at 2009-12-28 17:07:52

The behavior with the version `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6) continues to be the case on boxen.math after the upgrade at #6532.  On the plus side, it no longer refers to someone else's installation.

Here is another interesting error which might help us - is it possible that a number of R packages require non-universal libraries?
{{{* installing *source* package ‘rgl’ ...
checking for gcc... gcc -std=gnu99
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables... 
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc -std=gnu99 accepts -g... yes
checking for gcc -std=gnu99 option to accept ISO C89... none needed
checking how to run the C preprocessor... gcc -std=gnu99 -E
checking for gcc... (cached) gcc -std=gnu99
checking whether we are using the GNU C compiler... (cached) yes
checking whether gcc -std=gnu99 accepts -g... (cached) yes
checking for gcc -std=gnu99 option to accept ISO C89... (cached) none needed
checking for libpng-config... yes
configure: using libpng-config
configure: using libpng dynamic linkage
checking for X... libraries /usr/lib, headers /usr/include
checking GL/gl.h usability... no
checking GL/gl.h presence... no
checking for GL/gl.h... no
checking GL/glu.h usability... no
checking GL/glu.h presence... no
checking for GL/glu.h... no
configure: error: missing required header GL/gl.h
ERROR: configuration failed for package ‘rgl’
}}}
This was on boxen.math; on my own Mac I did not have any problems with this package (a package installed by the package 'depth', which I needed for some other computations).  This tells me that


---

Comment by kcrisman created at 2010-01-25 19:18:21

With the Fortran issues in #7485 cleared up, #6532 seems to now work to fix this.  We can definitely get rid of the warning for OSX!  Look on #7521 for that.


---

Comment by mvngu created at 2010-01-25 23:26:12

Close as fixed by #6532.


---

Comment by mvngu created at 2010-01-25 23:26:12

Resolution: fixed
