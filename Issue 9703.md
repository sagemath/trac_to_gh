# Issue 9703: Doctest failures caused by non-working sympow on Solaris x86

Issue created by migration from https://trac.sagemath.org/ticket/9703

Original creator: drkirkby

Original creation time: 2010-08-07 16:17:42

Assignee: GeorgSWeber

CC:  jhpalmieri jsp leif pjeremy fbissey was cremona mhansen

John Palmieri has built most of Sage on the host fulvia, but there are a number of tests related to sympow that are failing. The summary at the end shows:



```
The following tests failed:
<snip>
	sage -t  -long devel/sage/sage/lfunctions/sympow.py # 13 doctests failed
<snip>
Total time for all tests: 7305.2 seconds
```


Looking at the source code, it is not valid C, so it's quite possible the code gets mis-compiled. In fact, IMHO, gcc should reject the code - just as the Sun compiler does. 

I'll try to work out what was intended and see if the code can be re-written in a way that compiles with the Sun compiler, in which case gcc should have more chance of generating correct code.


---

Comment by drkirkby created at 2010-08-12 17:38:56

The same issue is observed on a 32-bit build on OpenSolaris.


---

Comment by mpatel created at 2010-08-16 01:59:29

By generating the data files directly, with `SAGE_LOCAL/lib/sympow/new_data`,  I was able to get the "optional" and "not tested" examples [here](http://www.sagemath.org/doc/reference/sage/lfunctions/sympow.html) to run.  To really run `./sympow -new_data 2` for the example `a = sympow.L(EllipticCurve('11a'), 2, 16); a`, I ran

```sh
$ ./sage -sh
> cd SAGE_LOCAL/lib/sympow
> ./new_data sh gp '-sp 2'
```

For the example `print sympow.Lderivs(EllipticCurve('11a'), 1, 16, 2)`, I ran

```sh
$ ./sage -sh
> cd SAGE_LOCAL/lib/sympow
> ./new_data sh gp '-sp 1 -dv 0'
> ./new_data sh gp '-sp 1 -dv 1'
> ./new_data sh gp '-sp 1 -dv 2'
```

It seems that part of the Sage interface to SYMPOW is broken.

But I don't know if missing data files caused the failures reported here and at #9166.


---

Comment by mpatel created at 2010-08-16 02:00:49

Replying to [comment:3 mpatel]:
> It seems that part of the Sage interface to SYMPOW is broken.

Or maybe `sympow` itself doesn't properly call `new_data`?


---

Comment by jhpalmieri created at 2010-08-16 05:44:28

On the other hand, there is this (after running "sage -sh" and "cd $SAGE_LOCAL/lib/sympow"):

```
$ ./sympow -curve "[0,-1,1,-10,-20]" -moddeg
sympow 1.018 RELEASE  (c) Mark Watkins -**ERROR** QD_check failed at x[1]
```

On my mac or on sage.math, this produces valid output, including the line

```
Modular Degree is 1
```

which is what is parsed by the `modular_degree` method.  So it looks to me as though sympow is really broken, not just its interface.  

(Furthermore, regardless of the C code, I think that sympow.py would never be accepted into Sage today: too many untested methods.)


---

Comment by jhpalmieri created at 2010-08-16 05:45:32

I wasn't clear enough above: the line `**ERROR**...` was produced on fulvia, an x86 box running Solaris.


---

Comment by drkirkby created at 2010-08-16 09:59:48

Replying to [comment:3 mpatel]:
> By generating the data files directly, with `SAGE_LOCAL/lib/sympow/new_data`,  I was able to get the "optional" and "not tested" examples [here](http://www.sagemath.org/doc/reference/sage/lfunctions/sympow.html) to run.  To really run `./sympow -new_data 2` for the example 

Try that on the *global* installation of sage on sage.math - not your own private one. 

I'm told part of the problem is that SYMPOW is trying to write data files below its installation directory. So it fails on a global installation of Sage, unless the user the user has root access. 

But there's very little error checking, so the fact the data files are not created is not reported. 

> It seems that part of the Sage interface to SYMPOW is broken.

If it was only that! 
 
> But I don't know if missing data files caused the failures reported here and at #9166.

To the best of my knowledge, not all examples need data files. When they do, a message is printed telling one how to create the data files. So that is not all the reason. That is certainly applied by the README file in the source code. 

I've run the `smypow` executable from the command line, and find problems unrelated to the generation of data files. 

It's not just the C code that is bad. There's a `Configure script` that starts with `#!/bin/sh`, then has code which checks if `sh` is on your system or not! 

My preference would be to remove this, or at least move it to experimental, but William seems keen to keep it as a standard package. It seems a bit strange to me given. 

 * This is apparently very specialised code. 
 * It is so badly written
 * It is causing problems on Solaris x86, Cygwin and ArchLinux. 

That seems an alful lot of problems 

I'm cc'ing a few people that I know have looked at SYMPOW at some point in the past. They might have some comments. Perhaps William has some comments to he would like to add to the ticket. 

Dave


---

Comment by fbissey created at 2010-08-16 10:42:42

Replying to [comment:7 drkirkby]:
> 
> Try that on the *global* installation of sage on sage.math - not your own private one. 
> 
> I'm told part of the problem is that SYMPOW is trying to write data files below its installation directory. So it fails on a global installation of Sage, unless the user the user has root access. 

I'll comment. I am the one who told that to David. I have shamelessly sat on this info for about 3 years. I noticed it when I first tried to package sympow for Gentoo as part of my sage porting drive. At the time I had to allow the directory where the sympow scripts are installed to be world writable....

That no one really noticed means that no one using a global sage install has been using sympow for their work. The only people using it must have used a private installation. We now have a fix for this problem in sage-on-gentoo, Christopher, the other sage-on-gentoo dev, has figured a way of getting sympow to write in $HOME/.sympow in the last month or so.

I think there is a case for trying to replace sympow. It seems like the original author has abandoned it - the sympow homepage has gone. Sage could become sympow
upstream. But given the quality of the code there is a high burden for maintenance. It probably would be more beneficial in the long run to rewrite the functionality altogether. Given that there are references I think it could be a nice student project. 

That's my opinion. 

Francois


---

Comment by cschwan created at 2010-08-16 12:44:54

Replying to [comment:8 fbissey]:
> That no one really noticed means that no one using a global sage install has been using sympow for their work. The only people using it must have used a private installation. We now have a fix for this problem in sage-on-gentoo, Christopher, the other sage-on-gentoo dev, has figured a way of getting sympow to write in $HOME/.sympow in the last month or so.

I prepared a small patch which should fix the directory/permission problems. I did not fully test it because I got little time but you should be able see its basic idea - it includes the sed fixes from our sage-on-gentoo overlay: http://github.com/cschwan/sage-on-gentoo/blob/master/sci-mathematics/sympow/sympow-1.018-r1.ebuild (look at it for more detailed comments on what the patch does). To successfully use it, apply it to sympow's source and do the following (would go into spkg-install):

 * install sympow's *.gp scripts into $SAGE_LOCAL/share/sympow
 * install sympow's datafiles (A012M.txt, A012S.txt and so on) into $SAGE_LOCAL/share/sympow/datafiles
 * the patch creates a wrapper script "sympow-start" which copies the datafiles from the share-directory to $HOME/.sympow (if it does not exist yet) so that sympow can read and write in that directory - give the script execute-permissions and make sure you start the script "sympow-start" instead of the binary. A better idea would be to rename the sympow binary and to rename the script to "sympow" (without "-start"), of course.

With the patch you also should be able to create the precomputed data which is needed for some optional tests.

Christopher


---

Comment by drkirkby created at 2010-08-22 01:31:40

I now have a better understanding of why SYMPOW is failing to work correctly on Cygwin and Solaris on x86 chips. SYMPOW makes use of the [Quad Double](http://crd.lbl.gov/~dhbailey/mpdist/) code which relies on IEE-754 double-precision maths, with a 53-bit mantissa and 64-bits in total. However, the default mode of the x86 CPUs is to use extended precision where 64-bits are used for the mantissa and 80 bits in total. It is necessary to change the mode of operation of the floating point processor in order that the Quad double code will work at all. SYMPOW had code for this in a file fpu.c, but it only worked on Linux. It made use of Linux-specific header files too. 

The main change necessary was to add some inline assembly code to alter the values of bits 8 and 9 in the 16-bit control register of the floating point processor. I got the relevant information about the exact bits needed from an old (1987) copy of the Intel 80387 Programmer's Reference Manual. 

Here's a revised package which builds and passes all relevant tests on 
 * OpenSolaris (32-bit) on x64 
 * Linux (64-bit)
 * OS X (64-bit)
 * Solaris 10 (32-bit) SPARC

It was not possible to test on Solaris 10 x86, as access to the Skynet machines is currently unavailable, but I do not believe ll present any problems, since it builds fine on OpenSolaris as a 32-bit application. 

http://boxen.math.washington.edu/home/kirkby/patches/sympow-1.018.1.p8.spkg

Apart from a couple of minor changes, it is the same code which Mike Hansen tested on Cygwin and said it works there too. 

I've not implemented Christopher's changes which are necessary to get this to pass all the optional tests. Someone who is more keen than me can open a ticket for that if they wish. I just want to see the back of this rather annoying package. 

A note to reviewers (mainly aimed at Leif!) I know there are 1001 things wrong with this package, but I have no desire to clean them all up. Please review on the basis of the actual changes I made - not what it might be desirable to make. Otherwise it will never get reviewed. 

## Test results a Sun Ultra 27 running OpenSolaris 06/2009 (Originally SYMPOW failed all tests on this workstation)

```
drkirkby@hawk:~/32/sage-4.5.3.alpha1$ uname -a
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
drkirkby@hawk:~/32/sage-4.5.3.alpha1$ cat /etc/release
                       OpenSolaris Development snv_134 X86
           Copyright 2010 Sun Microsystems, Inc.  All Rights Reserved.
                        Use is subject to license terms.
                             Assembled 01 March 2010
drkirkby@hawk:~/32/sage-4.5.3.alpha1$ ./sage -t  -long devel/sage/sage/modular/abvar/abvar.py
sage -t -long "devel/sage/sage/modular/abvar/abvar.py"      
	 [27.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 27.5 seconds
drkirkby@hawk:~/32/sage-4.5.3.alpha1$ ./sage -t  -long devel/sage/sage/lfunctions/sympow.py
sage -t -long "devel/sage/sage/lfunctions/sympow.py"        
	 [5.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.8 seconds
drkirkby@hawk:~/32/sage-4.5.3.alpha1$ ./sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
	 [212.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 212.8 seconds
drkirkby@hawk:~/32/sage-4.5.3.alpha1$ 
```

## Test results on Ubunta Linux (sage.math)

```
kirkby@sage:~/sage-4.5.alpha4$ uname -a
Linux sage.math.washington.edu 2.6.24-28-server #1 SMP Sat Jul 31 18:41:35 UTC 2010 x86_64 GNU/Linux
kirkby@sage:~/sage-4.5.alpha4$ cat /etc/issue
Ubuntu 8.04.4 LTS \n \l

kirkby@sage:~/sage-4.5.alpha4$ ./sage -t  -long devel/sage/sage/modular/abvar/abvar.py
sage -t -long "devel/sage/sage/modular/abvar/abvar.py"      
	 [34.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 34.1 seconds
kirkby@sage:~/sage-4.5.alpha4$ ./sage -t  -long devel/sage/sage/lfunctions/sympow.py
sage -t -long "devel/sage/sage/lfunctions/sympow.py"        
	 [9.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 9.1 seconds
kirkby@sage:~/sage-4.5.alpha4$ ./sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
	 [170.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 170.6 seconds
```


 == Test results on OS X (bsd.math) ==

```
[kirkby@bsd sage-4.5.rc1]$ uname -a
Darwin bsd.local 10.4.0 Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386 i386 i386 MacPro1,1 Darwin
[kirkby@bsd sage-4.5.rc1]$ ./sage -t  -long devel/sage/sage/modular/abvar/abvar.py
sage -t -long "devel/sage/sage/modular/abvar/abvar.py"      
	 [40.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 40.5 seconds
[kirkby@bsd sage-4.5.rc1]$ ./sage -t  -long devel/sage/sage/lfunctions/sympow.py
sage -t -long "devel/sage/sage/lfunctions/sympow.py"        
	 [7.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 7.7 seconds
[kirkby@bsd sage-4.5.rc1]$ ./sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
	 [184.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 184.0 seconds

```

 == Test results on a Sun T5240 SPARC running Solaris 10 update 7 (t2.math) ==

```
kirkby@t2:32 ~/t2/32/sage-4.5.3.alpha0$ uname -a
SunOS t2 5.10 Generic_141414-02 sun4v sparc SUNW,T5240
kirkby@t2:32 ~/t2/32/sage-4.5.3.alpha0$ cat /etc/release
                       Solaris 10 5/09 s10s_u7wos_08 SPARC
           Copyright 2009 Sun Microsystems, Inc.  All Rights Reserved.
                        Use is subject to license terms.
                             Assembled 30 March 2009
kirkby@t2:32 ~/t2/32/sage-4.5.3.alpha0$ 
kirkby@t2:32 ~/t2/32/sage-4.5.3.alpha0$ ./sage -t  -long devel/sage/sage/modular/abvar/abvar.py
sage -t -long "devel/sage/sage/modular/abvar/abvar.py"      
         [321.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 321.5 seconds
kirkby@t2:32 ~/t2/32/sage-4.5.3.alpha0$ ./sage -t  -long devel/sage/sage/lfunctions/sympow.py
sage -t -long "devel/sage/sage/lfunctions/sympow.py"        
         [89.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 89.2 seconds
kirkby@t2:32 ~/t2/32/sage-4.5.3.alpha0$ ./sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
         [3219.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3219.8 seconds

```

Dave


---

Comment by drkirkby created at 2010-08-22 01:31:40

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-08-22 01:33:09

Changes the FPU to double-precession IEEE-754 from Intel's expended precisiion.


---

Attachment

If #9722 is ready to merge soon and this ticket is also positively reviewed, I'll consider including this in a 4.5.3.alpha2.


---

Comment by mpatel created at 2010-08-23 13:26:24

Replying to [comment:12 mpatel]:
> If #9722 is ready to merge soon and this ticket is also positively reviewed, I'll consider including this in a 4.5.3.alpha2.

And #9693, too.


---

Comment by drkirkby created at 2010-08-23 13:38:13

Replying to [comment:13 mpatel]:
> Replying to [comment:12 mpatel]:
> > If #9722 is ready to merge soon and this ticket is also positively reviewed, I'll consider including this in a 4.5.3.alpha2.
> 
> And #9693, too.
Thank you. That would be great. That should give all doc tests passing on Solaris 10 x86, OpenSolaris and Solaris 10 SPARC. 

I just need someone to change it to positive. I think I've provided quite a bit of evidence that it passes the tests on every platform I can test on.


---

Attachment

Test whether FPU is 53-bit or more


---

Comment by jdemeyer created at 2010-08-23 14:01:33

Maybe the attached program might be useful.  It runs a simple computation to check whether or not the FPU is 53-bit or more.  For example, on a x86_64 Intel machine, I get:


```
gcc -mfpmath=387 testfpu.c -o testfpu && ./testfpu 134217728 134217728
a = 134217728, b = 134217728
result = 1
```


```
gcc -mfpmath=sse testfpu.c -o testfpu && ./testfpu 134217728 134217728
a = 134217728, b = 134217728
result = 0
```


```
gcc -mfpmath=387 -mpc64 testfpu.c -o testfpu && ./testfpu 134217728 134217728
a = 134217728, b = 134217728
result = 0
```


You could use to check
 * whether or not the patch needs to be applied
 * whether the result is correct after possibly applying the patch (do this on all systems!)


---

Comment by leif created at 2010-08-23 14:52:49

Sage 4.6.prealpha3, which includes this ticket, passed all tests (`ptestlong`) on 64-bit Fedora 13 (Core2, gcc 4.4.4), see also http://trac.sagemath.org/sage_trac/ticket/9343#comment:308 .


---

Comment by jdemeyer created at 2010-08-23 15:14:09

Sage 4.6.prealpha3, which includes this ticket, passed all tests (ptestlong) on a Sun UltraSPARC with Solaris 10.


---

Comment by drkirkby created at 2010-08-23 17:38:53

Replying to [comment:15 jdemeyer]:
> Maybe the attached program might be useful.  It runs a simple computation to check whether or not the FPU is 53-bit or more.  For example, on a x86_64 Intel machine, I get:

It is an interesting little program. It does show the behavior someone (probably you) suspected, that in 64-bit builds, the behaviour changes. 

> You could use to check
>  * whether or not the patch needs to be applied
>  * whether the result is correct after possibly applying the patch (do this on all systems!)

I don't personally feel there is a need to do this. 
 * It makes use of gcc-specific options. It would be nice to get Sage to build with the Sun compiler. At least now, this will try to build with the Sun compiler, and the error message seen is useful, as it highlights where the code is not valid C. 
 * Some of those compiler options may not be supported in gcc 4.0.1, which is the earliest Sage supports. I think you said some were very new. 
 * It was not done before, so I end up making further changes to a package which is already a complete mess. 
 * If the FPU is already in using the lower precision, changing the bits to put it there will do no harm. 
 * This has been quite extensively tested now, and has not failed on any system at all. 
 
I think if the result is incorrect (i.e. for some reason the FPU remained in the wrong precision), the doctests will pick this up very quickly. This was the reason the program built, but failed tests on Cygwin and Solairs x86. 

Dave


---

Comment by drkirkby created at 2010-08-23 17:39:45

Replying to [comment:16 leif]:
> Sage 4.6.prealpha3, which includes this ticket, passed all tests (`ptestlong`) on 64-bit Fedora 13 (Core2, gcc 4.4.4), see also http://trac.sagemath.org/sage_trac/ticket/9343#comment:308 .

Thank you for the Fedora confirmation. I had already tested on Ubunta, but not Fedora.


---

Comment by drkirkby created at 2010-08-23 17:41:48

Replying to [comment:17 jdemeyer]:
> Sage 4.6.prealpha3, which includes this ticket, passed all tests (ptestlong) on a Sun UltraSPARC with Solaris 10.
Note the SPARC that Jeroen used (a Sun Blade 1000 belonging to me), was not the same as as I used, which was the Sun T5240 (t2.,math). 

So that's confirmation on two different Sun systems. One running the 2005 release of Solaris 10, the other running a much more recent release. 

Dave


---

Comment by jdemeyer created at 2010-08-23 18:25:23

Replying to [comment:18 drkirkby]:
> > You could use to check
> >  * whether or not the patch needs to be applied
> >  * whether the result is correct after possibly applying the patch (do this on all systems!)
> 
> I don't personally feel there is a need to do this. 
>  * It makes use of gcc-specific options.
It doesn't.  I just added those options to show how the behaviour changes.  My idea would be to run testfpu.c without any options and check the result.

>  * It was not done before, so I end up making further changes to a package which is already a complete mess.
I believe that my program is a cleaner solution. For example, are you sure you don't need the patch on Darwin? Also, the following code looks very suspicious:

```
for machine_hardware in ix86 i386 i486 i586 i686 x86_64 i86pc ia64
```



---

Comment by jdemeyer created at 2010-08-23 19:19:45

By the way, my comment should not prevent this patch from being included in 4.5.3 if that was the plan.  If this patch works, I'm certainly happy with that.  I just wanted to indicate that there might be better ways to solve the issue.


---

Comment by drkirkby created at 2010-08-23 19:49:15

Replying to [comment:22 jdemeyer]:
> By the way, my comment should not prevent this patch from being included in 4.5.3 if that was the plan.  If this patch works, I'm certainly happy with that.  I just wanted to indicate that there might be better ways to solve the issue.

The:

 
`for machine_hardware in ix86 i386 i486 i586 i686 x86_64 i86pc ia64`

was there before - I only added `i86pc` and changed `x` to `machine_hardware`, as I thought it was a bit more informative. 

The fpu patch has never been applied on OS X - note the original code specifically checked the platform was Linux. But since the C code used Linux-specific header files, I could not simply apply it everywhere. 

Given SYMPOW is going to be withdrawn from Sage since it's poorly written and unmaintained, I think this is enough. You may notice today that Bill said on `sage-devel` that the author has made it clear he has no desire to maintain this package, as it works on his computer. 

I really want to avoid adding things to this code, since no matter what I do, it is still going to be very poor. This solves the only remaining Solaris x86 problem and is one less problem for the Cygwin port. 

Dave


---

Comment by mpatel created at 2010-08-23 21:48:04

I'm testing

 http://boxen.math.washington.edu/home/kirkby/patches/sympow-1.018.1.p8.spkg

on bsd, redhawk, sage, and t2.math.

The patch looks good to me, except that I'm not qualified to review the new `fpu.c`.  But apart from that, I think we have a positive review.

Jeroen, can you comment on `fpu.c`?  Alternatively, David, could you find someone to review this file?


---

Comment by mpatel created at 2010-08-23 22:13:52

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-08-23 22:17:03

Can we close #9166 if/when this ticket is merged?


---

Comment by drkirkby created at 2010-08-23 22:33:19

Replying to [comment:26 mpatel]:
> Can we close #9166 if/when this ticket is merged?

It should be possible, but you should wait for confirmation from Mike Hansen.

Mike confirmed the earlier version I wrote had worked on Cygwin and passed all tests. However, I had did make a small change since then. 

The change was only the way I wrote the numbers in fpu.c. Initially I wrote them as binary using `0b` in front of the 0's and 1's. Later I converted the two binary numbers to hex, so used `0x}} instead. I found using {{{0b` is not portable - it works with gcc, but not Sun Studio. 

So the only changes from the patch that Mike said worked were

 * Convert numbers from binary to hex form. 
 * Add a few more comments in SPKG.txt and/or fpu.c
 * Committed the changes to the repository. 

Dave


---

Comment by drkirkby created at 2010-08-23 22:34:49

Oops, I should have previewed that once more. 

`0b` was changed to `0x` and the numbers obviously changed from a string of 0's and 1's to the hexadecimal equivalents.


---

Comment by drkirkby created at 2010-08-23 22:54:24

Replying to [comment:24 mpatel]:
> I'm testing
> 
>  http://boxen.math.washington.edu/home/kirkby/patches/sympow-1.018.1.p8.spkg
> 
> on bsd, redhawk, sage, and t2.math.
> 
> The patch looks good to me, except that I'm not qualified to review the new `fpu.c`.  But apart from that, I think we have a positive review.
> 
> Jeroen, can you comment on `fpu.c`?  Alternatively, David, could you find someone to review this file?


I've asked on sage-devel if someone can comment on it. I suspect Jeroen can. Here's the 

[original fpu.c](http://boxen.math.washington.edu/home/kirkby/patches/sympow-1.018.1.p8/src/fpu.c)

and here's the changed version

[patched fpu.c](http://boxen.math.washington.edu/home/kirkby/patches/sympow-1.018.1.p8/patches/fpu.c) 

One obvious difference is the original code just writes a number to the control word, but I first read the control word, set two bits, then write the control word. 

The reason I did that was that one of the bits in that control word is reserved  by Intel, so I did not think it wise to write a number to the register directly. 

Having carefully read the documentation that comes with the later version of quad-double, the only changes that should be made to that code is the precision control bits, which is all I change. 

Dave


---

Comment by cwitty created at 2010-08-23 23:16:02

Changing status from needs_review to positive_review.


---

Comment by cwitty created at 2010-08-23 23:16:02

I've read and understood the new and old versions of fpu.c, and I confirm that the new version is equivalent to the old version under Linux but is more portable in general.  So positive review for fpu.c .

(I'll go ahead and mark as positive review, relying on mpatel's review for everything except fpu.c .)


---

Comment by mpatel created at 2010-08-23 23:20:50

Thanks, Carl!

Replying to [comment:24 mpatel]:
> I'm testing
> 
>  http://boxen.math.washington.edu/home/kirkby/patches/sympow-1.018.1.p8.spkg
> 
> on bsd, redhawk, sage, and t2.math.

The long doctests pass on these machines.


---

Comment by mpatel created at 2010-08-24 02:50:34

Resolution: fixed
