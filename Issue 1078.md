# Issue 1078: DSage cannot find Cpu_time.sobj

Issue created by migration from https://trac.sagemath.org/ticket/1078

Original creator: jvoight

Original creation time: 2007-11-03 17:09:24

Assignee: was

Hi Yi,

I'm mostly up to speed, but just tonight I started running into the
following bug:

       Traceback (most recent call last):
         File "/home/jvoight/sage/local/lib/python2.5/site-packages/twisted/internet/posixbase.py",
line 220, in run
           self.mainLoop()
         File "/home/jvoight/sage/local/lib/python2.5/site-packages/twisted/internet/posixbase.py",
line 228, in mainLoop
           self.runUntilCurrent()
         File "/home/jvoight/sage/local/lib/python2.5/site-packages/twisted/internet/base.py",
line 561, in runUntilCurrent
           call.func(*call.args, **call.kw)
         File "/home/jvoight/sage/local/lib/python2.5/site-packages/twisted/internet/task.py",
line 108, in __call__
           d = defer.maybeDeferred(self.f, *self.a, **self.kw)
       --- <exception caught here> ---
         File "/home/jvoight/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py",
line 107, in maybeDeferred
           result = f(*args, **kw)
         File "/home/jvoight/sage/local/bin/dsage_worker.py", line
372, in check_work
           cpu_time = cPickle.loads(open('cpu_time.sobj', 'rb').read())
       exceptions.IOError: [Errno 2] No such file or directory: 'cpu_time.sobj'

Have you patched something recently?

You can check it out by running your favorite jobs on
/home/jvoight/sage/sage on sage.math.  It's possible the problem is that I'm running 2.8.9...


---

Comment by yi created at 2007-11-03 17:33:53

Changing assignee from was to yi.


---

Comment by yi created at 2007-11-03 20:23:48

Reported as fixed by jvoight in 2.8.11.


---

Comment by yi created at 2007-11-03 20:23:48

Resolution: fixed
