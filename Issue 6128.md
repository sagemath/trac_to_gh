# Issue 6128: [with patch; needs review] Bug - sage-cleaner failed due to NULLs in spawned-processes files written by cleaner.py

Issue created by migration from https://trac.sagemath.org/ticket/6128

Original creator: was

Original creation time: 2009-05-25 13:18:17

Assignee: cwitty

From: adavid (on sage-devel)

```
After building 4.0rc0 overnight, on my laptop, I started make test
the next morning. . I shutdown the laptop before completion as I had
to rush out the door (suspend would have been a good idea...).

Regardless, I ended up with a temporary file structure with a number
of
spawned_processes files consisting of NULLs which triggers the bug as
detailed below.

Why is there NULLs instead of numeric string? <--rhetorical question

$SAGE_BASE/sage-main/sage/interfaces/cleaner.py writes the PID

Async I/O means the PID may or may not be written on a shutdown/power
outage etc.

Patch:
(against 4.0rc0)

# HG changeset patch
# User Anthony David <adavid@adavid.com.au>
# Date 1243176398 -36000
# Node ID 958178a11b9e809788f1eda0cc29107c456a1bbe
# Parent  b25ac645ae77e49db250243280eab38c2431937a
Improve write assurance of spawned_processes file by local/bin/sage-
cleaner

diff -r b25ac645ae77 -r 958178a11b9e sage/interfaces/cleaner.py
--- a/sage/interfaces/cleaner.py Thu May 21 07:10:11 2009 -0700
+++ b/sage/interfaces/cleaner.py Mon May 25 00:46:38 2009 +1000
@@ -28,6 +28,8 @@
            return
        o = open(F,'w')
    o.write('%s %s\n'%(pid, cmd))
+    o.flush()
+    os.fsync(f.fileno())
    o.close()
    start_cleaner_if_not_running()



Notes:


- Linux carbonate 2.6.18-4-686 #1 SMP Mon Mar 26 17:17:36 UTC 2007
i686 GNU/Linux
- Debian GNU/Linux 5.0

- tested patch with a shutdown during a make test, 82 spawned-
processes files created.
Successful sage-cleaner invocation on sage  startup.

- no tests yet on other OSes/arches etc

-  The sage-cleaner statement i=L.find(' ') in kill_spawned_jobs fails
to find any spaces

- could fix the above problem but it is better to attack the root
cause,
hence the patch to cleaner.py and not sage-cleaner

- patch could be improved by creating a temporary file and them
performing
a rename after the close.

- The debug print statements in sage-cleaner were uncommented to
assist with
defining the problem

- Don't have access to TRAC

- This is not a specific 4.0rc0 bug

Bug:


anthonyd@carbonate:~/sage-4.0.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
starting the cleaner
sage: doing a cleanup
checking on 4306
it is no longer running, so we clean up
SAGE Cleaner: deleting /home/anthonyd/.sage//temp/carbonate//4306
checking on 4623
it is running
checking on 31727
it is no longer running, so we clean up
killing 31727's spawned jobs
| Sage Version 4.0.rc0, Release Date: 2009-05-21                     |
| Type notebook() for the GUI, and license() for information.        |
SAGE-Cleaner: trying to kill  with parent 31727

Traceback (most recent call last):
 File "/home/anthonyd/sage-4.0.rc0/local/bin/sage-cleaner", line 108,
in <module>
   while cleanup() > 0:
 File "/home/anthonyd/sage-4.0.rc0/local/bin/sage-cleaner", line 53,
in cleanup
   if not e or (e and kill_spawned_jobs(spawned_processes,
parent_pid)):
 File "/home/anthonyd/sage-4.0.rc0/local/bin/sage-cleaner", line 75,
in kill_spawne\
d_jobs
   os.killpg(int(pid), 9)
ValueError: invalid literal for int() with base 10: ''


...

$ ls -laR /home/anthonyd/.sage/temp/carbonate/31727/
/home/anthonyd/.sage/temp/carbonate/31727/:
total 12
drwxr-xr-x 3 anthonyd anthonyd    46 2009-05-24 06:58 .
drwxr-xr-x 9 anthonyd anthonyd 12288 2009-05-24 22:26 ..
drwxr-xr-x 2 anthonyd anthonyd    21 2009-05-24 06:58 interface
-rw-r--r-- 1 anthonyd anthonyd    10 2009-05-24 06:58
spawned_processes

/home/anthonyd/.sage/temp/carbonate/31727/interface:
total 4
drwxr-xr-x 2 anthonyd anthonyd  21 2009-05-24 06:58 .
drwxr-xr-x 3 anthonyd anthonyd  46 2009-05-24 06:58 ..
-rw-r--r-- 1 anthonyd anthonyd 110 2009-05-24 06:58 tmp31727

 od -xc /home/anthonyd/.sage/temp/carbonate/31727/spawned_processes
0000000 0000 0000 0000 0000 0000
        \0  \0  \0  \0  \0  \0  \0  \0  \0  \0
0000012
```



---

Comment by adavid created at 2009-05-26 00:46:47

