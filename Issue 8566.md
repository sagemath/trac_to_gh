# Issue 8566: Upate prereq to 0.8, removing 'm' option from 'tar'

archive/issues_008566.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nAs reported on sage-support:\n\nhttp://groups.google.com/group/sage-support/msg/c636e1b5b820eb19\n\nthe 'm' option to tar used in prereq is causing a problem on a minimal linux system, as no such option is supported. The option seems to be unnecessary, as Sage seems to build fine without this option, which is only to 'touch' the files. I don't see this being necessary. \n\nI'll update the prereq script, to remove the option - a simple one-byte change. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8566\n\n",
    "created_at": "2010-03-20T11:00:49Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Upate prereq to 0.8, removing 'm' option from 'tar'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8566",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

As reported on sage-support:

http://groups.google.com/group/sage-support/msg/c636e1b5b820eb19

the 'm' option to tar used in prereq is causing a problem on a minimal linux system, as no such option is supported. The option seems to be unnecessary, as Sage seems to build fine without this option, which is only to 'touch' the files. I don't see this being necessary. 

I'll update the prereq script, to remove the option - a simple one-byte change. 


Issue created by migration from https://trac.sagemath.org/ticket/8566





---

archive/issue_comments_077550.json:
```json
{
    "body": "Attachment [prereq-0.8.tar](tarball://root/attachments/some-uuid/ticket8566/prereq-0.8.tar) by drkirkby created at 2010-04-03 16:56:38\n\nprereq 0.8 tar file - unchanged from 0.7, except directory name",
    "created_at": "2010-04-03T16:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8566#issuecomment-77550",
    "user": "drkirkby"
}
```

Attachment [prereq-0.8.tar](tarball://root/attachments/some-uuid/ticket8566/prereq-0.8.tar) by drkirkby created at 2010-04-03 16:56:38

prereq 0.8 tar file - unchanged from 0.7, except directory name



---

archive/issue_comments_077551.json:
```json
{
    "body": "Attachment [prereq-0.8-install](tarball://root/attachments/some-uuid/ticket8566/prereq-0.8-install) by drkirkby created at 2010-04-03 16:57:33\n\nprereq 0.8 script - removes 'm' option to 'tar'",
    "created_at": "2010-04-03T16:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8566#issuecomment-77551",
    "user": "drkirkby"
}
```

Attachment [prereq-0.8-install](tarball://root/attachments/some-uuid/ticket8566/prereq-0.8-install) by drkirkby created at 2010-04-03 16:57:33

prereq 0.8 script - removes 'm' option to 'tar'



---

archive/issue_comments_077552.json:
```json
{
    "body": "this is dealt with in #11280",
    "created_at": "2011-05-06T16:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8566#issuecomment-77552",
    "user": "dimpase"
}
```

this is dealt with in #11280



---

archive/issue_comments_077553.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-06T16:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8566#issuecomment-77553",
    "user": "dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077554.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-05-09T09:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8566#issuecomment-77554",
    "user": "jdemeyer"
}
```

Resolution: duplicate
