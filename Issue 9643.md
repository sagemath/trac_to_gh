# Issue 9643: Force ECL to disable assembly code on Solaris 10 as it does on OpenSolaris

Issue created by migration from https://trac.sagemath.org/ticket/9643

Original creator: drkirkby

Original creation time: 2010-07-29 23:30:46

Assignee: drkirkby

CC:  jhpalmieri jsp mariah mpatel

#9474 disabled assembly code in ECL if the following three conditions were all met

 * OpenSolaris  (also known as Solaris 11 or SunOS 5.11)
 * x64 platform
 * 64-bit build

These conditions were checked, by testing the output of `uname -rsm`, which was: 


```
drkirkby@hawk:~$ uname -rsm
SunOS 5.11 i86pc
```


A note was added in `spkg-install` that it might be necessary to disable the assembly code on other variants of Solaris, but I was unsure at the time. 

John Palmieri has discovered ECL fails to build on Solaris 10 with the x64 processor in 64-bit mode. So the conditions for disabling the assembly code needs to be made less strict, as the release number (5.10 for Solaris 10, 5.11 for OpenSolaris), must be ignored. Instead the test will use `uname -sm`, dropping the `-r` option which checked the release. 


```
drkirkby@hawk:~$ uname -sm
SunOS i86pc
```


This should be a very easy fix. 


---

Comment by drkirkby created at 2010-07-29 23:37:35

A new .spkg file can be found at 

http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p2.spkg

This is currently untested, so I am not marking this for review just now. But I'm 95% sure this will resolve the issue. 

Dave


---

Comment by drkirkby created at 2010-07-29 23:38:34

Mercurial patch which should disable assembly code on Solaris 10 or OpenSolaris in 64-bit mode on x64 hardware


---

Attachment


---

Comment by drkirkby created at 2010-08-07 19:18:58

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-08-09 08:09:13

Just to make it clear, on any Solaris 10 or OpenSolaris machine, with an Intel/AMD processor, the output of `uname -m` is the same:

 * On my Sun Ultra 27 running OpenSolaris

```
drkirkby@hawk:~$ uname -m
i86pc
drkirkby@hawk:~$ uname -sm
SunOS i86pc
drkirkby@hawk:~$ uname -rsm
SunOS 5.11 i86pc
drkirkby@hawk:~$ 
```

 * On fulvia on skynet:

```
64 drkirkby@fulvia:[~] $ uname -m
i86pc
64 drkirkby@fulvia:[~] $ uname -sm
SunOS i86pc
64 drkirkby@fulvia:[~] $ uname -rsm
SunOS 5.10 i86pc
```


One can differentiate Solaris 10 and Solaris 11 machines by using the release version of the operating system (Solaris 10 shows 5.10, and OpenSolaris shows 5.11). 

Since I now wish to disable the assembly code on both Solaris 10 and Solaris 11, the option which shows the release (`-r`) needs removing. 

I'm choosing not to use the `-p` option to `uname`, as it's not portable. 

http://www.opengroup.org/onlinepubs/009695399/utilities/uname.html

The only portable options to uname are `-a, -m, -n, -r` and `-v`.


---

Comment by drkirkby created at 2010-08-09 08:10:57

Replying to [comment:4 drkirkby]:
 
> I'm choosing not to use the `-p` option to `uname`, as it's not portable. 
> 
> http://www.opengroup.org/onlinepubs/009695399/utilities/uname.html
> 
> The only portable options to uname are `-a, -m, -n, -r` and `-v`.

Oops, `-s`, which writes the name of the implementation of the operating system, is portable too.


---

Comment by fbissey created at 2010-08-09 09:52:03

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2010-08-09 09:52:03

Looks good to me.


---

Comment by drkirkby created at 2010-08-09 09:54:37

## Note to the release manager

There are no library patches. The patch is already integrated into this .spkg, so it only needs to be merged - nothing else. 

http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p2.spkg


---

Comment by mpatel created at 2010-08-15 08:03:49

Resolution: fixed
