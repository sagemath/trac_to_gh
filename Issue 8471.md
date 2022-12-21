# Issue 8471: Upgrade or patch pexpect

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2010-03-07 02:47:33

Assignee: was

Keywords: pexpect

Specifying the full path of a command to `Expect` hits a bug in the `pexpect` module shipped with Sage:

```
karkwa: which sage
/home/saliola/Applications/bin/sage

karkwa: sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: from sage.interfaces.expect import Expect
sage: s = Expect('sage', 'sage> ', command='/home/saliola/Applications/bin/sage')
sage: s.is_running()
False
sage: s._start()
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
/home/saliola/Applications/sage-4.3.3/data/extcode/sage/<ipython console> in <module>()

/home/saliola/Applications/sage-4.3.3/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _start(self, alt_message, block_during_init)
    447                 c = 'sage-native-execute  ssh %s "nohup sage -cleaner"  &'%self._server
    448                 os.system(c)
--> 449             self._expect = pexpect.spawn(cmd, logfile=self.__logfile)
    450             if self._do_cleaner():
    451                 cleaner.cleaner(self._expect.pid, cmd)

/home/saliola/Applications/sage-4.3.3/local/lib/python2.6/site-packages/pexpect.pyc in __init__(self, command, args, timeout, maxread, searchwindowsize, logfile)
    324             self.command = command
    325
--> 326         command_with_path = which(self.command)
    327         if command_with_path == None:
    328             raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)

/home/saliola/Applications/sage-4.3.3/local/lib/python2.6/site-packages/pexpect.pyc in which(filename)
   1131     # Special case where filename already contains a path.

   1132     if os.path.dirname(filename) != '':
-> 1133         if os.access (filename, os.X_OK) and not os.path.isdir(f):
   1134             return filename
   1135

UnboundLocalError: local variable 'f' referenced before assignment
sage: 
```

Note that this is a bug in the `pexpect` Python module shipped with Sage.

```
sage: import pexpect
sage: pexpect.__version__
'2.0'
```

It appears to be fixed in the newest version of `pexpect` (version 2.3).

Should we patch `pexpect` or upgrade?


---

Comment by saliola created at 2010-03-10 23:49:42

We discussed this a bit on sage-devel:
[http://groups.google.com/group/sage-devel/browse_thread/thread/8213950ab1abbeb2](http://groups.google.com/group/sage-devel/browse_thread/thread/8213950ab1abbeb2)

Some highlights:

 - William Stein pointed out that pexpect was rewritten after 2.0 and has had some performance issues; it is worth trying the latest version of pexpect to see if the situation has improved.

 - Robert Bradshaw pointed out that we need to add a blurb to pexpect's SPKG.txt explaining this issue.

So these should be addressed appropriately by this ticket.


---

Comment by saliola created at 2010-03-10 23:49:42

Changing assignee from was to saliola.


---

Comment by saliola created at 2010-05-11 21:38:30

The `gap3.py` file at #8380 contains a reference to this ticket. When this issues is resolved, the comment in that file should be changed appropriately.


---

Comment by leif created at 2015-05-07 03:07:43

Duplicate of #10295.


---

Comment by leif created at 2015-05-07 03:07:43

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2015-05-08 16:31:19

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-05-19 06:42:28

Resolution: duplicate
