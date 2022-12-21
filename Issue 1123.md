# Issue 1123: relocation breaks notebook.

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2007-11-07 17:18:19

Assignee: cwitty

Keywords: relocation, notebook

I had sage installed by the IT folks at my university, and they compiled it in one directory and then moved it to another location.  Most things work, but the notebook has some bugs.  In particular, I can create a worksheet but then I cannot open it.  The notebook says:

Internal Server Error
An error occurred rendering the requested page. More information is available in the server log.

On the server log, there is a reference to the original directory (in this case /root/sage-2.8.11) in the error:

        Traceback (most recent call last):
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 182, in addCallbacks
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 317, in _runCallbacks
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 281, in _continue
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 277, in unpause
        --- <exception caught here> ---
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 317, in _runCallbacks
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/twisted/web2/server.py", line 268, in <lambda>
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 85, in renderHTTP
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 202, in http_GET
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 128, in http_GET
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 1103, in render
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 1151, in sage
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 99, in one_prestarted_sage
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 93, in init_sage_prestart
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 79, in initialized_sage
          File "/root/sage-2.8.11/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 421, in _start
          File "/root/sage-2.8.11/local/lib/python2.5/os.py", line 165, in makedirs
          File "/root/sage-2.8.11/local/lib/python2.5/os.py", line 165, in makedirs
          File "/root/sage-2.8.11/local/lib/python2.5/os.py", line 165, in makedirs
          File "/root/sage-2.8.11/local/lib/python2.5/os.py", line 172, in makedirs
        exceptions.OSError: [Errno 13] Permission denied: '/root/sage-2.8.11'

I am going to have them recompile it in its present directory and see if that fixes it.


---

Comment by mabshoff created at 2007-12-15 03:34:34

After discussion during Bug Day 7 we came to the conclusion that this is an invalid report.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-15 03:34:34

Resolution: invalid
