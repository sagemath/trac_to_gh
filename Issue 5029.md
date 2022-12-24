# Issue 5029: Better diffs for trac

archive/issues_005029.json:
```json
{
    "body": "Assignee: schilly\n\nI got tired of not knowing what (new) file /dev/null is when reviewing tickets, or being able to see the hg comments, so I updated the hg plugin to show this info. I'm using this for trac.cython.org. \n\nThis just needs to go into the plugin directory of this trac server, and then restart the trac server. Make sure the filename matches the python version (e.g. py2.4 or py2.5), just rename it if not. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5029\n\n",
    "created_at": "2009-01-19T20:17:13Z",
    "labels": [
        "website/wiki",
        "critical",
        "bug"
    ],
    "title": "Better diffs for trac",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5029",
    "user": "robertwb"
}
```
Assignee: schilly

I got tired of not knowing what (new) file /dev/null is when reviewing tickets, or being able to see the hg comments, so I updated the hg plugin to show this info. I'm using this for trac.cython.org. 

This just needs to go into the plugin directory of this trac server, and then restart the trac server. Make sure the filename matches the python version (e.g. py2.4 or py2.5), just rename it if not. 

Issue created by migration from https://trac.sagemath.org/ticket/5029





---

archive/issue_comments_038305.json:
```json
{
    "body": "Attachment [HgBundleViewer-0.2-py2.4.egg](tarball://root/attachments/some-uuid/ticket5029/HgBundleViewer-0.2-py2.4.egg) by robertwb created at 2009-01-19 20:18:12",
    "created_at": "2009-01-19T20:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38305",
    "user": "robertwb"
}
```

Attachment [HgBundleViewer-0.2-py2.4.egg](tarball://root/attachments/some-uuid/ticket5029/HgBundleViewer-0.2-py2.4.egg) by robertwb created at 2009-01-19 20:18:12



---

archive/issue_comments_038306.json:
```json
{
    "body": "Changing assignee from schilly to mabshoff.",
    "created_at": "2009-01-19T20:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38306",
    "user": "schilly"
}
```

Changing assignee from schilly to mabshoff.



---

archive/issue_comments_038307.json:
```json
{
    "body": "`@`mabshoff: this is probably for you since you are managing the trac server.",
    "created_at": "2009-01-19T20:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38307",
    "user": "schilly"
}
```

`@`mabshoff: this is probably for you since you are managing the trac server.



---

archive/issue_comments_038308.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-19T20:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38308",
    "user": "schilly"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_038309.json:
```json
{
    "body": "Also, the Trac 0.11 series has a diff viewer that shows this information.  Are we switching after SD12?",
    "created_at": "2009-01-19T22:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38309",
    "user": "mhansen"
}
```

Also, the Trac 0.11 series has a diff viewer that shows this information.  Are we switching after SD12?



---

archive/issue_comments_038310.json:
```json
{
    "body": "Oh, I didn't know that. However we do it, it would be really handy.",
    "created_at": "2009-01-19T22:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38310",
    "user": "robertwb"
}
```

Oh, I didn't know that. However we do it, it would be really handy.



---

archive/issue_comments_038311.json:
```json
{
    "body": "I installed this on the Trac server, but it doesn't seem to work.",
    "created_at": "2009-01-24T12:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38311",
    "user": "mhansen"
}
```

I installed this on the Trac server, but it doesn't seem to work.



---

archive/issue_comments_038312.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T12:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38312",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_038313.json:
```json
{
    "body": "> I got tired of not knowing what (new) file /dev/null is when reviewing tickets, or being able to see the hg comments,\n\n\nThanks, Robert, for raising this issue and have it fixed. With trac now able to display diff comments, it has made my life easier when it comes to crediting patch authors. Previously, I would need to download a patch in raw text format in order to see the patch author's name (and I'm bad at spelling people's names).",
    "created_at": "2009-01-26T08:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38313",
    "user": "mvngu"
}
```

> I got tired of not knowing what (new) file /dev/null is when reviewing tickets, or being able to see the hg comments,


Thanks, Robert, for raising this issue and have it fixed. With trac now able to display diff comments, it has made my life easier when it comes to crediting patch authors. Previously, I would need to download a patch in raw text format in order to see the patch author's name (and I'm bad at spelling people's names).
