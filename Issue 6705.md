# Issue 6705: ATLAS has no tuning parameters for sun4v machines

Issue created by migration from https://trac.sagemath.org/ticket/6705

Original creator: drkirkby

Original creation time: 2009-08-09 09:48:52

Assignee: tbd

CC:  dimpase

Code in ATLAS can not detect the processor type on machines like the Sun T5240 ('t2') as it 

This has been passed upstream

https://sourceforge.net/tracker/?func=detail&aid=2825994&group_id=23725&atid=379483

but there is no fix yet. I probably have enough information to fix this, but have not done so yet. 




---

Comment by drkirkby created at 2009-11-23 00:56:55

This has been closed on the ATLAS tracker, but there is still no solution.


---

Comment by mpatel created at 2010-09-01 10:22:09

If I run `./sage -f -m spkg/standard/atlas-*.spkg` on t2, where can I find the tuning parameters under `spkg/build/atlas-*`?  Can we include them in an updated ATLAS package?  I assume this will speed up the build, but please correct me if I'm wrong.


---

Comment by drkirkby created at 2010-09-01 22:57:02

Replying to [comment:4 mpatel]:
> If I run `./sage -f -m spkg/standard/atlas-*.spkg` on t2, where can I find the tuning parameters under `spkg/build/atlas-*`?  Can we include them in an updated ATLAS package?  I assume this will speed up the build, but please correct me if I'm wrong.

They end up in a .tgz file, but it's not as easy to add them as you might think. I've read the ATLAS documentation, and find it confusing. I even asked on the support tracker, and are still not sure how to do it. Apparently one Sage developer did know how (Micheal) - I don't think anyone else has succeeded! 

I understand the latest ATLAS will build on 't2' in under an hour. However, I don't know if that is for 32-bit, 64-bit or both builds. I somehow suspect it might only be for 64-bit builds, as I suspect it was tested in the default method, which is 64-bit. 

On my own Intel Xeon W5680 processor, I can build ATLAS in under 10 minutes on a 64-bit build, but on a 32-bit build it takes nearly two hours. Clearly the ATLAS package has the tuning parameters for my CPU when built 64-bit, but not when built 32-bit. 

Given ATLAS will by default build 64-bit, I suspect the latest ATLAS will not be any faster. 

I suspect that integrating the 32-bit tuning parameters to the latest ATLAS might be a lot easier than integrating them into the current version. The current code can't detect the CPU type at all, and reports it as "UNKNOWN". I think the new ATLAS should at least know what CPU type this is. 

The problem with updating ATLAS is the package is so messy. I looked at building it in parallel (it's clearly designed for that, and has options specifically for parallel builds), but it failed for me. Given it takes a long time to build if the system is unknown, it would be nice to get parallel builds working. There are special configure options for using a parallel make. 

I'd be tempted to re-write the whole package as /bin/sh shell script. Remove the python, remove the perl. But some might object to that. I can't see why we should have to wait for python to build before building ATLAS - it would be sensible to get ATLAS building as soon as possible. 

If you look at the current build process, there's a very small python script calling a huge bash script. Those few lines of python could be removed I think. (The only small hitch I hit was generating a random number - not sure how to do that in /bin/sh, but it does not need to be a very good random number. In fact, I'm not sure I see the point of starting the build after a random delay myself). Not sure if anyone would like removing Python though. Getting a review of a re-write of spkg-install might be difficult. I'm also keen to avoid the hassle I had with #9603, where wanting to add `&& [ "x$UNAME" != xHP-UX ] ` has made a ticket last 5 weeks. Leif virtually wanted the whole thing re-written. All I *originally* wanted to do was get it to build on HP-UX too! I'm not denying the package is better now, but I don't think it really warranted the work. (I did add a Solaris change a couple of days back, but prior to that, it had dragged on for a month when all I wanted to add was 20 bytes or so). 

I guess we could just drop the latest ATLAS source code in, and hope it works. But I actually doubt it will tune any quicker on 32-bit builds. 

Hopefully, when the 64-bit issues are resolved, there wont be much point in building a 32-bit version of Sage on Solaris. 

How would you feel about a re-write of the build process as a bash script, without a review process that drags on for months? (Hiding it from Leif would be nice!!) 

Dave


---

Comment by mpatel created at 2010-09-02 01:23:01

Replying to [comment:5 drkirkby]:
> The problem with updating ATLAS is the package is so messy. I looked at building it in parallel (it's clearly designed for that, and has options specifically for parallel builds), but it failed for me. Given it takes a long time to build if the system is unknown, it would be nice to get parallel builds working. There are special configure options for using a parallel make. 

Is there a system on which ATLAS does build / tune successfully in parallel?

> I'd be tempted to re-write the whole package as /bin/sh shell script. Remove the python, remove the perl. But some might object to that. I can't see why we should have to wait for python to build before building ATLAS - it would be sensible to get ATLAS building as soon as possible. 

We'll also need to do the same with the Fortran spkg, in order to start building ATLAS earlier in the Sage build process.  If this will help generally and significantly with parallel spkg builds, we _might_ convince others that this worthwhile.  Of course, we'll need to test it well.

Can we use bash and its `$RANDOM`?


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by dimpase created at 2020-07-09 13:38:47

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid
