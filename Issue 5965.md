# Issue 5965: Check {{{/dev/pts}}} and {{{/dev/shm}}} requirement on linux

archive/issues_005965.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  was jdemeyer jhpalmieri mkoeppe dimpase mjo\n\nSage requires both pseudoterminals (for pexpect) and shared memory (for pyprocessing semaphores). On modern linux, those are implemented via special filesystem mounts:\n- `/dev/pts` for pseudoterminals (of type `devpts`)\n- `/dev/shm` for shared memory (of type `tmpfs`)\nA normal system has those mounts active. However, running sage in a chroot fails in weird ways if we neglect to mount those inside the chroot:\n- the first one makes pexpect interfaces to fail, e.g.:\n\n```\nsage: gap(2)\nA workspace appears to have been corrupted... automatically rebuilding (this is harmless).\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/tornaria/.sage/temp/arf/10828/_home_tornaria__sage_init_sage_0.py in <module>()\n\n/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)\n   1002             return cls(self, x, name=name)\n   1003         try:\n-> 1004             return self._coerce_from_special_method(x)\n   1005         except TypeError:\n   1006             raise\n\n/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in _coerce_from_special_method(self, x)\n   1026             s = '_gp_'\n   1027         try:\n-> 1028             return (x.__getattribute__(s))(self)\n   1029         except AttributeError:\n   1030             return self(x._interface_init_())\n\n/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._gap_ (sage/structure/sage_object.c:3370)()\n\n/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3018)()\n\n/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)\n   1000             return x\n   1001         if isinstance(x, basestring):\n-> 1002             return cls(self, x, name=name)\n   1003         try:\n   1004             return self._coerce_from_special_method(x)\n\n/opt/sage-3.4.1-x86_64-Linux/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)\n   1375             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n   1376                 self._session_number = -1\n-> 1377                 raise TypeError, x\n   1378         self._session_number = parent._session_number\n   1379 \n\nTypeError: Unable to start gap because the command 'gap -r -b -p -T -o 9999G /opt/sage-3.4.1-x86_64-Linux/data//extcode/gap/sage.g' failed.\n```\n\n- the second one makes pyprocessing to fail, which can be reproduced by:\n\n```\nsage: import processing, processing.synchronize                      \nsage: processing._processing.SemLock(processing.synchronize.BOUNDED_SEMAPHORE, 1)                           \n---------------------------------------------------------------------------\nOSError                                   Traceback (most recent call last)\n\n/home/tornaria/.sage/temp/arf/10892/_home_tornaria__sage_init_sage_0.py in <module>()\n\nOSError: [Errno 38] Function not implemented\n```\n\nBoth failures are detected by doctests. The first one all over the place, and the second one by doctests in `sage/parallel/multiprocessing.py` and `sage/parallel/decorate.py`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5965\n\n",
    "created_at": "2009-05-02T23:41:40Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "Check {{{/dev/pts}}} and {{{/dev/shm}}} requirement on linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5965",
    "user": "tornaria"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/5965





---

archive/issue_comments_047241.json:
```json
{
    "body": "Actually, it may make more sense to just check that pseudoterminals and shared memory work (say, from python), and in case of failure on linux suggest the user to check `/dev/pts` and/or `/dev/shm`.",
    "created_at": "2009-05-05T03:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47241",
    "user": "tornaria"
}
```

Actually, it may make more sense to just check that pseudoterminals and shared memory work (say, from python), and in case of failure on linux suggest the user to check `/dev/pts` and/or `/dev/shm`.



---

archive/issue_comments_047242.json:
```json
{
    "body": "Attachment\n\nThis simple python script checks availability of pseudoterminals and shared memory.",
    "created_at": "2009-05-05T03:25:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47242",
    "user": "tornaria"
}
```

Attachment

This simple python script checks availability of pseudoterminals and shared memory.



---

archive/issue_comments_047243.json:
```json
{
    "body": "The python script I attached does the job, except the error messages need to be written (say, inform the user that /dev/pts is possibly missing, etc). Also, this needs to be placed in a proper place in the sage startup scripts or somewhere...",
    "created_at": "2009-05-05T03:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47243",
    "user": "tornaria"
}
```

The python script I attached does the job, except the error messages need to be written (say, inform the user that /dev/pts is possibly missing, etc). Also, this needs to be placed in a proper place in the sage startup scripts or somewhere...



---

archive/issue_comments_047244.json:
```json
{
    "body": "Changing assignee from mabshoff to tornaria.",
    "created_at": "2009-05-05T03:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47244",
    "user": "tornaria"
}
```

Changing assignee from mabshoff to tornaria.



---

archive/issue_comments_047245.json:
```json
{
    "body": "I will look at this later. I think this is a much more elegant solution than what was initially proposed.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T03:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47245",
    "user": "mabshoff"
}
```

I will look at this later. I think this is a much more elegant solution than what was initially proposed.

Cheers,

Michael



---

archive/issue_comments_047246.json:
```json
{
    "body": "A hard to figure out when reported, yet simple fix. 4.0 it is.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T14:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47246",
    "user": "mabshoff"
}
```

A hard to figure out when reported, yet simple fix. 4.0 it is.

Cheers,

Michael



---

archive/issue_comments_047247.json:
```json
{
    "body": "Where does this go?",
    "created_at": "2009-05-28T07:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47247",
    "user": "was"
}
```

Where does this go?



---

archive/issue_comments_047248.json:
```json
{
    "body": "Replying to [comment:6 was]:\n> Where does this go?\n\nWherever the check for, e.g. sage-flags.txt is done, i.e. at startup. The idea is to make sure that those two features are available, because they are actually required by Sage, and if they are missing the error messages tend to be very confusing (see the description for a taste).\n\nNote that this actually happens at least when one does a quick chroot and doesn't mount either /dev/pts and /dev/shm.\n\nJust to record the relative importance of the two: pseudottys are absolutely required for sage (pexpect), while shared memory seems to be only used through pyprocessing, i.e. maybe only dsage needs it.",
    "created_at": "2009-05-28T12:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47248",
    "user": "tornaria"
}
```

Replying to [comment:6 was]:
> Where does this go?

Wherever the check for, e.g. sage-flags.txt is done, i.e. at startup. The idea is to make sure that those two features are available, because they are actually required by Sage, and if they are missing the error messages tend to be very confusing (see the description for a taste).

Note that this actually happens at least when one does a quick chroot and doesn't mount either /dev/pts and /dev/shm.

Just to record the relative importance of the two: pseudottys are absolutely required for sage (pexpect), while shared memory seems to be only used through pyprocessing, i.e. maybe only dsage needs it.



---

archive/issue_comments_047249.json:
```json
{
    "body": "I think this looks good. I've added a patch above that calls this script from the sage startup, as Gonzalo suggested. So I guess I'm positively reviewing Gonzalo's code, but maybe someone should rubber-stamp the code I added that calls it.\n\nHowever, it just occurred to me that we're switching to python 2.6 in the next release -- and that means we need to switch to `multiprocessing` instead of `processing`. I just read the documentation for `multiprocessing` online, and I believe that checking that semaphores are available will be even easier -- according to the first warning on this page:\n  http://docs.python.org/library/multiprocessing.html#introduction\nall we need to do is `import multiprocessing.synchronize`, and it'll fail if not. \n\nSo as soon as an alpha is out with the new python spkg in place, I'll go ahead and update this patch -- it should probably wait to be merged until then, but people are welcome to try it out now and offer other comments.",
    "created_at": "2009-06-21T07:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47249",
    "user": "craigcitro"
}
```

I think this looks good. I've added a patch above that calls this script from the sage startup, as Gonzalo suggested. So I guess I'm positively reviewing Gonzalo's code, but maybe someone should rubber-stamp the code I added that calls it.

However, it just occurred to me that we're switching to python 2.6 in the next release -- and that means we need to switch to `multiprocessing` instead of `processing`. I just read the documentation for `multiprocessing` online, and I believe that checking that semaphores are available will be even easier -- according to the first warning on this page:
  http://docs.python.org/library/multiprocessing.html#introduction
all we need to do is `import multiprocessing.synchronize`, and it'll fail if not. 

So as soon as an alpha is out with the new python spkg in place, I'll go ahead and update this patch -- it should probably wait to be merged until then, but people are welcome to try it out now and offer other comments.



---

archive/issue_comments_047250.json:
```json
{
    "body": "I don't know how the milestone got unset. Oops.",
    "created_at": "2009-06-21T07:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47250",
    "user": "craigcitro"
}
```

I don't know how the milestone got unset. Oops.



---

archive/issue_comments_047251.json:
```json
{
    "body": "This looks incomplete to me, I'm moving it to \"needs work\".",
    "created_at": "2009-07-15T22:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47251",
    "user": "boothby"
}
```

This looks incomplete to me, I'm moving it to "needs work".



---

archive/issue_comments_047252.json:
```json
{
    "body": "Two years later, I've attached an updated Python script. :)\n\nNote that meanwhile also `sage -b` (i.e., `devel/sage/setup.py`) uses semaphores (because it builds the Sage library in parallel by default), which means now Sage also **won't build** without them.\n\nAt least for binary distributions, we should add some check (perhaps calling the attached script) to some start-up script, but please **not** `sage-env` (since that's used by a lot of scripts that simply don't need such a check).",
    "created_at": "2011-07-29T17:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47252",
    "user": "leif"
}
```

Two years later, I've attached an updated Python script. :)

Note that meanwhile also `sage -b` (i.e., `devel/sage/setup.py`) uses semaphores (because it builds the Sage library in parallel by default), which means now Sage also **won't build** without them.

At least for binary distributions, we should add some check (perhaps calling the attached script) to some start-up script, but please **not** `sage-env` (since that's used by a lot of scripts that simply don't need such a check).



---

archive/issue_comments_047253.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-07-29T17:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47253",
    "user": "leif"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_047254.json:
```json
{
    "body": "Updated script to work with newer Python, also advises to mount the respective devices on Linux.",
    "created_at": "2011-07-29T17:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47254",
    "user": "leif"
}
```

Updated script to work with newer Python, also advises to mount the respective devices on Linux.



---

archive/issue_comments_047255.json:
```json
{
    "body": "Changing keywords from \"\" to \"GAP PExpect cannot start server pty pseudo ttys shared memory mount chroot\".",
    "created_at": "2011-08-29T01:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47255",
    "user": "leif"
}
```

Changing keywords from "" to "GAP PExpect cannot start server pty pseudo ttys shared memory mount chroot".



---

archive/issue_comments_047256.json:
```json
{
    "body": "Attachment\n\nRaising the priority to \"critical\" since this issue came up multiple times recently, especially in server setups (which usually use a chroot environment or virtualization), and also minimal Linux installations.\n\nPeople are rather unlikely to immediately relate the failure in starting GAP to pseudo ttys or device mounts.\n\nAlternatively, we could catch / check for the pty error in the code that creates PExpect interfaces, e.g. in `sage/interfaces/gap.py` (around line 903), in order to give a more appropriate error message.",
    "created_at": "2011-08-29T01:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47256",
    "user": "leif"
}
```

Attachment

Raising the priority to "critical" since this issue came up multiple times recently, especially in server setups (which usually use a chroot environment or virtualization), and also minimal Linux installations.

People are rather unlikely to immediately relate the failure in starting GAP to pseudo ttys or device mounts.

Alternatively, we could catch / check for the pty error in the code that creates PExpect interfaces, e.g. in `sage/interfaces/gap.py` (around line 903), in order to give a more appropriate error message.



---

