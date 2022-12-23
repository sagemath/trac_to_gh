# Issue 2037: out-of-date tutorial section on errors and exceptions

Issue created by migration from https://trac.sagemath.org/ticket/2037

Original creator: AlexGhitza

Original creation time: 2008-02-03 19:36:03

Assignee: tba

Section 3.5 "Errors and Exceptions" in the tutorial appears to be out of date.  The error messages that come up have changed since the section was written, and the debugger is/looks different (ipdb versus Pdb).



---

Comment by wdj created at 2008-02-22 16:40:46

I just tried to create a patch for this. I also added a section for 3d plotting, copying a few jmol examples from the reference manual. The problem is that sage -t failed horribly, though apparently not due to anything I added. Most seemed to be line return issues. I'm I'm to ignore these then i can proceed to try to create a patch...


---

Comment by wdj created at 2008-02-22 16:52:20

That last sentence should read: "If I'm supposed to ignore
these failures then I can proceed to try to create a patch..." I guess my
question is: has the format to sage -t changed in such a way that one
is to ignore such failures? Or, maybe I'm using sage -t incorrectly.


---

Comment by mabshoff created at 2008-02-22 17:04:56

Sage 2.10.2.alphaX has a broken tut.tex. Take Sage 2.10.2.rc0 or later as a base for a patch.

Cheers,

Michael


---

Comment by wdj created at 2008-02-23 00:01:02

I compiled 2.10.2.rc0 from source (4h5m) and had exactly the same problem. The bundle is attached. The export command would not work to create a patch (sorry, Micheal).


---

Attachment

Sorry, this made it too late for 2.10.2. It will hopefully go right into 2.10.3.alpha0 :(

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-02-23 03:00:20

I've taken David's bundle and manually applied it against 2.10.2.rc0, making a few small fixes in the process (fixed a few long lines, added a citation for Jmol, etc.)  The result is in the attached patch, which (if positively reviewed) should be applied instead of the bundle.

I ran sage -t tut.tex and it succeeded, and ./build_pdf and looked at the resulting pdf file.


---

Attachment


---

Attachment

The last patch ( 2037.patch ) applies cleanly after #2323.


---

Comment by mabshoff created at 2008-02-28 00:16:37

Merged 2037.patch in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-28 00:16:37

Resolution: fixed
