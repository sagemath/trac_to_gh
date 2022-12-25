# Issue 5025: tinymce issues

archive/issues_005025.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @mwhansen\n\nThis was posted to the mailing list about #4705:\n\n\n```\nI have been using TinyMCE for about three weeks now. My ultimate goal\nwould be to to do something along the lines that David Joyner mentions\nin a previous message (have students create worksheets that have\ncomments/interpretation between the cells).\n\nTinyMCE works very well as far as editing goes, and I didn't test all\nbuttons available in the tool bar. I think it would be a nice edition\nto Sage. It does not seem to affect how responsively the code is\nexecuted, but what I am doing is not very demanding.\n\nHowever, I noticed the following: (I'm using it in Firefox 3.0.5 in\nUbuntu 10.2. The Sage version is 3.2.2.)\n\n(1)\nIf I click the menu Action-Evaluate All, exceptions are thrown in\ncertain situations. The following is the sequence that will trigger\nit:\n     - Execute the code in some cells\n     - Create text using TinyMCE and save it.\n     - Do Action-Evaluate All\nThe problem does not appear to happen with worksheets that had been\nsaved in a previous Sage session, and then are opened in a new\nsession. Quitting the worksheet and reopening it also seems to fix the\nproblem, as long as there were no previous exceptions thrown. I'm not\nincluding a worksheet reproducing the problem because it seems to be\n\"dynamic\", it only occurs as one is working on the worksheet. I am\nattaching a text file with the output of the sage session.\n\n(2)\nIf one creates a link in TinyMCE (highlight text, use the link\nbutton), save the changes in the TinyMCE editor and then follow the\nlink, when returning to the page with the worksheet (using the\nbrowser's back button), the text that has just been typed disappears.\nIt reappears if the reload button in the browser is used. (So, it\nseems to be a problem of refreshing the cached page). The same happens\nif the HTML is directly edited to create the link. In my opinion, the\ndefault behavior on clicking a link in a worksheet should be to open\nit in another tab/window in the browser. The idea is that the links\nmight have reference to documentation, math references, etc, and users\nwill want to continue to do their math in Sage.\n\n(3)\nThis is more in the \"weirdness\" department. I noticed that, sometimes,\neach time I reopen a worksheet, a new empty cell is created at the\nbottom. I was not able to reproduce it consistently.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5025\n\n",
    "created_at": "2009-01-19T13:55:59Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "tinymce issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5025",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

CC:  @mwhansen

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



Issue created by migration from https://trac.sagemath.org/ticket/5025





---

