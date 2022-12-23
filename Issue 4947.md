# Issue 4947: worksheets with interact cells auto-launch

Issue created by migration from https://trac.sagemath.org/ticket/4947

Original creator: mhampton

Original creation time: 2009-01-07 03:42:39

Assignee: boothby

CC:  timothyclemans

Keywords: notebook, interact

Note: this is NOT a duplicate of #4363.

Since 3.2.2 (possibly 3.2.1?), worksheets which contain `@`interact cells auto-launch when the notebook is started.  This is an extremely serious problem for notebooks with many such worksheets.


---

Comment by was created at 2009-01-07 15:12:48

> Note: this is NOT a duplicate of #4363.

> Since 3.2.2 (possibly 3.2.1?), worksheets which contain `@`interact
> cells auto-launch when the notebook is started. This is an extremely 
> serious problem for notebooks with many such worksheets. 

Are you sure???   This would be so wrong/horrible, that I would think I would have noticed.  Also, I can't imagine how this is possible; from my understanding of the notebook code, this is highly unlikely to happen.   Finally, I tried creating a worksheet with an interact cell on my laptop with sage-3.2.3 then restarting the sage notebook server, and that worksheet was *not* running.  In only started running when I clicked to open the worksheet.

Can you please check that you didn't just get confused?  Thanks.


---

Comment by was created at 2009-01-07 17:17:12

I just checked on the public sagenb.org, and *did* observe this behavior.  So it does happen systematically on some installs.  This is obviously a terrible bug.


---

Comment by kcrisman created at 2009-01-07 22:00:05

This happened to me, but I cannot replicate it on 3.2.1 - only 3.2.2.  I hope that helps track it down.


---

Comment by kcrisman created at 2009-01-15 16:44:04

After a non-expert look at all changesets for 3.2.2, the only one that really stuck out was #3950 - not that there was anything immediately obvious in it that would cause this behavior, but it seemed to be the only nontrivial change to the notebook.  There were a few others that touched it, though all (including this one) seemed to be mostly on the listing of worksheets or html, not starting processes!


---

Comment by jason created at 2009-01-16 17:49:14

Is it possible that #3950 could have opened each worksheet, and when doing that, #4363 kicks in and starts running things?

TimothyClemans, can you look at this and see if #3950 caused the problem?


---

Comment by ghtdak created at 2009-01-17 07:48:45

I can verify this behavior on 3.2.3 (ubuntu 8.10 x86_64) and wanted to also verify that the worksheets are indeed running and have `@`interact cells


---

Comment by mhansen created at 2009-01-19 04:20:04

This is fixed by #4363.


---

Comment by mabshoff created at 2009-01-19 06:11:58

Fixed in Sage 3.3.alpha0 by merging #4363.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 06:11:58

Resolution: fixed
