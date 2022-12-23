# Issue 2635: MAJOR NOTEBOOK BUG -- sending unevaluated cells back to the server is severly broken.

Issue created by migration from https://trac.sagemath.org/ticket/2635

Original creator: was

Original creation time: 2008-03-21 19:10:38

Assignee: boothby

CC:  boothby




---

Comment by was created at 2008-03-21 19:10:48


```

On Fri, Mar 21, 2008 at 11:22 AM, Marshall Hampton <hamptonio@gmail.com> wrote:
> 
>  If I kill my notebook session, and then restart, it seems that often
>  the "+" character has been stripped from my worksheets.  However, this
>  doesn't always happen.  It does happen frequently, using 2.10.4 on
>  both ppc and intel macs.
>  
>  Can anyone else reproduce this?

I think this is a ** MAJOR BUG ** introduced by a new feature that Tom Boothby
just implemented in the notebook (and that I didn't catch in the referee process).  
This is definitely a block for 2.11.    Try the following to replicate it:
   1. Create a new blank worksheet with several blank cells
   2. Type 2+2 in the first cell -- do *NOT* press shift enter. 
   3. Simply move the cursor out of the first cell to the second one (use down arrow).
   4. Now refresh the page -- or better leave the page and go back and refresh.
  The plus sign vanishes!

The problem is that when you change a cell and move the cursor out,
the changed cell is incorrectly sent back to the server.   To avoid this
for now, never ever change a cell without shift-entering it. 

William

```



---

Attachment

DANG!  Sorry, guys.  This fixes it.


---

Comment by was created at 2008-03-22 00:07:40

It works!


---

Comment by mabshoff created at 2008-03-22 00:13:52

Merged in Sage 2.11.alpha1


---

Comment by mabshoff created at 2008-03-22 00:13:52

Resolution: fixed
