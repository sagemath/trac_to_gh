# Issue 8520: Optional package gap_packages-4.4.12_2  fails to install on Solaris 10 SPARC

Issue created by migration from https://trac.sagemath.org/ticket/8520

Original creator: drkirkby

Original creation time: 2010-03-13 14:19:37

Assignee: tbd

CC:  dimpase

## Hardware & associated software

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
 * 4.3.4.alpha1
 * Patch #8509 removing the -o option to grep to allow packages to install. 

 == The problem with the optional gap_packages-4.4.12_2 ==


```
gap_packages-4.4.12_2/SPKG.txt
gap_packages-4.4.12_2/.hgignore
Finished extraction
****************************************************
Host system
uname -a:
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran
Thread model: posix
gcc version 4.4.3 (GCC)
****************************************************
./spkg-install: bad substitution

real    0m0.010s
user    0m0.003s
sys     0m0.007s
sage: An error occurred while installing gap_packages-4.4.12_2
```




---

Comment by dimpase created at 2010-03-15 08:32:56

The following line in spkg-install is the problem

```
${gapver:=$SAGE_ROOT/spkg/standard/newest_version gap}
```

Not quite nclear how to fix, at the moment...


---

Comment by dimpase created at 2010-03-15 08:32:56

Changing status from new to needs_work.


---

Comment by drkirkby created at 2010-03-15 11:12:58

I just asked on comp.unix.shell There might be some follow up there. 


http://groups.google.com/group/comp.unix.shell/browse_thread/thread/2d7921cb2a113592#


---

Comment by dimpase created at 2010-03-15 12:10:41

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2010-03-15 12:10:41

Replying to [comment:2 drkirkby]:

please test 

http://sage.math.washington.edu/home/dima/packages/gap_packages-4.4.12_3.spkg

It works on t2 now, after a trivial change in spkg-install


---

Comment by drkirkby created at 2010-03-15 15:08:45

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-03-15 15:08:45

I get gobbledygook. 

BTW, if there is no Mercurial repository (I've not checked, but know some optional packages don't have one), it would seem sensible to create one. But for now at least, I can't do anything with this. 


```
gap_packages-4.4.12_2/.hg/patches/status
gap_packages-4.4.12_2/.hg/patches/gap_packages.patch
gap_packages-4.4.12_2/.hg/patches/~/
gap_packages-4.4.12_2/.hg/patches/~/gap_packages.patch
gap_packages-4.4.12_2/.hg/patches/series
gap_packages-4.4.12_2/.hg/undo.branch
gap_packages-4.4.12_2/spkg-install
gap_packages-4.4.12_2/patches/
gap_packages-4.4.12_2/patches/guava/
gap_packages-4.4.12_2/patches/guava/Makefile.in
tar: This does not look like a tar archive
tar: Skipping to next header
tar: Archive contains obsolescent base-64 headers
tar: Archive contains `�;��\221g=\b�ku�' where numeric off_t value expected
tar: Archive contains `��RsC\000\020v' where numeric mode_t value expected
tar: Archive contains `\030�\214S;�\223�N��\203' where numeric time_t value expected
tar: Archive contains `�B�\034���G' where numeric major_t value expected
tar: Archive contains `�\235z\037oN&I' where numeric minor_t value expected
tar: Archive contains `"`��3V\231v' where numeric uid_t value expected
tar: Archive contains `�\233\025���1�' where numeric gid_t value expected
~�IE\210ӥ�\202\020\021\0223�\220\225��\fz5�\031\206�\t\032r�\002\177\027z���k��):lJ����\227��c\033W�4M�\rD�\224\023�\fU��\227\214�w\230�h\017��\020�o��\226��I`.\004�G\211\033\224e�]]\023]
tar: ~�IE\210ӥ�\202\020\021\0223�\220\225��\fz5�\031\206�\t\032r�\002\177\027z���k��)\:lJ����\227��c\033W�4M�\rD�\224\023�\fU��\227\214�w\230�h\017��\020�o��\226��I`.\004�G\211\033\224e�]]\023]: Unknown file type 'X', extracted as normal file
tar: ~�IE�ӥς���3Ő���
D����               z5����   �r����z���k��):lJ���֗��c
     U�闌�w��h����o嫖��I`.��G���e�]]�]: implausibly old time stamp 1970-01-01 00:59:59
