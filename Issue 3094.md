# Issue 3094: [with patch; needs review] Update to SAGE Debian packaging

archive/issues_003094.json:
```json
{
    "body": "Assignee: tabbott\n\nThe attached patch updates the SAGE dist/debian/ from the extcode repository to work with polybori and zn_poly as separate packages, include a missing cddlib dependency, set SAGE_TESTDIR in the wrapper script, and various other minor fixes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3094\n\n",
    "created_at": "2008-05-03T08:28:33Z",
    "labels": [
        "debian-package",
        "blocker",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch; needs review] Update to SAGE Debian packaging",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3094",
    "user": "tabbott"
}
```
Assignee: tabbott

The attached patch updates the SAGE dist/debian/ from the extcode repository to work with polybori and zn_poly as separate packages, include a missing cddlib dependency, set SAGE_TESTDIR in the wrapper script, and various other minor fixes.

Issue created by migration from https://trac.sagemath.org/ticket/3094





---

archive/issue_comments_021356.json:
```json
{
    "body": "Attachment [sage-debian-package-3.0.1.patch](tarball://root/attachments/some-uuid/ticket3094/sage-debian-package-3.0.1.patch) by tabbott created at 2008-05-03 08:28:40",
    "created_at": "2008-05-03T08:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3094#issuecomment-21356",
    "user": "tabbott"
}
```

Attachment [sage-debian-package-3.0.1.patch](tarball://root/attachments/some-uuid/ticket3094/sage-debian-package-3.0.1.patch) by tabbott created at 2008-05-03 08:28:40



---

archive/issue_comments_021357.json:
```json
{
    "body": "I added a second patch that makes it so SAGE can find the cdd tests.",
    "created_at": "2008-05-03T08:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3094#issuecomment-21357",
    "user": "tabbott"
}
```

I added a second patch that makes it so SAGE can find the cdd tests.



---

archive/issue_comments_021358.json:
```json
{
    "body": "Attachment [sage-cdd-bin.patch](tarball://root/attachments/some-uuid/ticket3094/sage-cdd-bin.patch) by tabbott created at 2008-05-03 08:36:02",
    "created_at": "2008-05-03T08:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3094#issuecomment-21358",
    "user": "tabbott"
}
```

Attachment [sage-cdd-bin.patch](tarball://root/attachments/some-uuid/ticket3094/sage-cdd-bin.patch) by tabbott created at 2008-05-03 08:36:02



---

archive/issue_comments_021359.json:
```json
{
    "body": "I skimmed sage-debian-package-3.0.1.patch and it looks correct, but I am no expert there. sage-cdd-bin.patch looks good to me. Since this patch only potentially breaks the Debian build and Tim will fix it himself positive review. It would be great if we could get more people from the Debian community to increase the bus factor on the Debian packaging.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T14:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3094#issuecomment-21359",
    "user": "mabshoff"
}
```

I skimmed sage-debian-package-3.0.1.patch and it looks correct, but I am no expert there. sage-cdd-bin.patch looks good to me. Since this patch only potentially breaks the Debian build and Tim will fix it himself positive review. It would be great if we could get more people from the Debian community to increase the bus factor on the Debian packaging.

Cheers,

Michael



---

archive/issue_comments_021360.json:
```json
{
    "body": "Merged in Sage 3.0.1.final",
    "created_at": "2008-05-03T14:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3094#issuecomment-21360",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.final



---

archive/issue_comments_021361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-03T14:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3094#issuecomment-21361",
    "user": "mabshoff"
}
```

Resolution: fixed
