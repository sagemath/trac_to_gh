# Issue 3069: notebook -- typeset checkbox doesn't work after save/reload

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-30 18:45:08

Assignee: boothby


```


On Wed, Apr 30, 2008 at 11:36 AM, John H Palmieri <jhpalmieri64`@`gmail.com> wrote:
> 
>  This is with Sage 3.0, Firefox 2.0.0.14, linux.
>  
>  If I check the little "Typeset" box at the top of the notebook, save
>  and quit the notebook, then re-enter it, the box is still checked, but
>  my output is not typeset.  If I uncheck it and then check it again, it
>  works.
>  
>  Can anyone else reproduce this?
>  

I've seen this.  I consider it a bug.

```



---

Attachment


---

Comment by jhpalmieri created at 2008-05-13 19:30:31

I've checked it on a Mac with Safari and Firefox, and also on a linux box with Firefox.  Looks good.


---

Comment by jhpalmieri created at 2008-05-13 19:30:31

Resolution: fixed


---

Comment by mabshoff created at 2008-05-13 19:34:38

Hi,

this is now how things work around here. If you review the patch and give it a positive review you should change the summary. Only when the patch is actually merged the release manager closes the ticket. 

Ergo: reopened.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-13 19:34:38

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-05-13 19:34:38

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-05-13 19:35:42

To make the first sentence understandable: "now->not" :)

Cheers,

Michael


---

Comment by jhpalmieri created at 2008-05-13 19:44:01

Behaves well for me, both on a Mac (Safari and Firefox) and on a linux box (Firefox).  Code looks good.


---

Comment by mabshoff created at 2008-05-17 18:41:38

Resolution: fixed


---

Comment by mabshoff created at 2008-05-17 18:41:38

Merged in Sage 3.0.2.alpha1
