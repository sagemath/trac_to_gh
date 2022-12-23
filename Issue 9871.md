# Issue 9871: PolyBoRi incorrectly reports a GNU linker is used with gcc and produces libraries with text relocations.

Issue created by migration from https://trac.sagemath.org/ticket/9872

Original creator: drkirkby

Original creation time: 2010-09-08 03:52:49

Assignee: tbd

CC:  polybori jhpalmieri alexanderdreyer

When I try to build PolyBoRi on a Sun Ultra 27 running OpenSolaris, I notice the message:


```
GNU linker detected!
```


This message is in the SConstruct file and comes from some discussions on #6437.

It would appear the test is not useful on OpenSolaris, as the linker now takes the GNU options too. however, I don't feel this is a the cause of the main problem. 

A problem exists in that the link-editor thinks the library contains code which is not position independant - i.e. it is not PIC. This can be seen with the `elfdump` command. 


```
drkirkby@hawk:~/sage-4.5.3/local/lib$ elfdump -d libpolybori-0.6.4.so | grep TEXTREL
      [25]  TEXTREL           0                   
      [34]  FLAGS             0x4                 [ TEXTREL ]
```


and, what I assume is part of PolyBoRi as the version number is identical. 


```
drkirkby@hawk:~/sage-4.5.3/local/lib$ elfdump -d libgroebner-0.6.4.so  | grep TEXTREL
      [25]  TEXTREL           0                   
      [34]  FLAGS             0x4                 [ TEXTREL ]
```


This is a bad sign - see for example 

http://blogs.sun.com/rie/entry/my_relocations_don_t_fit

