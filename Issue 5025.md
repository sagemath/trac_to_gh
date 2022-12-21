# Issue 5025: tinymce issues

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-01-19 13:55:59

Assignee: boothby

CC:  mhansen

This was posted to the mailing list about #4705:


```
I have been using TinyMCE for about three weeks now. My ultimate goal
would be to to do something along the lines that David Joyner mentions
in a previous message (have students create worksheets that have
comments/interpretation between the cells).

TinyMCE works very well as far as editing goes, and I didn't test all
buttons available in the tool bar. I think it would be a nice edition
to Sage. It does not seem to affect how responsively the code is
executed, but what I am doing is not very demanding.

However, I noticed the following: (I'm using it in Firefox 3.0.5 in
Ubuntu 10.2. The Sage version is 3.2.2.)

(1)
If I click the menu Action-Evaluate All, exceptions are thrown in
certain situations. The following is the sequence that will trigger
it:
     - Execute the code in some cells
     - Create text using TinyMCE and save it.
     - Do Action-Evaluate All
The problem does not appear to happen with worksheets that had been
saved in a previous Sage session, and then are opened in a new
session. Quitting the worksheet and reopening it also seems to fix the
problem, as long as there were no previous exceptions thrown. I'm not
including a worksheet reproducing the problem because it seems to be
"dynamic", it only occurs as one is working on the worksheet. I am
attaching a text file with the output of the sage session.

(2)
If one creates a link in TinyMCE (highlight text, use the link
button), save the changes in the TinyMCE editor and then follow the
link, when returning to the page with the worksheet (using the
browser's back button), the text that has just been typed disappears.
It reappears if the reload button in the browser is used. (So, it
seems to be a problem of refreshing the cached page). The same happens
if the HTML is directly edited to create the link. In my opinion, the
default behavior on clicking a link in a worksheet should be to open
it in another tab/window in the browser. The idea is that the links
might have reference to documentation, math references, etc, and users
will want to continue to do their math in Sage.

(3)
This is more in the "weirdness" department. I noticed that, sometimes,
each time I reopen a worksheet, a new empty cell is created at the
bottom. I was not able to reproduce it consistently.
```




---

Comment by mhampton created at 2009-01-19 15:16:20

I can reproduce (1) on sage-3.3.alpha0.  I think the new text cells have to have some additional properties, based on the server log's:

line 1049, in render
	    new_input = cell.changed_input_text()
	exceptions.AttributeError: TextCell instance has no attribute 'changed_input_text'


---

Comment by jason created at 2009-01-22 11:27:07

Okay, the (soon-to-be) attached patch fixes (1) and also fixes the bug mhampton pointed out a while ago that there are multiple cells with the same id.

(2) This is how standard linking works in web browsers in general, and is just implemented in TinyMCE to be consistent with most other links on the internet.  I think I'd classify (2) as a wontfix, since there are standard mechanisms for opening a link in another tab that are widely known and understood.

(3) This does seem weird, but we'd need some steps to reproduce the problem.

Hence, I'd say that this ticket is really concerned with the bug in (1), which is addressed in the patch.


---

Comment by jason created at 2009-01-22 11:33:18

These bugfixes also correct a number of small issues that were bugging people too.


---

Comment by jason created at 2009-01-22 16:53:21

(I found one other small issue, which I corrected in the refreshed patch I just attached.)


---

Comment by boothby created at 2009-01-24 10:32:32

I applied the patch, and got the following when I clicked on a worksheet:


```
	Traceback (most recent call last):
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 186, in addCallbacks
	    self._runCallbacks()
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 289, in _continue
	    self.unpause()
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 285, in unpause
	    self._runCallbacks()
	--- <exception caught here> ---
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/server.py", line 296, in <lambda>
	    d.addCallback(lambda res, req: res.renderHTTP(req), self)
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 85, in renderHTTP
	    return method(request)
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 202, in http_GET
	    return super(Resource, self).http_GET(request)
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 128, in http_GET
	    return self.render(request)
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 1333, in render
	    self.worksheet.sage()
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 2547, in sage
	    self.initialize_sage()
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 2523, in initialize_sage
	    self._enqueue_auto_cells()
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 2917, in _enqueue_auto_cells
	    if c.is_auto_cell():
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 1103, in is_auto_cell
	    return 'auto' in self.percent_directives()
	  File "/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 1064, in percent_directives
	    return self._percent_directives
	exceptions.AttributeError: Cell instance has no attribute '_percent_directives'
```



