# Issue 4734: sage -notebook option now broken

archive/issues_004734.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n\nDear Sage-Devels,\n\nLet me again thank you for the excellent work put in building sage.\n\nI've found a bug in the most recent release. Specifically, when\ninvoked with the -notebook switch, the current release does not\nproperly quote paths. So, if I execute:\n\n/Applications/sage/sage -notebook \"/Users/carson/doc/math/\nsage_notebook/\"\n\nSage says:\n\nTraceback (most recent call last):\n File \"/Applications/sage/local/bin/sage-notebook\", line 14, in\n<module>\n   exec \"notebook(\" + \",\".join(sys.argv[1:]) + \")\"\n File \"<string>\", line 1\n   notebook(/Users/carson/doc/math/sage_notebook/)\n            ^\nSyntaxError: invalid syntax\n\nIf I edit the offending line in local/bin/sage-notebook:\n\n   exec \"notebook(\" + \",\".join(sys.argv[1:]) + \")\"\n\nTo instead read:\n\n   exec \"notebook('\" + \",\".join(sys.argv[1:]) + \"')\"\n\nThen the -notebook switch works as expected. Please consider using the\nfollowing sage-notebook file to correct this bug:\n\nhttp://bentham.k2.t.u-tokyo.ac.jp/media/bugs/sage/sage-notebook\n\nCheers,\n```\n\n\nMakes sense.  This was indeed caused by a patch in the last version of sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4734\n\n",
    "created_at": "2008-12-07T04:49:58Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "sage -notebook option now broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4734",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby


```

Dear Sage-Devels,

Let me again thank you for the excellent work put in building sage.

I've found a bug in the most recent release. Specifically, when
invoked with the -notebook switch, the current release does not
properly quote paths. So, if I execute:

/Applications/sage/sage -notebook "/Users/carson/doc/math/
sage_notebook/"

Sage says:

Traceback (most recent call last):
 File "/Applications/sage/local/bin/sage-notebook", line 14, in
<module>
   exec "notebook(" + ",".join(sys.argv[1:]) + ")"
 File "<string>", line 1
   notebook(/Users/carson/doc/math/sage_notebook/)
            ^
SyntaxError: invalid syntax

If I edit the offending line in local/bin/sage-notebook:

   exec "notebook(" + ",".join(sys.argv[1:]) + ")"

To instead read:

   exec "notebook('" + ",".join(sys.argv[1:]) + "')"

Then the -notebook switch works as expected. Please consider using the
following sage-notebook file to correct this bug:

http://bentham.k2.t.u-tokyo.ac.jp/media/bugs/sage/sage-notebook

Cheers,
```


Makes sense.  This was indeed caused by a patch in the last version of sage.

Issue created by migration from https://trac.sagemath.org/ticket/4734





---

archive/issue_comments_035664.json:
```json
{
    "body": "The -notebook command line option takes the same arguments as the\nnotebook() sage command. The directory argument to both the command\nline option and the sage command should be a python string. So the\nproper way to write your code is\n\n/Applications/sage/sage -notebook '\"/Users/carson/doc/math/\nsage_notebook/\"'\n\nHere the outer single quotes ' ' quote the python string \"/Users/\ncarson/doc/math/sage_notebook/\". This is a function of your shell.\n\nThe most recent release of Sage also accepts for example\n\n/Applications/sage/sage -notebook '\"/Users/carson/doc/math/\nsage_notebook/\"' secure=True open_viewer=False\n\nThis did not work for the old release of Sage.",
    "created_at": "2008-12-07T10:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4734#issuecomment-35664",
    "user": "https://github.com/kwankyu"
}
```

The -notebook command line option takes the same arguments as the
notebook() sage command. The directory argument to both the command
line option and the sage command should be a python string. So the
proper way to write your code is

/Applications/sage/sage -notebook '"/Users/carson/doc/math/
sage_notebook/"'

Here the outer single quotes ' ' quote the python string "/Users/
carson/doc/math/sage_notebook/". This is a function of your shell.

The most recent release of Sage also accepts for example

/Applications/sage/sage -notebook '"/Users/carson/doc/math/
sage_notebook/"' secure=True open_viewer=False

This did not work for the old release of Sage.



---

archive/issue_comments_035665.json:
```json
{
    "body": "Since the first input two notebook has to be a string, if there are no named parameters we should rewrite the code to make the original user's input work.  I.e., This should work no matter what, and I see no reason not to make this work:\n\n```\nsage -notebook \"/Users/carson/doc/math/sage_notebook/\"\n```\n",
    "created_at": "2008-12-07T19:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4734#issuecomment-35665",
    "user": "https://github.com/williamstein"
}
```

Since the first input two notebook has to be a string, if there are no named parameters we should rewrite the code to make the original user's input work.  I.e., This should work no matter what, and I see no reason not to make this work:

```
sage -notebook "/Users/carson/doc/math/sage_notebook/"
```




---

archive/issue_comments_035666.json:
```json
{
    "body": "Then the patch for ticket #4641 applied to Sage 3.2.1 should be abolished, and the original code\n\nnotebook(*sys.argv[1:])\n\nshould be recovered, until a better solution be found. The original code seems better than the code proposed by the reporter of this bug.",
    "created_at": "2008-12-08T04:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4734#issuecomment-35666",
    "user": "https://github.com/kwankyu"
}
```

Then the patch for ticket #4641 applied to Sage 3.2.1 should be abolished, and the original code

notebook(*sys.argv[1:])

should be recovered, until a better solution be found. The original code seems better than the code proposed by the reporter of this bug.



---

archive/issue_comments_035667.json:
```json
{
    "body": "Attachment [trac_4734.patch](tarball://root/attachments/some-uuid/ticket4734/trac_4734.patch) by @williamstein created at 2009-01-24 15:49:38",
    "created_at": "2009-01-24T15:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4734#issuecomment-35667",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4734.patch](tarball://root/attachments/some-uuid/ticket4734/trac_4734.patch) by @williamstein created at 2009-01-24 15:49:38



---

archive/issue_events_010815.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-01-24T15:50:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4734",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4734#event-10815"
}
```



---

archive/issue_comments_035668.json:
```json
{
    "body": "apply the patch to the *SCRIPTS* repo!",
    "created_at": "2009-01-24T15:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4734#issuecomment-35668",
    "user": "https://github.com/williamstein"
}
```

apply the patch to the *SCRIPTS* repo!



---

archive/issue_comments_035669.json:
```json
{
    "body": "Nice, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T04:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4734#issuecomment-35669",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice, positive review.

Cheers,

Michael



---

archive/issue_comments_035670.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T04:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4734#issuecomment-35670",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035671.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T04:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4734#issuecomment-35671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_events_010816.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-02T04:58:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4734",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4734#event-10816"
}
```
