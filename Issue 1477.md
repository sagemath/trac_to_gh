# Issue 1477: notebook -- make it unicode aware

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-12 16:37:05

Assignee: boothby


```


On Dec 12, 2007 7:48 AM, greg2k4`@`mail.ru <greg2k4`@`mail.ru> wrote:
> 
> Hi all,
> 
> I need to use non-english characters (in comments) in Notebook
> worksheet.
> While working, they're shown w/o problem, but if I save ("download to
> file") worksheet, then close
> SAGE, then open again and load .sws file, sometimes (!) I see just
> unicode codes (like %u4041)
> instead of my chars.
> Strange, but sometimes they're loaded correctly...
> I'm using Sage v 2.8.13 (VMware) under winXP Pro.
> 
> Am I missing something?

No, more likely I'm missing something in how that functionality
was implemened.  You're probably one of the first ever Russian uses of 
Sage, and we have had very little testing of Unicode in Sage. 
Hopefully fixing the above is for developers just a 
matter of changing a few lines in 

  SAGE_ROOT/devel/sage/sage/server/noteboook

that relate to loading and saving the file worksheet.txt. 
   
```



---

Comment by was created at 2007-12-13 18:59:48


```
> Could you summarize the situation with rendering problems?  Is it as follows:
> (1) When you try to put them in input cells, they get corrupted on load/save.

To be correct, they're replaced by "non-browser"  unicode codes (like
%u0440 instead of &#x0440; )

> (2) Using edit mode, unicode not in ``'s gets saved just fine.

Yes, as they are NOT processed (as I understand) and get saved "as
is".


> Oh, by the way, when you're entering html in edit mode, you can just do,
> e.g., consider $y^2 = x^3 + \sqrt{x}$ and the formula will get typeset
> using jsmath.

Thanks, can be helpful when writing my materials.
```



---

Comment by mabshoff created at 2008-03-29 22:34:06

Hmm, didn't we fix this by adding UTF-8 support?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 05:54:51

This sounds very much like #2896. It is not fixed.

Cheers,

Michael


---

Comment by mhansen created at 2009-01-19 13:18:35

Sage's support for Unicode and UTF-8 in the notebook is _awful_.  It will take a bit of work to fix this.  For starters, we should be using encodeURIComponent in the Javascript instead of escape since escape fails miserably for non-ASCII characters.

I'll look into this more once the templating is done.  There's too many strings floating as it is.


---

Comment by AlexGhitza created at 2009-01-23 02:49:00

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2009-03-23 21:38:30

Resolution: fixed


---

Comment by mabshoff created at 2009-03-23 21:38:30

Fixed via #4547 and #5211.

Cheers,

Michael
