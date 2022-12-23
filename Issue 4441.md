# Issue 4441: [with patch, needs review] fixes to the doc repo

Issue created by migration from https://trac.sagemath.org/ticket/4441

Original creator: GeorgSWeber

Original creation time: 2008-11-04 21:15:17

Assignee: GeorgSWeber

Splitted away from #4370 as the reviewer requested.
The patch is identical and was just renamed.
From #4370:
  After applying the patch to devel/doc, you have to do there once:

  chmod a+x needed_additions_Sage-3.2.alpha2_doc-repository

  ./needed_additions_Sage-3.2.alpha2_doc-repository

  (Writing that script was faster than trying to explain what to do with words.)

I was tempted to give this ticket the priority "blocker" :-)

Now seriously, this should be taken in ASAP for two reasons.
Firstly, it removes the build of two obsolete chapters of no-more-existing modules in the documentation (sage.modular.abvar.torsion_point, sage.modular.abvar.hecke_operator), whose contents are currently doubled (the contents being currently also in sage.modular.abvar.finite_subgroup resp. sage.modular.abvar.morphism).
Secondly, and much more importantly, it puts the doc repo in a clean state, in order to start with the ReST integration.


---

Comment by GeorgSWeber created at 2008-11-04 21:16:32

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-04 21:22:21

I wanted 4370-sage_library.patch - the attached patch also need to change since the ReST transformation will start with a clean repo, i.e. we will nuke the old repo. The bit from the patch that removes the old and no longer existing input files should go in.

And by the way: my doc repo does not need any fixes:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3/devel/doc$ hg status
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3/devel/doc$ hg verify
checking changesets
checking manifests
crosschecking files in changesets and manifests
checking files
149 files, 683 changesets, 964 total revisions
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3/devel/doc$
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-11-04 21:36:08

Ok, I see the congroup fixes are now at #4442. So you can ignore that part of the comment.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-04 22:52:14

Hi, after the patch:

```
susanne-webers-computer:~/Public/sage/sage-3.2.alpha2/devel/doc georgweber$ hg verify
checking changesets
checking manifests
crosschecking files in changesets and manifests
checking files
185 files, 683 changesets, 999 total revisions
```

That's 185 files now, and not only 149!

The main focus is to add essential files to the repo for the first time (!), but only those that are needed/important to be complete after doing a "hg clone".

IMHO, the wording "fixing the doc repo" is appropriate if even the basic "Makefile" and "Makefile.deps" files are missing entirely from a spkg hg repository. Although formally the repo isn't broken, it is not of much use in this incomplete state.

The many, many other files not in the doc hg repo, but currently delivered with the doc spkg, should definitely "jump over the blade" in the ReST transition. But those 36 (=185-149) files addressed in the patch should not. (Another dozen or so of these 36 files could be disposed of easily, too, but that would require changes in the Makefile).

Please consider the patch as-is again, thanks!


---

Comment by mabshoff created at 2008-11-04 22:59:48

Nope, I see no point adding those files to the repo since they will be deleted anyway. Adding those files will onlu needlessly increase the size.

When one runs -sdist there are files that are copied over into the new spkg that are not in the hg repo, so *if* we were to merge such a patch it would not add the files to the repo. Since we are waiting for ReST anyway the patch will not go into 3.2.

Please post a patch removing the two stale files from ref/modabvar.tex - negative review on the script.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-05 06:55:47

apply only this one


---

Attachment

Hi Michael, thanks for your patience.

I'm still the newbie in the learning phase. Obviously, the current sage documentation repo does not miss files, but contains too many. It probably would have been sufficient in the past if only certain tex files would have been in there, like prog.tex.

>Please post a patch removing the two stale files from ref/modabvar.tex 
Here you go.


---

Comment by GeorgSWeber created at 2008-11-05 07:02:14

Changing priority from critical to minor.


---

Comment by mabshoff created at 2008-11-05 20:23:56

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-05 20:24:08

Resolution: fixed


---

Comment by mabshoff created at 2008-11-05 20:24:08

Merged in Sage 3.2.alpha3
