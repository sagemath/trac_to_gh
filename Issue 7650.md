# Issue 7650: Fix sagenb doctesting

archive/issues_007650.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein @TimDumol @mwhansen @jasongrout\n\n`sage -t sagenb/` yields several\n\n```\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7650\n\n",
    "created_at": "2009-12-10T03:12:15Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Fix sagenb doctesting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7650",
    "user": "@qed777"
}
```
Assignee: @williamstein

CC:  @williamstein @TimDumol @mwhansen @jasongrout

`sage -t sagenb/` yields several

```
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
```


Issue created by migration from https://trac.sagemath.org/ticket/7650





---

archive/issue_comments_065390.json:
```json
{
    "body": "Part of the problem is that notebook directories now need to end in `.sagenb`.\n\nI'm working on a patch for this and whatever other problems I can fix.",
    "created_at": "2009-12-10T03:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65390",
    "user": "@qed777"
}
```

Part of the problem is that notebook directories now need to end in `.sagenb`.

I'm working on a patch for this and whatever other problems I can fix.



---

archive/issue_comments_065391.json:
```json
{
    "body": "\n```python\nsage -t -verbose \"notebook.py\"                              \nTraceback (most recent call last):\n  File \"/home/.sage//tmp/.doctest_notebook.py\", line 18, in <module>\n    from notebook import *\n  File \"/home/.sage/tmp/notebook.py\", line 38, in <module>\n    import css          # style\nImportError: No module named css\n         [2.5 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -verbose \"notebook.py\"\nTotal time for all tests: 2.5 seconds\n```\n\n\nAdding\n\n```python\nimport sys\nsys.path.append('/home/sage/notebook/sagenb/sagenb')\nsys.path.append('/home/sage/notebook/sagenb/sagenb/notebook')\n```\n\nto the top of `notebook.py` allows testing to proceed.  I'm not sure about a real solution.",
    "created_at": "2009-12-10T03:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65391",
    "user": "@qed777"
}
```


```python
sage -t -verbose "notebook.py"                              
Traceback (most recent call last):
  File "/home/.sage//tmp/.doctest_notebook.py", line 18, in <module>
    from notebook import *
  File "/home/.sage/tmp/notebook.py", line 38, in <module>
    import css          # style
