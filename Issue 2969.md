# Issue 2969: [with patches; needs review] Autocomputing Debian package version numbers

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-04-20 04:20:24

Assignee: tabbott

I've attached a series of patches that makes the Debian package version numbers get computed automatically from the SAGE spkg version numbers.  

The code I ran rename the existing spkgs is the following shell one-liner:

for i in `\ls *.spkg`; do mv $i `echo $i | sed 's/\.\(p.*\.spkg\)/-\1/'`; done

There are also a few patches that decrease version numbers of some Debian packages whose version numbers were too high, and another patch that fixes the guava Debianization to find the right version number.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment

lcalc-debian-cleanup.patch conflicts/has some of the same hunks as #2967. Reverting that patch then  makes this patch import fine.

Cheers,

Michael


---

Comment by tabbott created at 2008-04-20 05:02:26

Oops, yeah, lcalc-debian-cleanup.patch is the same patch as in #2967.  Sorry about that.


---

Comment by mabshoff created at 2008-04-20 05:07:32

Patches look good to me [I fixed the issue I noted above]. Positive review.

Tim: no problem ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 05:07:44

Merged in Sage 3.0.rc0


---

Comment by mabshoff created at 2008-04-20 05:08:14

Merged in Sage 3.0.rc0


---

Comment by mabshoff created at 2008-04-20 05:08:14

Resolution: fixed