archive/issue_comments_047257.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2011-08-29T01:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47257",
    "user": "leif"
}
```

Changing priority from major to critical.



---

archive/issue_comments_047258.json:
```json
{
    "body": "Likewise, we could add a check for `/dev/shm` to `devel/sage/setup.py`, since building the Sage library doesn't involve starting up Sage, and I wouldn't put such checks into places where they would unnecessarily get run continually or frequently (even when there's no need for e.g. `/dev/pts` at that point, like during the build), as I said earlier.",
    "created_at": "2011-08-29T01:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47258",
    "user": "leif"
}
```

Likewise, we could add a check for `/dev/shm` to `devel/sage/setup.py`, since building the Sage library doesn't involve starting up Sage, and I wouldn't put such checks into places where they would unnecessarily get run continually or frequently (even when there's no need for e.g. `/dev/pts` at that point, like during the build), as I said earlier.



---

archive/issue_comments_047259.json:
```json
{
    "body": "ping",
    "created_at": "2012-03-22T22:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47259",
    "user": "leif"
}
```

ping



---

archive/issue_comments_047260.json:
```json
{
    "body": "I don't really understand the issues here to do anything with this ticket in its current state. If there were a patch to actually apply somewhere, that would at least be a start.",
    "created_at": "2012-03-23T00:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47260",
    "user": "jhpalmieri"
}
```

I don't really understand the issues here to do anything with this ticket in its current state. If there were a patch to actually apply somewhere, that would at least be a start.



---

archive/issue_comments_047261.json:
```json
{
    "body": "Could you please run this script somewhere in the beginning of the build process? I also tried to build sage in a chroot where /dev/shm was not user-writable for some reason and got a not very helpful \"Permission denied\". This script would have given me a much better error message.",
    "created_at": "2015-03-05T21:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47261",
    "user": "thansen"
}
```

Could you please run this script somewhere in the beginning of the build process? I also tried to build sage in a chroot where /dev/shm was not user-writable for some reason and got a not very helpful "Permission denied". This script would have given me a much better error message.



---

archive/issue_comments_047262.json:
```json
{
    "body": "Changing component from distribution to build: configure.",
    "created_at": "2016-04-11T09:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47262",
    "user": "jdemeyer"
}
```

Changing component from distribution to build: configure.



---

archive/issue_comments_047263.json:
```json
{
    "body": "Is this still necessary? If so, it's pretty easy to hack into the `./configure` script:\n\n\n```patch\ndiff --git a/configure.ac b/configure.ac\nindex 78cc95febc..35763c77ac 100644\n--- a/configure.ac\n+++ b/configure.ac\n@@ -150,7 +150,21 @@ The Sage community would also appreciate any patches you s$\n\n # The following are all supported platforms.\n *-*-freebsd*);;\n-*-*-linux*);;\n+*-*-linux*)\n+# We need /dev/pts and /dev/shm mounted on Linux, see Trac 5965.\n+if ! test -d /dev/pts; then\n+AC_MSG_ERROR([[\n+A filesystem of type devpts must be mounted at /dev/pts on Linux.\n+See the pts(4) man page.\n+]])\n+fi\n+if ! test -d /dev/shm; then\n+AC_MSG_ERROR([[\n+A filesystem of type tmpfs must be mounted at /dev/shm on Linux.\n+See the shm_overview(7) man page.\n+]])\n+fi\n+;;\n *-*-darwin*);;\n *-*-solaris*);;\n *-*-cygwin*);;\n```\n",
    "created_at": "2020-08-31T02:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47263",
    "user": "mjo"
}
```

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

archive/issue_comments_047264.json:
```json
{
    "body": "we can add this (and perhaps even a test that /dev/shm is user-writeable (cf comment:21), no harm, even though perhaps nowadays there are no weird environments left where these things are broken.",
    "created_at": "2020-08-31T10:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47264",
    "user": "dimpase"
}
```

we can add this (and perhaps even a test that /dev/shm is user-writeable (cf comment:21), no harm, even though perhaps nowadays there are no weird environments left where these things are broken.



---

archive/issue_comments_047265.json:
```json
{
    "body": "Replying to [comment:24 dimpase]:\n> nowadays there are no weird environments left where these things are broken.\n\nThey were accidentally left out of a chroot in the original report. Catching them at `./configure` just saves a lot of time, since otherwise you go through the whole build and get an incomprehensible test failure a few hours later.\n\nMy main question is, do these things still depend on `/dev/pts` and `/dev/shm` at all? A lot can change in 11 years. And if it's pexpect/pyprocessing that are trying to use them, then it might make more sense to send this check upstream.",
    "created_at": "2020-08-31T11:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47265",
    "user": "mjo"
}
```

Replying to [comment:24 dimpase]:
> nowadays there are no weird environments left where these things are broken.

They were accidentally left out of a chroot in the original report. Catching them at `./configure` just saves a lot of time, since otherwise you go through the whole build and get an incomprehensible test failure a few hours later.

My main question is, do these things still depend on `/dev/pts` and `/dev/shm` at all? A lot can change in 11 years. And if it's pexpect/pyprocessing that are trying to use them, then it might make more sense to send this check upstream.



---

archive/issue_comments_047266.json:
```json
{
    "body": "by the way https://github.com/pexpect/pexpect/releases/tag/4.8.0 - our's is 4.6, more than 2 years old.",
    "created_at": "2020-08-31T12:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47266",
    "user": "dimpase"
}
```

by the way https://github.com/pexpect/pexpect/releases/tag/4.8.0 - our's is 4.6, more than 2 years old.



---

archive/issue_comments_047267.json:
```json
{
    "body": "Changing priority from critical to major.",
    "created_at": "2020-09-03T02:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47267",
    "user": "mkoeppe"
}
```

Changing priority from critical to major.



---

archive/issue_comments_047268.json:
```json
{
    "body": "Replying to [comment:25 mjo]:\n> My main question is, do these things still depend on `/dev/pts` and `/dev/shm` at all? A lot can change in 11 years. \n\nI think it's a tale from ancient linux times. If it is ever reported again, we know what to do.",
    "created_at": "2020-09-03T02:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47268",
    "user": "mkoeppe"
}
```

Replying to [comment:25 mjo]:
> My main question is, do these things still depend on `/dev/pts` and `/dev/shm` at all? A lot can change in 11 years. 

I think it's a tale from ancient linux times. If it is ever reported again, we know what to do.



---

archive/issue_comments_047269.json:
```json
{
    "body": "Let's just close this. The ten-year-old crash log for a collection of packages that no longer exist isn't benefiting anyone. If a user ever reports this problem on a modern system, we can easily fix it now.",
    "created_at": "2021-02-23T02:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47269",
    "user": "mjo"
}
```

Let's just close this. The ten-year-old crash log for a collection of packages that no longer exist isn't benefiting anyone. If a user ever reports this problem on a modern system, we can easily fix it now.



---

archive/issue_comments_047270.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2021-02-23T02:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47270",
    "user": "mjo"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_047271.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-02-26T19:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47271",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047272.json:
```json
{
    "body": "Yes, I agree.",
    "created_at": "2021-02-26T19:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47272",
    "user": "jhpalmieri"
}
```

Yes, I agree.



---

archive/issue_comments_047273.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-04-01T06:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47273",
    "user": "chapoton"
}
```

Resolution: invalid



---

archive/issue_comments_047274.json:
```json
{
    "body": "Replying to [comment:26 dimpase]:\n> by the way https://github.com/pexpect/pexpect/releases/tag/4.8.0 - ours is 4.6, more than 2 years old.\n\nTicket #29240, merged in Sage 9.2.beta11 (released 2020-09-02),\nupgraded to pexpect 4.8.0.",
    "created_at": "2021-04-01T07:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5965#issuecomment-47274",
    "user": "slelievre"
}
```

Replying to [comment:26 dimpase]:
> by the way https://github.com/pexpect/pexpect/releases/tag/4.8.0 - ours is 4.6, more than 2 years old.

Ticket #29240, merged in Sage 9.2.beta11 (released 2020-09-02),
upgraded to pexpect 4.8.0.
