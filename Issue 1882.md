# Issue 1882: new phcpack spkg

archive/issues_001882.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: phcpack\n\nPhcpack has had many releases since the last spkg.  This brings it up to date as of January 21, 2008, with release 2.3.38.  I have changed the install script to python instead of a shell script, because that's what I know how to do.  I have also tried to add AIX support but I don't have a machine to test it on.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1882\n\n",
    "created_at": "2008-01-21T23:06:32Z",
    "labels": [
        "packages",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "new phcpack spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1882",
    "user": "mhampton"
}
```
Assignee: mabshoff

Keywords: phcpack

Phcpack has had many releases since the last spkg.  This brings it up to date as of January 21, 2008, with release 2.3.38.  I have changed the install script to python instead of a shell script, because that's what I know how to do.  I have also tried to add AIX support but I don't have a machine to test it on.

Issue created by migration from https://trac.sagemath.org/ticket/1882





---

archive/issue_comments_011903.json:
```json
{
    "body": "file is at:\n\nhttp://www.d.umn.edu/~mhampton/phc-2.3.38.spkg\n\n[with experimental spkg]",
    "created_at": "2008-01-21T23:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11903",
    "user": "mhampton"
}
```

file is at:

http://www.d.umn.edu/~mhampton/phc-2.3.38.spkg

[with experimental spkg]



---

archive/issue_comments_011904.json:
```json
{
    "body": "Oops, 2.3.21 is the version that is currently in the repo.",
    "created_at": "2008-01-21T23:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11904",
    "user": "mabshoff"
}
```

Oops, 2.3.21 is the version that is currently in the repo.



---

archive/issue_comments_011905.json:
```json
{
    "body": "Unfortunately it looks like the Mac Intel version is broken, so this should not be included.  I am corresponding with Jan Verschelde (the creator of phcpack) to figure out what is going on.",
    "created_at": "2008-01-22T01:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11905",
    "user": "mhampton"
}
```

Unfortunately it looks like the Mac Intel version is broken, so this should not be included.  I am corresponding with Jan Verschelde (the creator of phcpack) to figure out what is going on.



---

archive/issue_comments_011906.json:
```json
{
    "body": "I have changed the install file so that, as before, intel macs will run the ppc version (through rosetta).  This makes the update much less exciting but it actually works.",
    "created_at": "2008-01-22T13:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11906",
    "user": "mhampton"
}
```

I have changed the install file so that, as before, intel macs will run the ppc version (through rosetta).  This makes the update much less exciting but it actually works.



---

archive/issue_comments_011907.json:
```json
{
    "body": "I have edited the installer slightly, please re-download this for putting in 10.2.3.\n\nI have also added to the phc interface (in sage/interfaces) and fixed a typo of mine that incorrectly described the type of an output.  The new file is:\n[www.d.umn.edu/~mhampton/phc.py]\n\nThis adds a command phc.mixed_volume that quickly computes the mixed volume of a polynomial system.",
    "created_at": "2008-02-24T17:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11907",
    "user": "mhampton"
}
```

I have edited the installer slightly, please re-download this for putting in 10.2.3.

I have also added to the phc interface (in sage/interfaces) and fixed a typo of mine that incorrectly described the type of an output.  The new file is:
[www.d.umn.edu/~mhampton/phc.py]

This adds a command phc.mixed_volume that quickly computes the mixed volume of a polynomial system.



---

archive/issue_comments_011908.json:
```json
{
    "body": "Sorry I should have previewed.  Interface file is at:\n\n[http://www.d.umn.edu/~mhampton/phc.py](http://www.d.umn.edu/~mhampton/phc.py)\n\nand the spkg is at\n\n[http://www.d.umn.edu/~mhampton/phc-2.3.38.spkg](http://www.d.umn.edu/~mhampton/phc-2.3.38.spkg)",
    "created_at": "2008-02-24T17:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11908",
    "user": "mhampton"
}
```

Sorry I should have previewed.  Interface file is at:

[http://www.d.umn.edu/~mhampton/phc.py](http://www.d.umn.edu/~mhampton/phc.py)

and the spkg is at

[http://www.d.umn.edu/~mhampton/phc-2.3.38.spkg](http://www.d.umn.edu/~mhampton/phc-2.3.38.spkg)



---

archive/issue_comments_011909.json:
```json
{
    "body": "I changed the patch so that the Integer type is imported; the previous one had a bug. I am actively using this for a research project so it should get some more stress testing this week.",
    "created_at": "2008-02-26T00:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11909",
    "user": "mhampton"
}
```

I changed the patch so that the Integer type is imported; the previous one had a bug. I am actively using this for a research project so it should get some more stress testing this week.



---

archive/issue_comments_011910.json:
```json
{
    "body": "Fixed a bug that affected larger problems, added optional tag to doctests - I assume that causes them to be skipped usually.",
    "created_at": "2008-02-27T00:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11910",
    "user": "mhampton"
}
```

Fixed a bug that affected larger problems, added optional tag to doctests - I assume that causes them to be skipped usually.



---

archive/issue_comments_011911.json:
```json
{
    "body": "Changing assignee from mabshoff to @williamstein.",
    "created_at": "2008-02-28T18:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11911",
    "user": "mhampton"
}
```

Changing assignee from mabshoff to @williamstein.



---

archive/issue_comments_011912.json:
```json
{
    "body": "Changing component from packages to interfaces.",
    "created_at": "2008-02-28T18:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11912",
    "user": "mhampton"
}
```

Changing component from packages to interfaces.



---

archive/issue_comments_011913.json:
```json
{
    "body": "The spkg installs and appears to work on my 32-bit x86 Debian testing system.  However, the spkg does include some junk OSX files (._spkg-install, .DS_Store, etc.)\n\nThe patch includes a syntax error, which I fixed like this:\n\n```\n--- a/sage/interfaces/phc.py    Tue Feb 26 18:36:37 2008 -0600\n+++ b/sage/interfaces/phc.py    Thu Mar 13 18:34:51 2008 -0700\n@@ -274,7 +274,7 @@ class PHC:\n         child_phc.expect('results')\n         dots = child_phc.read()\n         if verbose:\n-            print \"should be ... :\" dots\n+            print \"should be ... :\", dots\n         child_phc.close()\n         if not os.path.exists(output_filename):\n             raise RuntimeError, \"The output file does not exist; something went wrong running phc.\"\n```\n\n\nAfter applying the patch and installing the spkg, testing phc.py (with -optional) failed with:\n\n```\nsage -t -optional devel/sage-mq/sage/interfaces/phc.py      **********************************************************************\nFile \"phc.py\", line 181:\n    e: v.solutions()                    # optional\nExpected:\n    [[-1.00000000000000*I, 1.00000000000000*I], [1.00000000000000*I, -1.00000000000000*I]]\nGot:\n    [[1.00000000000000*I, -1.00000000000000*I], [-1.00000000000000*I, 1.00000000000000*I]]\n**********************************************************************\nFile \"phc.py\", line 183:\n    e: v.solution_dicts()               # optional\nExpected:\n    [{x: -1.00000000000000*I, y: 1.00000000000000*I}, {x: 1.00000000000000*I, y: -1.00000000000000*I}]\nGot:\n    [{y: 1.00000000000000*I, x: -1.00000000000000*I}, {y: -1.00000000000000*I, x: 1.00000000000000*I}]\n**********************************************************************\n1 items had failures:\n   2 of   9 in __main__.example_5\n***Test Failed*** 2 failures.\n```\n\n\nIt looks like you may need to sort the results.  Also, printing dictionaries often gives different results on 32-bit vs. 64-bit systems (due to the different hash functions used); you may need to have \"# 32-bit\" and \"# 64-bit\" versions of the output.",
    "created_at": "2008-03-14T01:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11913",
    "user": "cwitty"
}
```

The spkg installs and appears to work on my 32-bit x86 Debian testing system.  However, the spkg does include some junk OSX files (._spkg-install, .DS_Store, etc.)

The patch includes a syntax error, which I fixed like this:

```
--- a/sage/interfaces/phc.py    Tue Feb 26 18:36:37 2008 -0600
+++ b/sage/interfaces/phc.py    Thu Mar 13 18:34:51 2008 -0700
@@ -274,7 +274,7 @@ class PHC:
         child_phc.expect('results')
         dots = child_phc.read()
         if verbose:
-            print "should be ... :" dots
+            print "should be ... :", dots
         child_phc.close()
         if not os.path.exists(output_filename):
             raise RuntimeError, "The output file does not exist; something went wrong running phc."
```


After applying the patch and installing the spkg, testing phc.py (with -optional) failed with:

```
sage -t -optional devel/sage-mq/sage/interfaces/phc.py      **********************************************************************
File "phc.py", line 181:
    e: v.solutions()                    # optional
Expected:
    [[-1.00000000000000*I, 1.00000000000000*I], [1.00000000000000*I, -1.00000000000000*I]]
Got:
    [[1.00000000000000*I, -1.00000000000000*I], [-1.00000000000000*I, 1.00000000000000*I]]
**********************************************************************
File "phc.py", line 183:
    e: v.solution_dicts()               # optional
Expected:
    [{x: -1.00000000000000*I, y: 1.00000000000000*I}, {x: 1.00000000000000*I, y: -1.00000000000000*I}]
Got:
    [{y: 1.00000000000000*I, x: -1.00000000000000*I}, {y: -1.00000000000000*I, x: 1.00000000000000*I}]
**********************************************************************
1 items had failures:
   2 of   9 in __main__.example_5
***Test Failed*** 2 failures.
```


It looks like you may need to sort the results.  Also, printing dictionaries often gives different results on 32-bit vs. 64-bit systems (due to the different hash functions used); you may need to have "# 32-bit" and "# 64-bit" versions of the output.



---

archive/issue_comments_011914.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-03-18T18:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11914",
    "user": "mhampton"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_011915.json:
```json
{
    "body": "The file phc.py at http://www.d.umn.edu/~mhampton/phc.py has been changed to address the review comments.  I have updated the spkg to try to remove the superfluous OS X files.",
    "created_at": "2008-03-18T18:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11915",
    "user": "mhampton"
}
```

The file phc.py at http://www.d.umn.edu/~mhampton/phc.py has been changed to address the review comments.  I have updated the spkg to try to remove the superfluous OS X files.



---

archive/issue_comments_011916.json:
```json
{
    "body": "Attachment [trac_1882_phc-interface.patch](tarball://root/attachments/some-uuid/ticket1882/trac_1882_phc-interface.patch) by mhampton created at 2008-03-18 18:24:01",
    "created_at": "2008-03-18T18:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11916",
    "user": "mhampton"
}
```

Attachment [trac_1882_phc-interface.patch](tarball://root/attachments/some-uuid/ticket1882/trac_1882_phc-interface.patch) by mhampton created at 2008-03-18 18:24:01



---

archive/issue_comments_011917.json:
```json
{
    "body": "I just noticed that Jan released another version, so I have updated to that and fixed a bug in my spkg-install script.  The new spkg is at:\n\nhttp://www.d.umn.edu/~mhampton/phc-2.3.39.spkg\n\n[with experimental spkg]",
    "created_at": "2008-03-20T19:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11917",
    "user": "mhampton"
}
```

I just noticed that Jan released another version, so I have updated to that and fixed a bug in my spkg-install script.  The new spkg is at:

http://www.d.umn.edu/~mhampton/phc-2.3.39.spkg

[with experimental spkg]



---

archive/issue_comments_011918.json:
```json
{
    "body": "Attachment [trac_1882_phc-referee.patch](tarball://root/attachments/some-uuid/ticket1882/trac_1882_phc-referee.patch) by cwitty created at 2008-03-29 15:02:35",
    "created_at": "2008-03-29T15:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11918",
    "user": "cwitty"
}
```

Attachment [trac_1882_phc-referee.patch](tarball://root/attachments/some-uuid/ticket1882/trac_1882_phc-referee.patch) by cwitty created at 2008-03-29 15:02:35



---

archive/issue_comments_011919.json:
```json
{
    "body": "I've attached a patch to fix some minor doctest issues.\n\n1) add a missing \"# optional\"\n\n2) improve (IMHO) the solution_dicts() doctest to make it clearer (IMHO) what the method returns, while still letting the doctest be portable\n\n3) copy some doctests from a class docstring to a method docstring, to make \"sage -coverage\" happier\n\nWith this patch and phc-2.3.39, doctests pass in interfaces/phc.py, both with and without -optional.  Positive review.",
    "created_at": "2008-03-29T15:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11919",
    "user": "cwitty"
}
```

I've attached a patch to fix some minor doctest issues.

1) add a missing "# optional"

2) improve (IMHO) the solution_dicts() doctest to make it clearer (IMHO) what the method returns, while still letting the doctest be portable

3) copy some doctests from a class docstring to a method docstring, to make "sage -coverage" happier

With this patch and phc-2.3.39, doctests pass in interfaces/phc.py, both with and without -optional.  Positive review.



---

archive/issue_comments_011920.json:
```json
{
    "body": "I fixed some issues in the spkg. It is now at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/optional/phc-2.3.39.p0.spkg\n\nIn addition I put up the new SPKG.txt at \n\nhttp://wiki.sagemath.org/spkg/phcpack\n\nThe SPKG has been uploaded to the optional repo and mirrored out.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T15:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11920",
    "user": "mabshoff"
}
```

I fixed some issues in the spkg. It is now at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/optional/phc-2.3.39.p0.spkg

In addition I put up the new SPKG.txt at 

http://wiki.sagemath.org/spkg/phcpack

The SPKG has been uploaded to the optional repo and mirrored out.

Cheers,

Michael



---

archive/issue_comments_011921.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T15:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11921",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011922.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T15:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1882#issuecomment-11922",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0