---

Comment by jason created at 2009-01-25 00:22:59

Okay, this looks like a conflict with mhansen's new percent directive handling.  I'm CCing him to see if he knows what is going on here.


---

Comment by jason created at 2009-01-25 00:26:18

Actually, mhansen, is this a problem with your percent directive patch?  In particular, if you create a worksheet with a text cell, is it asked for percent directives, like appears what is happening above?


---

Comment by mhansen created at 2009-01-25 11:24:28

I'm having a hard time duplicating this problem with Sage 3.3.alpha2.


---

Comment by jason created at 2009-01-27 16:28:23

This patch makes the tinymce text cells not break the navigation and evaluate-all functionalities of the notebook.  Without this patch, the navigation arrows stop at text cells and other things become frustratingly cumbersome, so I'm marking this as critical, since tinymce is already merged.

Boothby, can you post the worksheet you had a problem with and confirm that the problem exists on 3.3alpha2?


---

Comment by jason created at 2009-01-27 16:28:23

Changing priority from major to critical.


---

Comment by jason created at 2009-01-27 16:42:29

I can reproduce this on 3.3alpha2 by:

creating a new worksheet

entering 1+1 and evaluating the first cell

create a text cell below all other cells.  Save changes to text cell

create a calculation cell below all other cells.  Enter 1+1 and evaluate

Select "Evaluate All" from the menu.


---

Comment by jason created at 2009-01-27 23:16:12

Okay, I reproduced this with the above steps with a stock sage-3.3alpha2 (without this patch applied), so this patch is not at fault here.  Can we merge this patch and open up another (critical) ticket for the issue with Text cells above?

In other words, can someone change this to a positive review, since this patch isn't the one causing the problem?


---

Comment by jason created at 2009-01-28 17:01:40

I found one problem in the above patch.  I'm posting an updated patch soon.


---

Attachment

Okay, the bug should be fixed.  The only change is on line 3354 or so, where when inserting a text cell after all other cells, the previous patch called insert_new_cell_after, but should have called insert_new_text_cell_after.  The refreshed patch corrects this.


---

Comment by kcrisman created at 2009-01-29 03:51:44

My testing gives that this mysteriously makes the Edit button non-functional, or rather that the Edit button gives the usual interface but without any actual text to edit, not even a blank box - nothing!  

I also once or twice got a similar error to Boothby's where the cell instance was missing a different attribute, but couldn't get it to reproduce reliably. (BTW, I also occasionally get this mysterious addition of new cells, but it's extremely difficult to reproduce and of course it's unrelated to the current patch.)


---

Comment by jason created at 2009-01-29 04:20:27

The edit button works fine for me.  I'm using FF 3.0.5 on Ubuntu Intrepid.

Just to clarify, the edit button works fine for you without this patch applied.  You apply the patch, and the edit button no longer works.  Is that correct?  What browser and OS are you using?

The bug I fixed when I refreshed the patch a few hours ago should fix the cell instance missing an attribute problem.  What was the error message?


---

Comment by jason created at 2009-01-29 04:21:50

kcrisman: also, are you using sage 3.3 alpha 2?  This patch depends on the alpha2 (that alpha contains, for example, the other tinymce patches)


---

Comment by mhansen created at 2009-01-29 06:39:32

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-29 06:39:32

Having looked at the patch and tested it on alpha2 on Firefox on Linux and Safari on OS X.  I think it can go into alpha3 where it will get more widespread testing.

I have no idea what is going on with kcrisman's system.  I'll dedicate some time to take care of all of this before 3.3.


---

Comment by mhansen created at 2009-01-29 06:39:32

Changing assignee from boothby to mhansen.


---

Comment by mabshoff created at 2009-01-29 06:50:26

Resolution: fixed


---

Comment by mabshoff created at 2009-01-29 06:50:26

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by kcrisman created at 2009-01-29 12:49:28

Replying to [comment:18 jason]:
> kcrisman: also, are you using sage 3.3 alpha 2?  This patch depends on the alpha2 (that alpha contains, for example, the other tinymce patches)
That could be the problem.  I just don't know why Edit would work without this patch, then not work with the patch, as well as why this patch would even apply correctly!  Don't worry, I'll let you know if it happens in 3.3 proper - my sense is not, based on mhansen's review.
