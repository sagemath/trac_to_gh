# Issue 9464: R depends on Fortran, but has no such dependancy in spkg/standard/deps

archive/issues_009464.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @rlmill @jhpalmieri @qed777\n\nIn the sage-4.5.alpha4 code, the $SAGE_ROOT/spkg/standard/deps file has this entry for R:\n\n\n```\n$(INST)/$(R): $(BASE) $(INST)/$(PYTHON) $(INST)/$(ATLAS) $(INST)/$(ICONV)\n        $(INSTALL) \"$(SAGE_SPKG) $(R) 2>&1\" \"tee -a $(SAGE_LOGS)/$(R).log\"\n```\n\n\nNote, there is no Fortran dependency listed, yet R does have Fortran files:\n\n\n```\ndrkirkby@hawk:~/sage-4.5.alpha4/spkg/standard$ find r-2.10.1.p2 -name '*.f'\nr-2.10.1.p2/src/src/library/stats/src/stxwx.f\nr-2.10.1.p2/src/src/library/stats/src/sgram.f\nr-2.10.1.p2/src/src/library/stats/src/bsplvd.f\nr-2.10.1.p2/src/src/library/stats/src/stl.f\nr-2.10.1.p2/src/src/library/stats/src/hclust.f\nr-2.10.1.p2/src/src/library/stats/src/sslvrg.f\nr-2.10.1.p2/src/src/library/stats/src/qsbart.f\nr-2.10.1.p2/src/src/library/stats/src/bvalue.f\nr-2.10.1.p2/src/src/library/stats/src/loessf.f\nr-2.10.1.p2/src/src/library/stats/src/lminfl.f\nr-2.10.1.p2/src/src/library/stats/src/kmns.f\nr-2.10.1.p2/src/src/library/stats/src/eureka.f\nr-2.10.1.p2/src/src/library/stats/src/sinerp.f\nr-2.10.1.p2/src/src/library/stats/src/bvalus.f\nr-2.10.1.p2/src/src/library/stats/src/ppr.f\nr-2.10.1.p2/src/src/library/stats/src/portsrc.f\nr-2.10.1.p2/src/src/appl/dchdc.f\nr-2.10.1.p2/src/src/appl/chol.f\nr-2.10.1.p2/src/src/appl/dqrsl.f\nr-2.10.1.p2/src/src/appl/dqrdc2.f\nr-2.10.1.p2/src/src/appl/eigen.f\nr-2.10.1.p2/src/src/appl/dpoco.f\nr-2.10.1.p2/src/src/appl/dposl.f\nr-2.10.1.p2/src/src/appl/dpbfa.f\nr-2.10.1.p2/src/src/appl/dtrco.f\nr-2.10.1.p2/src/src/appl/dtrsl.f\nr-2.10.1.p2/src/src/appl/ch2inv.f\nr-2.10.1.p2/src/src/appl/dpofa.f\nr-2.10.1.p2/src/src/appl/dqrutl.f\nr-2.10.1.p2/src/src/appl/dqrdc.f\nr-2.10.1.p2/src/src/appl/dpbsl.f\nr-2.10.1.p2/src/src/appl/dpodi.f\nr-2.10.1.p2/src/src/appl/dqrls.f\nr-2.10.1.p2/src/src/appl/dsvdc.f\nr-2.10.1.p2/src/src/modules/lapack/dlapack4.f\nr-2.10.1.p2/src/src/modules/lapack/vecLibg95f.f\nr-2.10.1.p2/src/src/modules/lapack/dlapack3.f\nr-2.10.1.p2/src/src/modules/lapack/dlapack2.f\netc\n```\n\n\nI'll upload a patch and deps file\n\nDave \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9464\n\n",
    "created_at": "2010-07-09T12:38:51Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "R depends on Fortran, but has no such dependancy in spkg/standard/deps",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9464",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @rlmill @jhpalmieri @qed777

