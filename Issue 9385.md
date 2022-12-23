# Issue 9385: Building ATLAS goes into an infinite loop

Issue created by migration from https://trac.sagemath.org/ticket/9385

Original creator: olazo

Original creation time: 2010-06-29 22:26:24

Assignee: olazo

CC:  jsp vbraun alexghitza rlm was

I'm compiling Sage in a fedora 13 Intel Core Duo laptop (1.8 Gb RAM). It normally takes about 6 hours to build previous versions of sage, however, it now seems to enter an infinite loop while building ATLAS (After 28 hours it is still building ATLAS).

Someone in #archlinux said libreadline is segfaulting or something like that and that it was looping.

I'll compile a previous version of Sage and see if that works for now.


---

Comment by drkirkby created at 2010-06-30 10:10:05

In what version of Sage did you find this problem? 

What was your most recent build of Sage that built without this problem?


---

Comment by olazo created at 2010-06-30 13:22:24

It happened with sage-4.4.4, my latest succesful compilation was sage-4.4.1. I am under the impression that ATLAS was changed towards a more recent version (a beta) in this latest version of sage. 

http://groups.google.com/group/sage-devel/browse_thread/thread/f3fa4f8737437d7f/f4a78427d007d3d8?lnk=raot

That is the most obvious explanation to the problem, so, perhaps we should go back to the version of ATLAS used before...


---

Comment by drkirkby created at 2010-06-30 14:52:16

Replying to [comment:2 olazo]:
> It happened with sage-4.4.4, my latest succesful compilation was sage-4.4.1. I am under the impression that ATLAS was changed towards a more recent version (a beta) in this latest version of sage. 
> 
> http://groups.google.com/group/sage-devel/browse_thread/thread/f3fa4f8737437d7f/f4a78427d007d3d8?lnk=raot
> 
> That is the most obvious explanation to the problem, so, perhaps we should go back to the version of ATLAS used before...

There was a discussion of updating ATLAS, but it has not been changed to any beta version - I looked at doing it, but it is a non-trivial task. 

The changes to the ATLAS package are listed in the file SPKG.txt in the ATLAS package.

Try something like:


```
drkirkby@hawk:~/clean$ cd sage-4.5.alpha0/spkg/standard
drkirkby@hawk:~/clean/sage-4.5.alpha0/spkg/standard$ tar xfj atlas-3.8.3.p12.spkg
drkirkby@hawk:~/clean/sage-4.5.alpha0/spkg/standard$ cat atlas-3.8.3.p12/SPKG.txt
```


Looking further down you will see the ChangeLog section. 


```
## ChangeLog

### atlas-3.8.3.p12 (Jaap Spies, Februari 22th 2010)
 * #8039 For use with the Sun ld with SAGE64="yes" change ldflag -melf_86_64 to -64
 * See also the remarks from David Kirky on atlas-3.8.3.p5

=== atlas-3.8.3.p11 (Peter Jeremy, 2010-01-25)===
 * #7827: Fix atlas-3.8.3.p9 compilation on FreeBSD
 * Minh Van Nguyen: patch spkg-install-script to copy
   patches/SpewMakeInc.c over to src/CONFIG/src/SpewMakeInc.c

### atlas-3.8.3.p10 (David Kirkby, January 5th 2010)
 * replace bitwidth.py which uses 'ctypes' at that is broken 
   on many platforms. 
```


The most recent change, #8039 was in February this year and was merged in sage-4.3.4.alpha0. So the ATLAS .spkg has not been updated since your last successful build on 4.4.1. 

So I would look outside of there for the problem. As to what it might be, the obvious one is the load average on the system is too high, in which case ATLAS will be rebuilt a maximum of 5 times. If that's not the case, then I don't know what it might be. You mentioned readline elsewhere as a possible candidate. That has been updated. 

Dave


---

Comment by olazo created at 2010-07-01 20:50:19

Replying to [comment:3 drkirkby]:
> The most recent change, #8039 was in February this year and was merged in sage-4.3.4.alpha0. So the ATLAS .spkg has not been updated since your last successful build on 4.4.1. 
> 
> So I would look outside of there for the problem. As to what it might be, the obvious one is the load average on the system is too high, in which case ATLAS will be rebuilt a maximum of 5 times. If that's not the case, then I don't know what it might be. You mentioned readline elsewhere as a possible candidate. That has been updated. 
> 

I tried the compilation again, and found the following behaviour:
1.- Several packages are compiled during aproximately 1 hour and a half.
2.- ATLAS starts to compile
3.- About 2 hours later, ATLAS fails to compile with the following message:

Error report error_<ARCH>.tgz has been created in your top-level ATLAS
directory.  Be sure to include this file in any help request.
cat: ../../CONFIG/error.txt: No existe el fichero o el directorio
cat: ../../CONFIG/error.txt: No existe el fichero o el directorio


