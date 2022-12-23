# Issue 1751: Notebook revision information leakage

Issue created by migration from https://trac.sagemath.org/ticket/1751

Original creator: nbruin

Original creation time: 2008-01-10 20:34:48

Assignee: boothby

It seems that publishing a notebook publishes the entire notebook directory - including its revision history (if that is what the "snapshots" are). This is almost certainly unexpected behaviour and could lead to serious trouble if someone wants to publish a notebook with an assignment in which he has previously worked out the solution. A tech savvy student might be able to dig that solution up from a "downloaded" SWS file.

Also, currently there does not seem to be any way to delete a published notebook.

I might be wrong on this, but I think it is a serious enough issue that someone should look into it an make sure that no such revision info leakage occurs.

[For "shared" worksheets, similar problems arise. Should there be a "clear revision information" function?]



---

Comment by was created at 2008-05-11 05:54:06

Resolution: invalid


---

Comment by was created at 2008-05-11 05:54:06

Nils wrote:
> It seems that publishing a notebook publishes the entire notebook directory 
> - including its revision history (if that is what the "snapshots" are).
> This is almost certainly unexpected behaviour and could lead to serious trouble ...

That's just not true.  I created a worksheet with 20 stored revisions, published it,
and looked at the published worksheet directory.  It doesn't have those revisions stored
in its snapshot directory. 

> Also, currently there does not seem to be any way to delete a published notebook.

True.  This should be a separate enhancement ticket.  Now #3156

> I might be wrong on this, but I think it is a serious enough issue that 
> someone should look into it an make sure that no such revision info leakage occurs.

I looked and I think you are wrong.  I also looked at the source code which also says
you're wrong. 

> [For "shared" worksheets, similar problems arise. Should there be a "clear 
> revision information" function?]

Revision history shouldn't be something you want to clear, since it's a cheap
and powerful safety feature.  A simple workaround is to just make a copy of
a worksheet using File --> Copy Worksheet.  This results in a new copy of the
original worksheet, but with all revision history gone.