In the sage-4.5.alpha4 code, the $SAGE_ROOT/spkg/standard/deps file has this entry for R:


```
$(INST)/$(R): $(BASE) $(INST)/$(PYTHON) $(INST)/$(ATLAS) $(INST)/$(ICONV)
        $(INSTALL) "$(SAGE_SPKG) $(R) 2>&1" "tee -a $(SAGE_LOGS)/$(R).log"
```


Note, there is no Fortran dependency listed, yet R does have Fortran files:


```
drkirkby@hawk:~/sage-4.5.alpha4/spkg/standard$ find r-2.10.1.p2 -name '*.f'
r-2.10.1.p2/src/src/library/stats/src/stxwx.f
r-2.10.1.p2/src/src/library/stats/src/sgram.f
r-2.10.1.p2/src/src/library/stats/src/bsplvd.f
r-2.10.1.p2/src/src/library/stats/src/stl.f
r-2.10.1.p2/src/src/library/stats/src/hclust.f
r-2.10.1.p2/src/src/library/stats/src/sslvrg.f
r-2.10.1.p2/src/src/library/stats/src/qsbart.f
r-2.10.1.p2/src/src/library/stats/src/bvalue.f
r-2.10.1.p2/src/src/library/stats/src/loessf.f
r-2.10.1.p2/src/src/library/stats/src/lminfl.f
r-2.10.1.p2/src/src/library/stats/src/kmns.f
r-2.10.1.p2/src/src/library/stats/src/eureka.f
r-2.10.1.p2/src/src/library/stats/src/sinerp.f
r-2.10.1.p2/src/src/library/stats/src/bvalus.f
r-2.10.1.p2/src/src/library/stats/src/ppr.f
r-2.10.1.p2/src/src/library/stats/src/portsrc.f
r-2.10.1.p2/src/src/appl/dchdc.f
r-2.10.1.p2/src/src/appl/chol.f
r-2.10.1.p2/src/src/appl/dqrsl.f
r-2.10.1.p2/src/src/appl/dqrdc2.f
r-2.10.1.p2/src/src/appl/eigen.f
r-2.10.1.p2/src/src/appl/dpoco.f
r-2.10.1.p2/src/src/appl/dposl.f
r-2.10.1.p2/src/src/appl/dpbfa.f
r-2.10.1.p2/src/src/appl/dtrco.f
r-2.10.1.p2/src/src/appl/dtrsl.f
r-2.10.1.p2/src/src/appl/ch2inv.f
r-2.10.1.p2/src/src/appl/dpofa.f
r-2.10.1.p2/src/src/appl/dqrutl.f
r-2.10.1.p2/src/src/appl/dqrdc.f
r-2.10.1.p2/src/src/appl/dpbsl.f
r-2.10.1.p2/src/src/appl/dpodi.f
r-2.10.1.p2/src/src/appl/dqrls.f
r-2.10.1.p2/src/src/appl/dsvdc.f
r-2.10.1.p2/src/src/modules/lapack/dlapack4.f
r-2.10.1.p2/src/src/modules/lapack/vecLibg95f.f
r-2.10.1.p2/src/src/modules/lapack/dlapack3.f
r-2.10.1.p2/src/src/modules/lapack/dlapack2.f
etc
```


I'll upload a patch and deps file

Dave 



Issue created by migration from https://trac.sagemath.org/ticket/9464





---

archive/issue_comments_090606.json:
```json
{
    "body": "This looks like the cause of #9435",
    "created_at": "2010-07-09T13:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90606",
    "user": "https://github.com/rlmill"
}
```

This looks like the cause of #9435



---

archive/issue_comments_090607.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-07-09T13:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90607",
    "user": "https://github.com/rlmill"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_090608.json:
