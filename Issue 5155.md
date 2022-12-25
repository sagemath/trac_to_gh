# Issue 5155: Sage 3.3.a3: fix doctests that want write access to $SAGE_LOCAL

archive/issues_005155.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @lftabera @nexttime\n\nAll doctests in Sage should pass when they are run as a user that does not own the Sage tree. To do that set SAGE_TESTDIR to some place writable, i.e.\n\n```\nexport SAGE_TESTDIR=/scratch/mabshoff/tmp\n```\nand run the doctests on a Sage install that isn't owned by the user. When doing so the following doctests fail:\n\n```\n\tsage -t -long devel/sage/sage/matrix/matrix2.pyx # 1 doctests failed\n\tsage -t -long devel/doc/tut/tut.tex # 5 doctests failed\n\tsage -t -long devel/sage/sage/interfaces/qepcad.py # 2 doctests failed\n\tsage -t -long devel/sage/sage/plot/plot.py # 6 doctests failed\n\tsage -t -long devel/sage/sage/databases/database.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/calculus/calculus.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/misc/package.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/gsl/ode.pyx # 4 doctests failed\n\tsage -t -long devel/sage/sage/server/support.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/server/notebook/notebook.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/server/notebook/twist.py # 8 doctests failed\n\tsage -t -long devel/sage/sage/structure/sage_object.pyx # 6 doctests failed\n```\nThis ticket might need to be split up since it covers a rather large number of doctest failures.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5155\n\n",
    "created_at": "2009-02-02T01:25:42Z",
    "labels": [
        "component: doctest",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.7",
    "title": "Sage 3.3.a3: fix doctests that want write access to $SAGE_LOCAL",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @lftabera @nexttime

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

Issue created by migration from https://trac.sagemath.org/ticket/5155





---

archive/issue_comments_039380.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T07:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39380",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039381.json:
```json
{
    "body": "Before applying the patch, I get two doctest failures (with a non-writeable Sage install).  Applying the patch \"trac_5155.patch\" fixes both.  So positive review for that.\n\nThe scripts patch wasn't necessary to get those tests to pass, and it also doesn't apply cleanly to 4.3.1:\n\n```\napplying /Users/palmieri/Downloads/scripts_5155.patch\npatching file sage-doctest\nHunk #1 FAILED at 55\n1 out of 1 hunks FAILED -- saving rejects to file sage-doctest.rej\nunable to find 'sage-dsage-trial' for patching\n1 out of 1 hunks FAILED -- saving rejects to file sage-dsage-trial.rej\npatching file sage-maketest\nHunk #1 succeeded at 1 with fuzz 1 (offset -1 lines).\npatching file sage-test\nHunk #1 FAILED at 40\n1 out of 1 hunks FAILED -- saving rejects to file sage-test.rej\nsage-dsage-trial: No such file or directory\nabort: patch failed to apply\n```\nThe changes there look fine in principle, though.  So once it's rebased, positive review there, too.",
    "created_at": "2010-01-21T21:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39381",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_039382.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-21T21:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39382",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_039383.json:
```json
{
    "body": "Some of the doctest are ok nowadays but there are other new fails. See for example #9965\n\nI can confirm that, with sage 4.5.3 I get the following doctest failures:\n\n        sage -t  -long \"devel/sage/doc/common/builder.py\"\n        sage -t  -long \"devel/sage/sage/interfaces/qepcad.py\"\n        sage -t  -long \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n        sage -t  -long \"devel/sage/sage/modular/hecke/submodule.py\"\n        sage -t  -long \"devel/sage/sage/modular/abvar/abvar.py\"\n        sage -t  -long \"devel/sage/sage/lfunctions/sympow.py\"\n\nAll except quecad are trying to be solved in #9965",
    "created_at": "2010-09-23T11:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39383",
    "user": "https://github.com/lftabera"
}
```

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

archive/issue_comments_039384.json:
```json
{
    "body": "qepcad failures\n\n```\nsage -t -long \"devel/sage/sage/interfaces/qepcad.py\"        \n**********************************************************************\nFile \"/opt/SAGE/sage/devel/sage/sage/interfaces/qepcad.py\", line 638:\n    sage: _rewrite_qepcadrc()\nException raised:\n    Traceback (most recent call last):\n      File \"/opt/SAGE/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/opt/SAGE/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/opt/SAGE/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[3]>\", line 1, in <module>\n        _rewrite_qepcadrc()###line 638:\n    sage: _rewrite_qepcadrc()\n      File \"/opt/SAGE/sage/local/lib/python/site-packages/sage/interfaces/qepcad.py\", line 660, in _rewrite_qepcadrc\n        open(fn, 'w').write(text)\n    IOError: [Errno 13] Permission denied: '/opt/SAGE/sage/local//default.qepcadrc'\n**********************************************************************\nFile \"/opt/SAGE/sage/devel/sage/sage/interfaces/qepcad.py\", line 689:\n    sage: Qepcad_expect(memcells=100000, logfile=sys.stdout)\nException raised:\n    Traceback (most recent call last):\n      File \"/opt/SAGE/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/opt/SAGE/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/opt/SAGE/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[3]>\", line 1, in <module>\n        Qepcad_expect(memcells=Integer(100000), logfile=sys.stdout)###line 689:\n    sage: Qepcad_expect(memcells=100000, logfile=sys.stdout)\n      File \"/opt/SAGE/sage/local/lib/python/site-packages/sage/interfaces/qepcad.py\", line 692, in __init__\n        _rewrite_qepcadrc()\n      File \"/opt/SAGE/sage/local/lib/python/site-packages/sage/interfaces/qepcad.py\", line 660, in _rewrite_qepcadrc\n        open(fn, 'w').write(text)\n    IOError: [Errno 13] Permission denied: '/opt/SAGE/sage/local//default.qepcadrc'\n**********************************************************************\n2 items had failures:\n   1 of   6 in __main__.example_3\n   1 of   4 in __main__.example_6\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/usuario/.sage//tmp/.doctest_qepcad.py\n         [1.9 s]\n```",
    "created_at": "2010-09-23T11:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39384",
    "user": "https://github.com/lftabera"
}
```

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

archive/issue_comments_039385.json:
```json
{
    "body": "Another issue, if you compile sage but the very first access of sage is made by a user without write permissions, you get the following error:\n\n---\n| Sage Version 4.5.3, Release Date: 2010-09-04                       |\n| Type notebook() for the GUI, and license() for information.        |\n---\nTraceback (most recent call last):\n  File \"/opt/SAGE/sage-4.5.3/local/bin/sage-location\", line 174, in <module>\n    t, R = install_moved()\n  File \"/opt/SAGE/sage-4.5.3/local/bin/sage-location\", line 18, in install_moved\n    write_flags_file()\n  File \"/opt/SAGE/sage-4.5.3/local/bin/sage-location\", line 82, in write_flags_file\n    open(flags_file,'w').write(get_flags_info())\nIOError: [Errno 13] Permission denied: '/opt/SAGE/sage-4.5.3/local/lib/sage-flags.txt'",
    "created_at": "2010-09-23T14:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39385",
    "user": "https://github.com/lftabera"
}
```

Another issue, if you compile sage but the very first access of sage is made by a user without write permissions, you get the following error:

---
| Sage Version 4.5.3, Release Date: 2010-09-04                       |
| Type notebook() for the GUI, and license() for information.        |
---
Traceback (most recent call last):
  File "/opt/SAGE/sage-4.5.3/local/bin/sage-location", line 174, in <module>
    t, R = install_moved()
  File "/opt/SAGE/sage-4.5.3/local/bin/sage-location", line 18, in install_moved
    write_flags_file()
  File "/opt/SAGE/sage-4.5.3/local/bin/sage-location", line 82, in write_flags_file
    open(flags_file,'w').write(get_flags_info())
IOError: [Errno 13] Permission denied: '/opt/SAGE/sage-4.5.3/local/lib/sage-flags.txt'



---

archive/issue_comments_039386.json:
```json
{
    "body": "With Sage 4.7.2.alpha2, I see problems with qepcad and sympow.  I think the qepcad problem should be easy to solve, basically as mhansen did before:\n\n```diff\ndiff --git a/sage/interfaces/qepcad.py b/sage/interfaces/qepcad.py\n--- a/sage/interfaces/qepcad.py\n+++ b/sage/interfaces/qepcad.py\n@@ -636,14 +636,14 @@ def _rewrite_qepcadrc():\n     EXAMPLES:\n         sage: from sage.interfaces.qepcad import _rewrite_qepcadrc\n         sage: _rewrite_qepcadrc()\n-        sage: from sage.misc.misc import SAGE_LOCAL\n-        sage: open('%s/default.qepcadrc'%SAGE_LOCAL).readlines()[-1]\n+        sage: from sage.misc.misc import DOT_SAGE\n+        sage: open('%s/default.qepcadrc'%DOT_SAGE).readlines()[-1]\n         'SINGULAR .../local//bin'\n     \"\"\"\n     global _rewrote_qepcadrc\n     if _rewrote_qepcadrc: return\n \n-    SL = sage.misc.misc.SAGE_LOCAL\n+    SL = sage.misc.misc.DOT_SAGE\n     fn = '%s/default.qepcadrc'%SL\n     text = \\\n \"\"\"# THIS FILE IS AUTOMATICALLY GENERATED -- DO NOT EDIT\n```\nSympow will be harder to deal with, because of how the spkg is written: it tries to write files to SAGE_LOCAL/lib/sympow.  See [http://trac.sagemath.org/sage_trac/ticket/9703#comment:9](http://trac.sagemath.org/sage_trac/ticket/9703#comment:9) for a possible fix.\n\nI'm attaching a patch to try to deal with the situation when you run Sage for the very first time as a user without write permissions.\n\nFinally, there may be other issues if you compile Sage but don't run it, and then run doctests as a user without write permissions (the first time doctests get run, they might write some files which don't need to be written later).  These issues should be fixed, too.",
    "created_at": "2011-09-12T23:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39386",
    "user": "https://github.com/jhpalmieri"
}
```

With Sage 4.7.2.alpha2, I see problems with qepcad and sympow.  I think the qepcad problem should be easy to solve, basically as mhansen did before:

```diff
diff --git a/sage/interfaces/qepcad.py b/sage/interfaces/qepcad.py
--- a/sage/interfaces/qepcad.py
+++ b/sage/interfaces/qepcad.py
@@ -636,14 +636,14 @@ def _rewrite_qepcadrc():
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

