# Issue 225: loading files and worksheets from urls

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-28 05:13:49

Assignee: was


```
On Sat, 27 Jan 2007 21:02:14 -0800, Timothy Clemans <timothy.clemans`@`gmail.com> wrote:

>
> Could a system be added for loading code from a url 

Yes. 

> and uploading
> worksheets from urls?

Yes. 

Great idea!  It wouldn't be hard either, since I just
added (for sage-1.9.1) a file remote_file.py with this
function, which would make adding what you suggest
quite easy.   This will have to wait until > sage-2.0 though.
So this is now trac # 

def get_remote_file(filename, verbose=True):
    """
    INPUT:
        filename -- the URL of a file on the web, e.g.,
             "http://modular.math.washington.edu/myfile.txt"
        verbose -- whether to display download status
    OUTPUT:
        creates a file in the temp directory and returns the
        absolute path to that file.
    """
```



---

Attachment


---

Comment by was created at 2007-08-23 06:01:35


```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1187841524 25200
# Node ID a1d6af5dbe318ece8a09838a6b27779dfe648439
# Parent  969de27b13ba72b3033415ec1929a85d4d5ba57f
More work on trac #225.

diff -r 969de27b13ba -r a1d6af5dbe31 sage/server/notebook/worksheet.py
--- a/sage/server/notebook/worksheet.py Wed Aug 22 20:56:36 2007 -0700
+++ b/sage/server/notebook/worksheet.py Wed Aug 22 20:58:44 2007 -0700
`@``@` -22,6 +22,8 `@``@` import traceback
 import traceback
 import time
 import crypt
+
+import sage.misc.remote_file as remote_file

 import bz2

`@``@` -1775,6 +1777,8 `@``@` class Worksheet:
         return [self.directory() + '/data/'] + [D + x for x in os.listdir(D)]

     def hunt_file(self, filename):
+        if filename.lower().startswith('http://'):
+            filename = remote_file.get_remote_file(filename)
         if not os.path.exists(filename):
             fn = os.path.split(filename)[-1]
             for D in self.load_path():
```



---

Comment by was created at 2007-08-23 06:01:35

Resolution: fixed


---

Comment by mabshoff created at 2007-08-23 06:23:06


```
[07:40] <mabshoff> What about #255 - I thing that works by now, too.
[07:40] <mabshoff> Sorry, #225
[07:40] <was_> That's how I always do it, actually.
[07:41] <was_> #225 is only halfway done.
[07:41] <was_> to finish, this need to work:
[07:41] <mabshoff> okay. Should I target it for 2.9?
[07:41] <was_> load "http://sage.math.washington.edu/home/was/a.sage"
[07:41] <mabshoff> ok
[07:41] <was_> I bet I can implement it in 5 minutes or less.  Whatch.
[07:42] <mabshoff> Maybe I should ask you about more tickets :)
[07:49] <was_> ok, done.
[07:49] <mabshoff> :)
[07:50] <mabshoff> I will quote in the ticket.
[07:50] <was_> except i didn't get to test it from the notebook, since my local install is not done upgrading...
[07:50] <was_> it took 7 minutes.
[07:50] <mabshoff> I guess no cookie for you then :)
[07:51] <was_> oh well.  i'll try harder next time.
```


:)
