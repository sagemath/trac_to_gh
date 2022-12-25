# Issue 104: wiki() doesn't work

archive/issues_000104.json:
```json
{
    "body": "Assignee: @williamstein\n\nI've tried this on both MacIntel and PowerPC Macs (10.4.8).  I get this from SAGE:\n\n\n```\n....\nSuccessfully installed moin-1.5.4.p0\n<justin@zippo-w:sage-1.4> sage\n--------------------------------------------------------\n--------------------------------------------------------\n| SAGE Version 1.4, Build Date: 2006-10-01             |\n| Distributed under the GNU General Public License V2. |\n\nsage: wiki() \nServing on localhost:9000\nlocalhost - - [01/Oct/2006 23:14:42] \"GET / HTTP/1.1\" 500 -\n[Sun Oct  1 23:14:42 2006] UnboundLocalError: local variable 'File' referenced before assignment\n\nlocalhost - - [01/Oct/2006 23:14:43] \"GET /favicon.ico HTTP/1.1\" 200 -\nlocalhost - - [01/Oct/2006 23:14:53] \"GET / HTTP/1.1\" 500 -\n[Sun Oct  1 23:14:53 2006] UnboundLocalError: local variable 'File' referenced before assignment\n```\n\nThe first entry is from my first contact with the wiki (using http://localhost:9000).  If I refresh, I get the second (from the favicon line).\n\nThe first time I contact the wiki, I get a blank page (it's blank when I \"view source\" as well).  If I refresh the page, I get the crud I'll try to attach to this ticket.\n\nOnce I use this the first time, all subsequent attempts, even with a fresh copy of SAGE, give me the crud I'm going to try to attach here.  It's only the very first attempt where I see a totally blank page.\n\nThis is with SAGE 1.4, but this same behavior has been with me since the MSRI workshop.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/104\n\n",
    "created_at": "2006-10-02T06:34:20Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "title": "wiki() doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/104",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

I've tried this on both MacIntel and PowerPC Macs (10.4.8).  I get this from SAGE:


```
....
Successfully installed moin-1.5.4.p0
<justin@zippo-w:sage-1.4> sage
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



Issue created by migration from https://trac.sagemath.org/ticket/104





---

archive/issue_comments_000484.json:
```json
{
    "body": "Errors raised when I try to connect to 'localhost:9000' while running the wiki",
    "created_at": "2006-10-02T06:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/104#issuecomment-484",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Errors raised when I try to connect to 'localhost:9000' while running the wiki



---

archive/issue_comments_000485.json:
```json
{
    "body": "Changing component from algebraic geometry to user interface.",
    "created_at": "2006-10-02T06:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/104#issuecomment-485",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Changing component from algebraic geometry to user interface.



---

archive/issue_comments_000486.json:
```json
{
    "body": "Attachment [junk](tarball://root/attachments/some-uuid/ticket104/junk) by justin created at 2006-10-02 06:36:23",
    "created_at": "2006-10-02T06:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/104#issuecomment-486",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Attachment [junk](tarball://root/attachments/some-uuid/ticket104/junk) by justin created at 2006-10-02 06:36:23



---

archive/issue_comments_000487.json:
```json
{
    "body": "Hi,\n\nI noticed this error myself once when you first reported it in the list a month ago.\nThe weird thing is that I haven't had it sense, and I definitely *do* use the\nwiki on Intel OS X.  I just tried it in in sage-1.3.7.3 and sage-1.4 and it worked\nfine in both cases.   Thus this might be tricky for me to debug.",
    "created_at": "2006-10-03T04:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/104#issuecomment-487",
    "user": "https://github.com/williamstein"
}
```

Hi,

I noticed this error myself once when you first reported it in the list a month ago.
The weird thing is that I haven't had it sense, and I definitely *do* use the
wiki on Intel OS X.  I just tried it in in sage-1.3.7.3 and sage-1.4 and it worked
fine in both cases.   Thus this might be tricky for me to debug.



---

archive/issue_comments_000488.json:
```json
{
    "body": "I tried this again, and it even seems to work fine on Justin's computer.\nI'm going to close this.",
    "created_at": "2006-10-15T18:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/104#issuecomment-488",
    "user": "https://github.com/williamstein"
}
```

I tried this again, and it even seems to work fine on Justin's computer.
I'm going to close this.



---

archive/issue_comments_000489.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-15T18:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/104#issuecomment-489",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000490.json:
```json
{
    "body": "OK, now I actually fixed it and am really closing it:\n\n\n```\nK, this was enough for me to track it down.  Thanks for your detailed\nreport and patience.\n \nThe file local/lib/python/site-packages/MoinMoin/util/filesys.py has this\nconstruction:\n \n        try:\n            from Carbon import File\n            return File.FSRef(path).as_pathname()\n        except (ImportError, File.Error):\n            return None\n \nThis is just wrong, since if an error occurs in the import,\nthen the tuple in the exception can't be constructed!  Maybe nobody\never tested it, since they didn't have just the right system where\nthat fails.  Anyway, it should be\n \n        try:\n            from Carbon import File\n        except ImportError:\n            return None\n        try:\n            return File.FSRef(path).as_pathname()\n        except File.Error:\n            return None\n \nWith that change the moin-moin wiki works on your computer.  I'll post a new\nversion of the spkg hopefully today (called moin-1.5.4.p1), or you can make\nthe change yourself and see it work.  Here's the udiff:\n \n--- ../MoinMoin/util/filesys.py 2006-05-11 09:24:00.000000000 -0700\n+++ filesys.py  2006-10-16 08:42:18.000000000 -0700\n@@ -159,10 +159,12 @@\n         \"\"\"\n         try:\n             from Carbon import File\n+        except ImportError:\n+            return None\n+        try:\n             return File.FSRef(path).as_pathname()\n-        except (ImportError, File.Error):\n+        except File.Error:\n             return None\n-\n else:\n \n     def realPathCase(path):\n }}}",
    "created_at": "2006-10-16T16:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/104#issuecomment-490",
    "user": "https://github.com/williamstein"
}
```

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
@@ -159,10 +159,12 @@
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
