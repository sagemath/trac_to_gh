# Issue 3676: [with patch, needs review] Refactor graph isom code.

archive/issues_003676.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  boothby\n\nKeywords: graphs\n\nAfter this patch, `graph_isom` will be essentially obsolete. Brought to the GNU General Public by Google, Inc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3676\n\n",
    "created_at": "2008-07-19T00:07:34Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] Refactor graph isom code.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3676",
    "user": "rlm"
}
```
Assignee: rlm

CC:  boothby

Keywords: graphs

After this patch, `graph_isom` will be essentially obsolete. Brought to the GNU General Public by Google, Inc.

Issue created by migration from https://trac.sagemath.org/ticket/3676





---

archive/issue_comments_026020.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-19T00:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26020",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_026021.json:
```json
{
    "body": "FYI, I got the following test failure:\n\n\n```\nwdj@hera:~/sagefiles/sage-3.0.4.rc0$ ./sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx\nsage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx    **********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.0.4.rc0/tmp/finite_field_ntl_gf2e.py\", line 170:\n    sage: k.modulus()\nExpected:\n    x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1\nGot:\n    x^17\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wdj/sagefiles/sage-3.0.4.rc0/tmp/.doctest_finite_field_ntl_gf2e.py\n         [2.9 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx\nTotal time for all tests: 2.9 seconds\n```\n",
    "created_at": "2008-07-19T05:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26021",
    "user": "wdj"
}
```

FYI, I got the following test failure:


```
wdj@hera:~/sagefiles/sage-3.0.4.rc0$ ./sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx    **********************************************************************
File "/home/wdj/sagefiles/sage-3.0.4.rc0/tmp/finite_field_ntl_gf2e.py", line 170:
    sage: k.modulus()
Expected:
    x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1
Got:
    x^17
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-3.0.4.rc0/tmp/.doctest_finite_field_ntl_gf2e.py
         [2.9 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
Total time for all tests: 2.9 seconds
```




---

archive/issue_comments_026022.json:
```json
{
    "body": "David,\n\nthe above doctest is a known issue and orthogonal to rlm's code. See #3634 for the patch that likely caused this.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-19T13:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26022",
    "user": "mabshoff"
}
```

David,

the above doctest is a known issue and orthogonal to rlm's code. See #3634 for the patch that likely caused this.

Cheers,

Michael



---

archive/issue_comments_026023.json:
```json
{
    "body": "Okay. I was just trying to help out with the doctesting, that's all. Seems like it tests fine then.",
    "created_at": "2008-07-19T13:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26023",
    "user": "wdj"
}
```

Okay. I was just trying to help out with the doctesting, that's all. Seems like it tests fine then.



---

archive/issue_comments_026024.json:
```json
{
    "body": "Attachment\n\nIt's so... readable...",
    "created_at": "2008-08-04T17:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26024",
    "user": "boothby"
}
```

Attachment

It's so... readable...



---

archive/issue_comments_026025.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-06T17:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26025",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_026026.json:
```json
{
    "body": "The patches here may depend on #3703.",
    "created_at": "2008-08-06T17:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26026",
    "user": "rlm"
}
```

The patches here may depend on #3703.



---

archive/issue_comments_026027.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-06T18:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26027",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_026028.json:
```json
{
    "body": "Attachment\n\nI can flatten those last three if desired...",
    "created_at": "2008-08-06T22:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26028",
    "user": "rlm"
}
```

Attachment

I can flatten those last three if desired...



---

archive/issue_comments_026029.json:
```json
{
    "body": "Once this ticket is merged #3786 should be next.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-10T20:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26029",
    "user": "mabshoff"
}
```

Once this ticket is merged #3786 should be next.

Cheers,

Michael



---

archive/issue_comments_026030.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-11T18:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26030",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_026031.json:
```json
{
    "body": "`3676-ncalexan-docstring-changes.patch` changes some documentation to be clearer.\n\nI am happy with this patch, save for a missing module docstring.  rlmiller will write said docstring, explaining programming API to his code, and then this is ready for showtime.\n\n\nApply all patches in order.",
    "created_at": "2008-08-11T18:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26031",
    "user": "ncalexan"
}
```

`3676-ncalexan-docstring-changes.patch` changes some documentation to be clearer.

I am happy with this patch, save for a missing module docstring.  rlmiller will write said docstring, explaining programming API to his code, and then this is ready for showtime.


Apply all patches in order.



---

archive/issue_comments_026032.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-08-11T22:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26032",
    "user": "boothby"
}
```

Looks good to me.



---

archive/issue_comments_026033.json:
```json
{
    "body": "The last patch is a flattened version of the previous ones, together with a recipe for implementing other objects. It should be finally ready to go. Apply only the last patch.",
    "created_at": "2008-08-12T01:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26033",
    "user": "rlm"
}
```

The last patch is a flattened version of the previous ones, together with a recipe for implementing other objects. It should be finally ready to go. Apply only the last patch.



---

archive/issue_comments_026034.json:
```json
{
    "body": "Apply only this patch (please do not delete the others!)",
    "created_at": "2008-08-12T01:29:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26034",
    "user": "rlm"
}
```

Apply only this patch (please do not delete the others!)



---

archive/issue_comments_026035.json:
```json
{
    "body": "Attachment\n\nrlm and I have gone back and forth on this and I think it's great.  I say apply!",
    "created_at": "2008-08-12T01:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26035",
    "user": "ncalexan"
}
```

Attachment

rlm and I have gone back and forth on this and I think it's great.  I say apply!



---

archive/issue_comments_026036.json:
```json
{
    "body": "Merged in Sage 3.1.alpha2",
    "created_at": "2008-08-12T05:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26036",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha2



---

archive/issue_comments_026037.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-12T05:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3676#issuecomment-26037",
    "user": "mabshoff"
}
```

Resolution: fixed
