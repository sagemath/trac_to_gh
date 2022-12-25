# Issue 5029: Better diffs for trac

archive/issues_005029.json:
```json
{
    "body": "Assignee: @haraldschilly\n\nI got tired of not knowing what (new) file /dev/null is when reviewing tickets, or being able to see the hg comments, so I updated the hg plugin to show this info. I'm using this for trac.cython.org. \n\nThis just needs to go into the plugin directory of this trac server, and then restart the trac server. Make sure the filename matches the python version (e.g. py2.4 or py2.5), just rename it if not. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5029\n\n",
    "created_at": "2009-01-19T20:17:13Z",
    "labels": [
        "component: website/wiki",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Better diffs for trac",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5029",
    "user": "https://github.com/robertwb"
}
```
Assignee: @haraldschilly

I got tired of not knowing what (new) file /dev/null is when reviewing tickets, or being able to see the hg comments, so I updated the hg plugin to show this info. I'm using this for trac.cython.org. 

This just needs to go into the plugin directory of this trac server, and then restart the trac server. Make sure the filename matches the python version (e.g. py2.4 or py2.5), just rename it if not. 

Issue created by migration from https://trac.sagemath.org/ticket/5029





---

archive/issue_comments_038233.json:
```json
{
    "body": "Attachment [HgBundleViewer-0.2-py2.4.egg](tarball://root/attachments/some-uuid/ticket5029/HgBundleViewer-0.2-py2.4.egg) by @robertwb created at 2009-01-19 20:18:12",
    "created_at": "2009-01-19T20:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38233",
    "user": "https://github.com/robertwb"
}
```

Attachment [HgBundleViewer-0.2-py2.4.egg](tarball://root/attachments/some-uuid/ticket5029/HgBundleViewer-0.2-py2.4.egg) by @robertwb created at 2009-01-19 20:18:12



---

archive/issue_comments_038234.json:
```json
{
    "body": "Changing assignee from @haraldschilly to mabshoff.",
    "created_at": "2009-01-19T20:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38234",
    "user": "https://github.com/haraldschilly"
}
```

Changing assignee from @haraldschilly to mabshoff.



---

archive/issue_comments_038235.json:
```json
{
    "body": "`@`mabshoff: this is probably for you since you are managing the trac server.",
    "created_at": "2009-01-19T20:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38235",
    "user": "https://github.com/haraldschilly"
}
```

`@`mabshoff: this is probably for you since you are managing the trac server.



---

archive/issue_comments_038236.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-19T20:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38236",
    "user": "https://github.com/haraldschilly"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_038237.json:
```json
{
    "body": "Also, the Trac 0.11 series has a diff viewer that shows this information.  Are we switching after SD12?",
    "created_at": "2009-01-19T22:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38237",
    "user": "https://github.com/mwhansen"
}
```

Also, the Trac 0.11 series has a diff viewer that shows this information.  Are we switching after SD12?



---

archive/issue_comments_038238.json:
```json
{
    "body": "Oh, I didn't know that. However we do it, it would be really handy.",
    "created_at": "2009-01-19T22:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38238",
    "user": "https://github.com/robertwb"
}
```

Oh, I didn't know that. However we do it, it would be really handy.



---

archive/issue_comments_038239.json:
```json
{
    "body": "I installed this on the Trac server, but it doesn't seem to work.",
    "created_at": "2009-01-24T12:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38239",
    "user": "https://github.com/mwhansen"
}
```

I installed this on the Trac server, but it doesn't seem to work.



---

archive/issue_events_011606.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-01-24T12:53:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5029#event-11606"
}
```



---

archive/issue_comments_038240.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T12:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38240",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_038241.json:
```json
{
    "body": "> I got tired of not knowing what (new) file /dev/null is when reviewing tickets, or being able to see the hg comments,\n\n\n\nThanks, Robert, for raising this issue and have it fixed. With trac now able to display diff comments, it has made my life easier when it comes to crediting patch authors. Previously, I would need to download a patch in raw text format in order to see the patch author's name (and I'm bad at spelling people's names).",
    "created_at": "2009-01-26T08:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5029#issuecomment-38241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

> I got tired of not knowing what (new) file /dev/null is when reviewing tickets, or being able to see the hg comments,



Thanks, Robert, for raising this issue and have it fixed. With trac now able to display diff comments, it has made my life easier when it comes to crediting patch authors. Previously, I would need to download a patch in raw text format in order to see the patch author's name (and I'm bad at spelling people's names).
