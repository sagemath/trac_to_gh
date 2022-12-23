# Issue 3358: Improve the building of eclib (shared/static objects) [with patch needs review]

Issue created by migration from https://trac.sagemath.org/ticket/3358

Original creator: fbissey

Original creation time: 2008-06-03 23:57:53

Assignee: mabshoff

CC:  tabbott@mit.edu

After sitting waiting for some answers on the last thread about this on debian-sage
I decided to go ahead. This patch do not add versionning for debian as it seems
to cause problem on other OS. It builds static objects (libraries and executables)
without any pic flag and shared object with pic flag on linux. I respected the earlier
setting where the flag is set in spkg-install and it is set to nothing on OS X and
CYGWIN although I think it should be set as well on this platform.
I also move executables in a created bin directory for convenience (this directory
is created by the Makefile).
I cleaned the spkg-install to accommodate the changes and added a few fix that I
thought necessary. -fPIC to -fpic, those are 2 slightly different flags, I don't
think I should go on the technical differences between them. I also cleaned
a conditional block were linux specific code would be executed on darwin - probably
without harm but still.


---

Comment by craigcitro created at 2008-06-15 22:01:50

Changing keywords from "" to "editor_mabshoff".


---

Comment by craigcitro created at 2008-06-15 22:02:27

Please remember to put the "[with patch, needs review]" at the *beginning* of the summary.


---

Comment by mabshoff created at 2008-06-20 04:02:29

I do not like the "-fPIC" -> "-fpic" change, otherwise I am fine with the patch.

Cheers,

Michael


---

Comment by fbissey created at 2008-06-20 08:03:08

Hi Michael,

I didn't think you would take it anyway as it has
GNU-ism like:
(SO_LIBNAME): FPICFLAG= $(PICFLAG)
	export FPICFLAG

I thought a bit more about -fPIC versus -fPIC and
I guess in the interest of KISS we should probably
stick to -fPIC as ppc and may be other may balk 
otherwise.


---

Comment by fbissey created at 2008-07-07 01:19:54

OK new patches to ungnu-ify the makefiles and build shared and static objects
properly and use the bin folder. Tested with bsd make and gnu make - didn't have 
time for sun make, should work though. 
spkg-install also updated. everything is against eclib-20080310.p4


---

Comment by fbissey created at 2008-07-08 22:34:24

updated the patches to 20080310.p5.


---

Comment by cremona created at 2008-08-10 16:23:39

I'm probably not the best person to review this but if there's anything I can do, please let me know.  John


---

Comment by mabshoff created at 2008-11-28 22:49:50

I think there are some issues with eclib-ungnu.patch:

 * the formal changes, i.e. the removal of the ".o" from the makefiles should be independent of the other changes for reviewing purposes
 * some of the fixes will have the makefiles as is working with Sage, but if anyone attempted to compile eclib without explicitly setting env variables like NTL the compile will break or the build will not include features like pari support. I don't care which way we go here, but this is up to John since it is his code project.

As is the patch needs to be rebased slighly:

```
/eclib-20080310.p7/src$ patch -p1 --dry-run < eclib-ungnu.patch\?format\=raw 
patching file Makefile
Hunk #4 FAILED at 45.
1 out of 4 hunks FAILED -- saving rejects to file Makefile.rej
patching file Makefile.dynamic
patching file g0n/Makefile
Hunk #2 succeeded at 25 with fuzz 2.
patching file procs/Makefile
Hunk #2 FAILED at 23.
1 out of 6 hunks FAILED -- saving rejects to file procs/Makefile.rej
patching file qcurves/Makefile
patching file qrank/Makefile
```


I am -1 on all the other three patches at this ticket. Some of those might be salvaged, i.e. from the spkg-install patches like the better installation, but the PIC->pic change is just plain wrong.

Cheers,

Michael


---

Comment by cremona created at 2008-11-28 22:58:58

Replying to [comment:9 mabshoff]:
> I think there are some issues with eclib-ungnu.patch:
> 
>  * the formal changes, i.e. the removal of the ".o" from the makefiles should be independent of the other changes for reviewing purposes
>  * some of the fixes will have the makefiles as is working with Sage, but if anyone attempted to compile eclib without explicitly setting env variables like NTL the compile will break or the build will not include features like pari support. I don't care which way we go here, but this is up to John since it is his code project.
> 
> As is the patch needs to be rebased slighly:
> {{{
> /eclib-20080310.p7/src$ patch -p1 --dry-run < eclib-ungnu.patch\?format\=raw 
> patching file Makefile
> Hunk #4 FAILED at 45.
> 1 out of 4 hunks FAILED -- saving rejects to file Makefile.rej
> patching file Makefile.dynamic
> patching file g0n/Makefile
> Hunk #2 succeeded at 25 with fuzz 2.
> patching file procs/Makefile
> Hunk #2 FAILED at 23.
> 1 out of 6 hunks FAILED -- saving rejects to file procs/Makefile.rej
> patching file qcurves/Makefile
> patching file qrank/Makefile
> }}}
> 
> I am -1 on all the other three patches at this ticket. Some of those might be salvaged, i.e. from the spkg-install patches like the better installation, but the PIC->pic change is just plain wrong.
> 
> Cheers,
> 
> Michael 

