# Issue 6929: Docs in functional and a few ring methods

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-09-14 19:54:27

Assignee: tba

Keywords: integer, integral closure

This patch mostly brings misc/functional.py to (nearly) 100%, but also does a few useful things like allow MUCH wider usage of the functional base_field and say that the integer ring is, in fact, integrally closed!


---

Attachment


---

Comment by jhpalmieri created at 2009-09-23 03:55:09

rebased against 4.1.2.alpha2. apply only this patch


---

Attachment

The patch needed to be rebased (only the changes in rings/ring.pyx).  I also added one fix (referee's prerogative: changing ``n`th` to ``n^{th}`` in misc/functional.py) to avoid a warning when building the reference manual.

Looks good, all tests pass, positive review.


---

Comment by mvngu created at 2009-09-24 11:44:06

set username as kcrisman


---

Attachment

The patch `trac_6929-rebased-v2.patch` is the same as `trac_6929-rebased.patch`. The only difference is that `trac_6929-rebased-v2.patch` sets the username to that of kcrisman's. That way, the patch would be committed in his name. Even after a rebase, the username of the original author should remain in the rebased patch.


---

Comment by kcrisman created at 2009-09-24 12:20:32

But how do you DO that?


---

Comment by mvngu created at 2009-09-24 13:50:24

Replying to [comment:5 kcrisman]:
> But how do you DO that?

 1. Download the patch `trac_6929-rebased.patch` to a local machine.
 1. Open `trac_6929-rebased.patch` in a text editor.
 1. Change the line
 {{{
# User J. H. Palmieri <palmieri`@`math.washington.edu>
 }}}
 to 
 {{{
# User Karl-Dieter Crisman <kcrisman`@`gmail.com>
 }}}
 1. Upload the patch with the modified username to the trac server.


---

Comment by kcrisman created at 2009-09-24 13:59:14

I see, quite manually.  I was wondering whether that was possible in HG, but I like this better.  Perhaps the instructions are a little TOO clear... :)


---

Comment by mvngu created at 2009-09-24 14:04:24

Merged `trac_6929-rebased-v2.patch`.


---

Comment by mvngu created at 2009-09-24 14:04:24

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:21:49

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
