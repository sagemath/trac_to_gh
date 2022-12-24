# Issue 4354: loading a file with spaces in the filename doesn't work

archive/issues_004354.json:
```json
{
    "body": "Assignee: tbd\n\ntry it at home:\n\n\n```\n$ echo 'print \"ok\"' > 'test file.sage'\n$ sage \"test file.sage\"\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4354\n\n",
    "created_at": "2008-10-24T00:41:49Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "loading a file with spaces in the filename doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4354",
    "user": "anakha"
}
```
Assignee: tbd

try it at home:


```
$ echo 'print "ok"' > 'test file.sage'
$ sage "test file.sage"
```


Issue created by migration from https://trac.sagemath.org/ticket/4354





---

archive/issue_comments_031969.json:
```json
{
    "body": "Changing assignee from tbd to anakha.",
    "created_at": "2008-10-24T00:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31969",
    "user": "anakha"
}
```

Changing assignee from tbd to anakha.



---

archive/issue_comments_031970.json:
```json
{
    "body": "Crap, I need to relax on the submit button",
    "created_at": "2008-10-24T00:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31970",
    "user": "anakha"
}
```

Crap, I need to relax on the submit button



---

archive/issue_comments_031971.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2008-10-24T00:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31971",
    "user": "anakha"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_031972.json:
```json
{
    "body": "Attachment [trac_4354.patch](tarball://root/attachments/some-uuid/ticket4354/trac_4354.patch) by anakha created at 2008-10-24 01:01:34\n\nWith the above patch and replacement sage script the example given should work and print 'ok'.\n\nBe aware that if you copied the sage script somewhere (like /usr/local/bin) for convenience you need to modify that copy too.  The line near the end that reads \n\n```\n\"$SAGE_ROOT/local/bin/sage-sage\" $*\n```\n\nneeds to be replaced by\n\n```\n\"$SAGE_ROOT/local/bin/sage-sage\" \"$@\"\n```\n",
    "created_at": "2008-10-24T01:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31972",
    "user": "anakha"
}
```

Attachment [trac_4354.patch](tarball://root/attachments/some-uuid/ticket4354/trac_4354.patch) by anakha created at 2008-10-24 01:01:34

With the above patch and replacement sage script the example given should work and print 'ok'.

Be aware that if you copied the sage script somewhere (like /usr/local/bin) for convenience you need to modify that copy too.  The line near the end that reads 

```
"$SAGE_ROOT/local/bin/sage-sage" $*
```

needs to be replaced by

```
"$SAGE_ROOT/local/bin/sage-sage" "$@"
```




---

archive/issue_comments_031973.json:
```json
{
    "body": "For the patch **sage**, below are some possible fixes to the documentation. Please also refer to #1389.\n\n\n\n1.\n\n```\n-echo \"You must compile SAGE first using 'make' in the SAGE root directory.\" >&2\n+echo \"You must compile Sage first using 'make' in the Sage root directory.\" >&2\n```\n\n\n\n2.\n\n```\n-echo \"(If you have already compiled SAGE, you must set the SAGE_ROOT variable in \"\n+echo \"(If you have already compiled Sage, you must set the SAGE_ROOT variable in \"\n```\n\n\n\n3.\n\n```\n-# whenver SAGE exists.\n+# whenever Sage exits.\n```\n",
    "created_at": "2008-10-27T12:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31973",
    "user": "mvngu"
}
```

For the patch **sage**, below are some possible fixes to the documentation. Please also refer to #1389.



1.

```
-echo "You must compile SAGE first using 'make' in the SAGE root directory." >&2
+echo "You must compile Sage first using 'make' in the Sage root directory." >&2
```



2.

```
-echo "(If you have already compiled SAGE, you must set the SAGE_ROOT variable in "
+echo "(If you have already compiled Sage, you must set the SAGE_ROOT variable in "
```



3.

```
-# whenver SAGE exists.
+# whenever Sage exits.
```




---

archive/issue_comments_031974.json:
```json
{
    "body": "REFEREE:\n\nCan you please rebase this against 3.2.1.alpha*?  I tried applying and got some many failed hunks I can't go further.\n\n```\nsage: hg_scripts.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4354/trac_4354.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4354/trac_4354.patch?format=raw\nLoading: [..]\ncd \"/Users/wstein/sage/local/bin\" && hg status\ncd \"/Users/wstein/sage/local/bin\" && hg status\ncd \"/Users/wstein/sage/local/bin\" && hg import   \"/Users/wstein/.sage/temp/teragon_2.local/1537/tmp_0.patch\"\napplying /Users/wstein/.sage/temp/teragon_2.local/1537/tmp_0.patch\npatching file sage-sage\nHunk #5 succeeded at 227 with fuzz 1 (offset 4 lines).\nHunk #6 succeeded at 246 with fuzz 1 (offset 4 lines).\nHunk #7 FAILED at 332\nHunk #8 FAILED at 376\nHunk #10 succeeded at 474 with fuzz 1 (offset 41 lines).\nHunk #12 succeeded at 507 with fuzz 1 (offset 41 lines).\nHunk #18 succeeded at 603 with fuzz 1 (offset 41 lines).\nHunk #20 succeeded at 647 with fuzz 1 (offset 41 lines).\nHunk #27 FAILED at 768\nHunk #28 FAILED at 794\n4 out of 28 hunks FAILED -- saving rejects to file sage-sage.rej\nabort: patch failed to apply\n```\n\n\nNote -- I did *read* the patch and I think it's very good.  Also, I'm very glad for Mvngu's observations about all those typos, especially line -2 of SAGE_ROOT/sage.  Can you fix those typos in sage too?",
    "created_at": "2008-11-29T02:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31974",
    "user": "was"
}
```

REFEREE:

Can you please rebase this against 3.2.1.alpha*?  I tried applying and got some many failed hunks I can't go further.

```
sage: hg_scripts.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4354/trac_4354.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4354/trac_4354.patch?format=raw
Loading: [..]
cd "/Users/wstein/sage/local/bin" && hg status
cd "/Users/wstein/sage/local/bin" && hg status
cd "/Users/wstein/sage/local/bin" && hg import   "/Users/wstein/.sage/temp/teragon_2.local/1537/tmp_0.patch"
applying /Users/wstein/.sage/temp/teragon_2.local/1537/tmp_0.patch
patching file sage-sage
Hunk #5 succeeded at 227 with fuzz 1 (offset 4 lines).
Hunk #6 succeeded at 246 with fuzz 1 (offset 4 lines).
Hunk #7 FAILED at 332
Hunk #8 FAILED at 376
Hunk #10 succeeded at 474 with fuzz 1 (offset 41 lines).
Hunk #12 succeeded at 507 with fuzz 1 (offset 41 lines).
Hunk #18 succeeded at 603 with fuzz 1 (offset 41 lines).
Hunk #20 succeeded at 647 with fuzz 1 (offset 41 lines).
Hunk #27 FAILED at 768
Hunk #28 FAILED at 794
4 out of 28 hunks FAILED -- saving rejects to file sage-sage.rej
abort: patch failed to apply
```


Note -- I did *read* the patch and I think it's very good.  Also, I'm very glad for Mvngu's observations about all those typos, especially line -2 of SAGE_ROOT/sage.  Can you fix those typos in sage too?



---

archive/issue_comments_031975.json:
```json
{
    "body": "From patch author:\n\n```\nI'm kind of overloaded with work from school now, so it will have to\nwait about 2 or 3 weeks.  If nobody does it before then, I'll do it.\n```\n",
    "created_at": "2008-11-29T07:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31975",
    "user": "was"
}
```

From patch author:

```
I'm kind of overloaded with work from school now, so it will have to
wait about 2 or 3 weeks.  If nobody does it before then, I'll do it.
```




---

archive/issue_comments_031976.json:
```json
{
    "body": "Attachment [sage.2](tarball://root/attachments/some-uuid/ticket4354/sage.2) by abergeron created at 2008-12-24 04:18:31",
    "created_at": "2008-12-24T04:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31976",
    "user": "abergeron"
}
```

Attachment [sage.2](tarball://root/attachments/some-uuid/ticket4354/sage.2) by abergeron created at 2008-12-24 04:18:31



---

archive/issue_comments_031977.json:
```json
{
    "body": "Changing assignee from anakha to abergeron.",
    "created_at": "2008-12-24T04:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31977",
    "user": "abergeron"
}
```

Changing assignee from anakha to abergeron.



---

archive/issue_comments_031978.json:
```json
{
    "body": "I'm back in buisness!\n\ntrac_4354.2.patch is a rebase against 3.2.2\n\nsage.2 is the sage startup script with the doc changes proposed by mvngu.",
    "created_at": "2008-12-24T04:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31978",
    "user": "abergeron"
}
```

I'm back in buisness!

trac_4354.2.patch is a rebase against 3.2.2

sage.2 is the sage startup script with the doc changes proposed by mvngu.



---

archive/issue_comments_031979.json:
```json
{
    "body": "Target time for the review: January 13th",
    "created_at": "2008-12-29T21:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31979",
    "user": "GeorgSWeber"
}
```

Target time for the review: January 13th



---

archive/issue_comments_031980.json:
```json
{
    "body": "Rescheduled for January 18th",
    "created_at": "2009-01-15T21:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31980",
    "user": "GeorgSWeber"
}
```

Rescheduled for January 18th



---

archive/issue_comments_031981.json:
```json
{
    "body": "Unfortunately, this patch no longer applies cleanly against Sage 3.2.3.\nIt is obvious how to rebase it, though (sigh).",
    "created_at": "2009-01-19T00:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31981",
    "user": "GeorgSWeber"
}
```

Unfortunately, this patch no longer applies cleanly against Sage 3.2.3.
It is obvious how to rebase it, though (sigh).



---

archive/issue_comments_031982.json:
```json
{
    "body": "Attachment [trac_4354_rebase.patch](tarball://root/attachments/some-uuid/ticket4354/trac_4354_rebase.patch) by abergeron created at 2009-01-24 02:47:56\n\nRebase against 3.3.alpha1",
    "created_at": "2009-01-24T02:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31982",
    "user": "abergeron"
}
```

Attachment [trac_4354_rebase.patch](tarball://root/attachments/some-uuid/ticket4354/trac_4354_rebase.patch) by abergeron created at 2009-01-24 02:47:56

Rebase against 3.3.alpha1



---

archive/issue_comments_031983.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T02:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31983",
    "user": "abergeron"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031984.json:
```json
{
    "body": "Attachment [trac_4354_rebase_3.3.rc0.patch](tarball://root/attachments/some-uuid/ticket4354/trac_4354_rebase_3.3.rc0.patch) by GeorgSWeber created at 2009-02-14 21:47:20\n\nrebase against 3.3.rc0 (you'll need also to put \"sage.2\" as \"sage\" into $SAGE_ROOT )",
    "created_at": "2009-02-14T21:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31984",
    "user": "GeorgSWeber"
}
```

Attachment [trac_4354_rebase_3.3.rc0.patch](tarball://root/attachments/some-uuid/ticket4354/trac_4354_rebase_3.3.rc0.patch) by GeorgSWeber created at 2009-02-14 21:47:20

rebase against 3.3.rc0 (you'll need also to put "sage.2" as "sage" into $SAGE_ROOT )



---

archive/issue_comments_031985.json:
```json
{
    "body": "Well, this time \"sage-run\" had changed in between 3.3.alpha0 and 3.3.rc0.\n\nI carefully hand-edited the 3.3.alpha0 patch (which did apply to 3.3.rc0 \"sage-sage\" only, but no longer to \"sage-run\") to reflect these changes, so the HG changeset header with the credit stayed the same.\n\nThe resulting patch now applies cleanly against 3.3.rc0.",
    "created_at": "2009-02-14T21:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31985",
    "user": "GeorgSWeber"
}
```

Well, this time "sage-run" had changed in between 3.3.alpha0 and 3.3.rc0.

I carefully hand-edited the 3.3.alpha0 patch (which did apply to 3.3.rc0 "sage-sage" only, but no longer to "sage-run") to reflect these changes, so the HG changeset header with the credit stayed the same.

The resulting patch now applies cleanly against 3.3.rc0.



---

archive/issue_comments_031986.json:
```json
{
    "body": "Hello Michael,\n\nthis should go in 3.3 now. Of the handful files above, you'll need two:\n\nA) The third one \"sage.2\" to go directly (no repo!!) right under $SAGE_ROOT as \"sage\" to replace the older script of the same name there. Mind the usual file executable flag issues ;-)\n\nB) The last one \"trac_4354_rebase_3.3.rc0.patch\" applies as a HG patch to /local/bin (Sage scripts) repo.\n\nThen test (as the original ticket comment says) from the bash command line (say after \"your_favourite_path_to/sage -sh\"):\n\n```\n$ echo 'print \"ok\"' > 'test file.sage'\n$ sage \"test file.sage\"\n```\n\n\n(This can hardly be a doctest, it's just outside scope --- and IMHO the issue of testing this kind of environmental stuff should not burden this ticket here, although it is a valid question.)",
    "created_at": "2009-02-14T22:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31986",
    "user": "GeorgSWeber"
}
```

Hello Michael,

this should go in 3.3 now. Of the handful files above, you'll need two:

A) The third one "sage.2" to go directly (no repo!!) right under $SAGE_ROOT as "sage" to replace the older script of the same name there. Mind the usual file executable flag issues ;-)

B) The last one "trac_4354_rebase_3.3.rc0.patch" applies as a HG patch to /local/bin (Sage scripts) repo.

Then test (as the original ticket comment says) from the bash command line (say after "your_favourite_path_to/sage -sh"):

```
$ echo 'print "ok"' > 'test file.sage'
$ sage "test file.sage"
```


(This can hardly be a doctest, it's just outside scope --- and IMHO the issue of testing this kind of environmental stuff should not burden this ticket here, although it is a valid question.)



---

archive/issue_comments_031987.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-15T14:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31987",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031988.json:
```json
{
    "body": "Merged sage.2 and trac_4354_rebase_3.3.rc0.patch in Sage 3.3.rc1.\n\nI double checked both patches and I am confident they do the right thing.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T14:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4354#issuecomment-31988",
    "user": "mabshoff"
}
```

Merged sage.2 and trac_4354_rebase_3.3.rc0.patch in Sage 3.3.rc1.

I double checked both patches and I am confident they do the right thing.

Cheers,

Michael
