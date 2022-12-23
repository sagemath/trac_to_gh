# Issue 2726: [with patch; needs review] SAGE debian build system update

archive/issues_002726.json:
```json
{
    "body": "Assignee: tabbott\n\nI've updated the SAGE Debian build system to support uploading to an apt repository as things build (so that the building of packages later in the build process can get their dependencies via apt).  Attached are the relevant patches.\n\nOne thing that's kinda annoying is that renaming SbuildHack.pm to sage-SbuildHack.pm was problematic because perl modules can't have dashes in their name.  We should figure out how to get SbuildHack.pm installed now that it's name doesn't start with sage.\n\nI'm trying to get a version of the code in SbuildHack.pm into mainline sbuild so that we don't need to bother with this, but am uncertain how long that will take.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2726\n\n",
    "created_at": "2008-03-29T22:15:57Z",
    "labels": [
        "debian-package",
        "major",
        "enhancement"
    ],
    "title": "[with patch; needs review] SAGE debian build system update",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2726",
    "user": "tabbott"
}
```
Assignee: tabbott

I've updated the SAGE Debian build system to support uploading to an apt repository as things build (so that the building of packages later in the build process can get their dependencies via apt).  Attached are the relevant patches.

One thing that's kinda annoying is that renaming SbuildHack.pm to sage-SbuildHack.pm was problematic because perl modules can't have dashes in their name.  We should figure out how to get SbuildHack.pm installed now that it's name doesn't start with sage.

I'm trying to get a version of the code in SbuildHack.pm into mainline sbuild so that we don't need to bother with this, but am uncertain how long that will take.

Issue created by migration from https://trac.sagemath.org/ticket/2726





---

archive/issue_comments_018781.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-29T22:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2726#issuecomment-18781",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_018782.json:
```json
{
    "body": "Attachment\n\nmake sure SbuildHack.pm gets copied by -sdist",
    "created_at": "2008-04-01T20:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2726#issuecomment-18782",
    "user": "mabshoff"
}
```

Attachment

make sure SbuildHack.pm gets copied by -sdist



---

archive/issue_comments_018783.json:
```json
{
    "body": "Attachment\n\nPatch looks good to me. My minimal patch makes sure that SbuildHack.pm is copied on `-sdist`\n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T20:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2726#issuecomment-18783",
    "user": "mabshoff"
}
```

Attachment

Patch looks good to me. My minimal patch makes sure that SbuildHack.pm is copied on `-sdist`

Cheers,

Michael



---

archive/issue_comments_018784.json:
```json
{
    "body": "Merged in Sage 3.0.alpha0",
    "created_at": "2008-04-01T20:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2726#issuecomment-18784",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha0



---

archive/issue_comments_018785.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T20:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2726#issuecomment-18785",
    "user": "mabshoff"
}
```

Resolution: fixed
