# Issue 5194: add option to turn off automatic updates for an interact

Issue created by migration from Trac.

Original creator: john_perry

Original creation time: 2009-02-06 03:38:45

Assignee: boothby

CC:  jason

Whenever the user of an interact tabs from one input_box to another, the function is called, which sets off all the computations associated with the interact. Even when the computations are not very time-consuming, it can be a hassle if, for example, the user wishes to change several input boxes at once, before getting an update.

This enhancement, discussed [here](http://groups.google.com/group/sage-devel/browse_thread/thread/9ff935e0d6a729b3/554c6c448e6a75e5?lnk=gst&q=interact+update#554c6c448e6a75e5) on sage-devel, would allow an interact to turn off automatic update, adding a user interface element that will prompt the interact to re-run.


---

Attachment

a patch that adds a checkbox to control automatic updating


---

Comment by john_perry created at 2009-02-06 03:43:56

The patch I've attached is *not* the one described in the final version of the discussion. Mike Hansen recommended that we provide a button that, when pressed, updates the interact, and when not pressed, does not.

I don't know how to create a button (Sage doesn't have them yet), but I do know how to create a checkbox. After looking at the code tonight, I also suspect that it will take a more serious rewrite of interact to make that version work. The submitted patch can serve as a stopgap.


---

Comment by jason created at 2009-02-06 20:04:51

This stopgap patch: 
 * still causes a roundtrip to the server
 * //deletes// the output when unchecked, and you can't see the output again until you check it.  This could be considered a good thing.

However, it's still a nice stopgap approach.  The documentation is missing, though.  Positive review when the documentation to the interact function mentions this parameter and tells what it does.


---

Comment by mabshoff created at 2009-02-06 23:03:01

3.4 is for ReST tickets only.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2009-02-07 05:58:10

I've posted a patch which implements what was discussed on sage-devel.  A lot of it is mostly general infrastructure stuff such as separating the updating of values from the running of the interact function.

Currently, when the values are changed, the output is deleted.  One could get around this, but the implementation is a bit messy since the update button would have to go through all of the controls and update the values in the Sage process for each of them.


---

Comment by mhansen created at 2009-02-07 05:58:10

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2009-02-07 05:58:10

Changing status from new to assigned.


---

Comment by john_perry created at 2009-02-08 17:43:33

The second patch does exactly what I would have liked. It is unfortunate that the output is deleted, but the current situation is much better than the previous one. In addition, it adds some infrastructure for a button object to interact, although anything beyond the Update button is non-trivial to get working.

The only caution I would issue is that when I ran `sage -t` I initially encountered the following failure:

**********************************************************************
File "/home/software/sage-3.2.1/devel/sage-main/sage/server/notebook/interact.py", line 677:
    sage: sage.server.notebook.interact.InputBox('theta', 1).render()
Expected:
    '<input type=\'text\' value="1" size=80 onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"theta\\", ..., sage.server.notebook.interact.standard_b64decode(\\""+encode64(this.value)+"\\"), globals());sage.server.notebook.interact.recompute(0)")\'></input>'
Got:
    '<input type=\'text\' value=\'1\' size=80 onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"theta\\", 27, sage.server.notebook.interact.standard_b64decode(\\""+encode64(this.value)+"\\"), globals());sage.server.notebook.interact.recompute(0)")\'></input>'
**********************************************************************

This appears to be due to a difference in code that your patch did not update: once I changed the relevant line to return `value="%r"` and `value="%s"` instead of `value='%r'` and `value='%s'` this worked. Maybe I was missing some intermediate patch?


---

Comment by john_perry created at 2009-02-08 17:43:33

Resolution: worksforme


---

Comment by mabshoff created at 2009-02-08 18:35:29

Resolution changed from worksforme to 


---

Comment by mabshoff created at 2009-02-08 18:35:29

John,

 * do not close tickets, the release manager does that once the patch has been merged.
 * do not give an unconditional positive review to ticket that have doctest failures

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 18:35:29

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-02-09 11:07:26

Ok, according to the doctesting this is the problem:

```
    '<input type=\'text\' value="1" size=80 
    '<input type=\'text\' value=\'1\' size=80 
```

i.e. a change in escaping. This looks fine to me, but I will apply the patches and see if the doctest issue is still even there.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 11:15:43

With my merge tree and mhansen's patch only:

```
All tests passed!
Timings have been updated.
Total time for all tests: 266.2 seconds
```

So back to positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 11:16:00

Resolution: fixed


---

Comment by mabshoff created at 2009-02-09 11:16:00

Merged in Sage 3.3.rc0.

Cheers,

Michael
