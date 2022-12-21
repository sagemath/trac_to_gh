# Issue 5155: Sage 3.3.a3: fix doctests that want write access to $SAGE_LOCAL

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-02 01:25:42

Assignee: mabshoff

CC:  lftabera leif

All doctests in Sage should pass when they are run as a user that does not own the Sage tree. To do that set SAGE_TESTDIR to some place writable, i.e.

```
export SAGE_TESTDIR=/scratch/mabshoff/tmp
```

and run the doctests on a Sage install that isn't owned by the user. When doing so the following doctests fail:

```
	sage -t -long devel/sage/sage/matrix/matrix2.pyx # 1 doctests failed
	sage -t -long devel/doc/tut/tut.tex # 5 doctests failed
	sage -t -long devel/sage/sage/interfaces/qepcad.py # 2 doctests failed
	sage -t -long devel/sage/sage/plot/plot.py # 6 doctests failed
	sage -t -long devel/sage/sage/databases/database.py # 1 doctests failed
	sage -t -long devel/sage/sage/calculus/calculus.py # 1 doctests failed
	sage -t -long devel/sage/sage/misc/package.py # 1 doctests failed
	sage -t -long devel/sage/sage/gsl/ode.pyx # 4 doctests failed
	sage -t -long devel/sage/sage/server/support.py # 1 doctests failed
	sage -t -long devel/sage/sage/server/notebook/notebook.py # 1 doctests failed
	sage -t -long devel/sage/sage/server/notebook/twist.py # 8 doctests failed
	sage -t -long devel/sage/sage/structure/sage_object.pyx # 6 doctests failed
```

This ticket might need to be split up since it covers a rather large number of doctest failures.

Cheers,

Michael


---

Comment by mhansen created at 2010-01-19 07:56:42

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-01-21 21:04:23

Before applying the patch, I get two doctest failures (with a non-writeable Sage install).  Applying the patch "trac_5155.patch" fixes both.  So positive review for that.

The scripts patch wasn't necessary to get those tests to pass, and it also doesn't apply cleanly to 4.3.1:

```
applying /Users/palmieri/Downloads/scripts_5155.patch
patching file sage-doctest
Hunk #1 FAILED at 55
1 out of 1 hunks FAILED -- saving rejects to file sage-doctest.rej
unable to find 'sage-dsage-trial' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage-dsage-trial.rej
patching file sage-maketest
Hunk #1 succeeded at 1 with fuzz 1 (offset -1 lines).
patching file sage-test
Hunk #1 FAILED at 40
1 out of 1 hunks FAILED -- saving rejects to file sage-test.rej
sage-dsage-trial: No such file or directory
abort: patch failed to apply
```

The changes there look fine in principle, though.  So once it's rebased, positive review there, too.


---

Comment by jhpalmieri created at 2010-01-21 21:04:23

Changing status from needs_review to needs_work.


---

Comment by lftabera created at 2010-09-23 11:10:16

Some of the doctest are ok nowadays but there are other new fails. See for example #9965

I can confirm that, with sage 4.5.3 I get the following doctest failures:

        sage -t  -long "devel/sage/doc/common/builder.py"
        sage -t  -long "devel/sage/sage/interfaces/qepcad.py"
        sage -t  -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
        sage -t  -long "devel/sage/sage/modular/hecke/submodule.py"
        sage -t  -long "devel/sage/sage/modular/abvar/abvar.py"
        sage -t  -long "devel/sage/sage/lfunctions/sympow.py"

All except quecad are trying to be solved in #9965


---

Comment by lftabera created at 2010-09-23 11:11:17

qepcad failures


```
sage -t -long "devel/sage/sage/interfaces/qepcad.py"        
**********************************************************************
File "/opt/SAGE/sage/devel/sage/sage/interfaces/qepcad.py", line 638:
    sage: _rewrite_qepcadrc()
Exception raised:
    Traceback (most recent call last):
      File "/opt/SAGE/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/opt/SAGE/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/opt/SAGE/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        _rewrite_qepcadrc()###line 638:
    sage: _rewrite_qepcadrc()
      File "/opt/SAGE/sage/local/lib/python/site-packages/sage/interfaces/qepcad.py", line 660, in _rewrite_qepcadrc
        open(fn, 'w').write(text)
    IOError: [Errno 13] Permission denied: '/opt/SAGE/sage/local//default.qepcadrc'
**********************************************************************
File "/opt/SAGE/sage/devel/sage/sage/interfaces/qepcad.py", line 689:
    sage: Qepcad_expect(memcells=100000, logfile=sys.stdout)
Exception raised:
    Traceback (most recent call last):
      File "/opt/SAGE/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/opt/SAGE/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/opt/SAGE/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[3]>", line 1, in <module>
        Qepcad_expect(memcells=Integer(100000), logfile=sys.stdout)###line 689:
    sage: Qepcad_expect(memcells=100000, logfile=sys.stdout)
      File "/opt/SAGE/sage/local/lib/python/site-packages/sage/interfaces/qepcad.py", line 692, in __init__
        _rewrite_qepcadrc()
      File "/opt/SAGE/sage/local/lib/python/site-packages/sage/interfaces/qepcad.py", line 660, in _rewrite_qepcadrc
        open(fn, 'w').write(text)
    IOError: [Errno 13] Permission denied: '/opt/SAGE/sage/local//default.qepcadrc'
**********************************************************************
2 items had failures:
   1 of   6 in __main__.example_3
   1 of   4 in __main__.example_6
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/usuario/.sage//tmp/.doctest_qepcad.py
         [1.9 s]
```