archive/issue_comments_039387.json:
```json
{
    "body": "I'm not sure this patch is a good idea or needed, considering #11926.  If the Sage install was moved, it is probably good to bail out with an error if there is no write access.",
    "created_at": "2011-10-17T12:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39387",
    "user": "https://github.com/jdemeyer"
}
```

I'm not sure this patch is a good idea or needed, considering #11926.  If the Sage install was moved, it is probably good to bail out with an error if there is no write access.



---

archive/issue_comments_039388.json:
```json
{
    "body": "Changing assignee from mabshoff to @jdemeyer.",
    "created_at": "2011-10-17T12:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39388",
    "user": "https://github.com/jdemeyer"
}
```

Changing assignee from mabshoff to @jdemeyer.



---

archive/issue_comments_039389.json:
```json
{
    "body": "Changing component from doctest to scripts.",
    "created_at": "2011-10-17T16:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39389",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from doctest to scripts.



---

archive/issue_comments_039390.json:
```json
{
    "body": "A few quick comments:\n\n- you have a typo in line 93, \"eyactly\"\n- on line 583, `# optional - qepcad, note \"algeraic\" [sic]`, this is not the way to format an optional doctest: it will only run if you do \"sage -t -optional-only=qepcad,not,algeraic,sic\" or something like that.\n- same on line 1220\n\nFor the scripts patch:\n\n- why not apply os.path.abspath to SAGE_ROOT?",
    "created_at": "2011-10-17T16:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39390",
    "user": "https://github.com/jhpalmieri"
}
```

A few quick comments:

- you have a typo in line 93, "eyactly"
- on line 583, `# optional - qepcad, note "algeraic" [sic]`, this is not the way to format an optional doctest: it will only run if you do "sage -t -optional-only=qepcad,not,algeraic,sic" or something like that.
- same on line 1220

