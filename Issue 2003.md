# Issue 2003: gnutls configure script finds local copy of guile when it shouldn't

Issue created by migration from https://trac.sagemath.org/ticket/2003

Original creator: justin

Original creation time: 2008-01-31 18:34:54

Assignee: mabshoff

On Mac OS X (10.4.11 in my case), when the configure script for 'gnutls' runs, it will detect 'guile' and attempt to build the Guile bindings, if it finds a locally-installed Guile package (in my case, from MacPorts, in "/opt").  This causes the build to break.


```
checking whether building Guile bindings... yes
***
*** Detecting GNU Guile...

checking for guile-snarf... /opt/local/bin/guile-snarf
checking for guile... /opt/local/bin/guile
checking for guile-config... /opt/local/bin/guile-config
checking for guile-tools... /opt/local/bin/guile-tools
checking libguile compile flags... -I/opt/local/include -D_THREAD_SAFE
checking libguile link flags... -D_THREAD_SAFE  -lguile -lltdl -L/opt/ 
local/lib -L/opt/local/lib -lgmp -lm -lltdl
checking whether GNU Guile is recent enough... yes

make[5]: warning: -jN forced in submake: disabling jobserver mode.
/opt/local/bin/guile -L ../../guile/modules make-enum-map.scm > enum-map.i.c
/opt/local/bin/guile -L ../../guile/modules make-smob-types.scm > smob-types.i.c
/opt/local/bin/guile -L ../../guile/modules make-enum-header.scm > enums.h
ERROR: In procedure dynamic-link:
ERROR: file: "libguile-srfi-srfi-1-v-3", message: "dlopen(libguile-srfi-srfi-1-v-3.s
o, 9): image not found"
make[5]: *** [enum-map.i.c] Error 1
make[5]: *** Waiting for unfinished jobs....
ERROR: In procedure dynamic-link:
ERROR: file: "libguile-srfi-srfi-1-v-3", message: "dlopen(libguile-srfi-srfi-1-v-3.s
o, 9): image not found"
make[5]: *** [enums.h] Error 1
make[4]: *** [all-recursive] Error 1
make[3]: *** [all-recursive] Error 1
make[2]: *** [all] Error 2
failed to build GNUTLS
```


If the PATH variable does not give access to the installed Guile package, the build proceeds without a problem.

I think this is a bug, since building Sage should be independent of the packages installed elsewhere on the system (that is why Sage has so many pieces, after all).

Some possible fixes:
  - force the PATH variable to some plain-vanilla setting.
  - use the "-norc" and "-noprofile" switches when starting subshells
     (and maybe make sure the shells are not 'login' or 'interactive')
  - force the building of 'gnutls' to avoid this particular problem
     (I think this can be done with "--enable-guile=no' in the configure
     script)





---

Comment by mabshoff created at 2008-01-31 22:50:15

Hi Justin, 

I am not sure if disabling guile support will work as you suggest, i.e. `--enable-guile=no`, but the spkg at 

http://sage.math.washington.edu/home/mabshoff/SPKG/gnutls-2.2.1.p1.spkg

does that. I don't think your other suggestions will work since it will break the build for other people. It might actually be also worth to fix the issue by fixing the Makefiles.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-31 22:50:23

Changing status from new to assigned.


---

Comment by justin created at 2008-02-03 05:50:13

Based on my experience with 2.10.1.rc[345], this can be overcome the 'configure' flag "--enable-guile=no".  That seems to be the most straight-forward solution.


---

Comment by mabshoff created at 2008-02-03 16:05:16

Replying to [comment:3 justin]:
> Based on my experience with 2.10.1.rc[345], this can be overcome the 'configure' flag "--enable-guile=no".  That seems to be the most straight-forward solution.
> 

Hi Justin,

this is exactly what the updated gnutls.spkg linked above does. So if it works for you you should give it a positive review so that I can merge it into 2.10.2.alpha0 :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-04 05:04:53

Merged in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-04 05:04:53

Resolution: fixed