IN STAGE 1 INSTALL:  SYSTEM PROBE/AUX COMPILE


   Level 1 cache size calculated as 32KB
   dFPU: Combined muladd instruction with 5 cycle pipeline.
         Apparent number of registers : 6
         Register-register performance=810.76MFLOPS
   sFPU: Separate multiply and add instructions with 3 cycle pipeline.
         Apparent number of registers : 7
         Register-register performance=811.10MFLOPS


IN STAGE 2 INSTALL:  TYPE-DEPENDENT TUNING


STAGE 2-1: TUNING PREC='d' (precision 1 of 4)


   STAGE 2-1-1 : BUILDING BLOCK MATMUL TUNE
make -f Makefile INSTALL_LOG/dMMRES pre=d 2>&1 | ./xatlas_tee INSTALL_LOG/dMMSEARCH.LOG
      dL1MATMUL: lat=1, nb=60, pf=512, mu=6, nu=1, ku=60, if=6, nf=1;
                 Performance: 704.53 (37.74 percent of of detected clock rate)
make -f Makefile INSTALL_LOG/dNCNB pre=d 2>&1 | ./xatlas_tee INSTALL_LOG/dMMSEARCH.LOGmake -f Makefile INSTALL_LOG/dbestNN_56x56x56 pre=d nb=56 2>&1 | ./xatlas_tee INSTALL_LOG/dMMSEARCH.LOG      NCgemmNN : muladd=0, lat=1, pf=512, nb=56, mu=6, nu=1 ku=56,
                 ForceFetch=1, ifetch=6 nfetch=1
                 Performance = 647.68 (91.93 of copy matmul, 34.69 of clock)
make -f Makefile INSTALL_LOG/dbestNT_56x56x56 pre=d nb=56 2>&1 | ./xatlas_tee INSTALL_LOG/dMMSEARCH.LOG      NCgemmNT : muladd=0, lat=4, pf=512, nb=56, mu=6, nu=1 ku=56,
                 ForceFetch=1, ifetch=6 nfetch=1
                 Performance = 617.01 (87.58 of copy matmul, 33.05 of clock)
make -f Makefile INSTALL_LOG/dbestTN_56x56x56 pre=d nb=56 2>&1 | ./xatlas_tee INSTALL_LOG/dMMSEARCH.LOG      NCgemmTN : muladd=0, lat=3, pf=512, nb=56, mu=6, nu=1 ku=56,
                 ForceFetch=1, ifetch=6 nfetch=1
                 Performance = 655.13 (92.99 of copy matmul, 35.09 of clock)
make -f Makefile INSTALL_LOG/dbestTT_56x56x56 pre=d nb=56 2>&1 | ./xatlas_tee INSTALL_LOG/dMMSEARCH.LOG      NCgemmTT : muladd=0, lat=8, pf=512, nb=56, mu=6, nu=1 ku=56,
                 ForceFetch=1, ifetch=6 nfetch=1
                 Performance = 624.61 (88.66 of copy matmul, 33.46 of clock)
make -f Makefile MMinstall pre=d 2>&1 | ./xatlas_tee INSTALL_LOG/dMMSEARCH.LOG


   STAGE 2-1-2: CacheEdge DETECTION
make -f Makefile INSTALL_LOG/atlas_cacheedge.h pre=d 2>&1 | ./xatlas_tee INSTALL_LOG/dMMCACHEEDGE.LOG
make[3]: *** [build] Error 255
make[3]: se sale del directorio `/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build'
make[2]: *** [build] Error 2
make[2]: se sale del directorio `/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build'
Failed to build ATLAS.

4.- The terminal prompt does not appear (the process seems to have paused, but not ended). CPU usage descends from nearly full usage to almost none.

5 .- After approximately 20 minutes, return to No 2

I asked a friend who has also installed Fedora 13 in his 32 bit computer, to compile sage as well, and got the same behaviour.

