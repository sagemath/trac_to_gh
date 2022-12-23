# Issue 4691: Minor docstring change for timeout on notebook

Issue created by migration from https://trac.sagemath.org/ticket/4691

Original creator: kcrisman

Original creation time: 2008-12-04 01:38:59

Assignee: boothby

From sage-support:

> > c) could easily. Did you set the timeout parameter for the server? 
> >       timeout       -- (default: 0) seconds until idle worksheet sessions 
> >                              automatically timeout, i.e., the corresponding 
> >                              Sage session terminates.  0 means 'never timeout'. 

> That seems to have been the other main problem, and we fixed it. 


Care to open a ticket to update the docstring? I think it would be 
good to mention that on low memory systems one should set some timeout 
since otherwise Sage will gobble up all available memory if there are 
many users. 



---

Attachment


---

Comment by ddrake created at 2008-12-04 05:35:42

Patch uploaded. I also edited http://wiki.sagemath.org/StartingTheNotebook .


---

Comment by mabshoff created at 2008-12-04 08:24:07

Thanks, Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-04 14:10:42

Merged in Sage 3.2.2.alpha0


---

Comment by mabshoff created at 2008-12-04 14:10:42

Resolution: fixed
