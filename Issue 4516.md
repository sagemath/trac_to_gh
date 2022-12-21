# Issue 4516: make check on binaries should smoothly 100% pass -- right now it fails on the docs and gives lots of verbosity at the start, and #4515

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-13 22:59:26

Assignee: mabshoff




---

Comment by was created at 2008-11-14 00:45:03

The main bug is that the devel/doc directory isn't copied into the bdist.  This is because of a stupid bug in local/bin/sage-bdist, which is fixed by the attached 1-line patch. 

To test this, apply the patch, do "./sage -bdist" then look in the SAGE_ROOT/dist directory and confirm that the resulting binary has a devel/doc directory.


---

Attachment

By chance, I had experimented with "sage -bdist" on Sage 3.2.alpha2, so I could verify that indeed, without this patch the "devel/doc-main" directory is missing.

With this patch applied, it is there after "sage-bdist".


---

Comment by mabshoff created at 2008-11-15 05:04:50

Resolution: fixed


---

Comment by mabshoff created at 2008-11-15 05:04:50

Merged in Sage 3.2.rc1
