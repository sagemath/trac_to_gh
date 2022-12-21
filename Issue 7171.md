# Issue 7171: HP-UX failure of libm4ri 20090617 as it attempts to find L1 cache size

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-10 07:56:59

Assignee: tbd

Keywords: HP-UX L1 cache

The code appears to be trying to find information about the number of CPUS, the fails completely trying to find the L1 cache size

It would seem sensible to me the authors change the code so it does not break if it can't get the information it needs. 

However, in the case of HP-UX, I can give them access to the box, but even then you could get another Unix system where you don't know what CPUs it has, or the cache size. In which case assume something sensible  


```

checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking for a BSD-compatible install... ./install-sh -c
checking mm_malloc.h usability... no
checking mm_malloc.h presence... no
checking for mm_malloc.h... no
checking the number of available CPUs... unable to detect (assuming 1)
checking the number of available CPUs... unable to detect (assuming 1)
checking for x86 cpuid 0x0 output... unknown
checking for the processor vendor... Unknown
checking the L1 cache size... ./configure[12992]: unknown*1024: The specified number is not valid for this command.
Make: No arguments or description file.  Stop.
Error building libm4ri

real    0m18.199s
user    0m10.660s
sys     0m5.770s
sage: An error occurred while installing libm4ri-20090617
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/drkirkby/sage-4.1.2.rc0/install.log.  Describe your computer, operating system, etc.

```



---

Comment by malb created at 2009-11-18 16:51:46

I have uploaded a new SPKG to #7375


---

Comment by mhansen created at 2009-11-29 05:27:45

Resolution: fixed


---

Comment by mhansen created at 2009-11-29 05:27:45

Fixed by #7375