tar: Skipping to next header
tar: Read 7566 bytes from /export/home/drkirkby/sage-4.3.4.alpha1/spkg/optional/gap_packages-4.4.12_3.spkg
tar: Error exit delayed from previous errors
Finished extraction
sage: After decompressing the directory gap_packages-4.4.12_3 does not exist
This means that the corresponding .spkg needs to be downloaded
again.
http://www.sagemath.org//packages/optional/gap_packages-4.4.12_3.spkg --> gap_packages-4.4.12_3.spkg
[ ]
http://www.sagemath.org//packages/standard/gap_packages-4.4.12_3.spkg --> gap_packages-4.4.12_3.spkg
[ ]
http://www.sagemath.org//packages/experimental/gap_packages-4.4.12_3.spkg --> gap_packages-4.4.12_3.spkg
[ ]
http://www.sagemath.org//packages/archive/gap_packages-4.4.12_3.spkg --> gap_packages-4.4.12_3.spkg
[ ]
**********************************************************************
* Unable to download gap_packages-4.4.12_3
* Please see http://www.sagemath.org//packages for a list of valid
* packages or check the package name.
**********************************************************************
/export/home/drkirkby/sage-4.3.4.alpha1/spkg/build
bunzip2: Can't open input file gap_packages-4.4.12_3.spkg: No such file or directory.
tar: gap_packages-4.4.12_3.spkg: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
Second download resulted in a corrupted package.
```



---

Comment by dimpase created at 2010-03-15 16:22:45

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2010-03-15 16:22:45

Replying to [comment:4 drkirkby]:

oops, careless renaming of files... It's not just a tar file ;-)

I created gap_packages-4.4.12_2.spkg using sage -spkg (takes looong time on t2 :))
and then renamed the file gap_packages-4.4.12_3.spkg

And this does not fly, as sage does some checking on the spkg filename...
If you still have that downloaded file, rename it please to gap_packages-4.4.12_2.spkg and try 
spkg -f again.
Otherwise, please download and sage -f
 http://sage.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
(this is the updated version)



> I get gobbledygook. 
> 
> BTW, if there is no Mercurial repository (I've not checked, but know some optional packages don't have one), it would seem


---

Comment by drkirkby created at 2010-03-15 16:45:58

Did you mean to name this 'gap_packages-4.4.12_2.spkg' ? The original ended in _2, then you changed it to _3 (the one with the gobbledygook), then back to _2. I assume it should really have a .p0 appended. 

I'm just downloading now, but need to do something else, so I'll come back when it is downloaded. 

Dave


---

Comment by drkirkby created at 2010-03-15 16:59:31

It installs (whether or not it works I don't know), but there is no entry in SPKG.txt and the version number is the same as before, so effectively any record of the changes is going to be lost. 

I would have thought it needed to be called gap_packages-4.4.12_2.p0 and an entry added to SPKG.txt to indicate what changes have been made. 

Is this likely to fix the other gap issue? If so, I'll try that later, but I have other things to do today, so can't spend long over it. By the weekend, I should have more time. 


Dave


---

Comment by drkirkby created at 2010-03-15 16:59:31

Changing assignee from tbd to drkirkby.


---

Comment by dimpase created at 2010-03-16 12:42:58

Replying to [comment:7 drkirkby]:
> It installs (whether or not it works I don't know), but there is no entry in SPKG.txt and the version number is the same as before, so effectively any record of the changes is going to be lost. 
> 
> I would have thought it needed to be called gap_packages-4.4.12_2.p0 and an entry added to SPKG.txt to indicate what changes have been made. 

OK, so here is the version with with consistent numbering. That _2, etc, was originally due to David Joyner, and not consistent with anything. So I removed that _2 from the name, and added p0.

http://sage.math.washington.edu/home/dima/packages/gap_packages-4.4.12.p0.spkg

Regarding SPKG.txt, I followed the predecessors, who didn't bother with it. :-)

Well, it's an optional package, and I will to update it soon with more GAP
packages (and make SPKG.txt good and proper...).


---

Comment by drkirkby created at 2010-03-17 01:23:01

I'm not in a position to test this now. The server is off and I don't fancy going out in the cold to power it on - I'll do that in the morning (UK time). 

But I think it would be worth adding SPKG.txt and a repository now. I had someone email me recently saying he did not feel the need to write a better script, as there were worst ones in Sage. I think we need to be careful to try to improve the documentation & quality. There are plenty of AddOns for Mathematica, but they are all documented. 

I don't understand much about GAP (I'm not a mathematician), but I get the feeling from the web site there are tons of packages. I wonder the logic of including a subset of them, when people would probably be better to get what they need. It will be almost impossible to keep all the packages upto date. Some, like FactInt might have quite wide appeal, but others I get the feeling are not so usefully included. Anyway, I guess that is another issue. 

Dave


---

Comment by dimpase created at 2010-03-17 12:43:04

Replying to [comment:9 drkirkby]:

[...]
> I think it would be worth adding SPKG.txt and a repository now. 

done (as of 17.03.2010) 12:30 UK time

> 
> I don't understand much about GAP (I'm not a mathematician), but I get the feeling from the web site there are tons of packages. 

most of them a very specialised, and people would be better off usign them in 
GAP directly. Some of them, moreover, as just interfaces to other CA systems, 
or contain such interfaces, and thus are largely useless within Sage.

At least one GAP package, ace, is packaged as a separate spkg
(and needs to be installed after gap_packages)
 
ace was broken since 4.3.3, and noone complained, so that's about how wide
the user base of a typical GAP package is in Sage.
(I fixed ace, by the way, there is a recent ticket opened by my, with a ready fix)
 

> I wonder the logic of including a subset of them, when people would probably be > better to get what they need. It will be almost impossible to keep all the > packages upto date. Some, like FactInt might have quite wide appeal, but others I get the feeling are not so usefully included. Anyway, I guess that is another issue. 
> 

I basically only have enough time to maintain and improve what I need in Sage for my research and teaching. I am on a tenure-track...


---

Comment by drkirkby created at 2010-03-17 19:03:33

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-03-17 19:03:33

That is fine. 

 * The bug is fixed, so the packages install on Solaris.
 * There is now a SPKG.txt
 * There is now a Mercurial repository.

Positve review. I'm not sure how to get the old package removed and this one put in its place. I better ask on sage-devel.

You confirmed what I thought about the speciality of the packages. 

I did notice ace failed to install, though I realise the method I used to install them was working through them alphabetically, so ace would have been tried before gap_packages. I don't think there is any automatic way for a package to install its dependencies. 

I'll look for your ace package and will review that. 

Thank you for fixing this. Not that I personally will be using it, but its nice to know it installs correctly now. 

Realistically these optional packages should be checked before a release is made, so things like the breakage of ace since 4.3.3 do not happen. I can not believe Wolfram Research would release a new release of Mathematica without verifying the 'AddOns' install properly. If sage is going to be a viable alternative to Mathematica, for me at least there needs to be a bit more emphasis on quality control. 

Dave


---

Comment by jhpalmieri created at 2010-04-20 22:52:25

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-20 22:52:25

Merged 2010/04/20.
