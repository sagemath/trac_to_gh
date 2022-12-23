# Issue 407: improve how gap workspace caching works

Issue created by migration from https://trac.sagemath.org/ticket/407

Original creator: was

Original creation time: 2007-07-27 03:16:33

Assignee: was


```
On 7/26/07, Dan Christensen <jdc@uwo.ca> wrote:
> 
> "David Joyner" <wdjoyner@gmail.com> writes:
> 
> > Could you please try gap_reset_workspace() and then restart SAGE
> > and see if the examples start?
> 
> That fixed it!  Thanks.  Not sure what I did.  The problem occurred on
> two different systems, which my home directory is mirrored between.
> If it happens again, I'll report any additional info I can think of.

Very interesting.  When you install the gap database, SAGE runs
gap_reset_workspace() to update the cached workspace on the machine
on which the database is installed.  Because a single home directory could
be used by multiple machines, there are potentially multiple gap workspace
cache files, and for you only one was updated.   

This is an annoying design (due to me), since multiple users of a single
SAGE install will all have to type gap_reset_workspace() to get the new gap
libraries (when one installs, e.g., the small group database). 

I should change the implementation so when installing database_gap (or
anything else that might invalidate the stored gap workspace, or more precisely
make it not optimal), then *all* gap workspace cache files from all users of
that SAGE install become invalid.  They would then be regenerated (which takes
only a few seconds) the next time any user starts GAP from a SAGE session.
I could do this by assigning a sequence number, e.g., in a file like 
local/lib/gap-sequence-number, which is incremented any time gap is updated
in some way.  Then I could make the cached workspace (or another file
with a similar name next to the gap workspace file) also store this 
sequence number (the cached workspaces are in ~/.sage/gap/).  
Then whenever a gap interpreter is first started in interface/gap.py, 
this sequence number is checked, and if it doesn't match, then the gap workspace
is regenerated.  This should completely eliminate all future gap_reset_workspace
synchronization errors. 

I'll wait to see if anybody thinks the above idea is stupid, and if not,
I'll implement it (which shouldn't take long). 

 -- William
```



---

Comment by mabshoff created at 2007-09-10 02:48:52

Looks like a duplicate of #527.

Cheers,

Michael


---

Comment by was created at 2007-10-06 23:00:50

Changing status from new to assigned.


---

Comment by was created at 2007-11-03 14:56:53

Resolution: duplicate
