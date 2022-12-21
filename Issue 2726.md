# Issue 2726: [with patch; needs review] SAGE debian build system update

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-03-29 22:15:57

Assignee: tabbott

I've updated the SAGE Debian build system to support uploading to an apt repository as things build (so that the building of packages later in the build process can get their dependencies via apt).  Attached are the relevant patches.

One thing that's kinda annoying is that renaming SbuildHack.pm to sage-SbuildHack.pm was problematic because perl modules can't have dashes in their name.  We should figure out how to get SbuildHack.pm installed now that it's name doesn't start with sage.

I'm trying to get a version of the code in SbuildHack.pm into mainline sbuild so that we don't need to bother with this, but am uncertain how long that will take.


---

Attachment


---

Attachment

make sure SbuildHack.pm gets copied by -sdist


---

Attachment

Patch looks good to me. My minimal patch makes sure that SbuildHack.pm is copied on `-sdist`

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-01 20:33:01

Merged in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-01 20:33:01

Resolution: fixed
