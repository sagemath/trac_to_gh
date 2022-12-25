# Issue 1021: real_roots sometimes returns incorrect roots

archive/issues_001021.json:
```json
{
    "body": "Assignee: @williamstein\n\nFor example:\n\n```\nsage: x = polygen(ZZ)\nsage: (x^5 * (x^2 - 9999)^2 - 1).real_root_intervals()\n\n[((-120886537286091774329444377/1208925819614629174706176,\n   -60443268541873225202027201/604462909807314587353088),\n  1),\n ((-29274496381311/9007199254740992, 419601125186091/2251799813685248), 1),\n ((2126658450145849453951061654415153249597/21267647932558653966460912964485513216,\n   4253316902721330018853696359533061621799/42535295865117307932921825928971026432),\n  1),\n ((1063329226287740282451317352558954186101/10633823966279326983230456482242756608,\n   531664614358685696701445201630854654353/5316911983139663491615228241121378304),\n  1)]\nsage: len((x^5 * (x^2 - 9999)^2 - 1).real_root_intervals())\n4\n```\n\n\nThis example returns 4 roots, even though the polynomial in question actually has only 3.\n\nThis is because the root finder finds a list of intervals known to have either 0 or 1 root, but is not correctly weeding out some of the intervals that are known to have 0 roots.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1021\n\n",
    "created_at": "2007-10-28T17:31:26Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "real_roots sometimes returns incorrect roots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1021",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

For example:

```
sage: x = polygen(ZZ)
sage: (x^5 * (x^2 - 9999)^2 - 1).real_root_intervals()

[((-120886537286091774329444377/1208925819614629174706176,
   -60443268541873225202027201/604462909807314587353088),
  1),
 ((-29274496381311/9007199254740992, 419601125186091/2251799813685248), 1),
 ((2126658450145849453951061654415153249597/21267647932558653966460912964485513216,
   4253316902721330018853696359533061621799/42535295865117307932921825928971026432),
  1),
 ((1063329226287740282451317352558954186101/10633823966279326983230456482242756608,
   531664614358685696701445201630854654353/5316911983139663491615228241121378304),
  1)]
sage: len((x^5 * (x^2 - 9999)^2 - 1).real_root_intervals())
4
```


This example returns 4 roots, even though the polynomial in question actually has only 3.

This is because the root finder finds a list of intervals known to have either 0 or 1 root, but is not correctly weeding out some of the intervals that are known to have 0 roots.

Issue created by migration from https://trac.sagemath.org/ticket/1021





---

archive/issue_comments_006240.json:
```json
{
    "body": "Attachment [1021.patch](tarball://root/attachments/some-uuid/ticket1021/1021.patch) by cwitty created at 2007-10-28 17:43:48",
    "created_at": "2007-10-28T17:43:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1021#issuecomment-6240",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [1021.patch](tarball://root/attachments/some-uuid/ticket1021/1021.patch) by cwitty created at 2007-10-28 17:43:48



---

archive/issue_comments_006241.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-28T17:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1021#issuecomment-6241",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed
