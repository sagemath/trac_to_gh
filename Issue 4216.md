# Issue 4216: [with patch, needs review] use sage-native-execute to run 'convert' in animate.py

archive/issues_004216.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: animate, convert, sage-native-execute\n\nOn my Mac, I was getting this error with the animate command:\n\n```\nsage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.3)],\nxmin=0, xmax=2*pi, figsize=[2,1])\nsage: a.show()\ndyld: Symbol not found: __cg_png_create_info_struct\n  Referenced from:\n/System/Library/Frameworks/ApplicationServices.framework/Versions/A/\nFrameworks/ImageIO.framework/Versions/A/ImageIO\n  Expected in: /Applications/sage/local/lib//libPng.dylib\n\nsh: line 1: 75999 Trace/BPT trap          convert -delay 20 -loop 0\n*.png\n\"/Users/palmieri/.sage/sage_notebook/worksheets/admin/46/cells/37/\nsage0.gif\" \n```\n\nIn the discussion <http://groups.google.com/group/sage-support/browse_frm/thread/526afa1bcc4b7ad5>, it was suggested that 'sage-native-execute' should be used to run the 'convert' command, and this seems to fix the problems.\n\nPlease check this on several different platforms.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4216\n\n",
    "created_at": "2008-09-29T18:16:30Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] use sage-native-execute to run 'convert' in animate.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4216",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: somebody

Keywords: animate, convert, sage-native-execute

On my Mac, I was getting this error with the animate command:

```
sage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.3)],
xmin=0, xmax=2*pi, figsize=[2,1])
sage: a.show()
dyld: Symbol not found: __cg_png_create_info_struct
  Referenced from:
/System/Library/Frameworks/ApplicationServices.framework/Versions/A/
Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Applications/sage/local/lib//libPng.dylib

sh: line 1: 75999 Trace/BPT trap          convert -delay 20 -loop 0
*.png
"/Users/palmieri/.sage/sage_notebook/worksheets/admin/46/cells/37/
sage0.gif" 
```

In the discussion <http://groups.google.com/group/sage-support/browse_frm/thread/526afa1bcc4b7ad5>, it was suggested that 'sage-native-execute' should be used to run the 'convert' command, and this seems to fix the problems.

Please check this on several different platforms.


Issue created by migration from https://trac.sagemath.org/ticket/4216





---

archive/issue_comments_030572.json:
```json
{
    "body": "Attachment [4216.patch](tarball://root/attachments/some-uuid/ticket4216/4216.patch) by @jhpalmieri created at 2008-09-29 18:16:58",
    "created_at": "2008-09-29T18:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4216#issuecomment-30572",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [4216.patch](tarball://root/attachments/some-uuid/ticket4216/4216.patch) by @jhpalmieri created at 2008-09-29 18:16:58



---

archive/issue_events_009548.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2008-09-29T18:17:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "milestone": "sage-3.1.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4216#event-9548"
}
```



---

archive/issue_comments_030573.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-29T19:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4216#issuecomment-30573",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_030574.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-29T19:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4216#issuecomment-30574",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030575.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-29T19:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4216#issuecomment-30575",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_events_009549.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-29T19:01:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4216#event-9549"
}
```



---

archive/issue_comments_030576.json:
```json
{
    "body": "These are related: #3012 and #767",
    "created_at": "2008-09-29T22:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4216#issuecomment-30576",
    "user": "https://github.com/mwhansen"
}
```

These are related: #3012 and #767
