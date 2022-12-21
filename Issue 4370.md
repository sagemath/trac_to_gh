# Issue 4370: Add ability to clone the doc repository

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-10-26 13:25:22

Assignee: tba

It would be very useful to be able to clone the documentation repository as well as the source repo.  As Minh Van Nguyen said:

```
Is there a corresponding command or process that I can use to clone the
doc-main repo as well?

Whenever I review the official documentation that's shipped with each
Sage release, I would go into

<sage-home>/devel/doc-main

and then review the documentation from there. If I'm reviewing someone's
patch to any file in the latter directory, I would not clone doc-main
(since I don't yet know how to do that). Instead, I would go ahead with
applying the patch and then do more review of the patch. At this point,
at least one of two things can happen:

[1] If the patch gets a positive review, then all is fine and good.

[2] However, in case there's something wrong with the patched file and I
want to un-apply the patch, I would do this:

sage: hg_doc.revert()

This command reverts back to the stage at which the file in question is
unpatched.

Another possibility is for me to copy a source distro to more than one
directory, and then build (and test) the distro from those different
directories. That way, I would have a copy of Sage that I can use and
with which I won't apply any documentation patches. And I would also
have another copy of Sage for applying documentation patches. Building
one copy of a source distro usually takes a _very_ long time on each
machine that I have access to --- and running all standard tests further
add to my waiting time. As you can imagine, repeating the build and test
processes on the same machine for another copy of the same source distro
would further add to the waiting time. (Man, I can't wait to work on
Sage ;-)
```

and as mabshoff replied:

```
it is fairly simple to add a clone command for the doc repo. If you
want it just open a ticket and someone will take care of it. You can
even try yourself - just look at local/bin/sage-clone and ignore
nearly everything toward the end since that deals with build file
issues.
```


I think this will encourage people to add / improce the existing docs and to review enhancements of the docs.



---

Comment by mvngu created at 2008-10-26 23:57:49

Replying to [ticket:4370 cremona]:
> It would be very useful to be able to clone the documentation repository as well as the source repo.


Indeed.


+1 for your comment




> and as mabshoff replied:

```
it is fairly simple to add a clone command for the doc repo. If you
want it just open a ticket and someone will take care of it. You can
even try yourself - just look at local/bin/sage-clone and ignore
nearly everything toward the end since that deals with build file
issues.
```

> 
> I think this will encourage people to add / improce the existing docs and to review enhancements of the docs.


I'll try to figure out how to implement the suggested clone command. Since I often work with the doc-main directory tree, this is more for my personal benefit. Of course, suggestions are always welcome.


---

Comment by mvngu created at 2008-10-26 23:57:49

Changing status from new to assigned.


---

Comment by mvngu created at 2008-10-26 23:57:49

Changing assignee from tba to mvngu.


---

Comment by mvngu created at 2008-10-29 08:13:49

Changing status from assigned to new.


---

Comment by mvngu created at 2008-10-29 08:13:49

Changing assignee from mvngu to tba.


---

Comment by GeorgSWeber created at 2008-11-02 14:31:58

Changing status from new to assigned.


---

Comment by GeorgSWeber created at 2008-11-02 14:31:58

Hmph,

that is a bit more work than I expected. I got "sage -clonedoc", "sage -bdoc" and "sage -branchdoc" already to work fine. However, obviously there are some fixes needed to get the documentation for 3.2.alpha2 texing (unescaped # in at least two different new patches). I'll see to that in another ticket. Next comes the update to hg.py so that hg_doc works (again). There would be documentation fixes needed, too (in the programming guide), but that is probably best yet another ticket.


---

Comment by GeorgSWeber created at 2008-11-02 14:31:58

Changing assignee from tba to GeorgSWeber.


---

Attachment

applies independently, but the other two are highly recommended first


---

Comment by GeorgSWeber created at 2008-11-04 00:26:34

Well,
the hg.py patch is not ready yet, but the three patches attached already fulfil all the requirements of this ticket. So you can give it a review already now.

The three patches are for three different repos: devel/sage, devel/doc, and finally local/bin.

After applying the patch to devel/doc, you have to do there once:

chmod a+x needed_additions_Sage-3.2.alpha2_doc-repository

./needed_additions_Sage-3.2.alpha2_doc-repository

(Writing that script was faster than trying to explain what to do with words.)


---

Comment by GeorgSWeber created at 2008-11-04 00:30:23

Forgot to add:

If someones really needs the possibility to clone the doc repo not on shell level, but inside sage using hg.py, please open another ticket for it, because it will take me quite some while before I will be able to sacrifice the time needed to finally adapt hg.py, thanks!


---

Comment by mabshoff created at 2008-11-04 00:39:35

Hi Georg,

4370-sage_library.patch should go to its own ticker since it is independent. 

I would also not per default build the Sage documentation on clone - we do not do this for the sage library repo itself.

I can't see seem to fine the alleged possibility to clone the sage-scripts repo. Either way, I would not recommend that we allow this since there are numerous binaries in the bin directory and switching back and forth between various bin directories can cause subtle bugs at runtime.

Another thing I would like to wait for is the switch to the ReST documentation before we allow cloing the doc repo.

In the end I don't think this should be merged into 3.2 :(.

Cheers,

Michael


---

Attachment

obsoleted, don't use (moved to #4441 upon request of the reviewer)


---

Comment by GeorgSWeber created at 2008-11-04 21:27:33

obsoleted, don't use (moved to #4442)


---

Attachment

Hi Michael,
thanks for the review!

> 4370-sage_library.patch should go to its own ticker since it is independent. 
Done, it is now #4441. I also moved the congroup.py patch away to #4442.

>I would also not per default build the Sage documentation on clone
OK. I will address that in an update.

> - we do not do this for the sage library repo itself. 
You're wrong here. See lines 68-91 of the "sage-clone" script, where explicitly "sage -b branch" is called. But let's clone the doc dir without (re-)build, OK.

> I can't see seem to fine the alleged possibility to clone the sage-scripts repo. Either way, I would not recommend that we allow this since there are numerous binaries in the bin directory and switching back and forth between various bin directories can cause subtle bugs at runtime. 
Ah, misunderstanding! I meant that the patch-files attached are to applied themselves to these three different repos, not more. I totally agree that cloning "$SAGE_ROOT/local/bin" would be a bad idea. But the content of the patch(es) did not and will not allow for that.

>Another thing I would like to wait for is the switch to the ReST documentation before we allow cloing the doc repo. 
Well. It might be helpful for the ReST documentation deployment.

>In the end I don't think this should be merged into 3.2 :(. 
Fine, at least for me.


---

Comment by mabshoff created at 2008-11-04 22:12:59

Replying to [comment:7 GeorgSWeber]:
> > - we do not do this for the sage library repo itself. 
> You're wrong here. See lines 68-91 of the "sage-clone" script, where explicitly "sage -b branch" is called. But let's clone the doc dir without (re-)build, OK.

You are right, but "sage -b" on an uptodate repo only rebuilds libcsage.so, so the build is more or less instant. Building the documentation takes *forever* with the current toolchain, but ReST will fix that.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-05 07:05:59

Work on this ticket will be resumed after the move to ReST is completed.


---

Comment by mabshoff created at 2008-11-21 09:40:48

Resolution: wontfix


---

Comment by mabshoff created at 2008-11-21 09:40:48

The new documentation will reside in the main Sage repo, so this is a wontfix.

Cheers,

Michael
