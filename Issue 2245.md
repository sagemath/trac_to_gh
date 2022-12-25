# Issue 2245: abvar -- increase the doctest coverage to 100%

archive/issues_002245.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe doctest coverage for devel/sage/sage/modular/abvar is as follows:\n\n```\nteragon:abvar was$ sage -coverage .\nabvar.py: 62% (20 of 32)\nabvar_ambient_jacobian.py: 28% (2 of 7)\nabvar_modsym_factor.py: 60% (3 of 5)\nabvar_newform.py: 0% (0 of 1)\nconstructor.py: 100% (3 of 3)\ncuspidal_subgroup.py: 16% (1 of 6)\nfinite_subgroup.py: 12% (4 of 33)\nhecke_operator.py: 66% (4 of 6)\nhomology.py: 57% (16 of 28)\nhomspace.py: 0% (0 of 2)\nlseries.py: 0% (0 of 6)\nmorphism.py: 0% (0 of 2)\ntorsion_point.py: 0% (0 of 2)\ntorsion_subgroup.py: 37% (3 of 8)\n\nOverall weighted coverage score:  39.4%\nTotal number of functions:  141\n```\n\n\nThe goal of this ticket is to change that to 100%.\n\nThis is in preparation for substantial work to move\nthe modular abelian varieties package forward in preparation\nfor lots of enhancements to it that are coming up. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2245\n\n",
    "created_at": "2008-02-21T07:31:34Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "abvar -- increase the doctest coverage to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2245",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

The doctest coverage for devel/sage/sage/modular/abvar is as follows:

```
teragon:abvar was$ sage -coverage .
abvar.py: 62% (20 of 32)
abvar_ambient_jacobian.py: 28% (2 of 7)
abvar_modsym_factor.py: 60% (3 of 5)
abvar_newform.py: 0% (0 of 1)
constructor.py: 100% (3 of 3)
cuspidal_subgroup.py: 16% (1 of 6)
finite_subgroup.py: 12% (4 of 33)
hecke_operator.py: 66% (4 of 6)
homology.py: 57% (16 of 28)
homspace.py: 0% (0 of 2)
lseries.py: 0% (0 of 6)
morphism.py: 0% (0 of 2)
torsion_point.py: 0% (0 of 2)
torsion_subgroup.py: 37% (3 of 8)

Overall weighted coverage score:  39.4%
Total number of functions:  141
```


The goal of this ticket is to change that to 100%.

This is in preparation for substantial work to move
the modular abelian varieties package forward in preparation
for lots of enhancements to it that are coming up. 

Issue created by migration from https://trac.sagemath.org/ticket/2245





---

archive/issue_comments_014850.json:
```json
{
    "body": "After:\n\n```\nteragon:abvar was$ sage -coverage .\nabvar.py: 100% (38 of 38)\nabvar_ambient_jacobian.py: 100% (8 of 8)\nabvar_modsym_factor.py: 100% (7 of 7)\nabvar_newform.py: 100% (3 of 3)\nconstructor.py: 100% (3 of 3)\ncuspidal_subgroup.py: 100% (6 of 6)\nfinite_subgroup.py: 100% (33 of 33)\nhecke_operator.py: 100% (6 of 6)\nhomology.py: 100% (30 of 30)\nhomspace.py: 100% (2 of 2)\nlseries.py: 100% (11 of 11)\nmorphism.py: 100% (1 of 1)\ntorsion_subgroup.py: 100% (8 of 8)\n\nOverall weighted coverage score:  100.0%\nTotal number of functions:  156\n```\n",
    "created_at": "2008-02-25T05:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2245#issuecomment-14850",
    "user": "https://github.com/williamstein"
}
```

After:

```
teragon:abvar was$ sage -coverage .
abvar.py: 100% (38 of 38)
abvar_ambient_jacobian.py: 100% (8 of 8)
abvar_modsym_factor.py: 100% (7 of 7)
abvar_newform.py: 100% (3 of 3)
constructor.py: 100% (3 of 3)
cuspidal_subgroup.py: 100% (6 of 6)
finite_subgroup.py: 100% (33 of 33)
hecke_operator.py: 100% (6 of 6)
homology.py: 100% (30 of 30)
homspace.py: 100% (2 of 2)
lseries.py: 100% (11 of 11)
morphism.py: 100% (1 of 1)
torsion_subgroup.py: 100% (8 of 8)

Overall weighted coverage score:  100.0%
Total number of functions:  156
```




