# Issue 2381: plot_vector_field can't plot arbitrary vector fields

archive/issues_002381.json:
```json
{
    "body": "Assignee: was\n\nKeywords: plot vector quiver\n\nIs the a way to produce \"quiver plots\" for 2d vector fields? plot_vector_field should accept functions of two parameters, but doesn't:\n\nUsage example:\n\n```\nsage: vf1 = plot_vector_field((lambda x:sin(x), lambda y:cos(y)), (-3,3), (-3,3))\n```\n\n\nWith 2 arguments:\n\n```\nsage: plot_vector_field((lambda x,y:y,lambda x,y:(cos(x)-2)*sin(x)),(-pi,pi),(-pi,pi))\n<type 'exceptions.TypeError'>: <lambda>() takes exactly 2 arguments (1 given)\n```\n\n\nSee http://groups.google.com/group/sage-support/browse_thread/thread/13e52e07c7d7a7f9/ca8623384c7a1f55\n\nIssue created by migration from https://trac.sagemath.org/ticket/2381\n\n",
    "created_at": "2008-03-04T04:15:15Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "plot_vector_field can't plot arbitrary vector fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2381",
    "user": "edrex"
}
```
Assignee: was

Keywords: plot vector quiver

Is the a way to produce "quiver plots" for 2d vector fields? plot_vector_field should accept functions of two parameters, but doesn't:

Usage example:

```
sage: vf1 = plot_vector_field((lambda x:sin(x), lambda y:cos(y)), (-3,3), (-3,3))
```


With 2 arguments:

```
sage: plot_vector_field((lambda x,y:y,lambda x,y:(cos(x)-2)*sin(x)),(-pi,pi),(-pi,pi))
<type 'exceptions.TypeError'>: <lambda>() takes exactly 2 arguments (1 given)
```


See http://groups.google.com/group/sage-support/browse_thread/thread/13e52e07c7d7a7f9/ca8623384c7a1f55

Issue created by migration from https://trac.sagemath.org/ticket/2381





---

archive/issue_comments_016061.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-04T04:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2381#issuecomment-16061",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_016062.json:
```json
{
    "body": "Having functions that take two arguments is the right thing to do.  I have a patch that I'll post here in a second.",
    "created_at": "2008-03-04T04:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2381#issuecomment-16062",
    "user": "mhansen"
}
```

Having functions that take two arguments is the right thing to do.  I have a patch that I'll post here in a second.



---

archive/issue_comments_016063.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-04T04:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2381#issuecomment-16063",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016064.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-03-04T04:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2381#issuecomment-16064",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_016065.json:
```json
{
    "body": "mhansen and I independently came up with the same solution in about the same time.",
    "created_at": "2008-03-04T06:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2381#issuecomment-16065",
    "user": "jason"
}
```

mhansen and I independently came up with the same solution in about the same time.



---

archive/issue_comments_016066.json:
```json
{
    "body": "Attachment [vector-field.patch](tarball://root/attachments/some-uuid/ticket2381/vector-field.patch) by mhansen created at 2008-03-04 06:49:17\n\nLooks good to me.",
    "created_at": "2008-03-04T06:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2381#issuecomment-16066",
    "user": "mhansen"
}
```

Attachment [vector-field.patch](tarball://root/attachments/some-uuid/ticket2381/vector-field.patch) by mhansen created at 2008-03-04 06:49:17

Looks good to me.



---

archive/issue_comments_016067.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc2",
    "created_at": "2008-03-05T06:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2381#issuecomment-16067",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc2



---

archive/issue_comments_016068.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T06:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2381#issuecomment-16068",
    "user": "mabshoff"
}
```

Resolution: fixed