There should be no output from the above command, which is the case with most libraries. (Only ECL, PolyBoRi and Cliquer have this problem, but I've solved the Cliquer issue - see #9871)

As far as I can tell, -fPIC is used when building all the files, so there must be another reason for this problem. 

Dave 


---

Comment by AlexanderDreyer created at 2010-09-08 07:23:42

Is the OpenSolaris environment somewhere available on sage.math? 

My best,
  Alexander


---

Comment by drkirkby created at 2010-09-08 08:40:12

Replying to [comment:1 AlexanderDreyer]:
> Is the OpenSolaris environment somewhere available on sage.math? 
> 
> My best,
>   Alexander

No, there are no virtual machines on sage.math with OpenSolaris. 

However, whilst not OpenSolaris on x86, the issue with text relocations is seen on Solaris 10 on SPARC too - i.e. t2.math


```
kirkby@t2:64 ~/t2/32$ elfdump -d ./sage-4.5.3.alpha0/local/lib/libpolybori-0.6.4.so | grep TEXTREL
      [19]  TEXTREL           0                   
      [27]  FLAGS             0x4                 [ TEXTREL ]
kirkby@t2:64 ~/t2/32$ 
```


On OpenSolaris, the Sun linker does actually take all the GNU options, so getting the linker wrong is not a problem, so I would not waste too much time over that.

The method chosen to get the linker is not ideal. It is based on something I wrote, but I think my method is flawed. It assumes the first linker in the path is the one used by gcc, but there is no reason for that to be so, as gcc has the linker path hard-coded. I really no not know how best to find the linker used by gcc. As a long term solution, it would probably be worth looking at how autoconf does this. 

If you set up your environment on t2.math as detailed in /etc/motd, then PolyBoRi will chose the right linker, but the text relocation problem will be seen. This does not cause a problem with 32-bit builds, but it does with 64-bit builds. 

Since Sage is stable on 32-bit versions of Solaris 10 and OpenSolaris, we are looking to get it working 64-bit. The text relocation problem then comes more serious. There's a discussion of this issue on this blog 

http://blogs.sun.com/rie/entry/my_relocations_don_t_fit

What I found with ECL is that the Sun compiler will in fact produce a binary that does not have the issue, but that does not help us with Sage, as we must use gcc to compile a lot of Sage. 

Dave


---

Comment by drkirkby created at 2010-09-08 08:46:33

Replying to [comment:2 drkirkby]:
> What I found with ECL is that the Sun compiler will in fact produce a binary that does not have the issue, but that does not help us with Sage, as we must use gcc to compile a lot of Sage. 
> 
> Dave 

One could argue this is a gcc bug, as the Sun compiler is more clever and can work around the problem, but it's a gcc issue we need to work around. With Cliquer, it was just a matter of choosing the right options for the linker (see #9871), but in some cases it may need changes to the code, as discussed on that Sun blog. 

Dave


---

Comment by AlexanderDreyer created at 2010-09-08 08:50:23

Ok, may I copy your sage-4.5.3-alpha build from /scratch?


---

Comment by drkirkby created at 2010-09-08 09:38:18

Replying to [comment:4 AlexanderDreyer]:
> Ok, may I copy your sage-4.5.3-alpha build from /scratch?

I suggest you use my build at: 


```
/rootpool2/local/kirkby/t2/32/sage-4.5.3.rc0
```


as that's the latest version I have that's fully working. It passed all doc tests except one, but that then passed when I run it manually. 

As you will see, it has the issue. 

```
kirkby@t2:32 ~/t2/32/sage-4.5.3.rc0$ elfdump -d /rootpool2/local/kirkby/t2/32/sage-4.5.3.rc0/local/lib/libpolybori-0.6.4.so | grep TEXTREL
      [19]  TEXTREL           0                   
      [27]  FLAGS             0x4                 [ TEXTREL ]
```


Dave


---

Comment by AlexanderDreyer created at 2010-09-08 19:47:02

Does PolyBoRi really cause problems here? In Sage 4.5.3 the most recent patch #9768, which reintroduce PolyBori's dynamic libraries, is not included yet. it is a bug, that hte libraries lib*0.6.4.so are not removed after building, but Sage should link to the static libraries libpolybori.a etc.


---

Comment by drkirkby created at 2010-09-08 20:02:02

Replying to [comment:6 AlexanderDreyer]:
> Does PolyBoRi really cause problems here? In Sage 4.5.3 the most recent patch #9768, which reintroduce PolyBori's dynamic libraries, is not included yet. it is a bug, that hte libraries lib*0.6.4.so are not removed after building, but Sage should link to the static libraries libpolybori.a etc.

To be fair I am not aware of a problem caused by PolyBoRi.

But I know the other two packages which have the text relocations issues (Cliquer and R) have both caused serious problems. Since the problems are serious enough to stop Sage building fully, I can't say what will happen with PolyBoRi. 

If the shared libraries can be deleted, then that would solve the problem. But one would need to delete `libgroebner* libpboriCudd*` and `libpolybori*` Is that an acceptable solution? 

BTW, I found a better test for the linker - see below. I will try to get a script added to the $SAGE_LOCAL/bin to test the linker that gcc uses. 


```/bin/sh 
# Assume the -v option when passed directly to the linker 
# will output "GNU" or "Binutils" if using the GNU linker. 
# Even if some other linker accepts -v (which is quite a common option
# for software to support), we would not expect a non-GNU linker to 
# output the text "GNU" or "Binutils"

# If that does not work, assume a native linker. 

if [ "x`gcc -Wl,-v 2>&1 | egrep \"Binutils|GNU\"`" != x ] ; then 
   # It must be a GNU linker, as it has output the word "GNU" or "Binutils"
   echo "GNU" 
elif [ "x`uname`" = xSunOS ] ; then
  # It must be Sun's linker, as it's not GNU and there are no other linkers
  # used on Solaris. 
  echo "Sun"  
elif [ "x`uname`" = xHP-UX ] ; then
  # It must be HP's linker, as it's not GNU and there are no other linkers
  # used on HP-UX 
  echo "HP"  
elif [ "x`uname`" = xAIX ]; then
  # It must be IBM's linker as it's not GNU and there are no other linkers
  # used on AIX
  echo "IBM"     
