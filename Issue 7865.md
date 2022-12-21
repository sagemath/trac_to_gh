# Issue 7865: R  - WARNING: cannot run mixed C/Fortran code (then exits)

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-07 05:47:58

Assignee: drkirkby

CC:  jsp dimpase

## Build environment
 * Sun Ultra 27 3.333 GHz Intel Xeon. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)
 * gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
 * 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 
 
## The problem

```
checking for inline... inline
checking for int... yes
checking size of int... 4
checking for long... yes
checking size of long... 8
checking for long long... yes
checking size of long long... 8
checking for double... yes
checking size of double... 8
checking for long double... yes
checking size of long double... 16
checking for size_t... (cached) yes
checking size of size_t... 8
checking whether we can compute C Make dependencies... yes, using gcc -std=gnu99 -MM
checking whether gcc -std=gnu99 supports -c -o FILE.lo... yes
checking how to get verbose linking output from sage_fortran... -v
checking for Fortran 77 libraries of sage_fortran...  -L/lib/64 -L/usr/lib/64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib/ -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/amd64 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../amd64 -L/lib/amd64 -L/usr/lib/amd64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../.. -lgfortranbegin -lgfortran -lm
checking how to get verbose linking output from gcc -std=gnu99... -v
checking for C libraries of gcc -std=gnu99...  -L/lib/64 -L/usr/lib/64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib/ -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/amd64 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../amd64 -L/lib/amd64 -L/usr/lib/amd64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../.. -lgcc_eh
checking for dummy main to link with Fortran 77 libraries... none
checking for Fortran 77 name-mangling scheme... lower case, underscore, no extra underscore
checking whether sage_fortran appends underscores to external names... yes
checking whether sage_fortran appends extra underscores to external names... no
checking whether mixed C/Fortran code can be run... configure: WARNING: cannot run mixed C/Fortran code
configure: error: Maybe check LDFLAGS for paths to Fortran libraries?
Error configuring R.

real	0m11.582s
user	0m3.994s
sys	0m4.392s
```



---

Comment by kcrisman created at 2011-11-20 01:19:07

I'm not sure whether this is still valid.  Could be.


---

Comment by kcrisman created at 2011-11-20 01:19:07

Changing keywords from "" to "r-project".


---

Comment by mkoeppe created at 2020-03-24 22:13:18

This is outdated and should be closed.


---

Comment by mkoeppe created at 2020-03-24 22:13:18

Changing status from new to needs_review.


---

Comment by dimpase created at 2020-03-25 01:47:31

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-03-29 06:50:17

Resolution: invalid
