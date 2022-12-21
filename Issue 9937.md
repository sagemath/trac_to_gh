# Issue 9937: GAP does not start if the path to the GAP workspace file contains more than 83 characters

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2010-09-17 21:31:06

Assignee: was

CC:  slabbe mrobado

Keywords: gap

As pointed out in 
[this thread](http://groups.google.com/group/sage-support/browse_thread/thread/7e169e371308838/a1403ee743fd6ea6?lnk=gst&q=tremblay+gap#a1403ee743fd6ea6), on some machines one there is a problem starting GAP from within Sage:

```
sage: gap('3+2')
A workspace appears to have been corrupted... automatically rebuilding (this is harmless).
---------------------------------------------------------------------------
...
TypeError: Unable to start gap
```

The problem is in Sage's attempt to rebuild the GAP workspace. It turns out that Sage calls GAP's `SaveWorkspace` command incorrectly in a particular case.

To explain the problem, first recall the process used by the GAP interface to evaluate a line of GAP code, say `LineOfGapCode`. It begins by checking the length `LineOfGapCode` (as a string). If this length is greater than 100 (a pre-defined cut-off value), then a file is created containing:

```
Print(LineOfGapCode);
```

This file is read into GAP using the expect interface and the output is parsed and returned to Sage. (There is no problem if the length is less than 100, because the interface does not use a file.)

Let's apply this to the case where we need to rebuild a workspace. The workspace is just a file contained in a user's .sage directory. If the number of characters in the path to the workspace is greater than the cut-off, then Sage tries to execute the following command:

```
Print(SaveWorkspace("PathToWorkspaceFile"));
```

This is not permitted by GAP, as explained in the [GAP Reference Manual](http://www.gap-system.org/Manuals/doc/htm/ref/CHAP003.htm#SSEC011.1):

```
SaveWorkspace can only be used at the main gap> prompt. It cannot be included in the body of a loop or function, or called from a break loop.
```

So to fix this, we need to force the interface not to use a file to execute the `SaveWorkspace` command.

(This problem has plagued all the computers in our computer lab for months since a user's home directory is located on a network drive with a long name.)


---

Comment by saliola created at 2010-09-17 21:50:55

Changing assignee from was to saliola.


---

Attachment


---

Attachment

apply only this patch!


---

Comment by saliola created at 2010-09-18 02:42:19

Changing status from new to needs_review.


---

Comment by saliola created at 2010-09-18 02:43:22

Changing status from needs_review to needs_work.


---

Comment by saliola created at 2010-09-18 02:43:45

Changing status from needs_work to needs_review.


---

Attachment

Applies over the precedent patch


---

Comment by slabbe created at 2010-09-18 13:52:00

I was able to reproduce the problem on my osx 10.5 running sage-4.5.3. The patch fixes the problem. All tests pass on sage/interfaces/gap.py. Documentation builds fine.

I added a review patch that simply puts back the constant `sage.interfaces.gap.WORKSPACE` to its original value since the new value was used in all the rest of the doctests.

I am giving a positive review to Franco's patch. I let him change the status of this ticket to positive review if he agrees with my small fix.

I did not manage to apply a patch on the sage install of LaCIM laboratory by ssh. Maybe Jérôme could test the patch on Monday.


---

Comment by saliola created at 2010-09-19 14:35:45

I'm okay with your changes, Sébastien.

Apply patches in this order:

    1. [attachment:trac9938.patch]
    1. [attachment:trac9938-review-sl.patch]


---

Comment by saliola created at 2010-09-19 14:35:45

Changing status from needs_review to positive_review.


---

Comment by slabbe created at 2010-09-24 01:31:15

> I did not manage to apply a patch on the sage install of LaCIM laboratory by ssh. Maybe Jérôme could test the patch on Monday.

Last Monday, I tested the patch on one of the computer in the lab and I can confirm the patches solve the problem. Great!


---

Comment by mpatel created at 2010-09-28 09:14:39

Resolution: fixed


---

Comment by mpatel created at 2010-09-28 09:14:39

Thanks for fixing this!  I encountered just this problem about two days ago when doctesting with a long `DOT_SAGE`.