For the scripts patch:

- why not apply os.path.abspath to SAGE_ROOT?



---

archive/issue_comments_039391.json:
```json
{
    "body": "Replying to [comment:14 jhpalmieri]:\n> A few quick comments:\n> \n> - you have a typo in line 93, \"eyactly\"\n\nNo idea how that happened...\n\n>  - on line 583, `# optional - qepcad, note \"algeraic\" [sic]`, this is not the way to format an optional doctest: it will only run if you do \"sage -t -optional-only=qepcad,not,algeraic,sic\" or something like that.\n \nVery true, thanks!\n\n> For the scripts patch:\n> \n> - why not apply os.path.abspath to SAGE_ROOT?\n\nBecause `SAGE_ROOT` is already canonicalized by `realpath` at the top of that file:\n\n```\nSAGE_ROOT     = os.path.realpath(os.environ['SAGE_ROOT'])\n```",
    "created_at": "2011-10-17T18:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39391",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:14 jhpalmieri]:
> A few quick comments:
> 
> - you have a typo in line 93, "eyactly"

No idea how that happened...

>  - on line 583, `# optional - qepcad, note "algeraic" [sic]`, this is not the way to format an optional doctest: it will only run if you do "sage -t -optional-only=qepcad,not,algeraic,sic" or something like that.
 