---

Comment by lftabera created at 2010-09-23 14:40:00

Another issue, if you compile sage but the very first access of sage is made by a user without write permissions, you get the following error:

----------------------------------------------------------------------
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/SAGE/sage-4.5.3/local/bin/sage-location", line 174, in <module>
    t, R = install_moved()
  File "/opt/SAGE/sage-4.5.3/local/bin/sage-location", line 18, in install_moved
    write_flags_file()
  File "/opt/SAGE/sage-4.5.3/local/bin/sage-location", line 82, in write_flags_file
    open(flags_file,'w').write(get_flags_info())
IOError: [Errno 13] Permission denied: '/opt/SAGE/sage-4.5.3/local/lib/sage-flags.txt'


---

Comment by jhpalmieri created at 2011-09-12 23:53:54

With Sage 4.7.2.alpha2, I see problems with qepcad and sympow.  I think the qepcad problem should be easy to solve, basically as mhansen did before:

```diff
diff --git a/sage/interfaces/qepcad.py b/sage/interfaces/qepcad.py
--- a/sage/interfaces/qepcad.py
+++ b/sage/interfaces/qepcad.py
`@``@` -636,14 +636,14 `@``@` def _rewrite_qepcadrc():
     EXAMPLES:
         sage: from sage.interfaces.qepcad import _rewrite_qepcadrc
         sage: _rewrite_qepcadrc()
-        sage: from sage.misc.misc import SAGE_LOCAL
-        sage: open('%s/default.qepcadrc'%SAGE_LOCAL).readlines()[-1]
+        sage: from sage.misc.misc import DOT_SAGE
+        sage: open('%s/default.qepcadrc'%DOT_SAGE).readlines()[-1]
         'SINGULAR .../local//bin'
     """
     global _rewrote_qepcadrc
     if _rewrote_qepcadrc: return
 
-    SL = sage.misc.misc.SAGE_LOCAL
+    SL = sage.misc.misc.DOT_SAGE
     fn = '%s/default.qepcadrc'%SL
     text = \
 """# THIS FILE IS AUTOMATICALLY GENERATED -- DO NOT EDIT
```

Sympow will be harder to deal with, because of how the spkg is written: it tries to write files to SAGE_LOCAL/lib/sympow.  See [http://trac.sagemath.org/sage_trac/ticket/9703#comment:9](http://trac.sagemath.org/sage_trac/ticket/9703#comment:9) for a possible fix.

I'm attaching a patch to try to deal with the situation when you run Sage for the very first time as a user without write permissions.

Finally, there may be other issues if you compile Sage but don't run it, and then run doctests as a user without write permissions (the first time doctests get run, they might write some files which don't need to be written later).  These issues should be fixed, too.


---

Comment by jdemeyer created at 2011-10-17 12:05:42

I'm not sure this patch is a good idea or needed, considering #11926.  If the Sage install was moved, it is probably good to bail out with an error if there is no write access.


---

Comment by jdemeyer created at 2011-10-17 12:24:04

Changing assignee from mabshoff to jdemeyer.


---

Comment by jdemeyer created at 2011-10-17 16:09:58

Changing component from doctest to scripts.


---

Comment by jhpalmieri created at 2011-10-17 16:53:52

A few quick comments:

 - you have a typo in line 93, "eyactly"
 - on line 583, `# optional - qepcad, note "algeraic" [sic]`, this is not the way to format an optional doctest: it will only run if you do "sage -t -optional-only=qepcad,not,algeraic,sic" or something like that.
 - same on line 1220

For the scripts patch:

 - why not apply os.path.abspath to SAGE_ROOT?


---

Comment by jdemeyer created at 2011-10-17 18:47:14

Replying to [comment:14 jhpalmieri]:
> A few quick comments:
> 
>  - you have a typo in line 93, "eyactly"
No idea how that happened...

