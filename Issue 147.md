# Issue 147: libgd build breaks on sage-1.4.1.2

archive/issues_000147.json:
```json
{
    "body": "Assignee: was\n\nThe build breaks here because of missing headerrs:\n\n    gcc -DHAVE_CONFIG_H -I. -I. -I. -I/SandBox/Justin/sb/sage-1.4/local//include/freetype2 \\\n         -I/SandBox/Justin/sb/sage-1.4/local//include -g -O2 -MT gdft.lo -MD -MP -MF \\\n         .deps/gdft.Tpo -c gdft.c  -fno-common -DPIC -o .libs/gdft.lo\n    gdft.c:1366:35: error: fontconfig/fontconfig.h: No such file or directory\n\nIssue created by migration from https://trac.sagemath.org/ticket/147\n\n",
    "created_at": "2006-10-21T20:51:54Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "libgd build breaks on sage-1.4.1.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/147",
    "user": "justin"
}
```
Assignee: was

The build breaks here because of missing headerrs:

    gcc -DHAVE_CONFIG_H -I. -I. -I. -I/SandBox/Justin/sb/sage-1.4/local//include/freetype2 \
         -I/SandBox/Justin/sb/sage-1.4/local//include -g -O2 -MT gdft.lo -MD -MP -MF \
         .deps/gdft.Tpo -c gdft.c  -fno-common -DPIC -o .libs/gdft.lo
    gdft.c:1366:35: error: fontconfig/fontconfig.h: No such file or directory

Issue created by migration from https://trac.sagemath.org/ticket/147





---

archive/issue_comments_000672.json:
```json
{
    "body": "Attachment\n\nbuild log for gd",
    "created_at": "2006-10-21T20:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/147#issuecomment-672",
    "user": "justin"
}
```

Attachment

build log for gd



---

archive/issue_comments_000673.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-12T23:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/147#issuecomment-673",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000674.json:
```json
{
    "body": "libgd is now a standard component of SAGE and builds everywhere...",
    "created_at": "2007-01-12T23:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/147#issuecomment-674",
    "user": "was"
}
```

libgd is now a standard component of SAGE and builds everywhere...
