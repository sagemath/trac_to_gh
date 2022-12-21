# Issue 6743: port Sage to Microsoft Windows (via Cygwin)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-08-14 06:41:45

Assignee: tbd

CC:  dimpase mhansen jpflori kcrisman simonking




---

Comment by was created at 2009-08-14 06:42:54

The goal of this ticket is to port the standard Sage release to at least build and startup under Cygwin with GCC>=4.3.2.

This ticket could be closed by any significant advanced in this direction that can be merged in.


---

Attachment


---

Attachment


---

Attachment


---

Comment by was created at 2009-10-24 22:37:52

Important remark.  I got passed a lot of issues toward startup by copying csage.so to be /bin/csage.dll.   Also, this program is very helpful: http://www.dependencywalker.com/


---

Comment by was created at 2009-10-24 23:00:26

After using the dependency thing above, and only importing half the sage library, I finally got to test out libsingular... and it works fine!

```
sage: R.<x,y,z> = QQ[]
sage: f = (x+y+z+1)^2; f
x^2 + 2*x*y + y^2 + 2*x*z + 2*y*z + z^2 + 2*x + 2*y + 2*z + 1
sage: type(f)
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
```



Another key point is one should increase the RAM available to cygwin by editing the registry, as explained in the Cygwin user's manual.  The default 384MB limit with all cygwin installs is way way too small for sage.  Make it a gig. 

My working sage install is /home/wstein/sage-4.1 on the winxp3 virtual machine.


---

Comment by was created at 2010-02-14 06:55:56

Changing assignee from tbd to was.


---

Comment by was created at 2010-02-16 02:57:43

I rebased the sage library patch to get the sage library to build against sage-4.3.3.  Applying this patch *and* fixing some library naming issues (mainly .so --> .dll) allows "sage -b" to work. Sage does not startup though.


---

Attachment

these are my notes when I tried to build sage-4.3.3.alpha0 from source on cygwin


---

Attachment


---

Comment by mhansen created at 2010-02-16 08:11:19

Changing component from porting to cygwin.


---

Comment by kcrisman created at 2011-06-15 23:28:44

Anyone interested in this should check out [the wiki page](CygwinPort) for the latest.


---

Comment by kcrisman created at 2011-06-28 18:50:28

My proposal is that once Cygwin actually is able to be built out of the box (not necessarily running) that this ticket is then closed by updating prereq to include the various prereqs.  Again, see [the Cygwin wiki page on Sage Trac](CygwinPort) for details of what is currently needed.


---

Comment by kcrisman created at 2011-06-29 03:11:22

Updating description to have more precise instructions, at least for one particular setup that will hopefully work.


---

Comment by kcrisman created at 2011-06-30 01:00:34

I just got Sage to build on Cygwin 1.7.3 (not most recent) on XP (not most recent) with the ONLY stops being once when the computer decided to do an automatic update and restarted, and once when I had to add the patch at #11499.  So I would say that this is as close to automatic as you can get.  (Once again, Maxima built fun - and runs in `sage -maxima`.)


---

Comment by saliola created at 2011-07-05 04:19:07

I just tried to go through the install on Windows 7 and Cygwin 1.7.9-1 (latest version) with sage-4.7.1.alpha4, but there was an error while building python. I'm going to attach the install.log file.


---

Attachment

windows 7, cygwin 1.7.9-1, python build error


---

Comment by mhansen created at 2011-07-05 04:29:54

Franco, see http://cygwin.com/faq/faq.using.html#faq.using.bloda .  You may also want to do a rebaseall.


---

Comment by mhansen created at 2011-07-05 04:31:53

Also, see http://comments.gmane.org/gmane.os.cygwin.xfree/20979


---

Comment by kcrisman created at 2011-07-05 14:01:08

Replying to [comment:30 saliola]:
> I just tried to go through the install on Windows 7 and Cygwin 1.7.9-1 (latest version) with sage-4.7.1.alpha4, but there was an error while building python. I'm going to attach the install.log file.
> 
Thanks so much for trying this.  I think that it's almost certainly the case that mhansen's comment will lead you to happiness.  The Python spkg seems to be particularly vulnerable to this problem, in other reports as well as my own experience.  By the way, there are more detailed instructions about how to rebase the Sage dlls (not just the system ones) at the [wiki page about this](CygwinPort).


---

Comment by kcrisman created at 2011-07-05 14:02:10

Replying to [comment:32 mhansen]:
> Also, see http://comments.gmane.org/gmane.os.cygwin.xfree/20979
Which precise comment?  [http://permalink.gmane.org/gmane.os.cygwin.xfree/21742](http://permalink.gmane.org/gmane.os.cygwin.xfree/21742) or [http://permalink.gmane.org/gmane.os.cygwin.xfree/21344](http://permalink.gmane.org/gmane.os.cygwin.xfree/21344) or a different one?


---

Comment by saliola created at 2011-07-05 14:24:19

Replying to [comment:33 kcrisman]:
> Thanks so much for trying this.

It is the least I can do, considering all the hard work by all of you. Your email on sage-devel convinced me to try.

> I think that it's almost certainly the case that mhansen's comment will lead you to happiness.  The Python spkg seems to be particularly vulnerable to this problem, in other reports as well as my own experience.  By the way, there are more detailed instructions about how to rebase the Sage dlls (not just the system ones) at the [wiki page about this](CygwinPort).

So far, I just rebased Cygwin using `rebaseall -v`. I don't know whether this also rebases the Sage dlls, but the compilation is now continuing (it finished compiling Python).

I'm convinced that my problem is related to Windows update. I have Windows 7 installed on a partition on my laptop and almost never boot into it. It was really, really behind on updates, and Windows just kept on applying update and update (even after it told me there were no more updates to apply, it somehow managed to download some new updates....). It seems to have stopped updating now. Fingers crossed.


---

Comment by kcrisman created at 2011-07-05 14:26:03

> I'm convinced that my problem is related to Windows update. I have Windows 7 installed on a partition on my laptop and almost never boot into it. It was really, really behind on updates, and Windows just kept on applying update and update (even after it told me there were no more updates to apply, it somehow managed to download some new updates....). It seems to have stopped updating now. Fingers crossed.

Yes, you are totally right about this problem.  Windows just does it again and again without really asking.

You know what I do?  I disconnect from the internet :)  But that is on a computer I rented from our IT just for this purpose, hard to do with a main computer.


---

Comment by leif created at 2011-07-12 18:14:57

