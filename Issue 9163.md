# Issue 9163: cygwin: output of a subtle test in expect.py differs slightly on cygwin

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-07 04:00:41

Assignee: tbd

CC:  simonking


```

sage -t  "devel/sage/sage/interfaces/expect.py"             
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/interfaces/expect.py", line 808:
    sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Expected:
    Control-C pressed.  Interrupting Singular. Please wait a few seconds...
    ...
    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
Got:
    ---------------------------------------------------------------------------
    KeyboardInterrupt                         Traceback (most recent call last)
    <BLANKLINE>
    /home/wstein/sage-4.4.3/data/extcode/sage/<ipython console> in <module>()
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _expect_expr(self, expr, timeout)
        815             expr = self._prompt_wait
        816         if self._expect is None:
    --> 817             self._start()
        818         try:
        819             if timeout:
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/singular.pyc in _start(self, alt_message)
        373         """
        374         self.__libs = []
    --> 375         Expect._start(self, alt_message)
        376         # Load some standard libraries.
        377         self.lib('general')   # assumed loaded by misc/constants.py
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _start(self, alt_message, block_during_init)
        447                 c = 'sage-native-execute  ssh %s "nohup sage -cleaner"  &'%self._server
        448                 os.system(c)
    --> 449             self._expect = pexpect.spawn(cmd, logfile=self.__logfile)
        450             if self._do_cleaner():
        451                 cleaner.cleaner(self._expect.pid, cmd)
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/pexpect.pyc in __init__(self, command, args, timeout, maxread, searchwindowsize, logfile)
        331 
        332         self.name = '<' + ' '.join (self.args) + '>'
    --> 333         self.__spawn()
        334 
        335     def __del__(self):
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/pexpect.pyc in __spawn(self)
        399 
        400         try:
    --> 401             self.pid, self.child_fd = pty.fork()
        402         except OSError, e:
        403             raise ExceptionPexpect('Pexpect: pty.fork() failed: ' + str(e))
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python/pty.pyc in fork()
         93 
         94     try:
    ---> 95         pid, fd = os.forkpty()
         96     except (AttributeError, OSError):
         97         pass
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/misc/misc.pyc in __mysig(a, b)
       1690 __alarm_time=0
       1691 def __mysig(a,b):
    -> 1692     raise KeyboardInterrupt, "computation timed out because alarm was set for %s seconds"%__alarm_time
       1693 
       1694 def alarm(seconds):
    <BLANKLINE>
    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_15
***Test Failed*** 1 failures.
```



---

Comment by jdemeyer created at 2010-11-13 10:19:30

Changing component from cygwin to interfaces.


---

Comment by jdemeyer created at 2010-11-13 10:19:30

Changing keywords from "" to "cygwin osx expect doctest".


---

Comment by jdemeyer created at 2010-11-13 10:19:30

Changing assignee from tbd to was.


---

Comment by jdemeyer created at 2010-11-19 19:30:15

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-11-24 12:23:51

Does this happen because the interface might be slow to start up?

Should we move the lines

```python
        if self._expect is None:
            self._start()
```

in `sage.interfaces.expect.Expect._expect_expr` to inside its outermost `try` block?


---

Comment by mpatel created at 2010-11-24 12:28:12

Or remove "Control-C pressed.  Interrupting Singular. Please wait a few seconds..." from the expected output?


---

Comment by jdemeyer created at 2010-12-14 19:45:40

Changing assignee from was to jdemeyer.


---

Comment by jdemeyer created at 2010-12-14 19:45:40

The problem is with the Singular interface, see #10476.


---

Comment by jdemeyer created at 2010-12-14 19:47:09

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-12-14 20:02:42

Apart from this, `expect.py` is a *huge mess*...


---

Comment by jdemeyer created at 2010-12-15 08:42:23

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by jdemeyer created at 2010-12-16 20:37:07

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-12-17 14:54:17

I cannot test this on Cygwin since I don't have a build right now.  I do have one close to completion, but it fails due to #10247.


---

Comment by vbraun created at 2011-01-03 11:43:15

I agree that Singular isn't a good test for the expect interfaces since it is quite finicky with being interrupted/restarting. Improving the Singular interface will be pursued in #10247. In the meantime, positive review for this ticket.


---

Comment by vbraun created at 2011-01-03 11:43:15

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-07 19:16:49

Resolution: fixed
