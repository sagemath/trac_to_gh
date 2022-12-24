# Issue 4657: OSXL: gnuplot doesn't start due to dreaded libpng conflict

archive/issues_004657.json:
```json
{
    "body": "Assignee: mabshoff\n\nIn http://groups.google.com/group/sage-support/browse_thread/thread/9b61a7cf8fbfac7a Wayne reported:\n\n```\n/WW/Projects/Heart/bash$sage \n---------------------------------------------------------------------- \n---------------------------------------------------------------------- \nsage: gnuplot_console() \ndyld: Symbol not found: __cg_png_create_info_struct \n  Referenced from: /System/Library/Frameworks/ \nApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/ \nVersions/A/ImageIO \n  Expected in: /Users/ww/Applications/Scientific/sage/local/lib// \nlibpng12.0.dylib \nsage: \n```\n\n| Sage Version 3.2, Release Date: 2008-11-20                         | \n| Type notebook() for the GUI, and license() for information.        | \nThe fix should be obvious by now.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4657\n\n",
    "created_at": "2008-11-29T22:13:41Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "OSXL: gnuplot doesn't start due to dreaded libpng conflict",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4657",
    "user": "mabshoff"
}
```
Assignee: mabshoff

In http://groups.google.com/group/sage-support/browse_thread/thread/9b61a7cf8fbfac7a Wayne reported:

```
/WW/Projects/Heart/bash$sage 
---------------------------------------------------------------------- 
---------------------------------------------------------------------- 
sage: gnuplot_console() 
dyld: Symbol not found: __cg_png_create_info_struct 
  Referenced from: /System/Library/Frameworks/ 
ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/ 
Versions/A/ImageIO 
  Expected in: /Users/ww/Applications/Scientific/sage/local/lib// 
libpng12.0.dylib 
sage: 
```

| Sage Version 3.2, Release Date: 2008-11-20                         | 
| Type notebook() for the GUI, and license() for information.        | 
The fix should be obvious by now.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4657





---

archive/issue_comments_035083.json:
```json
{
    "body": "Attachment [trac_4657.patch](tarball://root/attachments/some-uuid/ticket4657/trac_4657.patch) by mabshoff created at 2008-11-29 22:33:24",
    "created_at": "2008-11-29T22:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4657#issuecomment-35083",
    "user": "mabshoff"
}
```

Attachment [trac_4657.patch](tarball://root/attachments/some-uuid/ticket4657/trac_4657.patch) by mabshoff created at 2008-11-29 22:33:24



---

archive/issue_comments_035084.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-29T22:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4657#issuecomment-35084",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035085.json:
```json
{
    "body": "The problem only manifests itself when using a system wide gnuplot, i.e. for example a Fink one. The patch should fix that. The experimental gnuplot-4.0.0.spkg in our repo is currently slightly broken on OSX since it calls Emacs at some point and then blows up due to the same libpng issues. Oh well ...\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T22:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4657#issuecomment-35085",
    "user": "mabshoff"
}
```

The problem only manifests itself when using a system wide gnuplot, i.e. for example a Fink one. The patch should fix that. The experimental gnuplot-4.0.0.spkg in our repo is currently slightly broken on OSX since it calls Emacs at some point and then blows up due to the same libpng issues. Oh well ...

Cheers,

Michael



---

archive/issue_comments_035086.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1",
    "created_at": "2008-11-30T05:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4657#issuecomment-35086",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc1



---

archive/issue_comments_035087.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-30T05:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4657#issuecomment-35087",
    "user": "mabshoff"
}
```

Resolution: fixed