archive/issue_comments_038193.json:
```json
{
    "body": "I can reproduce (1) on sage-3.3.alpha0.  I think the new text cells have to have some additional properties, based on the server log's:\n\nline 1049, in render\n\t    new_input = cell.changed_input_text()\n\texceptions.AttributeError: TextCell instance has no attribute 'changed_input_text'",
    "created_at": "2009-01-19T15:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38193",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I can reproduce (1) on sage-3.3.alpha0.  I think the new text cells have to have some additional properties, based on the server log's:

line 1049, in render
	    new_input = cell.changed_input_text()
	exceptions.AttributeError: TextCell instance has no attribute 'changed_input_text'



---

archive/issue_comments_038194.json:
```json
{
    "body": "Okay, the (soon-to-be) attached patch fixes (1) and also fixes the bug mhampton pointed out a while ago that there are multiple cells with the same id.\n\n(2) This is how standard linking works in web browsers in general, and is just implemented in TinyMCE to be consistent with most other links on the internet.  I think I'd classify (2) as a wontfix, since there are standard mechanisms for opening a link in another tab that are widely known and understood.\n\n(3) This does seem weird, but we'd need some steps to reproduce the problem.\n\nHence, I'd say that this ticket is really concerned with the bug in (1), which is addressed in the patch.",
    "created_at": "2009-01-22T11:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38194",
    "user": "https://github.com/jasongrout"
}
```

Okay, the (soon-to-be) attached patch fixes (1) and also fixes the bug mhampton pointed out a while ago that there are multiple cells with the same id.

(2) This is how standard linking works in web browsers in general, and is just implemented in TinyMCE to be consistent with most other links on the internet.  I think I'd classify (2) as a wontfix, since there are standard mechanisms for opening a link in another tab that are widely known and understood.

(3) This does seem weird, but we'd need some steps to reproduce the problem.

Hence, I'd say that this ticket is really concerned with the bug in (1), which is addressed in the patch.



---

archive/issue_comments_038195.json:
```json
{
    "body": "These bugfixes also correct a number of small issues that were bugging people too.",
    "created_at": "2009-01-22T11:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38195",
    "user": "https://github.com/jasongrout"
}
```

These bugfixes also correct a number of small issues that were bugging people too.



---

archive/issue_comments_038196.json:
```json
{
    "body": "(I found one other small issue, which I corrected in the refreshed patch I just attached.)",
    "created_at": "2009-01-22T16:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38196",
    "user": "https://github.com/jasongrout"
}
```

(I found one other small issue, which I corrected in the refreshed patch I just attached.)



---

archive/issue_comments_038197.json:
```json
{
    "body": "I applied the patch, and got the following when I clicked on a worksheet:\n\n\n```\n\tTraceback (most recent call last):\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 186, in addCallbacks\n\t    self._runCallbacks()\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n\t    self.result = callback(self.result, *args, **kw)\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 289, in _continue\n\t    self.unpause()\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 285, in unpause\n\t    self._runCallbacks()\n\t--- <exception caught here> ---\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n\t    self.result = callback(self.result, *args, **kw)\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/server.py\", line 296, in <lambda>\n\t    d.addCallback(lambda res, req: res.renderHTTP(req), self)\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 85, in renderHTTP\n\t    return method(request)\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 202, in http_GET\n\t    return super(Resource, self).http_GET(request)\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 128, in http_GET\n\t    return self.render(request)\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 1333, in render\n\t    self.worksheet.sage()\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 2547, in sage\n\t    self.initialize_sage()\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 2523, in initialize_sage\n\t    self._enqueue_auto_cells()\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 2917, in _enqueue_auto_cells\n\t    if c.is_auto_cell():\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/cell.py\", line 1103, in is_auto_cell\n\t    return 'auto' in self.percent_directives()\n\t  File \"/scratch/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/cell.py\", line 1064, in percent_directives\n\t    return self._percent_directives\n\texceptions.AttributeError: Cell instance has no attribute '_percent_directives'\n```\n",
    "created_at": "2009-01-24T10:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38197",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

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

archive/issue_comments_038198.json:
```json
{
    "body": "Okay, this looks like a conflict with mhansen's new percent directive handling.  I'm CCing him to see if he knows what is going on here.",
    "created_at": "2009-01-25T00:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38198",
    "user": "https://github.com/jasongrout"
}
```

Okay, this looks like a conflict with mhansen's new percent directive handling.  I'm CCing him to see if he knows what is going on here.



---

archive/issue_comments_038199.json:
```json
{
    "body": "Actually, mhansen, is this a problem with your percent directive patch?  In particular, if you create a worksheet with a text cell, is it asked for percent directives, like appears what is happening above?",
    "created_at": "2009-01-25T00:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38199",
    "user": "https://github.com/jasongrout"
}
```

Actually, mhansen, is this a problem with your percent directive patch?  In particular, if you create a worksheet with a text cell, is it asked for percent directives, like appears what is happening above?



---

archive/issue_comments_038200.json:
```json
{
    "body": "I'm having a hard time duplicating this problem with Sage 3.3.alpha2.",
    "created_at": "2009-01-25T11:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38200",
    "user": "https://github.com/mwhansen"
}
```

I'm having a hard time duplicating this problem with Sage 3.3.alpha2.



---

archive/issue_comments_038201.json:
```json
{
    "body": "This patch makes the tinymce text cells not break the navigation and evaluate-all functionalities of the notebook.  Without this patch, the navigation arrows stop at text cells and other things become frustratingly cumbersome, so I'm marking this as critical, since tinymce is already merged.\n\nBoothby, can you post the worksheet you had a problem with and confirm that the problem exists on 3.3alpha2?",
    "created_at": "2009-01-27T16:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38201",
    "user": "https://github.com/jasongrout"
}
```

This patch makes the tinymce text cells not break the navigation and evaluate-all functionalities of the notebook.  Without this patch, the navigation arrows stop at text cells and other things become frustratingly cumbersome, so I'm marking this as critical, since tinymce is already merged.

Boothby, can you post the worksheet you had a problem with and confirm that the problem exists on 3.3alpha2?



---

archive/issue_comments_038202.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-01-27T16:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38202",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to critical.



---

archive/issue_comments_038203.json:
```json
{
    "body": "I can reproduce this on 3.3alpha2 by:\n\ncreating a new worksheet\n\nentering 1+1 and evaluating the first cell\n\ncreate a text cell below all other cells.  Save changes to text cell\n\ncreate a calculation cell below all other cells.  Enter 1+1 and evaluate\n\nSelect \"Evaluate All\" from the menu.",
    "created_at": "2009-01-27T16:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38203",
    "user": "https://github.com/jasongrout"
}
```

I can reproduce this on 3.3alpha2 by:

creating a new worksheet

entering 1+1 and evaluating the first cell

create a text cell below all other cells.  Save changes to text cell

create a calculation cell below all other cells.  Enter 1+1 and evaluate

Select "Evaluate All" from the menu.



---

archive/issue_comments_038204.json:
```json
{
    "body": "Okay, I reproduced this with the above steps with a stock sage-3.3alpha2 (without this patch applied), so this patch is not at fault here.  Can we merge this patch and open up another (critical) ticket for the issue with Text cells above?\n\nIn other words, can someone change this to a positive review, since this patch isn't the one causing the problem?",
    "created_at": "2009-01-27T23:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38204",
    "user": "https://github.com/jasongrout"
}
```

Okay, I reproduced this with the above steps with a stock sage-3.3alpha2 (without this patch applied), so this patch is not at fault here.  Can we merge this patch and open up another (critical) ticket for the issue with Text cells above?

In other words, can someone change this to a positive review, since this patch isn't the one causing the problem?



---

archive/issue_comments_038205.json:
```json
{
    "body": "I found one problem in the above patch.  I'm posting an updated patch soon.",
    "created_at": "2009-01-28T17:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38205",
    "user": "https://github.com/jasongrout"
}
```

I found one problem in the above patch.  I'm posting an updated patch soon.



---

archive/issue_comments_038206.json:
```json
{
    "body": "Attachment [trac_5025-tinymce_bugfix.patch](tarball://root/attachments/some-uuid/ticket5025/trac_5025-tinymce_bugfix.patch) by @jasongrout created at 2009-01-28 17:09:57\n\nOkay, the bug should be fixed.  The only change is on line 3354 or so, where when inserting a text cell after all other cells, the previous patch called insert_new_cell_after, but should have called insert_new_text_cell_after.  The refreshed patch corrects this.",
    "created_at": "2009-01-28T17:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38206",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_5025-tinymce_bugfix.patch](tarball://root/attachments/some-uuid/ticket5025/trac_5025-tinymce_bugfix.patch) by @jasongrout created at 2009-01-28 17:09:57

Okay, the bug should be fixed.  The only change is on line 3354 or so, where when inserting a text cell after all other cells, the previous patch called insert_new_cell_after, but should have called insert_new_text_cell_after.  The refreshed patch corrects this.



---

archive/issue_comments_038207.json:
```json
{
    "body": "My testing gives that this mysteriously makes the Edit button non-functional, or rather that the Edit button gives the usual interface but without any actual text to edit, not even a blank box - nothing!  \n\nI also once or twice got a similar error to Boothby's where the cell instance was missing a different attribute, but couldn't get it to reproduce reliably. (BTW, I also occasionally get this mysterious addition of new cells, but it's extremely difficult to reproduce and of course it's unrelated to the current patch.)",
    "created_at": "2009-01-29T03:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38207",
    "user": "https://github.com/kcrisman"
}
```

My testing gives that this mysteriously makes the Edit button non-functional, or rather that the Edit button gives the usual interface but without any actual text to edit, not even a blank box - nothing!  

I also once or twice got a similar error to Boothby's where the cell instance was missing a different attribute, but couldn't get it to reproduce reliably. (BTW, I also occasionally get this mysterious addition of new cells, but it's extremely difficult to reproduce and of course it's unrelated to the current patch.)



---

archive/issue_comments_038208.json:
```json
{
    "body": "The edit button works fine for me.  I'm using FF 3.0.5 on Ubuntu Intrepid.\n\nJust to clarify, the edit button works fine for you without this patch applied.  You apply the patch, and the edit button no longer works.  Is that correct?  What browser and OS are you using?\n\nThe bug I fixed when I refreshed the patch a few hours ago should fix the cell instance missing an attribute problem.  What was the error message?",
    "created_at": "2009-01-29T04:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38208",
    "user": "https://github.com/jasongrout"
}
```

The edit button works fine for me.  I'm using FF 3.0.5 on Ubuntu Intrepid.

Just to clarify, the edit button works fine for you without this patch applied.  You apply the patch, and the edit button no longer works.  Is that correct?  What browser and OS are you using?

The bug I fixed when I refreshed the patch a few hours ago should fix the cell instance missing an attribute problem.  What was the error message?



---

archive/issue_comments_038209.json:
```json
{
    "body": "kcrisman: also, are you using sage 3.3 alpha 2?  This patch depends on the alpha2 (that alpha contains, for example, the other tinymce patches)",
    "created_at": "2009-01-29T04:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38209",
    "user": "https://github.com/jasongrout"
}
```

kcrisman: also, are you using sage 3.3 alpha 2?  This patch depends on the alpha2 (that alpha contains, for example, the other tinymce patches)



---

archive/issue_comments_038210.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-29T06:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38210",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038211.json:
```json
{
    "body": "Having looked at the patch and tested it on alpha2 on Firefox on Linux and Safari on OS X.  I think it can go into alpha3 where it will get more widespread testing.\n\nI have no idea what is going on with kcrisman's system.  I'll dedicate some time to take care of all of this before 3.3.",
    "created_at": "2009-01-29T06:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38211",
    "user": "https://github.com/mwhansen"
}
```

Having looked at the patch and tested it on alpha2 on Firefox on Linux and Safari on OS X.  I think it can go into alpha3 where it will get more widespread testing.

I have no idea what is going on with kcrisman's system.  I'll dedicate some time to take care of all of this before 3.3.



---

archive/issue_comments_038212.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-29T06:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38212",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_events_005269.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-29T06:50:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5025#event-5269"
}
```



---

archive/issue_comments_038213.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T06:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38213",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038214.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T06:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38214",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_038215.json:
```json
{
    "body": "Replying to [comment:18 jason]:\n> kcrisman: also, are you using sage 3.3 alpha 2?  This patch depends on the alpha2 (that alpha contains, for example, the other tinymce patches)\nThat could be the problem.  I just don't know why Edit would work without this patch, then not work with the patch, as well as why this patch would even apply correctly!  Don't worry, I'll let you know if it happens in 3.3 proper - my sense is not, based on mhansen's review.",
    "created_at": "2009-01-29T12:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5025#issuecomment-38215",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:18 jason]:
> kcrisman: also, are you using sage 3.3 alpha 2?  This patch depends on the alpha2 (that alpha contains, for example, the other tinymce patches)
That could be the problem.  I just don't know why Edit would work without this patch, then not work with the patch, as well as why this patch would even apply correctly!  Don't worry, I'll let you know if it happens in 3.3 proper - my sense is not, based on mhansen's review.