Very true, thanks!

> For the scripts patch:
> 
> - why not apply os.path.abspath to SAGE_ROOT?

Because `SAGE_ROOT` is already canonicalized by `realpath` at the top of that file:

```
SAGE_ROOT     = os.path.realpath(os.environ['SAGE_ROOT'])
```



---

archive/issue_comments_039392.json:
```json
{
    "body": "Moved the \"clean up\" part of the qepcad patch to #11933.",
    "created_at": "2011-10-17T18:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39392",
    "user": "https://github.com/jdemeyer"
}
```

Moved the "clean up" part of the qepcad patch to #11933.



---

archive/issue_comments_039393.json:
```json
{
    "body": "For the scripts patch: should there be any error checking when writing to files?  If a sysadmin installs Sage, runs it once (to generate the appropriate files) and then moves it but doesn't run it again, it would be nice if other users got helpful error messages.  One issue is the code\n\n```\n    check_processor_flags()\n    # Note: install_moved() may also run e.g. initialize_pkgconfig_files().\n    if install_moved():\n        print \"The Sage installation tree may have moved\"\n        print \"(from %s to %s).\" % (OLD_SAGE_ROOT, SAGE_ROOT)\n```\nThe problem is that `check_processor_flags` and `install_moved` already try to write to files, so if permissions are bad, the message about the installation tree may not get printed.  I'm attaching a patch to apply on top of yours (basically wraps everything in a try...except block).\n\nAlso, as discussed at #11760, the alternate implementation (commented out) of searching for SAGE_ROOT using regular expressions was slower than the one currently used, so I just deleted the comments altogether.\n\nI'll keep looking at your patch.",
    "created_at": "2011-10-17T21:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39393",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_039394.json:
