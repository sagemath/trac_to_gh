# Issue 2830: ace-5.0.spkg fails to install

archive/issues_002830.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe optional ace-5.0.spkg for the GAP component fails to install.  It tries to copy itself into the non-existent directory of GAP version 4.4.9 instead of the current version 4.4.10.\n\nThis can be fixed by changing line 3 of the spkg-install file to:\n\n\n```\nDEST=\"$SAGE_LOCAL\"/lib/gap-4.4.10/pkg/\n```\n\n\nHowever, as mabshoff says:\n\n''The proper fix in this  would be to use a variety of \"newest_version\". Right now it doesn't \nreturn the proper version you need: ''\n\n\n```\n$SAGE_ROOT/spkg/standard$ ./newest_version gap \ngap-4.4.10.p5 \n```\n\n*but after some discussion in debian-sage it now seems likely that we will switch to dashes for the patch level. *\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2830\n\n",
    "created_at": "2008-04-06T14:31:03Z",
    "labels": [
        "packages: optional",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "ace-5.0.spkg fails to install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2830",
    "user": "dunfield"
}
```
Assignee: mabshoff

The optional ace-5.0.spkg for the GAP component fails to install.  It tries to copy itself into the non-existent directory of GAP version 4.4.9 instead of the current version 4.4.10.

This can be fixed by changing line 3 of the spkg-install file to:


```
DEST="$SAGE_LOCAL"/lib/gap-4.4.10/pkg/
```


However, as mabshoff says:

''The proper fix in this  would be to use a variety of "newest_version". Right now it doesn't 
return the proper version you need: ''


```
$SAGE_ROOT/spkg/standard$ ./newest_version gap 
gap-4.4.10.p5 
```

*but after some discussion in debian-sage it now seems likely that we will switch to dashes for the patch level. *


Issue created by migration from https://trac.sagemath.org/ticket/2830





---

archive/issue_comments_019425.json:
```json
{
    "body": "I have uploaded a slightly updated spkg into the repo. It adds a mercurial repo and an .hgignore file. I also renamed it to ace-5.0.p0.spkg since changes to existing packages need to increment the patch level. Otherwise updates are not installed.\n\nThe new spkg installs, so positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T15:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2830#issuecomment-19425",
    "user": "mabshoff"
}
```

I have uploaded a slightly updated spkg into the repo. It adds a mercurial repo and an .hgignore file. I also renamed it to ace-5.0.p0.spkg since changes to existing packages need to increment the patch level. Otherwise updates are not installed.

The new spkg installs, so positive review.

Cheers,

Michael



---

archive/issue_comments_019426.json:
```json
{
    "body": "Merged into the package repo and mirrored out.",
    "created_at": "2008-04-06T15:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2830#issuecomment-19426",
    "user": "mabshoff"
}
```

Merged into the package repo and mirrored out.



---

archive/issue_comments_019427.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T15:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2830#issuecomment-19427",
    "user": "mabshoff"
}
```

Resolution: fixed