I am happy to go along with whatever is best for Sage. I agree that one should be able to type "make" without setting environment variables manually.  John


---

Comment by fbissey created at 2008-11-29 10:20:17

Hi guys,

I am a bit out of action at the moment but I should comment on what I
had done and why.

Replying to [comment:9 mabshoff]:
> I think there are some issues with eclib-ungnu.patch:
> 
>  * the formal changes, i.e. the removal of the ".o" from the makefiles should be independent of the other changes for reviewing purposes

I reviewed my patch and the removal of the ".o" and its inclusion in
$(OBJ_SUF) and $(SOBJ_SUF) was needed to write a working ".SUFFIXES:"
old unix style rule and keep putting "_n" in the object. It can be simplified
if we remove it. It is a remnant of the various building options that weren't
used in sage but could be restored with a bit of creativity and some environment
variables.

>  * some of the fixes will have the makefiles as is working with Sage, but if anyone attempted to compile eclib without explicitly setting env variables like NTL the compile will break or the build will not include features like pari support. I don't care which way we go here, but this is up to John since it is his code project.
> 

The behavior before and after the patch is currently the same if you
don't set any variables. It defaults to look for stuff in /usr/local .
Either you do some autodetection or you pass variables. It probably 
should be documented in a README.

> As is the patch needs to be rebased slighly:
> {{{
> /eclib-20080310.p7/src$ patch -p1 --dry-run < eclib-ungnu.patch\?format\=raw 
> patching file Makefile
> Hunk #4 FAILED at 45.
> 1 out of 4 hunks FAILED -- saving rejects to file Makefile.rej
> patching file Makefile.dynamic
> patching file g0n/Makefile
> Hunk #2 succeeded at 25 with fuzz 2.
> patching file procs/Makefile
> Hunk #2 FAILED at 23.
> 1 out of 6 hunks FAILED -- saving rejects to file procs/Makefile.rej
> patching file qcurves/Makefile
> patching file qrank/Makefile
> }}}
> 

I'll have a look and rebase it if that's all it takes.

> I am -1 on all the other three patches at this ticket. Some of those might be salvaged, i.e. from the spkg-install patches like the better installation, but the PIC->pic change is just plain wrong.
> 

The two first patches are really obsolete in many ways. And yes, after doing
some growing up I realise PIC->pic is wrong for something like sage. It is 
debatable that it could be selected appropriately at the start of the building 
process but that wouldn't be KISS.

> Cheers,
> 
> Michael 

Cheers,
Francois


---

Attachment

new patch for spkg.install + new patch file for environment variables


---

Comment by fbissey created at 2008-12-04 11:11:15

OK it took me a little bit more time than expected - because of life and going back to this uncovered several "itches". So in summary there are two patches.
eclib-ungnu.patch:
*rebased on 20080310.p7
*do away with multiple building options we only build with ntl - that simplifies the suffixes of object files.
*created an install target
*Got enough of sub-makefile including the top makefile just for environment variables,
creating a lot of noise about over-riding target and so on - splitting was the only option that I knew would result in something compatible with BSD make (and incidentally sun make: bonus!).

spkg.patch:
*rebased on 20080310.p7
*updated spkg-install to reflect changes in makefiles and the setting of environment variables.
*included a Makefile.env in the patch directory to put the environment variables correctly for sage.

cheers,
Francois


---

Comment by mabshoff created at 2008-12-04 11:15:18

Thanks Francois,

I have deleted the old and no longer useful patches so that only the two current patches remain. I will review those patches in the near future to avoid bitrot again. 

Cheers,

Michael


---

Comment by fbissey created at 2009-12-08 08:38:03

Oh dear me just seen that in the need review message.
I have to check if it needs a lot of rebasing as it was 
against p5. Then may be David Kirby should have a look.


---

Comment by fbissey created at 2009-12-09 20:15:51

Found problems with qrank's binary and the tests.
Back to need work. 
Hopefully I will update this soonish.


---

Comment by fbissey created at 2009-12-09 20:15:51

Changing status from needs_review to needs_work.


---

Comment by fbissey created at 2012-08-05 10:53:39

This is obsolete, solved by the current eclib, we should close it.


---

Comment by fbissey created at 2012-08-05 10:53:39

Changing status from needs_work to needs_review.


---

Comment by fbissey created at 2012-08-05 10:53:59

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2012-08-05 12:38:49

Replying to [comment:16 fbissey]:
> This is obsolete, solved by the current eclib, we should close it.

Agreed.


---

Comment by jdemeyer created at 2012-08-06 13:11:34

May I remind you to set the milestone to "sage-duplicate/invalid/wontfix" in such a case?


---

Comment by jdemeyer created at 2012-08-06 13:11:34

Changing keywords from "editor_mabshoff" to "".


---

Comment by jdemeyer created at 2012-08-06 13:13:39

Resolution: worksforme