ImportError: No module named css
         [2.5 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -verbose "notebook.py"
Total time for all tests: 2.5 seconds
```


Adding

```python
import sys
sys.path.append('/home/sage/notebook/sagenb/sagenb')
sys.path.append('/home/sage/notebook/sagenb/sagenb/notebook')
```

to the top of `notebook.py` allows testing to proceed.  I'm not sure about a real solution.



---

archive/issue_comments_065392.json:
```json
{
    "body": "Attachment [trac_7650-sagenb_doctesting.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting.patch) by @qed777 created at 2009-12-10 11:39:48\n\nAdd `--force_lib` option to `sage-doctest`.  Use `os.path.join`.  **scripts** repo.",
    "created_at": "2009-12-10T11:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65392",
    "user": "@qed777"
}
```

Attachment [trac_7650-sagenb_doctesting.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting.patch) by @qed777 created at 2009-12-10 11:39:48

Add `--force_lib` option to `sage-doctest`.  Use `os.path.join`.  **scripts** repo.



---

archive/issue_comments_065393.json:
```json
{
    "body": "Fix sagenb doctests.  **sagenb** repo.",
    "created_at": "2009-12-10T11:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65393",
    "user": "@qed777"
}
```

Fix sagenb doctests.  **sagenb** repo.



---

archive/issue_comments_065394.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-12-10T11:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65394",
    "user": "@qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_065395.json:
```json
{
    "body": "Attachment [trac_7650-scripts_doctest_force_lib.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-scripts_doctest_force_lib.patch) by @qed777 created at 2009-12-10 11:57:53\n\n**Please note: The attachments (or their descriptions) are switched.**  I apologize for this.\n\nAnyway, with the scripts repository patch, we can do, e.g.,\n\n```sh\n$ sage -t --force_lib sagenb/\n```\n\nWith the sagenb repository patch applied to #7625 + #7483 + #7482 + #7514 + #7648, all tests but 3 pass.  The failures are in `sagenb/misc/sageinspect.py` (cf. #7514).  The Selenium tests still pass.\n\nRemarks:\n\n* I hope I did not create false-negatives.\n* [This sage-notebook thread](http://groups.google.com/group/sage-notebook/browse_thread/thread/9dd524690bb1588b/38855ecc2819205a?#38855ecc2819205a) *might* be relevant to some tests that evaluate cells.\n* I \"untabified\" `cell.py`, `worksheet.py`, `notebook.py`, and `twist.py`.\n* I added `'nodoctest'` to `simple/twist.py`, since at least one test appears to hang indefinitely.  I don't know why.\n* Feel free to lower the priority.",
    "created_at": "2009-12-10T11:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65395",
    "user": "@qed777"
}
```

Attachment [trac_7650-scripts_doctest_force_lib.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-scripts_doctest_force_lib.patch) by @qed777 created at 2009-12-10 11:57:53

**Please note: The attachments (or their descriptions) are switched.**  I apologize for this.

Anyway, with the scripts repository patch, we can do, e.g.,

```sh
$ sage -t --force_lib sagenb/
```

With the sagenb repository patch applied to #7625 + #7483 + #7482 + #7514 + #7648, all tests but 3 pass.  The failures are in `sagenb/misc/sageinspect.py` (cf. #7514).  The Selenium tests still pass.

Remarks:

* I hope I did not create false-negatives.
* [This sage-notebook thread](http://groups.google.com/group/sage-notebook/browse_thread/thread/9dd524690bb1588b/38855ecc2819205a?#38855ecc2819205a) *might* be relevant to some tests that evaluate cells.
* I "untabified" `cell.py`, `worksheet.py`, `notebook.py`, and `twist.py`.
* I added `'nodoctest'` to `simple/twist.py`, since at least one test appears to hang indefinitely.  I don't know why.
* Feel free to lower the priority.



---

archive/issue_comments_065396.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-10T11:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65396",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065397.json:
```json
{
    "body": "Should we add, e.g., \n\n```sh\nsage -t --force_lib $SAGE_ROOT/local/lib/python/site-packages/sagenb\n```\n\nto `$SAGE_ROOT/makefile`?  Or `sage-test`?",
    "created_at": "2009-12-10T12:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65397",
    "user": "@qed777"
}
```

Should we add, e.g., 

```sh
sage -t --force_lib $SAGE_ROOT/local/lib/python/site-packages/sagenb
```

to `$SAGE_ROOT/makefile`?  Or `sage-test`?



---

archive/issue_comments_065398.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-10T18:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65398",
    "user": "@williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065399.json:
```json
{
    "body": "I like this patch a lot.  However, a nitpick: get rid of the / before tmp here:\n\n```\nSAGE_TESTDIR = os.path.join(DOT_SAGE, \"/tmp\") \n```\n\nLikewise, elsewhere in the patch there are a bunch of os.path.joins combined with explicit* slashes.  \n\nRegarding adding sage -t sagenb, etc., to sage-test or whatever: \"yes!\"",
    "created_at": "2009-12-10T18:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65399",
    "user": "@williamstein"
}
```

I like this patch a lot.  However, a nitpick: get rid of the / before tmp here:

```
SAGE_TESTDIR = os.path.join(DOT_SAGE, "/tmp") 
```

Likewise, elsewhere in the patch there are a bunch of os.path.joins combined with explicit* slashes.  

Regarding adding sage -t sagenb, etc., to sage-test or whatever: "yes!"



---

archive/issue_comments_065400.json:
```json
{
    "body": "Updated scripts repo patch.  Replaces previous.",
    "created_at": "2009-12-11T14:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65400",
    "user": "@qed777"
}
```

Updated scripts repo patch.  Replaces previous.



---

archive/issue_comments_065401.json:
```json
{
    "body": "Attachment [trac_7650-sagenb_doctesting_v2.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting_v2.patch) by @qed777 created at 2009-12-13 14:18:53\n\nQuit spawned worksheet processes.  Replaces previous sagenb repo patch.",
    "created_at": "2009-12-13T14:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65401",
    "user": "@qed777"
}
```

Attachment [trac_7650-sagenb_doctesting_v2.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting_v2.patch) by @qed777 created at 2009-12-13 14:18:53

Quit spawned worksheet processes.  Replaces previous sagenb repo patch.



---

archive/issue_comments_065402.json:
```json
{
    "body": "Auto-detect `site-packages`.  scripts repo.  Replaces previous.",
    "created_at": "2009-12-14T03:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65402",
    "user": "@qed777"
}
```

Auto-detect `site-packages`.  scripts repo.  Replaces previous.



---

archive/issue_comments_065403.json:
```json
{
    "body": "Attachment [trac_7650-scripts_doctest_force_lib_v3.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-scripts_doctest_force_lib_v3.patch) by @qed777 created at 2009-12-14 06:06:45\n\nAdds `-sagenb` option.  scripts repo.  Replaces previous.",
    "created_at": "2009-12-14T06:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65403",
    "user": "@qed777"
}
```

Attachment [trac_7650-scripts_doctest_force_lib_v3.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-scripts_doctest_force_lib_v3.patch) by @qed777 created at 2009-12-14 06:06:45

Adds `-sagenb` option.  scripts repo.  Replaces previous.



---

archive/issue_comments_065404.json:
```json
{
    "body": "Attachment [trac_7650-scripts_doctest_force_lib_v4.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-scripts_doctest_force_lib_v4.patch) by @qed777 created at 2009-12-14 06:09:51\n\nUpdated `SAGE_ROOT/makefile`.",
    "created_at": "2009-12-14T06:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65404",
    "user": "@qed777"
}
```

Attachment [trac_7650-scripts_doctest_force_lib_v4.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-scripts_doctest_force_lib_v4.patch) by @qed777 created at 2009-12-14 06:09:51

Updated `SAGE_ROOT/makefile`.



---

archive/issue_comments_065405.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-14T06:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65405",
    "user": "@qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065406.json:
```json
{
    "body": "Attachment [makefile](tarball://root/attachments/some-uuid/ticket7650/makefile) by @qed777 created at 2009-12-14 06:18:29\n\nWith [attachment:trac_7650-scripts_doctest_force_lib_v4.patch] and an updated top-level [attachment: makefile], we can do\n\n* `make test`\n* `make ptest`\n* `sage -t -sagenb`\n* `sage -tp -sagenb`\n\netc.  Maybe we should unify the test scripts and use [optparse](http://docs.python.org/library/optparse.html)?",
    "created_at": "2009-12-14T06:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65406",
    "user": "@qed777"
}
```

Attachment [makefile](tarball://root/attachments/some-uuid/ticket7650/makefile) by @qed777 created at 2009-12-14 06:18:29

With [attachment:trac_7650-scripts_doctest_force_lib_v4.patch] and an updated top-level [attachment: makefile], we can do

* `make test`
* `make ptest`
* `sage -t -sagenb`
* `sage -tp -sagenb`

etc.  Maybe we should unify the test scripts and use [optparse](http://docs.python.org/library/optparse.html)?



---

archive/issue_comments_065407.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-21T03:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65407",
    "user": "@TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065408.json:
```json
{
    "body": "The new options to `sage -t` (-force_lib and -sagenb) are not documented in the help message. Please do so.",
    "created_at": "2009-12-21T03:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65408",
    "user": "@TimDumol"
}
```

The new options to `sage -t` (-force_lib and -sagenb) are not documented in the help message. Please do so.



---

archive/issue_comments_065409.json:
```json
{
    "body": "I'm declaring a total feature freeze on sage-4.3.",
    "created_at": "2009-12-24T07:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65409",
    "user": "@williamstein"
}
```

I'm declaring a total feature freeze on sage-4.3.



---

archive/issue_comments_065410.json:
```json
{
    "body": "Also: Be more agressive with `os.path.join`-ery.",
    "created_at": "2009-12-24T18:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65410",
    "user": "@qed777"
}
```

Also: Be more agressive with `os.path.join`-ery.



---

archive/issue_comments_065411.json:
```json
{
    "body": "Attachment [trac_7650-scripts_doctest_force_lib_v5.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-scripts_doctest_force_lib_v5.patch) by @qed777 created at 2009-12-28 23:10:03\n\nDocument new options.  More `os.path.join`-ery.  Replaces previous.",
    "created_at": "2009-12-28T23:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65411",
    "user": "@qed777"
}
```

Attachment [trac_7650-scripts_doctest_force_lib_v5.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-scripts_doctest_force_lib_v5.patch) by @qed777 created at 2009-12-28 23:10:03

Document new options.  More `os.path.join`-ery.  Replaces previous.



---

archive/issue_comments_065412.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-28T23:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65412",
    "user": "@qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065413.json:
```json
{
    "body": "Rebased vs. #7482's v4.  Replaces previous **sagenb** patch.",
    "created_at": "2010-01-01T10:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65413",
    "user": "@qed777"
}
```

Rebased vs. #7482's v4.  Replaces previous **sagenb** patch.



---

archive/issue_comments_065414.json:
```json
{
    "body": "Attachment [trac_7650-sagenb_doctesting_v3.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting_v3.patch) by @qed777 created at 2010-01-01 10:57:37",
    "created_at": "2010-01-01T10:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65414",
    "user": "@qed777"
}
```

Attachment [trac_7650-sagenb_doctesting_v3.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting_v3.patch) by @qed777 created at 2010-01-01 10:57:37



---

archive/issue_comments_065415.json:
```json
{
    "body": "Rebased vs. 4.3.1.alpha0 + #7269.  Replaces previous sagenb patch.",
    "created_at": "2010-01-05T00:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65415",
    "user": "@qed777"
}
```

Rebased vs. 4.3.1.alpha0 + #7269.  Replaces previous sagenb patch.



---

archive/issue_comments_065416.json:
```json
{
    "body": "Attachment [trac_7650-sagenb_doctesting_v4.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting_v4.patch) by @qed777 created at 2010-01-05 00:49:32",
    "created_at": "2010-01-05T00:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65416",
    "user": "@qed777"
}
```

Attachment [trac_7650-sagenb_doctesting_v4.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting_v4.patch) by @qed777 created at 2010-01-05 00:49:32



---

archive/issue_comments_065417.json:
```json
{
    "body": "I've attached a rebased sagenb patch.  I added `\"\"\"nodoctests\"\"\"` to the top of `sagenb.misc.ipaddr`.  It's also easy to make its doctest pass, but I haven't done this.  Please let me know, if I should.",
    "created_at": "2010-01-05T00:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65417",
    "user": "@qed777"
}
```

I've attached a rebased sagenb patch.  I added `"""nodoctests"""` to the top of `sagenb.misc.ipaddr`.  It's also easy to make its doctest pass, but I haven't done this.  Please let me know, if I should.



---

archive/issue_comments_065418.json:
```json
{
    "body": "Attachment [trac_7650-sagenb_doctesting_v5.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting_v5.patch) by @qed777 created at 2010-01-14 21:58:17\n\nFix tags / user_view asymmetry.  Replaces previous sagenb patch.",
    "created_at": "2010-01-14T21:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65418",
    "user": "@qed777"
}
```

Attachment [trac_7650-sagenb_doctesting_v5.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting_v5.patch) by @qed777 created at 2010-01-14 21:58:17

Fix tags / user_view asymmetry.  Replaces previous sagenb patch.



---

archive/issue_comments_065419.json:
```json
{
    "body": "V5 makes it so a worksheet `reconstruct`ed from the `basic` representation of another has the same `tags` and `user_view` as the original.",
    "created_at": "2010-01-14T22:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65419",
    "user": "@qed777"
}
```

V5 makes it so a worksheet `reconstruct`ed from the `basic` representation of another has the same `tags` and `user_view` as the original.



---

archive/issue_comments_065420.json:
```json
{
    "body": "Fix interact doctests for 4.3.1.alpha2 (colors.py).  Replaces previous sagenb patch.",
    "created_at": "2010-01-15T21:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65420",
    "user": "@qed777"
}
```

Fix interact doctests for 4.3.1.alpha2 (colors.py).  Replaces previous sagenb patch.



---

archive/issue_comments_065421.json:
```json
{
    "body": "Attachment [trac_7650-sagenb_doctesting_v6.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting_v6.patch) by @TimDumol created at 2010-01-16 21:22:05\n\nReplying to [comment:17 mpatel]:\n> V5 makes it so a worksheet `reconstruct`ed from the `basic` representation of another has the same `tags` and `user_view` as the original.\n\nShouldn't this be put in a new ticket?",
    "created_at": "2010-01-16T21:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65421",
    "user": "@TimDumol"
}
```

Attachment [trac_7650-sagenb_doctesting_v6.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-sagenb_doctesting_v6.patch) by @TimDumol created at 2010-01-16 21:22:05

Replying to [comment:17 mpatel]:
> V5 makes it so a worksheet `reconstruct`ed from the `basic` representation of another has the same `tags` and `user_view` as the original.

Shouldn't this be put in a new ticket?



---

archive/issue_comments_065422.json:
```json
{
    "body": "Yes, but it's already here.  :)  In the course of fixing many failed doctests, I noticed it and a few other small problems:\n\n* In `run_notebook.notebook_twisted`: Replaced `nb.directory()` (not defined) with `nb._dir`.\n* In `worksheet`: Replaced `self.__collaborators` (`AttributeError`) with `self.collaborators()` in a few places.\n* In `worksheet.set_filename`:\n\n```diff\n-        self.__dir = os.path.join(self.notebook().worksheet_directory(), filename)\n+        self.__dir = os.path.join(self.notebook()._dir, filename)\n```\n\n* In `worksheet.tags`:\n\n```diff\n             d = dict(self.__user_view)\n         except AttributeError:\n             self.user_view(self.owner())\n-            d = self.__user_view\n+            d = copy.copy(self.__user_view)\n         for user, val in d.iteritems():\n-            d[user] = [val]\n+            if not isinstance(val, list):\n+                d[user] = [val]\n         return d\n```\n\n This ensures the tests in `Worksheet.reconstruct_from_basic` pass and that calling `tags` does not alter the current user view, e.g., turning `1` into `[1]`.\n\nAlso:\n\n* Removed argument `verbose` (obsolete) from `Cell.set_introspect_html`.",
    "created_at": "2010-01-17T14:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65422",
    "user": "@qed777"
}
```

Yes, but it's already here.  :)  In the course of fixing many failed doctests, I noticed it and a few other small problems:

* In `run_notebook.notebook_twisted`: Replaced `nb.directory()` (not defined) with `nb._dir`.
* In `worksheet`: Replaced `self.__collaborators` (`AttributeError`) with `self.collaborators()` in a few places.
* In `worksheet.set_filename`:

```diff
-        self.__dir = os.path.join(self.notebook().worksheet_directory(), filename)
+        self.__dir = os.path.join(self.notebook()._dir, filename)
```

* In `worksheet.tags`:

```diff
             d = dict(self.__user_view)
         except AttributeError:
             self.user_view(self.owner())
-            d = self.__user_view
+            d = copy.copy(self.__user_view)
         for user, val in d.iteritems():
-            d[user] = [val]
+            if not isinstance(val, list):
+                d[user] = [val]
         return d
```

 This ensures the tests in `Worksheet.reconstruct_from_basic` pass and that calling `tags` does not alter the current user view, e.g., turning `1` into `[1]`.

Also:

* Removed argument `verbose` (obsolete) from `Cell.set_introspect_html`.



---

archive/issue_comments_065423.json:
```json
{
    "body": "This bags a positive review from me, except for the few changes I've made in the reviewer patch. Can someone sign them off?",
    "created_at": "2010-01-17T18:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65423",
    "user": "@TimDumol"
}
```

This bags a positive review from me, except for the few changes I've made in the reviewer patch. Can someone sign them off?



---

archive/issue_comments_065424.json:
```json
{
    "body": "A few documentation fixes (precision errors and style), and a couple of changes to try-except blocks to make it easier to transition to Python 3",
    "created_at": "2010-01-17T19:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65424",
    "user": "@TimDumol"
}
```

A few documentation fixes (precision errors and style), and a couple of changes to try-except blocks to make it easier to transition to Python 3



---

archive/issue_comments_065425.json:
```json
{
    "body": "Attachment [trac_7650-reviewer.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-reviewer.patch) by @qed777 created at 2010-01-18 04:10:43\n\nFix two doctest failures.  Replaces reviewer patch.  sagenb repo.",
    "created_at": "2010-01-18T04:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65425",
    "user": "@qed777"
}
```

Attachment [trac_7650-reviewer.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-reviewer.patch) by @qed777 created at 2010-01-18 04:10:43

Fix two doctest failures.  Replaces reviewer patch.  sagenb repo.



---

archive/issue_comments_065426.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T04:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65426",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065427.json:
```json
{
    "body": "Attachment [trac_7650-reviewer_v2.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-reviewer_v2.patch) by @qed777 created at 2010-01-18 04:17:30\n\nV2 of the reviewer patch:\n\n* Adds a missing dot (`.`) in `interact.py`.\n* Moves `# output depends on timezone` to the input statement in `worksheet.py`.\n* [Pre-existing] `most be defined` --> `must be defined`.",
    "created_at": "2010-01-18T04:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65427",
    "user": "@qed777"
}
```

Attachment [trac_7650-reviewer_v2.patch](tarball://root/attachments/some-uuid/ticket7650/trac_7650-reviewer_v2.patch) by @qed777 created at 2010-01-18 04:17:30

V2 of the reviewer patch:

* Adds a missing dot (`.`) in `interact.py`.
* Moves `# output depends on timezone` to the input statement in `worksheet.py`.
* [Pre-existing] `most be defined` --> `must be defined`.



---

archive/issue_comments_065428.json:
```json
{
    "body": "I applied the scripts patch and replaced makefile in SAGE_ROOT. Please post a `sagenb-0.5.1.spkg`.",
    "created_at": "2010-01-19T01:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65428",
    "user": "@rlmill"
}
```

I applied the scripts patch and replaced makefile in SAGE_ROOT. Please post a `sagenb-0.5.1.spkg`.



---

archive/issue_comments_065429.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T02:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65429",
    "user": "@rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_065430.json:
```json
{
    "body": "Merged http://boxen.math.washington.edu/home/timdumol/sagenb-0.6.spkg into spkg/standard.",
    "created_at": "2010-01-19T02:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7650#issuecomment-65430",
    "user": "@rlmill"
}
```

Merged http://boxen.math.washington.edu/home/timdumol/sagenb-0.6.spkg into spkg/standard.