---

archive/issue_comments_014851.json:
```json
{
    "body": "Attachment [sage-2245.patch](tarball://root/attachments/some-uuid/ticket2245/sage-2245.patch) by @williamstein created at 2008-02-26 23:11:05\n\nthis is the whole thing flattened and rebased against sage-2.10.3.alpha0",
    "created_at": "2008-02-26T23:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2245#issuecomment-14851",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2245.patch](tarball://root/attachments/some-uuid/ticket2245/sage-2245.patch) by @williamstein created at 2008-02-26 23:11:05

this is the whole thing flattened and rebased against sage-2.10.3.alpha0



---

archive/issue_comments_014852.json:
```json
{
    "body": "Looks great. I went through and edited a few things here and there, mostly correcting typos and over-long lines. \n\nThere's one thing that still bothers me, though: given a modular abelian variety `A`, one uses `A.lseries()` and `A.padic_lseries(5)` to get the complex and p-adic L-series, which is totally reasonable. However, for an elliptic curve `E`, it's `E.Lseries()` and `E.padic_lseries(5)` -- I don't like that one of the four is uppercase, while the other three are lowercase. I think we should make everything consistent, and I personally prefer lowercase. If someone else (e.g. William) agrees, I'll go ahead and make another patch to correct that.",
    "created_at": "2008-03-03T06:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2245#issuecomment-14852",
    "user": "https://github.com/craigcitro"
}
```

Looks great. I went through and edited a few things here and there, mostly correcting typos and over-long lines. 

There's one thing that still bothers me, though: given a modular abelian variety `A`, one uses `A.lseries()` and `A.padic_lseries(5)` to get the complex and p-adic L-series, which is totally reasonable. However, for an elliptic curve `E`, it's `E.Lseries()` and `E.padic_lseries(5)` -- I don't like that one of the four is uppercase, while the other three are lowercase. I think we should make everything consistent, and I personally prefer lowercase. If someone else (e.g. William) agrees, I'll go ahead and make another patch to correct that.



---

archive/issue_comments_014853.json:
```json
{
    "body": "Attachment [trac-2245-touch-ups.patch](tarball://root/attachments/some-uuid/ticket2245/trac-2245-touch-ups.patch) by @craigcitro created at 2008-03-03 06:15:25\n\nminor typo corrections; apply after william's patch above",
    "created_at": "2008-03-03T06:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2245#issuecomment-14853",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2245-touch-ups.patch](tarball://root/attachments/some-uuid/ticket2245/trac-2245-touch-ups.patch) by @craigcitro created at 2008-03-03 06:15:25

minor typo corrections; apply after william's patch above



---

archive/issue_comments_014854.json:
```json
{
    "body": "Good job fixing up my patch.  I just looked over your touch ups.  Very nice.",
    "created_at": "2008-03-03T07:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2245#issuecomment-14854",
    "user": "https://github.com/williamstein"
}
```

Good job fixing up my patch.  I just looked over your touch ups.  Very nice.



---

archive/issue_comments_014855.json:
```json
{
    "body": "Attachment [trac-2245-lseries.patch](tarball://root/attachments/some-uuid/ticket2245/trac-2245-lseries.patch) by @craigcitro created at 2008-03-03 07:27:20\n\napply this third",
    "created_at": "2008-03-03T07:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2245#issuecomment-14855",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2245-lseries.patch](tarball://root/attachments/some-uuid/ticket2245/trac-2245-lseries.patch) by @craigcitro created at 2008-03-03 07:27:20

apply this third



---

archive/issue_comments_014856.json:
```json
{
    "body": "Added a patch to change `Lseries` to `lseries` throughout Sage. Apply after the above patches.",
    "created_at": "2008-03-03T07:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2245#issuecomment-14856",
    "user": "https://github.com/craigcitro"
}
```

Added a patch to change `Lseries` to `lseries` throughout Sage. Apply after the above patches.



---

archive/issue_events_005333.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-03T12:56:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2245",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2245#event-5333"
}
```



---

archive/issue_comments_014857.json:
```json
{
    "body": "Merged all three patches in Sage 2.10.3.rc1",
    "created_at": "2008-03-03T12:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2245#issuecomment-14857",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 2.10.3.rc1



---

archive/issue_comments_014858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T12:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2245#issuecomment-14858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
