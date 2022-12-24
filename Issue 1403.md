# Issue 1403: mwrank: crash upon exit

archive/issues_001403.json:
```json
{
    "body": "Assignee: @williamstein\n\nJustin Walker reported:\n\n```\n'mwrank' doesn't like it if you just exit (by typing \"^D\" or, more or  \nless equivalently, by \"ending a file\").\n\nThus, if you run 'mwrank' and give it a file containing, for example,  \n\"[0,0,1,-1,0]\" and nothing else, it will barf at the end.  If your  \nfile contains \"[0,0,0,0,0]\", the program sweetly closes up shop (when  \nit reads this) and quits.\n\nThe error I get is\n   bad ZZ input\n   Abort trap\n\nAnyone know why this doesn't show up in the test logs?  Is it worth  \ntracking down?\n\nThe issue is that the terminating condition for input processing in  \n'getcurve()' is a \"null curve\" (\"\"[0,0,0,0,0]\"\"), rather than EOF.  \nAn EOF is an error condition, hence the abort(). \n```\n\n\nSee also #1402.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1403\n\n",
    "created_at": "2007-12-05T11:42:07Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "mwrank: crash upon exit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1403",
    "user": "mabshoff"
}
```
Assignee: @williamstein

Justin Walker reported:

```
'mwrank' doesn't like it if you just exit (by typing "^D" or, more or  
less equivalently, by "ending a file").

Thus, if you run 'mwrank' and give it a file containing, for example,  
"[0,0,1,-1,0]" and nothing else, it will barf at the end.  If your  
file contains "[0,0,0,0,0]", the program sweetly closes up shop (when  
it reads this) and quits.

The error I get is
   bad ZZ input
   Abort trap

Anyone know why this doesn't show up in the test logs?  Is it worth  
tracking down?

The issue is that the terminating condition for input processing in  
'getcurve()' is a "null curve" (""[0,0,0,0,0]""), rather than EOF.  
An EOF is an error condition, hence the abort(). 
```


See also #1402.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1403





---

archive/issue_comments_009049.json:
```json
{
    "body": "John Cremona wrote:\n\n```\ni.e. mwrank crashed rather than stopping cleanly when reachinf EOF on\ninput.  Should be an easy fix to qrank/getcurve.cc, so I'll do it.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-12-05T19:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9049",
    "user": "mabshoff"
}
```

John Cremona wrote:

```
i.e. mwrank crashed rather than stopping cleanly when reachinf EOF on
input.  Should be an easy fix to qrank/getcurve.cc, so I'll do it.
```


Cheers,

Michael



---

archive/issue_comments_009050.json:
```json
{
    "body": "patch for file qrank/getcurve.cc which fixes the problem",
    "created_at": "2007-12-05T20:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9050",
    "user": "@JohnCremona"
}
```

patch for file qrank/getcurve.cc which fixes the problem



---

archive/issue_comments_009051.json:
```json
{
    "body": "Attachment [getcurve.patch](tarball://root/attachments/some-uuid/ticket1403/getcurve.patch) by @JohnCremona created at 2007-12-05 20:23:15\n\nI have fixed this.  Patch attached.  JEC",
    "created_at": "2007-12-05T20:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9051",
    "user": "@JohnCremona"
}
```

Attachment [getcurve.patch](tarball://root/attachments/some-uuid/ticket1403/getcurve.patch) by @JohnCremona created at 2007-12-05 20:23:15

I have fixed this.  Patch attached.  JEC



---

archive/issue_comments_009052.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-05T20:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9052",
    "user": "@JohnCremona"
}
```

Resolution: fixed



---

archive/issue_comments_009053.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-05T21:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9053",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_009054.json:
```json
{
    "body": "Hello John,\n\nthe release manager usually closes the ticket once the patch has been applied into the current release tree. That way we do not lose fixes.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-05T21:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9054",
    "user": "mabshoff"
}
```

Hello John,

the release manager usually closes the ticket once the patch has been applied into the current release tree. That way we do not lose fixes.

Cheers,

Michael



---

archive/issue_comments_009055.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-05T21:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9055",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_009056.json:
```json
{
    "body": "Merged in 2.9.alpha0.",
    "created_at": "2007-12-06T02:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9056",
    "user": "mabshoff"
}
```

Merged in 2.9.alpha0.



---

archive/issue_comments_009057.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T02:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9057",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009058.json:
```json
{
    "body": "Merged in 2.9.alpha0.",
    "created_at": "2007-12-06T02:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9058",
    "user": "mabshoff"
}
```

Merged in 2.9.alpha0.



---

archive/issue_comments_009059.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-06T09:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9059",
    "user": "@JohnCremona"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_009060.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-06T09:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9060",
    "user": "@JohnCremona"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_009061.json:
```json
{
    "body": "Attachment [reader.h.patch](tarball://root/attachments/some-uuid/ticket1403/reader.h.patch) by @JohnCremona created at 2007-12-06 09:09:08\n\nSecond patch file reader.h.patch to be applied to qcurves/reader.h will stop the same happening for other binaries (e.g. tate, conductor etc) built in the qcurves directory.",
    "created_at": "2007-12-06T09:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9061",
    "user": "@JohnCremona"
}
```

Attachment [reader.h.patch](tarball://root/attachments/some-uuid/ticket1403/reader.h.patch) by @JohnCremona created at 2007-12-06 09:09:08

Second patch file reader.h.patch to be applied to qcurves/reader.h will stop the same happening for other binaries (e.g. tate, conductor etc) built in the qcurves directory.



---

archive/issue_comments_009062.json:
```json
{
    "body": "Second patch merged in 2.9.alpha1.",
    "created_at": "2007-12-06T13:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9062",
    "user": "mabshoff"
}
```

Second patch merged in 2.9.alpha1.



---

archive/issue_comments_009063.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T13:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9063",
    "user": "mabshoff"
}
```

Resolution: fixed
