# Issue 2721: parallel doctest not robust against filesystem issues

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-29 17:23:13

Assignee: failure

I ran a parallel doctest while I was editing a file in Emacs.  Evidently Emacs creates strange symlinks that point to nowhere as a file locking mechanism:

```
lrwxrwxrwx 1 cwitty cwitty     46 2008-03-29 09:11 .#randstate.pyx -> cwitty`@`magnetar.newtonlabs.com.3701:1202495200
```


The doctest runner tried to doctest ".#randstate.pyx" and got this error message:

```
Exception in thread Thread-3:
Traceback (most recent call last):
  File "/home/cwitty/sage/local/lib/python2.5/threading.py", line 460, in __bootstrap
    self.run()
  File "/home/cwitty/sage/local/bin/sage-ptest", line 70, in run
    e = test(F, 'doctest '+opts)
  File "/home/cwitty/sage/local/bin/sage-ptest", line 140, in test
    if not skip(F):
  File "/home/cwitty/sage/local/bin/sage-ptest", line 116, in skip
    G = abspath(F)
  File "/home/cwitty/sage/local/bin/sage-ptest", line 86, in abspath
    return strip_automount_prefix(os.path.abspath(x))
  File "/home/cwitty/sage/local/bin/sage-ptest", line 103, in strip_automount_prefix
    inode1 = os.stat(filename)[1]
OSError: [Errno 2] No such file or directory: '/home/cwitty/sage/devel/sage-mq/sage/misc/.#randstate.pyx'
```


There are a couple of problems here.

1) I'm guessing that this crashed this doctest-running thread, so that I was running with one fewer thread than I wanted for the rest of the test run.

2) The problem did not show up in the report at the end of the run.



---

Attachment

Looks good; I tested a couple of things (including my original problem case) and couldn't make it fail.


---

Comment by mabshoff created at 2008-03-29 21:34:52

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 21:34:52

Merged in Sage 2.11.rc0
