# Issue 1449: very serious (but trivial to fix) notebook bug: shift-enter doesn't work on macs; it's shift-return!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-10 15:50:19

Assignee: boothby


```


On Dec 10, 2007 6:08 AM, G. Edgar <edgar`@`math.ohio-state.edu> wrote:
> 
> It says to use "shift enter" to evaluate an input cell.
> But it seems this is wrong on Mac, and one should use "shift return".
> Return and Enter are separate keys on the Mac keyboard.

You're right.  And this is especially bad since right now on a Mac
"shift enter" doesn't work.   I can't believe we missed this, given that
so many Sage developers (like me) work on Macs!

I think the fix will be to make it so "shift return" does work on macs,
in addition to "shift enter".  This will make the documentation stay
uniform (but we'll also mention shift-enter in the docs). 

William
```



---

Comment by was created at 2007-12-12 13:26:50


```
With my Mac G5, uising Safari...
shift-return and option-return evaluate the cell
shift-enter, option-enter do not. 
```


Tom Boothby asked for some specific details from the poster about this.
I don't know what happened as a result yet.


---

Comment by boothby created at 2008-01-02 23:10:12

This *should* fix the problem, but hasn't been tested on the target platform.


---

Attachment

The bundle also seems to contain the fix for #1661.

Cheers,

Michael


---

Comment by robertwb created at 2008-01-04 20:40:09

Works in Camino and Firefox for me, but not in Safari...


---

Attachment

Great idea!!

I posted a slight polish patch.


---

Comment by mabshoff created at 2008-01-05 02:23:53

Merged in 2.9.2.rc1. I open a new ticket for the remaining Safari issue, see #1690.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-05 02:23:53

Resolution: fixed
