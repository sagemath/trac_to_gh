# Issue 7899: Remove variable names like $LN, $MKDIR etc in ntl

archive/issues_007899.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jaapspies @jhpalmieri\n\nIt was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.\n\n http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot\n\n#7818 usets these, so this package will break. The fix is to simply replace things like\n\n$LN with 'ln'\n\nAn updated .spkg can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/ntl-5.4.2.p10/ntl-5.4.2.p10.spkg\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7899\n\n",
    "created_at": "2010-01-12T03:55:50Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Remove variable names like $LN, $MKDIR etc in ntl",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7899",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jaapspies @jhpalmieri

It was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.

 http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

#7818 usets these, so this package will break. The fix is to simply replace things like

$LN with 'ln'

An updated .spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/ntl-5.4.2.p10/ntl-5.4.2.p10.spkg



Issue created by migration from https://trac.sagemath.org/ticket/7899





---

archive/issue_comments_068585.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T03:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7899#issuecomment-68585",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068586.json:
```json
{
    "body": "Attachment [ntl-variables-to-commands.patch](tarball://root/attachments/some-uuid/ticket7899/ntl-variables-to-commands.patch) by drkirkby created at 2010-01-12 03:57:09",
    "created_at": "2010-01-12T03:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7899#issuecomment-68586",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [ntl-variables-to-commands.patch](tarball://root/attachments/some-uuid/ticket7899/ntl-variables-to-commands.patch) by drkirkby created at 2010-01-12 03:57:09



---

archive/issue_comments_068587.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T11:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7899#issuecomment-68587",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068588.json:
```json
{
    "body": "The new spkg looks good. Positive review.\n\nJaap",
    "created_at": "2010-01-12T11:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7899#issuecomment-68588",
    "user": "https://github.com/jaapspies"
}
```

The new spkg looks good. Positive review.

Jaap



---

archive/issue_comments_068589.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T02:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7899#issuecomment-68589",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