```json
{
    "body": "John, you are assuming a failure means that there was a problem was permissions.  We should probably catch `IOError` (and also `OSError` perhaps?) and print the message which came with the exception.",
    "created_at": "2011-10-18T10:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39394",
    "user": "https://github.com/jdemeyer"
}
```

John, you are assuming a failure means that there was a problem was permissions.  We should probably catch `IOError` (and also `OSError` perhaps?) and print the message which came with the exception.



---

archive/issue_comments_039395.json:
```json
{
    "body": "Replying to [comment:20 jdemeyer]:\n> John, you are assuming a failure means that there was a problem was permissions.  We should probably catch `IOError` (and also `OSError` perhaps?) and print the message which came with the exception.\n\n\nI think that a permissions problem is the most likely issue.  I've modified the patch a bit: if it looks like bad permissions, print a friendly error message.  If it's an `IOError` unrelated to permissions, explicitly raise the error.  If it's some other kind of error, don't catch it at all, so it should get raised, too.  You can test this by changing my patch: change the line\n\n```\nif e.strerror.find('Permission denied') != -1:\n```\nby changing `!=` to `==`, or on the previous line, change `IOError` to `ValueError` or something else irrelevant.  Move sage and make the directory unwriteable; then when you run sage, you should see the raw error message.",
    "created_at": "2011-10-19T02:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39395",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:20 jdemeyer]:
> John, you are assuming a failure means that there was a problem was permissions.  We should probably catch `IOError` (and also `OSError` perhaps?) and print the message which came with the exception.


I think that a permissions problem is the most likely issue.  I've modified the patch a bit: if it looks like bad permissions, print a friendly error message.  If it's an `IOError` unrelated to permissions, explicitly raise the error.  If it's some other kind of error, don't catch it at all, so it should get raised, too.  You can test this by changing my patch: change the line

```
if e.strerror.find('Permission denied') != -1:
```
by changing `!=` to `==`, or on the previous line, change `IOError` to `ValueError` or something else irrelevant.  Move sage and make the directory unwriteable; then when you run sage, you should see the raw error message.



---

archive/issue_comments_039396.json:
```json
{
    "body": "John, your patch looks good on first glance.",
    "created_at": "2011-10-19T07:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39396",
    "user": "https://github.com/jdemeyer"
}
```

John, your patch looks good on first glance.



---

archive/issue_comments_039397.json:
```json
{
    "body": "#11920 (sympow) needs review.",
    "created_at": "2011-10-19T21:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39397",
    "user": "https://github.com/jdemeyer"
}
```

#11920 (sympow) needs review.



---

archive/issue_comments_039398.json:
```json
{
    "body": "I plan to come back to this once the dependencies are settled.  Otherwise I would just be rebasing pointlessly.",
    "created_at": "2011-10-30T20:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39398",
    "user": "https://github.com/jdemeyer"
}
```

I plan to come back to this once the dependencies are settled.  Otherwise I would just be rebasing pointlessly.



---

archive/issue_comments_039399.json:
```json
{
    "body": "Milestone sage-4.7.3 deleted",
    "created_at": "2011-11-03T16:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39399",
    "user": "https://github.com/jdemeyer"
}
```

Milestone sage-4.7.3 deleted



---

archive/issue_events_011940.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-06T21:32:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "milestone": "sage-4.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5155#event-11940"
}
```



---

archive/issue_comments_039400.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-09-14T12:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39400",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_039401.json:
```json
{
    "body": "This seems to be fixed with these patches, so I'm putting it to *needs_review*.\n\nHowever, this depends on so many other tickets, so it might be good to postpone the review and wait for the other tickets.",
    "created_at": "2012-09-14T12:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39401",
    "user": "https://github.com/jdemeyer"
}
```

This seems to be fixed with these patches, so I'm putting it to *needs_review*.

However, this depends on so many other tickets, so it might be good to postpone the review and wait for the other tickets.



---

