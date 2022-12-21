# Issue 637: notebook improvement --

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-11 04:39:49

Assignee: boothby


```
> 1) It would be nice if one could upload directly the text of a
>    worksheet to SAGE and have it automatically evaluated as an
>    uploaded worksheet.

I like this suggestion.  It has always been on my (perhaps only mental)
todo list. 
```



---

Comment by was created at 2007-09-11 04:40:49

Changing priority from major to minor.


---

Comment by was created at 2008-03-17 04:43:12


```
21:39 < boothby> wstein -- can we close #637?
21:40 < wstein> no.
21:40 < wstein> I don't think so.
21:40 < wstein> The idea was supposed to be that you could make a wiki
21:40 < wstein> marked up .txt file, with {{{'s
21:40 < wstein> and upload it.
21:40 < wstein> And get a worksheet.
```



---

Comment by TimothyClemans created at 2008-05-11 02:57:47


```
19:55 < tclemans> for the upload a plain text worksheet ticket: would it just
                  work to create an empty worksheet and then call edit_save
                  with the plain text?
19:55 < wstein-3121> tclemans -- yep.
19:55 < wstein-3121> That's exactly right.
```



---

Attachment


---

Comment by was created at 2008-05-11 05:04:01

The attached patch:

  1. Implements uploading .txt files (plain text worksheets).
  2. Adds lots of related documentation, docstrings, doctests, etc., and clean up some related code.


---

Comment by TimothyClemans created at 2008-05-11 14:05:40

I can't seem to apply the patch.


```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/637/sage-637.patch?format=raw')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/637/sage-637.patch?format=raw
Loading: [..]
cd "/home/tclemans/sage-3.0/devel/sage" && hg status
cd "/home/tclemans/sage-3.0/devel/sage" && hg status
cd "/home/tclemans/sage-3.0/devel/sage" && hg import   "/home/tclemans/.sage/temp/sage/27583/tmp_0.patch"
applying /home/tclemans/.sage/temp/sage/27583/tmp_0.patch
patching file sage/server/notebook/notebook.py
Hunk #1 FAILED at 148
1 out of 4 hunks FAILED -- saving rejects to file sage/server/notebook/notebook.py.rej
abort: patch failed to apply
sage: version()
'SAGE Version 3.0.1, Release Date: 2008-05-05'
```



---

Comment by mabshoff created at 2008-05-11 14:07:56

This is likely a dependency issue. William can provide a dependency tree for the 15+ notebook patches he did during Bug Day 12.

Cheers,

Michael


---

Comment by boothby created at 2008-05-12 06:15:15

I applied the patches in the following order and had no problems:

```
1733
1864
2359
2636
2884
2992
3024
3053
637
```



---

Comment by boothby created at 2008-05-12 06:23:40

Works, except when I tried to upload a rather old (from SD3) worksheet:


```
2008-05-11 22:47:55-0700 [-] cd "/home/boothby/.sage/temp/eight/32244/dir_1"; tar -jxf "/home/boothby/.sage/temp/eight/32244/dir_0/pippenger.sws"
2008-05-11 22:47:55-0700 [-] Exception rendering:
2008-05-11 22:47:55-0700 [-] Unhandled Error
        Traceback (most recent call last):
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 609, in gotResult
            _deferGenerator(g, deferred)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 586, in _deferGenerator
            deferred.callback(result)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 242, in callback
            self._startRunCallbacks(result)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 307, in _startRunCallbacks
            self._runCallbacks()
        --- <exception caught here> ---
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 323, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 230, in <lambda>
            ).addCallback(lambda res: self.render(request))
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 326, in render
            W = notebook.import_worksheet(filename, self.username)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 800, in import_worksheet
            return self._import_worksheet_sws(filename, owner)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 882, in _import_worksheet_sws
            worksheet_txt = open(text_filename).read()
        exceptions.IOError: [Errno 2] No such file or directory: '/home/boothby/.sage/temp/eight/32244/dir_1/pippenger/worksheet.txt'
```


It would be nice be able to recover this.  It isn't a problem (for me) to do this manually, and this is probably irrelevant to this ticket.


---

Comment by boothby created at 2008-05-12 06:24:26

Accidentally pasted this url to the description, not my comment:


http://sage.math.washington.edu/home/boothby/pippenger.sws


---

Attachment


---

Comment by boothby created at 2008-05-15 02:00:20

This occurs whenever I try to upload from a URL:


```
2008-05-14 18:28:20-0700 [-] Unhandled Error
        Traceback (most recent call last):
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 609, in gotResult
            _deferGenerator(g, deferred)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 586, in _deferGenerator
            deferred.callback(result)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 242, in callback
            self._startRunCallbacks(result)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 307, in _startRunCallbacks
            self._runCallbacks()
        --- <exception caught here> ---
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 323, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 230, in <lambda>
            ).addCallback(lambda res: self.render(request))
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 333, in render
            os.unlink(filename)
        exceptions.UnboundLocalError: local variable 'filename' referenced before assignment
```



---

Attachment


---

Comment by boothby created at 2008-05-15 03:17:02

works!


---

Comment by mabshoff created at 2008-05-17 18:36:20

Merged all three patches in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-17 18:36:20

Resolution: fixed
