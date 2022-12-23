# Issue 1590: notebook -- change it so changes are saved even in cells that aren't evaluated

Issue created by migration from https://trac.sagemath.org/ticket/1590

Original creator: was

Original creation time: 2007-12-23 07:09:35

Assignee: boothby


```
> On Dec 18, 12:51pm, pgdoyle <> wrote:
> > Changes to my Sage notebooks are not always getting saved. I'm
> > running Sage 2.9 from Firefox 2.0.0.11 on Mac OS 10.4.11 on a PowerMac
> > G5.
> 
> I've tried this now on with Safari instead of Firefox, and on a Linux
> box instead of the Mac.  And it appears to me that in every case,
> changes to any cell that doesn't get evaluated just get discarded when
> you `Save & close'.  Now, I would think that this could be fixed,
> because after all the notebook knows how to `Evaluate All', which must
> require it to inform itself about all edits that have been done to
> cells in the worksheet.  But, if for some reason this can't be fixed,
> then I think users ought to be warned, because I don't think it will
> be clear (it certainly wasn't to me) that unless you are careful to
> evaluate any cell you change or any new cell you enter, you'll lose
> your work.

The current behavior is not a bug and is exactly the way we designed
it to work.  That said, I *do* want to change the implementation
so that any time a cell is changed and the cursor leaves the cell
or "save & close" is clicked, the changed version is sent back to the
server.  I think Tom Boothby has argued against this,
which is why it hasn't happened already.
```



---

Comment by boothby created at 2008-01-02 23:38:31

This was implemented some time before the notebook went to Twisted.  I'll try to do it again...


---

Comment by boothby created at 2008-03-16 18:51:16

This one slipped through the cracks...


---

Comment by was created at 2008-03-16 20:31:03

REVIEW:

 1. It works!

 2. This line is lame:

```
       if ctx.args.has_key('save_only'): 
```

instead you should test that the save_only key is there *and* equal to '1'. 
Since it would be very reasonable to write query code someday with save_only=0,
and it would be mysteriously buggy. 

 3. When 2 is fixed I recommend this for inclusion in Sage.


---

Attachment


---

Comment by mabshoff created at 2008-03-17 04:50:20

Merged in Sage 2.10.4.final


---

Comment by mabshoff created at 2008-03-17 04:50:20

Resolution: fixed
