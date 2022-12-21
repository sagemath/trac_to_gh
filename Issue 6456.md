# Issue 6456: Upgrade cvxopt in sage from 0.9 to 1.1.1

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-01 21:02:23

Assignee: mabshoff

We are shipping an *ancient* version of cvxopt in sage.  It's worse than Debian shipping sage-3.0.5!

Note that upgrading cvxopt should be fairly easy, since basically nothing in Sage depends on cvxopt.


---

Comment by wdj created at 2009-07-01 23:22:38

Fly in the ointment: The recent version has this statement on its license page http://abel.ee.ucla.edu/cvxopt/copyright.html:


```
CVXOPT is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
```

Older versions apparently did not have that.


---

Comment by schilly created at 2010-01-26 12:47:15

I've recently upgraded it for me to 1.1.2. The problem is, that the sources from them did not compile on my ubuntu 9.10 machine. So I went to the [ubuntu packges db for lucid](http://packages.ubuntu.com/lucid/python-cvxopt) and grabbed their version. I don't know what they did in their patch, but I guess it's non trivial...

My spkg is [here](http://boxen.math.washington.edu/home/schilly/sage/spkg/).

The only remaining modification I had to made to run the examples from the cvxopt website in `%python` mode was to replace 


```
from random import ...
```

to

```
from sage.misc.prandom import ...
```

in `./src/src/python/__init__.py` at several places.

*Q:*

 1. what's the usual/best mechanism to avoid using Sage's `random` and switch back to python's random?!
 1. i have no idea what the solaris patches did in the older version, neither do i know how to get it building on another system :(


---

Comment by schilly created at 2010-01-27 13:13:41

I've created an updated p1 spkg.

Using the 1.1.2 sources directly, I get this error `site-packages/cvxopt/base.so: undefined symbol: _g95_stop_blank` ... I also fiddled around with the setup.py file.

[cvxopt 1.1.2 p1 spkg is here](http://boxen.math.washington.edu/home/schilly/sage/spkg/)


---

Comment by mvngu created at 2010-02-02 07:15:08

Ticket #1620 is a duplicate of this one.


---

Comment by dimpase created at 2010-02-04 10:33:38

Changing status from new to needs_work.


---

Comment by dimpase created at 2010-02-04 10:33:38

Replying to [comment:3 schilly]:
> I've created an updated p1 spkg.
> 
> Using the 1.1.2 sources directly, I get this error `site-packages/cvxopt/base.so: undefined symbol: _g95_stop_blank` ... I also fiddled around with the setup.py file.
> 
> [cvxopt 1.1.2 p1 spkg is here](http://boxen.math.washington.edu/home/schilly/sage/spkg/)
sage -t  "devel/sage-work/sage/numerical/optimize.py"

bumps out essentially due to:

```

sage: from cvxopt import cholmod
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/dima/sage/devel/sage-work/sage/<ipython console> in <module>()

ImportError: /home/dima/sage/local/lib/python2.6/site-packages/cvxopt/cholmod.so: undefined symbol: _g95_filename
sage: 
```


Can you reproduce this on a stand-alone build of cvxopt?


---

Attachment

patch for cvxopt-1.1.2.p1/src/src/setup.py


---

Comment by dimpase created at 2010-02-04 16:25:55

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2010-02-04 16:25:55

Replying to [comment:3 schilly]:
> I've created an updated p1 spkg.
> 
> Using the 1.1.2 sources directly, I get this error `site-packages/cvxopt/base.so: undefined symbol: _g95_stop_blank` ... I also fiddled around with the setup.py file.
> 
> [cvxopt 1.1.2 p1 spkg is here](http://boxen.math.washington.edu/home/schilly/sage/spkg/)

please check the patch I just uploaded. It fixes this problem;
you just had to link against more dynamic libs...


---

Comment by schilly created at 2010-02-04 17:03:47

Replying to [comment:6 dimpase]:

> please check the patch I just uploaded. It fixes this problem; you just had to link against more dynamic libs...

Thanks, I knew that it is something with that! Works now!!! ;) 

I've uploaded [1.1.1.p2 here](http://boxen.math.washington.edu/home/schilly/sage/spkg/)

Next I'll try if using the debian/ubuntu version of it was really necessary.

For everyone who wants to try this, don't forget that you have to disable the preparser in Sage via `preparser(False)` ... otherwise there are unknown types when you try to create a matrix with cvxopt's matrix command.


---

Comment by dimpase created at 2010-02-05 05:31:51

Replying to [comment:7 schilly]:

> I've uploaded [1.1.1.p2 here](http://boxen.math.washington.edu/home/schilly/sage/spkg/)
> 
> Next I'll try if using the debian/ubuntu version of it was really necessary.
> 
please take out f77blas all over in setup.py, for this is apparently obsolete and not needed - and also nukes the installation on Mac OS X (ppc) -- (otherwise it works on the latter platform)


---

Comment by dimpase created at 2010-02-05 05:31:51

Changing status from needs_review to needs_work.


---

Comment by dimpase created at 2010-02-15 13:51:50

Replying to [comment:7 schilly]:


I think that really what remains to be done is to remove dependencies on 
obsolete fortrans (f77), see my other comment on this.
Let's get it done!


> Replying to [comment:6 dimpase]:
> 
> > please check the patch I just uploaded. It fixes this problem; you just had to link against more dynamic libs...
> 
> Thanks, I knew that it is something with that! Works now!!! ;) 
> 
> I've uploaded [1.1.1.p2 here](http://boxen.math.washington.edu/home/schilly/sage/spkg/)
> 
> Next I'll try if using the debian/ubuntu version of it was really necessary.

I don't see a necessity to try non-debian/ubunty version.
If you look at the debian patches, you see that all they changed is the source
were slight tweaks in setup.py

> 
> For everyone who wants to try this, don't forget that you have to disable the preparser in Sage via `preparser(False)` ... otherwise there are unknown types when you try to create a matrix with cvxopt's matrix command.

Does this mean that we should think of importing cvxopt's matrix into Sage under some other name? I don't know what the usual Sage's way to deal with such things, i.e. name clashes between packages, is.


---

Comment by drkirkby created at 2010-02-16 12:36:01

* Have the license issue been resolved? 
 * Has this been tested on Solaris?


---

Comment by dimpase created at 2010-02-16 13:21:59

Replying to [comment:10 drkirkby]:
>  * Have the license issue been resolved? 

it is GPL v3 or later. Does it matter?
I suppose I can ask the authors to tweak it, if it is really necessary. 

>  * Has this been tested on Solaris? 

no, but I can try on one of Skynet's machines (perhaps you can tell me which 
one is most likely to work :)), or you can try it yourself.
(I don't have a ready Solaris install anywhere).


---

Comment by drkirkby created at 2010-02-16 16:04:48

You better check the license issue with William. Code should be GPL 2 or GPL2+, but there are exceptions if a package is optional and some other conditions - I've never fully understood  under what conditions code can be GLP 3. But you might find you can only use the latest version which is GPL 2, and not a GPL 3 version. 


```
sage: license()
```


says all code except jsmath is GPL2, and apparently jsmath is ok, as Sage does not link to it. 

The code will not build on skynet, as there are no SPARC machines there. It should build it on 't2' easily though. 

I suggest you download sage 4.3.0.1 from one of the mirrors

http://www.sagemath.org/download-solaris.html

Use the following settings. 


```
kirkby`@`t2:[~] $ echo $PATH
/usr/local/gcc-4.4.1-sun-linker/bin:/usr/local/bin2:/usr/bin:/usr/ccs/bin:/usr/local/bin:/usr/sfw/bin:/bin:/usr/sbin
kirkby`@`t2:[~] $ echo $LD_LIBRARY_PATH
/usr/local/gcc-4.4.1-sun-linker/lib:=/usr/local/gcc-4.4.1-sun-linker/lib/sparcv9:/usr/local/lib
```


type make, and build Sage, then try your package. 

There is also a binary of Sage on the mirrors. You could download that. I'm not precisely sure what you then need to do to build just your package using the binary as a starting point. 

The latest Sage source will not build on Solaris, but 4.3.0.1 will. 

Dave


---

Comment by dimpase created at 2010-02-16 19:20:07

Replying to [comment:12 drkirkby]:
> You better check the license issue with William. Code should be GPL 2 or GPL2+, but there are exceptions if a package is optional and some other conditions - I've never fully understood  under what conditions code can be GLP 3. But you might find you can only use the latest version which is GPL 2, and not a GPL 3 version. 


Well, cvxopt is an optional package, so it must be in the same boat as jmath,
or some gap packages, that are also not GPL 2.


> 
> {{{
> sage: license()
> }}}
> 
> says all code except jsmath is GPL2, and apparently jsmath is ok, as Sage does not link to it. 
> 
> The code will not build on skynet, as there are no SPARC machines there. It should build it on 't2' easily though. 
> 

hmm, isn't this a sparc/solaris?

SunOS mark2 5.10 Generic_127111-01 sun4u sparc SUNW,Sun-Blade-2500

Dima


---

Comment by drkirkby created at 2010-02-16 20:45:01

Replying to [comment:13 dimpase]:
> Replying to [comment:12 drkirkby]:
> > You better check the license issue with William. Code should be GPL 2 or GPL2+, but there are exceptions if a package is optional and some other conditions - I've never fully understood  under what conditions code can be GLP 3. But you might find you can only use the latest version which is GPL 2, and not a GPL 3 version. 
> 
> 
> Well, cvxopt is an optional package, so it must be in the same boat as jmath,
> or some gap packages, that are also not GPL 2.

Fair enough. 

> > 
> > {{{
> > sage: license()
> > }}}
> > 
> > says all code except jsmath is GPL2, and apparently jsmath is ok, as Sage does not link to it. 
> > 
> > The code will not build on skynet, as there are no SPARC machines there. It should build it on 't2' easily though. 
> > 
> 
> hmm, isn't this a sparc/solaris?
> 
> SunOS mark2 5.10 Generic_127111-01 sun4u sparc SUNW,Sun-Blade-2500
> 
> Dima

Yes, it is. Sorry, I was not aware of the existance of that machine. 

However, I do not know how the compilers and paths are configured on that machine. You need to have GNU make & GNU tar in your path before the Sun ones, and you need to have the Sun linker (/usr/ccs/bin/ld) in your path before any GNU ones. There are some general instructions on building Sage on Solaris at http://wiki.sagemath.org/solaris which you would need to follow. 

I've written some somewhat simpler instructions at http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2 on how to build Sage on 't2'. They are simpler, as I have already put the right tools in the right locations. 

The Sun Blade 2500 (mark2) should be quicker than the T5240 (t2) at building Sage. However it would require some setting up of the build environment to build Sage. If you just want an easy solution, 't2' will just work, albeit not as quickly as the Sun Blade 2500. 

Dave


---

Comment by dimpase created at 2010-02-16 21:18:45

Replying to [comment:14 drkirkby]:

> > hmm, isn't this a sparc/solaris?
> > 
> > SunOS mark2 5.10 Generic_127111-01 sun4u sparc SUNW,Sun-Blade-2500
> > 
> > Dima
> 
> Yes, it is. Sorry, I was not aware of the existance of that machine. 
> 
> However, I do not know how the compilers and paths are configured on that machine. You need to have GNU make & GNU tar in your path before the Sun ones, and you need to have the Sun linker (/usr/ccs/bin/ld) in your path before any GNU ones. There are some general instructions on building Sage on Solaris at http://wiki.sagemath.org/solaris which you would need to follow. 

well, on Skynet there is /usr/local/skynet_bash_profile 
that you can source upon login (from .bashrc, or just manually), 
and this gives you the ready setup to build Sage.

I don't have an account on t2, it seems to me.
By the way, absent-mindedly I started building 4.3.3.alpha on there,
and it went till gnutls, where it stopped... I noticed that gnutls is over 2 years old, version 2.2.2, whereas the current one is 2.8.5. Shouldn't one upgrade to this one, before even trying to fix this?


Dima


---

Comment by dimpase created at 2010-02-16 21:32:48

Replying to [comment:12 drkirkby]:
> You better check the license issue with William. Code should be GPL 2 or GPL2+, but there are exceptions if a package is optional and some other conditions - I've never fully understood  under what conditions code can be GLP 3. But you might find you can only use the latest version which is GPL 2, and not a GPL 3 version. 

I emailed William about this, and he said it's OK in this case, it can be v3.


---

Comment by drkirkby created at 2010-02-16 22:20:03

Replying to [comment:15 dimpase]:
> Replying to [comment:14 drkirkby]: 
> > However, I do not know how the compilers and paths are configured on that machine. You need to have GNU make & GNU tar in your path before the Sun ones, and you need to have the Sun linker (/usr/ccs/bin/ld) in your path before any GNU ones. There are some general instructions on building Sage on Solaris at http://wiki.sagemath.org/solaris which you would need to follow. 
> 
> well, on Skynet there is /usr/local/skynet_bash_profile 
> that you can source upon login (from .bashrc, or just manually), 
> and this gives you the ready setup to build Sage.

I'm not however aware of anyone building Sage on there recently, so I don't know if the environment is set up suitably. Quite a few Solaris-specific changes have been made in the last year, and some of them might not be compatible with the build system on there. I don't know. Specifically, if 

```
gcc -v 
```


shows gcc was configured with the GNU linker, then the GNU linker must be in your path before the Sun linker. (Basically, whatever linker gcc uses, must be in your path first, as some code makes the assumption the first linker in your path is the one gcc uses, which might not be true.) I'm not aware of a foolproof test of this.

There should be something like 


```
--with-ld=/usr/ccs/bin/ld
```

if the Sun linker was used, or 

```
--with-ld=/path/to/gnu/ld
```

if the GNU linker was used. 

Certainly, I've never had a problem with gnutls failing on 't2'. 
 
> I don't have an account on t2, it seems to me.

I've emailed William to ask if you can have an account on t2, as that might be the simplest solution, though that Blade 2500 would be significantly faster than 't2'. 

> By the way, absent-mindedly I started building 4.3.3.alpha on there,
> and it went till gnutls, where it stopped... I noticed that gnutls is over 2 years old, version 2.2.2, whereas the current one is 2.8.5. Shouldn't one upgrade to this one, before even trying to fix this?
> 
> Dima

I can see your point about upgrading, though I'm not aware of any particular issues with the version in Sage. That version will build on Solaris. You could try appending /usr/sfw/lib to your LD_LIBRARY_PATH. I have known of issues with gnutls on OpenSolaris, but not on Solaris 10. 

I see your post about the GPL 3. That bit is sorted out then. 

Dave


---

Comment by dimpase created at 2010-03-18 15:58:18

Replying to [comment:8 dimpase]:

> Replying to [comment:7 schilly]:
>
Here is an updated version, that also works on Solaris (this needed copying sun_complex.h from old cvxopt-0.9
and patching cvxopt.h). I also turned on building GSL-extension (by turning on the appropriate option in setup.py, 
and supplying right include and lib-paths)
  
[http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.2.p3.spkg](http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.2.p3.spkg)


---

Comment by dimpase created at 2010-03-18 15:58:18

Changing status from needs_work to needs_review.


---

Comment by schilly created at 2010-03-18 18:05:34

hi, great work, your 1.1.2.p3.spkg works for me on intel core2 duo with ubuntu 9.04 running 4.3.4.rc0.

It's just that the name shouldn't have the .p3, the SPKG.txt is not correct (your name missing), the patches aren't yours but still mine and there is no mention what you have really done with the *.h files for solaris. where is a good page to read about the spkg policies?!?


---

Comment by schilly created at 2010-03-18 18:05:34

Changing status from needs_review to needs_work.


---

Comment by dimpase created at 2010-03-24 16:04:04

Replying to [comment:19 schilly]:
> hi, great work, your 1.1.2.p3.spkg works for me on intel core2 duo with ubuntu 9.04 running 4.3.4.rc0.
> 
> It's just that the name shouldn't have the .p3, the SPKG.txt is not correct (your name missing), the patches aren't yours but still mine and there is no mention what you have really done with the *.h files for solaris. where is a good page to read about the spkg policies?!?

OK, finally here comes an update:
[http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.2.spkg](http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.2.spkg)

Fixed SPKG.txt, added all the patches in patches/,  further changes as we discussed by email (see SPKG.txt).
Tested (with Sage 4.3.4) on Linux x86 and x86_64, Solaris (t2) and on MacOSX 10.5 PPC (G4)


---

Comment by dimpase created at 2010-03-24 16:04:04

Changing status from needs_work to needs_review.


---

Comment by schilly created at 2010-03-24 16:50:49

Replying to [comment:20 dimpase]:
> Fixed SPKG.txt

spkg works for me on ubuntu 9.04, intel core2 duo and sage 4.3.4. I've just further cleaned up the SPKG.txt file since only the net changes are relevant and now there is also a title plus a description.

final spkg is [here](http://boxen.math.washington.edu/home/schilly/sage/spkg/)


---

Comment by dimpase created at 2010-03-24 18:09:08

Replying to [comment:21 schilly]:
> Replying to [comment:20 dimpase]:
> > Fixed SPKG.txt
> 
> spkg works for me on ubuntu 9.04, intel core2 duo and sage 4.3.4. I've just further cleaned up the SPKG.txt file since only the net changes are relevant and now there is also a title plus a description.
> 
> final spkg is [here](http://boxen.math.washington.edu/home/schilly/sage/spkg/)

OK, great, thanks! How do we finalise this? Should I make myself the owner? Should I make you (and/or myself?) the author?


---

Comment by schilly created at 2010-03-24 18:33:48

Replying to [comment:22 dimpase]:
> OK, great, thanks! How do we finalise this? Should I make myself the owner? Should I make you (and/or myself?) the author?

Uhm, we both are the authors and well, we need a thrid party to give us a positive review ;)


---

Comment by ncohen created at 2010-03-25 16:25:56

Hello !!!

This patch applies, the spkg compiles fine and is well built, everything runs in the end and the doctest using it passes !!!

The only trouble I could find is the need to disable the preparser (mentionned by Harald earlier) to use regular CVXOPT scripts in Sage, but this is not new and could be adressed later. Clearly, this is an improvement for Sage :-)

Thank you for your work !!!

Nathann

P.S. : what would you think of creating another ticket to add a line about this perparsing bug somewhere there : http://www.sagemath.org/doc/numerical_sage/cvxopt.html ?


---

Comment by ncohen created at 2010-03-25 16:25:56

Changing status from needs_review to positive_review.


---

Comment by schilly created at 2010-03-25 18:10:07

Replying to [comment:24 ncohen]:
> P.S. : what would you think of creating another ticket to add a line about this perparsing bug somewhere there : http://www.sagemath.org/doc/numerical_sage/cvxopt.html ?

That's not a bug, the examples in that tutorial redefine `Integer` as `int` and similar workarounds. I prefer disabling the preparser or switching to pure python mode. However, maybe this could be done automatically somehow (as with numpy arrays?) but that's not the scope of this ticket.


---

Comment by schilly created at 2010-03-28 19:58:55

trival changes to the cvxopt chapter in the numerical sage tutorial


---

Attachment

Any ideas why the new spkg is so much smaller than the old one?

```
-rw-r--r-- 1 palmieri palmieri 2463336 2010-02-11 08:56 spkg/standard/cvxopt-0.9.p8.spkg
-rw-r--r-- 1 palmieri palmieri  733213 2010-03-24 09:49 spkg/standard/cvxopt-1.1.2.spkg
```



---

Comment by schilly created at 2010-04-19 22:09:24

Replying to [comment:26 jhpalmieri]:
> Any ideas why the new spkg is so much smaller than the old one?

iirc we have removed documentation and examples. They are not exposed in any way or not used at all (tex sources).


---

Comment by mhansen created at 2010-04-28 06:39:16

Changing status from positive_review to needs_work.


---

Comment by mhansen created at 2010-04-28 06:39:16

I don't think this is ready to go in.  Some issues:

1. I don't think there should be a patches-old directory.  If people need them for historical reasons, then they should get them from the hg repo since that's what it is there for.

2. Files are modified in place in the src/ directory.  That should be as close to clean as vanilla upstream as possible.  The modified files should be copied over from patches/

3. In the patches directory, the patches should be unified diffs (diff -Naur).

4. In spkg-install, you should just remove the old, unnecessary code instead of just commenting it out.  Also, I don't think the SAGE_LOCAL check is necessary.


---

Comment by dimpase created at 2010-04-28 07:06:25

Replying to [comment:28 mhansen]:
> I don't think this is ready to go in.  Some issues:
> 
> 1. I don't think there should be a patches-old directory.  If people need them for historical reasons, then they should get them from the hg repo since that's what it is there for.

OK, this is clear. We need to check if we didn't nuke the old .hg/,
and put it back, if necessary. 

> 
> 2. Files are modified in place in the src/ directory.  That should be as close to clean as vanilla upstream as possible.  The modified files should be copied over from patches/

OK, this is clear too (although this seems to be against the historic way cvxopt spkg was created)

> 
> 3. In the patches directory, the patches should be unified diffs (diff -Naur).

I don't get this. Are you saying that patches cannot be just files that are ready to be copied, that they must be diffs, and the spkg-install must be patching rather than copying?


> 
> 4. In spkg-install, you should just remove the old, unnecessary code instead of just commenting it out.  Also, I don't think the SAGE_LOCAL check is necessary.

we'll see.


---

Comment by mhansen created at 2010-04-28 07:11:32

Replying to [comment:29 dimpase]:
> I don't get this. Are you saying that patches cannot be just files that are ready to be copied, that they must be diffs, and the spkg-install must be patching rather than copying?

You should have both the patched file and the diff in the patches/ directory.  The diff is useful when upgrading the spkg.


---

Comment by dimpase created at 2010-04-28 07:15:56

Replying to [comment:30 mhansen]:
> Replying to [comment:29 dimpase]:
> > I don't get this. Are you saying that patches cannot be just files that are ready to be copied, that they must be diffs, and the spkg-install must be patching rather than copying?
> 
> You should have both the patched file and the diff in the patches/ directory.  The diff is useful when upgrading the spkg.

This seems to be an unnecessary duplication of information. The diffs can be trivially created, if needed.


---

Comment by mhansen created at 2010-05-25 00:12:49

Replying to [comment:31 dimpase]:
> This seems to be an unnecessary duplication of information. The diffs can be trivially created, if needed.

They can be recreated if you have the correct version of the source from which the patched file was created.  It's easier if the actual diff is in the version control.


---

Comment by dimpase created at 2010-07-15 21:56:46

Replying to [comment:32 mhansen]:
> Replying to [comment:31 dimpase]:
> > This seems to be an unnecessary duplication of information. The diffs can be trivially created, if needed.
> 
> They can be recreated if you have the correct version of the source from which the patched file was created.  It's easier if the actual diff is in the version control.

I should have time next week to fix this, finally...
Dima


---

Comment by mhansen created at 2010-07-17 18:30:29

There is also the issue at #9525 which needs to be taken care of.


---

Attachment

Check for errors while installing cvxopt. Note there is still no spkg-check file. That may or may not be useful - it depends on the source code whether it supports tests.


---

Comment by dimpase created at 2010-07-26 14:59:01

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2010-07-26 14:59:01

Replying to [comment:28 mhansen]:
> I don't think this is ready to go in.  Some issues:
> 
> 1. I don't think there should be a patches-old directory.  If people need them for historical reasons, then they should get them from the hg repo since that's what it is there for.
> 
> 2. Files are modified in place in the src/ directory.  That should be as close to clean as vanilla upstream as possible.  The modified files should be copied over from patches/
> 
> 3. In the patches directory, the patches should be unified diffs (diff -Naur).
> 
> 4. In spkg-install, you should just remove the old, unnecessary code instead of just commenting it out.  Also, I don't think the SAGE_LOCAL check is necessary.

the update, that takes your comments into account, is here
http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.2.spkg

Please have a look, hopefully it is OK now.
Dima


---

Comment by dunfield created at 2010-07-26 15:15:20

This ticket should be coordinated with #9598, which adds GLPK support to cvxopt.


---

Comment by schilly created at 2010-07-26 15:28:04

spkg looks fine for me, builds and also solves some randomly choosen example from the user guide. additionally, i tested if my patch for the documentation `6456-numerical_sage_cvxopt.patch` still works and yes, it does.

regarding glpk, Dima are you able to enable the glpk flag and try building it? if it works i can test it again and see if that's fine - if it doesn't build and you run into bigger problems, we should finally update this spkg anyways and postpone glpk support in cvxopt.


---

Comment by dunfield created at 2010-07-26 15:30:38

Replying to [comment:37 schilly]:
> regarding glpk, Dima are you able to enable the glpk flag and try building it? if it works i can test it again and see if that's fine - if it doesn't build and you run into bigger problems, we should finally update this spkg anyways and postpone glpk support in cvxopt.

There's a patch for glpk for the old cvxopt 0.9 at #9598.   The changes there should work find for cvxopt 1.1 as well.


---

Comment by drkirkby created at 2010-07-26 15:33:50

Looking in 


```
cvxopt-1.1.2/src
```


I see 


```
drwxr-xr-x   3 drkirkby staff          5 Mar 24 11:40 cvxopt-1.1.2
lrwxrwxrwx   1 drkirkby staff         16 Jul 26 16:10 src -> cvxopt-1.1.2/src
```


It is certainly unusual to do this. Normally the top level src directory contains the source, not another directory with a link like this. I know of no other package like this. 

I'm also puzzled why we have this:


```
# Solaris-specific patches
cp -p patches/sun_complex.h src/src/C/
cp -p patches/cvxopt.h src/src/C/
```


There is no file `src/src/C/sun_complex.h` so the first line just creates copies the file `/usr/include/complex.h` from Solaris to the patches directory. That file is from Sun, and its doubtful we can legally distribute `/usr/include/complex.h`

The second patch, patches/cvxopt.h differs from src/src/C/cvxopt.h by very little. A diff shows:


```
drkirkby`@`hawk:~/sage-4.5.2.alpha0/spkg/optional/cvxopt-1.1.2$ diff -u src/src/C/cvxopt.h patches/cvxopt.h
--- src/src/C/cvxopt.h	Mon Jul 26 11:16:09 2010
+++ patches/cvxopt.h	Mon Jul 26 10:58:48 2010
`@``@` -26,7 +26,14 `@``@`
 /* ANSI99 complex is disabled during build of CHOLMOD */
 
 #ifndef NO_ANSI99_COMPLEX
+
+/* work around Solaris 10 specific problem in complex.h */
+#if defined (__sun)
+#include "sun_complex.h"
+#else
 #include "complex.h"
+#endif
+
 #define MAT_BUFZ(O)  ((complex *)((matrix *)O)->buffer)
 #endif
```


If I'm not mistaken, all these two patches achieve is to  

 * Add a file `/usr/include/complex.h` to Sage taken from Solaris, that it is doubtful we can legally include, though I doubt Sun (now Oracle) will complain. 
 * Change a file `patches/cvxopt.h` to include the file we have just illegally copied. 

It would to me at least be a lot easier to just change the second file so it had


```
#ifdef if defined __sun /* Need to check if that's the best one */ 
#include <complex.h>
#endif
```


Why are we bothering to copy a system file from Solaris, rather than just not use `#include <complex.h>`?

Dave


---

Comment by drkirkby created at 2010-07-26 15:37:41

I should add, `/usr/include/complex.h` is included in the first release of Solaris 10 (released in March 2005) and also in the latest OpenSolaris build. There seems little point in doing what we are doing, espeically given it is doubtful if this is legal - the header is not released under the GPL. 


Dave


---

Comment by schilly created at 2010-07-26 15:40:34

Replying to [comment:39 drkirkby]:
> Why are we bothering to copy a system file from Solaris, rather than just not use `#include <complex.h>`?

Because that's the way it was done in 0.9 and nobody of us knows about this in such a detail.


---

Comment by dimpase created at 2010-07-26 16:00:19

Replying to [comment:36 dunfield]:
> This ticket should be coordinated with #9598, which adds GLPK support to cvxopt.
please see

http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.2.p1.spkg

This incorporates the #9598 in 1.1.2.
Only tested on Linux Debian 32bit.
I won't be having much internet until after tomorrow.

Dima


---

Comment by schilly created at 2010-07-26 16:16:16

Replying to [comment:42 dimpase]:
> This incorporates the #9598 in 1.1.2.

I tested it again and also tried to use glpk as an lp solver and it worked:


```
sage: from cvxopt import matrix, solvers
sage: c = matrix([-4., -5.])
sage: G = matrix([[2., 1., -1., 0.], [1., 2., 0., -1.]])
sage: h = matrix([3., 3., 0., 0.])
sage: sol = solvers.lp(c, G, h, solver='glpk')
GLPK Simplex Optimizer, v4.44
4 rows, 2 columns, 6 non-zeros
Preprocessing...
2 rows, 2 columns, 4 non-zeros
Scaling...
 A: min|aij| =  1.000e+00  max|aij| =  2.000e+00  ratio =  2.000e+00
Problem data seem to be well scaled
Constructing initial basis...
Size of triangular part = 2
*     0: obj =   0.000000000e+00  infeas =  0.000e+00 (0)
*     2: obj =  -9.000000000e+00  infeas =  0.000e+00 (0)
OPTIMAL SOLUTION FOUND
```


----

dear release manager, please don't forget to include GLPL as a dependency for cvxopt in the spkg/standard/deps file according to [this comment](http://trac.sagemath.org/sage_trac/ticket/9598#comment:3).


---

Comment by dunfield created at 2010-07-26 16:20:14

> This incorporates the #9598 in 1.1.2.
> Only tested on Linux Debian 32bit.

Works fine on OS X Leopard, used same test as shilly above.


---

Comment by drkirkby created at 2010-07-26 17:45:40

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-07-26 17:45:40

Are you sure its a good idea to merge the changes from #9598? IMHO, it would be better to make these tickets separate, as:

 * #9598 has not been tested properly. 
 * There is no documentation for the updates, so nothing to indicate that cvxopt can be used with the glpk solver.
 * There are no additional doc tests which show the output of using cvxopt with the glpk solver. 
 * The author does not know if it's platform dependent or not, and says he has only checked on OS X. 

I've marked #9598 as needs work, as based on what I deduce, it does need work before being what I personally consider acceptable. 

Dave


---

Comment by drkirkby created at 2010-07-26 18:18:23

Replying to [comment:27 schilly]:
> Replying to [comment:26 jhpalmieri]:
> > Any ideas why the new spkg is so much smaller than the old one?
> 
> iirc we have removed documentation and examples. They are not exposed in any way or not used at all (tex sources).

I don't think that was such a good idea, as the documentation and the examples can be used to test the package. To quote from the `INSTALL` file. 


```
Test it:
--------
To test that the installation was successful, go to the examples
directory and try one of the examples, for example,

    $ cd examples/doc/chap8
    $ python lp
```


So if a spkg-check file was created, whilst leaving the documentation and examples in place, it would be possible to check this. 

Given there is only one .spkg which will be merged in 4.5.2, would it not be better to work on this a bit more? I can see some obvious things that could be improved. 

 * Put back the examples and documentation. 
 * Add an spkg-check file and test the examples - this will only happen if SAGE_CHECK=yes
 * Try removing all the Solaris specific patches. I just did a *very* quick test on an OpenSolaris machine, and found this built without those patches. 
 * Change the directory structure to what is standard in Sage, and not as it is now. 
 * Remove the patches from #9598, which IMHO have not been checked carefully. 

I'll leave it up to you guys how you resolve it. If you want me to make a package based on that above, I'd be willing to do it. 

Dave


---

Comment by dunfield created at 2010-07-26 19:45:47

Over at #9598, I just uploaded a change in the Sage docs of cvxopt which includes shilly's test of the glpk side.  I also changed the URL for the original cvxopt docs; the current link is broken.


---

Comment by dimpase created at 2010-07-27 11:12:47

Replying to [comment:45 drkirkby]:
> Are you sure its a good idea to merge the changes from #9598? IMHO, it would be better to make these tickets separate, as:

Dave, it's just the question of turning a particular interface on.
There should be no problems --- most of all cause there is 0 exposure of
this to any Sage code at the moment.

The next step would be to have a proper test for this somewhere...

> 
>  * #9598 has not been tested properly. 
>  * There is no documentation for the updates, so nothing to indicate that cvxopt can be used with the glpk solver.
>  * There are no additional doc tests which show the output of using cvxopt with the glpk solver. 
>  * The author does not know if it's platform dependent or not, and says he has only checked on OS X. 
> 
> I've marked #9598 as needs work, as based on what I deduce, it does need work before being what I personally consider acceptable. 
> 
> Dave 
>


---

Comment by drkirkby created at 2010-07-27 11:50:16

Replying to [comment:48 dimpase]:
> Replying to [comment:45 drkirkby]:
> > Are you sure its a good idea to merge the changes from #9598? IMHO, it would be better to make these tickets separate, as:
> 
> Dave, it's just the question of turning a particular interface on.
> There should be no problems --- most of all cause there is 0 exposure of
> this to any Sage code at the moment.
> 
> The next step would be to have a proper test for this somewhere...

But my understanding is that there should be a test, so code like that in #9598 can't be committed until there is a test and documentation for it - I note that some documentation has now been added, though I'm not sure about test code. It does not seem right to me to link to a library when

* Whether the linking on some platforms is untested.
* The is no documentation to cvxopt to show how to use this library.
* There is no test code. 

(That was the situation at the time I marked it as needing work - that may have changed now). 

Note also that cvxopt does have test code, which is not executed. Since that was not before, I'm not suggesting that should be made conditional on getting a positive review. But given this ticket will not be merged in 4.5.2 (as only one .spkg file will be), it would seem wise to sort out that too, and run the package's self-tests. That would mean restoring the documentation and examples, as that is how this code gets tested. 

Sorry if I appear too pedantic, but I'm just trying to ensure that what we have works on all platforms, is tested on all platforms, and is documented properly. 

Dave


---

Attachment

6456-freebsd-spkg-install.patch adds support for FreeBSD (this is a port of the patch in #9601).  I have compile-tested this but not yet tried to use the resultant module.

Note that further changes are necessary for cvxopt-1.1.2.p1.spkg to work on most 64-bit OSs.
Compiling in FreeBSD/amd64 (with or without the above patch) gives:

```
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/mnt/sage-4.5/local/include -fPIC -DDLONG= -I/mnt/sage-4.5/local/include/python2.6 -c C/misc_solvers.c -o build/temp.freebsd-8.1-PRERELEASE-amd64-2.6/C/misc_solvers.o
C/misc_solvers.c: In function 'scale':
C/misc_solvers.c:152:13: warning: passing argument 1 of 'dscal_' from incompatible pointer type
C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:152:13: warning: passing argument 4 of 'dscal_' from incompatible pointer type
C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:155:13: warning: passing argument 3 of 'dgemv_' from incompatible pointer type
C/misc_solvers.c:39:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:156:9: warning: passing argument 1 of 'dscal_' from incompatible pointer type
C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:156:9: warning: passing argument 4 of 'dscal_' from incompatible pointer type
C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:158:13: warning: passing argument 2 of 'dger_' from incompatible pointer type
C/misc_solvers.c:41:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:160:13: warning: passing argument 1 of 'dscal_' from incompatible pointer type
C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:160:13: warning: passing argument 4 of 'dscal_' from incompatible pointer type
C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c: In function 'pack2':
C/misc_solvers.c:459:17: warning: passing argument 3 of 'dlacpy_' from incompatible pointer type
C/misc_solvers.c:49:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:459:17: warning: passing argument 5 of 'dlacpy_' from incompatible pointer type
C/misc_solvers.c:49:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:461:17: warning: passing argument 1 of 'dscal_' from incompatible pointer type
C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:463:17: warning: passing argument 3 of 'dlacpy_' from incompatible pointer type
C/misc_solvers.c:49:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
C/misc_solvers.c:463:17: warning: passing argument 7 of 'dlacpy_' from incompatible pointer type
C/misc_solvers.c:49:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
```


`Py_ssize_t` is typedef'd from `ssize_t`, which is `long` on at least FreeBSD, Linux and Solaris.  I believe this is a blocking issue.


---

Comment by jhpalmieri created at 2010-07-28 00:44:16

While this builds on t2.math, it fails to build on mark (a skynet solaris machine).  Of course, the old version of cvxopt doesn't build on mark, either...

With either version, I get this, right at the start of the build:

```
running build_ext
building 'glpk' extension
creating build/temp.solaris-2.10-sun4u-2.6
creating build/temp.solaris-2.10-sun4u-2.6/C
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/pa\
lmieri/mark/sage-4.5.2.alpha1/local/include -I/home/palmieri/mark/sage-4.5.2.alpha1/local/include/\
python2.6 -c C/glpk.c -o build/temp.solaris-2.10-sun4u-2.6/C/glpk.o
In file included from C/cvxopt.h:32:0,
                 from C/glpk.c:20:
C/sun_complex.h:33:32: error: expected identifier or '(' before '_Imaginary'
error: command 'gcc' failed with exit status 1
Error building/installing cvxopt
```



---

Comment by drkirkby created at 2010-07-28 02:07:41

Replying to [comment:51 jhpalmieri]:
> While this builds on t2.math, it fails to build on mark (a skynet solaris machine).  Of course, the old version of cvxopt doesn't build on mark, either...
> 
> With either version, I get this, right at the start of the build:
> {{{
> running build_ext
> building 'glpk' extension
> creating build/temp.solaris-2.10-sun4u-2.6
> creating build/temp.solaris-2.10-sun4u-2.6/C
> gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/pa\
> lmieri/mark/sage-4.5.2.alpha1/local/include -I/home/palmieri/mark/sage-4.5.2.alpha1/local/include/\
> python2.6 -c C/glpk.c -o build/temp.solaris-2.10-sun4u-2.6/C/glpk.o
> In file included from C/cvxopt.h:32:0,
>                  from C/glpk.c:20:
> C/sun_complex.h:33:32: error: expected identifier or '(' before '_Imaginary'
> error: command 'gcc' failed with exit status 1
> Error building/installing cvxopt
> }}}

John, what is the md5 checksum of the package you used? Where did you get it from? I took Dima's package 

 http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.2.p1.spkg

(md5 = 38681db8e19f69b0e7972c5278e8e183)

but get no such error message on t2.math (Solaris 10). I do notice a lot of unused variables, and other compiler warnings, which always make me a bit weary of code. 

I think in light of what Peter Jeremy has found, it would be foolish to not add an spkg-check file and execute the self-tests for cvxopt. 

Dave


---

Comment by jhpalmieri created at 2010-07-28 02:15:59

I misspoke earlier.  I haven't tried to build this on t2, so I don't know if it builds there.  I have of course built the old version on t2 with no problem.

On the skynet machine mark, I can't build either the old version or the new one (= Dima's package), despite using the new gcc compiler with the sun linker which successfully built lots of other packages, making more progress than I'd seen before on that machine.  (I get the same md5sum as you posted.)


---

Comment by dimpase created at 2010-07-28 11:40:22

Replying to [comment:50 pjeremy]:
> 6456-freebsd-spkg-install.patch adds support for FreeBSD (this is a port of the patch in #9601).  I have compile-tested this but not yet tried to use the resultant module.
> 
> Note that further changes are necessary for cvxopt-1.1.2.p1.spkg to work on most 64-bit OSs.

could it simply be that some -m64 or whatever flag settings to be added to spkg-install? 

It can very well be that the standalone cvxopt does not work on that fancy 64-bit systems anyway. If this is the case, I am not willing to do anything on this at this ticket.

Last but not least, I would object in strongest possible terms to call a blocker an issue that is present in the current cvxopt (0.9) spkg. We must upgrade, and then try to improve, and not sit endlessly here...


---

Comment by dimpase created at 2010-07-28 11:49:59

Replying to [comment:40 drkirkby]:
> I should add, `/usr/include/complex.h` is included in the first release of Solaris 10 (released in March 2005) and also in the latest OpenSolaris build. There seems little point in doing what we are doing, espeically given it is doubtful if this is legal - the header is not released under the GPL. 

sun_complex.h is in the current cvxopt spkg.
I added the sun_complex.h inclusion to 1.1.2 cause I was not able to make it work on t2 otherwise. So I just went with the solution that is known to work. 

Note that <complex.h> is included in cvxopt.h by default, albeit under some condition, etc.

If you have a better solution that works on t2, please post a patch here, and I make 
cvxopt-1.1.2.p2.spkg that incorporates it.
I am also willing to put back examples and docs.

Dima


---

Comment by drkirkby created at 2010-07-28 12:10:53

Replying to [comment:55 dimpase]:
> Replying to [comment:40 drkirkby]:
> > I should add, `/usr/include/complex.h` is included in the first release of Solaris 10 (released in March 2005) and also in the latest OpenSolaris build. There seems little point in doing what we are doing, espeically given it is doubtful if this is legal - the header is not released under the GPL. 
> 
> sun_complex.h is in the current cvxopt spkg.
> I added the sun_complex.h inclusion to 1.1.2 cause I was not able to make it work on t2 otherwise. So I just went with the solution that is known to work. 
> 
> Note that <complex.h> is included in cvxopt.h by default, albeit under some condition, etc.
> 
> If you have a better solution that works on t2, please post a patch here, and I make 
> cvxopt-1.1.2.p2.spkg that incorporates it.
> I am also willing to put back examples and docs.
> 
> Dima

The current patch for Solaris does not work at all with gcc 4.5, as there's a syntax error in the code I wrote above, which you copied. 

This line is not legal C


```
#ifdef if defined __sun /* Need to check if that's the best one */
```


and gives a warning from the compiler


```
In file included from C/glpk.c:20:0:
C/cvxopt.h:30:11: warning: extra tokens at end of #ifdef directive
```


It then goes on to give an error message, as I suspect the header file <complex.h> does not get included. I suspect gcc is interpreting this as 


```
#ifdef if
```


I think we need the documentation and examples back, add an spkg-check file, and run all the self-tests. Unfortunately, I don't have time to do any of that now, though I can do it later today. (My wife is waiting on me to do some things in the house!)

Note Peter's problem is new to this upgrade, and the warning looks to me that it could cause a problem on any 64-bit system - irrespective of whether -m64 is added as a compiler flag. In fact, I doubt Peter ever uses -m64 in his builds on FreeBSD. 

Dave


---

Comment by drkirkby created at 2010-07-28 13:56:49

I'm working on a version now which runs the self-tests and hopefully builds on all platforms. I'm still concerned about what Peter found though. Give me an hour or two, and I'll post a new package. 

Dave


---

Comment by drkirkby created at 2010-07-28 16:12:19

I've spent as long on this as I am able to for a while, so I thought I'd post what I have got. 

Note, that since 1.12 has never been merged into sage, this should be called 1.12 and not 1.12.p0, 1.12.p1 or similar. There's noting wrong with people adding a temporary letter or patch level if they want, but when its finally merged, it should not have all these temporary builds. 

I've created a package which builds on Solaris, but it fails all self-tests on Solaris.

http://boxen.math.washington.edu/home/kirkby/patches/cvxopt-1.1.2.spkg

It builds on Linux, but fails about half the self-tests on Linux.

To run the self-tests, type


```
$ export SAGE_CHECK=yes
$ ./sage -i http://boxen.math.washington.edu/home/kirkby/patches/cvxopt-1.1.2.spkg
```


I've not committed any changes. 

I'm not sure what to make of this. I don't feel this is ready, given the high failure rate of the self-tests. 

Dave


---

Comment by drkirkby created at 2010-07-28 16:12:19

Changing status from needs_info to needs_work.


---

Comment by jhpalmieri created at 2010-07-28 16:19:44

Two quick comments: both Dima's and Dave's packages seem to contain a file `.SPKG.txt.swp`, which should not be there.  Also, I can't build these on the skynet machine mark (sparc solaris), but I can if (following Dave's suggestion), I comment out these lines in spkg-install:

```
cp -p patches/sun_complex.h src/src/C/
cp -p patches/cvxopt.h src/src/C/
```

I haven't tried building on t2 with this modification.


---

Comment by drkirkby created at 2010-07-28 17:49:04

Replying to [comment:59 jhpalmieri]:
> Two quick comments: both Dima's and Dave's packages seem to contain a file `.SPKG.txt.swp`, which should not be there.  

Well spotted. 
> Also, I can't build these on the skynet machine mark (sparc solaris), but I can if (following Dave's suggestion), I comment out these lines in spkg-install:
> {{{
> cp -p patches/sun_complex.h src/src/C/
> cp -p patches/cvxopt.h src/src/C/
> }}}

It's odd, since if I comment those lines out on OpenSolaris, it fails to build:


```
copying python/coneprog.py -> build/lib.solaris-2.11-i86pc-2.6/cvxopt
running build_ext
building 'base' extension
creating build/temp.solaris-2.11-i86pc-2.6
creating build/temp.solaris-2.11-i86pc-2.6/C
gcc -DNDEBUG -g -O3 -m64 -Wall -Wstrict-prototypes -m64 -fPIC -I/export/home/drkirkby/sage-4.5.2.alpha1/local/include/python2.6 -c C/base.c -o build/temp.solaris-2.11-i86pc-2.6/C/base.o
C/base.c: In function 'convert_znum':
C/base.c:156: error: '_Imaginary_I' undeclared (first use in this function)
C/base.c:156: error: (Each undeclared identifier is reported only once
C/base.c:156: error: for each function it appears in.)
C/base.c: In function 'initbase':
C/base.c:1727: warning: dereferencing type-punned pointer will break strict-aliasing rules
C/base.c:1736: warning: dereferencing type-punned pointer will break strict-aliasing rules
error: command 'gcc' failed with exit status 1
Error building/installing cvxopt
```


I think Dima's package 

http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.2.p1.spkg

has a syntax error in the patch, so that will fail on Solaris. But my own package 

http://boxen.math.washington.edu/home/kirkby/patches/cvxopt-1.1.2.spkg

lacks that syntax error. But it seems to be necessary to add patches on some version of Solaris and messes up the build on another. 

> I haven't tried building on t2 with this modification.

Do not be too surprised if you need to change it again!

I will need to double-check if the old version of cvxopt was building on OpenSolaris. I think it was, but #9525 shows that the package would report it had built, even if it failed. 

I've deleted my older builds on OpenSolaris but since I use a ZFS file system, with snapshots enabled every 15 minutes, so I can easily get back to an older build. Or I could just rebuild an older Sage on here, as it takes less than half an hour. I do need to check what's happening here. 

Unfortunately, the last few weeks I seem to be spending a lot of time trying to test things on Solaris for people. I've been involved in the cvxopt, Pari, Singular and some other package updates. 



Dave


---

Comment by drkirkby created at 2010-07-28 17:53:57

I'm attaching a log of the test results on Linux. Either there is a big problem here, or my code for the testing is wrong. The cvxopt does not have a simple `make check` as on most packages, so there is a bigger chance of an error on my part.


---

Comment by drkirkby created at 2010-07-28 17:57:15

Results from running cvxopt's self tests on a Linux system (sage.math), but setting SAGE_CHECK=yes.


---

Attachment

Replying to [comment:58 drkirkby]:
> I'm not sure what to make of this. I don't feel this is ready, given the high failure rate of the self-tests. 

I've run them locally and many open a plot window. Do you have installed all the appropriate libraries for plotting? For me, this smells like it is clearly not designed for automated testing because I had to close all windows manually. Besides that, your script also tests `/chap7/covsel.bin` which is not a python file and also not found by the appropriate `/chap7/covsel` script due to relative paths.

I appreciate to try to include testing - and in general it makes sense to do it - but my point of view is that it is much more important to update this years old library and get compiling working on all platforms and resort fixing the library later in separate tickets. 0.9 is not useful at all.


---

Comment by schilly created at 2010-07-28 18:14:43

ok, i have to take that back, with spkg-check there are no popup windows and with the exception of this covsel/covsel.bin file everything passes. The error in your log is nearly always this ZZ thing, I don't know where this comes from ... it doesn't happen for me.


---

Attachment

ubuntu 10.4, pentium 4


---

Comment by mhansen created at 2010-07-28 18:22:41

There are still currently some problems with the spkg.

- All of the .patch files are made in the wrong direction (i.e. removing Sage-specific code and adding generic code).

- On OSX, the package links against libgslcblas which is not what we want to do.  See #3435.  The blas libraries for OSX are found in `/usr/lib`.  We also don't build ATLAS on OS X.

- This fails on Cygwin as well since we don't build ATLAS there.  There are BLAS libraries in `/usr/lib` as well.


---

Comment by schilly created at 2010-07-28 18:23:31

and btw, covsel also works and looks like this:


```
harri`@`stdbox:~/Downloads/cvxopt-1.1.2/src/examples/doc/chap7$ sage -python covsel
500 rows/columns, 1741 nonzeros

Newton decrement squared: 5.01869e+08
Newton decrement squared: 1.29139e+08
Newton decrement squared: 3.26344e+07
Newton decrement squared: 1.14508e+02
Newton decrement squared: 2.68329e+01
Newton decrement squared: 1.52504e+00
Newton decrement squared: 5.25935e-03
Newton decrement squared: 6.89978e-08
Newton decrement squared: 1.34440e-17
number of iterations:  9
harri`@`stdbox:~/Downloads/cvxopt-1.1.2/src/examples/doc/chap7$ echo "$?"
0
```



---

Comment by drkirkby created at 2010-07-28 18:41:50

Replying to [comment:62 schilly]:
> Replying to [comment:58 drkirkby]:
> > I'm not sure what to make of this. I don't feel this is ready, given the high failure rate of the self-tests. 
> 
> I've run them locally and many open a plot window. Do you have installed all the appropriate libraries for plotting? 

Probably not. 

> For me, this smells like it is clearly not designed for automated testing because I had to close all windows manually. 

That may be true. I don't know exactly what exists on sage.math. But many of the messages do not seem to indicate such a problem to me. Things like:


```
   from sage.misc.prandom import seed
   ImportError: cannot import name seed
```


does not look like a plotting problem or library to me. Would you agree? 

> Besides that, your script also tests `/chap7/covsel.bin` which is not a python file and also not found by the appropriate `/chap7/covsel` script due to relative paths.

Yes, I had noticed that, but given the large number of problems, it was only one in around 20 tests. I can easily change that, but it seems to be in the noise at the minute. 

> I appreciate to try to include testing - and in general it makes sense to do it - but my point of view is that it is much more important to update this years old library and get compiling working on all platforms and resort fixing the library later in separate tickets. 0.9 is not useful at all.

At the minute, this is certainly worst than the previous version on Solaris. 

The warning messages noticed by Peter look pretty serious to me and are new to this version. Those occur on any platform. 

I personally feel these issues should be resolved, otherwise we could end up making matters worst. If the upgrade does not get done properly now, it probably never will. 

Dave


---

Comment by pjeremy created at 2010-07-28 19:26:38

Replying to [comment:54 dimpase]:
> Replying to [comment:50 pjeremy]:
> > 6456-freebsd-spkg-install.patch adds support for FreeBSD (this is a port of the patch in #9601).  I have compile-tested this but not yet tried to use the resultant module.
> > 
> > Note that further changes are necessary for cvxopt-1.1.2.p1.spkg to work on most 64-bit OSs.
> 
> could it simply be that some -m64 or whatever flag settings to be added to spkg-install? 

No.  The code is wrong/buggy/broken.  The breakage is probably hidden in 32-bit builds.

> It can very well be that the standalone cvxopt does not work on that fancy 64-bit systems anyway. If this is the case, I am not willing to do anything on this at this ticket.

I do not consider an amd64/x86_64 system to be "fancy".  I suspect that anyone wanting to do serious work with Sage will be using a 64-bit system.

> Last but not least, I would object in strongest possible terms to call a blocker an issue that is present in the current cvxopt (0.9) spkg. We must upgrade, and then try to improve, and not sit endlessly here...

There is little point in upgrading to a package that is known to be broken.  This particular bug does not appear to be present in cvxopt-0.9 (at least I can't find the "incompatible pointer type" warnings in either my own or boxen builds) so by upgrading, we would be introducing a regression into Sage.  I am very concerned at this "release it now, we'll make it work later" mentality.  If Sage is going to be a viable alternative to the M's, it needs to be trustworthy - complaints of "feature X is missing" are easily rectified, claims of "Sage gave me wrong answers" can quickly turn into "you can't trust the output from Sage" and are far more difficult to refute.


---

Comment by jhpalmieri created at 2010-07-28 19:37:47

Replying to [comment:60 drkirkby]:

> But my own package lacks that syntax error. But it seems to be necessary to add patches on some version of Solaris and messes up the build on another.

It still fails to build on mark:

```
building 'glpk' extension
creating build/temp.solaris-2.10-sun4u-2.6
creating build/temp.solaris-2.10-sun4u-2.6/C
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/palmieri/mark/sage-4.5.2.alpha1/local/include -I/home/palmieri/mark/sage-4.5.2.alpha1/local/include/python2.6 -c C/glpk.c -o build/temp.solaris-2.10-sun4u-2.6/C/glpk.o
In file included from C/cvxopt.h:32:0,
                 from C/glpk.c:20:
C/sun_complex.h:33:32: error: expected identifier or '(' before '_Imaginary'
error: command 'gcc' failed with exit status 1
Error building/installing cvxopt
```

I'm not sure what syntax error you're referring to, but I don't see a difference in any of the files in the "patches" directory between your spkg and Dima's.


---

Comment by drkirkby created at 2010-07-28 20:05:33

Replying to [comment:68 jhpalmieri]:
> Replying to [comment:60 drkirkby]:
> 
> > But my own package lacks that syntax error. But it seems to be necessary to add patches on some version of Solaris and messes up the build on another.
> 
> It still fails to build on mark:

Did the previous version build on the Solaris host 'mark' on Skynet? 

> I'm not sure what syntax error you're referring to, but I don't see a difference in any of the files in the "patches" directory between your spkg and Dima's.

In a build log I see of yours on mark, there was a warning reported about extra items on line 30 (IIRC) of a header file. That came from the code


```
#ifdef if defined __sun /* Need to check if that's the best one */ 
```


which I typed above in this ticket, but appears to have been copied into one of the versions of this package. That code was incorrectly typed by me - it was put as a comment in this ticket, and I'd not checked it with a C compiler. It certainly does not what do what I had intended. I assumed that was in Dima's package, but I appolise if I was mistaken. Either way, the code is wrong. 

Dave


---

Comment by drkirkby created at 2010-07-28 20:26:41

Replying to [comment:67 pjeremy]:
 
> There is little point in upgrading to a package that is known to be broken. 

Agreed. 

I don't think some of the people commenting on the ticket realise what that warning is about. In fact, I personally feel gcc should consider that an error and not just issue a warning. I doubt the Sun compiler would permit that code. 


> This particular bug does not appear to be present in cvxopt-0.9 (at least I can't find the "incompatible pointer type" warnings in either my own or boxen builds) 

Me neither. That bug is a regression. 

> so by upgrading, we would be introducing a regression into Sage.  

Yes. 

> I am very concerned at this "release it now, we'll make it work later" mentality.  

Me too. There is *far* too much emphasis in Sage of adding features and far too little in controlling quality. This ticket seems to be a prime example of that. 

> If Sage is going to be a viable alternative to the M's, it needs to be trustworthy - 

Yes. 

> complaints of "feature X is missing" are easily rectified, claims of "Sage gave me wrong answers" can quickly turn into "you can't trust the output from Sage" and are far more difficult to refute.

Yes. Likewise complaints of Sage crashed damages Sage's reputation. The bug you found could certainly cause a crash. 

Dave


---

Comment by drkirkby created at 2010-07-29 00:10:11

I see three possible ways forward with this ticket - there might be others, but these two seem the most likely to get a positive result. 

 * Try an earlier release (i.e newer than 0.9, but not the latest)
 * Contact the author, making him aware of the bug Peter found - i.e. passing 64-bit pointers when the code is expecting 32-bit ones. Also point out there are a lot of variables declared, which are never used. 
 * Try without the GLPK linking. It's possible the error is only seen when linking to that, though I don't think that's the case. 



Dave


---

Comment by pjeremy created at 2010-07-29 04:00:38

Replying to [comment:71 drkirkby]:
>  * Try an earlier release (i.e newer than 0.9, but not the latest)

I don't see any benefit in this. The only justification I can find mentioned in this thread for updating cvxopt is that the current version is "ancient". Unless someone comes up with a more compelling reason for updating, I would suggest sticking to the current spkg until problems with cvxopt-1.1.2 are resolved.

>  * Contact the author, making him aware of the bug Peter found - i.e. passing 64-bit pointers when the code is expecting 32-bit ones. Also point out there are a lot of variables declared, which are never used.

To be precise, the code is passing pointers to 64-bit objects to functions expecting pointers to 32-bit objects.

I started to look at how difficult it would be to fix this morning but ran out of train journey before I got very far.

Also, whilst reading through the revision history for cvxopt, I notice that there have been a couple of changes that don't appear to be backward compatible: The `cvxopt.random` module was deleted in 0.9.2 and the definition of `bool(A)` (where `A` is a matrix) was changed in 1.1. Are these changes likely to impact other components of Sage?


---

Comment by dimpase created at 2010-07-29 10:37:40

Replying to [comment:61 drkirkby]:
> I'm attaching a log of the test results on Linux. Either there is a big problem here, or my code for the testing is wrong. The cvxopt does not have a simple `make check` as on most packages, so there is a bigger chance of an error on my part. 
> 

I am presently using Sage+cvxopt-1.1.2 in my research computations, and results I get make sense, so I cannot expect the problem you report being too hard to fix. I'll have a look now.

Dima


---

Comment by dimpase created at 2010-07-29 10:47:00

Replying to [comment:72 pjeremy]:
> Replying to [comment:71 drkirkby]:
> >  * Try an earlier release (i.e newer than 0.9, but not the latest)
> 
> I don't see any benefit in this. The only justification I can find mentioned in this thread for updating cvxopt is that the current version is "ancient". Unless someone comes up with a more compelling reason for updating, I would suggest sticking to the current spkg until problems with cvxopt-1.1.2 are resolved.
> 
> >  * Contact the author, making him aware of the bug Peter found - i.e. passing 64-bit pointers when the code is expecting 32-bit ones. Also point out there are a lot of variables declared, which are never used.
> 
> To be precise, the code is passing pointers to 64-bit objects to functions expecting pointers to 32-bit objects.
> 
> I started to look at how difficult it would be to fix this morning but ran out of train journey before I got very far.
> 
> Also, whilst reading through the revision history for cvxopt, I notice that there have been a couple of changes that don't appear to be backward compatible: The `cvxopt.random` module was deleted in 0.9.2 and the definition of `bool(A)` (where `A` is a matrix) was changed in 1.1. Are these changes likely to impact other components of Sage? 

I am not aware of any Sage component that uses cvxopt. Surely, upgrading from 0.9 to 1.1 will break some code using cvxopt, but this is to be expected. The structure of the library has changed somewhat, so some imports might need to be fixed.

Regarding random, cvxopt has switched to using external random sources before 0.9.8, which is the currently used in Sage 4.5.1 spkg version. So I do not see why this is relevant at this point at all.


---

Comment by dimpase created at 2010-07-29 11:18:33

Replying to [comment:67 pjeremy]:
> Replying to [comment:54 dimpase]:
> > Replying to [comment:50 pjeremy]:
> > > 6456-freebsd-spkg-install.patch adds support for FreeBSD (this is a port of the patch in #9601).  I have compile-tested this but not yet tried to use the resultant module.
> > > 
> > > Note that further changes are necessary for cvxopt-1.1.2.p1.spkg to work on most 64-bit OSs.
> > 
> > could it simply be that some -m64 or whatever flag settings to be added to spkg-install? 
> 
> No.  The code is wrong/buggy/broken.  The breakage is probably hidden in 32-bit builds.
> 
> > It can very well be that the standalone cvxopt does not work on that fancy 64-bit systems anyway. If this is the case, I am not willing to do anything on this at this ticket.
> 
> I do not consider an amd64/x86_64 system to be "fancy".  I suspect that anyone wanting to do serious work with Sage will be using a 64-bit system.
> 
> > Last but not least, I would object in strongest possible terms to call a blocker an issue that is present in the current cvxopt (0.9) spkg. We must upgrade, and then try to improve, and not sit endlessly here...
> 
> There is little point in upgrading to a package that is known to be broken.  

There is also little point in keeping 0.9.8 in Sage! It's next to impossible to use 0.9.8 for anything serious, as it's not supported, it is known to be buggy in one or another way (one can dig this up in cvxopt archives, if needed), there are no easy to find examples to look at for 0.9, etc etc etc.

Sticking to 0.9.8 is the same as having no cvxopt in Sage at all...


---

Comment by drkirkby created at 2010-07-29 11:29:27

Replying to [comment:74 dimpase]:
> Replying to [comment:72 pjeremy]:
> > Replying to [comment:71 drkirkby]:
> > >  * Try an earlier release (i.e newer than 0.9, but not the latest)
> > 
> > I don't see any benefit in this. The only justification I can find mentioned in this thread for updating cvxopt is that the current version is "ancient". Unless someone comes up with a more compelling reason for updating, I would suggest sticking to the current spkg until problems with cvxopt-1.1.2 are resolved.
> > 
> > >  * Contact the author, making him aware of the bug Peter found - i.e. passing 64-bit pointers when the code is expecting 32-bit ones. Also point out there are a lot of variables declared, which are never used.
> > 
> > To be precise, the code is passing pointers to 64-bit objects to functions expecting pointers to 32-bit objects.
> > 
> > I started to look at how difficult it would be to fix this morning but ran out of train journey before I got very far.
> > 
> > Also, whilst reading through the revision history for cvxopt, I notice that there have been a couple of changes that don't appear to be backward compatible: The `cvxopt.random` module was deleted in 0.9.2 and the definition of `bool(A)` (where `A` is a matrix) was changed in 1.1. Are these changes likely to impact other components of Sage? 
> 
> I am not aware of any Sage component that uses cvxopt. Surely, upgrading from 0.9 to 1.1 will break some code using cvxopt, but this is to be expected. The structure of the library has changed somewhat, so some imports might need to be fixed.
> 
> Regarding random, cvxopt has switched to using external random sources before 0.9.8, which is the currently used in Sage 4.5.1 spkg version. So I do not see why this is relevant at this point at all.

The pointer problem could potentially cause segfaults and data corruption. That's my single biggest concern. Not a single test passed on my Solaris build. 

There appears to be a split view on this ticket

 * Those that want it updated for the functionality. 
 * Those that don't want the current code updated because they feel it's a regression. 

How about making the updated version an optional or experimental package? (Personally I feel the latter is more appropriate). Those that feel they need the update can use it, whilst those that consider it makes Sage less stable will simply not bother installing it. 

I think Peter's comments about the: 

_"release it now, we'll make it work later" mentality_'

is very true here. 

Dave


---

Comment by drkirkby created at 2010-07-29 11:33:58

Replying to [comment:75 dimpase]:

> Sticking to 0.9.8 is the same as having no cvxopt in Sage at all...

Why was 0.9.8 ever put in Sage if its so useless? 

Your comment about 0.9.8 being buggy is interesting. 

Version 1.1.2 is most obviously buggy. 

Dave


---

Comment by dimpase created at 2010-07-29 12:05:03

Replying to [comment:66 drkirkby]:
> Replying to [comment:62 schilly]:
> > Replying to [comment:58 drkirkby]:
> > > I'm not sure what to make of this. I don't feel this is ready, given the high failure rate of the self-tests. 
> > 
> > I've run them locally and many open a plot window. Do you have installed all the appropriate libraries for plotting? 
> 
> Probably not. 
> 
> > For me, this smells like it is clearly not designed for automated testing because I had to close all windows manually. 
> 
> That may be true. I don't know exactly what exists on sage.math. But many of the messages do not seem to indicate such a problem to me. Things like:
> 
> {{{
>    from sage.misc.prandom import seed
>    ImportError: cannot import name seed
> }}}
> 
> does not look like a plotting problem or library to me. Would you agree? 
> 
> > Besides that, your script also tests `/chap7/covsel.bin` which is not a python file and also not found by the appropriate `/chap7/covsel` script due to relative paths.
> 
> Yes, I had noticed that, but given the large number of problems, it was only one in around 20 tests. I can easily change that, but it seems to be in the noise at the minute. 
> 
> > I appreciate to try to include testing - and in general it makes sense to do it - but my point of view is that it is much more important to update this years old library and get compiling working on all platforms and resort fixing the library later in separate tickets. 0.9 is not useful at all.
> 
> At the minute, this is certainly worst than the previous version on Solaris. 
> 
> The warning messages noticed by Peter look pretty serious to me and are new to this version. Those occur on any platform. 
> 
> I personally feel these issues should be resolved, otherwise we could end up making matters worst. If the upgrade does not get done properly now, it probably never will. 
> 

Dave, 

your spkg-check is buggy. You probably end up calling a very wrong python to run the examples. E.g. if I cd to  
cvxopt-1.1.2/src/examples/doc/chap8
make a symbolic link mcsdp.py to mcsdp, fire up sage, and do

sage: load('mcsdp.py')

it happily runs without any errors etc. And this is one of examples your spkg-check fails on with weird error messages. So the problem does not seem to be in cvxopt here, but rather in your script...
 
Dima


---

Comment by drkirkby created at 2010-07-29 13:18:42

Replying to [comment:78 dimpase]:

> Dave, 
> 
> your spkg-check is buggy. You probably end up calling a very wrong python to run the examples. E.g. if I cd to  
> cvxopt-1.1.2/src/examples/doc/chap8
> make a symbolic link mcsdp.py to mcsdp, fire up sage, and do
> 
> sage: load('mcsdp.py')
> 
> it happily runs without any errors etc. And this is one of examples your spkg-check fails on with weird error messages. So the problem does not seem to be in cvxopt here, but rather in your script...
>  
> Dima
> 

Dima, 

I made it very clear that "I've spent as long on this as I am able to for a while, so I thought I'd post what I have got." I also made it clear I'd not committed the changes - a clear reflection I was not confident of them all. 

http://trac.sagemath.org/sage_trac/ticket/6456#comment:58

If the wrong python is being called, that's a bug, as the first in the path, which is the one in Sage, should be called. One could work around that with "$SAGE_LOCAL/nib/python"

I'm aware of the issue with calling the .bin file, but as I remarked above, that's in the noise compared to the most significant issues of warnings from the compiler. 

Feel free to improve the test suite. Rather than execute them all in a loop, perhaps its better to cd to the directory and run them from there. But those changes are not going to get around the more serious issue, which is seen well before the test suite is run. 

I'm involved in many things at Sage at the moment. 

 * This ticket
 * #9343 - the upgrade of Pari, which is a non-trivial issue
 * #9281 - trying to get more self-tests into Sage. 
 * #8059 - update Singular SPKG to newest upstream release. Another big package

In addition, I've involved in same way with other less time consuming tickets

 * #9533: Update GSL to the latest upstream release (1.14) & permit parallel building.
 * #9568: Update IML to the newest upstream release, and improve spkg-install
 * #9603: Force iconv to build + install on HP-UX. Currently it is only installed on Solaris and Cygwin.
 
I really don't have a huge amount of time to devote to this one. I'm less inclined to devote time to improving the self-tests on this package, as its clear the package is more seriously broken when its compiled. 

I seem to get cc'ed on a number of tickets where people can't be bothered to build on Solaris, so they think I will do the work for them. I'm tending to do that less now. There should be a much larger disk on t2 soon, so there will be even less excuse for people to pester me do do the Solaris checking. I never pester others other check code on Linux or OS X. I just do it myself. 

To be fair Dima, this is not aimed at you, as you have checked code on Solaris many times.

With all the comments above on this ticket, how many people have actually made an effort to test cvxopt on a few computers with a few different operating systems. Compare that with 

#9533: Update GSL to the latest upstream release (1.14) & permit parallel building.

where a lot of people have tested the code on multiple operating systems, with multiple compilers and run all the self-tests and run all the doctests on popular platforms. That's been done on 

    * Cygwin
    * FreeBSD
    * HP-UX
    * Linux
    * OpenSolaris
    * OS X
    * Solaris 


Dave


---

Comment by dimpase created at 2010-07-29 16:21:09

Replying to [comment:50 pjeremy]:
> 6456-freebsd-spkg-install.patch adds support for FreeBSD (this is a port of the patch in #9601).  I have compile-tested this but not yet tried to use the resultant module.
> 
> Note that further changes are necessary for cvxopt-1.1.2.p1.spkg to work on most 64-bit OSs.
> Compiling in FreeBSD/amd64 (with or without the above patch) gives:
> {{{
> gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/mnt/sage-4.5/local/include -fPIC -DDLONG= -I/mnt/sage-4.5/local/include/python2.6 -c C/misc_solvers.c -o build/temp.freebsd-8.1-PRERELEASE-amd64-2.6/C/misc_solvers.o
> C/misc_solvers.c: In function 'scale':
> C/misc_solvers.c:152:13: warning: passing argument 1 of 'dscal_' from incompatible pointer type
> C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:152:13: warning: passing argument 4 of 'dscal_' from incompatible pointer type
> C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:155:13: warning: passing argument 3 of 'dgemv_' from incompatible pointer type
> C/misc_solvers.c:39:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:156:9: warning: passing argument 1 of 'dscal_' from incompatible pointer type
> C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:156:9: warning: passing argument 4 of 'dscal_' from incompatible pointer type
> C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:158:13: warning: passing argument 2 of 'dger_' from incompatible pointer type
> C/misc_solvers.c:41:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:160:13: warning: passing argument 1 of 'dscal_' from incompatible pointer type
> C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:160:13: warning: passing argument 4 of 'dscal_' from incompatible pointer type
> C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c: In function 'pack2':
> C/misc_solvers.c:459:17: warning: passing argument 3 of 'dlacpy_' from incompatible pointer type
> C/misc_solvers.c:49:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:459:17: warning: passing argument 5 of 'dlacpy_' from incompatible pointer type
> C/misc_solvers.c:49:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:461:17: warning: passing argument 1 of 'dscal_' from incompatible pointer type
> C/misc_solvers.c:32:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:463:17: warning: passing argument 3 of 'dlacpy_' from incompatible pointer type
> C/misc_solvers.c:49:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> C/misc_solvers.c:463:17: warning: passing argument 7 of 'dlacpy_' from incompatible pointer type
> C/misc_solvers.c:49:13: note: expected 'int *' but argument is of type 'Py_ssize_t *'
> }}}

the following 2-byte change appears to cure the problem. Semantically, this 
restricts the dense matrices that are dealt with to the sizes 2^31 by 2^31, but this
is OK for all the practical purposes.
Hopefully CVXOPT people will come up with a better fix, but for the time being
this should suffice and cure this particular headache.



```
--- a/patches/cvxopt.h  Mon Jul 26 18:45:42 2010 +0300
+++ b/patches/cvxopt.h  Thu Jul 29 09:12:21 2010 -0700
`@``@` -61,7 +61,7 `@``@`
 typedef struct {
   PyObject_HEAD
   void *buffer;          /* in column-major-mode array of type 'id' */
-  int_t nrows, ncols;    /* number of rows and columns */
+  int nrows, ncols;    /* number of rows and columns -- was int_t */
   int   id;              /* DOUBLE, INT, COMPLEX */
 } matrix;
```

 

> 
> `Py_ssize_t` is typedef'd from `ssize_t`, which is `long` on at least FreeBSD, Linux and Solaris.  I believe this is a blocking issue.


It remains to sort out the complex.h stuff on Solaris...


---

Comment by dimpase created at 2010-07-30 15:36:48

Replying to [comment:80 dimpase]:
> Replying to [comment:50 pjeremy]:
[...]

> the following 2-byte change appears to cure the problem. Semantically, this 
> restricts the dense matrices that are dealt with to the sizes 2^31 by 2^31, but this
> is OK for all the practical purposes.
> Hopefully CVXOPT people will come up with a better fix, but for the time being
> this should suffice and cure this particular headache.
> 
> 

```
 --- a/patches/cvxopt.h  Mon Jul 26 18:45:42 2010 +0300
 +++ b/patches/cvxopt.h  Thu Jul 29 09:12:21 2010 -0700
 `@``@` -61,7 +61,7 `@``@`
  typedef struct {
    PyObject_HEAD
    void *buffer;          /* in column-major-mode array of type 'id' */
 -  int_t nrows, ncols;    /* number of rows and columns */
 +  int nrows, ncols;    /* number of rows and columns -- was int_t */
    int   id;              /* DOUBLE, INT, COMPLEX */
  } matrix;
 }}}

One of cvxopt developers has acknowledged this as a valid fix. Further, he says that it will get into a new cvxopt release, 1.1.3, due shortly.

I am inclined to wait for 1.1.3, while preparing an spkg-check starting off from Dave's version, and eventually sorting out OSX and Cygwin.
(and eventually hooking up the cvxopt's documentation to Sage's documentation)

Further, the Sun complex.h related issue, I looked at the /usr/include/complex.h over on t2 and mark. It just does not make sense how  _Imaginary_I is (not) defined there,
something like
{{{
#define _Imaginary_I _Imaginary_I
}}}
---no wonder it does not work. While it does make sense in the supplied patches/sun_complex.h, which differs from the former at this and few other places. 

Dima


---

Comment by drkirkby created at 2010-07-30 23:46:26

Replying to [comment:82 dimpase]:
> Replying to [comment:80 dimpase]:
> > Replying to [comment:50 pjeremy]:
> [...]
> One of cvxopt developers has acknowledged this as a valid fix. Further, he says that it will get into a new cvxopt release, 1.1.3, due shortly.

Good.

> I am inclined to wait for 1.1.3, while preparing an spkg-check starting off from Dave's version, and eventually sorting out OSX and Cygwin.
> (and eventually hooking up the cvxopt's documentation to Sage's documentation)

I think having those self-tests will be very useful. It might need a change of method, to change to a directory before running them, rather than run them from a higher level directory as I did. 

> Further, the Sun complex.h related issue, 

Don't waste any time on that. I've spent most of the day looking at this, and will summarise my findings later.


---

Comment by pjeremy created at 2010-07-31 03:03:30

Replying to [comment:82 dimpase]:
> Replying to [comment:80 dimpase]:
> > the following 2-byte change appears to cure the problem. Semantically, this 
...
> One of cvxopt developers has acknowledged this as a valid fix. Further, he says that it will get into a new cvxopt release, 1.1.3, due shortly.

That's good.  I'm sorry that _Real Life_ intervened and I wasn't able to complete the investigation of this problem myself.  I've checked and it gets rid of the warnings on FreeBSD as well.  That leaves only just over 3000 warnings in a Sage build that need investigating.

> I am inclined to wait for 1.1.3, while preparing an spkg-check starting off from Dave's version, and eventually sorting out OSX and Cygwin.

Depending on the cvxopt project's definition of "shortly", that sounds reasonable.  I would appreciate the new SPKG including my fix to support FreeBSD (and something similar may be needed to support Cygwin)


---

Comment by drkirkby created at 2010-07-31 08:02:15

I set about trying to resolve why cvxopt would build on some Solaris systems but not on others. I believe I have finally got to the bottom of this. 

If one looks in the current cvxopt SPKG.txt file, there is a reference to this bug, and why the sun_complex.h was added. 

http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6549313

which does not appear to have any activity for more than 3 years. There's a little test program there, which I modified a bit to print good or bad:


```
#include <stdio.h>
#include <complex.h>

/*
 * "volatile" is meant to prevent gcc from calculating the sqrt as a
 * constant, we want to test libc.
 */
volatile complex double z = -_Complex_I;
int
main(void)
{
        z = csqrt(z);
        if (creal(z) > 0.0)
                printf("good\n");       /* good */
        else
                printf("bad\n");       /* bad */
}
```


After saving that to a file `test.c` I then tried to compile this using 


```
gcc -lm -std=c99 test.c  # Or in some cases using the Sun compiler.
```

in each case noting if the file compiled, or whether it gave an error like:

```
$ gcc -lm -std=c99 test.c
test.c:8: error: '_Complex_I' undeclared here (not in a function)
```

Assuming it did compile (which was the minority of cases), if that test program printed 'good' or 'bad' when it was run. 

Comparing different 12 systems I have access to, *sorted in order of the release date* of the operating system, this is what I found:

|          |     |          |    |               |          |         |         |
|----------|-----|----------|----|---------------|----------|---------|---------|
|*Computer*|*CPU*|*hostname*|*OS*|*Release of OS*|*Compiler*|*Compile*|_'Result_|
|Sun Blade 2000|SPARC|swan|Solaris 10|10/2009|gcc 4.5.0|Yes|Good|
|Sun Blade 2000|SPARC|swan|Solaris 10|10/2009|SunStudio 12.1|Yes|Bad|
|Sun Blade 2000|SPARC|swan|Solaris 10|10/2009|gcc 4.4.4|No|-|
|Sun Blade 2000|SPARC|swan|Solaris 10|10/2009|gcc 3.4.3|No|-|
|unknown |x86|orcus|Solaris 10|10/2009|gcc 4.3.4|No|-|
|unknown |x86|orcus|Solaris 10|10/2009|gcc 3.4.3|No|-|
|Sun Ultra 27|x86|hawk|OpenSolaris|06/2009|SunStudio 12.1|Yes|Good|
|Sun Ultra 27|x86|hawk|OpenSolaris|06/2009|gcc 4.5.0|Yes|Good|
|Sun Ultra 27|x86|hawk|OpenSolaris|06/2009|gcc 4.4.4|No|-|
|Sun Ultra 27|x86|hawk|OpenSolaris|06/2009|gcc 3.4.3|No|-|
|Sun Blade 2500|SPARC|mercury|Solaris 10|05/2009|gcc 4.3.4|No|-|
|Sun Blade 2500|SPARC|mercury|Solaris 10|05/2009|gcc 3.4.5|No|-|
|Sun Blade 2500|SPARC|mercury|Solaris 10|05/2009|gcc 3.4.3|No|-|
|Sun T5240|SPARC|t2|Solaris 10|05/2009|gcc 4.4.1|No|-|
|Sun T5240|SPARC|t2|Solaris 10|05/2009|gcc 3.4.3|No|-|
|Sun Fire X4540|x86|disk|OpenSolaris|11/2008|gcc 3.4.3|No|-|
|Dell OptiPlex 755|x86|fulvia|Solaris 10|05/2008|gcc 4.5.0|Yes|Good|
|Dell OptiPlex 755|x86|fulvia|Solaris 10|05/2008|gcc 3.4.3|No|-|
|Sun Blade 2500|SPARC|mark|Solaris 10|01/2006|gcc 4.5.0|Yes|Good|
|Sun Blade 2500|SPARC|mark|Solaris 10|01/2006|gcc 3.4.3|No|-|
|Sun Blade 2500|SPARC|mark|Solaris 10|01/2006|SunStudio 12|Yes|Bad|
|Sun Blade 1000|SPARC|redstart|Solaris 10|03/2005|4.5.0|Yes|Good|
|Sun Blade 1000|SPARC|redstart|Solaris 10|03/2005|4.4.3|No|-|
|Sun Blade 1000|SPARC|redstart|Solaris 10|03/2005|3.4.3|No|-|
|Sun Netra T1|SPARC|kestrel|Solaris 10|03/2005|4.4.2|No|-|
|Sun Netra T1|SPARC|kestrel|Solaris 10|03/2005|3.4.3|No|-|
|Sun Fire 480R|SPARC|ra|Solaris 8|02/2004|gcc 4.3.4|No|-|
Notes:
 * _swan_ , _redstart_ , _hawk_ and _kestrel_ are my own personal machines. 
 * _fulvia_, _mark_ and _mark2_ are hosts on Skynet. 
 * _disk_ and _t2_ are hosts on the *.math.washington.edu network.
 * _ra_ and _mercury_ are hosts on blastwave.org. (Dennis Clark of Blastwave has given me access to their network, which is useful, as their Sun Blade 2500 has faster CPUs than the Sun Blade 2500 on Skynet).
 * _orcus_ is a Solaris zone running on some x86 hardware on the blastwave.org network. I don't know what that hardware is - since it's in a Solaris zone, this is hidden. 
 * _ra_ on the blastwave.org network runs a version of Solaris older than what Sage aims to support. IMHO, we should aim to support all Solaris 10 releases, the first of which was released in March 2005, but not bother with older releases, where there are C99 related issues. 

Looking at those results, some patterns can be seen. 
 * Every time gcc 4.5.0 was used, `test.c` compiled and run OK. (gcc 4.5.0 was available on all the skynet machines and I built it on all my own machines. I did not bother building it on t2.math, disk.math or any of the machines on Blastwave.)
 * If an older version of gcc was used, `test.c` would never compile. 
 * Whether the system had SPARC or x86 processors did change the behavior. 
 * The age of the operating system did not matter. (Although I have some doubts if this would have worked with gcc 4.5 on the old Solaris 8 machine, but as noted above, this is too old to bother supporting.) 

I then realised that this is the same bug that hit us with the Sage library before (#7932). I reported that to the gcc bug database as two bugs - one for SPARC, one for x86. The GCC developers then closed one as a duplicate of the other. 
 * http://gcc.gnu.org/bugzilla/show_bug.cgi?id=42753
 * http://gcc.gnu.org/bugzilla/show_bug.cgi?id=42755

If you read [gcc bug 42753](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=42753), it basically boils down to the fact that the gcc developers claim it's a bug in the Sun header file, but that their _fixincludes_ is lacking the facility to deal with this. However, their _fixincludes_ was updated in gcc 4.5, so this problem was fixed in gcc 4.5. 

So I suspect we have two options. 
 * Force people to use gcc 4.5 on Solaris, then remove the `sun_complex.h` hack completely. That would be rather annoying, since that's the latest version of gcc, and I'm not aware of anywhere where one can download a pre-compiled gcc 4.5 binary. People would have to build it themselves, which is a non-trivial process on Solaris. 
 * We apply that patch on gcc versions older than 4.5, but omit the patch with gcc version 4.5 or later. There's an example of how to do this [here](http://www.redhat.com/docs/manuals/enterprise/RHEL-4-Manual/cpp/predefined-macros.html) using the gcc macros `__GNUC__`, `__GNUC_MINOR__` and `__GNUC_PATCHLEVEL__`. It's easy to see what macros gcc defines, by creating an empty file `foobar.c`, and using `gcc -c -E -dM foobar.c` 

So in summary, I think the solution to the Solaris problem is that the code in cvxopt needs changing so that the patched header only gets included when building with gcc less than 4.5.0. I suspect the easiest solution is to always apply a patched header file, but arrange for the patch to just include `<complex.h>` on gcc 4.5.0 or later, but have its current behavior on earlier gcc series. 

Although I've not yet modified `sun_complex.h` to have this behavior, I suspect it will allow the code to compile on any gcc >= 4.0.1, which is the earliest Sage supports. 


Dave


---

Comment by drkirkby created at 2010-08-01 00:50:22

I just noticed the current SPKG.txt file has a couple of issues, which means it does not meet the guidelines of [the Sage Developers Guide](http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt)

 * There is no `== License ==` section. I just looked at the [Copyright and license](http://abel.ee.ucla.edu/cvxopt/copyright.html) section on the cvxopt web site, and see there are multiple licenses (GPL2, GPL3, GNU Lesser General Public License, version 2.1), but all are compatible with Sage. 
 * The section marked `== Download Source ==` in SPKG.txt should be marked `== Upstream Contact ==`
 * There's no `== Dependencies ==` section. 
 * There's no `== Special Update/Build Instructions ==` section. 
 * The `== Releases ==` section should be renamed to `== Changelog ==`
 
These are all trivial changes, which will only take a few minutes to implement. 

Dave


---

Comment by drkirkby created at 2010-08-01 08:02:08

This problem with cvxopt on Solaris has become critical now, as there are no longer any compilers except gcc 4.5.0 on any of the Solaris machines. 

I've created a very small patch to fix the current version of cvxopt so it builds on Solaris. The #9657. I'd like to get that merged asap, as it is really a pain now we can't build on skynet, 

Dave


---

Comment by drkirkby created at 2010-08-01 08:12:57

Replying to [comment:87 drkirkby]:
> This problem with cvxopt on Solaris has become critical now, as there are no longer any compilers except gcc 4.5.0 on any of the Solaris machines. 
>

I meant to add there are no compilers able to build Sage on Solaris on and of the Skynet machines. 

> I've created a very small patch to fix the current version of cvxopt so it builds on Solaris. 

We should get that patch upstream if possible. As you can see, it is very trivial. All we need to add to the upstream source is something like this. 


```
#include <complex.h>
#if defined(__sun__) && defined(__GNUC__)
   #if __GNUC__ < 4  || ( __GNUC__ == 4 && __GNUC_MINOR__ < 5   )

      #undef  _Complex_I
      #define _Complex_I (__extension__ 1.0iF)

      #undef I
      #define I _Complex_I

   #endif
#endif
```


There's no need to have a huge great header file as there is at the minute. It is totally unnecessary. One two items are missing from the header file, so only two need to be added. The patch currently add a very large proprietary header file when only a few lines of code are needed. 
}}}


---

Comment by dimpase created at 2010-08-01 15:29:48

Replying to [comment:88 drkirkby]:
> Replying to [comment:87 drkirkby]:
> > This problem with cvxopt on Solaris has become critical now, as there are no longer any compilers except gcc 4.5.0 on any of the Solaris machines. 
> >
> 
> I meant to add there are no compilers able to build Sage on Solaris on and of the Skynet machines. 
> 
> > I've created a very small patch to fix the current version of cvxopt so it builds on Solaris. 
> 
> We should get that patch upstream if possible. As you can see, it is very trivial. All we need to add to the upstream source is something like this. 
> 

```
 #include <complex.h>
 #if defined(__sun__) && defined(__GNUC__)
    #if __GNUC__ < 4  || ( __GNUC__ == 4 && __GNUC_MINOR__ < 5   )
 
       #undef  _Complex_I
       #define _Complex_I (__extension__ 1.0iF)
 
       #undef I
       #define I _Complex_I
 
    #endif
 #endif
```


Why do you check for gcc here? I imagine with other compilers the problem
would be the same, too. (for the sake of reporting upstream...)
Is SunStudio 12 providing its own fix for this?

Otherwise I agree that this looks more pleasant than the current sun_complex.h hack;
I'll put it in the updated cvxopt 1.1.2 now.

Dima



> 
> There's no need to have a huge great header file as there is at the minute. It is totally unnecessary. One two items are missing from the header file, so only two need to be added. The patch currently add a very large proprietary header file when only a few lines of code are needed. 
> }}}
>


---

Comment by drkirkby created at 2010-08-01 15:51:30

Replying to [comment:89 dimpase]:

> Why do you check for gcc here? I imagine with other compilers the problem
> would be the same, too. (for the sake of reporting upstream...)
> Is "SunStudio 12 providing its own fix for this?


The fix is not needed with the SunStudio compiler. I can compile a test program that uses `_Complex_I` with the Sun compiler without resorting to any hacks - see the big table above I produced. 
 
http://trac.sagemath.org/sage_trac/ticket/6456#comment:85

In any case, I've not done much testing with SunStudio on this, so it would be unwise to start applying patches without testing them. 

> Otherwise I agree that this looks more pleasant than the current sun_complex.h hack;
> I'll put it in the updated cvxopt 1.1.2 now.
> 
> Dima

Yes, I think so too. gcc 4.5.0 creates a file with the fixed header, which I inspected. That is huge, looking similar to that the current patch in Sage. There's no need to repeat them all. And as I noted before, it is doubtful if its 100% legal to do so. All I did was copied the necessary parts. 

I did email the cvxopt developers about this, so hopefully it can be fixed upstream. You might not actually need the patch at all when 1.13 is released. 

Dave


---

Comment by dimpase created at 2010-08-01 19:00:03

Replying to [comment:84 pjeremy]:
> Replying to [comment:82 dimpase]:
> > Replying to [comment:80 dimpase]:
> > > the following 2-byte change appears to cure the problem. Semantically, this 
> ...
> > One of cvxopt developers has acknowledged this as a valid fix. Further, he says that it will get into a new cvxopt release, 1.1.3, due shortly.
> 
> That's good.  I'm sorry that _Real Life_ intervened and I wasn't able to complete the investigation of this problem myself.  I've checked and it gets rid of the warnings on FreeBSD as well.  That leaves only just over 3000 warnings in a Sage build that need investigating.
> 
> > I am inclined to wait for 1.1.3, while preparing an spkg-check starting off from Dave's version, and eventually sorting out OSX and Cygwin.
> 
> Depending on the cvxopt project's definition of "shortly", that sounds reasonable.  I would appreciate the new SPKG including my fix to support FreeBSD (and something similar may be needed to support Cygwin)

New spkg is here:
 http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.2.spkg

here is the list of goodies that got added/updated/fixed:
 * applied P.Jeremy's FreeBSD patch
 * corrected the 64-bit specific int* bug reported by pjeremy
 * turned on GSL extension (this is the default mode for CVXOPT, and GSL is a standard Sage spkg, so
   this makes perfect sense); this in particular allowed to get rid of strange random seed-related
   import bugs uncovered by David Kirkby's spkg-check
   TODO(?): one might want to enchance the code to allow other Sage random sources,
    at the moment only GSL is used in CVXOPT-1.1.2 spkg, apparently it will need an unclear
    to me "with seed(..)" construct.
   TODO: We will need to make sure that CVXOPT is built after GSL
 * modified spkg-check to report test names, cd to appropriate subdirs, and skip .bin files.
   TODO: add more tests.
 * corrected the .patch files in patches/ to be in right order --- just run the makepatchfiles
   script to re-create these files!
 * removed html doc files in src/doc; the .rst doc files are there, so it's a question of
   rebuilding them 
   (e.g. one can do sage -sh; cd src/doc; make html)
   TODO: incorporate docs buiding into spkg-install, and/or merge into 
   Sage documentation 
 * included David's shortened and gcc-version targeted Sun-specific patch
   (comment 88); removed sun_complex.h  
 * took care of SPKG.txt sections, as mentioned in comment 87

MAJOR change:
it now depends on GSL--- this gets rid of sage.prandom related problems

MAJOR TODOs:
MacOSX fixes, and testing with gcc-4.5 on as many platforms as possible
(otherwise it looks good to go !)

Dima


---

Comment by dimpase created at 2010-08-01 19:10:03

Replying to [comment:91 dimpase]:
forgot to add that I tested (also spkg-check) on Linux 32bit and 64bit (sage.math), 
as well as on Sparc Solaris (t2.math) with gcc 4.x, with x<=4.

Would appreciate hearing how it does with gcc 4.5 (Linux and Solaris)


---

Comment by drkirkby created at 2010-08-01 21:42:02

Replying to [comment:92 dimpase]:

> Would appreciate hearing how it does with gcc 4.5 (Linux and Solaris)

I've been to the pub tonight and have several beers. I think it's best if I don't start building anything now! 

But I'll look at that when I have sobered up a bit. 

Be aware, there is a ticket to update gsl #9533. However, IIRC, an inspection of the GSL ChangeLog shows that all the changes were related to way GSL is built, and nothing to do with actual changes in the algorithms. But please check that! As I said, I have had a few (well a few too many) beers tonight!

Dave


---

Comment by mhansen created at 2010-10-12 00:12:19

I've made a new spkg at http://sage.math.washington.edu/home/mhansen/cvxopt-1.1.3.spkg based on Dima's latest one.  I've also included the changes to make this build on Cygwin.  However, with both this and the 1.1.2 package, I get the following error on my Linux box:


```
ImportError: /opt/sage/local/lib/python2.6/site-packages/cvxopt/base.so: undefined symbol: _g95_stop_blank
```



---

Comment by dimpase created at 2010-10-12 00:43:08

Replying to [comment:94 mhansen]:
> I've made a new spkg at http://sage.math.washington.edu/home/mhansen/cvxopt-1.1.3.spkg based on Dima's latest one.  I've also included the changes to make this build on Cygwin.  However, with both this and the 1.1.2 package, I get the following error on my Linux box:

Do you run g95 rather than gfortran? As you might have noticed, there is no g95-specific configuration in my spkg.
I can look into this if you like.

Why do you call it 1.1.3? Have you got CVXOPT v1.1.3-sources?!


Dima

> 
> {{{
> ImportError: /opt/sage/local/lib/python2.6/site-packages/cvxopt/base.so: undefined symbol: _g95_stop_blank
> }}}


---

Comment by mhansen created at 2010-10-12 00:47:21

I use gfortran -- g95 isn't installed on my system.  Maybe some previous library that it's picking up used g95?  I'm not sure.  I'll try rebuilding the relevant spkgs.

This is based on the 1.1.3 sources which are on the CVXOPT website.


---

Comment by dimpase created at 2010-10-12 01:15:21

Replying to [comment:96 mhansen]:
> I use gfortran -- g95 isn't installed on my system.  Maybe some previous library that it's picking up used g95?  I'm not sure.  I'll try rebuilding the relevant spkgs.

g95 is distributed with Sage. Do you by any chance got in installed in your instance of Sage?
> 
> This is based on the 1.1.3 sources which are on the CVXOPT website.
Thanks. I was watching CVXOPT's googlegoup, but, weirdly enough, it is silent of this!


---

Comment by dimpase created at 2010-10-12 02:04:02

Replying to [comment:94 mhansen]:
> I've made a new spkg at http://sage.math.washington.edu/home/mhansen/cvxopt-1.1.3.spkg based on Dima's latest one.  I've also included the changes to make this build on Cygwin.  However, with both this and the 1.1.2 package, I get the following error on my Linux box:
> 
> {{{
> ImportError: /opt/sage/local/lib/python2.6/site-packages/cvxopt/base.so: undefined symbol: _g95_stop_blank
> }}}

I tried your spkg on Sage 4.6.alpha1 (Debian x64), and it seems to work just fine.
That undefined symbol you got must really have something to do with your setup, not with the spkg
(moreover, noone reported something like this with my latest 1.1.2 spkg, while you have this problem with 1.1.2, as well)


---

Comment by ncohen created at 2010-10-12 04:43:59

I met these "undefined symbol" several many times already, and it was often in my case because the libraries I was using needed to be linked with other libraries, which I did not do correctly... Just in case it can help, foggy as it is... I got used to debug segfaults, but I still do not like these "undefined symbol" errors `:-/`

Nathann


---

Comment by drkirkby created at 2010-10-12 07:08:59

A few comments. 
 * I changed the title, since this is a new version. 
 * There's a file `patches/setup.py.orig` which is not in the repository. What is this .orig supposed to be? Is it from the old version of this package, since it is totally different from the setup.py in the source files. If its only from the previous version of the package, it serves no real useful purpose and can be deleted. 


```
-rw-r--r--   1 drkirkby staff       5701 Sep 16 05:55 ./src/src/setup.py
-rw-r--r--   1 drkirkby staff       5648 Oct 12 00:53 ./patches/setup.py.patch
-rw-r--r--   1 drkirkby staff       6226 Oct 12 01:09 ./patches/setup.py
-rw-r--r--   1 drkirkby staff       6228 Oct 12 01:06 ./patches/setup.py.orig
```


 * The modification time of ./patches/setup.py.patch is Oct 12 00:53, yet the file that should be created from, ./patches/setup.py was last edited 16 minute later. I'm a bit suspicious of how this package has been patched, 
 * The description in SPKG.txt could be a lot more informative. There's a much better description in the file `setup.py`. 
 * It would be sensible to list the author's email addresses in the 'Upstream Contact' section of SPKG.txt. They are in the file setup.py. 
 * The entry for cvxopt-1.1.2 in SPKG.txt should be removed, since 1.1.2 was never merged into Sage at all. All the changes should be under the 1.1.3 section. 
 * All the "TODO" items in SPKG.txt would be better moved to the special build instructions section of SPKG.txt, since they have not been done, they should not be done in the ChangeLog, which should document changes made. 
 * Some of the TODO items *must* be done now, and can't be left. For example, this is now linking against both GSL and GLPK, so adding those dependencies to the file `spkg/standard/deps` must be listed as a change that has been made, rather than a TODO. 
 * I've attached a revised spkg/standard/deps which makes sure that both GSL and GLPK are built before cvxopt. 
 * All the authors who have contributed should be listed in SPKG.txt. There are several missing, including myself, Peter Jeremy and perhaps others. 
 * The authors field on here needs to have the full names of people, not their user names.


---

Attachment

Modified deps file to ensure both GSL and GLPK gets built before cvxopt


---

Attachment

Differences between the new 'deps' file and that in sage-4.6.alpha3. Only for review purposes - this should not be applied.


---

Comment by drkirkby created at 2010-10-12 07:25:23

I'd also consider that adding a couple of doc tests this is working with gsl and glpk should be done before this gets a positive review, since these are new functionality added, but are untested.


---

Comment by drkirkby created at 2010-10-12 07:37:27

One more thing. It seems the list of dependencies of this is far larger than listed in SPKG.txt file. See the file deps to see what this depends upon.


---

Comment by dimpase created at 2010-10-17 06:50:53

Replying to [comment:96 mhansen]:
> I use gfortran -- g95 isn't installed on my system.  Maybe some previous library that it's picking up used g95?  I'm not sure.  I'll try rebuilding the relevant spkgs.
> 
> This is based on the 1.1.3 sources which are on the CVXOPT website.

I just tested it on MacOSX 10.5 PPC that uses g95, and it works just fine (not only the doctest in numerical/optimize.py, but also some of my code that uses other CVXOPT features).
Very good, as I feared this to be the major sticking point...


---

Comment by mhansen created at 2010-11-04 05:12:30

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-11-04 05:12:30

I've posted a new spkg in the same place addressing many of David's points.


---

Comment by dimpase created at 2010-11-09 15:08:08

Replying to [comment:104 mhansen]:
> I've posted a new spkg in the same place addressing many of David's points.

tested on Linuces, MacOSX 10.5 PPC, OpenSolaris x86. All good!


---

Comment by dimpase created at 2010-11-09 15:08:08

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-10 09:08:58

I am not convinced that the licence issue is resolved.

 * cvxopt is a *standard* package in Sage (if that would matter).
 * `SPKG.txt` claims the licence to be "multiple licenses: GPLv2, GPLv3, GNU Lesser General Public License, v2.1" when in fact it is simply GPLv3+.  It is true that _parts_ of cvxopt have different licences, but the package as a whole is GPLv3+.  In any case, this has to be changed in `SPKG.txt`

I posted to sage-devel about this.


---

Comment by jdemeyer created at 2010-11-10 09:08:58

Changing status from positive_review to needs_work.


---

Comment by dimpase created at 2010-11-10 09:39:35

Replying to [comment:106 jdemeyer]:
> I am not convinced that the licence issue is resolved.
> 
>  * cvxopt is a *standard* package in Sage (if that would matter).
>  * `SPKG.txt` claims the licence to be "multiple licenses: GPLv2, GPLv3, GNU Lesser General Public License, v2.1" when in fact it is simply GPLv3+.  It is true that _parts_ of cvxopt have different licences, but the package as a whole is GPLv3+.  In any case, this has to be changed in `SPKG.txt`
> 
> I posted to sage-devel about this.

as I read on sage-devel, it's not a problem, as CVXOPT is not a part of sage-x.y.z.spkg. SPKG.txt merely reflects the CVXOPT's copyright notice, as given here:
http://abel.ee.ucla.edu/cvxopt/copyright.html
So we should not change SPKG.txt.


---

Comment by dimpase created at 2010-11-10 09:39:35

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-11-10 09:47:12

I disagree that `SPKG.txt` reflects CVXOPT's copyright notice.  It very clearly says on the CVXOPT page

```
CVXOPT is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
```


There is no mention of the other licences which are mentioned in SPKG.txt


---

Comment by jdemeyer created at 2010-11-10 09:47:12

Changing status from needs_review to needs_work.


---

Comment by dimpase created at 2010-11-10 11:42:00

Replying to [comment:108 jdemeyer]:
> I disagree that `SPKG.txt` reflects CVXOPT's copyright notice.  It very clearly says on the CVXOPT page

```
CVXOPT is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
```



> 
> There is no mention of the other licences which are mentioned in SPKG.txt

IMHO you're slightly misquoting. The text goes on there, and mentions more licences. Anyway.

Would you agree to the following text in SPKG.txt?


```
## License
GPLv3 or later. Includes parts under GPLv2, 
GNU Lesser General Public License, v2.1. See src/LICENSE for more details.
(Sage-compatible)
```



---

Comment by dimpase created at 2010-11-10 11:42:00

Changing status from needs_work to needs_info.


---

Comment by drkirkby created at 2010-11-10 11:49:13

Replying to [comment:108 jdemeyer]:
> I disagree that `SPKG.txt` reflects CVXOPT's copyright notice.  It very clearly says on the CVXOPT page
> {{{
> CVXOPT is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
> }}}
> 
> There is no mention of the other licences which are mentioned in SPKG.txt

Although the LICENSE file starts by saying it is GPL3, read further down and you will find:


```
The CVXOPT distribution includes source code for a subset of the 
SuiteSparse suite of sparse matrix algorithms, including:

- AMD Version 2.2. Copyright (c) 2007 by Timothy A. Davis, Patrick R. 
  Amestoy, and Iain S. Duff.
- CHOLMOD Version 1.7.1 Copyright (c) 2005-2009 by University of Florida,
  Timothy A. Davis and W. Hager.
- COLAMD version 2.7.  Copyright (c) 1998-2007 by Timothy A. Davis.
- UMFPACK Version 5.4.0. Copyright (c) 1994-2009 by Timothy A. Davis.

These packages are licensed under the terms of the GNU General Public 
License, version 2 or higher (UMFPACK, the Supernodal module of CHOLMOD)
and the GNU Lesser General Public License, version 2.1 or higher 
(the other CHOLMOD modules, AMD, COLAMD).  For copyright and license 
details, consult the README files in the source directories or the website 
listed below.
```


So there are multiple licenses.

IIRC, it was me who added those comments, though it might have been another package I'm thinking of. 

Dave


---

Comment by drkirkby created at 2010-11-10 12:12:05

Yes, it was me who added the comments - see my comments 3 months ago on this ticket. 

I don't see what the problem is though - Sage includes a lot of code licensed under the GNU Lesser General Public License - e.g. MPIR recently changed to that. Hence my comment this are "Sage compatible". Actually, I think someone has changed that, as I doubt I would have started the sentence with a lower case 's', but it's a minor point.  I think the license issue is a _non-issue_. 

I have some recollection that the cvxopt authors were going to incorporate my Solaris patch, so given this has ticket has been changed from using version 1.1.2 to using 1.1.3, I'm puzzled that does not appear to have happened. 

I'm more concerned we have made this use GLPK, but to the best of my knowledge, there's not a single doc test showing any example of how to use GLPK, so we have no idea of that functionality works at all.

Dave


---

Comment by dimpase created at 2010-11-10 12:32:28

Replying to [comment:111 drkirkby]:
> Yes, it was me who added the comments - see my comments 3 months ago on this ticket. 
> 
> I don't see what the problem is though - Sage includes a lot of code licensed under the GNU Lesser General Public License - e.g. MPIR recently changed to that. Hence my comment this are "Sage compatible". Actually, I think someone has changed that, as I doubt I would have started the sentence with a lower case 's', but it's a minor point.  I think the license issue is a _non-issue_. 
> 
> I have some recollection that the cvxopt authors were going to incorporate my Solaris patch, so given this has ticket has been changed from using version 1.1.2 to using 1.1.3, I'm puzzled that does not appear to have happened. 

They wanted to look into it, that's all. I guess this has become even more irrelevant, as I don't even have a machine where to test this patch any more. They are probably in the same position.

How about we upgrade this now, and then fix remaining issues in TODO in new ticket(s)? I need this stuff, and I am sick and tired of extra manual labour I need to do in order to use this version of cvxopt....

Dima

> 
> I'm more concerned we have made this use GLPK, but to the best of my knowledge, there's not a single doc test showing any example of how to use GLPK, so we have no idea of that functionality works at all.
> 
> Dave


---

Comment by jdemeyer created at 2010-11-10 12:36:30

Replying to [comment:109 dimpase]:
> Would you agree to the following text in SPKG.txt?
> 
> {{{
> == License ==
> GPLv3 or later. Includes parts under GPLv2, 
> GNU Lesser General Public License, v2.1. See src/LICENSE for more details.
> (Sage-compatible)
> }}}

Yes.


---

Comment by jdemeyer created at 2010-11-10 12:39:30

Changing status from needs_info to needs_work.


---

Comment by jdemeyer created at 2010-11-10 12:39:30

Replying to [comment:110 drkirkby]:
> Although the LICENSE file starts by saying it is GPL3, read further down and you will find:
> [...]
> So there are multiple licenses.

Well, it depends what you mean with "multiple licences".  It is true that cvxopt *includes* code under GPLv2, LGPL2.1 but the package *as a whole* is licenced as GPLv3.  So as far as Sage is concerned, the licence is GPLv3+ and that's it.


---

Comment by dimpase created at 2010-11-10 12:51:50

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2010-11-10 12:51:50

Replying to [comment:113 jdemeyer]:
> Replying to [comment:109 dimpase]:
> > Would you agree to the following text in SPKG.txt?
> > 
> > {{{
> > == License ==
> > GPLv3 or later. Includes parts under GPLv2, 
> > GNU Lesser General Public License, v2.1. See src/LICENSE for more details.
> > (Sage-compatible)
> > }}}
> 
> Yes.

the updated spkg is here:
http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.3.spkg

only the licence section of SPKG.txt has been changed.


---

Comment by drkirkby created at 2010-11-10 13:15:04

Replying to [comment:112 dimpase]:
> Replying to [comment:111 drkirkby]:
> > 
> > I have some recollection that the cvxopt authors were going to incorporate my Solaris patch, so given this has ticket has been changed from using version 1.1.2 to using 1.1.3, I'm puzzled that does not appear to have happened. 
> 
> They wanted to look into it, that's all. I guess this has become even more irrelevant, as I don't even have a machine where to test this patch any more. They are probably in the same position.

I've just set up t2.math after Williams screwed it by removing the NFS shares it depends on. I've not announced it yet, since I have not fully built Sage (it's building ATLAS now). But hopefully that situation will not exist any longer. 
 
> How about we upgrade this now, and then fix remaining issues in TODO in new ticket(s)? I need this stuff, and I am sick and tired of extra manual labour I need to do in order to use this version of cvxopt....
> 
> Dima

Well, personally I don't think testing the *new* functionality should be left to a TODO. There's not a single test of the GLPK working with CVXOPT. We have made changes to allow them to be used together, but not tested that they actually work. I think that's bad practice myself. 

Would it take you long to write a few doctests which show how to use GLPK with CVXOPT? 

Dave


---

Comment by drkirkby created at 2010-11-10 13:15:04

Changing status from needs_review to needs_info.


---

Comment by dimpase created at 2010-11-10 14:06:18

Replying to [comment:116 drkirkby]:
> Replying to [comment:112 dimpase]:
> > Replying to [comment:111 drkirkby]:
> > > 
> > > I have some recollection that the cvxopt authors were going to incorporate my Solaris patch, so given this has ticket has been changed from using version 1.1.2 to using 1.1.3, I'm puzzled that does not appear to have happened. 
> > 
> > They wanted to look into it, that's all. I guess this has become even more irrelevant, as I don't even have a machine where to test this patch any more. They are probably in the same position.
> 
> I've just set up t2.math after Williams screwed it by removing the NFS shares it depends on. I've not announced it yet, since I have not fully built Sage (it's building ATLAS now). But hopefully that situation will not exist any longer. 
>  
> > How about we upgrade this now, and then fix remaining issues in TODO in new ticket(s)? I need this stuff, and I am sick and tired of extra manual labour I need to do in order to use this version of cvxopt....
> > 
> > Dima
> 
> Well, personally I don't think testing the *new* functionality should be left to a TODO. There's not a single test of the GLPK working with CVXOPT. We have made changes to allow them to be used together, but not tested that they actually work. I think that's bad practice myself. 
> 
> Would it take you long to write a few doctests which show how to use GLPK with CVXOPT? 

I had them already written. :-) Please see and test the patch (tested on Debian x64 and on your Sun).

Dima


> 
> Dave


---

Comment by dimpase created at 2010-11-10 14:06:18

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-11-10 17:59:41

Hi Dima, a few points:

 * You have addressed most of the concerns I had 
   * The bug Peter found has been fixed. 
   * The Solaris/GCC bug has been resolved. 
   * There's now some doc tests testing the GLPK interface. 

 * I personally don't have the maths knowledge to review this properly. 

If I understand this correctly, the default solver gives a result of 6.2499999 and GLPK gives 6.25. These two are very similar, so although I've got no idea what sort of relative error can be expected of the different solvers, intuitively it looks like the two solvers are agreeing with each other. 

I've got no idea if the answer is right though! Is there any theoretical reason for accepting these answers? Or is the answer accepted just because that what's the computer gives? If it was possible to compute this in another way (perhaps using Mathematica or something like that), or better still a theoretical explanation of why it is right, it would give me personally more confidence. I really dislike numerical results which are not substantiated in any way. 

Of course, we are using two solvers here, but part of the code is common. 

Another concern I have is that the doctest might not be too good across multiple platforms. It would never surprise me, if on another CPU, the GLPK solver gave something like 6.2499999 instead of 6.25. Making the doctest accept any value starting with 6.2 would be silly, as that could allow huge errors to pass. But I don't know how best to handle this. This seems a weakness in the way we doctest. Assuming the real answer is 6.25, we really want something that will accept any x such that abs(x-6.25) < 1e-6 or something like that. 

I don't know what this does on SPARC ('mark' or 'mark2' on skynet), but I'd not be too surprised if the answers came out slightly differently. My Sun you tested on is not a SPARC processor, but an Intel Xeon. 

Overall I'm a *lot* happier with this than I was a few months ago, but don't have the maths knowledge to review it properly and have some concerns about the numerical results for the doctest. 

Dave


---

Comment by dimpase created at 2010-11-10 18:52:03

Replying to [comment:118 drkirkby]:

> If I understand this correctly, the default solver gives a result of 6.2499999 and GLPK gives 6.25. These two are very similar, so although I've got no idea what sort of relative error can be expected of the different solvers, intuitively it looks like the two solvers are agreeing with each other. 

these two solvers use rather different algorithms. The default solver uses an interior point method, and GLPK uses a simplex method. The latter is exact, the former is approximate. The exactness of the simplex method is not an absolute given though, as GLPK uses floating points to compute with, essentially, rational data. On this particular example it seems to have enough precision to give the exact answer.


> 
> I've got no idea if the answer is right though! Is there any theoretical reason for accepting these answers? Or is the answer accepted just because that what's the computer gives? If it was possible to compute this in another way (perhaps using Mathematica or something like that), or better still a theoretical explanation of why it is right, it would give me personally more confidence. I really dislike numerical results which are not substantiated in any way. 


This can be checked using the outputs of the solvers (so called complementary slackness condition). 

```
sage: v=vector([-1.0,-1.0,-1.0])
sage: m=matrix([[50.0,24.0,0.0],[30.0,33.0,0.0],[-1.0,0.0,0.0],[0.0,-1.0,0.0],[0.0,0.0,1.0],[0.0,0.0,-1.0
....: ]])
sage: h=vector([2400.0,2100.0,-45.0,-5.0,1.0,-1.0])
sage: sol=linear_program(v,m,h,solver='glpk')
GLPK Simplex Optimizer, v4.44
6 rows, 3 columns, 8 non-zeros
Preprocessing...
2 rows, 2 columns, 4 non-zeros
Scaling...
 A: min|aij| =  2.400e+01  max|aij| =  5.000e+01  ratio =  2.083e+00
GM: min|aij| =  8.128e-01  max|aij| =  1.230e+00  ratio =  1.514e+00
EQ: min|aij| =  6.606e-01  max|aij| =  1.000e+00  ratio =  1.514e+00
Constructing initial basis...
Size of triangular part = 2
*     0: obj =  -5.100000000e+01  infeas =  0.000e+00 (0)
*     1: obj =  -5.225000000e+01  infeas =  0.000e+00 (0)
OPTIMAL SOLUTION FOUND
sage: sol
{'status': 'optimal', 's': (-3.8369307731e-13, 543.75, 0.0, 1.25, 0.0, 0.0), 'primal objective': -52.250000000000014, 'y': (), 'x': (45.0, 6.25, 1.0), 'z': (0.0416666666667, -0.0, 1.08333333333, -0.0, 1.0, -0.0)}
sage: sol['s']*sol['z']
-1.59872115546e-14
sage: sol=linear_program(v,m,h)
sage: sol
{'status': 'optimal', 's': (1.26732907086e-07, 543.750000521, 1.09482003526e-08, 1.24999997812, 1.89761395929e-09, 2.07552470867e-09), 'primal objective': -52.249999985182768, 'y': (), 'x': (45.000000009, 6.24999997613, 1.00000000009), 'z': (0.0416666686307, 3.3075453137e-11, 1.08333341676, 3.70511110788e-08, 11.1479097616, 10.1479097616)}
sage: sol['s']*sol['z']
1.2365642167e-07
```

(the fact that `sol['s']*sol['z']` is 0.0 (well, with an acceptable error, for both solvers, although the default server could be tuned a bit better) is that complementary slackness condition in action)

But this is more coding, if done properly.
In fact, a function checking these should become a part of the library.
In this case, however, I am positive the answers are correct, and I can call myself an expert on this stuff :-)

Dima


---

Comment by drkirkby created at 2010-11-11 12:39:25

Dima, 

I don't have the maths knowledge to fully understand all this, but you are an expert in this area, so I'm going to accept all what you say. 

I'm not convinced the GPLK doctest will necessarily pass on Solaris 10 SPARC systems, due to different rounding issues. As you note, GPLK does give an exact answer on my Intel system and your system. However, it's far from obvious this will give the exact answer on SPARC, due to differences in the rounding of the floating point processors. The Intel/AMD use 80-bits for intermediate calculations, whereas SPARC uses 64. All processors return their answers using 64-bits. 

If you can test this on a Solaris 10 SPARC system, showing the 

 * The doctests pass 
 * The package's set-test pass (set `SAGE_CHECK=yes` when building cvxopt)

then I'm willing to give this a positive review! You can use 'mark', 'mark2' or t2.math for testing on Solaris 10 SPARC. 

If you use t2.math, you can set `SAGE_ATLAS_LIB=/usr/local/ATLAS32` which should mean that  ATLAS does not have to be built, so the build time will be significantly reduced. (I've just built the whole of Sage on t2.math, and have copied the necessary 32-bit ATLAS files to /usr/local/ATLAS32). I have not built Sage using those files, but I'm pretty confident that setting `SAGE_ATLAS_LIB` will work. If not, ATLAS will have to be built, but I doubt that will be necessary. So it should be possible to build Sage on t2.math in a few hours. 

Note Mercurial is not currently installed on t2.math, so it might be easier if you create a patched tar file and copy that over. I will install a new Python and Mercurial at some point on t2.math, but this is not yet set up. I only got t2.math working today after William messed it up. 

Sorry, I don't have time to test this myself, but if you can show the packages self-tests and the doctests pass on Solaris 10 SPARC, I'll give this a positive review. 

The ticket has been open for 17 months, but it should be possible to get a positive review in well under 17 hours! 

Dave


---

Comment by drkirkby created at 2010-11-11 12:39:25

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2010-11-11 14:36:59

If this hasn't been tested on OS X 10.4 PPC, I'm glad to do it.  I'll go ahead and install the packge on 4.6.1.alpha0, but it's not clear to me what other patches need to be imported.  In general, someone should clean up the Description - for instance, it has the wrong link to the spkg.


---

Comment by kcrisman created at 2010-11-11 14:46:13

Is there something else that needs to be upgraded with this?  I get the following installing this package on 4.6.alpha0 (not a build from scratch, though):

```
building 'gsl' extension
creating build/temp.macosx-10.4-ppc-2.6
creating build/temp.macosx-10.4-ppc-2.6/C
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/student/Desktop/sage-4.6/local/include -I/Users/student/Desktop/sage-4.6/local/include -I/Users/student/Desktop/sage-4.6/local/include/python2.6 -c C/gsl.c -o build/temp.macosx-10.4-ppc-2.6/C/gsl.o
gcc -L/Users/student/Desktop/sage-4.6/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.4-ppc-2.6/C/gsl.o -L/Users/student/Desktop/sage-4.6/local/lib -lm -llapack -lgsl -lgslcblas -lblas -lcblas -latlas -lgsl -o build/lib.macosx-10.4-ppc-2.6/cvxopt/gsl.so
/usr/bin/ld: can't locate file for: -lcblas
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1
Error building/installing cvxopt

```

I don't know what this error means - I guess it have something to do with linking.


---

Comment by dimpase created at 2010-11-11 15:18:33

Replying to [comment:122 kcrisman]:
> Is there something else that needs to be upgraded with this?  I get the following installing this package on 4.6.alpha0 (not a build from scratch, though):
> {{{
> building 'gsl' extension
> creating build/temp.macosx-10.4-ppc-2.6
> creating build/temp.macosx-10.4-ppc-2.6/C
> gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/student/Desktop/sage-4.6/local/include -I/Users/student/Desktop/sage-4.6/local/include -I/Users/student/Desktop/sage-4.6/local/include/python2.6 -c C/gsl.c -o build/temp.macosx-10.4-ppc-2.6/C/gsl.o
> gcc -L/Users/student/Desktop/sage-4.6/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.4-ppc-2.6/C/gsl.o -L/Users/student/Desktop/sage-4.6/local/lib -lm -llapack -lgsl -lgslcblas -lblas -lcblas -latlas -lgsl -o build/lib.macosx-10.4-ppc-2.6/cvxopt/gsl.so
> /usr/bin/ld: can't locate file for: -lcblas
> collect2: ld returned 1 exit status
> error: command 'gcc' failed with exit status 1
> Error building/installing cvxopt
> 
> }}}
> I don't know what this error means - I guess it have something to do with linking.  

It does. There is not SAGE_LOCAL/lib/libcblas* on MacOSX PPC (however linking works for me on MacOSX 10.5 PPC)
Please try the new, just updated, spkg. (Both on PPC and on MacOSX x86, if possible).

Dima


---

Comment by kcrisman created at 2010-11-11 15:28:50

On the 10.4 PPC:

```
building 'gsl' extension
creating build/temp.macosx-10.4-ppc-2.6
creating build/temp.macosx-10.4-ppc-2.6/C
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/student/Desktop/sage-4.6/local/include -I/Users/student/Desktop/sage-4.6/local/include -I/Users/student/Desktop/sage-4.6/local/include/python2.6 -c C/gsl.c -o build/temp.macosx-10.4-ppc-2.6/C/gsl.o
gcc -L/Users/student/Desktop/sage-4.6/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.4-ppc-2.6/C/gsl.o -L/Users/student/Desktop/sage-4.6/local/lib -lm -llapack -lgsl -lgslcblas -lblas -latlas -lgsl -o build/lib.macosx-10.4-ppc-2.6/cvxopt/gsl.so
/usr/bin/ld: can't locate file for: -latlas
collect2: ld returned 1 exit status
```

I have a feeling there are a few things that it won't be finding :) but of course these libraries exist, right?

I don't have 10.4 Intel, but I can try it on 10.6 Intel once this works.  I don't have time to check this, but I assume you're also keeping track of these on the SPKG.txt and diffs :)


---

Comment by dimpase created at 2010-11-11 15:51:58

Replying to [comment:125 kcrisman]:
> On the 10.4 PPC:
> {{{
> building 'gsl' extension
> creating build/temp.macosx-10.4-ppc-2.6
> creating build/temp.macosx-10.4-ppc-2.6/C
> gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/student/Desktop/sage-4.6/local/include -I/Users/student/Desktop/sage-4.6/local/include -I/Users/student/Desktop/sage-4.6/local/include/python2.6 -c C/gsl.c -o build/temp.macosx-10.4-ppc-2.6/C/gsl.o
> gcc -L/Users/student/Desktop/sage-4.6/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.4-ppc-2.6/C/gsl.o -L/Users/student/Desktop/sage-4.6/local/lib -lm -llapack -lgsl -lgslcblas -lblas -latlas -lgsl -o build/lib.macosx-10.4-ppc-2.6/cvxopt/gsl.so
> /usr/bin/ld: can't locate file for: -latlas
> collect2: ld returned 1 exit status
> }}}

> I have a feeling there are a few things that it won't be finding :) but of course these libraries exist, right?

no, they don't exist on MacOSX PPC! I don't know about MacOSX Intel, as I don't have such a machine yet.
Moreover, on my 10.5 PPC linker is not bothered by nonexistence of these libraries.
So this is an artefact of old hard- and soft-ware. What a bloody mess...
Could you tell me the result of the following on your 10.4:

```
$ sage -python
>>> import os
>>> os.uname()
```

so that  I can code this into setup.py of the package...

Dima



> 
> I don't have 10.4 Intel, but I can try it on 10.6 Intel once this works.  I don't have time to check this, but I assume you're also keeping track of these on the SPKG.txt and diffs :)


---

Comment by kcrisman created at 2010-11-11 16:26:13

You might want to look at the ticket #8664 for upgrading MPIR for some discussion of this - I think you've been involved on that ticket as well.

```
Dasher-03:~/Desktop/sage-4.6 student$ uname -m
Power Macintosh
Dasher-03:~/Desktop/sage-4.6 student$ uname -a
Darwin Dasher-03.local 8.11.0 Darwin Kernel Version 8.11.0: Wed Oct 10 18:26:00 PDT 2007; root:xnu-792.24.17~1/RELEASE_PPC Power Macintosh powerpc
```

and what you expected on sage-devel under Python.


---

Comment by kcrisman created at 2010-11-11 16:35:49

By the way, of 

```
-lm -llapack -lgsl -lgslcblas -lblas -lcblas -latlas -lgsl
```

if they should all be in `$SAGE_LOCAL/lib`, then I have 

```
liblapack.a
libgsl.a       
libgsl.dylib   
libgsl.la      
libgslcblas.a
libgslcblas.dylib
libgslcblas.la
libblas.a     
```

Maybe that helps.  Where does libcblas come from in other systems?  It's not a Sage package, and the BLAS spkg-install only installs libblas.a, as far as I can tell.


---

Comment by mhansen created at 2010-11-11 16:47:05

I believe libcblas comes from ATLAS which we do not install on OS X.  I had referred to (hinted at) these BLAS issues on OSX before in http://trac.sagemath.org/sage_trac/ticket/6456#comment:64 .


---

Comment by dimpase created at 2010-11-11 17:06:31

Replying to [comment:128 kcrisman]:
> By the way, of 
> {{{
> -lm -llapack -lgsl -lgslcblas -lblas -lcblas -latlas -lgsl
> }}}
if they should all be in `$SAGE_LOCAL/lib`, then I have 

```
 liblapack.a
 libgsl.a       
 libgsl.dylib   
 libgsl.la      
 libgslcblas.a
 libgslcblas.dylib
 libgslcblas.la
 libblas.a     
 }}}

sure, I have the same.

> Maybe that helps.  Where does libcblas come from in other systems?  It's not a Sage package, and the BLAS spkg-install only installs libblas.a, as far as I can tell.

On my machine I have, surely coming from Xcode (part of Accelerate framework, formerly altVec...): 
{{{
$ ls -l /usr/lib/*cblas*
lrwxr-xr-x 1 root wheel 112 Apr 12  1976 /usr/lib/libcblas.dylib -> ../..//System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libBLAS.dylib
$ ls -l /usr/lib/*atlas*
lrwxr-xr-x 1 root wheel 112 Apr 12  1976 /usr/lib/libatlas.dylib -> ../..//System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libBLAS.dylib
$ ls -l /usr/lib/*lapack*
lrwxr-xr-x 1 root wheel 114 Apr 12  1976 /usr/lib/libclapack.dylib -> ../..//System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libLAPACK.dylib
lrwxr-xr-x 1 root wheel 114 Apr 12  1976 /usr/lib/libf77lapack.dylib -> ../..//System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libLAPACK.dylib
lrwxr-xr-x 1 root wheel 114 Apr 12  1976 /usr/lib/liblapack.dylib -> ../..//System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libLAPACK.dylib
}}}
These are platform-optimised libraries, that should be used on MacOSX.
So your linker trouble seems to be a sign of Xcode not being properly installed, or that your Xcode is much older than mine, and the directories layout has changed.

Do you have anything like this in /usr/lib ?

But anyway, one just have to link against the native libraries.
What does your gcc -v say? In my case:
{{{
$ gcc -v
Using built-in specs.
Target: powerpc-apple-darwin9
Configured with: /var/tmp/gcc_42/gcc_42-5577~1/src/configure --disable-checking --prefix=/usr --mandir=/usr/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin9 --with-gxx-include-dir=/usr/include/c++/4.0.0 --program-prefix= --host=powerpc-apple-darwin9 --target=powerpc-apple-darwin9
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5577)
}}}
So you see with-slibdir=/usr/lib there, so this must mean that it picks up these libcblas, etc, there.


---

Comment by kcrisman created at 2010-11-11 17:18:39

> These are platform-optimised libraries, that should be used on MacOSX.
Yes.  Well, not the lapack, which we don't.
> So your linker trouble seems to be a sign of Xcode not being properly installed, or that your Xcode is much older than mine, and the directories layout has changed.
Yes.

> 
> Do you have anything like this in /usr/lib ?
> 
> But anyway, one just have to link against the native libraries.
> What does your gcc -v say? In my case:
Same.

Here are some things I get:

```
Dasher-03:~ student$ ls /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/
Headers          libBLAS.dylib    libvDSP.dylib    vecLib
Resources        libLAPACK.dylib  libvMisc.dylib   
Dasher-03:~ student$ ls /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/Headers/
cblas.h                 vBigNum.h               vecLib.h
clapack.h               vDSP.h                  vecLibTypes.h
vBLAS.h                 vDSP_translate.h        vectorOps.h
vBasicOps.h             vForce.h                vfp.h
Dasher-03:~ student$ ls -l /usr/lib/*atlas*ls: /usr/lib/*atlas*: No such file or directory
Dasher-03:~ student$ ls -l /usr/lib/*cblas*ls: /usr/lib/*cblas*: No such file or directory
```



---

Comment by dimpase created at 2010-11-11 17:36:51

Replying to [comment:131 kcrisman]:
> 
> > These are platform-optimised libraries, that should be used on MacOSX.
> Yes.  Well, not the lapack, which we don't.
> > So your linker trouble seems to be a sign of Xcode not being properly installed, or that your Xcode is much older than mine, and the directories layout has changed.
> Yes.
> 
> > 
> > Do you have anything like this in /usr/lib ?
> > 
> > But anyway, one just have to link against the native libraries.
> > What does your gcc -v say? In my case:
> Same.
> 
> Here are some things I get:
> {{{
> Dasher-03:~ student$ ls /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/
> Headers          libBLAS.dylib    libvDSP.dylib    vecLib
> Resources        libLAPACK.dylib  libvMisc.dylib   
> Dasher-03:~ student$ ls /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/Headers/
> cblas.h                 vBigNum.h               vecLib.h
> clapack.h               vDSP.h                  vecLibTypes.h
> vBLAS.h                 vDSP_translate.h        vectorOps.h
> vBasicOps.h             vForce.h                vfp.h
> Dasher-03:~ student$ ls -l /usr/lib/*atlas*ls: /usr/lib/*atlas*: No such file or directory
> Dasher-03:~ student$ ls -l /usr/lib/*cblas*ls: /usr/lib/*cblas*: No such file or directory
> }}}

I also removed atlas from the list of libraries to be linked on Darwin, and uploaded the updated spkg. Please test on OSX, both PPC and Intel. Thanks!

Dima


---

Comment by mhansen created at 2010-11-11 17:41:49

Can we also remove gslcblas which is quite slow?


---

Comment by kcrisman created at 2010-11-11 17:50:13

Replying to [comment:133 mhansen]:
> Can we also remove gslcblas which is quite slow?
Would that be a different ticket? I'm confused.

`@`dima - testing!  It already made it past the first few extensions, so that's a good sign.


---

Comment by mhansen created at 2010-11-11 17:59:03

Replying to [comment:134 kcrisman]:
> Replying to [comment:133 mhansen]:
> > Can we also remove gslcblas which is quite slow?
> Would that be a different ticket? I'm confused.

I mean make it so that CVXOPT never tries to link against it.


---

Comment by kcrisman created at 2010-11-11 18:13:34

Replying to [comment:135 mhansen]:
> Replying to [comment:134 kcrisman]:
> > Replying to [comment:133 mhansen]:
> > > Can we also remove gslcblas which is quite slow?
> > Would that be a different ticket? I'm confused.
> 
> I mean make it so that CVXOPT never tries to link against it.
Okay, as in your earlier comment.


---

Comment by kcrisman created at 2010-11-11 18:49:01

I tested sage/numerical/ and got only a couple failures, but they look ominous - all of this type, where it can't find a symbol with g95.  Which is weird, because of course I used G95 to compile this Sage.

```
sage -t  "devel/sage/sage/numerical/optimize.py"            
**********************************************************************
File "/Users/student/Desktop/sage-4.6/devel/sage/sage/numerical/optimize.py", line 468:
    sage: sol=linear_program(c,G,h)
Exception raised:
    Traceback (most recent call last):
      File "/Users/student/Desktop/sage-4.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[5]>", line 1, in <module>
        sol=linear_program(c,G,h)###line 468:
    sage: sol=linear_program(c,G,h)
      File "/Users/student/Desktop/sage-4.6/local/lib/python/site-packages/sage/numerical/optimize.py", line 485, in linear_program
        from cvxopt.base import matrix as m
      File "/Users/student/Desktop/sage-4.6/local/lib/python/site-packages/cvxopt/__init__.py", line 31, in <module>
        import base
    ImportError: dlopen(/Users/student/Desktop/sage-4.6/local/lib/python/site-packages/cvxopt/base.so, 2): Symbol not found: __g95_stop_blank
      Referenced from: /Users/student/Desktop/sage-4.6/local/lib/python/site-packages/cvxopt/base.so
      Expected in: dynamic lookup
**********************************************************************
File "/Users/student/Desktop/sage-4.6/devel/sage/sage/numerical/test.py", line 4:
    sage: from cvxopt.base import *
Exception raised:
    Traceback (most recent call last):
      File "/Users/student/Desktop/sage-4.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        from cvxopt.base import *###line 4:
    sage: from cvxopt.base import *
      File "/Users/student/Desktop/sage-4.6/local/lib/python/site-packages/cvxopt/__init__.py", line 31, in <module>
        import base
    ImportError: dlopen(/Users/student/Desktop/sage-4.6/local/lib/python/site-packages/cvxopt/base.so, 2): Symbol not found: __g95_st_write_done
      Referenced from: /Users/student/Desktop/sage-4.6/local/lib/python/site-packages/cvxopt/base.so
      Expected in: dynamic lookup

```



---

Comment by dimpase created at 2010-11-12 06:26:25

Replying to [comment:137 kcrisman]:
> I tested sage/numerical/ and got only a couple failures, but they look ominous - all of this type, where it can't find a symbol with g95.  Which is weird, because of course I used G95 to compile this Sage.

well, an old gcc toolchain (?): g95 somehow doesn't know where to look for its own libf95.a
(it worked for me, also with g95...)
This should be fixed in  just uploaded update of  the spkg.
Could you please test it?

(also, if it builds, could you try building it with SAGE_CHECK=yes, too ?)


---

Comment by dimpase created at 2010-11-12 06:27:44

Replying to [comment:133 mhansen]:
> Can we also remove gslcblas which is quite slow?

removed in the update. Please test...


---

Comment by dimpase created at 2010-11-12 09:32:34

Replying to [comment:118 drkirkby]:



> 
> Another concern I have is that the doctest might not be too good across multiple platforms. It would never surprise me, if on another CPU, the GLPK solver gave something like 6.2499999 instead of 6.25. Making the doctest accept any value starting with 6.2 would be silly, as that could allow huge errors to pass. But I don't know how best to handle this. This seems a weakness in the way we doctest. Assuming the real answer is 6.25, we really want something that will accept any x such that abs(x-6.25) < 1e-6 or something like that. 
> 
> I don't know what this does on SPARC ('mark' or 'mark2' on skynet), but I'd not be too surprised if the answers came out slightly differently. My Sun you tested on is not a SPARC processor, but an Intel Xeon. 

Just tested on t2, on Sage 4.6, with SAGE_CHECK=yes, and the tests in sage/numerical/optimize.py, all works.
(Actually, it already worked on PPC, which is also not an 80-bit floating point, but only 64...)

Now waiting for OSX 10.4 results, and hopefully MacOSX Intel, too.

Dima


---

Comment by kcrisman created at 2010-11-12 15:56:32

> well, an old gcc toolchain (?): g95 somehow doesn't know where to look for its own libf95.a
> (it worked for me, also with g95...)
> This should be fixed in  just uploaded update of  the spkg.
> Could you please test it?
Builds.
> (also, if it builds, could you try building it with SAGE_CHECK=yes, too ?)
With `SAGE_CHECK=yes` I get a whole bunch of errors, all looking for the same thing - like this one:

```
Error: /Users/student/Desktop/sage-4.6/local/bin/python l2ac.py failed
Testing  robls.py ...
Traceback (most recent call last):
  File "robls.py", line 5, in <module>
    from cvxopt import solvers, blas, lapack
  File "/Users/student/Desktop/sage-4.6/local/lib/python2.6/site-packages/cvxopt/__init__.py", line 31, in <module>
    import base
ImportError: dlopen(/Users/student/Desktop/sage-4.6/local/lib/python2.6/site-packages/cvxopt/base.so, 2): Symbol not found: _cblas_zhemm
  Referenced from: /Users/student/Desktop/sage-4.6/local/lib//libgsl.0.dylib
  Expected in: dynamic lookup
```

All of these ask about `_cblas_zhemm`.

Testing sage/numerical gives me all tests passed, though.

Is there any other part of Sage which would conceivably depend on these changes at all?  Testing the whole thing on this computer would take until Monday.


---

Comment by kcrisman created at 2010-11-12 16:11:03

I can't test it on OS X 10.6 Intel because I have upgraded in place so much and get things like

```
gcc -L/Users/.../sage-4.6/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.6-i386-2.6/C/gsl.o -L/Users/.../sage-4.6.1.alpha0/local/lib
```

with an error that they can't find the sage-4.6 folder - which makes sense, because it's not there.  So someone else might have to test this.  

Just to put this down, the previous cvxopt didn't have an spkg-check, I guess, because I reinstalled that and it successfully reinstalled (on the PPC machine).   Hopefully this issue is really easy to fix; it would be a shame to upgrade cvxopt without it passing its new check, though on the balance it sounds like having this ancient of cvxopt is tantamount to being even worse than that.


---

Comment by drkirkby created at 2010-11-12 16:51:20

Replying to [comment:141 kcrisman]:
 
> Is there any other part of Sage which would conceivably depend on these changes at all?  Testing the whole thing on this computer would take until Monday.

Do you have an account on bsd.math? If not, ask William for one. That is not a speed daemon, but its an Mac with an Intel CPU running 10.6. It takes a few hours, but not days to test Sage on that.


---

Comment by kcrisman created at 2010-11-12 17:42:16

Replying to [comment:143 drkirkby]:
> Replying to [comment:141 kcrisman]:
>  
> > Is there any other part of Sage which would conceivably depend on these changes at all?  Testing the whole thing on this computer would take until Monday.
> 
> Do you have an account on bsd.math? If not, ask William for one. That is not a speed daemon, but its an Mac with an Intel CPU running 10.6. It takes a few hours, but not days to test Sage on that. 

Sorry, that's irrelevant - this is for the OS X 10.4 PPC.  I think one of the skynet ones has this (?) but I'm not interested in, nor probably qualified for, access to that.  My best work happens on machines I have physical access to :)


---

Comment by dimpase created at 2010-11-12 18:43:08

Replying to [comment:141 kcrisman]:
> > well, an old gcc toolchain (?): g95 somehow doesn't know where to look for its own libf95.a
> > (it worked for me, also with g95...)
> > This should be fixed in  just uploaded update of  the spkg.
> > Could you please test it?
> Builds.
> > (also, if it builds, could you try building it with SAGE_CHECK=yes, too ?)
> With `SAGE_CHECK=yes` I get a whole bunch of errors, all looking for the same thing - like this one:

```
 Error: /Users/student/Desktop/sage-4.6/local/bin/python l2ac.py failed
Testing  robls.py ...
Traceback (most recent call last):
 File "robls.py", line 5, in <module>
     from cvxopt import solvers, blas, lapack
   File "/Users/student/Desktop/sage-4.6/local/lib/python2.6/site-packages/cvxopt/__init__.py", line 31, in <module>
     import base
 ImportError: dlopen(/Users/student/Desktop/sage-4.6/local/lib/python2.6/site-packages/cvxopt/base.so, 2): Symbol not found: _cblas_zhemm
   Referenced from: /Users/student/Desktop/sage-4.6/local/lib//libgsl.0.dylib
   Expected in: dynamic lookup
```

> All of these ask about `_cblas_zhemm`.

Most probably this is due to missing gslcblas in the list of libraries to link. I've put it back in and uploaded the updated
spkg. Please test! (with SAGE_CHECK=yes, naturally).
Thanks.

> 
> Testing sage/numerical gives me all tests passed, though.
> 
> Is there any other part of Sage which would conceivably depend on these changes at all?  Testing the whole thing on this computer would take until Monday.

No, there is no need to test anything else; the only exposure to cvxopt is in sage/numerical/optimize.py.

Dima


---

Comment by kcrisman created at 2010-11-12 21:12:27

Well, this latest one installed normally, which is good.  So far the test suite hasn't failed, which is also good.  However, it seems to be taking a long time (>10 minutes) for the first file

```
Successfully installed cvxopt-1.1.3
Running the test suite.
Testing in src/examples/doc/chap10 
Testing  l1svc.py ...
```

and unfortunately I need to leave now to catch my train before it's too dark to bike without lights.  So Monday morning you will find out whether this has worked.  Eventually I will learn how to ssh tunnel into this computer, but I don't have time to do so right now :)  

At any rate this is a good sign.  I might also get to build a brand-new alpha on OS X 10.6 eventually and test this there too.  Good luck! 

What else needs to be done for positive review - have all the license etc. issues been resolved?


---

Comment by dimpase created at 2010-11-14 13:09:29

Replying to [comment:146 kcrisman]:
> Well, this latest one installed normally, which is good.  So far the test suite hasn't failed, which is also good.  However, it seems to be taking a long time (>10 minutes) for the first file

> At any rate this is a good sign.  I might also get to build a brand-new alpha on OS X 10.6 eventually and test this there too.  Good luck! 
> 

I got an account on bsd.math and tested on OSX 10.4 Intel. I had to change the way the package detects which fortran compiler is used, so this is now done without resorting to checking for platforms (Darwin, etc) at all.
So after these changes it tested OK on OSX10.4 Intel, OSX10.5 PPC, Solaris (t2) and Debian x64.
The updated version is uploaded.

At any rate, a test on OSX 10.6 would be great to have.



> What else needs to be done for positive review - have all the license etc. issues been resolved?


---

Comment by jhpalmieri created at 2010-11-14 15:51:34

Replying to [comment:147 dimpase]:
> I got an account on bsd.math and tested on OSX 10.4 Intel. I had to change the way the package detects which fortran compiler is used, so this is now done without resorting to checking for platforms (Darwin, etc) at all.
> So after these changes it tested OK on OSX10.4 Intel, OSX10.5 PPC, Solaris (t2) and Debian x64.
> The updated version is uploaded.
> 
> At any rate, a test on OSX 10.6 would be great to have.

bsd.math runs 10.6, not 10.4.  You might have been confused because of the output of "uname", more particularly "uname -r":

```
bsd:~ palmieri$ uname -r
10.4.0
```

The "10" corresponds somehow to OS X 10.6, and the "4" means it's running OS X 10.6.4.  (OS X 10.4 would return "8.???" and OS X 10.5 would return "9.???".)


---

Comment by drkirkby created at 2010-11-14 18:26:49

Replying to [comment:148 jhpalmieri]:
> Replying to [comment:147 dimpase]:
> > I got an account on bsd.math and tested on OSX 10.4 Intel. I had to change the way the package detects which fortran compiler is used, so this is now done without resorting to checking for platforms (Darwin, etc) at all.
> > So after these changes it tested OK on OSX10.4 Intel, OSX10.5 PPC, Solaris (t2) and Debian x64.
> > The updated version is uploaded.
> > 
> > At any rate, a test on OSX 10.6 would be great to have.
> 
> bsd.math runs 10.6, not 10.4.  You might have been confused because of the output of "uname", more particularly "uname -r":
> {{{
> bsd:~ palmieri$ uname -r
> 10.4.0
> }}}
> The "10" corresponds somehow to OS X 10.6, and the "4" means it's running OS X 10.6.4.  (OS X 10.4 would return "8.???" and OS X 10.5 would return "9.???".)

Why the hell do the operating systems do this. Solaris is just as bad. 

This is Solaris 10

```
kirkby`@`t2:64 ~$ uname -r
5.10
```


and AIX 6.1

```
$ uname -r
1
$ uname -a
AIX lpar5 1 6 00C6B7C04C00
```


Linux is no better 

```
kirkby`@`sage:~$ uname -r
2.6.24-28-server
```


I can't recall if HP-UX is a bit more sensible, and can't be bothered to switch on my HP-UX machine to find out. 
</gripe>


---

Comment by jdemeyer created at 2010-11-15 12:18:27

Patch for spkg/standard/deps assuming #9418 has been applied


---

Attachment

Please make it clear which patches have to be applied.  I am assuming the following, but I can't be sure:

 1. [attachment:6456-numerical_sage_cvxopt.patch]
 1. [attachment:6456-cvxopt-glpk-interface.patch]
 1. [attachment:6456_after_9418_deps.patch] (assuming #9418 is merged of course)

Also, you should change the commit message of the patches (use `hg qrefresh -e` for that) such that the first line contains the ticket number and a short description of the patch (you may use following lines for a longer description).


---

Comment by dimpase created at 2010-11-15 13:19:52

option to linear_program() to use glpk as the solver


---

Attachment

Replying to [comment:150 jdemeyer]:
> Please make it clear which patches have to be applied.  I am assuming the following, but I can't be sure:
> 
>  1. [attachment:6456-numerical_sage_cvxopt.patch]
>  1. [attachment:6456-cvxopt-glpk-interface.patch]
>  1. [attachment:6456_after_9418_deps.patch] (assuming #9418 is merged of course)
> 

right, only instead of [attachment:6456-numerical_sage_cvxopt.patch] please take [attachment:6456-numerical_sage_cvxopt-with-updated-commitmessage.patch] (I am not its author, so I can't just update).

> Also, you should change the commit message of the patches (use `hg qrefresh -e` for that) such that the first line contains the ticket number and a short description of the patch (you may use following lines for a longer description).

done.

Dima


---

Comment by dimpase created at 2010-11-15 13:29:34

Changing status from needs_info to needs_review.


---

Comment by kcrisman created at 2010-11-15 13:51:30

Just an update - OS X 10.4 (Tiger!) on PPC does pass `SAGE_CHECK=yes` and the tests for sage/numerical.  This was with the original `sage_cvxopt` patch; I only had time to check the output, not to do anything else.  

Presumably cumulative positive review from all the testers plus Dima's OR knowledge, unless the license issue is still a problem.  Maybe someone other than Dima should also quickly check that the spkg is in proper shape, including commit messages - I apologize for not having time to do this, again, just to report in.


---

Comment by jdemeyer created at 2010-11-15 15:32:48

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-11-15 15:32:48

Replying to [comment:151 dimpase]:
> > Also, you should change the commit message of the patches (use `hg qrefresh -e` for that) such that the first line contains the ticket number and a short description of the patch (you may use following lines for a longer description).
> 
> done.

Except that the ticket number in [attachment:6456-numerical_sage_cvxopt-with-updated-commitmessage.patch] is wrong...


---

Comment by dimpase created at 2010-11-15 15:39:56

changes for the doctested examples in the numerical_sage section for cvxopt


---

Comment by dimpase created at 2010-11-15 15:41:37

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:153 jdemeyer]:
> Replying to [comment:151 dimpase]:
> > > Also, you should change the commit message of the patches (use `hg qrefresh -e` for that) such that the first line contains the ticket number and a short description of the patch (you may use following lines for a longer description).
> > 
> > done.
> 
> Except that the ticket number in [attachment:6456-numerical_sage_cvxopt-with-updated-commitmessage.patch] is wrong...

AUB


---

Comment by mpatel created at 2010-11-22 13:51:54

There's a failure with 4.6.1.alpha2 on Skynet's iras (ia64-Linux-suse):

```python
$ ./sage -t -long  -force_lib devel/sage/doc/en/numerical_sage/cvxopt.rst 
sage -t -long -force_lib "devel/sage/doc/en/numerical_sage/cvxopt.rst"
**********************************************************************
File "/tmp/sage_iras/sage-4.6.1.alpha2/devel/sage/doc/en/numerical_sage/cvxopt.rst", line 129:
    sage: print sol['x']      # ... below since can get -00 or +00 depending on architecture
Expected:
    [ 1.00e+00]
    [ 1.00e+00]
Got:
    [ 1.00e-00]
    [ 1.00e+00]
    <BLANKLINE>
```



---

Comment by jdemeyer created at 2010-11-22 14:27:49

Replying to [comment:156 mpatel]:
> There's a failure with 4.6.1.alpha2 on Skynet's iras (ia64-Linux-suse):

Patch at #10309


---

Attachment


---

Comment by kcrisman created at 2010-12-02 16:20:48

Is there anything else that needs to happen for this to get positive review?  I'm unclear on how spkgs merged before positive review finally do get positive review.


---

Comment by jdemeyer created at 2010-12-02 16:55:42

Replying to [comment:158 kcrisman]:
> Is there anything else that needs to happen for this to get positive review?

Somebody should look at the spkg, check that `spkg-install`, `SPKG.txt` make sense, check any patches (I believe there are none in this spkg),...


---

Comment by dimpase created at 2010-12-02 17:15:20

Replying to [comment:159 jdemeyer]:
> Replying to [comment:158 kcrisman]:
> > Is there anything else that needs to happen for this to get positive review?
> 
> Somebody should look at the spkg, check that `spkg-install`, `SPKG.txt` make sense, check any patches (I believe there are none in this spkg),...

Being an author, I am biased, but I think it has been reviewed over and over to near-death already, and found sound enough :-)


---

Comment by kcrisman created at 2010-12-02 17:38:42

Replying to [comment:160 dimpase]:
> Replying to [comment:159 jdemeyer]:
> > Replying to [comment:158 kcrisman]:
> > > Is there anything else that needs to happen for this to get positive review?
> > 
> > Somebody should look at the spkg, check that `spkg-install`, `SPKG.txt` make sense, check any patches (I believe there are none in this spkg),...
> 
> Being an author, I am biased, but I think it has been reviewed over and over to near-death already, and found sound enough :-)
Of course!

I have a brief question about the patches.  The Solaris one and the init one seem fine, and most of the setup.py makes sense for finding Sage-specific things.  

I do have a question about `BUILD_GLPK` being set to 1, since there is a comment that one can only do this if glpk is installed, "optional at this moment".  So will this cause problems?  Apparently not... There is a hanging parenthesis there as well.   Anyway, I'd like to know what that is about.

Also, in SPKG.txt there is a spelling "enchance" instead of "enhance", and "recongnision" instead of "recognition".

Everything else seems to make sense, though I should note I am not a shell script or install expert :)  Still, with no problems reported on 4.6.1.alpha2, perhaps it's time for positive review once those things get resolved.


---

Comment by dimpase created at 2010-12-02 18:10:54

Replying to [comment:161 kcrisman]:

> I do have a question about `BUILD_GLPK` being set to 1, since there is a comment that one can only do this if glpk is installed, "optional at this moment".  So will this cause problems?  Apparently not... There is a hanging parenthesis there as well.   Anyway, I'd like to know what that is about.

Fixed. A leftover from times when GLPK was still optional. Now GLPK is standard.

> 
> Also, in SPKG.txt there is a spelling "enchance" instead of "enhance", and "recongnision" instead of "recognition".
> 

fixed.

> Everything else seems to make sense, though I should note I am not a shell script or install expert :)  Still, with no problems reported on 4.6.1.alpha2, perhaps it's time for positive review once those things get resolved.

OK so the fixes are in the spkg file in the same location.

Thanks for your time,

Dima


---

Comment by kcrisman created at 2010-12-02 18:24:40

Okay, these were just cosmetic changes, and I verified they are in the updated spkg, and it's been tested at a basic level without destroying Sage for a while now, so this should go in.


---

Comment by kcrisman created at 2010-12-02 18:24:40

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-12-02 22:54:06

Since the package is not pure upstream and contains pacthes, I believe it should be renamed to `cvxopt-1.1.3.p0.spkg`.


---

Comment by jdemeyer created at 2010-12-02 22:54:06

Changing status from positive_review to needs_work.


---

Comment by drkirkby created at 2010-12-03 02:45:07

Replying to [comment:164 jdemeyer]:
> Since the package is not pure upstream and contains pacthes, I believe it should be renamed to `cvxopt-1.1.3.p0.spkg`.

I thought this had been debated on sage-devel before, and William's opinion is that it should not be .p0. There's noting in the Sage Developers Guide to say it should be either. As such, I don't think that this is a reasonable reason for putting the ticket to needs work. 

Dave


---

Comment by dimpase created at 2010-12-03 05:58:26

Replying to [comment:164 jdemeyer]:
> Since the package is not pure upstream and contains pacthes, I believe it should be renamed to `cvxopt-1.1.3.p0.spkg`.

I believe the opposite, and was specifically indoctorinated into my belief when I was updating GAP and its GAP-packages spkgs.
Hereby I blatantly change the status to Positive Review :-)


---

Comment by dimpase created at 2010-12-03 05:58:26

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2010-12-03 08:54:42

Resolution: fixed