else
  # A rare linker like Sun's on Linux, or Intel's on Linux might 
  # get here.  
  echo "Unknown" 
fi
```



---

Comment by AlexanderDreyer created at 2010-09-08 20:13:01

It would be `libgroebner*.so` `libpboriCudd*.so` and `libpolybori*.so`, which needs to be removed (still need the static ones!). But since I plan to reintroduce the dynamic libraries, this needs further investigation.
BTW: how did you debig the textref issue on cliquer?

I'll integrate your linke test in the next stable release.


---

Comment by drkirkby created at 2010-09-08 20:22:29

Replying to [comment:8 AlexanderDreyer]:
> It would be `libgroebner*.so` `libpboriCudd*.so` and `libpolybori*.so`, which needs to be removed (still need the static ones!). But since I plan to reintroduce the dynamic libraries, this needs further investigation.
> BTW: how did you debig the textref issue on cliquer?

I got there pretty quickly by changing the linker options to be the same as used on other platforms. I think R is going to be more of a challenge though - the R manual says R can't be built with gcc on 64-bit Solaris due to these problems. 

However, Leif makes an interesting remark at #9833, that a shared library should not have a main(). Do you by chance have a main in the shared library? He believes that is why Cliquer caused problems, though as I say, with different linker options the problem goes away. 

> I'll integrate your linker test in the next stable release.

Thank you. I would however use $CC rather than 'gcc'. The `-Wl,` option to pass something directly to the linker appears to work with all compilers I've tried. 

Dave


---

Comment by AlexanderDreyer created at 2010-09-09 10:49:36

Ok, it seems, that this issue could be fixed in likewise manner like you fixed it for cliquer.

So, I can easily fix this upstream. Is is necessary to backport it to the spkg of #9768? (It only makes sense for that spkg, sinc the dynamic libraries were ignored before.)

> > I'll integrate your linker test in the next stable release.
> 
> Thank you. I would however use $CC rather than 'gcc'. The `-Wl,` option to pass something directly to the linker appears to work with all compilers I've tried. 

Do you mean the environment variable $CC? The polybori spkg already uses its value.

My best,
   Alexander


---

Comment by drkirkby created at 2010-09-09 11:13:33

Replying to [comment:10 AlexanderDreyer]:
> Ok, it seems, that this issue could be fixed in likewise manner like you fixed it for cliquer.

No, changing a compiler flag will not necessarily work - I just got lucky with Cliquer. 

If it was a matter of just changing a compiler flag, I would have done it. There does not appear to be anything obviously wrong with the flags in PolyBoRi, though perhaps there's some subtle error I have not spotted.

There appears however to be several ways to write shared libraries which exhibit this problem - one way Leif said is to have a main(), though I've not confirmed that myself. Another is given on that Sun blog, by having data declared as constant. Another it to omit -fPIC when compiling, but I know you have not made that mistake. There are probably other ways. 

> So, I can easily fix this upstream. Is is necessary to backport it to the spkg of #9768? (It only makes sense for that spkg, sinc the dynamic libraries were ignored before.)

It would be good if you could remove the shared libraries, since if any code links to them, it will cause problems. I don't know enough about your code, but if there is a main() getting into the shared library code, then it might be sensible to do as Leif says, and conditionally include the main() only when building a standard-alone executable, but not when building a shared library. In essence, something like:


```
foobar1() {
} 
foobar2(){
}

