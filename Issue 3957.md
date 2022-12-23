# Issue 3957: notebook -- major bug in opening notebooks and plots

Issue created by migration from https://trac.sagemath.org/ticket/3957

Original creator: was

Original creation time: 2008-08-26 15:50:26

Assignee: boothby


```


On Tue, Aug 26, 2008 at 4:53 AM, Stan Schymanski <schymans@gmail.com> wrote:
>
> Dear all,
>
> Is there a way of saving and automatically re-loading plots generated
> in a notebook when I re-open the notebook?

This is *not* by design, and wasn't the case until very recently.  It's a
bug in the notebook that was introduced very recently.  

>
> Currently, when I close and re-open a notebook, all previously
> displayed plots are gone and even Action... -> Evaluate All does not
> bring them back. I have to keep pressing Shift+Return to see the plots
> again, which is very time consuming. I already figured out that the
> combination of save_session and load_session allows me to re-create
> most of my variables and save a lot of computation time, but it still
> does not bring back the plots.
>
> Thanks for  your help!
>
> Stan
>
> PS: sage 3.1.1 on Mac OS 10.4.11
```



---

Comment by mhansen created at 2008-09-09 01:43:38

I've posted a patch which fixes this issue and have written the corresponding Selenium test which passes with this patch and fails without it.  Some more extensive manual testing should be done to make sure things are be behaving correctly.


---

Attachment

I did hand testing of this, and the bug seems to have been resolved.


---

Comment by mabshoff created at 2008-09-13 01:54:36

Merged in Sage 3.1.2.rc2


---

Comment by mabshoff created at 2008-09-13 01:54:36

Resolution: fixed
