# Issue 3711: notebook -- folder of worksheets not properly saved

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-23 00:21:00

Assignee: boothby


```


On Wed, Jul 23, 2008 at 1:35 AM, John H Palmieri <jhpalmieri64`@`gmail.com> wrote:
>
> On Jul 11, 3:21 pm, John H Palmieri <jhpalmier...`@`gmail.com> wrote:
>> Since upgrading to Sage 3.0.4 on my intel Mac, when I enter the
>> notebook, my Sage worksheet list shows all of the worksheets I've ever
>> worked on.  If I mark some to be archived or some to be deleted, it
>> has a short-term effect: the worksheets disappear from the "Active"
>> list.  This does not last, though: the next time I start the notebook,
>> the worksheets are back in the active list.
>
> This also happens on my linux box (although I am able to successfully
> empty the trash there).  It's quite annoying to have something like 50
> worksheets listed, instead of the half a dozen I want marked as
> "Active".
>
>> Also, if I mark some worksheets to be deleted, click "Trash" to view
>> the list of those worksheets, then click "Empty Trash", I get a
>> warning about how this will permanently delete the items, etc.  I
>> click "Continue" and am taken back to the list of Active worksheets,
>> but if I click "Trash", I see the old list: the trash has not been
>> emptied.

I can replicate this.

 -- William
```



---

Attachment


---

Comment by mhansen created at 2008-09-08 00:00:13

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2008-09-08 00:00:13

I add a selenium doctest for this (test_3711) which can be found at http://sage.math.washington.edu/home/mhansen/sage_selenium/test_notebook.py


---

Comment by mhansen created at 2008-09-08 00:00:13

Changing status from new to assigned.


---

Comment by TimothyClemans created at 2008-09-08 11:30:55

I didn't run the selenium doctest, but I did various file operations to make sure that the bug was resolved and that some new bug didn't pop up.


---

Comment by mabshoff created at 2008-09-09 00:40:25

Merged in Sage 3.1.2.rc1


---

Comment by mabshoff created at 2008-09-09 00:40:25

Resolution: fixed
