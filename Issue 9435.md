# Issue 9435: sage-4.5.alpha3 fails on bsd.math

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-07-06 12:10:50

Assignee: tbd

... and I haven't yet tried this version on any other OS X platforms. Reported by William Stein:


```
This fails completely to build on bsd.math.washington.edu (OS X 10.6).

/i686-apple-darwin10/4.2.1/../../.. -lSystem
checking for dummy main to link with Fortran 77 libraries... none
checking for Fortran 77 name-mangling scheme... unknown
configure: WARNING: unknown Fortran name-mangling scheme
checking whether sage_fortran appends underscores to external names... unknown
configure: error: cannot use Fortran
Error configuring R.

real    1m10.765s
user    0m10.200s
sys     0m16.450s
sage: An error occurred while installing r-2.10.1.p2
```



---

Comment by mpatel created at 2010-07-07 07:35:38

Sage 4.5.alpha4 builds for me on bsd.math with `env MAKE="make -j4" make build`.  I did not set any `SAGE_*` variables.  The long doctests pass.

By the way, Maxima is built _after_ the Sage library:

```sh
$ ls -ltr spkg/installed | tail -15
8 -rw-r--r--  1 mpatel  staff  287 Jul  6 23:11 sage-4.5.alpha4
8 -rw-r--r--  1 mpatel  staff  285 Jul  6 23:12 gap-4.4.12.p4
8 -rw-r--r--  1 mpatel  staff  287 Jul  6 23:14 gfan-0.4plus.p1
8 -rw-r--r--  1 mpatel  staff  294 Jul  6 23:14 lcalc-20100428-1.23.p0
8 -rw-r--r--  1 mpatel  staff  288 Jul  6 23:24 maxima-5.20.1.p1
8 -rw-r--r--  1 mpatel  staff  285 Jul  6 23:27 moin-1.9.1.p1
8 -rw-r--r--  1 mpatel  staff  283 Jul  6 23:27 palp-1.1.p3
8 -rw-r--r--  1 mpatel  staff  285 Jul  6 23:28 sagetex-2.2.5
8 -rw-r--r--  1 mpatel  staff  293 Jul  6 23:28 polytopes_db-20100210
8 -rw-r--r--  1 mpatel  staff  284 Jul  6 23:28 pil-1.1.6.p2
8 -rw-r--r--  1 mpatel  staff  284 Jul  6 23:38 scipy-0.7.p5
8 -rw-r--r--  1 mpatel  staff  297 Jul  6 23:38 scipy_sandbox-20071020.p5
8 -rw-r--r--  1 mpatel  staff  289 Jul  6 23:39 sympow-1.018.1.p7
8 -rw-r--r--  1 mpatel  staff  292 Jul  6 23:39 tachyon-0.98beta.p11
8 -rw-r--r--  1 mpatel  staff  286 Jul  6 23:39 weave-0.4.9.p0
```

But I don't know if this is significant.


---

Comment by rlm created at 2010-07-09 09:11:13

Fortran and R were both updated in sage-4.5.alpha0. Can someone try replacing the R spkg with the old one, to see if it is that or the new fortran spkg which is causing this?


---

Comment by drkirkby created at 2010-07-09 14:48:54

#9464 might (probably is) the cause of this.


---

Comment by drkirkby created at 2010-07-09 16:54:32

Replying to [comment:3 drkirkby]:
> #9464 might (probably is) the cause of this. 
John Palmieri has rather dashed that hope, so the reasons for this failure are almost certainly not related to #9464.


---

Comment by drkirkby created at 2010-07-09 20:18:49

Is William's problem reproducible by others? I just took:

 * host bad.math.washington.edu
 * sage-4.5.alpha4
 * An updated R, which disables the ICU library when SAGE_FAT_BINARY is set to "yes". This is #9396 (But I did *not* set SAGE_FAT_BINARY)
 * The updated deps at #9464 which makes 'deps' look a bit cleaner.
Set typed the following.  


``` 
$ export MAKE="make -j6"
$ export SAGE_PARALLEL_SPKG_BUILD=yes
$ make
```


R builds OK for me on bsd.math. Then Sage completes the build. 

```
dumping object inventory... done
build succeeded.
Build finished.  The built documents can be found in /Users/kirkby/sage-4.5.alpha4/devel/sage/doc/output/html/fr/tutorial
[kirkby`@`bsd sage-4.5.alpha4]$ make ptestlong
cd spkg && ./install all 2>&1 | tee -a ../install.log
make[1]: Nothing to be done for `all'.

real	0m0.099s
user	0m0.004s
sys	0m0.007s
To install gap, gp, singular, etc., scripts
in a standard bin directory, start sage and
type something like
   sage: install_scripts('/usr/local/bin')
at the Sage command prompt.

To build the documentation, run
   make doc

Sage build/upgrade complete!
```


I do not believe the updated deps or R will make any difference. 
 * The updated R only disables the ICU library if SAGE_FAT_BINARY is set to "yes", but I did not set it to yes, so it would have had no effect. 
 * The updated 'deps' makes the dependency of R on Fortran clearer, but it is implied via a long chain rule, so it should not be necessary. 

Anyway, it works for me, as it does for Mitesh. 

Dave


---

Comment by rlm created at 2010-07-11 19:49:47

Changing status from new to needs_info.


---

Comment by rlm created at 2010-07-18 09:48:31

Resolution: worksforme


---

Comment by rlm created at 2010-07-18 09:48:31

Fixed by adding Python to the deps for Fortran, change to deps file is on ticket #9368.
