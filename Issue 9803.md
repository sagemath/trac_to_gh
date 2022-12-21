# Issue 9803: Remove unnecessary dependy for cliquer in spkg/standard/deps

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-26 01:17:47

Assignee: GeorgSWeber

CC:  mvngu mpatel ncohen

cliquer used use to SCons, but for various reasons it was replaced by a simple `Makefile`. (IMHO, a good idea, as fighting with SCons seems to be a nightmare). Minh did the replacment, but there is an unnecessary dependency in `spkg/standard/deps`, which potentially means parallel builds are slower than they need be, as currently cliquer can't be built without SCons first being built.


---

Attachment

Replacement deps, which removes SCONS dependency


---

Comment by drkirkby created at 2010-08-26 01:22:17

Unified diff file for spkg/standard/deps. Relative to 'deps' in sage-4.5.3.alpha2


---

Comment by drkirkby created at 2010-08-26 01:25:29

Changing status from new to needs_review.


---

Attachment


---

Comment by drkirkby created at 2010-08-28 19:08:24

I'm adding Nathann Cohen to the CC list, as he is the package maintainer.


---

Comment by drkirkby created at 2010-09-04 00:32:40

Can you review it Leif? 

Dave


---

Comment by leif created at 2010-09-04 05:06:23

Just for the record: Upstream comes with a Makefile, too (no SConscript).

The attached `deps` and `deps.diff` still apply to Sage 4.5.3.rc0.

*Positive review.*


---

Comment by leif created at 2010-09-04 05:06:23

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-04 05:09:30

P.S.: There's a lot wrong with the Cliquer spkg, perhaps to be addressed at #9767.


---

Comment by mpatel created at 2010-09-15 22:47:41

Resolution: fixed
