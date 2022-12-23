# Issue 8951: Clear /tmp/ECL* after building ECL

Issue created by migration from https://trac.sagemath.org/ticket/8951

Original creator: drkirkby

Original creation time: 2010-05-11 20:38:47

Assignee: drkirkby

CC:  was mvngu juanjose.garciaripoll@googlemail.com kcrisman nbruin

As reported here

http://groups.google.com/group/sage-devel/browse_thread/thread/54544d8649bd027a

there is a problem when temp files created during the build of ECL. A correct fix requires changes made to ECL source code, but as a temporary fix, it may be sufficient to remove /tmp/ECL* after building ecl. 




---

Comment by drkirkby created at 2010-05-12 23:54:22

I've attached a patch. It removes the files only on Solaris. It also has a couple of minor corrections 

 * It no longer reports a 32-bit build. Previously it reported a 32-bit build unless a 64-bit build was requested, but on some systems the default is 64-bit, so the message was incorrect. 
 * Checks for SAGE64 being 'yes' and not 'yes' and '1' as before, as there is other code in Sage which prevents '1' being used. 

These two are just very minor changes - the main change is to delete /tmp/ECL*

What I find a bit odd, is that I don't see these tmp files on my own Sun Blade 2000 SPARC, which runs Solaris 10 update 8 (05/2009). I can only assume they are created them removed by ecl, so why this should not happen on 't2' is a mystery. 

http://boxen.math.washington.edu/home/kirkby/Solaris-fixes/ecl-10.2.1.p0.spkg


Dave


---

Comment by drkirkby created at 2010-05-12 23:54:22

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-05-13 13:07:22

Note #8808 as another ECL spkg update.  

Also, the patch about the 'yes' and '1' still says

```
# Compile for 64-bit if SAGE64 is set to 'yes' or '1' 
```

although of course the code behaves as Dave describes... but maybe that's ok?


---

Comment by drkirkby created at 2010-05-14 09:27:58

I'll create a new package based on Williams at #8808, which address all issues about ECL


---

Comment by drkirkby created at 2010-05-14 09:27:58

Changing status from needs_review to needs_work.


---

Attachment

Mercurial patch - removes tmp files, based on latest verison of ecl


---

Comment by drkirkby created at 2010-05-14 12:17:05

Here's a revised ecl-10.4.1. 


http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.4.1/ecl-10.4.1.spkg

It includes 

 * The latest release of ecl - taken from the package posted at #8808
 * Removes /tmp/ECL* on Solaris. 
 * Corrected minor issue with SAGE64, which would have in theory worked if SAGE64 was set to '1', but earlier bits of sage force SAGE64 to be only 'yes' or 'no', so there was no point checking for this. 
 * Comment in the code about this SAGE64 change is now more accurate. 

I've tested this on sage.math and it works fine. 

```
real	2m20.869s
user	1m47.690s
sys	0m23.480s
Successfully installed ecl-10.4.1
kirkby@sage:~/sage-4.4.2.alpha0$ uname -a
Linux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux
```



*Note, this code to remove /tmp/ECL* is not a perfect solution. Once ECL is fixed, this should be removed.*
Dave


---

Comment by drkirkby created at 2010-05-14 12:17:05

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-05-14 12:22:08

## Note to release manager

 * Apply the patch at #8808
 * Apply the patch attacked here. 
 * Copy the file http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.4.1/ecl-10.4.1.spkg to the new source. 
 * Do *NOT* use the .spkg at http://wstein.org/home/wstein/patches/ecl-10.4.1.spkg as that lacks the patches here, whereas this ticket includes the updated ECL at http://wstein.org/home/wstein/patches/ecl-10.4.1.spkg. 

Dave


---

Comment by jason created at 2010-05-14 15:02:59

Replying to [comment:6 drkirkby]:
> == Note to release manager ==
> 
>  * Apply the patch at #8808
>  * Apply the patch attacked here. 

Both of these patches are included in your spkg, right?  In that case, the release manager would just use your spkg, and wouldn't apply any patches anywhere.


---

Comment by jason created at 2010-05-14 15:03:32

As a reminder here, this should *only* be merged simultaneously with the new maxima at #8731.


---

Comment by jason created at 2010-05-14 17:18:14

As pointed out in #8808, #8645 actually built the new spkg correctly, so we should have started with the spkg from #8645 instead of the spkg from #8808.  I've posted a new spkg which removes the directories that #8645 removed, as per the spkg instructions.


