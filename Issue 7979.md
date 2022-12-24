# Issue 7979: pari-2.3.3 sometimes ignores --graphic=none build option

archive/issues_007979.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  jsp\n\npdehaye reported a build error in pari on IRC.\n\nWe tracked this down to what seems to be a bug in pari's Configure script (or rather config/get_fltk): if X11 is not found, and fltk is found, it ignores the --graphic=none option. It then tries to build with fltk support, and fails spectacularly.\n\n(Aside: pari-2.4.2.alpha still has the same logic in config/get_fltk.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7979\n\n",
    "created_at": "2010-01-18T17:48:44Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "pari-2.3.3 sometimes ignores --graphic=none build option",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7979",
    "user": "wjp"
}
```
Assignee: GeorgSWeber

CC:  jsp

pdehaye reported a build error in pari on IRC.

We tracked this down to what seems to be a bug in pari's Configure script (or rather config/get_fltk): if X11 is not found, and fltk is found, it ignores the --graphic=none option. It then tries to build with fltk support, and fails spectacularly.

(Aside: pari-2.4.2.alpha still has the same logic in config/get_fltk.)

Issue created by migration from https://trac.sagemath.org/ticket/7979





---

archive/issue_comments_069613.json:
```json
{
    "body": "Attachment [pari_fltk.patch](tarball://root/attachments/some-uuid/ticket7979/pari_fltk.patch) by wjp created at 2010-01-18 18:21:12\n\nI contacted Karim Belabas about this, suggesting the attached patch to pari's `config/get_fltk`.",
    "created_at": "2010-01-18T18:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7979#issuecomment-69613",
    "user": "wjp"
}
```

Attachment [pari_fltk.patch](tarball://root/attachments/some-uuid/ticket7979/pari_fltk.patch) by wjp created at 2010-01-18 18:21:12

I contacted Karim Belabas about this, suggesting the attached patch to pari's `config/get_fltk`.



---

archive/issue_comments_069614.json:
```json
{
    "body": "Updated spkg is up at\n\nhttp://boxen.math.washington.edu/home/mvngu/spkg/standard/pari/pari-2.3.3.p8.spkg\n\nThis has Willem's patch for `src/config/get_fltk`. This spkg might need to be based on that at #8099.",
    "created_at": "2010-02-02T17:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7979#issuecomment-69614",
    "user": "mvngu"
}
```

Updated spkg is up at

http://boxen.math.washington.edu/home/mvngu/spkg/standard/pari/pari-2.3.3.p8.spkg

This has Willem's patch for `src/config/get_fltk`. This spkg might need to be based on that at #8099.



---

archive/issue_comments_069615.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-02T17:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7979#issuecomment-69615",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069616.json:
```json
{
    "body": "Ticket #8453 upgrades Pari to version 2.3.5, so this ticket is no longer relevant. So I'm closing this ticket as \"wontfix\". However, the file `config/get_fltk` in Pari 2.3.5 has the same logic as in Pari 2.3.3 so it's possible that Pari 2.3.5 also ignores the build option \"--graphic=none\". If that issue comes up, open another ticket to patch Pari 2.3.5 for Sage.",
    "created_at": "2010-04-29T06:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7979#issuecomment-69616",
    "user": "mvngu"
}
```

Ticket #8453 upgrades Pari to version 2.3.5, so this ticket is no longer relevant. So I'm closing this ticket as "wontfix". However, the file `config/get_fltk` in Pari 2.3.5 has the same logic as in Pari 2.3.3 so it's possible that Pari 2.3.5 also ignores the build option "--graphic=none". If that issue comes up, open another ticket to patch Pari 2.3.5 for Sage.



---

archive/issue_comments_069617.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-04-29T06:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7979#issuecomment-69617",
    "user": "mvngu"
}
```

Resolution: wontfix
