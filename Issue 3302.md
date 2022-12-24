# Issue 3302: python_gnutls fails to upgrade on OSX in case Sage was moved

archive/issues_003302.json:
```json
{
    "body": "Assignee: mabshoff\n\nOk, you seem to have moved the Sage install from\n\n    /Users/saliola/Desktop/sage-3.0.1/\n\nto\n\n    /Users/saliola/sage-3.0.1/\n\nConsequently the linker does not find some libraries:\n\n/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: warning can't open dynamic library: /Users/saliola/Desktop/sage-3.0.1/local/lib/libgpg-error.0.dylib referenced from: /Users/saliola/sage-3.0.1/local/lib//libgcrypt.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)\n/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: warning can't open dynamic library: /Users/saliola/Desktop/sage-3.0.1/local/lib/libz.1.dylib referenced from: /Users/saliola/sage-3.0.1/local/lib//libgnutls.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)\n/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: warning can't open dynamic library: /Users/saliola/Desktop/sage-3.0.1/local/lib/libopencdk.10.dylib referenced from: /Users/saliola/sage-3.0.1/local/lib//libgnutls-extra.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)\n\n\nThis can probably be fixed by adding \"-L$SAGE_LOCAL/lib\" to the build flags.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3302\n\n",
    "created_at": "2008-05-25T20:54:34Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "python_gnutls fails to upgrade on OSX in case Sage was moved",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3302",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Ok, you seem to have moved the Sage install from

    /Users/saliola/Desktop/sage-3.0.1/

to

    /Users/saliola/sage-3.0.1/

Consequently the linker does not find some libraries:

/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: warning can't open dynamic library: /Users/saliola/Desktop/sage-3.0.1/local/lib/libgpg-error.0.dylib referenced from: /Users/saliola/sage-3.0.1/local/lib//libgcrypt.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: warning can't open dynamic library: /Users/saliola/Desktop/sage-3.0.1/local/lib/libz.1.dylib referenced from: /Users/saliola/sage-3.0.1/local/lib//libgnutls.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: warning can't open dynamic library: /Users/saliola/Desktop/sage-3.0.1/local/lib/libopencdk.10.dylib referenced from: /Users/saliola/sage-3.0.1/local/lib//libgnutls-extra.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)


This can probably be fixed by adding "-L$SAGE_LOCAL/lib" to the build flags.




Issue created by migration from https://trac.sagemath.org/ticket/3302





---

archive/issue_comments_022843.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-10-05T09:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3302#issuecomment-22843",
    "user": "@jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_022844.json:
```json
{
    "body": "GNUTLS is no longer part of Sage.",
    "created_at": "2012-10-05T09:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3302#issuecomment-22844",
    "user": "@jdemeyer"
}
```

GNUTLS is no longer part of Sage.