#ifdef BUILDING_EXECUTABLE
  main() {
  foobar1();
  foobar2();
} 
#endif
```

and only include the compiler flag `-DBUILDING_EXECUTABLE` when building the code for the executable and not the libraries. 

I've no idea if that would work with your code or not. I really don't know where the problem is, and as you can see from that Sun blog, it is not the easiest thing to track down.  

> > > I'll integrate your linker test in the next stable release.
> > 
> > Thank you. I would however use $CC rather than 'gcc'. The `-Wl,` option to pass something directly to the linker appears to work with all compilers I've tried. 
> 
> Do you mean the environment variable $CC? The polybori spkg already uses its value.

Yes. My test code used 'gcc' as I quickly put it together yesterday to test an idea out. I've not tested it fully, but I would certainly replace my use of gcc in that script with $CC and check it works ok. 
 
> My best,
>    Alexander

Dave


---

Comment by AlexanderDreyer created at 2010-09-09 11:33:33

> No, changing a compiler flag will not necessarily work - I just got lucky with Cliquer. 
> 
> If it was a matter of just changing a compiler flag, I would have done it. There does not appear to be anything obviously wrong with the flags in PolyBoRi, though perhaps there's some subtle error I have not spotted.
Maybe, because you didn't test it with the most recent spkg, or mabe something went wrong the the flags propagation. When I changed the flags, the problem disappeared, i. e. elfdump didn't show any TEXTREL sections.
(But of course, I could only test this on t2.) I'll try to find some time to provide an updated spkg. Then you can test it on the other systems.


> Yes. My test code used 'gcc' as I quickly put it together yesterday to test an idea out. I've not tested it fully, but I would certainly replace my use of gcc in that script with $CC and check it works ok. 
Ah, sorry, I didn't get that this was about the script.

My best,
   Alexander


---

Comment by drkirkby created at 2010-09-09 12:11:58

Replying to [comment:12 AlexanderDreyer]:
> > No, changing a compiler flag will not necessarily work - I just got lucky with Cliquer. 
> > 
> > If it was a matter of just changing a compiler flag, I would have done it. There does not appear to be anything obviously wrong with the flags in PolyBoRi, though perhaps there's some subtle error I have not spotted.
> Maybe, because you didn't test it with the most recent spkg, or mabe something went wrong the the flags propagation. When I changed the flags, the problem disappeared, i. e. elfdump didn't show any TEXTREL sections.

I did not test the most recent package you are correct. 

> (But of course, I could only test this on t2.) I'll try to find some time to provide an updated spkg. Then you can test it on the other systems.


I think if it works on t2.math, with no text relocations, it will work on OpenSolaris and Solaris 10 on x86 too. Generally speaking, if a problem occurs on one of these systems it occurs on them all. 

Can you just confirm the link to download the latest version and I will do so. I need to go out now, so will be unable to report for several hours

Dave


---

Comment by AlexanderDreyer created at 2010-09-09 14:17:57

Try out this one:
http://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4.p6.spkg

My best,
  Alexander


---

Comment by AlexanderDreyer created at 2010-09-09 14:17:57

Changing status from new to needs_review.


---

Attachment

Hi Alexander, 

I'm not going to suggest you change this, as polybori-0.6.4.p5.spkg has positive review and I don't want to hold that up, as it fixes the main issue here, which is not the linker. 

Personally I would not have returned 'platform' though in the case of a non-GNU linker, as it is a bit inconsistent to return GNU when the GNU linker is used, and sunos, hp-ux or whatever when the GNU linker is not used. 

I think using Sun, HP, IBM etc would have been more consistent, or perhaps return the word "native" in the case of non-GNU linker. 

But it's a minor point. The main thing is your changes get this working. There are no longer any text relocations to deal with, which only leaves Cliquer, ECL and R which have this problem. Cliquer can be solved easily - R and ECL are less easy, though both are ok if built with the Sun compiler. 

Dave


---

Comment by drkirkby created at 2010-09-13 15:17:01

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 11:45:45

Just to check: Does this ticket subsume #9768 completely?


---

Comment by drkirkby created at 2010-09-15 12:11:58

The patch at http://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4.p6.spkg

fixes both the issues here and on #9768. An earlier version on the other ticket did not address this problem. So only http://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4.p6.spkg needs to be merged. 

Dave


---

Comment by mpatel created at 2010-09-16 00:48:36

Resolution: fixed
