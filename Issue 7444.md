# Issue 7444: Broken: searching published worksheets after publishing a worksheet for the first time

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-11-12 14:02:43

Assignee: boothby

CC:  was timdumol

From Tim Dumol (also [comment:6:ticket:7343 here]):

Creating and publishing a worksheet, and then searching for it on the /pub/ page causes an HTTP 500. Server logs show:


```
[...]
File "/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/twist.py", line 1652, in render
            s = render_worksheet_list(ctx.args, pub=True, username=self.username)
          File "/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/twist.py", line 1483, in render_worksheet_list
            search=search, reverse=reverse)
          File "/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/notebook.py", line 1292, in worksheet_list_for_public
            W = [x for x in W if x.satisfies_search(search)]
          File "/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/worksheet.py", line 1977, in satisfies_search
            + open(filename).read().lower())
exceptions.IOError: [Errno 2] No such file or directory: '/home/timdumol/.sage/sage_notebook.sagenb/home/pub/0/worksheet.html'
```



---

Comment by mpatel created at 2009-11-12 14:20:35

Save a newly initialized worksheet.  Apply to sagenb repo.


---

Comment by mpatel created at 2009-11-12 14:33:03

Changing status from new to needs_review.


---

Attachment

Notes:

 * This depends on #7428.
 * I assume it's OK to call `worksheet.save` in `notebook._initialize_worksheet`.
 * `TestWorksheetList.test_searching_for_worksheets` no longer fails --- it now yields an error.


---

Comment by timdumol created at 2009-11-13 20:28:58

Patch works. Positive review.

The error is due to the lack of the javascript libraries on the Log page. This is now #7455.


---

Comment by timdumol created at 2009-11-13 20:28:58

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-08 05:56:26

Resolution: fixed
