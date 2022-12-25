# Issue 6314: optional doctest failure -- many failures in linear_codes related to wtdist

archive/issues_006314.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long --optional devel/sage/sage/coding/linear_code.py\nsh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found\nsh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found\nsh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py\", line 2188:\n    sage: C.spectrum(method=\"leon\")   # requires optional GAP package Guava\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_44[10]>\", line 1, in <module>\n        C.spectrum(method=\"leon\")   # requires optional GAP package Guava###line 2188:\n    sage: C.spectrum(method=\"leon\")   # requires optional GAP package Guava\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 2236, in spectrum\n        raise RuntimeError(\"Problem calling Leon's wtdist program.\")\n    RuntimeError: Problem calling Leon's wtdist program.\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py\", line 2196:\n    sage: C.spectrum() == C.spectrum(method=\"leon\")   # requires optional GAP package Guava\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_44[14]>\", line 1, in <module>\n        C.spectrum() == C.spectrum(method=\"leon\")   # requires optional GAP package Guava###line 2196:\n    sage: C.spectrum() == C.spectrum(method=\"leon\")   # requires optional GAP package Guava\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 2236, in spectrum\n        raise RuntimeError(\"Problem calling Leon's wtdist program.\")\n    RuntimeError: Problem calling Leon's wtdist program.\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py\", line 2200:\n    sage: C.spectrum() == C.spectrum(method=\"leon\")   # requires optional GAP package Guava\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_44[16]>\", line 1, in <module>\n        C.spectrum() == C.spectrum(method=\"leon\")   # requires optional GAP package Guava###line 2200sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found\n:\n    sage: C.spectrum() == C.spectrum(method=\"leon\")   # requires optional GAP package Guava\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 2236, in spectrum\n        raise RuntimeError(\"Problem calling Leon's wtdist program.\")\n    RuntimeError: Problem calling Leon's wtdist program.\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py\", line 2204:\n    sage: C.spectrum() == C.spectrum(method=\"leon\")   # requires optional GAP package Guava\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_44[18]>\", line 1, in <module>\n        C.spectrum() == C.spectrum(method=\"leon\")   # requires optional GAP package Guava###line 2204:\n    sage: C.spectrum() == C.spectrum(method=\"leon\")   # requires optional GAP package Guava\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 2236, in spectrum\n        raise RuntimeError(\"Problem calling Leon's wtdist program.\")\n    RuntimeError: Problem calling Leon's wtdist program.\n**********************************************************************\n1 items had failures:\n   4 of  19 in __main__.example_44\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_linear_code.py\n\t [22.0 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6314\n\n",
    "created_at": "2009-06-16T14:43:05Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "optional doctest failure -- many failures in linear_codes related to wtdist",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6314",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
sage -t -long --optional devel/sage/sage/coding/linear_code.py
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py", line 2188:
    sage: C.spectrum(method="leon")   # requires optional GAP package Guava
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[10]>", line 1, in <module>
        C.spectrum(method="leon")   # requires optional GAP package Guava###line 2188:
    sage: C.spectrum(method="leon")   # requires optional GAP package Guava
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 2236, in spectrum
        raise RuntimeError("Problem calling Leon's wtdist program.")
    RuntimeError: Problem calling Leon's wtdist program.
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py", line 2196:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[14]>", line 1, in <module>
        C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava###line 2196:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 2236, in spectrum
        raise RuntimeError("Problem calling Leon's wtdist program.")
    RuntimeError: Problem calling Leon's wtdist program.
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py", line 2200:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[16]>", line 1, in <module>
        C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava###line 2200sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found
:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 2236, in spectrum
        raise RuntimeError("Problem calling Leon's wtdist program.")
    RuntimeError: Problem calling Leon's wtdist program.
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py", line 2204:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[18]>", line 1, in <module>
        C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava###line 2204:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 2236, in spectrum
        raise RuntimeError("Problem calling Leon's wtdist program.")
    RuntimeError: Problem calling Leon's wtdist program.
**********************************************************************
1 items had failures:
   4 of  19 in __main__.example_44
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_linear_code.py
	 [22.0 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6314





---

archive/issue_comments_050304.json:
```json
{
    "body": "Attachment [trac_6314.patch](tarball://root/attachments/some-uuid/ticket6314/trac_6314.patch) by @wdjoyner created at 2009-06-16 23:45:11\n\napplies to 4.0.2.rc1",
    "created_at": "2009-06-16T23:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6314#issuecomment-50304",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_6314.patch](tarball://root/attachments/some-uuid/ticket6314/trac_6314.patch) by @wdjoyner created at 2009-06-16 23:45:11

applies to 4.0.2.rc1



---

archive/issue_comments_050305.json:
```json
{
    "body": "Patch applies fine to 4.0.2.rc1 and passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds \nsage -docbuild constructions html (resp., pdf) went fine and sage -t -long --optional devel/sage/sage/coding/linear_code.py passes.",
    "created_at": "2009-06-16T23:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6314#issuecomment-50305",
    "user": "https://github.com/wdjoyner"
}
```

Patch applies fine to 4.0.2.rc1 and passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds 
sage -docbuild constructions html (resp., pdf) went fine and sage -t -long --optional devel/sage/sage/coding/linear_code.py passes.



---

archive/issue_comments_050306.json:
```json
{
    "body": "From an email:\n\n> You should make a ticket for fixing that problem too and put a link to it from 6314. - William\n\nThe guava binaries are now currently being compiled properly due to a problem in the \"newest-version gap\" script (in the gap_packages*.spkg spkg-install script). This is fixed in http://trac.sagemath.org/sage_trac/ticket/6352.",
    "created_at": "2009-06-17T23:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6314#issuecomment-50306",
    "user": "https://github.com/wdjoyner"
}
```

From an email:

> You should make a ticket for fixing that problem too and put a link to it from 6314. - William

The guava binaries are now currently being compiled properly due to a problem in the "newest-version gap" script (in the gap_packages*.spkg spkg-install script). This is fixed in http://trac.sagemath.org/sage_trac/ticket/6352.



---

archive/issue_comments_050307.json:
```json
{
    "body": "This is an easy review- the patch is simple, applies, and tests pass with or without the optional flag.",
    "created_at": "2009-06-21T12:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6314#issuecomment-50307",
    "user": "https://github.com/rlmill"
}
```

This is an easy review- the patch is simple, applies, and tests pass with or without the optional flag.



---

archive/issue_comments_050308.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6314#issuecomment-50308",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
