# Issue 4515: make it so "make check" runs Sage once before running itself, to ensure that sage-location is called, and that sage works

archive/issues_004515.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4515\n\n",
    "created_at": "2008-11-13T22:52:25Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "make it so \"make check\" runs Sage once before running itself, to ensure that sage-location is called, and that sage works",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4515",
    "user": "was"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/4515





---

archive/issue_comments_033511.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-13T23:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33511",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_033512.json:
```json
{
    "body": "Attachment\n\npart 2 -- creates a sage-starts script which is used to verify that sage works.",
    "created_at": "2008-11-13T23:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33512",
    "user": "was"
}
```

Attachment

part 2 -- creates a sage-starts script which is used to verify that sage works.



---

archive/issue_comments_033513.json:
```json
{
    "body": "carefully place this in SAGE_ROOT -- do a diff before doing so.  This is against sage-3.2.rc0",
    "created_at": "2008-11-13T23:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33513",
    "user": "was"
}
```

carefully place this in SAGE_ROOT -- do a diff before doing so.  This is against sage-3.2.rc0



---

archive/issue_comments_033514.json:
```json
{
    "body": "Attachment\n\nThis ticket includes three files.  sage-4515-sage_c_bug.patch fixes a bug in the sage-sage script where `sage -c \"...\"` didn't correctly run the sage_setup function in sage-sage.   The second file sage-4515-sage_starts.patch adds a sage-starts script, that verifies that ones sage actually starts up.  The third file `makefile` replaces the makefile in SAGE_ROOT by a new one that runs sage-starts before running any of the make check targets. \n\nTo test this patch, take any sage install, edit the file SAGE_ROOT/local/lib/sage-current-location.txt and put some random crap in there.  Then do \n\n```\nsage -c \"2+2\"\n```\n\nand see that the current location stuff gets updated.  Corrupt sage-current-location.txgt again, then do\n\n```\nmake check  # or any other target\n```\n\nand verify that the location stuff gets updated.",
    "created_at": "2008-11-13T23:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33514",
    "user": "was"
}
```

Attachment

This ticket includes three files.  sage-4515-sage_c_bug.patch fixes a bug in the sage-sage script where `sage -c "..."` didn't correctly run the sage_setup function in sage-sage.   The second file sage-4515-sage_starts.patch adds a sage-starts script, that verifies that ones sage actually starts up.  The third file `makefile` replaces the makefile in SAGE_ROOT by a new one that runs sage-starts before running any of the make check targets. 

To test this patch, take any sage install, edit the file SAGE_ROOT/local/lib/sage-current-location.txt and put some random crap in there.  Then do 

```
sage -c "2+2"
```

and see that the current location stuff gets updated.  Corrupt sage-current-location.txgt again, then do

```
make check  # or any other target
```

and verify that the location stuff gets updated.



---

archive/issue_comments_033515.json:
```json
{
    "body": "Note: In the list of the options of Sage that is displayed by \"sage --advanced\", the explanation for \"sage -tp ...\" (presumably \"parallel\" testing) is missing.\n\n(I found this out because this patch changes in the makefile some calls \"sage -tp 8 ...\" into \"sage -tp 12 ...\" and was curious what this means --- presumably the number of threads to be started.)",
    "created_at": "2008-11-14T21:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33515",
    "user": "GeorgSWeber"
}
```

Note: In the list of the options of Sage that is displayed by "sage --advanced", the explanation for "sage -tp ..." (presumably "parallel" testing) is missing.

(I found this out because this patch changes in the makefile some calls "sage -tp 8 ..." into "sage -tp 12 ..." and was curious what this means --- presumably the number of threads to be started.)



---

archive/issue_comments_033516.json:
```json
{
    "body": "The \"-tp\" option is undocumented on purpose and will remain so until some issues with termination of run away processes are resolved.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-14T21:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33516",
    "user": "mabshoff"
}
```

The "-tp" option is undocumented on purpose and will remain so until some issues with termination of run away processes are resolved.

Cheers,

Michael



---

archive/issue_comments_033517.json:
```json
{
    "body": "Note: \"make testoptional\" adds the option \"-optional\" and creates a logfile \"testall.log\".\n\n\"make ptestall\" (new with this patch) also adds the option \"-optional\", and creates a logfile \"ptest.log\", possibly overwriting a file with the same name generated by a previous run of \"make ptest\".\n\nAll this naming is pretty inconsistent, but would not stand in the way of a possible positive review.",
    "created_at": "2008-11-14T21:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33517",
    "user": "GeorgSWeber"
}
```

Note: "make testoptional" adds the option "-optional" and creates a logfile "testall.log".

"make ptestall" (new with this patch) also adds the option "-optional", and creates a logfile "ptest.log", possibly overwriting a file with the same name generated by a previous run of "make ptest".

All this naming is pretty inconsistent, but would not stand in the way of a possible positive review.



---

archive/issue_comments_033518.json:
```json
{
    "body": "Applying the \"sage_start\" script patch vanilla as is, copying the new makefile over, corrupting the file \"sage-current-location.txt\" and doing \"make testlong\" does not run very long:\n\n```\n. local/bin/sage-env && sage-starts && ./sage -t -long devel/sage/sage 2>&1 | tee -a testlong.log\n/bin/sh: line 1: /Users/georgweber/Public/sage/sage-3.2.rc0/local/bin/sage-starts: Permission denied\nmake: *** [testlong] Error 126\n```\n\nObviously a \"chmod a+x sage-starts\" in local/bin is needed. I do not know however if this is an issue which could be healed by a somehow \"corrected\" version of the patch, or if it is a mercurial nuisance.",
    "created_at": "2008-11-14T21:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33518",
    "user": "GeorgSWeber"
}
```

Applying the "sage_start" script patch vanilla as is, copying the new makefile over, corrupting the file "sage-current-location.txt" and doing "make testlong" does not run very long:

```
. local/bin/sage-env && sage-starts && ./sage -t -long devel/sage/sage 2>&1 | tee -a testlong.log
/bin/sh: line 1: /Users/georgweber/Public/sage/sage-3.2.rc0/local/bin/sage-starts: Permission denied
make: *** [testlong] Error 126
```

Obviously a "chmod a+x sage-starts" in local/bin is needed. I do not know however if this is an issue which could be healed by a somehow "corrected" version of the patch, or if it is a mercurial nuisance.



---

archive/issue_comments_033519.json:
```json
{
    "body": "This is a mercurial annoyance. Just chmod the script.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-14T22:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33519",
    "user": "mabshoff"
}
```

This is a mercurial annoyance. Just chmod the script.

Cheers,

Michael



---

archive/issue_comments_033520.json:
```json
{
    "body": "Works fine. And now back to #3761.",
    "created_at": "2008-11-14T22:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33520",
    "user": "GeorgSWeber"
}
```

Works fine. And now back to #3761.



---

archive/issue_comments_033521.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-15T05:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33521",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033522.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.rc1",
    "created_at": "2008-11-15T05:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4515#issuecomment-33522",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.2.rc1
