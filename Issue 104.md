# Issue 104: wiki() doesn't work

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2006-10-02 06:34:20

Assignee: was

I've tried this on both MacIntel and PowerPC Macs (10.4.8).  I get this from SAGE:


```
....
Successfully installed moin-1.5.4.p0
<justin`@`zippo-w:sage-1.4> sage
--------------------------------------------------------
--------------------------------------------------------
| SAGE Version 1.4, Build Date: 2006-10-01             |
| Distributed under the GNU General Public License V2. |

sage: wiki() 
Serving on localhost:9000
localhost - - [01/Oct/2006 23:14:42] "GET / HTTP/1.1" 500 -
[Sun Oct  1 23:14:42 2006] UnboundLocalError: local variable 'File' referenced before assignment

localhost - - [01/Oct/2006 23:14:43] "GET /favicon.ico HTTP/1.1" 200 -
localhost - - [01/Oct/2006 23:14:53] "GET / HTTP/1.1" 500 -
[Sun Oct  1 23:14:53 2006] UnboundLocalError: local variable 'File' referenced before assignment
```

The first entry is from my first contact with the wiki (using http://localhost:9000).  If I refresh, I get the second (from the favicon line).

The first time I contact the wiki, I get a blank page (it's blank when I "view source" as well).  If I refresh the page, I get the crud I'll try to attach to this ticket.

Once I use this the first time, all subsequent attempts, even with a fresh copy of SAGE, give me the crud I'm going to try to attach here.  It's only the very first attempt where I see a totally blank page.

This is with SAGE 1.4, but this same behavior has been with me since the MSRI workshop.




---

Comment by justin created at 2006-10-02 06:35:14

Errors raised when I try to connect to 'localhost:9000' while running the wiki


---

Comment by justin created at 2006-10-02 06:36:23

Changing component from algebraic geometry to user interface.


---

Attachment


---

Comment by was created at 2006-10-03 04:28:23

Hi,

I noticed this error myself once when you first reported it in the list a month ago.
The weird thing is that I haven't had it sense, and I definitely *do* use the
wiki on Intel OS X.  I just tried it in in sage-1.3.7.3 and sage-1.4 and it worked
fine in both cases.   Thus this might be tricky for me to debug.


---

Comment by was created at 2006-10-15 18:29:18

I tried this again, and it even seems to work fine on Justin's computer.
I'm going to close this.


---

Comment by was created at 2006-10-15 18:29:18

Resolution: fixed


---

Comment by was created at 2006-10-16 16:29:57

OK, now I actually fixed it and am really closing it:


```
K, this was enough for me to track it down.  Thanks for your detailed
report and patience.
 
The file local/lib/python/site-packages/MoinMoin/util/filesys.py has this
construction:
 
        try:
            from Carbon import File
            return File.FSRef(path).as_pathname()
        except (ImportError, File.Error):
            return None
 
This is just wrong, since if an error occurs in the import,
then the tuple in the exception can't be constructed!  Maybe nobody
ever tested it, since they didn't have just the right system where
that fails.  Anyway, it should be
 
        try:
            from Carbon import File
        except ImportError:
            return None
        try:
            return File.FSRef(path).as_pathname()
        except File.Error:
            return None
 
With that change the moin-moin wiki works on your computer.  I'll post a new
version of the spkg hopefully today (called moin-1.5.4.p1), or you can make
the change yourself and see it work.  Here's the udiff:
 
--- ../MoinMoin/util/filesys.py 2006-05-11 09:24:00.000000000 -0700
+++ filesys.py  2006-10-16 08:42:18.000000000 -0700
`@``@` -159,10 +159,12 `@``@`
         """
         try:
             from Carbon import File
+        except ImportError:
+            return None
+        try:
             return File.FSRef(path).as_pathname()
-        except (ImportError, File.Error):
+        except File.Error:
             return None
-
 else:
 
     def realPathCase(path):
 }}}