FLINT spkg now references the new p8 ([re]based on the latest p7 from #11246), located on `spkg-upload`.


---

Comment by was created at 2011-08-24 23:48:12

Changing keywords from "" to "sd32".


---

Comment by kcrisman created at 2011-08-25 01:43:22

Changing keywords from "sd32" to "sd31 sd32".


---

Comment by jpflori created at 2012-07-10 21:34:43

For info, to build the python spkg 2.7.3-p0 from sage 5.1.rc1, at least the patches from python issue tracker issues 9665, 14437, 14438 are needed.


---

Comment by kcrisman created at 2012-07-11 02:04:57

If you can also update [CygwinPort](CygwinPort), that would be wonderful!  (This is just for building - that is for _everything_.)


---

Comment by jpflori created at 2012-07-11 02:06:23

I'll do when I'm finished (if that ever happens).
I've just beaten MPIR, don't know what's coming next.
The main issue is that everything is so slow....


---

Comment by kcrisman created at 2012-07-11 02:08:38

> I'll do when I'm finished (if that ever happens).
Yeah, just be sure to keep every issue if you only know it works on one kind of Windows.
> I've just beaten MPIR, don't know what's coming next.
Hopefully just #12089 and then the Pari segfault?  We'll see.
> The main issue is that everything is so slow....
True.  And rebasing.


---

Comment by jpflori created at 2012-12-06 15:52:09

I had to install zlib-devel as well or had horrible linking problems with freetype and gd.


---

Comment by kcrisman created at 2012-12-06 16:19:32

> I had to install zlib-devel as well or had horrible linking problems with freetype and gd.
Huh, maybe that's only on Win 7.  Well, add it to the list here and on the [CygwinPort](CygwinPort) page.


---

Comment by kcrisman created at 2012-12-18 21:09:56

What we now need is mainly an update to the prereq spkg.  We need to somehow check for:
 * `file`
 * `patch`
 * `liblapack`, `liblapack0`, `liblapack-devel`
 * `libiconv`, `openssl`, `openssl-devel`
 * `libgc-devel`
 * `zlib-devel`
 * `libncurses-devel`
 * `make`, `perl`, `m4`
 * `gcc4-x.y.z` and `g++-x.y.z`, `fortran`; the versions *must* match
How does one go about doing this?  I assume that it should happen in `prereq-1.x-install` and not the configure, but I don't know a lot about these things.  I've also asked about this at [this sage-devel thread](https://groups.google.com/forum/?fromgroups#!topic/sage-devel/NAWeTIsQrQw).


---

Comment by jdemeyer created at 2012-12-19 08:01:56

Replying to [comment:72 kcrisman]:
> What we now need is mainly an update to the prereq spkg.  We need to somehow check for:
>  * `file`
Why is this needed? I don't think Sage should ever use `file`.

>  * `patch`
Why do we need this? `patch` comes with Sage.

>  * `liblapack`, `liblapack0`, `liblapack-devel`
Why do we need this? `lapack` comes with Sage.

>  * `libiconv`
Why do we need this? `iconv` comes with Sage.

>  * `openssl`, `openssl-devel`
I don't think these are required anymore.

>  * `libgc-devel`
Is this `boehm_gc`? This comes with Sage.

>  * `zlib-devel`
Why do we need this? `zlib` comes with Sage.

>  * `libncurses-devel`
Are you sure this is needed? Does #12725 help with not requiring `ncurses`?

>  * `make`, `perl`, `m4`
This is already checked I believe.

>  * `gcc4-x.y.z` and `g++-x.y.z`, `fortran`; the versions *must* match
So, the GCC spkg doesn't build on Cygwin? Then also `spkg/install` should be changed not to install GCC on Cygwin. The version checking already exists.

> I assume that it should happen in `prereq-1.x-install` and not the configure.
Please don't! Ideally, `prereq-1.x-install` should be essentially empty and all checks are done in `configure`. That's how things are supposed to be done autotools-style.


---

Comment by jpflori created at 2012-12-19 08:23:50

The resulting install is not that bad, see
http://boxen.math.washington.edu/home/jpflori/ptest-sage-5.5.rc0-cygwin.log

I got a lot of OverflowError, surely due to the fact that I'm running a 64 bits Windows 7.
And my install also lacks some tickets posted here and there on Trac.

Not sure about the prereq, but I seem to remember that without zlib-devel a lot of things including zlib-devel got messed up in freetype and spkg depending on it (I'd say gd), I'll try to dig out the logs.

About patch, not sure what http://trac.sagemath.org/sage_trac/ticket/11232 does.


---

Comment by jpflori created at 2012-12-19 10:09:37

I've reinstalled a minimal Cygwin (a few weeks old though, no internet access on the used computer right now) and will add required Cygwin packages incrementally to be sure of what matters.


---

Comment by vbraun created at 2012-12-19 12:04:45

First of all, please put the cygwin package checking into its own script. Its opposite to any sane prerequisite checking, but then thats because the underlying platform lacks sanity.

Each Cygwin package installs a gzipped listing of files under `/etc/setup/<package>.lst.gz`, so I would use that to check that the prerequisite packages are installed. As usual, setting `SAGE_PORT=yes` should let you skip the prerequisite check if you think you know better.


---

Comment by dimpase created at 2012-12-19 12:52:37

Replying to [comment:73 jdemeyer]:
> >  * `liblapack`, `liblapack0`, `liblapack-devel`
> Why do we need this? `lapack` comes with Sage.
> 
atlas 3.8 does not build on cygwin.


---

Comment by kcrisman created at 2012-12-19 14:17:32

> > What we now need is mainly an update to the prereq spkg.  We need to somehow check for:
> >  * `file`
> Why is this needed? I don't think Sage should ever use `file`.

I appreciate all the questions here trying to narrow it down.  However, I think the point is to FIRST get Sage to build reliably on Cygwin, and if we need all these things, then so be it.  We can remove them later, precisely because we're not targeting people just randomly building Sage on Cygwin.

Also, these were definitely all needed at some point in the process, but it's been 3+ years, so of course some might not be.  But Cygwin is _remarkably_ picky about these things.  With respect to patch, for instance, why not just require it on such an unusual platform?

Similarly, I have no idea if the gcc package builds on Cygwin, but we still need _some_ compiler to build _that_!  It would be worth testing it without that, but I at least have no time to try all the various permutations and combinations of prereqs.  Let's get this done first, then remove things we don't need, otherwise we'll _never_ catch up to Sage (if only because of updates to spkgs).


---

Comment by jdemeyer created at 2012-12-19 14:27:15

Replying to [comment:78 kcrisman]:
> I appreciate all the questions here trying to narrow it down.  However, I think the point is to FIRST get Sage to build reliably on Cygwin, and if we need all these things, then so be it.  We can remove them later, precisely because we're not targeting people just randomly building Sage on Cygwin.

If you're still at this early stage like you're suggesting, maybe updating the prereq should be postponed until it's clearer what the real requirements are. What's the point of putting effort in checking some dependency if the dependency might be removed in a next release? (honest question, no offense meant)


---

Comment by jdemeyer created at 2012-12-19 14:28:46

Replying to [comment:78 kcrisman]:
> I have no idea if the gcc package builds on Cygwin, but we still need _some_ compiler to build _that_!
Sure, but this is already checked in `prereq`. Also, the fact that the gcc/g++/gfortran versions match (if GCC isn't built) is checked already. Both these are relevant for all platforms, not only Cygwin.


---

Comment by kcrisman created at 2012-12-19 14:38:55

> > I have no idea if the gcc package builds on Cygwin, but we still need _some_ compiler to build _that_!
> Sure, but this is already checked in `prereq`. Also, the fact that the gcc/g++/gfortran versions match (if GCC isn't built) is checked already. Both these are relevant for all platforms, not only Cygwin.
Oh, that's very helpful.
> What's the point of putting effort in checking some dependency if the dependency might be removed in a next release? (honest question, no offense meant)
None taken.  The amount of effort put into this port thus far by JP, Mike Hansen, William, Dima, myself, ... I think that I probably speak for them in saying that the marginal effort of checking for the dependency is nil compared to the value of not having to worry about it.  That said, naturally if JP wants to check them, I'm not opposed. 

I should also point out that I will not have access to my XP machine starting Friday afternoon US for several weeks, so anything XP-specific would be nice to have resolved by then.


---

Comment by jpflori created at 2012-12-19 23:19:03

For what it is worth, I've begun looking at prereqs for cygwin by starting with a minimal cygwin install and only adding packages when needed and am posting results on the [CygwinPort](CygwinPort) page.

In particular, something should be done for libiconv.

As far as the gcc spkg is concerned I got a segfault earlier after a few hours.
Maybe that was just because of memory leaks and memory exhaustion, so Ive relaunched a build now, but it takes hours...


---

Comment by jpflori created at 2012-12-20 12:17:13

So the gcc spkg failed again because of exhaustion memory, but restarting from the build dir finishes fine and everything seems ok then.


---

Comment by jpflori created at 2012-12-20 12:34:08

In fact it seems to fail to compile ECL from #13324.


---

Comment by jpflori created at 2012-12-20 12:41:32

The ECL problem was already encountered here:
http://sourceforge.net/mailarchive/message.php?msg_id=28466506

(This did not happen with the Cywgin gcc 4.5.something.)


---

Comment by jpflori created at 2012-12-20 14:29:37

Replying to [comment:77 dimpase]:
> Replying to [comment:73 jdemeyer]:
> > >  * `liblapack`, `liblapack0`, `liblapack-devel`
> > Why do we need this? `lapack` comes with Sage.
> > 
> atlas 3.8 does not build on cygwin. 
> 
Any hint why?

Will atlas 3.10 from #10508 fix this issue?


---

Comment by vbraun created at 2012-12-20 14:54:34

Its possible to build ATLAS on Windows but as with both ATLAS and Windows my best guess is that it won't work right out of the box. I certainly haven't even tried.


---

Comment by dimpase created at 2012-12-20 14:58:02

Replying to [comment:86 jpflori]:
> Replying to [comment:77 dimpase]:
> > Replying to [comment:73 jdemeyer]:
> > > >  * `liblapack`, `liblapack0`, `liblapack-devel`
> > > Why do we need this? `lapack` comes with Sage.
> > > 
> > atlas 3.8 does not build on cygwin. 
> > 
> Any hint why?

E.g. [MANIFEST crap](https://sites.google.com/site/dpovey/compilation-instructions-for-atlas-with-cygwin-under-windows-7)
I imagine it's only part of the story.
> 
> Will atlas 3.10 from #10508 fix this issue?
perhaps. Or maybe not... But, again, the more stuff we build, the more stuff we will need to rebase, etc...

Actually, we should make a Windows batch file to automate the build/rebase loop.


---

Comment by jpflori created at 2012-12-20 15:11:54

Not sure if cygwin got better, but with my 5.5.rc0 I only had to rebase when I actually wanted to launch sage, so this might not be a real issue anymore.

The most worrying things for me are:
* memory leaks, I've removed many things which made dlls from windows linked to different cygwin process and I don't see anything fishy now, but they are still here,
* slowness, especially for all the configure stuff.


---

Comment by jpflori created at 2012-12-20 16:04:57

About ATLAS, I'm mostly asking that because the policy of Sage seems to be: require the fewest system packages as possible.

So if ATLAS can be built without much hassle let's build it by default, just as we only require gcc and build g++ and gfortran by default and try to build patch.

The user can always decide to install the g++ and gfortran and to set SAGE_ATLAS_LIB.

Personally I never install the ATLAS spkg, but use the system one, because it always took ages to build when it did not fail, and could never correctly detect my cpus to choose a sensible default.
I would be very happy to use my system patch as well (but I guess that some creepy system do not even provide a working patch so the spkg is needed).


---

Comment by jpflori created at 2012-12-21 16:42:48

Replying to [comment:88 dimpase]:
> Replying to [comment:86 jpflori]:
> > Replying to [comment:77 dimpase]:
> > > Replying to [comment:73 jdemeyer]:
> > > > >  * `liblapack`, `liblapack0`, `liblapack-devel`
> > > > Why do we need this? `lapack` comes with Sage.
> > > > 
> > > atlas 3.8 does not build on cygwin. 
> > > 
> > Any hint why?
> 
> E.g. [MANIFEST crap](https://sites.google.com/site/dpovey/compilation-instructions-for-atlas-with-cygwin-under-windows-7)
> I imagine it's only part of the story.
No it looks like its all of it and is not needed anymore from 3.9.

The final crap is because they want a .lib file we do not care about.
> > 
> > Will atlas 3.10 from #10508 fix this issue?
> perhaps. Or maybe not... But, again, the more stuff we build, the more stuff we will need to rebase, etc...
> 
> Actually, we should make a Windows batch file to automate the build/rebase loop.
>


---

Comment by kcrisman created at 2013-01-04 14:38:52

By the way, JP, did you end up needing libiconv or not?


---

Comment by jpflori created at 2013-01-04 14:43:32

Replying to [comment:93 kcrisman]:
> By the way, JP, did you end up needing libiconv or not?
Not sure yet if the one provided by cygwin is now sufficient.
I'll test this weekend.

What is sure is that building the libiconv spkg on a minimal cygwin was a real pain.
But I'll provide that as well, for "completeness".


---

Comment by kcrisman created at 2013-01-04 16:47:07

> I'll test this weekend.
I see now that we only use the iconv spkg on Solaris, Cygwin, and (?) HP-UX, so maybe in the meantime we don't need it.
> What is sure is that building the libiconv spkg on a minimal cygwin was a real pain.
Or maybe we do...
> But I'll provide that as well, for "completeness".


---

Comment by jpflori created at 2013-01-04 16:52:35

The easiest way to build the libiconv spkg is to install the Cygwin libiconv package, although I don't think it is the most proper solution as it add a (kind of lame) new dependency.

Apart from that, it is also possible that now, building our own spkg is not necessary anymore, Cygwin package seem to tend to become better as time passes (see the libm example, we now do not need to build our own cephes!).


---

Comment by jdemeyer created at 2013-01-08 12:53:41

Dear Cygwin testers, could you please test the following two PARI packages, whether these build (if possible with `SAGE_CHECK=yes`) and whether `./sage --gp` seems to work.

1. [http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p2.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p2.spkg) (a plain bug-fix package, #13921)

2. [http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p3.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p3.spkg) (some Cygwin-specific workarounds removed)


---

Comment by kcrisman created at 2013-01-15 18:08:39

> 1. [http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p2.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p2.spkg) (a plain bug-fix package, #13921)
> 
Looks like JP experienced success with this, given that he compiled 5.6.rc0.  I'm currently doing this one.

> 2. [http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p3.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p3.spkg) (some Cygwin-specific workarounds removed)

Making him aware of this one - I assume there isn't a ticket yet :)


---

Comment by jpflori created at 2013-01-15 18:33:44

Not sure what exactly the pari p3 spkg is but the changes look sane (if the first hacks are indeed not needed anymore, the second one definitely looks useless now).


---

Comment by kcrisman created at 2013-01-15 18:44:49

> 1. [http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p2.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p2.spkg) (a plain bug-fix package, #13921)
With `SAGE_CHECK=yes`, I get a successful installation and almost successful tests.  However, the factoring example in the description of #13921 works fine.  Here's [the only failure](http://sage.math.washington.edu/home/kcrisman/program-sta.dif):

```
*** ../src/test/32/program	2012-09-25 17:10:47.000000000 -0400
--- gp.out	2013-01-15 13:26:27.531250000 -0500
***************
*** 129,137 ****
  400 1.632424285532931448171405619
  ? install(addii,GG)
  ? addii(1,2)
! 3
  ? kill(addii)
  ? getheap
! [23, 3317]
  ? print("Total time spent: ",gettime);
! Total time spent: 24
--- 129,139 ----
  400 1.632424285532931448171405619
  ? install(addii,GG)
  ? addii(1,2)
!   ***   at top-level: addii(1,2)
!   ***                 ^----------
!   *** addii: bug in PARI/GP (Segmentation Fault), please report
  ? kill(addii)
  ? getheap
! [22, 3310]
  ? print("Total time spent: ",gettime);
! Total time spent: 31
```

> 2. [http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p3.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p3.spkg) (some Cygwin-specific workarounds removed)
I'll check this next.


---

Comment by kcrisman created at 2013-01-15 18:49:13

Replying to [comment:102 jpflori]:
Just checking - looks like you removed zlib-devel, libgc-devel, file, and patch from the prereqs - but are these fixes in yet?  Add these if necessary above.  What happened to libgc-devel and file?
 * #13914
 * #13844


---

Comment by kcrisman created at 2013-01-15 19:12:36

> > 2. [http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p3.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/pari-2.5.3.p3.spkg) (some Cygwin-specific workarounds removed)
> I'll check this next.
It built and installed fine, with pretty much the same exact error in the tests, and factored the huge number fine in the console.  If all else is well, these spkgs can be included.  Well, I guess one of them is :)


---

Comment by kcrisman created at 2013-01-15 19:18:13

> Not sure what exactly the pari p3 spkg is but the changes look sane (if the first hacks are indeed not needed anymore, the second one definitely looks useless now).

I can't comment on whether these really are or are not necessary, but apparently not if self-tests are passing?  I haven't had a chance to test any files that _use_ Pari, and I'll probably get forking errors anyway :(


---

Comment by jpflori created at 2013-01-15 20:21:47

Replying to [comment:105 kcrisman]:
> Replying to [comment:102 jpflori]:
> Just checking - looks like you removed zlib-devel, libgc-devel, file, and patch from the prereqs - but are these fixes in yet?  Add these if necessary above.  What happened to libgc-devel and file?
>  * #13914
>  * #13844
I removed them because I was able to build and run Sage without installing them;
Quoting from [CygwinPort](CygwinPort) the Cygwin packages I have installed:

```
$ cygcheck -c
Cygwin Package Information
Package              Version              Status
_autorebase          000192-1             OK
_update-info-dir     01100-1              OK
alternatives         1.3.30c-10           OK
base-cygwin          3.1-1                OK
base-files           4.1-1                OK
bash                 4.1.10-4             OK
binutils             2.22.51-2            OK
bzip2                1.0.6-2              OK
coreutils            8.15-1               OK
crypt                1.2-1                OK
csih                 0.9.6-1              OK
cygrunsrv            1.40-2               OK
cygutils             1.4.10-2             OK
cygwin               1.7.17-1             OK
cygwin-doc           1.7-1                OK
dash                 0.5.7-1              OK
diffutils            3.2-1                OK
dos2unix             6.0.2-1              OK
editrights           1.01-2               OK
file                 5.11-1               OK
findutils            4.5.9-2              OK
gawk                 4.0.2-1              OK
gcc4-core            4.5.3-3              OK
gettext              0.18.1.1-2           OK
grep                 2.6.3-1              OK
groff                1.21-2               OK
gzip                 1.4-1                OK
ipc-utils            1.0-1                OK
lapack               3.4.2-1              OK
less                 444-1                OK
libasn1_8            1.5.2-4              OK
libattr1             2.4.46-1             OK
libbz2_1             1.0.6-2              OK
libcharset1          1.14-2               OK
libcloog0            0.15.7-1             OK
libcom_err2          1.42.6-1             OK
libdb4.5             4.5.20.2-3           OK
libedit0             20120311-1           OK
libexpat1            2.1.0-1              OK
libffi4              4.5.3-3              OK
libgcc1              4.5.3-3              OK
libgdbm4             1.8.3-20             OK
libgfortran3         4.5.3-3              OK
libgmp3              4.3.2-1              OK
libgmpxx4            4.3.2-1              OK
libgomp1             4.5.3-3              OK
libgssapi3           1.5.2-4              OK
libheimbase1         1.5.2-4              OK
libheimntlm0         1.5.2-4              OK
libhx509_5           1.5.2-4              OK
libiconv             1.14-2               OK
libiconv2            1.14-2               OK
libintl8             0.18.1.1-2           OK
libkafs0             1.5.2-4              OK
libkrb5_26           1.5.2-4              OK
liblapack-devel      3.4.2-1              OK
liblapack0           3.4.2-1              OK
liblzma5             5.0.2_20110517-1     OK
libmpc1              0.8-1                OK
libmpfr1             2.4.1-4              OK
libmpfr4             3.0.1-1              OK
libncurses-devel     5.7-18               OK
libncurses10         5.7-18               OK
libncurses9          5.7-16               OK
libncursesw10        5.7-18               OK
libopenssl100        1.0.1c-2             OK
libpcre0             8.21-2               OK
libpopt0             1.6.4-4              OK
libppl               0.10.2-1             OK
libreadline7         6.1.2-3              OK
libroken18           1.5.2-4              OK
libsigsegv2          2.10-1               OK
libsqlite3_0         3.7.13-1             OK
libssp0              4.5.3-3              OK
libstdc++6           4.5.3-3              OK
libwind0             1.5.2-4              OK
libwrap0             7.6-21               OK
libxml2              2.9.0-1              OK
login                1.10-10              OK
m4                   1.4.16-1             OK
make                 3.82.90-1            OK
man                  1.6g-1               OK
mintty               1.1.2-1              OK
nano                 2.2.5-1              OK
openssh              6.1p1-1              OK
perl                 5.14.2-3             OK
perl_vendor          5.14.2-3             OK
rebase               4.3.0-1              OK
run                  1.1.13-1             OK
sed                  4.2.1-2              OK
tar                  1.26-1               OK
terminfo             5.7_20091114-14      OK
texinfo              4.13-4               OK
tzcode               2012j-1              OK
w32api               9999-1               OK
w32api-headers       3.0b_svn5496-1       OK
w32api-runtime       3.0b_svn5496-1       OK
which                2.20-2               OK
xz                   5.0.2_20110517-1     OK
zlib0                1.2.7-1              OK
```

you can check they were indeed not installed.

Of course, you don't need patch and zlib-devel if you use the fixed spkg I posted at #13844 and #13914, not sure about libgc-devel, but hey it was not there and I had no problems yet.
Of course I did not test everything so if it appears it is really needed, I'll put it back it as a prereq to "run" Sage.


---

Comment by jpflori created at 2013-01-15 20:25:47

Replying to [comment:107 kcrisman]:
> > Not sure what exactly the pari p3 spkg is but the changes look sane (if the first hacks are indeed not needed anymore, the second one definitely looks useless now).
> 
> I can't comment on whether these really are or are not necessary, but apparently not if self-tests are passing?  I haven't had a chance to test any files that _use_ Pari, and I'll probably get forking errors anyway :(
If both you oon XP and I on 7 are able to "build" PARI, then these changes should definitely get in.
They remove useless Cygwin specific "hacks", so this is a good thing.

And as I said, I think the second one is indeed useless, I barely have doubts about that, as it must have been fixed by a patch I suggested upstream.

As far as the second one is concerned, the fact you could build PARI leaves little doubt as well.


---

Comment by kcrisman created at 2013-01-15 20:28:00

Replying to [comment:109 jpflori]:
> Replying to [comment:105 kcrisman]:
> > Replying to [comment:102 jpflori]:
> > Just checking - looks like you removed zlib-devel, libgc-devel, file, and patch from the prereqs - but are these fixes in yet?  Add these if necessary above.  What happened to libgc-devel and file?
> >  * #13914
> >  * #13844
> I removed them because I was able to build and run Sage without installing them;
My point was that you didn't add the two tickets here, without which assuredly patch would not have worked, which is used a lot!  I added them to the list above, as you can check.

But `file` is in your list in comment:109, so I'm not sure why you removed it from the list.  Did it install with something else automatically?
> Of course, you don't need patch and zlib-devel if you use the fixed spkg I posted at #13844 and #13914, not sure about libgc-devel, but hey it was not there and I had no problems yet.
> Of course I did not test everything so if it appears it is really needed, I'll put it back it as a prereq to "run" Sage.
It's conceivable that libgc-devel is, but I think that #9617 fixed that.


---

Comment by jpflori created at 2013-01-15 20:33:43

Replying to [comment:111 kcrisman]:

> > I removed them because I was able to build and run Sage without installing them;
> My point was that you didn't add the two tickets here, without which assuredly patch would not have worked, which is used a lot!  I added them to the list above, as you can check.
Good point.
> 
> But `file` is in your list in comment:109, so I'm not sure why you removed it from the list.  Did it install with something else automatically?
Oops, I was not careful.
But indeed I did not explicitely add it, so either it was there with the basic Cygwin install, or it was pulled by something else, I'll tend to say it's the former solution as every time I installed something I had a quick look at what was pulled, but I might have missed it as well...


---

Comment by jdemeyer created at 2013-01-15 22:02:05

Replying to [comment:101 kcrisman]:
> I assume there isn't a ticket yet :)
Not yet.  I just noticed this Cygwin-specific stuff when working on #13921 and wondered whether it could be removed.  Apparently yes.


---

Comment by jpflori created at 2013-01-16 08:26:56

I ran ptest over the night and the result is not bad at all, especially that I did not include all the fixes we have (lcalc, rpy2 ar least), some of them are time outs (potentially just because Cygwin is sloooooooooooow), some of them passed when reran (e.g. the maxima.py one) and some of them are still the PARI lacking memory (cos I cannot devise how to convince Cygwin to get more than 500000000 bytes).

The result is at http://boxen.math.washington.edu/home/jpflori/ptest-5.6.rc0-cygwin.log

I've got a previous one at http://boxen.math.washington.edu/home/jpflori/ptest-5.5.rc0-cygwin.log which is not that bad as well.


---

Comment by jpflori created at 2013-01-16 12:45:06

Not really sure anymore about the libncurses-devel dependency as I'm rebuilding singular on top of my 5.6.rc0 after removing libncurses-devel and it does not complain (yet).


---

Comment by jpflori created at 2013-01-30 17:16:09

New ptest log for 5.7.beta1 at
http://boxen.math.washington.edu/home/jpflori/ptest-5.7.beta1-cygwin.log

The failing tests are:

```
The following tests failed:

	sage -t  -force_lib devel/sagenb-main/sagenb/misc/misc.py # Exception from doctest framework
	sage -t  -force_lib devel/sage/sage/functions/other.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/geometry/lattice_polytope.py # 96 doctests failed
	sage -t  -force_lib devel/sage/sage/graphs/genus.pyx # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/gsl/ode.pyx # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/libs/lcalc/lcalc_Lfunction.pyx # 69 doctests failed
	sage -t  -force_lib devel/sage/sage/libs/pari/gen.pyx # 4 doctests failed
	sage -t  -force_lib devel/sage/sage/misc/cython.py # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/misc/getusage.py # 4 doctests failed
	sage -t  -force_lib devel/sage/sage/misc/inline_fortran.py # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/misc/sageinspect.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/plot/graphics.py # Time out
	sage -t  -force_lib devel/sage/sage/plot/plot.py # Time out
	sage -t  -force_lib devel/sage/sage/plot/plot3d/implicit_plot3d.py # Time out
	sage -t  -force_lib devel/sage/sage/plot/plot3d/plot3d.py # Time out
	sage -t  -force_lib devel/sage/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py # 13 doctests failed
	sage -t  -force_lib devel/sage/sage/rings/arith.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/rings/tests.py # 4 doctests failed
	sage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # Time out
	sage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/heegner.py # Time out
	sage -t  -force_lib devel/sage/sage/schemes/toric/fano_variety.py # 12 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/expression.pyx # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/tests/cmdline.py # Time out
----------------------------------------------------------------------
```


Some were expected:
* sage/libs/lcalc/lcalc_Lfunction.pyx with fix at #13351
* sage/geometry/lattice_polytope.py with fix at #13960
* sage/schemes/toric/fano_variety.py is #13960 as well
* sage/misc/getusage.py which is #9170
* sage/graphs/genus.pyx which is in fact #9170
* sage/libs/pari/gen.pyx which is also #9170
* sage/rings/tests.py as well #9170
* sage/quadratic_forms/quadratic_form__ternary_Tornaria.py which is hopefully the same pari stack problem as #9176
Some are trivial:
* sage/functions/other.py which is numerical noise
* sage/rings/arith.py as well
* sage/symbolic/expression.pyx as well
Some look more serious:
* sage/misc/cython.py but that might just be a dynamic library extension problem
* sage/misc/inline_fortran.py which does not find gfortran?!
* sage/misc/sageinspect.py -> fork errors... maybe a rebase could fix that
* sage/gsl/ode.pyx

And the other are timeouts (for now).


But the aim of this ticket is to build Sage, so I guess we can say we are quite finished with that :)
And #13841 which aims at starting Sage is as well :)


---

Comment by jpflori created at 2013-01-30 17:16:09

Changing status from new to needs_review.


---

Comment by jpflori created at 2013-01-30 17:20:34

FYI a rebase fixed the sage/misc/sageinspect.py failure.


---

Comment by jpflori created at 2013-01-30 17:52:35

Replying to [comment:116 jpflori]:
> New ptest log for 5.7.beta1 at
> http://boxen.math.washington.edu/home/jpflori/ptest-5.7.beta1-cygwin.log
>
> Some were expected:
> * sage/libs/lcalc/lcalc_Lfunction.pyx with fix at #13351
Fixed by #13351 indeed.
> * sage/geometry/lattice_polytope.py with fix at #13960
> * sage/schemes/toric/fano_variety.py is #13960 as well
Both fixed by #13960 indeed.
> * sage/misc/getusage.py which is #9170
> * sage/graphs/genus.pyx which is in fact #9170
> * sage/libs/pari/gen.pyx which is also #9170
> * sage/rings/tests.py as well #9170
All fixed by #9170 indeed.
> * sage/quadratic_forms/quadratic_form__ternary_Tornaria.py which is hopefully the same pari stack problem as #9176
Fixed after increasing the max cygwin heap size of python.exe using peflags ("peflags --cygwin-heap=600 local/bin/python.exe").
> Some are trivial:
> * sage/functions/other.py which is numerical noise
> * sage/rings/arith.py as well
> * sage/symbolic/expression.pyx as well
> Some look more serious:
> * sage/misc/cython.py but that might just be a dynamic library extension problem
> * sage/misc/inline_fortran.py which does not find gfortran?!
> * sage/misc/sageinspect.py -> fork errors... maybe a rebase could fix that
> * sage/gsl/ode.pyx
> 
> And the other are timeouts (for now).
> 
> 
> But the aim of this ticket is to build Sage, so I guess we can say we are quite finished with that :)
> And #13841 which aims at starting Sage is as well :)


---

Comment by jpflori created at 2013-01-30 17:54:16

Replying to [comment:118 jpflori]:
> > Some are trivial:
> > * sage/functions/other.py which is numerical noise
> > * sage/rings/arith.py as well
> > * sage/symbolic/expression.pyx as well
See https://groups.google.com/d/topic/sage-devel/QACdziLhniU/discussion which looks related.


---

Comment by kcrisman created at 2013-01-30 17:58:45

> But the aim of this ticket is to build Sage, so I guess we can say we are quite finished with that :)
> And #13841 which aims at starting Sage is as well :) 

Awesome!  But we do need something in prereq or configure or SOMEWHERE that ensures that these things still will stay the case.  So we can't close it yet.


---

Comment by jpflori created at 2013-01-30 18:46:39

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2013-01-30 18:46:39

After increasing SAGE_TIMEOUT, the following tests passed:
* sage/plot/graphics.py
* sage/plot/plot3d/implicit_plot3d.py
* sage/plot/plot3d/plot3d.py
* sage/schemes/elliptic_curves/heegner.py

The following still fail:
* sage/plot/plot.py problems with GSL like sage/gsl/ode.pyx (GSL handler blabla)
* sage/schemes/elliptic_curves/ell_rational_field.py fork erros it seems when starting external programs
* sage/tests/cmdline.py seemingly fork errors (calling os.fork() might not be a great idea)

And there is the one I omitted before:
* sagenb/misc/misc.py # Exception from doctest framework
The exception bit seems to be from an error I had with previous release as well about an alarm set to 1 second and is random.
I guess Cygwin is just to slow for such a timeout.
After a few tries I indeed get a bunch only one real error on the test with 'print "ignore this' because of a (Python) RuntimeError about "no available port" from the find_next_available_port function.


---

Comment by kcrisman created at 2013-01-30 19:02:19

> After increasing SAGE_TIMEOUT, the following tests passed:

Maybe it's time to open a new ticket to get Cygwin to pass all tests (at least on 64-bit)?


---

Comment by jpflori created at 2013-01-30 20:03:21

Yep, I guess so.
Although I'm not convinced we will ever be able to deal with the one involving horrible fork errors.


---

Comment by kcrisman created at 2013-01-31 02:09:28

Well, it was partly rhetorical!  Maybe we could repurpose #13841 to have it pass most reasonable tests.

Sorry I can't help at all right now other than morally - zero time and of course crazy fork/BLODA problems.  I will try to ask my computer folks for a Win 7 box to try things on when things calm down.


---

Comment by jdemeyer created at 2013-01-31 13:16:34

Replying to [comment:106 kcrisman]:
> It built and installed fine, with pretty much the same exact error in the tests, and factored the huge number fine in the console.  If all else is well, these spkgs can be included.  Well, I guess one of them is :)

I have to update PARI anyway for #13054 and will remove all Cygwin-specific code from `spkg-install`.


---

Comment by kcrisman created at 2013-01-31 14:52:38

> > It built and installed fine, with pretty much the same exact error in the tests, and factored the huge number fine in the console.  If all else is well, these spkgs can be included.  Well, I guess one of them is :)
> 
> I have to update PARI anyway for #13054 and will remove all Cygwin-specific code from `spkg-install`.

JP, did you have any problems with this?  I guess you can just try the spkg from #13054, which does what Jeroen says.


---

Comment by jpflori created at 2013-02-04 21:06:07

FYI, although it might be unrelated, the GSL failing tests passed after I installed a shared version of the lib and rebuilt the related Sage library files.


---

Comment by jpflori created at 2013-02-05 09:55:28

I've started building 5.7.beta2 plus some patches on a notebook running a 32 bits Windows 7 install.


---

Comment by jpflori created at 2013-02-06 14:23:09

R was upgraded at #14008 and merged in sage-5.7.beta2 and now needs math functions for long doubles, more precisely logl, which is not provided by Cygwin's libm.

Not sure if its possible to disable the use of this function in R, otherwise I guess we're back to installing Cephes on Cygwin.


---

Comment by jpflori created at 2013-02-06 14:36:15

In the devel version there is support to build without long double, see
http://stat.ethz.ch/R-manual/R-devel/doc/html/NEWS.html
but that does not seem to be the case in 2.15.2.


---

Comment by dimpase created at 2013-02-06 14:43:30

Replying to [comment:129 jpflori]:
> R was upgraded at #14008 and merged in sage-5.7.beta2 and now needs math functions for long doubles, more precisely logl, which is not provided by Cygwin's libm.
> 
> Not sure if its possible to disable the use of this function in R, otherwise I guess we're back to installing Cephes on Cygwin.
Yes, that's where my Cygwin install of 5.7.beta2 got stuck, too.

as a temporary plug, we can do something like

```
#define logl log
```

in the right place.
Cygwin has a weird long double size - 12 bytes, so in that sense it's not as huge loss of precision as for sane platforms.


---

Comment by jpflori created at 2013-02-06 14:47:17

I'm seeing if we cannot just backport the support for --disable-long-double.
That seems difficult but who knows.


---

Comment by jpflori created at 2013-02-06 17:17:48

Replying to [comment:131 dimpase]:
> Replying to [comment:129 jpflori]:
> > R was upgraded at #14008 and merged in sage-5.7.beta2 and now needs math functions for long doubles, more precisely logl, which is not provided by Cygwin's libm.
> > 
> > Not sure if its possible to disable the use of this function in R, otherwise I guess we're back to installing Cephes on Cygwin.
> Yes, that's where my Cygwin install of 5.7.beta2 got stuck, too.
> 
> as a temporary plug, we can do something like
> {{{
> #define logl log
> }}}
> in the right place.
FYI this is exactly what R (not using the same mechanism) does when --disable-long-double.
> Cygwin has a weird long double size - 12 bytes, so in that sense it's not as huge loss of precision as for sane platforms.


---

Comment by jpflori created at 2013-02-06 17:34:52

But it also completely disable long double, which is a little unfortunate, so I guess we'll have to provide a custom patch to just disable the use of logl.

It later lots of such functions get used we could consider falling back to --disable-long-double or using Cephes.

Any thoughts?


---

Comment by kcrisman created at 2013-02-06 17:58:19

Anything that allows us to get this Cygwin show on the road is best, assuming it is not about "core" functionality.  I think it's okay to have the custom patch as long as it doesn't break R being used at all; we shouldn't be relying on R for multi precision stuff anyway.  Add that patch just for Cygwin.


---

Comment by jpflori created at 2013-02-07 10:09:26

See #14078 for the R issue.

By the way all Sage and its doc built fine on my 32 bits Windows 7.


---

Comment by jpflori created at 2013-02-08 12:32:55

And result of "make ptest" is

```
The following tests failed:

	sage -t  -force_lib devel/sagenb-main/sagenb/misc/misc.py # Exception from doctest framework
	sage -t  -force_lib devel/sage/sage/combinat/partition_algebra.py # Time out
	sage -t  -force_lib devel/sage/sage/combinat/skew_tableau.py # Time out
	sage -t  -force_lib devel/sage/sage/combinat/crystals/kirillov_reshetikhin.py # Time out
	sage -t  -force_lib devel/sage/sage/functions/other.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/geometry/lattice_polytope.py # Time out
	sage -t  -force_lib devel/sage/sage/groups/perm_gps/cubegroup.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/interfaces/sage0.py # Time out
	sage -t  -force_lib devel/sage/sage/libs/gap/test_long.py # Time out
	sage -t  -force_lib devel/sage/sage/misc/cython.py # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/misc/inline_fortran.py # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/misc/temporary_file.py # 5 doctests failed
	sage -t  -force_lib devel/sage/sage/plot/graphics.py # Time out
	sage -t  -force_lib devel/sage/sage/plot/plot.py # Time out
	sage -t  -force_lib devel/sage/sage/plot/plot3d/implicit_plot3d.py # Time out
	sage -t  -force_lib devel/sage/sage/plot/plot3d/plot3d.py # Time out
	sage -t  -force_lib devel/sage/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py # 13 doctests failed
	sage -t  -force_lib devel/sage/sage/rings/arith.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/sandpiles/sandpile.py # Time out
	sage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/ell_number_field.py # Time out
	sage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # Time out
	sage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/heegner.py # Time out
	sage -t  -force_lib devel/sage/sage/symbolic/expression.pyx # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/tests/cmdline.py # Time out
----------------------------------------------------------------------
Total time for all tests: 92015.4 seconds
```



---

Comment by jpflori created at 2013-02-08 12:37:59

Log is at http://boxen.math.washington.edu/home/jpflori/ptest-5.7.beta2-cygwin-w7-32.log

Apart from time outs and errors similar to the one on my 64 bits W7, we got:
* cubegroup.py, strange error about string out of range,
* temporary_file.py which looks like a time out as well.


---

Comment by jpflori created at 2013-02-08 13:31:06

Increasing the timeout limit, let all tests which teimed out pass except for:
* heegner.py because of the limited size of the PARI stack,
* cmdline.py which fails like temporary_file.py because of "timeout in test_executable()", note there were no fork errors!


---

Comment by jpflori created at 2013-02-08 13:34:30

Also note that sage/schemes/elliptic_curves/ell_rational_field.py did not fail with fork errors as on my 64bits W7.


---

Comment by jdemeyer created at 2013-02-08 13:38:25

Replying to [comment:139 jpflori]:
> heegner.py because of the limited size of the PARI stack
It's known that this test simply needs a lot of RAM, so perhaps your machine doesn't have enough memory available. What's the error message and how much memory do you have?


---

Comment by jpflori created at 2013-02-08 13:43:45

Replying to [comment:141 jdemeyer]:
> Replying to [comment:139 jpflori]:
> > heegner.py because of the limited size of the PARI stack
> It's known that this test simply needs a lot of RAM, so perhaps your machine doesn't have enough memory available. What's the error message and how much memory do you have?
I'm aware of that, I was just reporting the results of a straight test.
The problem on Cygwin is that the maximal virtual memomy available is limited to something quite low by default, I'd say about 512MB.
In particular it prevents the PARI stack to grow above (a little less than) this limit, even if you have 1 billion GB of RAM available.
The solution is to modify this limit by hand for the python.exe file using the peflags executable, see some comments on #9176.


---

Comment by jdemeyer created at 2013-02-08 13:50:55

OK fair enough, you obviously already thought about this :-)


---

Comment by jpflori created at 2013-02-08 14:21:58

After increasing the timeout value in sage/tests/cmdline.py:test_executable():
* temporary_file.py passes,
* one doctest fails in cmdline.py, the one at line 376 which return -6 instead of 0.


---

Comment by jpflori created at 2013-02-08 14:41:32

FYI, quadratic_form__ternary_Tornaria.py and heegner.py pass their doctests after peflagging python.exe with cygwin-heap=600


---

Comment by jpflori created at 2013-02-08 15:24:32

And going through the "alarm set to 1 second" hassle, devel/sagenb-main/sagenb/misc/misc.py passed its doctests contrary to my 64bits W7 install (no port available blah).


---

Comment by jpflori created at 2013-02-12 21:18:18

I guess that with #14033, #11696 and #13351 Sage should build, run and pass tests quite nicely.

Now let's take care of adding some doc and modifying prereqs or whatever.


---

Comment by jpflori created at 2013-02-12 21:20:59

Replying to [comment:139 jpflori]:
> * cmdline.py which fails like temporary_file.py because of "timeout in test_executable()", note there were no fork errors!
Question for Jeroen: how would you deal with such problems? and even more with the one with the alarm set to 1 second getting triggered when one tries to launch the notebook? would setting the default timeoutsvelue to None and then setting then to something sensible in the function code depending on uname seem ok?


---

Comment by dimpase created at 2013-02-13 04:43:43

few things about Cygwin rebase/rebaseall.
 
  * we should rebase .so files, too;
  * `rebase` has a new handy -O switch, which means rebase (new) things, but do not touch the system dlls. So instead of rebaseall, assuming one installs Sage on a system without previous versions of Sage installed, one can do, at the Cygwin shell (no need to kill all the Cygwin processes, as is the case for rebaseall):

```
$ cd $SAGE_ROOT
$ find . -name *.dll >/tmp/list_of_files
$ find . -name *.so >>/tmp/list_of_files
$ rebase -O -T /tmp/list_of_files
```

  * previous versions of Sage clog up the limited static dll address space maintained by Cygwin in `/etc/rebase*` databases. I recommend to wipe them out before installing the new version of Sage; i.e. remove Sage installation(s) and `/etc/rebase*` and run rebaseall as usual, in `ash` or `dash`.


---

Comment by jpflori created at 2013-02-13 12:50:13

Replying to [comment:149 dimpase]:
> few things about Cygwin rebase/rebaseall.
>  
>   * we should rebase .so files, too;
I think you should go even further and only have *.dll files.
>   * `rebase` has a new handy -O switch, which means rebase (new) things, but do not touch the system dlls. So instead of rebaseall, assuming one installs Sage on a system without previous versions of Sage installed, one can do, at the Cygwin shell (no need to kill all the Cygwin processes, as is the case for rebaseall):
> {{{
> $ cd $SAGE_ROOT
> $ find . -name *.dll >/tmp/list_of_files
> $ find . -name *.so >>/tmp/list_of_files
> $ rebase -O -T /tmp/list_of_files
> }}}
Good to know, thanks for the hint!
I finally got rid of the BLODA which memleak on my 64 bis W7 (that was the Lenovo FastBoot thing, not even sure what it does, except keeping 20K of memory in page table for every app ever launched, Cygwin or not...) and might find this really useful.
>   * previous versions of Sage clog up the limited static dll address space maintained by Cygwin in `/etc/rebase*` databases. I recommend to wipe them out before installing the new version of Sage; i.e. remove Sage installation(s) and `/etc/rebase*` and run rebaseall as usual, in `ash` or `dash`.
Yup, that's a good idea.

Could you provide more info, or pointers, on why Cygwin running on a native 32 bits system would have more address space available than one running under wow64 on 64 bits, and so less affected by fork errors, one as I seem to remember you evoked that at some point here?
I would be interested.


---

Comment by jdemeyer created at 2013-02-13 13:08:43

Replying to [comment:148 jpflori]:
> Replying to [comment:139 jpflori]:
> > * cmdline.py which fails like temporary_file.py because of "timeout in test_executable()", note there were no fork errors!
> Question for Jeroen: how would you deal with such problems?
I don't mind if you increase the timeout unconditionally in `test_executable()`. Would 100 seconds (now it is 50) be sufficient?

> and even more with the one with the alarm set to 1 second getting triggered when one tries to launch the notebook?
Increase the alarm time.

I don't like the `find_next_available_port()` function anyway, it's un-Pythonic (the Pythonic thing to do would be to try to `bind()` to a port and use a next port if that fails) and therefore prone to race conditions.


---

Comment by dimpase created at 2013-02-13 13:28:37

Replying to [comment:150 jpflori]:
> Could you provide more info, or pointers, on why Cygwin running on a native 32 bits system would have more address space available than one running under wow64 on 64 bits, and so less affected by fork errors, one as I seem to remember you evoked that at some point here?
> I would be interested.

no, my conviction was that it's not possible to have a full install of Cygwin and a Sage on a 32-bit system, they just don't fit in that addess space - which is bigger on wow64 on 64 bits. You are welcome to prove me wrong. Perhaps it was some BLODA on that system I no longer have, anyway.


---

Comment by jpflori created at 2013-02-13 13:33:48

Replying to [comment:152 dimpase]:
> Replying to [comment:150 jpflori]:
> > Could you provide more info, or pointers, on why Cygwin running on a native 32 bits system would have more address space available than one running under wow64 on 64 bits, and so less affected by fork errors, one as I seem to remember you evoked that at some point here?
> > I would be interested.
> 
> no, my conviction was that it's not possible to have a full install of Cygwin and a Sage on a 32-bit system, they just don't fit in that addess space - which is bigger on wow64 on 64 bits. You are welcome to prove me wrong. Perhaps it was some BLODA on that system I no longer have, anyway.
Hum, I got less problems with my 32bits W7 (although it was slower and had less cores) than with my 64bits W7.
Indeed, I got fork errors in the end on the 64 bits install and not on the 32 bits install.


---

Comment by kcrisman created at 2013-02-13 15:46:58

> > Could you provide more info, or pointers, on why Cygwin running on a native 32 bits system would have more address space available than one running under wow64 on 64 bits, and so less affected by fork errors, one as I seem to remember you evoked that at some point here?
> > I would be interested.
> 
> no, my conviction was that it's not possible to have a full install of Cygwin and a Sage on a 32-bit system, they just don't fit in that addess space - which is bigger on wow64 on 64 bits. You are welcome to prove me wrong. Perhaps it was some BLODA on that system I no longer have, anyway.

But that actually makes a lot of sense for the problems I've had.  I haven't had any time lately but perhaps next week I will completely uninstall and reinstall Cygwin on my XP box and see what happens.

Also, love the idea to have the `rebase` instead of `rebaseall`.  Could the relevant ticket about the Cygwin rebase script (#14031) be updated with that too?


---

Comment by jpflori created at 2013-02-20 14:56:05

Ok, I think we now only need #13351 to get Sage to quite completely build, start, correctly work and pass (most of) its doctests.

We should open other tickets to add doc about usage of peflags, use of the rebasing script (#14031), modifying prereqs and other cosmetic things.

Then we should deal with the failing doctests mentioned above, most of them are "quite" easy or we can just document why they are expected to fail (e.g., you have to peflags python.exe, or Cygwin is just too slow, so you have to increase SAGE_TIMEOUT, or you have to install procps to have top).


---

Comment by jpflori created at 2013-02-20 14:56:42

We should also deal with the few .so files remaining.


---

Comment by jpflori created at 2013-02-25 14:22:21

See #14179 for the problematic default timeout values.


---

Comment by jpflori created at 2013-03-01 10:35:09

I've opened #14207 for documenting usage of peflags and leverage max heap memory issues.


---

Comment by jpflori created at 2013-03-01 10:37:29

And #14208 for *.so files, this could be a metaticket if there is a lot of work.


---

Comment by kcrisman created at 2013-03-06 01:55:56

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2013-03-06 01:55:56

Replying to [comment:155 jpflori]:
> Ok, I think we now only need #13351 to get Sage to quite completely build, start, correctly work and pass (most of) its doctests.
So ... once that is merged, is this ticket done?
> We should open other tickets to add doc about usage of peflags, use of the rebasing script (#14031), modifying prereqs and other cosmetic things.
So is there really no prereq modification necessary here?  (Or, as Volker says, some other script somewhere to check this?) All along, from when William opened this ticket, the assumption was that we would put _some_ checking in that a given Cygwin had the proper prereqs to function.  From [the wiki](http://trac.sagemath.org/sage_trac/wiki/CygwinPort): 

```
Also installed the lapack packages, the gcc, g++ and gfortran ones, m4, make, binutils, perl
```

We do ask for gcc, m4, make, and perl ahead of time.  Does Sage already throw an error at the start if the lapack stuff isn't there?  What about binutils - is that equivalent to a "standard" dependency?

The top/procps/file thing is presumably separate - we don't need that to build, just test, correct?  Also there was that "custom GSL" remark, but perhaps that wasn't an issue.

One reason I am a little scared about this is the tendency of Sage to creep beyond the latest efforts here.  So I want to hesitate to close this until we are really sure we are "state-of-the-art".  I wish we could acquire a Cygwin buildbot.

Anyway, all that to say that I should have a little time for this in the next week and a half to help test some of the many many fixes you have contributed - amazing stuff.  Thank you to Dima so much for picking up a lot of my slack on this the past few months.


---

Comment by jdemeyer created at 2013-03-06 07:40:31

Replying to [comment:160 kcrisman]:
> We do ask for gcc, m4, make, and perl ahead of time.  Does Sage already throw an error at the start if the lapack stuff isn't there?  What about binutils - is that equivalent to a "standard" dependency?
A C compiler, `m4`, `make`, `perl` and `binutils` are always checked by prereq. Lapack surely not, since it's included with Sage.


---

Comment by lftabera created at 2013-03-06 14:35:22

This is amazing. Thanks to all the people involved. I have checked that sage-5.8.beta2 compiles on a windows vista machine, 32 bits OS. I had to rebase once while compiling and another after compiling for booting sage without errors.


---

Comment by jpflori created at 2013-03-06 15:16:54

Replying to [comment:161 jdemeyer]:
> Replying to [comment:160 kcrisman]:
> > We do ask for gcc, m4, make, and perl ahead of time.  Does Sage already throw an error at the start if the lapack stuff isn't there?  What about binutils - is that equivalent to a "standard" dependency?
> A C compiler, `m4`, `make`, `perl` and `binutils` are always checked by prereq. Lapack surely not, since it's included with Sage.
The current ATLAS spkg exits if it does not finds a system wide ATLAS or LAPACK, don't remember, and asks you to install the corresponding Cygwin packages (lapack-bin, lapack-devel IIRC, or stg like that).

Nonetheless, I'm quite convinced we can build the new ATLAS spkg from #10508 quite easily on Cygwin.
I've had some trouble with shared library and the 3.8 ATLAS spkg, with memleaks on top of that.
Bu now I've removed the memleaks culprit so I could try again to vuild ATLAS 3.10.

Unfortunately that's not my top priority, and on top of that I'm very happy with installing a system wide ATLAS.


---

Comment by jpflori created at 2013-03-06 15:18:27

For the record, note that GCC 4.6.3 cannot compile ECL on Cygwin.


---

Comment by jpflori created at 2013-03-06 15:19:25

Replying to [comment:162 lftabera]:
> This is amazing. Thanks to all the people involved. I have checked that sage-5.8.beta2 compiles on a windows vista machine, 32 bits OS. I had to rebase once while compiling and another after compiling for booting sage without errors.
Great news!


---

Comment by jdemeyer created at 2013-03-06 15:35:57

Replying to [comment:164 jpflori]:
> For the record, note that GCC 4.6.3 cannot compile ECL on Cygwin.
Is there a ticket for this?  What goes wrong?


---

Comment by kcrisman created at 2013-03-06 15:46:30

> The current ATLAS spkg exits if it does not finds a system wide ATLAS or LAPACK, don't remember, and asks you to install the corresponding Cygwin packages (lapack-bin, lapack-devel IIRC, or stg like that).

```
# On Cygwin we simply require that the system-wide lapack is installed.
# This includes BLAS and is enough to build the rest of Sage.
if conf['CYGWIN?']:
    lib = '/usr/lib/libblas.dll.a'
    if not os.path.exists(lib):
        print '*'*75
        print 'On Cygwin you must install the standard LAPACK Cygwin package'
        print 'via the Cygwin setup.exe program in the "Math" category.'
        print '*'*75 
        sys.exit(1)
    cp(lib, os.path.join(conf['SAGE_LOCAL'], 'lib'))
    sys.exit(0)
```

I think this should be updated, perhaps at #10508, to be VERY explicit about which packages to install, and so we are not _quite_ ready to close this ticket.  Also, we might want to make sure that this dll.a is really all that we need to check for to not run into trouble.  That said, the default should be to not install ATLAS, but one should be able to force it with an appropriate environment variable or something - I thought #10508 dealt with that, but maybe not?  With 334 comments and counting, wow...


---

Comment by jpflori created at 2013-03-06 15:48:43

Replying to [comment:166 jdemeyer]:
> Replying to [comment:164 jpflori]:
> > For the record, note that GCC 4.6.3 cannot compile ECL on Cygwin.
> Is there a ticket for this?  What goes wrong?
No tickets here.

It goes ok with Cygwin 4.5.3 gcc or Sage's 4.7.2.

For more details see:
http://www.mail-archive.com/ecls-list`@`lists.sourceforge.net/msg02368.html

Upstream bug report:
http://gcc.gnu.org/bugzilla/show_bug.cgi?id=52061


---

Comment by jpflori created at 2013-03-06 15:49:40

Replying to [comment:167 kcrisman]:
> > The current ATLAS spkg exits if it does not finds a system wide ATLAS or LAPACK, don't remember, and asks you to install the corresponding Cygwin packages (lapack-bin, lapack-devel IIRC, or stg like that).
> {{{
> # On Cygwin we simply require that the system-wide lapack is installed.
> # This includes BLAS and is enough to build the rest of Sage.
> if conf['CYGWIN?']:
>     lib = '/usr/lib/libblas.dll.a'
>     if not os.path.exists(lib):
>         print '*'*75
>         print 'On Cygwin you must install the standard LAPACK Cygwin package'
>         print 'via the Cygwin setup.exe program in the "Math" category.'
>         print '*'*75 
>         sys.exit(1)
>     cp(lib, os.path.join(conf['SAGE_LOCAL'], 'lib'))
>     sys.exit(0)
> }}}
> I think this should be updated, perhaps at #10508, to be VERY explicit about which packages to install, and so we are not _quite_ ready to close this ticket.  Also, we might want to make sure that this dll.a is really all that we need to check for to not run into trouble.  That said, the default should be to not install ATLAS, but one should be able to force it with an appropriate environment variable or something - I thought #10508 dealt with that, but maybe not?  With 334 comments and counting, wow...
The latest spkg from #10508 let you "force" ATLAS build by setting SAGE_ATLAS_ARCH.


---

Comment by jdemeyer created at 2013-03-06 15:55:00

Replying to [comment:168 jpflori]:
> It goes ok with Cygwin 4.5.3 gcc or Sage's 4.7.2.
> 
> For more details see:
> http://www.mail-archive.com/ecls-list`@`lists.sourceforge.net/msg02368.html
> 
> Upstream bug report:
> http://gcc.gnu.org/bugzilla/show_bug.cgi?id=52061
Thanks for the pointers, too bad upstream doesn't care.


---

Comment by kcrisman created at 2013-03-07 04:46:29

Currently uninstalled and now reinstalling Cygwin on my XP box.  Let's hope :)

By the way, should closing this ticket also require removing the `SAGE_PORT=yes` necessity for Cygwin?  Just a thought.


---

Comment by jdemeyer created at 2013-03-07 07:37:57

Replying to [comment:171 kcrisman]:
> By the way, should closing this ticket also require removing the `SAGE_PORT=yes` necessity for Cygwin?
Indeed, maybe we should repurpose this ticket to do just that.

We also need to change `spkg/install` never to install Sage's GCC on Cygwin, since it doesn't work for ECL.


---

Comment by jpflori created at 2013-03-07 08:11:40

Replying to [comment:172 jdemeyer]:
> Replying to [comment:171 kcrisman]:
> > By the way, should closing this ticket also require removing the `SAGE_PORT=yes` necessity for Cygwin?
> Indeed, maybe we should repurpose this ticket to do just that.
> 
> We also need to change `spkg/install` never to install Sage's GCC on Cygwin, since it doesn't work for ECL.
Also note that Sage's GCC 4.7.2 is fine so we could check that all Cygwin gcc, g++ and gfortran 4.5.3 are installed or suggest using the Sage's optional 4.7.2 spkg.


---

Comment by jdemeyer created at 2013-03-07 09:27:51

Or upgrade GCC-in-Sage to version 4.7.2, I wouldn't have an objection with that.


---

Comment by leif created at 2013-03-07 13:16:39

Replying to [comment:174 jdemeyer]:
> Or upgrade GCC-in-Sage to version 4.7.2, I wouldn't have an objection with that.

Yep.  Any reason we shouldn't [yet]?


---

Comment by kcrisman created at 2013-03-07 14:19:14

Latest XP build report:

Weirdly, I just tried a brand-new Cygwin install with the minimal prereqs that JP has been talking about, and got a very strange error about cygmpfr-4.dll cannot open shared object file (as well as that I didn't have Gnu cc and that cc couldn't make executables.  Installing the mpfr-4 package from Cygwin seems to have allowed compilation to begin, but that mpfr came with a SLEW of other packages I didn't really want.  In this case, it seems that even our gcc package would not have compiled, since Sage thought that the gcc4 on Cygwin was defective somehow.  

Assuming this behaves properly over the next 48 hours or so, I'll yet again uninstall Cygwin and see what happens with a new one.  That said, IF we can build gcc-4.7 with the gcc3 that is preinstalled on Cygwin, maybe that would be a reason for the 4.7 standard version.


---

Comment by jpflori created at 2013-03-07 14:27:49

Replying to [comment:176 kcrisman]:
> Latest XP build report:
> 
> Weirdly, I just tried a brand-new Cygwin install with the minimal prereqs that JP has been talking about, and got a very strange error about cygmpfr-4.dll cannot open shared object file (as well as that I didn't have Gnu cc and that cc couldn't make executables.  Installing the mpfr-4 package from Cygwin seems to have allowed compilation to begin, but that mpfr came with a SLEW of other packages I didn't really want.  In this case, it seems that even our gcc package would not have compiled, since Sage thought that the gcc4 on Cygwin was defective somehow.  
> 
Strange, Ive always used the gcc4 package (more precisely, the latest version available for gcc4-core) and got no problems either with that package only to builg Sage's GCC 4.6.3 or 4.7.2, or together with the corresponding gcc4-g++ and gcc4-gfortran to builg Sage directly.
I think I never ever tried the gcc3 packages.
I've nevere (intentionally) installed gmp, mpfr not mpc neither.

I'll put my hand on a XP box and will give it a shot.
That may be in a week or two only though.
> Assuming this behaves properly over the next 48 hours or so, I'll yet again uninstall Cygwin and see what happens with a new one.  That said, IF we can build gcc-4.7 with the gcc3 that is preinstalled on Cygwin, maybe that would be a reason for the 4.7 standard version.


---

Comment by leif created at 2013-03-07 14:36:36

Replying to [comment:176 kcrisman]:
> Latest XP build report:
> 
> Weirdly, I just tried a brand-new Cygwin install with the minimal prereqs that JP has been talking about, and got a very strange error about cygmpfr-4.dll cannot open shared object file (as well as that I didn't have Gnu cc and that cc couldn't make executables.  Installing the mpfr-4 package from Cygwin seems to have allowed compilation to begin, but that mpfr came with a SLEW of other packages I didn't really want.  In this case, it seems that even our gcc package would not have compiled, since Sage thought that the gcc4 on Cygwin was defective somehow.

GCC 4.x (in contrast to 3.x) requires GMP, MPFR (and since 4.5 IIRC also MPC), so these packages should have been pulled in by Cygwin if/when you installed the GCC4 package.

But didn't you say "GCC3" was the default?


---

Comment by jpflori created at 2013-03-07 14:43:15

Replying to [comment:178 leif]:
> Replying to [comment:176 kcrisman]:
> > Latest XP build report:
> > 
> > Weirdly, I just tried a brand-new Cygwin install with the minimal prereqs that JP has been talking about, and got a very strange error about cygmpfr-4.dll cannot open shared object file (as well as that I didn't have Gnu cc and that cc couldn't make executables.  Installing the mpfr-4 package from Cygwin seems to have allowed compilation to begin, but that mpfr came with a SLEW of other packages I didn't really want.  In this case, it seems that even our gcc package would not have compiled, since Sage thought that the gcc4 on Cygwin was defective somehow.
> 
> GCC 4.x (in contrast to 3.x) requires GMP, MPFR (and since 4.5 IIRC also MPC), so these packages should have been pulled in by Cygwin if/when you installed the GCC4 package.
> 
> But didn't you say "GCC3" was the default?
Don't know what the official Cygwin guidelines are, but you may say its the default because it what the "gcc" package points to.

If you want GCC 4.x (which ships 4.5.x currently), you have to choose the "gcc4" packages (moreprecisely the "gcc4-core" one if you want the C compiler, and it should indeed pull mpfr and mpc automagically unless you prevent setup.exe from doing it, see a list of package I had installed and with which I got a mostly working Sage install at http://trac.sagemath.org/sage_trac/wiki/CygwinPort#TestingSage5.6.rc0on64bitsWindows7 )


---

Comment by jdemeyer created at 2013-03-07 14:44:55

Replying to [comment:176 kcrisman]:
> IF we can build gcc-4.7 with the gcc3 that is preinstalled on Cygwin

In theory, this should work.


---

Comment by kcrisman created at 2013-03-07 19:11:14

> GCC 4.x (in contrast to 3.x) requires GMP, MPFR (and since 4.5 IIRC also MPC), so these packages should have been pulled in by Cygwin if/when you installed the GCC4 package.

See, that's just what I thought.  So I was really surprised.  Perhaps something got interrupted in the download - Windows autoupdated or something, maybe.  I'm not worried about it.

Anyway, it's well into polybori now, so that is a positive sign.


---

Comment by kcrisman created at 2013-03-08 12:25:56

I only had trouble with #13351 and fork problems during matplotlib (which even rebasing didn't solve).  I do _not_ have libncurses-devel (checked `cygcheck -c`), only libncurses 8 through w10, so I'm removing that as a dependency based on the experiences JP reports above.


---

Comment by kcrisman created at 2013-03-08 12:57:14

Another question: will #12415 make all doctesting on Cygwin hopeless, given the problems with forking?


---

Comment by kcrisman created at 2013-03-08 16:30:10

> Another question: will #12415 make all doctesting on Cygwin hopeless, given the problems with forking?
Though I should say that on my current box, it's hopeless anyway; so many tests fail with something related to rebasing or forking or an inability to start gap or pari or maxima (or, currently, the lack of matplotlib).  There are one or two actually interesting tests I observe, randomly.  Like

```
File ... exp_integral.py, line 585
sage: N(f.integrate(x,2.0,3.0))
Expected:
    0.6016...587
Got:
    0.6016...588
```

But in general it's a mess when other programs are called.


---

Comment by kcrisman created at 2013-03-12 00:44:41

> Strange, Ive always used the gcc4 package (more precisely, the latest version available for gcc4-core) and got no problems either with that package only to builg Sage's GCC 4.6.3 or 4.7.2, or together with the corresponding gcc4-g++ and gcc4-gfortran to builg Sage directly.

Okay, I'm noting that on a Win 7 box I just got my hands on (just for this week) I'm getting exactly the same error message about mpfr-4 - failure in the same place, in fact, in the very first compilation, it won't even do bzip2.  Adding the gcc (as opposed to gcc-core et al.) package doesn't help.  Adding the libmpfr-4 package solves things.  I can't explain the discrepancy to JP's experience.  I have Cygwin 1.7.17-1 - I just installed it less than a half-hour ago, so it must be up-to-date!

Also, just as a point of information, it turns out gcc (3) does not install by default, I don't have it now.


---

Comment by kcrisman created at 2013-03-12 02:39:03

More fun on Win 7, two threads:
 * zn_poly only will build properly with one thread, otherwise the tuning goes too slow or something.
 * Got some probably rebase need in polybori.
 * Did I do something wrong in that lapack is really built?  Atlas just gets copied from /usr/lib/, but I had thought that lapack would just copy from the lapack Cygwin package.  Not important, probably just my ignorance.


---

Comment by kcrisman created at 2013-03-12 03:41:15

I get on startup (and test) a lot of 

```
Exception OverflowError: 'long int too large to convert to int' in <sage.structure.coerce_dict.TripleDictEraser object at 0xff9ad044> ignored
```

messages.  Doc did not build.  This seems also to have led to some doctest errors in sage/algebras/free_algebra.py.  Full test results tomorrow, if I can get it out.


---

Comment by dimpase created at 2013-03-12 05:54:00

Replying to [comment:187 kcrisman]:
> I get on startup (and test) a lot of 
> {{{
> Exception OverflowError: 'long int too large to convert to int' in <sage.structure.coerce_dict.TripleDictEraser object at 0xff9ad044> ignored
> }}}
> messages.  Doc did not build.  
not a surprise that docs don't get built, as you have a startup error...
Maybe Simon King can comment on this, as he's been working on this stuff a lot lately.  If you ask me, conversion of long ints to ints should not happen!


---

Comment by dimpase created at 2013-03-12 05:54:00

Changing status from needs_review to needs_info.


---

Comment by jdemeyer created at 2013-03-12 06:34:18

Replying to [comment:187 kcrisman]:
> {{{
> Exception OverflowError: 'long int too large to convert to int' in <sage.structure.coerce_dict.TripleDictEraser object at 0xff9ad044> ignored
> }}}
That is fixed by #14254.


---

Comment by kcrisman created at 2013-03-12 13:12:20

> > {{{
> > Exception OverflowError: 'long int too large to convert to int' in <sage.structure.coerce_dict.TripleDictEraser object at 0xff9ad044> ignored
> > }}}
> That is fixed by #14254.
Thanks, I'll try applying that and rerunning failed tests once they complete; as far as I can tell the only tests that failed were due to this (if one includes the tests that fail due to unbuilt doc, which as Dima points out is also due to this).

Related to this... did we ever merge a test option that reruns only the most recent failed tests?  I seem to recall discussion about this, maybe it's part of #12415, though I haven't been following that ticket.


---

Comment by SimonKing created at 2013-03-12 14:18:08

Replying to [comment:190 kcrisman]:
> Related to this... did we ever merge a test option that reruns only the most recent failed tests?  I seem to recall discussion about this, maybe it's part of #12415, though I haven't been following that ticket.

This would be useful. But since #14254 is implicitly used in every single instance of coercion (hence, _everywhere_!), I think rerunning the full test suite makes sense in this case.


---

Comment by kcrisman created at 2013-03-12 14:56:41

As it turns out, #14254 wasn't the (whole) problem.  Most of the errors were of the following ilk.

```
sage -t  devel/sage-main/sage/algebras/free_algebra.py
Exception KeyError: (The ring pointer -0x1f5282c,) in 'sage.libs.singular.ring.singular_ring_delete' ignored
Exception KeyError: (The ring pointer -0x1f52768,) in 'sage.libs.singular.ring.singular_ring_delete' ignored
Exception KeyError: (The ring pointer -0x1f526a4,) in 'sage.libs.singular.ring.singular_ring_delete' ignored
**********************************************************************
File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/algebras/free_algebra.py", line 820:
    sage: G=A.g_algebra({y*x:-x*y})
Exception raised:
    Traceback (most recent call last):
      File "/home/sagetest/sage-5.8.beta4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/sagetest/sage-5.8.beta4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/sagetest/sage-5.8.beta4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[3]>", line 1, in <module>
        G=A.g_algebra({y*x:-x*y})###line 820:
    sage: G=A.g_algebra({y*x:-x*y})
      File "/home/sagetest/sage-5.8.beta4/local/lib/python/site-packages/sage/algebras/free_algebra.py", line 872, in g_algebra
        order=order, check=check)
      File "factory.pyx", line 143, in sage.structure.factory.UniqueFactory.__call__ (sage/structure/factory.c:1119)
      File "factory.pyx", line 170, in sage.structure.factory.UniqueFactory.get_object (sage/structure/factory.c:1311)
      File "plural.pyx", line 180, in sage.rings.polynomial.plural.G_AlgFactory.create_object (sage/rings/polynomial/plural.cpp:4289)
      File "plural.pyx", line 358, in sage.rings.polynomial.plural.NCPolynomialRing_plural.__init__ (sage/rings/polynomial/plural.cpp:5351)
      File "plural.pyx", line 1471, in sage.rings.polynomial.plural.NCPolynomial_plural.__richcmp__ (sage/rings/polynomial/plural.cpp:11452)
      File "element.pyx", line 855, in sage.structure.element.Element._richcmp (sage/structure/element.c:7980)
      File "coerce.pyx", line 913, in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:8304)
      File "coerce.pyx", line 1068, in sage.structure.coerce.CoercionModel_cache_maps.coercion_maps (sage/structure/coerce.c:9855)
      File "coerce.pyx", line 1209, in sage.structure.coerce.CoercionModel_cache_maps.discover_coercion (sage/structure/coerce.c:11405)
      File "parent.pyx", line 2116, in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:14383)
      File "parent.pyx", line 2937, in sage.structure.parent._register_pair (sage/structure/parent.c:21545)
      File "parent.pyx", line 2911, in sage.structure.parent.EltPair.__hash__ (sage/structure/parent.c:21193)
      File "plural.pyx", line 573, in sage.rings.polynomial.plural.NCPolynomialRing_plural.__hash__ (sage/rings/polynomial/plural.cpp:6487)
    OverflowError: Python int too large to convert to C long
```

Notice the similarity, but now it's in sage/rings/polynomial/plural.

----
Unrelated to these:

```
sage -t  devel/sage-main/sage/misc/inline_fortran.py
**********************************************************************
File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/misc/inline_fortran.py", line 29:
    sage: fortran(_example)
Exception raised:
    Traceback (most recent call last):
      File "/home/sagetest/sage-5.8.beta4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/sagetest/sage-5.8.beta4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/sagetest/sage-5.8.beta4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[4]>", line 1, in <module>
        fortran(_example)###line 29:
    sage: fortran(_example)
      File "/home/sagetest/sage-5.8.beta4/local/lib/python/site-packages/sage/misc/inline_fortran.py", line 21, in __call__
        return self.eval(*args, **kwds)
      File "/home/sagetest/sage-5.8.beta4/local/lib/python/site-packages/sage/misc/inline_fortran.py", line 93, in eval
        raise RuntimeError("failed to compile Fortran code:\n" + log_string)
    RuntimeError: failed to compile Fortran code:
    Found executable /home/sagetest/sage-5.8.beta4/local/bin/sage-inline-fortran
    gnu: no Fortran 90 compiler found
 Found executable /usr/bin/ld
    Found executable /usr/bin/ar
    Found executable /usr/bin/ranlib
    gnu: no Fortran 90 compiler found

**********************************************************************
```



```
sage -t  devel/sage-main/sage/functions/other.py
**********************************************************************
File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/functions/other.py", line 664:
    sage: gamma1(float(6))
Expected:
    120.0
Got:
    119.99999999999997
**********************************************************************
```



```
sage -t  devel/sage-main/sage/misc/cython.py
Compiling hello.spyx...
cp: cannot stat `/home/Administrator/.sage/temp/CETGORD_J5FGIPM/7732/spyx/hello/hello.so': No such file or directory
**********************************************************************
File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/misc/cython.py", line 695:
    sage: cython_create_local_so('hello.spyx')
Exception raised:
    Traceback (most recent call last):
      File "/home/sagetest/sage-5.8.beta4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/sagetest/sage-5.8.beta4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/sagetest/sage-5.8.beta4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[8]>", line 1, in <module>
        cython_create_local_so('hello.spyx')###line 695:
    sage: cython_create_local_so('hello.spyx')
      File "/home/sagetest/sage-5.8.beta4/local/lib/python/site-packages/sage/misc/cython.py", line 706, in cython_create_local_so
        cython(filename, compile_message=True, use_cache=False, create_local_so_file=True)
      File "/home/sagetest/sage-5.8.beta4/local/lib/python/site-packages/sage/misc/cython.py", line 554, in cython
        raise RuntimeError, "Error making local copy of shared object library for %s"%filename
    RuntimeError: Error making local copy of shared object library for hello.spyx
**********************************************************************
```



```
sage -t  devel/sage-main/sage/symbolic/expression.pyx
**********************************************************************
File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/symbolic/expression.pyx", line 6721:
    sage: SR(10.0r).gamma()
Expected:
    362880.0
Got:
    362879.9999999998
#0: simplify_sum(expr='sum(q^k,k,0,inf))
#1: simplify_sum(expr=a*'sum(q^k,k,0,inf))
**********************************************************************
```



```
sage -t  devel/sage-main/sage/structure/sage_object.pyx
**********************************************************************
File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/structure/sage_object.pyx", line 1215:
    sage: if uid==0:
        raise OSError('You must not run the doctests as root, geez!')
    else: sage.structure.sage_object.picklejar(Integer(1), dir + '/noaccess')
Expected:
    Traceback (most recent call last):
    ...
    OSError: ...
Got nothing
**********************************************************************
```



```
sage -t  devel/sage-main/sage/tests/cmdline.py
**********************************************************************
File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/tests/cmdline.py", line 376:
    sage: ret
Expected:
    0
Got:
    -6
**********************************************************************
```



---

Comment by kcrisman created at 2013-03-12 15:07:18

> As it turns out, #14254 wasn't the (whole) problem.  Most of the errors were of the following ilk.
> {{{
> Exception KeyError: (The ring pointer -0x1f5282c,) in 'sage.libs.singular.ring.singular_ring_delete' ignored
> }}}
I don't know what is going on here.
>{{{
>       File "plural.pyx", line 573, in sage.rings.polynomial.plural.NCPolynomialRing_plural.__hash__ (sage/rings/polynomial/plural.cpp:6487)
>     OverflowError: Python int too large to convert to C long
> }}}
So ... would importing and using the `signed_id` function from #14254 be sufficient here?
> {{{
>     Found executable /home/sagetest/sage-5.8.beta4/local/bin/sage-inline-fortran
>     gnu: no Fortran 90 compiler found
>  Found executable /usr/bin/ld
>     Found executable /usr/bin/ar
>     Found executable /usr/bin/ranlib
>     gnu: no Fortran 90 compiler found
> }}}
I'm not sure why this isn't working.
> {{{
> sage -t  devel/sage-main/sage/functions/other.py
> **********************************************************************
> File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/functions/other.py", line 664:
>     sage: gamma1(float(6))
> Expected:
>     120.0
> Got:
>     119.99999999999997
> **********************************************************************
> }}}
This seems very familiar.  I am pretty sure we have other platforms where this happens - #10285 seems to have this, for instance.  #8847 should have fixed this a long time ago, but maybe I have the wrong stuff now?
> {{{
> sage -t  devel/sage-main/sage/misc/cython.py
> Compiling hello.spyx...
> cp: cannot stat `/home/Administrator/.sage/temp/CETGORD_J5FGIPM/7732/spyx/hello/hello.so': No such file or directory
> **********************************************************************
> File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/misc/cython.py", line 695:
>     sage: cython_create_local_so('hello.spyx')
>     RuntimeError: Error making local copy of shared object library for hello.spyx
> **********************************************************************
> }}}
No idea.  Maybe a permissions thing?
> {{{
> sage -t  devel/sage-main/sage/symbolic/expression.pyx
> **********************************************************************
> File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/symbolic/expression.pyx", line 6721:
>     sage: SR(10.0r).gamma()
> Expected:
>     362880.0
> Got:
>     362879.9999999998
> #0: simplify_sum(expr='sum(q^k,k,0,inf))
> #1: simplify_sum(expr=a*'sum(q^k,k,0,inf))
> **********************************************************************
> }}}
Same issue as above, I would say.
> {{{
> sage -t  devel/sage-main/sage/structure/sage_object.pyx
> **********************************************************************
> File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/structure/sage_object.pyx", line 1215:
>     sage: if uid==0:
>         raise OSError('You must not run the doctests as root, geez!')
>     else: sage.structure.sage_object.picklejar(Integer(1), dir + '/noaccess')
> Expected:
>     Traceback (most recent call last):
>     ...
>     OSError: ...
> Got nothing
> **********************************************************************
> }}}
Aside from the bizarre expected OSError, I would guess this is closely related to the next one.
> {{{
> sage -t  devel/sage-main/sage/tests/cmdline.py
> **********************************************************************
> File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/tests/cmdline.py", line 376:
>     sage: ret
> Expected:
>     0
> Got:
>     -6
> **********************************************************************
> }}}
This seems to be from the command

```
sage: (out, err, ret) = test_executable(["sage", "--ipython"], "\n3**33\n")
```

but when would IPython return negative 6?


---

Comment by SimonKing created at 2013-03-12 15:22:02

Replying to [comment:193 kcrisman]:
> > As it turns out, #14254 wasn't the (whole) problem.  Most of the errors were of the following ilk.
> > {{{
> > Exception KeyError: (The ring pointer -0x1f5282c,) in 'sage.libs.singular.ring.singular_ring_delete' ignored
> > }}}
> I don't know what is going on here.

There is a ticket #13447 concerning garbage collection of libsingular rings. The work stalled, because of problems related with #715 that eventually turned out to be upstream bugs in (a) Singular and (b) Cython. It would certainly make sense to try and revive this ticket.

> >{{{
> >       File "plural.pyx", line 573, in sage.rings.polynomial.plural.NCPolynomialRing_plural.__hash__ (sage/rings/polynomial/plural.cpp:6487)
> >     OverflowError: Python int too large to convert to C long
> > }}}
> So ... would importing and using the `signed_id` function from #14254 be sufficient here?

Note that the error message is different: Now, it is not a long int that can not be converted to an int, but it is a Python int that is too long for a long.


---

Comment by kcrisman created at 2013-03-12 15:25:44

> Note that the error message is different: Now, it is not a long int that can not be converted to an int, but it is a Python int that is too long for a long.
Hmm, good point.

----

Of course, none of this should keep us from finishing this ticket with the atlas check - just wanted to see if anyone else got these.  Certainly we don't need all tests to pass yet, though the moving target continues to be frustrating.


---

Comment by jpflori created at 2013-03-14 00:31:33

I had a quick look at the errors Karl Dieter reported and most of them are the same as the ones I reported earlier.

The strangest is from "sage -t  devel/sage-main/sage/tests/cmdline.py" where there seems to be some missynchronization.

I did not have time to llok at the gfortran and cython ones yet and have no clue whether they will be really problematic or not.

The precision problems seem indeed similar to the ones on ARM platforms, surely a glibc bug.

The coercion issues involving overflow are new.
I'll try to give a shot at 5.9.beta0 tomorrow.

And I think its normal the cblas and lapack spkg are really built, its just the atlas one which is not (at the moment, maybe #10508 will get merged one day and we'll build atlas on cygwin by default in a follow up ticket).


---

Comment by kcrisman created at 2013-03-14 13:02:00

Here is the current status for this ticket, then, in my view.
 * Figure out whether mpfr-4 needs to be installed or not.  I now have two different brand-new installs of Cygwin that failed with the current package list until I installed it.  It was _not_ pulled in with gcc-core and friends.
 * Patch to remove `SAGE_PORT=yes` requirement for Cygwin.
   * Related to that, we still get the message about `sqrtl in -lm` outdated math library, which presumably would make things fail if `SAGE_PORT` wasn't set, so we need to somehow fix things so that's not an issue.  What happens on FreeBSD?
 * Patch to atlas spkg-install (possibly at #10508, or possibly earlier) to say _precisely_ which lapack packages to install, as in the ticket description.
 * As Jeroen points out, make sure that we put something in so that we don't use the (current) Sage 4.6 GCC spkg to build on Cygwin.  This could involve making the 4.7.2 spkg standard (I don't believe there is a ticket for this yet, though there is a sage-devel thread reporting a fair amount of success), or something else.


---

Comment by jdemeyer created at 2013-03-14 13:17:27

Replying to [comment:197 kcrisman]:
> Here is the current status for this ticket, then, in my view.
>  * Figure out whether mpfr-4 needs to be installed or not.  I now have two different brand-new installs of Cygwin that failed with the current package list until I installed it.  It was _not_ pulled in with gcc-core and friends.

Just to make sure that I understand you correctly: you say that
1. A "brand-new install of Cygwin" does not come with a C compiler.
2. If one tries to install GCC by installing gcc-core, it does not automatically install the mpfr dependency.


---

Comment by kcrisman created at 2013-03-14 13:27:58

Another weird data point; when trying to build with `SAGE_INSTALL_GCC=yes` and the Sage gcc-4.7 package, I get

```
checking for __gmpz_init in -lgmp... no
configure: error: libgmp not found or uses a different ABI (including static vs shared).
Error configuring MPC.
```

I assume this is because of the "reduced" MPIR that we build when building gcc.  Properly speaking, this belongs on some other ticket, but I figured I'd point it out here.

----

As to Jeroen's question, I would say "yes" and "yes", but with the caveat of installing gcc4-core only installs mpfr-1, not mpfr-4 (whatever the difference is).  However, JP seems to have had a different experience, which is why I say "figure out", not just "add to prereqs".


---

Comment by jpflori created at 2013-03-14 14:50:33

Replying to [comment:199 kcrisman]:
> Another weird data point; when trying to build with `SAGE_INSTALL_GCC=yes` and the Sage gcc-4.7 package, I get
> {{{
> checking for __gmpz_init in -lgmp... no
> configure: error: libgmp not found or uses a different ABI (including static vs shared).
> Error configuring MPC.
> }}}
> I assume this is because of the "reduced" MPIR that we build when building gcc.  Properly speaking, this belongs on some other ticket, but I figured I'd point it out here.
Strange I just succesfully compiled gcc 4.7.2.p0 spkg with the list of Cygwin packages I posted earlier installed.
> 
> ----
> 
> As to Jeroen's question, I would say "yes" and "yes", but with the caveat of installing gcc4-core only installs mpfr-1, not mpfr-4 (whatever the difference is).  However, JP seems to have had a different experience, which is why I say "figure out", not just "add to prereqs".
Indeed, no compiler by default.

I'll check what happens on a clean install later as well.


---

Comment by kcrisman created at 2013-03-14 20:21:18

>  * Patch to atlas spkg-install (possibly at #10508, or possibly earlier) to say _precisely_ which lapack packages to install, as in the ticket description.
Note that in trying #10508 "straight up", I needed to move /usr/lib/libblas.dll.a and /usr/lib/liblapack.a to `$SAGE_LOCAL/lib`.  The latter for Scipy to build, I assume the former for the Sage library to build.  So whether or not this ticket goes in before #10508, we need to deal with this issue.


---

Comment by jpflori created at 2013-03-14 21:34:57

Replying to [comment:198 jdemeyer]:
> Replying to [comment:197 kcrisman]:
> > Here is the current status for this ticket, then, in my view.
> >  * Figure out whether mpfr-4 needs to be installed or not.  I now have two different brand-new installs of Cygwin that failed with the current package list until I installed it.  It was _not_ pulled in with gcc-core and friends.
> 
> Just to make sure that I understand you correctly: you say that
> 1. A "brand-new install of Cygwin" does not come with a C compiler.
> 2. If one tries to install GCC by installing gcc-core, it does not automatically install the mpfr dependency.
I just reinstalled Cygwin on my 32 bits W7 and pulled in the following packages:
* make
* perl
* binutils
* m4
* lapack
* liblapack-devel
* gcc4
* gcc4-core
* gcc4-g++
* gcc4-gfortran
I took the 4.7.2-1 versions which just popped up.
And indeed only the libmpfr1 package was pulled automatically and not the libmpfr4.
Here is the list of packages currently installed:

```
Cygwin Package Information
Package              Version              Status
_autorebase          000218-1             OK
_update-info-dir     01114-1              OK
alternatives         1.3.30c-10           OK
base-cygwin          3.1-1                OK
base-files           4.1-2                OK
bash                 4.1.10-4             OK
binutils             2.23.51-1            OK
bzip2                1.0.6-2              OK
coreutils            8.15-1               OK
crypt                1.2-1                OK
cygutils             1.4.10-2             OK
cygwin               1.7.17-1             OK
cygwin-doc           1.7-1                OK
dash                 0.5.7-1              OK
diffutils            3.2-1                OK
dos2unix             6.0.3-1              OK
editrights           1.01-2               OK
file                 5.11-1               OK
findutils            4.5.9-2              OK
gawk                 4.0.2-1              OK
gcc4                 4.7.2-1              OK
gcc4-core            4.7.2-1              OK
gcc4-fortran         4.7.2-1              OK
gcc4-g++             4.7.2-1              OK
gettext              0.18.1.1-2           OK
grep                 2.6.3-1              OK
groff                1.21-2               OK
gzip                 1.4-1                OK
ipc-utils            1.0-1                OK
lapack               3.4.2-1              OK
less                 444-1                OK
libattr1             2.4.46-1             OK
libbz2_1             1.0.6-2              OK
libcloog0            0.15.7-1             OK
libdb4.5             4.5.20.2-3           OK
libexpat1            2.1.0-1              OK
libffi4              4.7.2-1              OK
libgcc1              4.7.2-1              OK
libgdbm4             1.8.3-20             OK
libgfortran3         4.7.2-1              OK
libgmp3              4.3.2-1              OK
libgmpxx4            4.3.2-1              OK
libgomp1             4.7.2-1              OK
libiconv2            1.14-2               OK
libintl8             0.18.1.1-2           OK
liblapack-devel      3.4.2-1              OK
liblapack0           3.4.2-1              OK
liblzma5             5.0.2_20110517-1     OK
libmpc1              0.8-1                OK
libmpfr1             2.4.1-4              OK
libncurses10         5.7-18               OK
libncursesw10        5.7-18               OK
libopenssl100        1.0.1e-2             OK
libpcre0             8.21-2               OK
libpopt0             1.6.4-4              OK
libppl               0.10.2-1             OK
libquadmath0         4.7.2-1              OK
libreadline7         6.1.2-3              OK
libsigsegv2          2.10-1               OK
libssp0              4.7.2-1              OK
libstdc++6           4.7.2-1              OK
libstdc++6-devel     4.7.2-1              OK
libxml2              2.9.0-2              OK
login                1.10-10              OK
m4                   1.4.16-1             OK
make                 3.82.90-1            OK
man                  1.6g-1               OK
mintty               1.1.2-1              OK
perl                 5.14.2-3             OK
perl_vendor          5.14.2-3             OK
rebase               4.4.0-1              OK
run                  1.1.13-1             OK
sed                  4.2.1-2              OK
tar                  1.26-1               OK
terminfo             5.7_20091114-14      OK
texinfo              4.13-4               OK
tzcode               2012j-1              OK
upx-debuginfo        3.09-1               OK
w32api               9999-1               OK
w32api-headers       3.0b_svn5591-1       OK
w32api-runtime       3.0b_svn5591-1       OK
which                2.20-2               OK
xz                   5.0.2_20110517-1     OK
zlib0                1.2.7-1              OK
```

I'll launch the Sage build now and report later.

On my 64 bits W7 system with an old Cygwin install, I could build 5.9.beta0 with Cygwin gcc4 4.5.3 used to bootstrap Sage's gcc 4.7.2, except for matplotlib because of forking issues as reported by Karl Dieter.
libmpfr4 is present, not sure when it was pulled.


---

Comment by jpflori created at 2013-03-14 21:45:53

And the 32 bits build immediately failed because gcc could not find some library '? printed).

I guess libmpfr4 is indeed needed now and maybe was as well earlier.
See http://cygwin.1069669.n5.nabble.com/Shouldn-t-gcc-4-depend-on-libmpfr4-td96533.html

I just installed it and at least the build process starts.


---

Comment by kcrisman created at 2013-03-15 00:35:22

> I took the 4.7.2-1 versions which just popped up.
Interesting.  Indeed, then we could just make that the dependency and not build Sage's gcc.
> And indeed only the libmpfr1 package was pulled automatically and not the libmpfr4.
Glad your experience was similar.
> On my 64 bits W7 system with an old Cygwin install, I could build 5.9.beta0 with Cygwin gcc4 4.5.3 used to bootstrap Sage's gcc 4.7.2, except for matplotlib because of forking issues as reported by Karl Dieter.
> libmpfr4 is present, not sure when it was pulled.
I have a feeling that at some time not so long ago gcc4 _did_ pull this, but that that changed recently - your thread implies there was a lot of confusion about it!

----

In other news, can we figure out _exactly_ which lapack things we need minimally?  In particular, you took fewer than in the ticket description - in fact, not even a subset.  I don't care which, but we do need to know!  (Until we just build atlas, I suppose; it's annoying that we have to wait on that, but for now it's better to get this ticket done properly.)


---

Comment by jdemeyer created at 2013-03-15 22:09:29

Replying to [comment:197 kcrisman]:
>    * Related to that, we still get the message about `sqrtl in -lm` outdated math library, which presumably would make things fail if `SAGE_PORT` wasn't set, so we need to somehow fix things so that's not an issue.
Please elaborate (or better yet: post the prereq log, including `config.log` inside the prereq "build" directory).


---

Comment by kcrisman created at 2013-03-19 12:47:36

In the prereq spkg log, at the end:

```
checking gcc version... 4.5.3
checking if g++ accepts -dumpversion option... yes
checking g++ version... 4.5.3
configure: Excellent, the C, C++ and Fortran compilers are all GCC 4.5.3
configure: Excellent, GCC 4.5.3 is later than the minimum
configure: needed to build Sage, which is GCC version 4.0.1
checking for sqrt in -lm... yes
checking for sqrtl in -lm... no
configure: You have an outdated and/or broken math library.
configure: error: Exiting, since the library function 'sqrtl()' was not found.
You do not have all of the prerequisites needed to build Sage
from source. See the errors above.
However, since 'SAGE_PORT' is set, we will try to build anyway.
Now cleaning up tmp files.
```

Supposedly this was (I think?) provided by Cephes, but of course that never actually built on Cygwin, as JP discovered.  I wonder when this was even added in the configure script in the tar.gz in base.

Grepping through the entire Sage root directory shows that sqrtl mostly comes in play with Pynac and Scipy/Numpy, and we seem to even (?) define our own sqrtl... oh, also in the partitions code in combinat this is needed.  The Pari references I think are to sqrtlift, something else.  Maybe we don't need this any more?  I presume this was added by David Kirkby for Solaris or other platforms with weird base libraries.


---

Comment by kcrisman created at 2013-03-19 13:12:33

To be more specific, this was added in #8052:

```
Checks for the library function sqrtl() which will be found on modern systems, but may not on older systems. 
A warning is issued if the library function does not exist, but the build continues, to aid porting efforts. 
(I believe FreeBSD may lack this).
```

I don't know whether this is actually true (that sqrtl is needed), though, nor where the Cygwin build gets its sqrtl in that event.


---

Comment by leif created at 2013-03-19 15:31:51

Replying to [comment:206 kcrisman]:
> In the prereq spkg log, at the end:
> {{{
> ...
> checking for sqrtl in -lm... no
> configure: You have an outdated and/or broken math library.
> configure: error: Exiting, since the library function 'sqrtl()' was not found.
> ...
> }}}
> Supposedly this was (I think?) provided by Cephes, but of course that never actually built on Cygwin, as JP discovered.

WHAT?!  The only reason for including Cephes as a standard package was Cygwin, because it was said to lack some `long double` versions ('`l`' suffix) of standard math functions (such as `sqrt()`).

> Grepping through the entire Sage root directory shows that sqrtl mostly comes in play with Pynac and !Scipy/Numpy, and we seem to even (?) define our own sqrtl...

I recall somebody somewhere replacing (`#define`ing?) `sqrtl()` by `sqrt()`, arguing `double` precision was sufficient there, for the sake of Cygwin, and that AFAIK didn't get removed even after the inclusion of Cephes.  (Not 100% sure whether it was really `sqrt()`; probably some other function, but Cygwin was lacking its `long double` implementation.)

> oh, also in the partitions code in combinat this is needed.  The Pari references I think are to sqrtlift, something else.  Maybe we don't need this any more?  I presume this was added by David Kirkby for Solaris or other platforms with weird base libraries.

Certainly not for Solaris... ;-)


---

Comment by kcrisman created at 2013-03-19 15:43:06

> > In the prereq spkg log, at the end:
> > {{{
> > ...
> > checking for sqrtl in -lm... no
> > configure: You have an outdated and/or broken math library.
> > configure: error: Exiting, since the library function 'sqrtl()' was not found.
> > ...
> > }}}
> > Supposedly this was (I think?) provided by Cephes, but of course that never actually built on Cygwin, as JP discovered.
> 
> WHAT?!  The only reason for including Cephes as a standard package was Cygwin, because it was said to lack some `long double` versions ('`l`' suffix) of standard math functions (such as `sqrt()`).
> I recall somebody somewhere replacing (`#define`ing?) `sqrtl()` by `sqrt()`, arguing `double` precision was sufficient there, for the sake of Cygwin, and that AFAIK didn't get removed even after the inclusion of Cephes.  (Not 100% sure whether it was really `sqrt()`; probably some other function, but Cygwin was lacking its `long double` implementation.)
Wow, that would have been a long time ago... If you can find a reference that would be helpful.

Anyway, #8052 makes it reasonably clear that FreeBSD is the one David had in mind with this test, not Cygwin.  And we do indeed now use Cephes on FreeBSD (only), see #9543.


---

Comment by leif created at 2013-03-19 15:58:38

Replying to [comment:210 kcrisman]:
> > I recall somebody somewhere replacing (`#define`ing?) `sqrtl()` by `sqrt()`, arguing `double` precision was sufficient there, for the sake of Cygwin, and that AFAIK didn't get removed even after the inclusion of Cephes.  (Not 100% sure whether it was really `sqrt()`; probably some other function, but Cygwin was lacking its `long double` implementation.)
> Wow, that would have been a long time ago... If you can find a reference that would be helpful.

According to #14078 it was `logl()` (my second guess :-) [third was `gammal()` or `lgammal()`]), but the ticket only refers to R, while _I think<sup>TM</sup>_ the replacement was (also) done somewhere else.




> Anyway, #8052 makes it reasonably clear that FreeBSD is the one David had in mind with this test, not Cygwin.  And we do indeed now use Cephes on FreeBSD (only), see #9543.

Yes, FreeBSD is pretty broken as well...


---

Comment by leif created at 2013-03-19 16:11:41

Replying to [comment:211 leif]:
> Replying to [comment:210 kcrisman]:
> > > I recall somebody somewhere replacing (`#define`ing?) `sqrtl()` by `sqrt()`, arguing `double` precision was sufficient there, for the sake of Cygwin, and that AFAIK didn't get removed even after the inclusion of Cephes.  (Not 100% sure whether it was really `sqrt()`; probably some other function, but Cygwin was lacking its `long double` implementation.)
> > Wow, that would have been a long time ago... If you can find a reference that would be helpful.
> 
> According to #14078 it was `logl()` (my second guess :-) [third was `gammal()` or `lgammal()`]), but the ticket only refers to R, while _I think<sup>TM</sup>_ the replacement was (also) done somewhere else.

I only found #8847 (and #9162), but I don't think these are the instances I meant.

(#8847 adds wrapper functions with `#ifdef __CYGWIN__ ...`.)


---

Comment by jpflori created at 2013-03-19 16:25:57

Replying to [comment:209 leif]:
> Replying to [comment:206 kcrisman]:
> > In the prereq spkg log, at the end:
> > {{{
> > ...
> > checking for sqrtl in -lm... no
> > configure: You have an outdated and/or broken math library.
> > configure: error: Exiting, since the library function 'sqrtl()' was not found.
> > ...
> > }}}
> > Supposedly this was (I think?) provided by Cephes, but of course that never actually built on Cygwin, as JP discovered.
> 
> WHAT?!  The only reason for including Cephes as a standard package was Cygwin, because it was said to lack some `long double` versions ('`l`' suffix) of standard math functions (such as `sqrt()`).
I don't really know, but Cygwin libm was really lacking a LOT of functions, some of them were pulled from Cephes at some point, but not al of what Cephes provides, and the libm Cygwin now ships seems mostly sufficient to build Sage.
At least it was until a few realease and an update of R which requires one "long double"function, but that got easily patched (rather than requiring again to build Cephes which I would be happy with as well, but seems harder to maintain).
> 
> > Grepping through the entire Sage root directory shows that sqrtl mostly comes in play with Pynac and !Scipy/Numpy, and we seem to even (?) define our own sqrtl...
> 
> I recall somebody somewhere replacing (`#define`ing?) `sqrtl()` by `sqrt()`, arguing `double` precision was sufficient there, for the sake of Cygwin, and that AFAIK didn't get removed even after the inclusion of Cephes.  (Not 100% sure whether it was really `sqrt()`; probably some other function, but Cygwin was lacking its `long double` implementation.)
> 
> > oh, also in the partitions code in combinat this is needed.  The Pari references I think are to sqrtlift, something else.  Maybe we don't need this any more?  I presume this was added by David Kirkby for Solaris or other platforms with weird base libraries.
> 
> Certainly not for Solaris... ;-)
>


---

Comment by jdemeyer created at 2013-03-20 07:53:41

So the conclusion is that we should remove the `sqrtl()` test?


---

Comment by dimpase created at 2013-03-20 08:12:44

Replying to [comment:214 jdemeyer]:
> So the conclusion is that we should remove the `sqrtl()` test?

IIRC, R uses logl(), and a workaround has been put in place for this.
I don't recall the details, but, perhaps, the test for logl() instead would work, or can be made to work, on Cygwin.


---

Comment by jpflori created at 2013-03-28 23:08:28

I think Im on the track of the matplotlib failure.
On my system, the fork errors look like:

```
2 [main] python2.7 3540 child_info_fork::abort: C:\cygwin\home\jp\sage-5.9.beta0\local\bin\libpython2.7.dll: Loaded to different address: parent(0x5EC70000) != child(0x6A640000)
```

And in the rebase database, I can see

```
$ rebase -i -s|grep "libpython"
/usr/bin/libpython2.7.dll                                                                                                                                     base 0x5ec70000 size 0x00176000
/home/jp/sage-5.9.beta0/local/bin/libpython2.7.dll                                                                                                            base 0x6a640000 size 0x00599000
```

So it seems the system and Sage libpython2.7.dll get mixed up.
This was surely not a problem before as Cygwin just recently updated to Python 2.7, see http://cygwin.com/ml/cygwin-announce/2012-12/msg00024.html

Let's now find out why both libraries get mixed up.


---

Comment by jpflori created at 2013-03-28 23:18:47

And indeed, uninstalling the system wide python let matplotlib install correctly.
Of course that's not the right solution to promote :)


---

Comment by jpflori created at 2013-03-28 23:52:02

It seems its the _ctypes.dll library which loads the system wide libpython2.7.dll.
Just moving _ctypes.dll so that it does not get loaded and the wrong libpython2.7.dll does not, let matplotlib build.
Strange.


---

Comment by jpflori created at 2013-03-29 00:09:07

Indeed in ctypes/__init__.py

```
elif _sys.platform == "cygwin":
    pythonapi = PyDLL("libpython%d.%d.dll" % _sys.version_info[:2])
```


Basically PyDLL, loads the library calling _dlopen which is an alias from LoadLibrary from the _ctypes module (with an underscore).

And it seems it does not care about PATH.
But if I set LD_LIBRARY_PATH to point to where Sage's libpython2.7.dll is, then its correctly loaded rather than the system one.

Not sure what happens on linux :)
I seem to remember some recent discussion about _ctypes which was not built before and caused troubles recently.


---

Comment by jpflori created at 2013-03-29 00:11:40

My vague souvenir was about #14309 so not related.


---

Comment by jpflori created at 2013-03-29 00:22:28

Strange that the fact $SAGE_LOCAL/bin is in $PATH is not sufficient but whatever.
And not sure why in sage-enc $SAGE_LOCAL/lib is appended rather than prepended.
I mean, were prepending $SAGE_LOCAL/bin, so...


---

Comment by leif created at 2013-03-29 01:05:14

Replying to [comment:221 jpflori]:
> Strange that the fact $SAGE_LOCAL/bin is in $PATH is not sufficient but whatever.
> And not sure why in sage-enc $SAGE_LOCAL/lib is appended rather than prepended.
> I mean, were prepending $SAGE_LOCAL/bin, so...

? In both cases (`PATH` as well as `LD_LIBRARY_PATH`), directories get *pre*pended (provided they exist).

On Unices, `libpython-*.so*` is in `$SAGE_LOCAL/{lib,lib32,lib64}/`, so can be found along `$LD_LIBRARY_PATH`.

If Cygwin's `dlopen()` conforms to POSIX (it probably does), it doesn't use `PATH` but `LD_LIBRARY_PATH` (if set), unless an absolute path was given in the filename argument.


---

Comment by jdemeyer created at 2013-03-29 04:13:34

See #14378 for upgrading GCC.


---

Comment by jpflori created at 2013-03-29 08:07:10

Replying to [comment:222 leif]:
> Replying to [comment:221 jpflori]:
> > Strange that the fact $SAGE_LOCAL/bin is in $PATH is not sufficient but whatever.
> > And not sure why in sage-enc $SAGE_LOCAL/lib is appended rather than prepended.
> > I mean, were prepending $SAGE_LOCAL/bin, so...
> 
> ? In both cases (`PATH` as well as `LD_LIBRARY_PATH`), directories get *pre*pended (provided they exist).
It seems PATH is not, in sage-env:

```
export PATH="$SAGE_PACKAGES/bin:$SAGE_LOCAL/bin:$PATH"
```

> 
> On Unices, `libpython-*.so*` is in `$SAGE_LOCAL/{lib,lib32,lib64}/`, so can be found along `$LD_LIBRARY_PATH`.
But on Cygwin its in .../bin/ whence the problem I guess.
> 
> If Cygwin's `dlopen()` conforms to POSIX (it probably does), it doesn't use `PATH` but `LD_LIBRARY_PATH` (if set), unless an absolute path was given in the filename argument.
Yup.
That's fine, but also disturbing as all the (rest of the) dll magic uses PATH rather than LD_LIBRARY_PATH on Cygwin.
>


---

Comment by jpflori created at 2013-03-29 09:30:50

Replying to [comment:224 jpflori]:
> Replying to [comment:222 leif]:
> > Replying to [comment:221 jpflori]:
> > > Strange that the fact $SAGE_LOCAL/bin is in $PATH is not sufficient but whatever.
> > > And not sure why in sage-enc $SAGE_LOCAL/lib is appended rather than prepended.
> > > I mean, were prepending $SAGE_LOCAL/bin, so...
> > 
> > ? In both cases (`PATH` as well as `LD_LIBRARY_PATH`), directories get *pre*pended (provided they exist).
> It seems PATH is not, in sage-env:
> {{{
> export PATH="$SAGE_PACKAGES/bin:$SAGE_LOCAL/bin:$PATH"
> }}}
And I think it's normal.
We want Sage binaries to be found first.

As far as [LD_]LIBRARY_PATH is concerned, I wouldn't find it so disturbing to prepend SAGE local dirs as well.

But note that PATH is usually set (or the shell used might not be so useful) whereas [LD]_LIBRARY_PATH is not.
So prepending our local values in the first case is really the most sensible choice, whereas in the second you might think that the user has added something unusual knowingly and he wants it first, if that breaks that's his problem.
> > 
> > On Unices, `libpython-*.so*` is in `$SAGE_LOCAL/{lib,lib32,lib64}/`, so can be found along `$LD_LIBRARY_PATH`.
> But on Cygwin its in .../bin/ whence the problem I guess.
> > 
> > If Cygwin's `dlopen()` conforms to POSIX (it probably does), it doesn't use `PATH` but `LD_LIBRARY_PATH` (if set), unless an absolute path was given in the filename argument.
> Yup.
> That's fine, but also disturbing as all the (rest of the) dll magic uses PATH rather than LD_LIBRARY_PATH on Cygwin.
> >


---

Comment by jpflori created at 2013-03-29 09:42:26

Replying to [comment:224 jpflori]:
> Replying to [comment:222 leif]:
> > Replying to [comment:221 jpflori]:
> > > Strange that the fact $SAGE_LOCAL/bin is in $PATH is not sufficient but whatever.
> > > And not sure why in sage-enc $SAGE_LOCAL/lib is appended rather than prepended.
> > > I mean, were prepending $SAGE_LOCAL/bin, so...
> > 
> > ? In both cases (`PATH` as well as `LD_LIBRARY_PATH`), directories get *pre*pended (provided they exist).
> It seems PATH is not, in sage-env:
> {{{
> export PATH="$SAGE_PACKAGES/bin:$SAGE_LOCAL/bin:$PATH"
> }}}
> > 
> > On Unices, `libpython-*.so*` is in `$SAGE_LOCAL/{lib,lib32,lib64}/`, so can be found along `$LD_LIBRARY_PATH`.
> But on Cygwin its in .../bin/ whence the problem I guess.
> > 
> > If Cygwin's `dlopen()` conforms to POSIX (it probably does), it doesn't use `PATH` but `LD_LIBRARY_PATH` (if set), unless an absolute path was given in the filename argument.
> Yup.
> That's fine, but also disturbing as all the (rest of the) dll magic uses PATH rather than LD_LIBRARY_PATH on Cygwin.
> > 
In fact that's not really POSIX requested, from the doc of dlopen in POSIX specs (if those are what is at http://pubs.opengroup.org/onlinepubs/9699919799/):

```
...
The file argument is used to construct a pathname to the object file. If file contains a slash character, the file argument is used as the pathname for the file.
Otherwise, file is used in an implementation-defined manner to yield a pathname.
...
```

So Cygwin could decide to use PATH :)


---

Comment by jpflori created at 2013-03-29 10:23:31

This is now #14380.


---

Comment by leif created at 2013-03-29 12:45:55

Replying to [comment:225 jpflori]:
> Replying to [comment:224 jpflori]:
> > Replying to [comment:222 leif]:
> > > Replying to [comment:221 jpflori]:
> > > > Strange that the fact $SAGE_LOCAL/bin is in $PATH is not sufficient but whatever.
> > > > And not sure why in sage-enc $SAGE_LOCAL/lib is appended rather than prepended.
> > > > I mean, were prepending $SAGE_LOCAL/bin, so...
> > > 
> > > ? In both cases (`PATH` as well as `LD_LIBRARY_PATH`), directories get *pre*pended (provided they exist).
> > It seems PATH is not, in sage-env:
> > {{{
> > export PATH="$SAGE_PACKAGES/bin:$SAGE_LOCAL/bin:$PATH"
> > }}}
> And I think it's normal.
> We want Sage binaries to be found first.
> 
> As far as [LD_]LIBRARY_PATH is concerned, I wouldn't find it so disturbing to prepend SAGE local dirs as well.
> 
> But note that PATH is usually set (or the shell used might not be so useful) whereas [LD]_LIBRARY_PATH is not.
> So prepending our local values in the first case is really the most sensible choice, whereas in the second you might think that the user has added something unusual knowingly and he wants it first, if that breaks that's his problem.

I still don't understand what you mean.  In both cases, we already prepend _Sage's_ directories, such that Sage's shared libraries and binaries come first.

(That's orthogonal to putting DLLs into `*/bin/` or adding DLL dirs to `PATH` on Cygwin.  Note that IIRC we already do the former for some packages, so if you add `$SAGE_LOCAL/lib/` to `PATH` as well, we IMHO should no longer copy DLLs into `$SAGE_LOCAL/bin/`.)


---

Comment by jpflori created at 2013-03-29 13:50:47

Replying to [comment:228 leif]:
> Replying to [comment:225 jpflori]:
> > > > ? In both cases (`PATH` as well as `LD_LIBRARY_PATH`), directories get *pre*pended (provided they exist).
> > > It seems PATH is not, in sage-env:
> > > {{{
> > > export PATH="$SAGE_PACKAGES/bin:$SAGE_LOCAL/bin:$PATH"
> > > }}}
> > And I think it's normal.
> > We want Sage binaries to be found first.
> > 
> > As far as [LD_]LIBRARY_PATH is concerned, I wouldn't find it so disturbing to prepend SAGE local dirs as well.
> > 
> > But note that PATH is usually set (or the shell used might not be so useful) whereas [LD]_LIBRARY_PATH is not.
> > So prepending our local values in the first case is really the most sensible choice, whereas in the second you might think that the user has added something unusual knowingly and he wants it first, if that breaks that's his problem.
> 
> I still don't understand what you mean.  In both cases, we already prepend _Sage's_ directories, such that Sage's shared libraries and binaries come first.
Oh youre right...
I misread the LD_LIBRARY_PATH part.

```
PATH="$SAGE_ROOT:$SAGE_LOCAL/bin:$PATH" && export PATH
```


```
for d in lib/openmpi lib/R/lib lib32 lib64 lib; do
    libdir="$SAGE_LOCAL/$d"
    # Add only existing directories
    if [ -d "$libdir" ]; then
        [ -z "$LD_LIBRARY_PATH" ] || LD_LIBRARY_PATH=":${LD_LIBRARY_PATH}"
        LD_LIBRARY_PATH="${libdir}$LD_LIBRARY_PATH"
    fi
done
export LD_LIBRARY_PATH
```

But taht's only true on non Cygwin system.
There we have

```
if [ "$UNAME" = "CYGWIN" ]; then
    PATH="$PATH:$SAGE_LOCAL/lib:$SAGE_LOCAL/lib/R/lib" && export PATH
fi
```


> 
> (That's orthogonal to putting DLLs into `*/bin/` or adding DLL dirs to `PATH` on Cygwin.  Note that IIRC we already do the former for some packages, so if you add `$SAGE_LOCAL/lib/` to `PATH` as well, we IMHO should no longer copy DLLs into `$SAGE_LOCAL/bin/`.)
We don't really copy anything anymore in */bin/
At least for all the spkg I've taken care of.
The default scheme on Cygwin is to have:
* static archive (.a), import libraries (.dll.a), libtool magic (.la) in lib
* shared libraries (.dll), executables (.exe) in bin
And you shouldn't have to look in bin for libraries.
Normally (at least from my little experience) when you link (not when you load at runtime) you either use the static archive (which is in lib) or the import library (which is in lib), or you want to skip the import library mess and give full path to the shared library in bin.
And when you end up using the import library, in the end it points you to the shared library in bin, and in your own library or executable there is no trace of the import library, only of the shared library itself.

That's what Python does, but dlopen skip all the fun of import libraries (and it's right, it does not want to link to the library, it just wants to load it) and wants a real shared library ending in .dll.
And with our current values of LD_LIBRARY_PATH and PATH, it first find the system wide one because (that's only a guess) there must be some default search path used between LD_LIBRARY_PATH and PATH.


---

Comment by kcrisman created at 2013-03-29 16:19:31

> Here is the current status for this ticket, then, in my view.
>  * Figure out whether mpfr-4 needs to be installed or not.  I now have two different brand-new installs of Cygwin that failed with the current package list until I installed it.  It was _not_ pulled in with gcc-core and friends.
Looks like it's needed for now, or is there any action on the Cygwin front?
>  * Patch to remove `SAGE_PORT=yes` requirement for Cygwin.
Still needed.
>    * Related to that, we still get the message about `sqrtl in -lm` outdated math library, which presumably would make things fail if `SAGE_PORT` wasn't set, so we need to somehow fix things so that's not an issue.  What happens on FreeBSD?
Any updates with what we should do here?  The code for the sqrtl business that David wrote is a little convoluted for me, but perhaps it wouldn't be that hard to change to logl as was suggested above.
>  * Patch to atlas spkg-install (possibly at #10508, or possibly earlier) to say _precisely_ which lapack packages to install, as in the ticket description.
#10508 seems to now have taken care of this.
>  * As Jeroen points out, make sure that we put something in so that we don't use the (current) Sage 4.6 GCC spkg to build on Cygwin.  This could involve making the 4.7.2 spkg standard (I don't believe there is a ticket for this yet, though there is a sage-devel thread reporting a fair amount of success), or something else.
This is #14378, and Jeroen even has an spkg.


---

Comment by kcrisman created at 2013-03-30 01:05:12

> sage -t  devel/sage-main/sage/misc/inline_fortran.py
This is now #14386.
> 
> sage -t  devel/sage-main/sage/functions/other.py
> sage -t  devel/sage-main/sage/misc/cython.py

This is now #14387.


---

Comment by kcrisman created at 2013-03-30 01:25:12

I got a few new failures, but I think they will be solved mostly by #14370.

Here's one I don't recall seeing before.

```
$ ./sage -t devel/sage/sage/libs/gap/element.pyx
Running doctests with ID 2013-03-29-21-22-54-2674b5b5.
Doctesting 1 file.
sage -t devel/sage/sage/libs/gap/element.pyx
**********************************************************************
File "devel/sage/sage/libs/gap/element.pyx", line 1327, in sage.libs.gap.element.GapElement_Function.__call__
Failed example:
    libgap_exec('echo hello from the shell > /dev/null')
Expected nothing
Got:
    The system cannot find the path specified.
**********************************************************************
1 item had failures:
   1 of  26 in sage.libs.gap.element.GapElement_Function.__call__
    [256 tests, 1 failure, 4.6 s]
----------------------------------------------------------------------
sage -t devel/sage/sage/libs/gap/element.pyx  # 1 doctest failed
----------------------------------------------------------------------
Total time for all tests: 10.7 seconds
    cpu time: 3.7 seconds
    cumulative wall time: 4.6 seconds
```

Anyone seen this?


---

Comment by kcrisman created at 2013-03-30 01:32:19

> As it turns out, #14254 wasn't the (whole) problem.  Most of the errors were of the following ilk.
> {{{
> sage -t  devel/sage-main/sage/algebras/free_algebra.py
> Exception KeyError: (The ring pointer -0x1f5282c,) in 'sage.libs.singular.ring.singular_ring_delete' ignored
> Exception KeyError: (The ring pointer -0x1f52768,) in 'sage.libs.singular.ring.singular_ring_delete' ignored
> Exception KeyError: (The ring pointer -0x1f526a4,) in 'sage.libs.singular.ring.singular_ring_delete' ignored
> **********************************************************************
> File "/home/sagetest/sage-5.8.beta4/devel/sage-main/sage/algebras/free_algebra.py", line 820:
>     sage: G=A.g_algebra({y*x:-x*y})
> Exception raised:
>     Traceback (most recent call last):
>       File "/home/sagetest/sage-5.8.beta4/local/bin/ncadoctest.py", line 1231, in run_one_test
>         self.run_one_example(test, example, filename, compileflags)
>       File "/home/sagetest/sage-5.8.beta4/local/bin/sagedoctest.py", line 38, in run_one_example
>         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
>       File "/home/sagetest/sage-5.8.beta4/local/bin/ncadoctest.py", line 1172, in run_one_example
>         compileflags, 1) in test.globs
>       File "<doctest __main__.example_18[3]>", line 1, in <module>
>         G=A.g_algebra({y*x:-x*y})###line 820:
>     sage: G=A.g_algebra({y*x:-x*y})
>       File "/home/sagetest/sage-5.8.beta4/local/lib/python/site-packages/sage/algebras/free_algebra.py", line 872, in g_algebra
>         order=order, check=check)
>       File "factory.pyx", line 143, in sage.structure.factory.UniqueFactory.__call__ (sage/structure/factory.c:1119)
>       File "factory.pyx", line 170, in sage.structure.factory.UniqueFactory.get_object (sage/structure/factory.c:1311)
>       File "plural.pyx", line 180, in sage.rings.polynomial.plural.G_AlgFactory.create_object (sage/rings/polynomial/plural.cpp:4289)
>       File "plural.pyx", line 358, in sage.rings.polynomial.plural.NCPolynomialRing_plural.__init__ (sage/rings/polynomial/plural.cpp:5351)
>       File "plural.pyx", line 1471, in sage.rings.polynomial.plural.NCPolynomial_plural.__richcmp__ (sage/rings/polynomial/plural.cpp:11452)
>       File "element.pyx", line 855, in sage.structure.element.Element._richcmp (sage/structure/element.c:7980)
>       File "coerce.pyx", line 913, in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:8304)
>       File "coerce.pyx", line 1068, in sage.structure.coerce.CoercionModel_cache_maps.coercion_maps (sage/structure/coerce.c:9855)
>       File "coerce.pyx", line 1209, in sage.structure.coerce.CoercionModel_cache_maps.discover_coercion (sage/structure/coerce.c:11405)
>       File "parent.pyx", line 2116, in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:14383)
>       File "parent.pyx", line 2937, in sage.structure.parent._register_pair (sage/structure/parent.c:21545)
>       File "parent.pyx", line 2911, in sage.structure.parent.EltPair.__hash__ (sage/structure/parent.c:21193)
>       File "plural.pyx", line 573, in sage.rings.polynomial.plural.NCPolynomialRing_plural.__hash__ (sage/rings/polynomial/plural.cpp:6487)
>     OverflowError: Python int too large to convert to C long
> }}}
This is now #14388.


---

Comment by jpflori created at 2013-03-30 13:40:54

Replying to [comment:230 kcrisman]:
> > Here is the current status for this ticket, then, in my view.
> >  * Figure out whether mpfr-4 needs to be installed or not.  I now have two different brand-new installs of Cygwin that failed with the current package list until I installed it.  It was _not_ pulled in with gcc-core and friends.
> Looks like it's needed for now, or is there any action on the Cygwin front?
Looks like their gcc packages were really old and the maintainer has to change...


---

Comment by jpflori created at 2013-03-30 15:07:56

So from the old errors (I've not run "make ptest"):
Replying to [comment:116 jpflori]:
> New ptest log for 5.7.beta1 at
> {{{
> The following tests failed:
> 
> 	sage -t  -force_lib devel/sagenb-main/sagenb/misc/misc.py # Exception from doctest framework
> 	sage -t  -force_lib devel/sage/sage/functions/other.py # 1 doctests failed
> 	sage -t  -force_lib devel/sage/sage/geometry/lattice_polytope.py # 96 doctests failed
> 	sage -t  -force_lib devel/sage/sage/graphs/genus.pyx # 2 doctests failed
> 	sage -t  -force_lib devel/sage/sage/gsl/ode.pyx # 3 doctests failed
> 	sage -t  -force_lib devel/sage/sage/libs/lcalc/lcalc_Lfunction.pyx # 69 doctests failed
> 	sage -t  -force_lib devel/sage/sage/libs/pari/gen.pyx # 4 doctests failed
> 	sage -t  -force_lib devel/sage/sage/misc/cython.py # 3 doctests failed
> 	sage -t  -force_lib devel/sage/sage/misc/getusage.py # 4 doctests failed
> 	sage -t  -force_lib devel/sage/sage/misc/inline_fortran.py # 3 doctests failed
> 	sage -t  -force_lib devel/sage/sage/misc/sageinspect.py # 1 doctests failed
> 	sage -t  -force_lib devel/sage/sage/plot/graphics.py # Time out
> 	sage -t  -force_lib devel/sage/sage/plot/plot.py # Time out
> 	sage -t  -force_lib devel/sage/sage/plot/plot3d/implicit_plot3d.py # Time out
> 	sage -t  -force_lib devel/sage/sage/plot/plot3d/plot3d.py # Time out
> 	sage -t  -force_lib devel/sage/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py # 13 doctests failed
> 	sage -t  -force_lib devel/sage/sage/rings/arith.py # 1 doctests failed
> 	sage -t  -force_lib devel/sage/sage/rings/tests.py # 4 doctests failed
> 	sage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # Time out
> 	sage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/heegner.py # Time out
> 	sage -t  -force_lib devel/sage/sage/schemes/toric/fano_variety.py # 12 doctests failed
> 	sage -t  -force_lib devel/sage/sage/symbolic/expression.pyx # 1 doctests failed
> 	sage -t  -force_lib devel/sage/sage/tests/cmdline.py # Time out
> ----------------------------------------------------------------------
> }}}
> 
> Some were expected:
> * sage/libs/lcalc/lcalc_Lfunction.pyx with fix at #13351
> * sage/geometry/lattice_polytope.py with fix at #13960
> * sage/schemes/toric/fano_variety.py is #13960 as well
> * sage/misc/getusage.py which is #9170
> * sage/graphs/genus.pyx which is in fact #9170
> * sage/libs/pari/gen.pyx which is also #9170
> * sage/rings/tests.py as well #9170
> * sage/quadratic_forms/quadratic_form__ternary_Tornaria.py which is hopefully the same pari stack problem as #9176
Fixed.
> Some are trivial:
> * sage/functions/other.py which is numerical noise
> * sage/rings/arith.py as well
> * sage/symbolic/expression.pyx as well
Same glibc bug (https://bugs.launchpad.net/ubuntu/+source/eglibc/+bug/713985) as #14077, #10285, #12449.
arith.py now passes for me.
The two other doctests still fail. 
> Some look more serious:
> * sage/misc/cython.py but that might just be a dynamic library extension problem
> * sage/misc/inline_fortran.py which does not find gfortran?!
Fixed at #14386 and #14387.
> * sage/misc/sageinspect.py -> fork errors... maybe a rebase could fix that
Passes now on my system.
> * sage/gsl/ode.pyx
Fixed at #14096.


---

Comment by kcrisman created at 2013-03-30 20:49:30

Here's what I get for 5.9.beta2 on Win7 (presumably 32-bit, I have no idea) after a solution to #14388, though not the final one that JP put there, which I will be trying next.  Most will likely be fixed by #14387, #14386, and #14370, just putting for reference.

```
----------------------------------------------------------------------
sage -t sage/tests/interrupt.pyx  # Killed due to segmentation fault
sage -t sage/tests/cmdline.py  # 1 doctest failed
sage -t sage/symbolic/expression.pyx  # 1 doctest failed
sage -t sage/misc/interpreter.py  # 2 doctests failed
sage -t sage/misc/cython.py  # 3 doctests failed
sage -t sage/parallel/decorate.py  # 1 doctest failed
sage -t sage/functions/other.py  # 1 doctest failed
sage -t sage/interfaces/rubik.py  # 1 doctest failed
sage -t sage/structure/sage_object.pyx  # 1 doctest failed
sage -t sage/misc/inline_fortran.py  # 3 doctests failed
sage -t sage/libs/gap/element.pyx  # 1 doctest failed
sage -t sage/misc/sage_extension.py  # 10 doctests failed
sage -t sage/libs/ecl.pyx  # Killed due to segmentation fault
----------------------------------------------------------------------
```

Also, after a rebaseall (rebase -O was not sufficient) an XP build is once again on its way to completion.


---

Comment by kcrisman created at 2013-03-30 21:11:07

Other than the expected numerical ones, all that remains is

```
sage -t sage/libs/gap/element.pyx
**********************************************************************
File "sage/libs/gap/element.pyx", line 1327, in sage.libs.gap.element.GapElement_Function.__call__
Failed example:
    libgap_exec('echo hello from the shell > /dev/null')
Expected nothing
Got:
    The system cannot find the path specified.
**********************************************************************
1 item had failures:
   1 of  26 in sage.libs.gap.element.GapElement_Function.__call__
    [256 tests, 1 failure, 4.6 s]
sage -t sage/structure/sage_object.pyx
**********************************************************************
File "sage/structure/sage_object.pyx", line 1215, in sage.structure.sage_object.picklejar
Failed example:
    if uid==0:
        raise OSError('You must not run the doctests as root, geez!')
    else: sage.structure.sage_object.picklejar(1, dir + '/noaccess')
Expected:
    Traceback (most recent call last):
    ...
    OSError: ...
Got:
    <BLANKLINE>
**********************************************************************
1 item had failures:
   1 of  10 in sage.structure.sage_object.picklejar
    [152 tests, 1 failure, 5.1 s]
sage -t sage/parallel/decorate.py
**********************************************************************
File "sage/parallel/decorate.py", line 559, in sage.parallel.decorate.fork
Failed example:
    print "this works"; g()
Expected:
    this works...
    <BLANKLINE>
    ------------------------------------------------------------------------
    Unhandled SIG...
    ------------------------------------------------------------------------
    'NO DATA'
Got:
    this works
    'NO DATA'
**********************************************************************
1 item had failures:
   1 of  18 in sage.parallel.decorate.fork
    [90 tests, 1 failure, 14.4 s]
sage -t sage/tests/cmdline.py
**********************************************************************
File "sage/tests/cmdline.py", line 415, in sage.tests.cmdline.test_executable
Failed example:
    ret
Expected:
    0
Got:
    -6
*******************************************************************
```

and the more long

```
    Killed due to segmentation fault
**********************************************************************
Tests run before process failed:
sage: from sage.tests.interrupt import return_exception ## line 74 ##
sage: `@`return_exception
def raise_interrupt():
    raise KeyboardInterrupt("just testing") ## line 75 ##
sage: raise_interrupt() ## line 78 ##
KeyboardInterrupt('just testing',)
sage: sig_on_count() ## line 80 ##
0
sage: import sage.tests.interrupt ## line 105 ##
sage: try:
    sage.tests.interrupt.interrupt_after_delay()
    factor(10^1000 + 3)
except KeyboardInterrupt:
    print "Caught KeyboardInterrupt" ## line 106 ##
Caught KeyboardInterrupt
sage: sig_on_count() ## line 112 ##
0
sage: from sage.tests.interrupt import * ## line 123 ##
sage: test_sig_off() ## line 124 ##
sage: sig_on_count() ## line 125 ##
0
sage: from sage.tests.interrupt import * ## line 134 ##
sage: test_sig_on() ## line 135 ##
KeyboardInterrupt()
sage: sig_on_count() ## line 137 ##
0
sage: from sage.tests.interrupt import * ## line 146 ##
sage: test_sig_str() ## line 147 ##
sage: sig_on_count() ## line 151 ##
0
sage: from sage.tests.interrupt import * ## line 165 ##
sage: test_sig_on_cython() ## line 166 ##
KeyboardInterrupt()
sage: sig_on_count() ## line 168 ##
0
sage: from sage.tests.interrupt import * ## line 181 ##
sage: test_sig_on_cython_except() ## line 182 ##
KeyboardInterrupt()
sage: sig_on_count() ## line 184 ##
0
sage: from sage.tests.interrupt import * ## line 197 ##
sage: test_sig_on_cython_except_all() ## line 198 ##
KeyboardInterrupt()
sage: sig_on_count() ## line 200 ##
0
sage: from sage.tests.interrupt import * ## line 209 ##
sage: test_sig_check() ## line 210 ##
KeyboardInterrupt()
sage: sig_on_count() ## line 212 ##
0
sage: from sage.tests.interrupt import * ## line 222 ##
sage: test_sig_check_inside_sig_on() ## line 223 ##
KeyboardInterrupt()
sage: sig_on_count() ## line 225 ##
0
sage: from sage.tests.interrupt import * ## line 235 ##
sage: test_sig_retry() ## line 236 ##
10
sage: sig_on_count() ## line 238 ##
0
sage: from sage.tests.interrupt import * ## line 253 ##
sage: test_sig_retry_and_signal() ## line 254 ##
KeyboardInterrupt()
sage: sig_on_count() ## line 256 ##
0
sage: from sage.tests.interrupt import * ## line 273 ##
sage: test_sig_on_no_except() ## line 274 ##
42
sage: sig_on_count() ## line 276 ##
0
sage: from sage.tests.interrupt import * ## line 301 ##
sage: test_sig_str_no_except() ## line 302 ##
sage: sig_on_count() ## line 306 ##
0
sage: from sage.tests.interrupt import * ## line 324 ##
sage: test_sig_check_no_except() ## line 325 ##
KeyboardInterrupt()
sage: sig_on_count() ## line 327 ##
0
sage: from sage.tests.interrupt import * ## line 342 ##
sage: test_old_sig_off() ## line 343 ##
sage: sig_on_count() ## line 344 ##
0
sage: from sage.tests.interrupt import * ## line 353 ##
sage: test_old_sig_on() ## line 354 ##
KeyboardInterrupt()
sage: sig_on_count() ## line 356 ##
0
sage: from sage.tests.interrupt import * ## line 365 ##
sage: test_old_sig_str() ## line 366 ##
sage: sig_on_count() ## line 370 ##
0
sage: from sage.tests.interrupt import * ## line 383 ##
sage: test_signal_segv() ## line 384 ##
sage: sig_on_count() ## line 388 ##
0
sage: from sage.tests.interrupt import * ## line 397 ##
sage: test_signal_fpe() ## line 398 ##
sage: sig_on_count() ## line 402 ##
0
sage: from sage.tests.interrupt import * ## line 411 ##
sage: test_signal_ill() ## line 412 ##
sage: sig_on_count() ## line 416 ##
0
sage: from sage.tests.interrupt import * ## line 425 ##
sage: test_signal_abrt() ## line 426 ##
sage: sig_on_count() ## line 430 ##
0
sage: from sage.tests.interrupt import * ## line 439 ##
sage: test_signal_bus() ## line 440 ##
sage: sig_on_count() ## line 444 ##
0
sage: from sage.tests.interrupt import * ## line 460 ##
sage: test_dereference_null_pointer() ## line 461 ##

**********************************************************************
```



---

Comment by vbraun created at 2013-03-30 21:26:45

Does the following work? In a Cygwin shell:

```
$ echo > /dev/null
$ ls -l /dev/null
```

or in a windows shell (cmd.exe):

```
C:\> dir > NUL
```



---

Comment by jpflori created at 2013-03-30 21:39:59


```
jp`@`THINKPAD ~
$ echo > /dev/null

jp`@`THINKPAD ~
$ ls -l /dev/null
crw-rw-rw- 1 jp None 1, 3 30 mars  22:37 /dev/null

jp`@`THINKPAD ~
$ 
```

and

```
C:\> dir > NUL

C:\>
```

No errors.


---

Comment by jpflori created at 2013-03-30 21:59:25

On my 64 bits W7, Sage 5.9.beta0:
Replying to [comment:236 kcrisman]:
> sage -t sage/tests/interrupt.pyx  # Killed due to segmentation fault
Same long errors and  segfault as you.
> sage -t sage/tests/cmdline.py  # 1 doctest failed
I used to get a similar one (-6 instead of 0) but it passes now although I don't think anything changed.
> sage -t sage/symbolic/expression.pyx  # 1 doctest failed
Numerical noise.
> sage -t sage/misc/interpreter.py  # 2 doctests failed
Unicode, fixed IIRC.
> sage -t sage/misc/cython.py  # 3 doctests failed
Extension, fixed.
> sage -t sage/parallel/decorate.py  # 1 doctest failed
Same as you.
> sage -t sage/functions/other.py  # 1 doctest failed
Numerical noise.
> sage -t sage/interfaces/rubik.py  # 1 doctest failed
No problem for me.
> sage -t sage/structure/sage_object.pyx  # 1 doctest failed
No problem here.
> sage -t sage/misc/inline_fortran.py  # 3 doctests failed
Extension, fixed.
> sage -t sage/libs/gap/element.pyx  # 1 doctest failed
Same error as you.
> sage -t sage/misc/sage_extension.py  # 10 doctests failed
Unicode, fixed.
> sage -t sage/libs/ecl.pyx  # Killed due to segmentation fault
No problem here.


---

Comment by kcrisman created at 2013-03-31 04:07:07

Replying to [comment:239 jpflori]:
> {{{
> jp`@`THINKPAD ~
> $ echo > /dev/null
> 
> jp`@`THINKPAD ~
> $ ls -l /dev/null
> crw-rw-rw- 1 jp None 1, 3 30 mars  22:37 /dev/null
> 

Yeah, I don't have any problems here either.


---

Comment by kcrisman created at 2013-04-02 01:48:14

Some of these disappeared, sorry for not being more specific.  Here is what is left for me on Win7, if I recall correctly.
> > sage -t sage/tests/interrupt.pyx  # Killed due to segmentation fault
> Same long errors and  segfault as you.
> > sage -t sage/tests/cmdline.py  # 1 doctest failed
> I used to get a similar one (-6 instead of 0) but it passes now although I don't think anything changed.
> > sage -t sage/symbolic/expression.pyx  # 1 doctest failed
> Numerical noise.
> > sage -t sage/parallel/decorate.py  # 1 doctest failed
> Same as you.
> > sage -t sage/functions/other.py  # 1 doctest failed
> Numerical noise.
> > sage -t sage/libs/gap/element.pyx  # 1 doctest failed
> Same error as you.
Unfortunately, repeated rebasing doesn't help that I can't run doctests on XP.  I can run individual doctests and although I get fork errors and rebase messages, they can pass.  But trying to run all of them doesn't work.  I may try the trick at comment:9:ticket:14031 and see if that helps there.


---

Comment by jdemeyer created at 2013-04-03 13:04:02

Please see #14406 for prereq


---

Comment by kcrisman created at 2013-04-03 14:36:06

> > Here is the current status for this ticket, then, in my view.
> >  * Patch to remove `SAGE_PORT=yes` requirement for Cygwin.
> Still needed.
This is #14406, probably will be included soon.
> >    * Related to that, we still get the message about `sqrtl in -lm` outdated math library, which presumably would make things fail if `SAGE_PORT` wasn't set, so we need to somehow fix things so that's not an issue.  What happens on FreeBSD?
> Any updates with what we should do here?  The code for the sqrtl business that David wrote is a little convoluted for me, but perhaps it wouldn't be that hard to change to logl as was suggested above.
Also #14406.
> >  * As Jeroen points out, make sure that we put something in so that we don't use the (current) Sage 4.6 GCC spkg to build on Cygwin.  This could involve making the 4.7.2 spkg standard (I don't believe there is a ticket for this yet, though there is a sage-devel thread reporting a fair amount of success), or something else.
> This is #14378, and Jeroen even has an spkg.
And it's been closed.

----

> >  * Figure out whether mpfr-4 needs to be installed or not.  I now have two different brand-new installs of Cygwin that failed with the current package list until I installed it.  It was _not_ pulled in with gcc-core and friends.
> Looks like it's needed for now, or is there any action on the Cygwin front?
So the sole remaining issue _for this ticket_ is the check for mpfr-4.  What should we do about this?


---

Comment by jpflori created at 2013-04-03 14:55:49

Replying to [comment:244 kcrisman]:
> So the sole remaining issue _for this ticket_ is the check for mpfr-4.  What should we do about this?
I think we should do nothing.
The Cygwin folks seems to be working on a complete overhaul of their GCC packages so we can hope that quite quickly the situation will get better and installing "gcc4-core" will just work as it used to be and as it should be.
It is really a Cygwin packaging issue, not a Sage one, and trusting the Cygwin folk will avoid us the trouble to add a prereq that will soon be obsolete.


---

Comment by kcrisman created at 2013-04-03 15:24:43

> > So the sole remaining issue _for this ticket_ is the check for mpfr-4.  What should we do about this?
> I think we should do nothing.
> The Cygwin folks seems to be working on a complete overhaul of their GCC packages so we can hope that quite quickly the situation will get better and installing "gcc4-core" will just work as it used to be and as it should be.
> It is really a Cygwin packaging issue, not a Sage one, and trusting the Cygwin folk will avoid us the trouble to add a prereq that will soon be obsolete.
How soon is soon?  At any rate, I think that somewhere (maybe not even in prereq) there should be a warning.  In principle, we want someone to be able to download a Sage tarball, open it in Cygwin with the required Sage packages for any distro, and then do "make".  Maybe with some info about rebasing.

Maybe that means that we need to change the _installation guide_ here instead of the prereq!  We would need to provide info about rebasing anyway.  What do you think of that for resolving this ticket?  Then we could put a `..NOTE` to warn about mpfr-4 that could easily be removed.


---

Comment by jpflori created at 2013-04-03 16:37:32

Replying to [comment:246 kcrisman]:
> > > So the sole remaining issue _for this ticket_ is the check for mpfr-4.  What should we do about this?
> > I think we should do nothing.
> > The Cygwin folks seems to be working on a complete overhaul of their GCC packages so we can hope that quite quickly the situation will get better and installing "gcc4-core" will just work as it used to be and as it should be.
> > It is really a Cygwin packaging issue, not a Sage one, and trusting the Cygwin folk will avoid us the trouble to add a prereq that will soon be obsolete.
> How soon is soon?  At any rate, I think that somewhere (maybe not even in prereq) there should be a warning.  In principle, we want someone to be able to download a Sage tarball, open it in Cygwin with the required Sage packages for any distro, and then do "make".  Maybe with some info about rebasing.
> 
> Maybe that means that we need to change the _installation guide_ here instead of the prereq!  We would need to provide info about rebasing anyway.  What do you think of that for resolving this ticket?  Then we could put a `..NOTE` to warn about mpfr-4 that could easily be removed.
I'd say wait, from http://cygwin.com/ml/cygwin/2013-03/msg00116.html:

```
Forget the current gcc packages, they're history.  We're about to
upgrade to 4.7 and we anyways need another rebuild before it goes
stable.  If we ship all the updated prereqs now, each built against the
newest gmp, then 4.7.2-2 can be built against them and we won't have
this problem from here on out.
```

You could argue that you only trust what you see.


---

Comment by jpflori created at 2013-04-03 16:48:04

And I was quite surprised to discover the Cygwin crew seems to be actively working on 64 bits Cygwin:
http://cygwin.com/ml/cygwin-developers/2013-03/msg00008.html


---

Comment by kcrisman created at 2013-04-03 16:52:33

Slight update:
Note that actually we do still need the lapack thing since #10508 isn't in, see #14406 for details on this where JP mentions it.  So that's two issues.
> > > > So the sole remaining issue _for this ticket_ is the check for mpfr-4.  What should we do about this?
> > > I think we should do nothing.
> I'd say wait, from http://cygwin.com/ml/cygwin/2013-03/msg00116.html:
> You could argue that you only trust what you see.
Well, in any case I think that we should put something in the installation guide, since it even mentions AIX but not Cygwin.  I did just update [http://wiki.sagemath.org/SupportedPlatforms](http://wiki.sagemath.org/SupportedPlatforms).


---

Comment by jpflori created at 2013-04-03 17:03:34

Replying to [comment:250 kcrisman]:
> Slight update:
> Note that actually we do still need the lapack thing since #10508 isn't in, see #14406 for details on this where JP mentions it.  So that's two issues.
Please note that the spkg currently provided at #10508 will not build ATLAS on Cygwin by default.
And even if you set SAGE_ATLAS_ARCH as suggested to force the build, it will not work because the magic (or rather circumventing libtool stupidity) needed to build the shared libraries on Cygwin is not included yet and we don't install static libraries.
I don't plan on including any of these changes in #10508 although I think we should include both these changes.
That will be for follow up tickets, #10508 has been bitrotting for too long.
> > > > > So the sole remaining issue _for this ticket_ is the check for mpfr-4.  What should we do about this?
> > > > I think we should do nothing.
> > I'd say wait, from http://cygwin.com/ml/cygwin/2013-03/msg00116.html:
> > You could argue that you only trust what you see.
> Well, in any case I think that we should put something in the installation guide, since it even mentions AIX but not Cygwin.  I did just update [http://wiki.sagemath.org/SupportedPlatforms](http://wiki.sagemath.org/SupportedPlatforms).
Yes and take care of peflags and rebasing scripts and that will be most of it.
And a patchbot would be great, or even three of them at least (XP 32, 7 64 and 8 64 I'd say), preferably not virtual machines, but let's not dream too much.


---

Comment by kcrisman created at 2013-04-03 17:15:54

> > Note that actually we do still need the lapack thing since #10508 isn't in, see #14406 for details on this where JP mentions it.  So that's two issues.
> Please note that the spkg currently provided at #10508 will not build ATLAS on Cygwin by default.
Yes, I realize all this; I was just saying that at least there was a useful error message in some patch/spkg somewhere on that ticket.
> > > > > > So the sole remaining issue _for this ticket_ is the check for mpfr-4.  What should we do about this?
> > > > > I think we should do nothing.
> > Well, in any case I think that we should put something in the installation guide, since it even mentions AIX but not Cygwin.  I did just update [http://wiki.sagemath.org/SupportedPlatforms](http://wiki.sagemath.org/SupportedPlatforms).
> Yes and take care of peflags and rebasing scripts and that will be most of it.
Yes, though those aren't necessary to close this ticket.
> And a patchbot would be great, or even three of them at least (XP 32, 7 64 and 8 64 I'd say), preferably not virtual machines, but let's not dream too much.
Umm, no!  Especially since I can't get testing to even work on XP 32 - presumably because every time I rebase, I get a different problem related to having not enough space.  I wonder if deleting all the dlls in devel/sage/sage/ would work, since the ones in devel/sage/build/ are the ones that are actually (currently) used?


---

Comment by jdemeyer created at 2013-04-03 17:52:08

Replying to [comment:250 kcrisman]:
> I did just update [http://wiki.sagemath.org/SupportedPlatforms](http://wiki.sagemath.org/SupportedPlatforms).
Remember that this is meant for *released versions*, not betas.


---

Comment by kcrisman created at 2013-04-03 17:58:42

No, I didn't realize this.  However, I think Sage 5.8 builds and passes most doctests, so I don't think this was really that wrong.  That said, you can revert it if you need to.


---

Comment by leif created at 2013-04-03 18:03:51

Replying to [comment:253 jdemeyer]:
> Replying to [comment:250 kcrisman]:
> > I did just update [http://wiki.sagemath.org/SupportedPlatforms](http://wiki.sagemath.org/SupportedPlatforms).
> Remember that this is meant for *released versions*, not betas.


  _Dear Sage lovers,_
  
  _We're *releasing* Sage 5.9.*beta2*._

;-)


---

Comment by leif created at 2013-04-03 18:10:06

Replying to [comment:249 jpflori]:
> [...] the Cygwin crew seems to be actively working on 64 bits Cygwin:
> http://cygwin.com/ml/cygwin-developers/2013-03/msg00008.html

So Cygwin will keep you busy for the next few years... B)


---

Comment by jpflori created at 2013-04-04 07:53:02

I've opened #14410 for the ATLAS on Cygwin stuff.


---

Comment by jdemeyer created at 2013-04-04 08:06:12

Replying to [comment:254 kcrisman]:
> No, I didn't realize this.  However, I think Sage 5.8 builds and passes most doctests, so I don't think this was really that wrong.  That said, you can revert it if you need to.
Given that it doesn't even pass prereq on Sage 5.8, I did indeed move that part to "Probably will not work" to avoid confusion.


---

Comment by kcrisman created at 2013-04-04 13:29:21

> > No, I didn't realize this.  However, I think Sage 5.8 builds and passes most doctests, so I don't think this was really that wrong.  That said, you can revert it if you need to.
> Given that it doesn't even pass prereq on Sage 5.8, I did indeed move that part to "Probably will not work" to avoid confusion.
Good point.  I moved it back but with the caveat about `SAGE_PORT`.  Since several of the other things on the "almost works" list need special packages etc., I think that this is ok.


---

Comment by kcrisman created at 2013-04-10 02:41:21

Apply trac_6743-doc.patch for a first attempt at a doc patch.  This would satisfy my concern about libmpfr4 for now (in the meantime, the gcc4 package [apparently has been "orphaned"](http://cygwin.com/ml/cygwin/2013-03/msg00172.html)).

Is the only other issue here #14031?  I sort of assumed that was the case in my patch, but of course that is just a draft and references to those things could be removed.


---

Comment by jpflori created at 2013-04-11 20:31:17

Replying to [comment:260 kcrisman]:
> Apply trac_6743-doc.patch for a first attempt at a doc patch.  This would satisfy my concern about libmpfr4 for now (in the meantime, the gcc4 package [apparently has been "orphaned"](http://cygwin.com/ml/cygwin/2013-03/msg00172.html)).
> 
This is no longer necessary as the cygwin folks finally fixed the gcc 4.5.3 dependencies. See:
* http://cygwin.com/ml/cygwin/2013-04/msg00174.html
* http://cygwin.com/ml/cygwin/2013-04/msg00170.html
and a fresh install of mine has pulled it automatically.
> Is the only other issue here #14031?  I sort of assumed that was the case in my patch, but of course that is just a draft and references to those things could be removed.


---

Comment by kcrisman created at 2013-04-12 01:24:28

So annoying!  I totally waited for a while to do this in the hopes it would happen, and it happens just after I write this.

That said, I still think most of this is worthwhile.  What do you think of this updated patch?


---

Attachment


---

Comment by jdemeyer created at 2013-04-12 07:16:09

Remove the comment about `SAGE_TESTDIR`, that variable isn't used anymore.


---

Comment by jdemeyer created at 2013-04-12 07:18:14

Also mention _how_ one is supposed to run the `sage-rebase_sage.bat` or `sage-rebase_sage.sh` scripts. Something like: open a Sage shell and then type "sage-rebase_sage.sh" or equivalently

```
./sage --sh sage-rebase_sage.sh
```



---

Comment by jpflori created at 2013-04-12 11:52:37

Replying to [comment:252 kcrisman]:
> Umm, no!  Especially since I can't get testing to even work on XP 32 - presumably because every time I rebase, I get a different problem related to having not enough space.  I wonder if deleting all the dlls in devel/sage/sage/ would work, since the ones in devel/sage/build/ are the ones that are actually (currently) used?
FYI I succesfully built Sage on a 32 bits Windows XP (within a virtual machine).
Just had to rebase once to build the doc, and tests can be run fine!


---

Comment by kcrisman created at 2013-04-12 12:43:20

> Remove the comment about SAGE_TESTDIR, that variable isn't used anymore.
Really?  What is the new way to change the test directory?  (This is still necessary at times to avoid spaces, as far as I know.)
> Also mention how one is supposed to run the sage-rebase_sage.bat or sage-rebase_sage.sh scripts. 
I sort of purposely didn't, because I don't know how the bat one works.  Maybe this ticket should depend on #14031?
> FYI I succesfully built Sage on a 32 bits Windows XP (within a virtual machine). Just had to rebase once to build the doc, and tests can be run fine!
Awesome!  I guess my hardware even without a VM is just not powerful enough to avoid the eternal rebase.  It's really weird.  It _is_ an older machine.


---

Comment by jdemeyer created at 2013-04-12 14:52:57

Replying to [comment:266 kcrisman]:
> > Remove the comment about SAGE_TESTDIR, that variable isn't used anymore.
> Really?  What is the new way to change the test directory?
The whole concept of a "test directory" is gone.


---

Comment by jdemeyer created at 2013-04-12 14:56:11

Has anybody ever tried to make a binary Cygwin distribution with the usual command

```
./sage --bdist 5.9.beta5
```



---

Comment by kcrisman created at 2013-04-12 15:01:31

> The whole concept of a "test directory" is gone.
I didn't realize that was part of the change in the doctest framework - I only paid tangential attention to that :(
> Has anybody ever tried to make a binary Cygwin distribution with the usual command
Not yet!  (Or, at least not for quite a while - maybe William knows.)  That would be for another ticket :)


---

Comment by jpflori created at 2013-04-16 09:39:24

Replying to [comment:269 jdemeyer]:
> Has anybody ever tried to make a binary Cygwin distribution with the usual command
> {{{
> ./sage --bdist 5.9.beta5
> }}}
I tried and it seems to have worked fine.
I've not tried to unpack the archive into another Cygwin install yet though.


---

Comment by leif created at 2013-04-16 17:26:19

[SCNR.](http://www.fsf.org/blogs/community/friends-dont-let-friends-use-windows-8)

Should we ship the info graphic with Sage (and display it on Cygwin)? XD


---

Comment by jpflori created at 2013-04-16 20:19:34

Replying to [comment:263 jdemeyer]:
> Remove the comment about `SAGE_TESTDIR`, that variable isn't used anymore.
I've begun working on Karl-Dieter patch and came to the conclusion I'd better clean up much more of source.rst which is quite messy.
So I propose to move that to another ticket and make it a dependency here.


---

Comment by jpflori created at 2013-04-16 21:25:47

Replying to [comment:271 jpflori]:
> Replying to [comment:269 jdemeyer]:
> > Has anybody ever tried to make a binary Cygwin distribution with the usual command
> > {{{
> > ./sage --bdist 5.9.beta5
> > }}}
> I tried and it seems to have worked fine.
> I've not tried to unpack the archive into another Cygwin install yet though.
The archive was produced on 32 bits Windows XP within a virtual machine. 
I've untarred it in another 64 bits Windows 7 still within a virtual machine.
The Cygwin setup is basically the same, which surely explains I had no rebase troubles.
And Sage seems to work fine (I've not run "make ptestlong" though).
I can post the build somewhere if someone is interested but it was built on a recent enough Core i7 so won't be that portable.


---

Comment by jdemeyer created at 2013-04-16 21:39:32

That's super-cool. Any chance for a Cygwin buildbot?


---

Comment by jdemeyer created at 2013-04-16 21:41:19

Replying to [comment:274 jpflori]:

> I can post the build somewhere if someone is interested but it was built on a recent enough Core i7 so won't be that portable.
If you build Sage with `SAGE_FAT_BINARY=yes`, it _should_ work on other processors too (which doesn't mean that it actually _will_, there are surely bugs with `SAGE_FAT_BINARY`).


---

Comment by dimpase created at 2013-04-17 08:37:46

Replying to [comment:275 jdemeyer]:
> That's super-cool. Any chance for a Cygwin buildbot?
in some cases one has to rebase the whole Cygwin installation, and this can't be done from within Cygwin. So this requires more hacks, 
and it is not so clear if this will work well enough.

As a first step towards this one would need to automate rebasing at the time Sage is built. This is already not 100% trivial, as fork errors can manifest themselves in different ways.


---

Comment by jpflori created at 2013-04-17 21:51:34

I've put the updated source.rst patch a #14465.


---

Comment by jdemeyer created at 2013-05-13 20:39:35

Should this ticket be closed or do we want to do that only when there is a Cygwin buildbot?


---

Comment by jpflori created at 2013-05-13 21:24:04

I'd say we can close it.
Of course, it does not really builds completely automatically because you have to rebase sometimes (i had to do that once for 5.8 and 3 times for 5.9) but at least thats documented and we cannot really solve this prolblem in an easy way without hacking the build system.


---

Comment by jdemeyer created at 2013-05-22 12:30:20

Resolution: fixed
