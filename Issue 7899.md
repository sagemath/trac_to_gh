# Issue 7899: Remove variable names like $LN, $MKDIR etc in ntl

archive/issues_007899.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  jsp jhpalmieri\n\nIt was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.\n\n http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot\n\n#7818 usets these, so this package will break. The fix is to simply replace things like\n\n$LN with 'ln'\n\nAn updated .spkg can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/ntl-5.4.2.p10/ntl-5.4.2.p10.spkg\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7899\n\n",
    "created_at": "2010-01-12T03:55:50Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Remove variable names like $LN, $MKDIR etc in ntl",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7899",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  jsp jhpalmieri

It was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.

 http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

#7818 usets these, so this package will break. The fix is to simply replace things like

$LN with 'ln'

An updated .spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/ntl-5.4.2.p10/ntl-5.4.2.p10.spkg



Issue created by migration from https://trac.sagemath.org/ticket/7899





---

archive/issue_comments_068704.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T03:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7899#issuecomment-68704",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068705.json:
```json
{
    "body": "Attachment [ntl-variables-to-commands.patch](tarball://root/attachments/some-uuid/ticket7899/ntl-variables-to-commands.patch) by drkirkby created at 2010-01-12 03:57:09",
    "created_at": "2010-01-12T03:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7899#issuecomment-68705",
    "user": "drkirkby"
}
```

Attachment [ntl-variables-to-commands.patch](tarball://root/attachments/some-uuid/ticket7899/ntl-variables-to-commands.patch) by drkirkby created at 2010-01-12 03:57:09



---

archive/issue_comments_068706.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T11:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7899#issuecomment-68706",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068707.json:
```json
{
    "body": "The new spkg looks good. Positive review.\n\nJaap",
    "created_at": "2010-01-12T11:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7899#issuecomment-68707",
    "user": "jsp"
}
```

The new spkg looks good. Positive review.

Jaap



---

archive/issue_comments_068708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T02:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7899#issuecomment-68708",
    "user": "rlm"
}
```

Resolution: fixed