```json
{
    "body": "$SAGE_ROOT/spkg/standard/deps to force Fortran to build before R",
    "created_at": "2010-07-09T14:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90608",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

$SAGE_ROOT/spkg/standard/deps to force Fortran to build before R



---

archive/issue_comments_090609.json:
```json
{
    "body": "Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9464/deps.diff) by drkirkby created at 2010-07-09 14:46:51\n\nDiff between $SAGE_ROOT/spkg/standard/deps and that is sage-4.5.alpha4",
    "created_at": "2010-07-09T14:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90609",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9464/deps.diff) by drkirkby created at 2010-07-09 14:46:51

Diff between $SAGE_ROOT/spkg/standard/deps and that is sage-4.5.alpha4



---

archive/issue_comments_090610.json:
```json
{
    "body": "This change to deps seems fine -- making the dependencies explicit seems like a good idea -- but note that fortran is a dependency of lapack, lapack is a dependency of atlas, and atlas is a dependency of R.  So fortran should always get installed before R even without this change.  Have you seen otherwise?",
    "created_at": "2010-07-09T15:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90610",
    "user": "https://github.com/jhpalmieri"
}
```

This change to deps seems fine -- making the dependencies explicit seems like a good idea -- but note that fortran is a dependency of lapack, lapack is a dependency of atlas, and atlas is a dependency of R.  So fortran should always get installed before R even without this change.  Have you seen otherwise?



---

archive/issue_comments_090611.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> This change to deps seems fine -- making the dependencies explicit seems like a good idea -- but note that fortran is a dependency of lapack, lapack is a dependency of atlas, and atlas is a dependency of R.  So fortran should always get installed before R even without this change.  Have you seen otherwise?\n\nI've personally not seen a problem. \n\nI must admit I did not look carefully to see the Fortran/LAPACK/ATLAS/R dependency. But Robert thought it was the cause of an OS X problem (see #9435), so upgraded this ticket to blocker. I think you have rather dashed that hope however! \n\nDave",
    "created_at": "2010-07-09T16:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90611",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:2 jhpalmieri]:
> This change to deps seems fine -- making the dependencies explicit seems like a good idea -- but note that fortran is a dependency of lapack, lapack is a dependency of atlas, and atlas is a dependency of R.  So fortran should always get installed before R even without this change.  Have you seen otherwise?

I've personally not seen a problem. 

I must admit I did not look carefully to see the Fortran/LAPACK/ATLAS/R dependency. But Robert thought it was the cause of an OS X problem (see #9435), so upgraded this ticket to blocker. I think you have rather dashed that hope however! 

Dave



---

archive/issue_comments_090612.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-09T16:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90612",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090613.json:
```json
{
    "body": "Changing priority from blocker to minor.",
    "created_at": "2010-07-13T15:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90613",
    "user": "https://github.com/rlmill"
}
```

Changing priority from blocker to minor.



---

archive/issue_comments_090614.json:
```json
{
    "body": "This change is now incorporated in #9761, which already has positive review, **so this ticket can be closed as duplicate**.\n\nMitesh, that's your job... ;-)",
    "created_at": "2010-08-19T00:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90614",
    "user": "https://github.com/nexttime"
}
```

This change is now incorporated in #9761, which already has positive review, **so this ticket can be closed as duplicate**.

Mitesh, that's your job... ;-)



---

archive/issue_comments_090615.json:
```json
{
    "body": "I'm changing the status to \"positive review,\" so that the release mixer/masher/manager/monster will see it at report {11} or {32} and close this ticket as a \"duplicate\" after merging #9761.",
    "created_at": "2010-08-19T01:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90615",
    "user": "https://github.com/qed777"
}
```

I'm changing the status to "positive review," so that the release mixer/masher/manager/monster will see it at report {11} or {32} and close this ticket as a "duplicate" after merging #9761.



---

archive/issue_comments_090616.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-19T01:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90616",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023443.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-24T02:52:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9464#event-23443"
}
```



---

archive/issue_comments_090617.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-24T02:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9464#issuecomment-90617",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate



---

archive/issue_events_023444.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-24T02:52:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9464",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9464#event-23444"
}
```
