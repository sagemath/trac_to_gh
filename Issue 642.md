# Issue 642: update to GMP-ECM-6.1.3

archive/issues_000642.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  michael.abshoff@googlemail.com\n\n\n```\nHi,\n\nGMP-ECM-6.1.3 has been released. This is a bugfix release.\n\nChanges between ecm-6.1.2 and ecm-6.1.3:\n\n   * fixed incorrect computation of memory use in stage 2, especially for\n     machines that use Kronecker-Schoenhage multiplication even for large\n     degrees, such as Core 2\n   * fixed -B2scale option whose value hadn't been passed to the factoring\n     routines\n   * fixed default B2min for P-1 which could be truncated on 32 bit \nmachines,\n     causing stage 2 to take a little longer than necessary\n   * fixed bug for modular multiplication modulo Fermat numbers 2^2^n+1, \nwhere\n     a result of 2^2^n would be truncated to 0\n\n\nThe new version is available at https://gforge.inria.fr/projects/ecm/.\n\nWe would like to thank Peter-Lawrence Montgomery, Andreas Schindel and \nGeorge Woltman for their bug reports.\n\nEnjoy,\nAlex\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/642\n\n",
    "created_at": "2007-09-12T15:51:03Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "update to GMP-ECM-6.1.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/642",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  michael.abshoff@googlemail.com


```
Hi,

GMP-ECM-6.1.3 has been released. This is a bugfix release.

Changes between ecm-6.1.2 and ecm-6.1.3:

   * fixed incorrect computation of memory use in stage 2, especially for
     machines that use Kronecker-Schoenhage multiplication even for large
     degrees, such as Core 2
   * fixed -B2scale option whose value hadn't been passed to the factoring
     routines
   * fixed default B2min for P-1 which could be truncated on 32 bit 
machines,
     causing stage 2 to take a little longer than necessary
   * fixed bug for modular multiplication modulo Fermat numbers 2^2^n+1, 
where
     a result of 2^2^n would be truncated to 0


The new version is available at https://gforge.inria.fr/projects/ecm/.

We would like to thank Peter-Lawrence Montgomery, Andreas Schindel and 
George Woltman for their bug reports.

Enjoy,
Alex
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/642





---

archive/issue_comments_003314.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-12T15:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/642#issuecomment-3314",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003315.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-09-12T15:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/642#issuecomment-3315",
    "user": "mabshoff"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_003316.json:
```json
{
    "body": "There is an update spkg at\n\nhttp://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/ecm-6.1.3.spkg \n\nChangelog is in SPKG.txt\n\nCheers,\n\nMichael",
    "created_at": "2007-09-14T20:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/642#issuecomment-3316",
    "user": "mabshoff"
}
```

There is an update spkg at

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/ecm-6.1.3.spkg 

Changelog is in SPKG.txt

Cheers,

Michael



---

archive/issue_comments_003317.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-14T21:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/642#issuecomment-3317",
    "user": "@williamstein"
}
```

Resolution: fixed
