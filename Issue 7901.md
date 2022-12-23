# Issue 7901: Change $MKDIR to 'mkdir' in pari

archive/issues_007901.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  jsp jhpalmieri\n\nIt was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.\n\n     http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot\n\n#7818 usets these, so this package may break. The fix is to simply replace $MKDIR with 'mkdir' in spkg-install. \n\nAn updated .spkg can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/pari-2.3.3.p7/ari-2.3.3.p7.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/7901\n\n",
    "created_at": "2010-01-12T04:33:03Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Change $MKDIR to 'mkdir' in pari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7901",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  jsp jhpalmieri

It was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.

     http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

#7818 usets these, so this package may break. The fix is to simply replace $MKDIR with 'mkdir' in spkg-install. 

An updated .spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/pari-2.3.3.p7/ari-2.3.3.p7.spkg

Issue created by migration from https://trac.sagemath.org/ticket/7901





---

archive/issue_comments_068714.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T04:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7901#issuecomment-68714",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068715.json:
```json
{
    "body": "The patch of spkg-install looks ok. Maybe the SPKG.txt should be brought up to date.\n\nSee also: [http://trac.sagemath.org/sage_trac/ticket/7738](http://trac.sagemath.org/sage_trac/ticket/7738)\n\nDave, can you fix that?\n\nJaap",
    "created_at": "2010-01-12T10:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7901#issuecomment-68715",
    "user": "jsp"
}
```

The patch of spkg-install looks ok. Maybe the SPKG.txt should be brought up to date.

See also: [http://trac.sagemath.org/sage_trac/ticket/7738](http://trac.sagemath.org/sage_trac/ticket/7738)

Dave, can you fix that?

Jaap



---

archive/issue_comments_068716.json:
```json
{
    "body": "OK I've recreated the spkg, which again can be found at http://boxen.math.washington.edu/home/kirkby/portability/pari-2.3.3.p7/pari-2.3.3.p7.spkg Please check it again. \n\nI've attached the Mercurial patch, which overwrites the old one.",
    "created_at": "2010-01-12T16:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7901#issuecomment-68716",
    "user": "drkirkby"
}
```

OK I've recreated the spkg, which again can be found at http://boxen.math.washington.edu/home/kirkby/portability/pari-2.3.3.p7/pari-2.3.3.p7.spkg Please check it again. 

I've attached the Mercurial patch, which overwrites the old one.



---

archive/issue_comments_068717.json:
```json
{
    "body": "Attachment\n\nUpdated patch to fix spkg-install and SPKG.txt",
    "created_at": "2010-01-12T16:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7901#issuecomment-68717",
    "user": "drkirkby"
}
```

Attachment

Updated patch to fix spkg-install and SPKG.txt



---

archive/issue_comments_068718.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T17:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7901#issuecomment-68718",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068719.json:
```json
{
    "body": "All fixed. Positive review.\n\nJaap",
    "created_at": "2010-01-12T17:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7901#issuecomment-68719",
    "user": "jsp"
}
```

All fixed. Positive review.

Jaap



---

archive/issue_comments_068720.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T03:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7901#issuecomment-68720",
    "user": "rlm"
}
```

Resolution: fixed