archive/issue_comments_039402.json:
```json
{
    "body": "Attachment [5155_sage_location.patch](tarball://root/attachments/some-uuid/ticket5155/5155_sage_location.patch) by @jdemeyer created at 2012-09-16 18:44:12",
    "created_at": "2012-09-16T18:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39402",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [5155_sage_location.patch](tarball://root/attachments/some-uuid/ticket5155/5155_sage_location.patch) by @jdemeyer created at 2012-09-16 18:44:12



---

archive/issue_comments_039403.json:
```json
{
    "body": "The Fortran patch needed to be rebased because of #13579. Apart from that, things look fine.",
    "created_at": "2012-12-19T15:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39403",
    "user": "https://github.com/jdemeyer"
}
```

The Fortran patch needed to be rebased because of #13579. Apart from that, things look fine.



---

archive/issue_comments_039404.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-12-19T20:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39404",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_039405.json:
```json
{
    "body": "Some doctest failures...",
    "created_at": "2012-12-19T20:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39405",
    "user": "https://github.com/jdemeyer"
}
```

Some doctest failures...



---

archive/issue_comments_039406.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-12-19T21:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39406",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_039407.json:
```json
{
    "body": "Attachment [5155_sagelib.patch](tarball://root/attachments/some-uuid/ticket5155/5155_sagelib.patch) by @jdemeyer created at 2012-12-19 21:01:28",
    "created_at": "2012-12-19T21:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39407",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [5155_sagelib.patch](tarball://root/attachments/some-uuid/ticket5155/5155_sagelib.patch) by @jdemeyer created at 2012-12-19 21:01:28



---

archive/issue_comments_039408.json:
```json
{
    "body": "SAGE_LOCAL is a strange location for default.qepcadrc I suppose it really needs to be changed in the spkg first but SAGE_LOCAL/etc is a better location for this kind of file.",
    "created_at": "2012-12-30T10:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39408",
    "user": "https://github.com/kiwifb"
}
```

SAGE_LOCAL is a strange location for default.qepcadrc I suppose it really needs to be changed in the spkg first but SAGE_LOCAL/etc is a better location for this kind of file.



---

archive/issue_comments_039409.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-12T09:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39409",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039410.json:
```json
{
    "body": "My only objection is the location of default.qepcadrc but since it is for an experimental spkg and would require another ticket to change it I am giving this a positive review. Moving the default.qepcadrc location should be the object of a follow up ticket.",
    "created_at": "2013-01-12T09:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39410",
    "user": "https://github.com/kiwifb"
}
```

My only objection is the location of default.qepcadrc but since it is for an experimental spkg and would require another ticket to change it I am giving this a positive review. Moving the default.qepcadrc location should be the object of a follow up ticket.



---

archive/issue_comments_039411.json:
```json
{
    "body": "Replying to [comment:44 fbissey]:\n> My only objection is the location of default.qepcadrc\n\nAlso, you shouldn't blame this ticket for that, it has always been like that.\n\nThanks for the review!",
    "created_at": "2013-01-12T13:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39411",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:44 fbissey]:
> My only objection is the location of default.qepcadrc

Also, you shouldn't blame this ticket for that, it has always been like that.

Thanks for the review!



---

archive/issue_events_011941.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-12T13:40:39Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "milestone": "sage-4.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5155#event-11941"
}
```



---

archive/issue_events_011942.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-12T13:40:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "milestone": "sage-5.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5155#event-11942"
}
```



---

archive/issue_events_011943.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-21T21:06:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5155#event-11943"
}
```



---

archive/issue_comments_039412.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-01-21T21:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39412",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_039413.json:
```json
{
    "body": "I made a patch for the analogous problem for `$HOME` at #13985.  It would be nice if somebody could review that.",
    "created_at": "2013-01-22T19:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5155#issuecomment-39413",
    "user": "https://github.com/jdemeyer"
}
```

I made a patch for the analogous problem for `$HOME` at #13985.  It would be nice if somebody could review that.
