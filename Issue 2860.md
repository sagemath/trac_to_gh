# Issue 2860: easy-to-fix bug in html.py

Issue created by migration from https://trac.sagemath.org/ticket/2860

Original creator: was

Original creation time: 2008-04-09 05:55:21

Assignee: cwitty


```
Interesting.  That file where the bug is (html.py) hasn't been touched in nearly
a year.  But indeed there is clearly a bug in that function. 

On Tue, Apr 8, 2008 at 3:54 PM,   wrote:
> I just saw this traceback in my patched alpha2:
>  
>         Traceback (most recent call last):
>           File
> "/home/boothby/sage-3.0.alpha2/local/lib/python2.5/site-packages/twisted/internet/defer.py",
> line 185, in addCallbacks
>  
>           File
> "/home/boothby/sage-3.0.alpha2/local/lib/python2.5/site-packages/twisted/internet/defer.py",
> line 323, in _runCallbacks
>  
>           File
> "/home/boothby/sage-3.0.alpha2/local/lib/python2.5/site-packages/twisted/internet/defer.py",
> line 284, in _continue
>  
>           File
> "/home/boothby/sage-3.0.alpha2/local/lib/python2.5/site-packages/twisted/internet/defer.py",
> line 280, in unpause
>  
>         --- <exception caught here> ---
>           File
> "/home/boothby/sage-3.0.alpha2/local/lib/python2.5/site-packages/twisted/internet/defer.py",
> line 323, in _runCallbacks
>  
>           File
> "/home/boothby/sage-3.0.alpha2/local/lib/python2.5/site-packages/twisted/web2/server.py",
> line 296, in <lambda>
>  
>           File
> "/home/boothby/sage-3.0.alpha2/local/lib/python2.5/site-packages/twisted/web2/resource.py",
> line 85, in renderHTTP
>  
>           File
> "/home/boothby/sage-3.0.alpha2/local/lib/python2.5/site-packages/twisted/web2/resource.py",
> line 202, in http_GET
>  
>           File
> "/home/boothby/sage-3.0.alpha2/local/lib/python2.5/site-packages/twisted/web2/resource.py",
> line 128, in http_GET
>  
>           File
> "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py",
> line 1148, in render
>             s = notebook.html(worksheet_filename = self.name, 
> username=self.username)
>           File
> "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py",
> line 1936, in html
>             body = self._html_body(worksheet_filename=worksheet_filename,
> username=username, show_debug=show_debug)
>           File
> "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py",
> line 1609, in _html_body
>             worksheet_html = worksheet.html()
>           File
> "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py",
> line 828, in html
>             s += self.html_worksheet_body(do_print=do_print)
>           File
> "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py",
> line 984, in html_worksheet_body
>             s += cell.html(ncols, do_print=do_print) + '\n'
>           File
> "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/cell.py",
> line 72, in html
>             t = math_parse(t)
>           File
> "/home/boothby/sage/local/lib/python2.5/site-packages/sage/misc/html.py",
> line 33, in math_parse
>             if typ == 'div':
>         exceptions.UnboundLocalError: local variable 'typ' referenced before
> assignment
>  
>  
>  


```



---

Attachment

Attached patch fixes this.  

Nobody has a test case to reproduce the claimed problem.  So I read
the code, vastly improved its documentation, and did make a change that
logically must fix exactly the reported bug.


---

Comment by boothby created at 2008-05-17 19:43:23

Like was said, we've never been able to reproduce this.  However, the "continue" added to line 59 looks like it should do the trick.


---

Comment by mabshoff created at 2008-05-17 19:55:08

Resolution: fixed


---

Comment by mabshoff created at 2008-05-17 19:55:08

Merged in Sage 3.0.2.alpha1
