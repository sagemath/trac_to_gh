# Issue 4729: fix gnuplot execution issue

archive/issues_004729.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe patch for #4657 did *not* fix the problem reported by the user, and shouldn't have got a positive review.  From the user:\n\n```\n\n~/bash$sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2.1, Release Date: 2008-12-01                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: gnuplot_console()\ndyld: Symbol not found: __cg_png_create_info_struct\n Referenced from: /System/Library/Frameworks/\nApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/\nVersions/A/ImageIO\n Expected in: /Users/ww/Applications/Scientific/sage/local/lib//\nlibpng12.0.dylib\n\nOnly one function in gnuplot.py -- interact -- was fixed. However, the\ngnuplot_console() function needs it too. It should read:\n\ndef gnuplot_console():\n   os.system('sage-native-execute gnuplot')\n\nWith that fix, gnuplot_console() now works for me.\n\nWayne\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4729\n\n",
    "created_at": "2008-12-06T20:56:03Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "fix gnuplot execution issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4729",
    "user": "@williamstein"
}
```
Assignee: @williamstein

The patch for #4657 did *not* fix the problem reported by the user, and shouldn't have got a positive review.  From the user:

```

~/bash$sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.1, Release Date: 2008-12-01                       |
| Type notebook() for the GUI, and license() for information.        |
sage: gnuplot_console()
dyld: Symbol not found: __cg_png_create_info_struct
 Referenced from: /System/Library/Frameworks/
ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/
Versions/A/ImageIO
 Expected in: /Users/ww/Applications/Scientific/sage/local/lib//
libpng12.0.dylib

Only one function in gnuplot.py -- interact -- was fixed. However, the
gnuplot_console() function needs it too. It should read:

def gnuplot_console():
   os.system('sage-native-execute gnuplot')

With that fix, gnuplot_console() now works for me.

Wayne
```


Issue created by migration from https://trac.sagemath.org/ticket/4729





---

archive/issue_comments_035699.json:
```json
{
    "body": "Attachment [trac_4729.patch](tarball://root/attachments/some-uuid/ticket4729/trac_4729.patch) by @williamstein created at 2008-12-06 20:57:43",
    "created_at": "2008-12-06T20:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4729#issuecomment-35699",
    "user": "@williamstein"
}
```

Attachment [trac_4729.patch](tarball://root/attachments/some-uuid/ticket4729/trac_4729.patch) by @williamstein created at 2008-12-06 20:57:43



---

archive/issue_comments_035700.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-07T00:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4729#issuecomment-35700",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_035701.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha1",
    "created_at": "2008-12-07T09:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4729#issuecomment-35701",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha1



---

archive/issue_comments_035702.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-07T09:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4729#issuecomment-35702",
    "user": "mabshoff"
}
```

Resolution: fixed
