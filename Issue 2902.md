# Issue 2902: notebook -- resize of cell should also fire on paste into the cell

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-13 02:31:29

Assignee: boothby

CC:  was mpatel

When you paste into a cell it should resize as a result.


---

Comment by boothby created at 2008-04-13 16:09:32

This isn't an "easy" problem, but it looks [this](http://www.intridea.com/2007/12/16/faking-onpaste-in-firefox) should do the trick.


---

Attachment

Sets `onpaste` handler to resize cells.


---

Comment by timdumol created at 2009-11-19 19:07:04

This patch should fix it. I don't know how to test this in Selenium (C-C is not always copy, and same with C-V (e.g., mine are C-Z C-C and C-Z C-V)).


---

Comment by timdumol created at 2009-11-19 19:07:10

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-11-19 19:13:04

Oh, depends on #7433.


---

Comment by timdumol created at 2009-11-19 20:57:35

Replying to [comment:4 timdumol]:
> Oh, depends on #7433.
Nevermind. It doesn't.


---

Comment by boothby created at 2009-11-19 21:03:59

That will not work on cells that are created after the page loads.


---

Comment by mpatel created at 2009-11-19 21:17:19

Would any of the "auto-grow" plug-ins mentioned [comment:1:ticket:7201 here] help?  I'll email preliminary patches for two of them to timdumol, in case they're useful.  Unfortunately, I can't work on either ticket right now.

On the plug-ins: I think at least one of them uses a resizing strategy similar to the notebook's.  At least one uses a different strategy.  But the two I tried both have their quirks, discussed (and possibly fixed) in the comments on their pages.


---

Comment by mpatel created at 2009-11-19 21:20:01

Ticket #7201 is related.


---

Comment by was created at 2009-12-08 19:19:18

ISSUES:

1.

> That will not work on cells that are created after the page loads. 

Indeed.  I don't think this patch should go in with that major shortcoming.  Can we just set the onpaste handler for all worksheet cells whenever they are created? 

2. I just tried pasting text into both firefox and safari cells and they *already* do resize.  So is this whole ticket just invalid?   Maybe no patch is needed at all anyways?    That matches with my memory, which is that Tom and I fixed this problem a year ago or so by rewriting the textarea resize code.


---

Comment by was created at 2009-12-08 19:19:24

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2009-12-08 19:30:21

In FF 3.5.5 on Linux, the cells do not resize on paste.  V16 at #6855 includes a fix that seems to work.  I'll try to check other browser-OS combinations.


---

Comment by was created at 2009-12-09 14:25:22

Replying to [comment:11 mpatel]:
> In FF 3.5.5 on Linux, the cells do not resize on paste.  V16 at #6855 includes a fix that seems to work.  I'll try to check other browser-OS combinations.

Good point that I should remark that I was testing with FF 3.5.5 on OS X.

 -- William


---

Comment by mpatel created at 2010-01-18 05:48:51

#7666 subsumes this ticket.  Please close this ticket when that one merges.


---

Comment by timdumol created at 2010-01-19 02:58:15

Resolution: duplicate


---

Comment by timdumol created at 2010-01-19 02:58:15

Fixed with #7666 (sagenb-0.6)
