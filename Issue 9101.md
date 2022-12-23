# Issue 9101: linbox reports "ERROR: BLAS not found!" on 64-bit SPARC build

Issue created by migration from https://trac.sagemath.org/ticket/9101

Original creator: drkirkby

Original creation time: 2010-05-31 03:12:01

Assignee: drkirkby

CC:  mvngu jsp jhpalmieri

Trying to compile Sage as 64-bit on SPARC, I get an error with linbox:


```
checking whether GMP is 4.0 or greater... yes
checking whether GMP was compiled with --enable-cxx... yes
checking for NTL >= 5.0... found
checking for GIVARO >= 3.2.10... found
checking whether to compile the sage interface... yes
checking for C interface to BLAS... not found
checking for others BLAS... not found

*******************************************************************************
 ERROR: BLAS not found!

 BLAS routines are required for this library to compile. Please
 make sure BLAS are installed and specify its location with the option
 --with-blas=<lib> when running configure.
*******************************************************************************
Error configuring linbox

real    0m32.070s
user    0m15.156s
sys     0m12.915s
sage: An error occurred while installing linbox-1.1.6.p3
```


No such error occurs when building linbox on OpenSolaris in 64-bit mode. 

This looks to me like it might be an error in spkg/standard/deps, as there is nothing there as far as I can see 


```
$(INST)/$(LINBOX): $(BASE) $(INST)/$(MPIR) $(INST)/$(NTL) $(INST)/$(GIVARO) $(INST)/$(GSL) $(INST)/$(ATLAS)
        $(SAGE_SPKG) $(LINBOX) 2>&1

```


to make linbox dependent on BLAS. The BLAS library is not failing to install - it does not try to install.


---

Comment by drkirkby created at 2010-06-12 12:46:12

I've since been told ATLAS is a blas library, so this should find ATLAS


---

Comment by cpernet created at 2010-06-28 12:57:58

Sure ATLAS is a BLAS, and LinBox should be able to find it. Was ATLAS correctly installed before LinBox? If so, could you post the spkg/build/linbox-1.1.6p3/src/config.log file in order to inverstigate for which reason did the configure test fail to compile.


---

Comment by drkirkby created at 2010-06-28 13:45:55

On closer inspection of the linbox log file, I can see what is wrong. ATLAS has built 32-bit libraries, not 64-bit ones. This is a problem with ATLAS rather than linbox. 

Thank you very much. I'm quite surprised I did not notice this. I think I've spent more time recently on my Xeon machine making sure the objects were all 64-bit, and overlooked the SPARC. 

Dave


---

Comment by drkirkby created at 2010-07-14 08:08:19

This is invalid, as the problem was ATLAS, not linbox.


---

Comment by drkirkby created at 2010-07-14 08:08:19

Resolution: invalid


---

Comment by drkirkby created at 2010-07-15 14:24:11

I'm reopening this, as it does indicate a problem in Sage. Although Linbox is not at fault, the issue still exists, and causes Linbox to fail to build. 

I've created #9508 to try to sort out the way the ATLAS libraries are built on Solaris, as they are handled completely differently to other platforms like Linux, OS X and FreeBSD. 

Dave


---

Comment by drkirkby created at 2010-07-15 14:24:11

Resolution changed from invalid to 


---

Comment by drkirkby created at 2010-07-15 14:24:11

Changing status from closed to new.


---

Comment by jhpalmieri created at 2010-07-15 22:45:40

Won't this be fixed by #9508?  If so, do we need both tickets open?


---

Comment by drkirkby created at 2010-07-15 23:05:59

Replying to [comment:9 jhpalmieri]:
> Won't this be fixed by #9508?  If so, do we need both tickets open?

I would agree this will be fixed by #9508, but I'm not sure if this should be closed until #9508 is closed. My belief is the bug reported is still valid at this point in time. 

Dave


---

Comment by mhansen created at 2010-09-01 00:05:35

I'm closing this since #9508 was closed.


---

Comment by mhansen created at 2010-09-01 00:05:35

Resolution: invalid