>  - on line 583, `# optional - qepcad, note "algeraic" [sic]`, this is not the way to format an optional doctest: it will only run if you do "sage -t -optional-only=qepcad,not,algeraic,sic" or something like that.
Very true, thanks!

> For the scripts patch:
> 
>  - why not apply os.path.abspath to SAGE_ROOT?
Because `SAGE_ROOT` is already canonicalized by `realpath` at the top of that file:

```
SAGE_ROOT     = os.path.realpath(os.environ['SAGE_ROOT'])
```



---

Comment by jdemeyer created at 2011-10-17 18:55:49

Moved the "clean up" part of the qepcad patch to #11933.


---

Comment by jhpalmieri created at 2011-10-17 21:01:31

For the scripts patch: should there be any error checking when writing to files?  If a sysadmin installs Sage, runs it once (to generate the appropriate files) and then moves it but doesn't run it again, it would be nice if other users got helpful error messages.  One issue is the code

```
    check_processor_flags()
    # Note: install_moved() may also run e.g. initialize_pkgconfig_files().
    if install_moved():
        print "The Sage installation tree may have moved"
        print "(from %s to %s)." % (OLD_SAGE_ROOT, SAGE_ROOT)
```

The problem is that `check_processor_flags` and `install_moved` already try to write to files, so if permissions are bad, the message about the installation tree may not get printed.  I'm attaching a patch to apply on top of yours (basically wraps everything in a try...except block).

Also, as discussed at #11760, the alternate implementation (commented out) of searching for SAGE_ROOT using regular expressions was slower than the one currently used, so I just deleted the comments altogether.

I'll keep looking at your patch.


---

Comment by jdemeyer created at 2011-10-18 10:26:28

John, you are assuming a failure means that there was a problem was permissions.  We should probably catch `IOError` (and also `OSError` perhaps?) and print the message which came with the exception.


---

Comment by jhpalmieri created at 2011-10-19 02:36:19

Replying to [comment:20 jdemeyer]:
> John, you are assuming a failure means that there was a problem was permissions.  We should probably catch `IOError` (and also `OSError` perhaps?) and print the message which came with the exception.

I think that a permissions problem is the most likely issue.  I've modified the patch a bit: if it looks like bad permissions, print a friendly error message.  If it's an `IOError` unrelated to permissions, explicitly raise the error.  If it's some other kind of error, don't catch it at all, so it should get raised, too.  You can test this by changing my patch: change the line

```
if e.strerror.find('Permission denied') != -1:
```

by changing `!=` to `==`, or on the previous line, change `IOError` to `ValueError` or something else irrelevant.  Move sage and make the directory unwriteable; then when you run sage, you should see the raw error message.


---

Comment by jdemeyer created at 2011-10-19 07:08:00

John, your patch looks good on first glance.


---

Comment by jdemeyer created at 2011-10-19 21:09:26

#11920 (sympow) needs review.


---

Comment by jdemeyer created at 2011-10-30 20:30:56

I plan to come back to this once the dependencies are settled.  Otherwise I would just be rebasing pointlessly.


---

Comment by jdemeyer created at 2011-11-03 16:14:43

Milestone sage-4.7.3 deleted


---

Comment by jdemeyer created at 2012-09-14 12:24:23

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2012-09-14 12:24:23

This seems to be fixed with these patches, so I'm putting it to _needs_review_.

However, this depends on so many other tickets, so it might be good to postpone the review and wait for the other tickets.


---

Attachment


---

Comment by jdemeyer created at 2012-12-19 15:15:52

The Fortran patch needed to be rebased because of #13579. Apart from that, things look fine.


---

Comment by jdemeyer created at 2012-12-19 20:47:22

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2012-12-19 20:47:22

Some doctest failures...


---

Comment by jdemeyer created at 2012-12-19 21:01:28

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by fbissey created at 2012-12-30 10:21:26

SAGE_LOCAL is a strange location for default.qepcadrc I suppose it really needs to be changed in the spkg first but SAGE_LOCAL/etc is a better location for this kind of file.


---

Comment by fbissey created at 2013-01-12 09:39:04

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2013-01-12 09:39:04

My only objection is the location of default.qepcadrc but since it is for an experimental spkg and would require another ticket to change it I am giving this a positive review. Moving the default.qepcadrc location should be the object of a follow up ticket.


---

Comment by jdemeyer created at 2013-01-12 13:40:39

Replying to [comment:44 fbissey]:
> My only objection is the location of default.qepcadrc
Also, you shouldn't blame this ticket for that, it has always been like that.

Thanks for the review!


---

Comment by jdemeyer created at 2013-01-21 21:06:24

Resolution: fixed


---

Comment by jdemeyer created at 2013-01-22 19:41:33

I made a patch for the analogous problem for `$HOME` at #13985.  It would be nice if somebody could review that.
