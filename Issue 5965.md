# Issue 5965: Check {{{/dev/pts}}} and {{{/dev/shm}}} requirement on linux

Issue created by migration from https://trac.sagemath.org/ticket/5965

Original creator: tornaria

Original creation time: 2009-05-02 23:41:40

Assignee: mabshoff

CC:  was jdemeyer jhpalmieri mkoeppe dimpase mjo

Sage requires both pseudoterminals (for pexpect) and shared memory (for pyprocessing semaphores). On modern linux, those are implemented via special filesystem mounts:
 - `/dev/pts` for pseudoterminals (of type `devpts`)
 - `/dev/shm` for shared memory (of type `tmpfs`)
A normal system has those mounts active. However, running sage in a chroot fails in weird ways if we neglect to mount those inside the chroot:
 - the first one makes pexpect interfaces to fail, e.g.:

```
sage: gap(2)
A workspace appears to have been corrupted... automatically rebuilding (this is harmless).
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/tornaria/.sage/temp/arf/10828/_home_tornaria__sage_init_sage_0.py in <module>()

/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1002             return cls(self, x, name=name)
   1003         try:
-> 1004             return self._coerce_from_special_method(x)
   1005         except TypeError:
   1006             raise

/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in _coerce_from_special_method(self, x)
   1026             s = '_gp_'
   1027         try:
-> 1028             return (x.__getattribute__(s))(self)
   1029         except AttributeError:
   1030             return self(x._interface_init_())

/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._gap_ (sage/structure/sage_object.c:3370)()

/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3018)()

/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1000             return x
   1001         if isinstance(x, basestring):
-> 1002             return cls(self, x, name=name)
   1003         try:
   1004             return self._coerce_from_special_method(x)

/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1375             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1376                 self._session_number = -1
-> 1377                 raise TypeError, x
   1378         self._session_number = parent._session_number
   1379 

TypeError: Unable to start gap because the command 'gap -r -b -p -T -o 9999G /opt/sage-3.4.1-x86_64-Linux/data//extcode/gap/sage.g' failed.
```

 - the second one makes pyprocessing to fail, which can be reproduced by:

```
sage: import processing, processing.synchronize                      
sage: processing._processing.SemLock(processing.synchronize.BOUNDED_SEMAPHORE, 1)                           
---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)

/home/tornaria/.sage/temp/arf/10892/_home_tornaria__sage_init_sage_0.py in <module>()

OSError: [Errno 38] Function not implemented
```

Both failures are detected by doctests. The first one all over the place, and the second one by doctests in `sage/parallel/multiprocessing.py` and `sage/parallel/decorate.py`.


---

Comment by tornaria created at 2009-05-05 03:07:13

Actually, it may make more sense to just check that pseudoterminals and shared memory work (say, from python), and in case of failure on linux suggest the user to check `/dev/pts` and/or `/dev/shm`.


---

Attachment

This simple python script checks availability of pseudoterminals and shared memory.


---

Comment by tornaria created at 2009-05-05 03:27:07

The python script I attached does the job, except the error messages need to be written (say, inform the user that /dev/pts is possibly missing, etc). Also, this needs to be placed in a proper place in the sage startup scripts or somewhere...


---

Comment by tornaria created at 2009-05-05 03:27:15

Changing assignee from mabshoff to tornaria.


---

Comment by mabshoff created at 2009-05-05 03:31:42

I will look at this later. I think this is a much more elegant solution than what was initially proposed.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 14:35:26

A hard to figure out when reported, yet simple fix. 4.0 it is.

Cheers,

Michael


---

Comment by was created at 2009-05-28 07:10:43

Where does this go?


---

Comment by tornaria created at 2009-05-28 12:22:12

Replying to [comment:6 was]:
> Where does this go?

Wherever the check for, e.g. sage-flags.txt is done, i.e. at startup. The idea is to make sure that those two features are available, because they are actually required by Sage, and if they are missing the error messages tend to be very confusing (see the description for a taste).

Note that this actually happens at least when one does a quick chroot and doesn't mount either /dev/pts and /dev/shm.

Just to record the relative importance of the two: pseudottys are absolutely required for sage (pexpect), while shared memory seems to be only used through pyprocessing, i.e. maybe only dsage needs it.


---

Comment by craigcitro created at 2009-06-21 07:41:37

I think this looks good. I've added a patch above that calls this script from the sage startup, as Gonzalo suggested. So I guess I'm positively reviewing Gonzalo's code, but maybe someone should rubber-stamp the code I added that calls it.

However, it just occurred to me that we're switching to python 2.6 in the next release -- and that means we need to switch to `multiprocessing` instead of `processing`. I just read the documentation for `multiprocessing` online, and I believe that checking that semaphores are available will be even easier -- according to the first warning on this page:
  http://docs.python.org/library/multiprocessing.html#introduction
all we need to do is `import multiprocessing.synchronize`, and it'll fail if not. 

So as soon as an alpha is out with the new python spkg in place, I'll go ahead and update this patch -- it should probably wait to be merged until then, but people are welcome to try it out now and offer other comments.


---

Comment by craigcitro created at 2009-06-21 07:42:32

I don't know how the milestone got unset. Oops.


---

Comment by boothby created at 2009-07-15 22:10:17

This looks incomplete to me, I'm moving it to "needs work".


---

Comment by leif created at 2011-07-29 17:30:58

Two years later, I've attached an updated Python script. :)

Note that meanwhile also `sage -b` (i.e., `devel/sage/setup.py`) uses semaphores (because it builds the Sage library in parallel by default), which means now Sage also *won't build* without them.