---

Comment by jason created at 2010-05-14 17:24:23

New spkg up at http://sage.math.washington.edu/home/jason/ecl-10.4.1.spkg

I'm not sure who can review it, since I fixed it, to follow Nils' spkg, but David also fixed something on it.

Maybe kcrisman can review it, in conjunction with the new maxima update?


---

Comment by drkirkby created at 2010-05-14 21:19:47

Replying to [comment:7 jason]:
> Replying to [comment:6 drkirkby]:
> > == Note to release manager ==
> > 
> >  * Apply the patch at #8808
> >  * Apply the patch attacked here. 
> 
> Both of these patches are included in your spkg, right?  In that case, the release manager would just use your spkg, and wouldn't apply any patches anywhere.
> 
> 

My package should work fine.

My reason for saying to add #8808 first is because my patch was based on the patch applied in #8088, so assumed the wording of SPKG.txt in #8088 as a starting point and used the Mercurial repository in #8088 as a starting point. Also, since William updated the package, he should get credit for that ticket. It has already got positive review. 

From the point of view of actual code, it would have made no difference whatsoever.

Anyway, you have now posted another version, based on #8645. Someone needs to review it. I looked over spkg-install and SPKG.txt and they look OK to me, but I can hardly review it.


---

Comment by jason created at 2010-05-14 21:40:25

I positive reviewed #8808, which was a mistake.  That's why I posted a new spkg, giving credit to Nils, William, and you, but using #8645 as a base for your patch.  Well, actually I just took your spkg and removed the appropriate directories, since that should end up with the same final result.

If Nils agrees that the changes are good (i.e., the right directories were removed, I think we can mark this as positive review, because then at least 3 pairs of eyes will have looked at the spkg.


---

Comment by nbruin created at 2010-05-18 07:55:01

I confirm that the src directories in
`/home/nbruin/ecl-10.4.1.spkg`
and
`/home/jason/ecl-10.4.1.spkg`
agree according to `diff -r`. Differences are only in
`spkg-install` and `SPKG.txt`, as expected (and in .hg).


---

Comment by nbruin created at 2010-05-18 07:55:01

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-18 14:03:49

Replying to [comment:8 jason]:
> As a reminder here, this should *only* be merged simultaneously with the new maxima at #8731. 

Jason, 

what is there about this ticket that means it can only be merged simultaneously with the new Maxima at #8731? That Maxima ticket has not been updated for 3 weeks. If ECL & Maxima need to be updated together, that leaves a whole load of issues unresolved about ECL. Some I can think of are

 * The original aim of the ticket, which was to clear the tmp files - a trivial change, that does not need ECL updated, but allows Sage to build more relieably on 't2'
 * The minor SAGE64 issue - again, a trivial (cosmetic) change that does not need ECL updated.
 * It stops the building of spkg's in parallel, as the ECL makefile needs a trivial edit for that - see #9187. Again, that does not need a new version of ECL for this. 
 * It stops a build of ECL on 64-bit OpenSolaris - see #8089. Again, the option to permit this does not need a new upstream version of ECL. 

It seems to me we have three choices here:

 * Update ECL, without updating Maxima, which I think you are saying is not possible.  
 * Update both Maxima and ECL to the latest versions *quickly*. 
 * Apply all the other very small changes to the ECL 10.2.1 that is in Sage now. So leaving updating ECL to 10.4.1 until a later date. 

I've created #9264 to update ECL to 10.4.1 and apply all changes. 

It might however be wiser to create another ticket to just apply all the small changes to ECL 10.2.1. 

Dave


---

Comment by drkirkby created at 2010-06-18 14:04:15

Changing status from positive_review to needs_work.


---

Comment by drkirkby created at 2010-06-18 14:04:24

Changing status from needs_work to needs_info.


---

Comment by drkirkby created at 2010-06-21 09:00:29

#9264 solves this issue, and several others related to ECL. Hence #9264, which has positive review, can be merged whilst solving not just this issue, but others related to building packages in parallel and building on OpenSolaris.


---

Comment by rlm created at 2010-06-25 11:19:51

Resolution: duplicate


---

Comment by wjp created at 2011-01-17 16:02:08

For what it's worth, jjgarcia reports the original issue with `/tmp/ECLINIT.c` being used instead of a unique tempfile has been fixed in ECL. It appears to be in the latest ECL release already, but I haven't checked personally if it now works on Solaris.