Multiple tests of patch showed that null file was still created on occasions during shutdown.
Was unable to reproduce NULL-populated spawned-processes files by running test
and interrupting it with a power outage.
Conclusion: Supplied patch needs more work. Will try using all os level I/O functions
and introduce temp/rename approach.


---

Comment by adavid created at 2009-06-01 22:11:08

Patch ammended: typo.

Tested OK on i686 Debian 5.0


```
# HG changeset patch
# User Anthony David <adavid@adavid.com.au>
# Date 1243893998 -36000
# Node ID 82f9583a45eee9dae4ec4c8cde865e96c392396c
# Parent  fd89fee664d87b20ab77bb6e248d9a71c17affe4
Improve write assurance of spawned_processes files by cleaner

diff -r fd89fee664d8 -r 82f9583a45ee sage/interfaces/cleaner.py
--- a/sage/interfaces/cleaner.py	Fri May 29 21:41:28 2009 -0700
+++ b/sage/interfaces/cleaner.py	Tue Jun 02 08:06:38 2009 +1000
@@ -28,6 +28,8 @@
             return
         o = open(F,'w')
     o.write('%s %s\n'%(pid, cmd))
+    o.fflush()
+    os.fsync(o.fileno())
     o.close()
     start_cleaner_if_not_running()
 
```



---

Attachment

cleaner.patch


---

Attachment

Please ignore 12339.patch. Uploaded second patch (trac_6128.patch) to conform to patch name standards.


---

Comment by was created at 2009-06-20 14:40:03

I used 

```
sage -merge 6128 -t long -n 12
```


to try testing this on sage.math (debian 64-bit), and almost immediately got errors:


```
sage -t -long devel/sage/doc/en/tutorial/introduction.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2/devel/sage-main/doc/en/tutorial/introduction.rst", line 45:
    sage: E.rank()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[12]>", line 1, in <module>
        E.rank()###line 45:
    sage: E.rank()
      File "/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1714, in rank
        X = self.mwrank()
      File "/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 483, in mwrank
        return mwrank(self.a_invariants())
      File "/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/sage/interfaces/mwrank.py", line 77, in __call__
        return self.eval(str(cmd))
      File "/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/sage/interfaces/mwrank.py", line 97, in eval
        return Expect.eval(self, *args, **kwds)
      File "/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 975, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 637, in _eval_line
        self._start()
      File "/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 452, in _start
        cleaner.cleaner(self._expect.pid, cmd)
      File "/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/sage/interfaces/cleaner.py", line 31, in cleaner
        o.fflush()
    AttributeError: 'file' object has no attribute 'fflush'
**********************************************************************
1 items had failures:
   1 of  17 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the 
```


I also tried applying the patch manually.

I then keep seeing 

```
  File "/scratch/wstein/build/sage-4.0.2/local/bin/sage-cleaner", line 75, in kill_spawned_jobs
    os.killpg(int(pid), 9)
ValueError: invalid literal for int() with base 10: ''
```


which was the error that started this whole ticket... and which is an error I have never seen before today.

I then patched sage-cleaner so that it just deletes files that contain this empty pid and Sage works for me again.

I did try applying this patch again, but got lots of errors about

```
        o.fflush()
    AttributeError: 'file' object has no attribute 'fflush'
```


Anyway, in short, this patch doesn't work at all for me.  Maybe fflush works on some platforms but evidently not 64-bit debian linux.


---

Comment by ddrake created at 2009-11-02 01:15:39

Replying to [comment:4 was]:
> I also tried applying the patch manually.
> 
> I then keep seeing 
> {{{
>   File "/scratch/wstein/build/sage-4.0.2/local/bin/sage-cleaner", line 75, in kill_spawned_jobs
>     os.killpg(int(pid), 9)
> ValueError: invalid literal for int() with base 10: ''
> }}}
> 
> which was the error that started this whole ticket... and which is an error I have never seen before today.

I'm seeing a similar error in a freshly-built vanilla 4.2 on Ubuntu Jaunty: the build finished without errors, and when I start Sage, I get:

```
$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Traceback (most recent call last):
  File "/home/drake/k/urohome/sage-4.2/local/bin/sage-cleaner", line 108, in <module>
    while cleanup() > 0:
  File "/home/drake/k/urohome/sage-4.2/local/bin/sage-cleaner", line 53, in cleanup
    if not e or (e and kill_spawned_jobs(spawned_processes, parent_pid)):
  File "/home/drake/k/urohome/sage-4.2/local/bin/sage-cleaner", line 75, in kill_spawned_jobs
    os.killpg(int(pid), 9)
ValueError: invalid literal for int() with base 10: '\xb2\xb3\xb3M\xc7'
| Sage Version 4.2, Release Date: 2009-10-24                         |
| Type notebook() for the GUI, and license() for information.        |
sage: 
```

This seems to be slightly different than the reported bug, but I'm seeing the same errors that William did above, which is quite strange.


---

Comment by ddrake created at 2009-11-02 01:52:51

Replying to [comment:5 ddrake]:
> I'm seeing a similar error in a freshly-built vanilla 4.2 on Ubuntu Jaunty:

Ack, typo: it's Karmic.


---

Comment by adavid created at 2009-11-28 01:21:20

Information only: Testing in progress. Update coming,
