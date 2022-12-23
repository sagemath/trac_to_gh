# Issue 9978: Cliquer fails to install on AIX 5.3 as getopt.h does not exist

Issue created by migration from https://trac.sagemath.org/ticket/9979

Original creator: drkirkby

Original creation time: 2010-09-23 15:40:37

Assignee: drkirkby

CC:  chapoton

Using the following system: 

 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * DDS-4 tape drive 

Cliquer failed to install due to a lack of `getopt.h` It can't determine the platform, which probably does not help the situation. 


```
Cannot determine your platform or it is not supported
Since SAGE_PORT is set, setting SAGESOFLAGS to Linux defaults.
make[2]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/cliquer-1.2.p7/src'
make[2]: warning: jobserver unavailable: using -j1.  Add `+' to parent make rule.
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c
cl.c:7:20: error: getopt.h: No such file or directory
cl.c: In function 'read_options':
cl.c:324: error: array type has incomplete element type
cl.c:325: error: 'no_argument' undeclared (first use in this function)
cl.c:325: error: (Each undeclared identifier is reported only once
cl.c:325: error: for each function it appears in.)
cl.c:328: error: 'required_argument' undeclared (first use in this function)
cl.c:339: warning: implicit declaration of function 'getopt_long'
cl.c:324: warning: unused variable 'long_options'
```


It's quite possible that an installation of an AIX fileset would include the file `getopt.h`, but it looks like its a header will should at least consider checking for. However, comments on #9870 suggest we do not need the Cliquer executable (only the libraries), in which case there's no need for `getopt`. 




---

Comment by leif created at 2010-09-24 12:10:22

Yes, if we only (properly) build a shared library rather than the executable, we don't need it.

This will some day be fixed by #9870 I guess.

You could nevertheless report this upstream. (I think Cliquer should at least check for the presence of `getopt.h`.)


---

Comment by embray created at 2019-01-15 18:39:07

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).


---

Comment by mkoeppe created at 2020-06-23 21:26:55

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

We should close this ticket as outdated.


---

Comment by chapoton created at 2020-06-25 13:33:23

Resolution: invalid
