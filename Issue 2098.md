# Issue 2098: [with patch; needs review] rudimentary debian package build support

archive/issues_002098.json:
```json
{
    "body": "Assignee: tabbott\n\nAdd spkg-build-debian, and hook it in to sage-spkg.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2098\n\n",
    "created_at": "2008-02-08T03:51:37Z",
    "labels": [
        "debian-package",
        "major",
        "enhancement"
    ],
    "title": "[with patch; needs review] rudimentary debian package build support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2098",
    "user": "tabbott"
}
```
Assignee: tabbott

Add spkg-build-debian, and hook it in to sage-spkg.

Issue created by migration from https://trac.sagemath.org/ticket/2098





---

archive/issue_comments_013569.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-08T03:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2098#issuecomment-13569",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_013570.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-08T21:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2098#issuecomment-13570",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_013571.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-10T02:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2098#issuecomment-13571",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_013572.json:
```json
{
    "body": "sage-build-debian will probably eventually want to look something like this.  I'm not applying it as a patch because it'll break the previous patchset:\n\nDEBIAN_REPO would be set to point to a temporary Debian repository that is in the approx sources.list for SAGE, so that each package has its dependencies uploaded to the test repo when it comes time to build it for Debian.\n\n#!/bin/sh -x\necho \"Starting Debian build\"\n[ -d dist/debian ] || exit 0 # exit cleanly for packages we're using the Debian versions of\nmv dist/debian src/\nsage-dasource src/\nsage-sbuildhack \"$DEBIAN_RELEASE\" *.dsc || exit 1\nmkdir -p $SAGE_ROOT/deb\nDEBIAN_ARCH=$(echo lenny-amd64 | cut -f 2 -d-)\nreprepro -b $DEBIAN_REPO --ignore=wrongdistribution include *_${DEBIAN_ARCH}.changes\nmv *.dsc *.changes *.build *.deb *.tar.gz *.diff.gz /deb\necho \"Debian Build complete\"",
    "created_at": "2008-02-10T03:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2098#issuecomment-13572",
    "user": "tabbott"
}
```

sage-build-debian will probably eventually want to look something like this.  I'm not applying it as a patch because it'll break the previous patchset:

DEBIAN_REPO would be set to point to a temporary Debian repository that is in the approx sources.list for SAGE, so that each package has its dependencies uploaded to the test repo when it comes time to build it for Debian.

#!/bin/sh -x
echo "Starting Debian build"
[ -d dist/debian ] || exit 0 # exit cleanly for packages we're using the Debian versions of
mv dist/debian src/
sage-dasource src/
sage-sbuildhack "$DEBIAN_RELEASE" *.dsc || exit 1
mkdir -p $SAGE_ROOT/deb
DEBIAN_ARCH=$(echo lenny-amd64 | cut -f 2 -d-)
reprepro -b $DEBIAN_REPO --ignore=wrongdistribution include *_${DEBIAN_ARCH}.changes
mv *.dsc *.changes *.build *.deb *.tar.gz *.diff.gz /deb
echo "Debian Build complete"



---

archive/issue_comments_013573.json:
```json
{
    "body": "The 5th patch is to the sage spkg, not sage_scripts.",
    "created_at": "2008-02-10T03:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2098#issuecomment-13573",
    "user": "tabbott"
}
```

The 5th patch is to the sage spkg, not sage_scripts.



---

archive/issue_comments_013574.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-10T03:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2098#issuecomment-13574",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_013575.json:
```json
{
    "body": "Patches look good to me. I sat next to Tim as he wrote most of the code, so maybe somebody else wants to take another look. In the end we might need to generalize the code a little more for other packaging systems.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T13:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2098#issuecomment-13575",
    "user": "mabshoff"
}
```

Patches look good to me. I sat next to Tim as he wrote most of the code, so maybe somebody else wants to take another look. In the end we might need to generalize the code a little more for other packaging systems.

Cheers,

Michael



---

archive/issue_comments_013576.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-14T15:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2098#issuecomment-13576",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013577.json:
```json
{
    "body": "Merged debian1.patch-debian5.patch in Sage 2.10.2.alpha0",
    "created_at": "2008-02-14T15:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2098#issuecomment-13577",
    "user": "mabshoff"
}
```

Merged debian1.patch-debian5.patch in Sage 2.10.2.alpha0



---

archive/issue_comments_013578.json:
```json
{
    "body": "Attachment\n\nThis patch is needed to make the non-Debianized build work again",
    "created_at": "2008-02-14T17:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2098#issuecomment-13578",
    "user": "mabshoff"
}
```

Attachment

This patch is needed to make the non-Debianized build work again
