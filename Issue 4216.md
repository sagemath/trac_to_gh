# Issue 4216: [with patch, needs review] use sage-native-execute to run 'convert' in animate.py

archive/issues_004216.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: animate, convert, sage-native-execute\n\nOn my Mac, I was getting this error with the animate command:\n\n```\nsage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.3)],\nxmin=0, xmax=2*pi, figsize=[2,1])\nsage: a.show()\ndyld: Symbol not found: __cg_png_create_info_struct\n  Referenced from:\n/System/Library/Frameworks/ApplicationServices.framework/Versions/A/\nFrameworks/ImageIO.framework/Versions/A/ImageIO\n  Expected in: /Applications/sage/local/lib//libPng.dylib\n\nsh: line 1: 75999 Trace/BPT trap          convert -delay 20 -loop 0\n*.png\n\"/Users/palmieri/.sage/sage_notebook/worksheets/admin/46/cells/37/\nsage0.gif\" \n```\n\nIn the discussion <http://groups.google.com/group/sage-support/browse_frm/thread/526afa1bcc4b7ad5>, it was suggested that 'sage-native-execute' should be used to run the 'convert' command, and this seems to fix the problems.\n\nPlease check this on several different platforms.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4216\n\n",
    "created_at": "2008-09-29T18:16:30Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] use sage-native-execute to run 'convert' in animate.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4216",
    "user": "jhpalmieri"
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

archive/issue_comments_030634.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-29T18:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4216#issuecomment-30634",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_030635.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-29T19:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4216#issuecomment-30635",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_030636.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-29T19:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4216#issuecomment-30636",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030637.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-29T19:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4216#issuecomment-30637",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_030638.json:
```json
{
    "body": "These are related: #3012 and #767",
    "created_at": "2008-09-29T22:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4216#issuecomment-30638",
    "user": "mhansen"
}
```

These are related: #3012 and #767