There is currently no Fedora 13 compilation of sage (the fedora 12 version hasn't worked on my computer), so I must guess this must be a fedora 13 - related problem.

I hope this could get fixed soon, if it doesn't I'll have to change my OS.


---

Comment by gostrc created at 2010-07-02 13:22:32

Don't forget, there have been others affected on archlinux, so it isn't just fedora that's affected.


---

Comment by drkirkby created at 2010-07-02 13:32:25

Replying to [comment:5 gostrc]:
> Don't forget, there have been others affected on archlinux, so it isn't just fedora that's affected.

I don't have a clue what the problem might be, but I do know that the version of ATLAS in Sage has remained unchanged. Of course, each release of Sage many things do get changed, and its hard to know why something built ok but now does not. You could try building the version which you knew worked before, to confirm it is not something changed on your computer. 

I would ask for more help on sage-support and hope someone else can help you. 

Dave


---

Comment by olazo created at 2010-07-02 20:28:55

I thought I might compile a previous version, but unfortunately the previous version could not build in fedora 13 (libcrypt could not build). This bug has been fixed in sage-4.4.4, but now we have this new problem. Both sage-4.4.3 and 4.4.4 have been successfully built in fedora 12, so, unless this gets fixed soon i'll have to go back to 12.

Do you know of any sage version that has been build in fedora 13?


---

Comment by olazo created at 2010-07-02 20:35:23

Moreover, has anybody been able to compile in fedora 13/archlinux?


---

Comment by drkirkby created at 2010-07-02 21:01:47

I'm adding Jaap Spies to this ticket, as I believe he has built Sage on Fedora 13. He might know what is involved in getting Sage to build. 

As a general point, if you want to have a stable system with least hassle, it is often best to let others try the newest version of new software first. (Of course, if we all took that attitude, nobody would discover bugs with new systems, as nobody would install them. But genreally speaking, upgrading an operating system is not something I take lightly. 

Dave


---

Comment by vbraun created at 2010-07-03 14:06:37

Fedora 13 x86_64 here on an arrandale (i5) laptop, and ATLAS does not error out in build STAGE 2-1-2. Could someone with the bug post his
`sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/bin/INSTALL_LOG/dMMCACHEEDGE.LOG` after an unsuccessful build? Maybe that would give us the actual error message.


---

Attachment

this is mine


---

Comment by olazo created at 2010-07-03 15:11:32

I run in 32 bits though.


---

Comment by olazo created at 2010-07-03 15:26:00

That file has no errors on it, but searching in other logs in the same folder I found that zMMSEARCH.LOG and zMVTUNE.LOG, contain many errors. Mostly 'Bad register name' errors and overwritten register errors (in spanish "error: registro PIC ‘bx’ sobreescrito en ‘asm’").
I'll upload those too.


---

Attachment


---

Attachment

Those errors are harmless, that just means that ATLAS tried to compile some assembler optimized code that doesn't work on your particular CPU. Atlas will then use a different code path. 

However, if atlas would really die in stage 2-1-2 then it would never build zMMSEARCH.LOG, zMVTUNE.LOG. So the real bug must be something else further up in your log. Can you try to rebuild atlas (preferably with LANG=en_US or something like that) and upload the complete log?


---

Comment by olazo created at 2010-07-03 16:51:10

Replying to [comment:13 vbraun]:
> Those errors are harmless, that just means that ATLAS tried to compile some assembler optimized code that doesn't work on your particular CPU. Atlas will then use a different code path. 
> 
> However, if atlas would really die in stage 2-1-2 then it would never build zMMSEARCH.LOG, zMVTUNE.LOG. So the real bug must be something else further up in your log. Can you try to rebuild atlas (preferably with LANG=en_US or something like that) and upload the complete log? 

Which log do you mean? Is it sage-4.4.4/install.log ? That log will go into an infinite loop. So it is not clear at which point it should be halted. I ran the process only until the first looping. At that point install.log is over 20 Megabytes. Or is it some other "complete log"?

How do I turn on LANG=en_US?


---

Comment by vbraun created at 2010-07-03 17:02:47

Yes, I mean the complete install.log. Just wait until it loops once. Upload it somewhere with enough disk space ;-)

The fastest way is to start a new shell with a different locale like this:

```
[vbraun@volker-desktop ~]$ date
2010年  7月  3日 土曜日 18:00:03 IST
[vbraun@volker-desktop ~]$ LANG=en_US bash
[vbraun@volker-desktop ~]$ date
Sat Jul  3 18:00:14 IST 2010
```



---

Comment by drkirkby created at 2010-07-03 17:28:17

I suggests here compress the log first. 

Dave


---

Comment by olazo created at 2010-07-03 17:39:17

Ok, I have already started the compilation again. I should upload the log by tomorrow morning.


---

Comment by jhpalmieri created at 2010-07-03 18:25:19

Rather than attaching the log here, especially if it's large, it would be much better to post it somewhere else on a web page and just put the link here.


---

Comment by drkirkby created at 2010-07-03 22:43:48

Replying to [comment:5 gostrc]:
> Don't forget, there have been others affected on archlinux, so it isn't just fedora that's affected.

Note this comment by Alex Ghitza on sage-devel. 

http://groups.google.co.uk/group/sage-devel/browse_thread/thread/fba88176344c2814

Alex is able to both build Sage 4.4.4 from scratch, and perform an upgrade on Arch Linux. So if some people are having problems with ATLAS on Arch Linux, it is certainly not all users of that distribution. 



Dave


---

Comment by jsp created at 2010-07-04 13:15:40

ATLAS builds here ok on Fedora 13, 32 bit.

Jaap


---

Comment by drkirkby created at 2010-07-04 14:05:24

Resolution: worksforme


---

Comment by drkirkby created at 2010-07-04 14:05:24

Replying to [comment:20 jsp]:
> ATLAS builds here ok on Fedora 13, 32 bit.
> 
> Jaap
> 

Thank you Jaap. 

I've set this to 'worksforme', though a more accurate description would be 'works for some'. I don't believe this can remain a blocker for the next release, when there are positive confirmations it can build on both Fedora 13 and Arch Linux - the two platforms olazo mentioned were causing problems. 

I'm not dismissing the fact there may be a problem, and this may break on some installations, but it can't remain a blocker. 

I've cc'ed the 4.5 release manager (Robert Miller), in case he feels otherwise. 

Dave


---

Comment by drkirkby created at 2010-07-04 14:10:05

I did not mean to close the ticket - in fact, I'm not 100% sure what one should do here. 

Oscar can still attach his log, and I'm sure others will still try to resolve it. But it is clear that ATLAS has not been updated during the periods where Oscar had a successful build and a failed build. It's also clear people can build 4.4.4 on both Fedora 13 and Arch Linux (unknown version I'm afraid). As such, this can't remain a blocker.


---

Comment by olazo created at 2010-07-04 14:44:29

Replying to [comment:21 drkirkby]:
> Replying to [comment:20 jsp]:
> > ATLAS builds here ok on Fedora 13, 32 bit.
> > 
> > Jaap
> > 
> 
> Thank you Jaap. 
> 
> I've set this to 'worksforme', though a more accurate description would be 'works for some'. I don't believe this can remain a blocker for the next release, when there are positive confirmations it can build on both Fedora 13 and Arch Linux - the two platforms olazo mentioned were causing problems. 
> 
> I'm not dismissing the fact there may be a problem, and this may break on some installations, but it can't remain a blocker. 
> 
> I've cc'ed the 4.5 release manager (Robert Miller), in case he feels otherwise. 
> 

Sadly, I agree. I'll put the log here, it's not that big once compressed (1.3 Megabytes).


---

Attachment


---

Comment by olazo created at 2010-07-04 14:48:29

Replying to [comment:20 jsp]:
> ATLAS builds here ok on Fedora 13, 32 bit.
> 
> Jaap
> 

Could you please post your binary to sagemath.org, so it's available from the mirrors?


---

Comment by drkirkby created at 2010-07-04 15:14:27

I'll take a look. BTW, was there any particular reason for creating a tar file with only one file in it? You could have simply compressed install.log. 

Dave


---

Comment by drkirkby created at 2010-07-04 15:22:13

This *might* be a clue:


```
It appears you have cpu throttling enabled, which makes timings
unreliable and an ATLAS install nonsensical.  Aborting.
See ATLAS/INSTALL.txt for further information
Ignoring CPU throttling by user override!
```


CPU throttling is whereby the CPU speed reduces when the system load is low. It could confuse ATLAS when it goes into its timing routines. 

I have a program called 'powertop' which shows the states of the CPUs. Since my machine is busy, it is currently running at 3499 MHz, but it can go down as low as 1600 MHz and can climb a bit more, depending on the temperature, how many cores are active etc. 

It may be worth trying to disable CPU throttling on your system. Google should indicate how you might be able to do that. 


```
                                                                                 OpenSolaris PowerTOP version 1.2

C-states (idle power)	Avg	Residency                                                                P-states (frequencies)
C0 (cpu	running)		(18.6%)                                                                  1600 Mhz	 0.0%
C1			2.2ms   (10.5%)                                                                  1733 Mhz	 0.0%
C2			1.8ms	(10.4%)                                                                  1867 Mhz	 0.0%
C3			2.1ms   (60.5%)                                                                  2000 Mhz	 0.0%
                                                                                                         2133 Mhz	 0.0%
                                                                                                         2267 Mhz	 0.0%
                                                                                                         2400 Mhz	 0.0%
                                                                                                         2533 Mhz	 0.0%
                                                                                                         2667 Mhz	 0.0%
                                                                                                         2800 Mhz	 0.0%
                                                                                                         2933 Mhz	 0.0%
                                                                                                         3067 Mhz	 0.0%
                                                                                                         3200 Mhz	 0.0%
                                                                                                         3333 Mhz	 0.0%
                                                                                                         3499 Mhz(turbo) 100.0%
```



---

Comment by vbraun created at 2010-07-04 15:29:55

I think the real bug is

```
gcc -DL2SIZE=4194304 -I/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/include -I/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/../src//include -I/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/../src//include/contrib -DAdd_ -DF77_INTEGER=int -DStringSunStyle -DATL_OS_Linux -DATL_ARCH_CoreDuo -DATL_CPUMHZ=800 -DATL_SSE3 -DATL_SSE2 -DATL_SSE1 -DATL_GAS_x8632  -fomit-frame-pointer -O3 -mfpmath=387 -fPIC -m32 -o xcsfindCE csfindCE.o \
                   /home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/src/blas/gemm/ATL_csFindCE_mm.o /home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/lib/libatlas.a -lm
/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/bin/ATLrun.sh /home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/tune/blas/gemm xcsfindCE -f res/atlas_csNKB.h
assertion t1 > 0.0 failed, line 257 of file /home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/../src//tune/blas/gemm/findCE.c
TA TB      M      N      K    alpha       beta     CacheEdge      TIME   MFLOPS
## ==

 T  N   1200   1200   1200   1.0   0.0   1.0   0.0         0     7.953  1738.26
 T  N   1200   1200   1200   1.0   0.0   1.0   0.0        64    -2.000     0.00
 T  N   1200   1200   1200   1.0   0.0   1.0   0.0       128    -2.000     0.00
 T  N   1200   1200   1200   1.0   0.0   1.0   0.0       256     7.945  1740.01
 T  N   1200   1200   1200   1.0   0.0   1.0   0.0       512     8.315  1662.59
 T  N   1200   1200   1200   1.0   0.0   1.0   0.0      1024     8.002  1727.61
 T  N   1200   1200   1200   1.0   0.0   1.0   0.0      2048     8.334  1658.80
make[6]: *** [csRunFindCE] Error 255
make[6]: Leaving directory `/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/tune/blas/gemm'
make[5]: *** [res/atlas_csNKB.h] Error 2
make[5]: Leaving directory `/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/tune/blas/gemm'
make[4]: *** [/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/tune/blas/gemm/res/atlas_csNKB.h] Error 2
make[4]: Leaving directory `/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/bin'
ERROR 664 DURING CACHE EDGE DETECTION!!.
```

This same assertion failure appears once on the atlas bugtracker at
http://sourceforge.net/tracker/index.php?func=detail&aid=878809&group_id=23725&atid=379483. The problem might be that there is not enough available RAM. Once the cache edge detection fails, the rest of the build is pretty much hopeless.


---

Comment by olazo created at 2010-07-04 15:54:34

Replying to [comment:27 vbraun]:
> This same assertion failure appears once on the atlas bugtracker at
> http://sourceforge.net/tracker/index.php?func=detail&aid=878809&group_id=23725&atid=379483. The problem might be that there is not enough available RAM. Once the cache edge detection fails, the rest of the build is pretty much hopeless.

Does this mean that I'm unable to build because of hardware limitations (not enough RAM)? But I built just fine in ubuntu.

Also, this ticket is clearly not resolved. I'll reverse that (I hope that's not against the rules).


---

Comment by olazo created at 2010-07-04 15:54:34

Resolution changed from worksforme to 


---

Comment by olazo created at 2010-07-04 15:54:34

Changing status from closed to new.


---

Comment by vbraun created at 2010-07-04 16:01:15

Changing priority from blocker to major.


---

Comment by vbraun created at 2010-07-04 16:01:15

Some questions for the OP:
  * Is your CPU trottled?
  * Were other applications open/running at build time?
  * Upload your `/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/error_CoreDuo32SSE3.tar`

I'll set the priority to the default since it seems to be working for most people.


---

Attachment

Replying to [comment:29 vbraun]:
> Some questions for the OP:
>   * Is your CPU trottled?

I guess it is, since the install.log says so (see a pervious message fro drkirkby in this ticket)

>   * Were other applications open/running at build time?

Yes, should I try again with no ther applications running?

>   * Upload your `/home/oscar/sage-4.4.4/spkg/build/atlas-3.8.3.p12/ATLAS-build/error_CoreDuo32SSE3.tar`

Done.

Also, thank you very much for helping me out!


---

Comment by drkirkby created at 2010-07-04 17:56:00

Replying to [comment:28 olazo]:
> Replying to [comment:27 vbraun]:
> > This same assertion failure appears once on the atlas bugtracker at
> > http://sourceforge.net/tracker/index.php?func=detail&aid=878809&group_id=23725&atid=379483. The problem might be that there is not enough available RAM. Once the cache edge detection fails, the rest of the build is pretty much hopeless.
> 
> Does this mean that I'm unable to build because of hardware limitations (not enough RAM)? But I built just fine in ubuntu.
> 
> Also, this ticket is clearly not resolved. I'll reverse that (I hope that's not against the rules).

Possibly with information like the amount of RAM and swap space, and what other applications were running, we might be able to make a judgment on that. I've regularly built Sage in 2 GB RAM on Solaris, but I'm just using the machine as a server, with no graphical interface running, so I could get away with less than someone with a Gnome or similar running. I've built older (4 month or so) versions of Sage with 1.5 GB on Solaris too. 

I know others have built Sage with < 2 GB on Linux. I'm not sure what the practical limit is though. I think if have 2 GB, then it should not be a problem and even 1 GB *may* be ok. Any less than 1 GB and you are certainly pushing your luck. 

You have not really provided much information about your system. Your initial report had little useful information to help someone debug the problem. You never stated the version of Sage you were using, or the version which built ok. (I realise you have since done this). 

In future, it would help if you provide more information. This is not just for Sage, but anytime you have build problems with any software. 


> Also, this ticket is clearly not resolved. I'll reverse that (I hope that's not against the rules).

It is actually against the rules. You should not reopen or close tickets without admin rights. However, in this case, I may have been wrong to close it. I was expecting that "wordsforme" would leave it open. Either way, from a practical point of view, I don't think it makes a lot of difference - we will still try to resolve the ticket. I suspect it should however be closed, but I'm not 100% sure. I will seek clarification on this issue. 

Things I would suggest include 
 * Stating the RAM and swap space you have. Google for how to find these out if you are not sure. 
 * Disable CPU throttling. 
 * If none of those work, download the latest ATLAS beta and try building that. If that fails, then report it to the ATLAS bug tracker. Since this is the latest stable ATLAS, report that to the ATLAS bug tracker too. 
 * Add the links to the ATLAS bug tracker to this ticket, so we have a reference of it. 

Maybe others have some more ideas how to solve this. 

Dave


---

Comment by olazo created at 2010-07-04 18:07:47

Replying to [comment:31 drkirkby]:
> Possibly with information like the amount of RAM and swap space, and what other applications were running, we might be able to make a judgment on that. I've regularly built Sage in 2 GB RAM on Solaris, but I'm just using the machine as a server, with no graphical interface running, so I could get away with less than someone with a Gnome or similar running. I've built older (4 month or so) versions of Sage with 1.5 GB on Solaris too. 
> 
> I know others have built Sage with < 2 GB on Linux. I'm not sure what the practical limit is though. I think if have 2 GB, then it should not be a problem and even 1 GB *may* be ok. Any less than 1 GB and you are certainly pushing your luck. 
> 
> You have not really provided much information about your system. Your initial report had little useful information to help someone debug the problem. You never stated the version of Sage you were using, or the version which built ok. (I realise you have since done this). 
> 
> In future, it would help if you provide more information. This is not just for Sage, but anytime you have build problems with any software. 

I've got an Intel Core Duo, and 1.8 Gb of RAM. My Swap is 5 Gb. I was probably running both Firefox and Thunderbird, watching stuff in YouTube... Thinking back that does seem quite CPU-expensive

> > Also, this ticket is clearly not resolved. I'll reverse that (I hope that's not against the rules).
> 
> It is actually against the rules. You should not reopen or close tickets without admin rights. However, in this case, I may have been wrong to close it. I was expecting that "wordsforme" would leave it open. Either way, from a practical point of view, I don't think it makes a lot of difference - we will still try to resolve the ticket. I suspect it should however be closed, but I'm not 100% sure. I will seek clarification on this issue. 
> 
> Things I would suggest include 
>  * Stating the RAM and swap space you have. Google for how to find these out if you are not sure. 
>  * Disable CPU throttling. 
>  * If none of those work, download the latest ATLAS beta and try building that. If that fails, then report it to the ATLAS bug tracker. Since this is the latest stable ATLAS, report that to the ATLAS bug tracker too. 
>  * Add the links to the ATLAS bug tracker to this ticket, so we have a reference of it. 

I will try all of that and report here

> Maybe others have some more ideas how to solve this. 
> 
> Dave 

Thank you too for your help!


---

Comment by olazo created at 2010-07-05 15:03:22

Replying to [comment:31 drkirkby]:
> I know others have built Sage with < 2 GB on Linux. I'm not sure what the practical limit is though. I think if have 2 GB, then it should not be a problem and even 1 GB *may* be ok. Any less than 1 GB and you are certainly pushing your luck. 

It has ocurred to me, that since I have a dual core processor (each core having 800 Mb of RAM) perhaps the compillation is not being done in parallel. I did notice that the CPU load during compilation was almost always near half. How can I make sure the compilation is done in parallel?


---

Comment by drkirkby created at 2010-07-05 15:51:13

Replying to [comment:33 olazo]:
> Replying to [comment:31 drkirkby]:
> > I know others have built Sage with < 2 GB on Linux. I'm not sure what the practical limit is though. I think if have 2 GB, then it should not be a problem and even 1 GB *may* be ok. Any less than 1 GB and you are certainly pushing your luck. 
> 
> It has ocurred to me, that since I have a dual core processor (each core having 800 Mb of RAM) perhaps the compillation is not being done in parallel. I did notice that the CPU load during compilation was almost always near half. How can I make sure the compilation is done in parallel?

Almost all modern machines (and 100% of all PCs) share the memory, so you do not have 800 MB/CPU. 

Typing


```
export SAGE_PARALLEL_SPKG_BUILD=yes
export MAKE="make -j 3"
```


will launch 3 threads and build upto 3 .spkg files in parallel. When .spkg files are independant of each other, they can be built in parallel. Other times, only one will be built. So my CPU load changed from about 12.5% (1/8th of the threads being used) to 100% in the instances where 8 can all be built in parallel.

However, building packages in parallel is not 100% reliable yet, so the last thing you want to do is try that. That will just add another thing that can go wrong. 

Dave


---

Comment by glebaron created at 2010-07-08 15:56:24

I'm seeing the same thing on Fedora 13 32 bit. Intel i3/4GB RAM

Turned off cpuspeed, disabled SpeedStep in the BIOS and finally booted into single user mode but the problem persisted unchanged.

The following error shows up a few lines before the "error 639 during edge detection":


```
ATL_dupKBmm_b0.c: In function ‘ATL_dpKBmm_b0’:
ATL_dupKBmm_b0.c:26: error: ‘else’ without a previous ‘if’
ATL_dupKBmm_b0.c:30: error: ‘else’ without a previous ‘if’
make[7]: *** [ATL_dupKBmm_b0.o] Error 1
make[7]: *** Waiting for unfinished jobs....
ATL_dupKBmm_b1.c: In function ‘ATL_dpKBmm_b1’:
ATL_dupKBmm_b1.c:27: error: ‘else’ without a previous ‘if’
ATL_dupKBmm_b1.c:31: error: ‘else’ without a previous ‘if’
make[7]: *** [ATL_dupKBmm_b1.o] Error 1

```

Compilation stops here.

The same code builds without problem on Fedora 12.


---

Comment by olazo created at 2010-07-13 00:09:40

I have just managed to compile sage in my fedora 13 32 bits computer. I am not completely sure what made the difference. I can see two differences between this and my previous atempts: 

1) I updated the compilers to their latest versions.
2) I was compiling in a partition formated as ext3, this time i used a partition formated as ext4.
3) I compiled as superuser

I did not disable throttling, and I was running gnome (other than that no other resource-consuming aplications were running).

Since I was the only person to have this bug, and it has now been resolved, I advice this ticket to be closed.


---

Comment by drkirkby created at 2010-07-13 00:35:32

Resolution: invalid


---

Comment by drkirkby created at 2010-07-13 00:35:32

Replying to [comment:36 olazo]:
> I have just managed to compile sage in my fedora 13 32 bits computer. I am not completely sure what made the difference. I can see two differences between this and my previous atempts: 
> 
> 1) I updated the compilers to their latest versions.
> 2) I was compiling in a partition formated as ext3, this time i used a partition formated as ext4.
> 3) I compiled as superuser

Compiling as root is a very dangerous thing to do. I've personally had builds of Sage fail when they try to write to system directories like /usr/lib. I'd rather them fail, than corrupt my system. Sage should not need root privileges to build. 

I'm glad you have solved this. Given most people had no problem, I will close this as invalid. 

Dave


---

Comment by vbraun created at 2010-07-13 00:39:48

Fedora 13 had already 4 gcc updates. Part of its purpose is trying the bleeding edge for the compiler. Installing the gcc updates is definitely recommended ;-)

```
yum.log:Apr 06 16:38:57 Installed: gcc-4.4.3-12.fc13.x86_64
yum.log:Apr 16 12:48:20 Updated: gcc-4.4.3-16.fc13.x86_64
yum.log:Apr 23 18:16:11 Updated: gcc-4.4.3-18.fc13.x86_64
yum.log:May 04 23:53:12 Updated: gcc-4.4.4-2.fc13.x86_64
yum.log:Jul 06 11:03:57 Updated: gcc-4.4.4-10.fc13.x86_64
```

If anyone still has problems please reopen with specific information about your compiler...


---

Comment by tux21b created at 2010-10-01 20:59:25

I've just spent several hours trying to compile sage (compiling on an Atom processor takes some time...) while I stumbled upon the same problem.

Distribution: Fedora 13 (i686)

System: EeePC 1000H / Intel Atom N270

Compiler: gcc-4.4.4-10.fc13

RAM: 1GB (completely used during the compilation of ATLAS)

Swap: 2GB (nearly unused)

What I've tried after reading all comments here:

 * adding more swap
 * no X, single user
 * disabling cpu throttling
 * closing all other services and programs

Unfortunately without any success. But then I've read about the `SAGE_ATLAS_LIB` environment variable in the [docs](http://www.sagemath.org/doc/installation/source.html#environment-variables). So here is a simple workaround for F13:

*Workaround:*

```
sudo yum install atlas atlas-devel
sudo mkdir /opt/atlas/
sudo ln -s /usr/lib/atlas /opt/atlas/lib
sudo mkdir /opt/atlas/include
sudo ln -s /usr/include/atlas /opt/atlas/include/atlas
export SAGE_ATLAS_LIB=/opt/atlas
make
```


Regards,

Christoph


---

Comment by drkirkby created at 2010-10-01 21:17:17

Replying to [comment:40 tux21b]:
> I've just spent several hours trying to compile sage (compiling on an Atom processor takes some time...) 

<snip>

> *Workaround:*

Thank you. I must admit, I'm a bit concerned at this bug. I've seen it myself on Debian in virtual machines too. Just installing another version of ATLAS is obviously fine for you, but in general it is not good. 

If you still have the log, can I suggest you open another ticket, attach the file spkg/logs/atlas$verison.log and leave it open as a bug, as there does appear to be a problem here. 

Dave


---

Comment by tux21b created at 2010-10-01 22:17:39

Replying to [comment:41 drkirkby]:
> Just installing another version of ATLAS is obviously fine for you, but in general it is not good.
Sure, that's why it's called a »workaround« and not »solution«. Anyway, I am happy with it and it might help many others too.

> If you still have the log, can I suggest you open another ticket, attach the file spkg/logs/atlas$verison.log and leave it open as a bug, as there does appear to be a problem here.
Here it is: http://trac.sagemath.org/sage_trac/ticket/10051

Feel free to ask for more information/test runs/whatever.

Christoph


---

Comment by drkirkby created at 2010-10-18 11:42:11

Resolution changed from invalid to 


---

Comment by drkirkby created at 2010-10-18 11:42:11

I'm reopening this, as it's not clear to me this issue has ever been resolved.


---

Comment by drkirkby created at 2010-10-18 11:42:11

Changing status from closed to new.


---

Comment by vbraun created at 2010-10-23 14:29:23

I think it is unavoidable that that ATLAS sometimes fails to get accurate timings. Nor is it always desirable to tune it to precisely your CPU, for example if you are building a binary distribution. Therefore, I propose we add a new variable `SAGE_ATLAS_ARCH` with values
  1. `auto` - run through the tuning process
  2. `fast` - reasonably modern ~2005 cpu: sse3 on x86, Niagara SPARC, ...
  3. `base` - really old cpus
  4. A particular architecture from `ATLAS/CONFIG/ARCHS/*.tgz`, e.g. `AMD64K10h32SSE3`
The ATLAS spkg then should then build a configuration according to `SAGE_ATLAS_ARCH`. If it it is not set, try 2x`auto`, if that fails `fast`, and if that fails `base`.

The Fedora rpm package has pre-built configurations for various cpus and shows how to patch them into the ATLAS build system.


---

Comment by drkirkby created at 2010-10-28 04:36:09

I've just experienced this problem on a VirtualBox virtual machine running openSUSE 11.3. ATLAS fails to build. The hardware is a Sun Ultra 27, quad core 3.33 GHz Intel Xeon. The host operating system is OpenSolaris 06/2009. 

Dave


---

Comment by tux21b created at 2010-11-22 23:06:41

My (related?) problem seems to have been solved in Sage 4.6. I've already updated my ticket: http://trac.sagemath.org/sage_trac/ticket/10051#comment:3

Maybe someone here can confirm this?


---

Comment by chris created at 2011-08-28 22:45:15

I'm trying to build sage on Fedora 16 but I'm also ending in an infinite ATLAS build loop.
Sage 4.7 builds fine in Fedora 15 on my AMD desktop but on my Intel notebook sage 4.7 and sage 4.7.1
are hanging at the ATLAS build.

Just looking at the install.log for example ATLAS was trying over 600 times to compile fc.c

```
[chris@thinkpad sage-4.7.1]$ cat install.log | grep -c "sage-4.7.1/spkg/build/atlas-3.8.3.p16/ATLAS-build/../src//tune/blas/gemm/fc.c"
648
```

Attatched:

```
install.log.lzma
cat /proc/meminfo >proc_meminfo
cat /proc/cpuinfo >proc_cpuinfo
```

Here you can see that there are some crashes in "ATLAS-build/tune/blas/":

```
cat /var/log/messages |grep abrt |grep "Aug 26 18" >abrt.log
```

I've also tried disabling cpu throttling with no effect.

```
sudo cpupower frequency-set -g performance
```

And the workaround from comment 40:

```
$ sudo yum install atlas atlas-devel
$ rpm -q atlas
atlas-3.8.4-1.fc16.x86_64
$ sudo mkdir /opt/atlas/
$ #sudo ln -s /usr/lib/atlas /opt/atlas/lib
$ sudo ln -s /usr/lib64/atlas /opt/atlas/lib
$ sudo mkdir /opt/atlas/include
$ sudo ln -s /usr/include/atlas /opt/atlas/include/atlas
$ export SAGE_ATLAS_LIB=/opt/atlas
$ export MAKE="make -j6"
$ make
```


But make will fail (see install_with_system_atlas.tar.lzma) because /opt/atlas/lib
only contains shared objects and no static library files.

"Unable to find one of liblapack.a, libcblas.a, libatlas.a or libf77blas.a
in the directory /opt/atlas/lib"

```
$ ls /opt/atlas/lib
libatlas.so      libcblas.so      libclapack.so      libf77blas.so      liblapack.so      libptcblas.so      libptf77blas.so
libatlas.so.3    libcblas.so.3    libclapack.so.3    libf77blas.so.3    liblapack.so.3    libptcblas.so.3    libptf77blas.so.3
libatlas.so.3.0  libcblas.so.3.0  libclapack.so.3.0  libf77blas.so.3.0  liblapack.so.3.0  libptcblas.so.3.0  libptf77blas.so.3.0
```


What should I do next? If you need more information to fix this bug please ask.

chris


---

Attachment


---

Attachment


---

Attachment


---

Attachment

Can you try the new atlas spkg, which is included in Sage-4.7.2.alpha1 or higher? This will at the very least let you use the system-wide atlas install.


---

Comment by chris created at 2011-08-29 10:16:11

OK. Thanks I've updated ATLAS and now the system-wide atlas install works but the ATLAS build will still go into a loop.

```
$ wget http://boxen.math.washington.edu/home/release/sage-4.7.2.alpha2/sage-4.7.2.alpha2/spkg/standard/atlas-3.8.4.spkg
$ cp atlas-3.8.4.spkg ~/excluded/sage-4.7.1/spkg/standard/
```


chris


---

Comment by jdemeyer created at 2013-05-24 12:25:25

It's not clear whether there really is a problem, I don't know any recent reports of this. Many people have _claimed_ that ATLAS goes into an infinite loop, but in reality they are just too impatient to wait for ATLAS to finish compiling.


---

Comment by jdemeyer created at 2013-05-24 12:25:25

Resolution: worksforme