At least for binary distributions, we should add some check (perhaps calling the attached script) to some start-up script, but please *not* `sage-env` (since that's used by a lot of scripts that simply don't need such a check).


---

Comment by leif created at 2011-07-29 17:30:58

Changing status from needs_work to needs_info.


---

Comment by leif created at 2011-07-29 17:53:07

Updated script to work with newer Python, also advises to mount the respective devices on Linux.


---

Comment by leif created at 2011-08-29 01:31:10

Changing keywords from "" to "GAP PExpect cannot start server pty pseudo ttys shared memory mount chroot".


---

Attachment

Raising the priority to "critical" since this issue came up multiple times recently, especially in server setups (which usually use a chroot environment or virtualization), and also minimal Linux installations.

People are rather unlikely to immediately relate the failure in starting GAP to pseudo ttys or device mounts.

Alternatively, we could catch / check for the pty error in the code that creates PExpect interfaces, e.g. in `sage/interfaces/gap.py` (around line 903), in order to give a more appropriate error message.


---

Comment by leif created at 2011-08-29 01:31:10

Changing priority from major to critical.


---

Comment by leif created at 2011-08-29 01:45:27

Likewise, we could add a check for `/dev/shm` to `devel/sage/setup.py`, since building the Sage library doesn't involve starting up Sage, and I wouldn't put such checks into places where they would unnecessarily get run continually or frequently (even when there's no need for e.g. `/dev/pts` at that point, like during the build), as I said earlier.


---

Comment by leif created at 2012-03-22 22:57:20

ping


---

Comment by jhpalmieri created at 2012-03-23 00:18:12

I don't really understand the issues here to do anything with this ticket in its current state. If there were a patch to actually apply somewhere, that would at least be a start.


---

Comment by thansen created at 2015-03-05 21:58:56

Could you please run this script somewhere in the beginning of the build process? I also tried to build sage in a chroot where /dev/shm was not user-writable for some reason and got a not very helpful "Permission denied". This script would have given me a much better error message.


---

Comment by jdemeyer created at 2016-04-11 09:53:02

Changing component from distribution to build: configure.


---

Comment by mjo created at 2020-08-31 02:17:02

Is this still necessary? If so, it's pretty easy to hack into the `./configure` script:


```patch
diff --git a/configure.ac b/configure.ac
index 78cc95febc..35763c77ac 100644
--- a/configure.ac
+++ b/configure.ac
@@ -150,7 +150,21 @@ The Sage community would also appreciate any patches you s$

 # The following are all supported platforms.
 *-*-freebsd*);;
-*-*-linux*);;
+*-*-linux*)
+# We need /dev/pts and /dev/shm mounted on Linux, see Trac 5965.
+if ! test -d /dev/pts; then
+AC_MSG_ERROR([[
+A filesystem of type devpts must be mounted at /dev/pts on Linux.
+See the pts(4) man page.
+]])
+fi
+if ! test -d /dev/shm; then
+AC_MSG_ERROR([[
+A filesystem of type tmpfs must be mounted at /dev/shm on Linux.
+See the shm_overview(7) man page.
+]])
+fi
+;;
 *-*-darwin*);;
 *-*-solaris*);;
 *-*-cygwin*);;
```



---

Comment by dimpase created at 2020-08-31 10:46:24

we can add this (and perhaps even a test that /dev/shm is user-writeable (cf comment:21), no harm, even though perhaps nowadays there are no weird environments left where these things are broken.


---

Comment by mjo created at 2020-08-31 11:41:46

Replying to [comment:24 dimpase]:
> nowadays there are no weird environments left where these things are broken.

They were accidentally left out of a chroot in the original report. Catching them at `./configure` just saves a lot of time, since otherwise you go through the whole build and get an incomprehensible test failure a few hours later.

My main question is, do these things still depend on `/dev/pts` and `/dev/shm` at all? A lot can change in 11 years. And if it's pexpect/pyprocessing that are trying to use them, then it might make more sense to send this check upstream.


---

Comment by dimpase created at 2020-08-31 12:24:29

by the way https://github.com/pexpect/pexpect/releases/tag/4.8.0 - our's is 4.6, more than 2 years old.


---

Comment by mkoeppe created at 2020-09-03 02:54:27

Changing priority from critical to major.


---

Comment by mkoeppe created at 2020-09-03 02:54:27

Replying to [comment:25 mjo]:
> My main question is, do these things still depend on `/dev/pts` and `/dev/shm` at all? A lot can change in 11 years. 

I think it's a tale from ancient linux times. If it is ever reported again, we know what to do.


---

Comment by mjo created at 2021-02-23 02:26:39

Let's just close this. The ten-year-old crash log for a collection of packages that no longer exist isn't benefiting anyone. If a user ever reports this problem on a modern system, we can easily fix it now.


---

Comment by mjo created at 2021-02-23 02:26:39

Changing status from needs_info to needs_review.


---

Comment by jhpalmieri created at 2021-02-26 19:47:10

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2021-02-26 19:47:10

Yes, I agree.


---

Comment by chapoton created at 2021-04-01 06:40:48

Resolution: invalid


---

Comment by slelievre created at 2021-04-01 07:54:47

Replying to [comment:26 dimpase]:
> by the way https://github.com/pexpect/pexpect/releases/tag/4.8.0 - ours is 4.6, more than 2 years old.

Ticket #29240, merged in Sage 9.2.beta11 (released 2020-09-02),
upgraded to pexpect 4.8.0.
