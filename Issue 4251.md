# Issue 4251: typo in installation manual

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-10-07 17:47:52

Assignee: tba

CC:  mhansen

This was reported to by a new user:

Section 2.2 Microsoft Windows in the 
Installation Guide seems to have a dead line.
Maybe 
"http://www.sagemath.org/SAGEbin/vmware/"
should be 
"http://www.sagemath.org/download.html"?

I'm not sure what milestone to assign this nor how to
submit a patch since we are in the process of 
switching the documentation over to a new system.



```
Dear David,
  I went to your first link, went to Windows version, at page:
http://www.sagemath.org/doc/inst/node4.html

where the first link is dead: http://www.sagemath.org/SAGEbin/vmware/

But I got the vmware download through some other path (that I don't remember
right now).
        Mark

-----Original Message-----
From: David Joyner 
Sent: Monday, October 06, 2008 12:06 PM
To: ....
Subject: Re: Sage question

Mark Meyerson wrote:
> Dear Dave,
>
> Is their a "quick start" document on line somewhere for SAGE - brief
> directions for a. installing it on my computer and b. using it?  Thanks.
>
> Mark
>
> -----------      
>
>
>   

Yes.
The installation document
http://www.sagemath.org/doc/inst/inst.html

discusses installation and the tutorial
http://www.sagemath.org/doc/tut/tut.html

and constructions document
http://www.sagemath.org/doc/const/const.html

have lots of examples.

Let me know if you need help.

David 
```



---

Comment by mabshoff created at 2008-10-07 21:06:56

David,

feel free to post a patch to fix the issue with the current TeX based documentation. All fixes are also applied (manually) to the ReST tree and while that is likely to come soon I would not hold off on fairly localizes fixes like the above. I would not start a major rewrite of the documentation ;)

Cheers,

Michael


---

Attachment

a change to 2 lines of inst.tex, based on 3.1.3.alpha2


---

Comment by wdj created at 2008-10-08 00:05:40

The attached patch seems to compile fine for me.


---

Comment by jhpalmieri created at 2008-10-17 21:12:40

The patch looks good to me, but I couldn't get it to apply, I think because the relevant lines contain "\SAGE" instead of "SAGE".  I'm attaching a slightly modified patch, which should be used instead.  With that, positive review.


---

Attachment


---

Comment by mabshoff created at 2008-10-18 09:10:42

Merged 4251.patch in Sage 3.2.alpha0


---

Comment by mabshoff created at 2008-10-18 09:10:42

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 09:11:09

Mike,

please make sure to shadow this fix to the ReST documentation.

Cheers,

Michael
