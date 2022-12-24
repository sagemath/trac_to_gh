# Issue 5229: [with patch, needs review] Jmol axes in the wrong place

archive/issues_005229.json:
```json
{
    "body": "Assignee: was\n\nAs is, it appears that 3d plots are wrong, according to the jmol axes, because the jmol axes apparently don't default to being centered at the origin.  This patch makes the jmol axes centered at the origin.  To show the jmol axes, you still need to right-click on the jmol plot, select Style, then Axes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5229\n\n",
    "created_at": "2009-02-10T21:18:01Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "[with patch, needs review] Jmol axes in the wrong place",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5229",
    "user": "jason"
}
```
Assignee: was

As is, it appears that 3d plots are wrong, according to the jmol axes, because the jmol axes apparently don't default to being centered at the origin.  This patch makes the jmol axes centered at the origin.  To show the jmol axes, you still need to right-click on the jmol plot, select Style, then Axes.

Issue created by migration from https://trac.sagemath.org/ticket/5229





---

archive/issue_comments_040079.json:
```json
{
    "body": "Attachment [trac_5229-jmol-axes.patch](tarball://root/attachments/some-uuid/ticket5229/trac_5229-jmol-axes.patch) by ncalexan created at 2009-02-10 21:49:16\n\n\n```\n[1:28pm] ncalexan: jason|log: either it's not working or I don't get it.\n[1:28pm] ncalexan: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2))\n[1:28pm] ncalexan: gives me a smooth cup-like surface.\n[1:28pm] ncalexan: But the value at x=0, y=0 (which is z=0) does not coincide with the jmol axes.\n```\n",
    "created_at": "2009-02-10T21:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5229#issuecomment-40079",
    "user": "ncalexan"
}
```

Attachment [trac_5229-jmol-axes.patch](tarball://root/attachments/some-uuid/ticket5229/trac_5229-jmol-axes.patch) by ncalexan created at 2009-02-10 21:49:16


```
[1:28pm] ncalexan: jason|log: either it's not working or I don't get it.
[1:28pm] ncalexan: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2))
[1:28pm] ncalexan: gives me a smooth cup-like surface.
[1:28pm] ncalexan: But the value at x=0, y=0 (which is z=0) does not coincide with the jmol axes.
```




---

archive/issue_comments_040080.json:
```json
{
    "body": "After further IRC discussion, the proposed fix does not work in all situations.",
    "created_at": "2009-02-10T22:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5229#issuecomment-40080",
    "user": "ncalexan"
}
```

After further IRC discussion, the proposed fix does not work in all situations.



---

archive/issue_comments_040081.json:
```json
{
    "body": "We don't give negative reviews any more, so change it to \"needs work\".\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T02:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5229#issuecomment-40081",
    "user": "mabshoff"
}
```

We don't give negative reviews any more, so change it to "needs work".

Cheers,

Michael



---

archive/issue_comments_040082.json:
```json
{
    "body": "See #3862",
    "created_at": "2010-01-17T08:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5229#issuecomment-40082",
    "user": "jason"
}
```

See #3862



---

archive/issue_comments_040083.json:
```json
{
    "body": "Also, and perhaps that merits a new ticket, the orientation of the axis is not what one would expect.\n\nNormally 3d plots are shown with the positive x axis to the viewer's left, the positive y axis to the right, and the positive z upwards. Currently it is: negative y axis to the left, positive x to the right, and positive z upwards.",
    "created_at": "2010-05-29T21:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5229#issuecomment-40083",
    "user": "olazo"
}
```

Also, and perhaps that merits a new ticket, the orientation of the axis is not what one would expect.

Normally 3d plots are shown with the positive x axis to the viewer's left, the positive y axis to the right, and the positive z upwards. Currently it is: negative y axis to the left, positive x to the right, and positive z upwards.
