# Issue 6184: mesh=True and dots=True don't work for 3D plots

archive/issues_006184.json:
```json
{
    "body": "Assignee: tbd\n\nJust like the title says; the options noted do not have any effect on 3D plots in Sage 4.0.rc0.\n\nFor example, the command\n\n```\nplot3d(lambda x,y: exp(x+y*I).real(), (-2, 2.4), (-3, 3), mesh=True)\n```\n\nShould display a 3D plot with mesh lines drawn in. However, the result does not have mesh lines.\n\n(This bug was discussed at [this forum thread](http://groups.google.com/group/sage-devel/browse_thread/thread/ac3ae56aa896826f).)\n\nI will attach a patch that fixes the issue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6184\n\n",
    "created_at": "2009-06-02T08:30:53Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "mesh=True and dots=True don't work for 3D plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6184",
    "user": "wcauchois"
}
```
Assignee: tbd

Just like the title says; the options noted do not have any effect on 3D plots in Sage 4.0.rc0.

For example, the command

```
plot3d(lambda x,y: exp(x+y*I).real(), (-2, 2.4), (-3, 3), mesh=True)
```

Should display a 3D plot with mesh lines drawn in. However, the result does not have mesh lines.

(This bug was discussed at [this forum thread](http://groups.google.com/group/sage-devel/browse_thread/thread/ac3ae56aa896826f).)

I will attach a patch that fixes the issue.

Issue created by migration from https://trac.sagemath.org/ticket/6184





---

archive/issue_comments_049371.json:
```json
{
    "body": "Attachment [trac6184.patch](tarball://root/attachments/some-uuid/ticket6184/trac6184.patch) by wcauchois created at 2009-06-02 08:32:58\n\nbased on sage 4.0.rc0",
    "created_at": "2009-06-02T08:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6184#issuecomment-49371",
    "user": "wcauchois"
}
```

Attachment [trac6184.patch](tarball://root/attachments/some-uuid/ticket6184/trac6184.patch) by wcauchois created at 2009-06-02 08:32:58

based on sage 4.0.rc0



---

archive/issue_comments_049372.json:
```json
{
    "body": "Does anyone know where this functionality was broken, and what the code was like before?",
    "created_at": "2009-06-02T08:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6184#issuecomment-49372",
    "user": "wcauchois"
}
```

Does anyone know where this functionality was broken, and what the code was like before?



---

archive/issue_comments_049373.json:
```json
{
    "body": "This seems to fix the problem and not cause others in the limited testing I have done.  Since it is a surgical-strike type of patch I feel good about giving it a positive review - this is basically two extra lines that correctly pass on an option.",
    "created_at": "2009-06-02T12:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6184#issuecomment-49373",
    "user": "mhampton"
}
```

This seems to fix the problem and not cause others in the limited testing I have done.  Since it is a surgical-strike type of patch I feel good about giving it a positive review - this is basically two extra lines that correctly pass on an option.



---

archive/issue_comments_049374.json:
```json
{
    "body": "Changing component from algebra to graphics.",
    "created_at": "2009-06-02T12:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6184#issuecomment-49374",
    "user": "mhampton"
}
```

Changing component from algebra to graphics.



---

archive/issue_comments_049375.json:
```json
{
    "body": "Changing assignee from tbd to was.",
    "created_at": "2009-06-02T12:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6184#issuecomment-49375",
    "user": "mhampton"
}
```

Changing assignee from tbd to was.



---

archive/issue_comments_049376.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-03T18:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6184#issuecomment-49376",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049377.json:
```json
{
    "body": "Merged in 4.0.1.rc0.",
    "created_at": "2009-06-03T18:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6184#issuecomment-49377",
    "user": "mhansen"
}
```

Merged in 4.0.1.rc0.
