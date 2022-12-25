# Issue 8737: compile plot3d/base.pyx and index_face_set with "-std=c99"

archive/issues_008737.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @robertwb @robert-marik drkirkby mvngu\n\nThis is a followup to [http://trac.sagemath.org/sage_trac/ticket/8424#comment:5](http://trac.sagemath.org/sage_trac/ticket/8424#comment:5).  Without this patch, the Sage library (as of 4.4.alpha0) doesn't build on t2.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8737\n\n",
    "created_at": "2010-04-21T15:25:00Z",
    "labels": [
        "component: graphics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "compile plot3d/base.pyx and index_face_set with \"-std=c99\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8737",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: jason, was

CC:  @robertwb @robert-marik drkirkby mvngu

This is a followup to [http://trac.sagemath.org/sage_trac/ticket/8424#comment:5](http://trac.sagemath.org/sage_trac/ticket/8424#comment:5).  Without this patch, the Sage library (as of 4.4.alpha0) doesn't build on t2.


Issue created by migration from https://trac.sagemath.org/ticket/8737





---

archive/issue_comments_079780.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-21T18:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79780",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079781.json:
```json
{
    "body": "Nearly every instance of `-std=c99` is also paired with `-D_XPG6`. I'm honestly unsure as to why, but if we don't we should justify it.",
    "created_at": "2010-04-21T18:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79781",
    "user": "https://github.com/robertwb"
}
```

Nearly every instance of `-std=c99` is also paired with `-D_XPG6`. I'm honestly unsure as to why, but if we don't we should justify it.



---

archive/issue_comments_079782.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n> Nearly every instance of `-std=c99` is also paired with `-D_XPG6`. I'm honestly unsure as to why, but if we don't we should justify it. \n\nIt looks like about half of them have `-D_XPG6`.  I can't really tell what this flag means (except something about \"issue 6 of the X/Open Portability Guide\"), so I have no idea if it's a good idea.  Without it for these two pyx files, the Sage library builds on t2, for what that's worth.",
    "created_at": "2010-04-21T18:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79782",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:2 robertwb]:
> Nearly every instance of `-std=c99` is also paired with `-D_XPG6`. I'm honestly unsure as to why, but if we don't we should justify it. 

It looks like about half of them have `-D_XPG6`.  I can't really tell what this flag means (except something about "issue 6 of the X/Open Portability Guide"), so I have no idea if it's a good idea.  Without it for these two pyx files, the Sage library builds on t2, for what that's worth.



---

archive/issue_comments_079783.json:
```json
{
    "body": "I would rephrase the question and ask why are people adding -D_XPG6? Can they justify it? \n\nWe can justify adding -std=c99, as we want to make use of a feature that was not defined until the C99 standard.  I don't know of any justification for adding -D_XPG6. (That is not to say there is not any, but I think the onus should be on someone who adds -D_XPG6 to justify why they add it.) \n\nThere are quite a few bits of code in Sage which appear to be added just because someone else did so before, without anyone understanding why they did it. One sees things like \n\n\n```\npath=\"$SAGE_LOCAL\"/bin\n```\n\n\nwhen it should be:\n\n```\npath=\"$SAGE_LOCAL/bin\"\n```\n\nI suspect people are just cutting/pasting without any understanding. \n\nI think it is better to just leave it as -std=c99, until such time as someone can justify why -D_XPG6 is best added. \n\nPlease note, I'm not saying -D_XPG6 might not be right, but only that I'd rather not add things we don't understand. \n\nDave",
    "created_at": "2010-04-21T23:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79783",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I would rephrase the question and ask why are people adding -D_XPG6? Can they justify it? 

We can justify adding -std=c99, as we want to make use of a feature that was not defined until the C99 standard.  I don't know of any justification for adding -D_XPG6. (That is not to say there is not any, but I think the onus should be on someone who adds -D_XPG6 to justify why they add it.) 

There are quite a few bits of code in Sage which appear to be added just because someone else did so before, without anyone understanding why they did it. One sees things like 


```
path="$SAGE_LOCAL"/bin
```


when it should be:

```
path="$SAGE_LOCAL/bin"
```

I suspect people are just cutting/pasting without any understanding. 

I think it is better to just leave it as -std=c99, until such time as someone can justify why -D_XPG6 is best added. 

Please note, I'm not saying -D_XPG6 might not be right, but only that I'd rather not add things we don't understand. 

Dave



---

archive/issue_comments_079784.json:
```json
{
    "body": "Changing assignee from jason, was to drkirkby.",
    "created_at": "2010-04-21T23:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79784",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from jason, was to drkirkby.



---

archive/issue_comments_079785.json:
```json
{
    "body": "The first time it popped up was for FLINT: \n\nhttp://hg.sagemath.org/sage-main/diff/89003ef36bd6/setup.py",
    "created_at": "2010-04-21T23:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79785",
    "user": "https://github.com/robertwb"
}
```

The first time it popped up was for FLINT: 

http://hg.sagemath.org/sage-main/diff/89003ef36bd6/setup.py



---

archive/issue_comments_079786.json:
```json
{
    "body": "I'm having the same problem with the file chmm.pyx, with the same solution.  So I'm adding it to this patch.",
    "created_at": "2010-04-22T02:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79786",
    "user": "https://github.com/jhpalmieri"
}
```

I'm having the same problem with the file chmm.pyx, with the same solution.  So I'm adding it to this patch.



---

archive/issue_comments_079787.json:
```json
{
    "body": "Attachment [trac_8737-std-c99.patch](tarball://root/attachments/some-uuid/ticket8737/trac_8737-std-c99.patch) by @jhpalmieri created at 2010-04-22 02:18:49",
    "created_at": "2010-04-22T02:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79787",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8737-std-c99.patch](tarball://root/attachments/some-uuid/ticket8737/trac_8737-std-c99.patch) by @jhpalmieri created at 2010-04-22 02:18:49



---

archive/issue_comments_079788.json:
```json
{
    "body": "I should say, it's not exactly the same problem with chmm.pyx: the Sage library seems to build successfully, and indeed the Sage build completes without complaint, but Sage won't start up: it gives errors about `isfinite` and the file `chmm.so`.",
    "created_at": "2010-04-22T02:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79788",
    "user": "https://github.com/jhpalmieri"
}
```

I should say, it's not exactly the same problem with chmm.pyx: the Sage library seems to build successfully, and indeed the Sage build completes without complaint, but Sage won't start up: it gives errors about `isfinite` and the file `chmm.so`.



---

archive/issue_comments_079789.json:
```json
{
    "body": "Regarding chmm: That makes sense, because I use isfinite in chmm.pyx:\n\n```\ncdef extern from \"math.h\":\n    double log(double)\n    double sqrt(double)\n    double exp(double)\n    int isnormal(double)\n    int isfinite(double)\n```\n\n\nSo I'm fine with building it with c99.\n\nWilliam",
    "created_at": "2010-04-22T02:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79789",
    "user": "https://github.com/williamstein"
}
```

Regarding chmm: That makes sense, because I use isfinite in chmm.pyx:

```
cdef extern from "math.h":
    double log(double)
    double sqrt(double)
    double exp(double)
    int isnormal(double)
    int isfinite(double)
```


So I'm fine with building it with c99.

William



---

archive/issue_comments_079790.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-22T22:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79790",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079791.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-23T17:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79791",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_079792.json:
```json
{
    "body": "Merged into 4.4.alpha2.",
    "created_at": "2010-04-23T17:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8737#issuecomment-79792",
    "user": "https://github.com/jhpalmieri"
}
```

Merged into 4.4.alpha2.
