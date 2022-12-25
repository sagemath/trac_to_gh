# Issue 7789: Improve the arguments for the default type of a variable in MixedIntegerLinearProgram

archive/issues_007789.json:
```json
{
    "body": "Assignee: jkantor\n\nThe help of MixedIntegerLinearProgram.new_variable shows a way to define a default type for new variables, but it uses the argument vtype and pre-defined constants (MixedIntegerLinearProgram.__INTEGER for example) which is really ugly.\n\nWe should accept things like :\n\n```\np.new_variable(boolean=True)\n```\n\nor\n\n\n```\np.new_variable(type=\"boolean\")\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7789\n\n",
    "created_at": "2009-12-29T18:14:06Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Improve the arguments for the default type of a variable in MixedIntegerLinearProgram",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7789",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jkantor

The help of MixedIntegerLinearProgram.new_variable shows a way to define a default type for new variables, but it uses the argument vtype and pre-defined constants (MixedIntegerLinearProgram.__INTEGER for example) which is really ugly.

We should accept things like :

```
p.new_variable(boolean=True)
```

or


```
p.new_variable(type="boolean")
```


Issue created by migration from https://trac.sagemath.org/ticket/7789





---

archive/issue_comments_067108.json:
```json
{
    "body": "Here it is !",
    "created_at": "2010-01-16T16:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67108",
    "user": "https://github.com/nathanncohen"
}
```

Here it is !



---

archive/issue_comments_067109.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T16:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67109",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067110.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67110",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_067111.json:
```json
{
    "body": "I think this needs more examples.",
    "created_at": "2010-04-03T13:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67111",
    "user": "https://github.com/wdjoyner"
}
```

I think this needs more examples.



---

archive/issue_comments_067112.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-03T13:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67112",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067113.json:
```json
{
    "body": "I just updated the patch to add 2 lines of test .. I am sorry but I do not really know which kind of examples you expect there... :-/ \n\nPlease tell me and I'll add them immediately !!\n\nNathann",
    "created_at": "2010-04-03T19:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67113",
    "user": "https://github.com/nathanncohen"
}
```

I just updated the patch to add 2 lines of test .. I am sorry but I do not really know which kind of examples you expect there... :-/ 

Please tell me and I'll add them immediately !!

Nathann



---

archive/issue_comments_067114.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-03T19:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67114",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067115.json:
```json
{
    "body": "You current code allows `real=True` and `binary=True` and will quietly make a choice.",
    "created_at": "2010-05-06T16:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67115",
    "user": "https://github.com/malb"
}
```

You current code allows `real=True` and `binary=True` and will quietly make a choice.



---

archive/issue_comments_067116.json:
```json
{
    "body": "Fixed !",
    "created_at": "2010-05-06T17:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67116",
    "user": "https://github.com/nathanncohen"
}
```

Fixed !



---

archive/issue_comments_067117.json:
```json
{
    "body": "Few comments:\n\nI think parameter 'name' should be documented. I couldn't find out any place where changing this parameter would affect at all. Also show() method lists 'binary' type variables as boolean variables, which I find bit ugly. Fixing that might be out of scope of this ticket though, as 'binary' is used extensively in code and documentation.\n\nI'm not native English speaker so I might be wrong here, but I think this: \"An exception is raised when two types are required\" at the documentation should maybe say something like \"An exception is raised when two types are _supplied_\".",
    "created_at": "2010-05-13T20:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67117",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Few comments:

I think parameter 'name' should be documented. I couldn't find out any place where changing this parameter would affect at all. Also show() method lists 'binary' type variables as boolean variables, which I find bit ugly. Fixing that might be out of scope of this ticket though, as 'binary' is used extensively in code and documentation.

I'm not native English speaker so I might be wrong here, but I think this: "An exception is raised when two types are required" at the documentation should maybe say something like "An exception is raised when two types are _supplied_".



---

archive/issue_comments_067118.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-13T20:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67118",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067119.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-13T20:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67119",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067120.json:
```json
{
    "body": "Sounds comments... Updated ! :-)\n\nNathann",
    "created_at": "2010-05-13T20:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67120",
    "user": "https://github.com/nathanncohen"
}
```

Sounds comments... Updated ! :-)

Nathann



---

archive/issue_comments_067121.json:
```json
{
    "body": "Unfortunately indentation at documentation for 'name' is off by one, so one more update required :-( Otherwise everything seems fine. I'm running doctest now, and if they come clean it'll get positive review after that last fix.",
    "created_at": "2010-05-13T21:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67121",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Unfortunately indentation at documentation for 'name' is off by one, so one more update required :-( Otherwise everything seems fine. I'm running doctest now, and if they come clean it'll get positive review after that last fix.



---

archive/issue_comments_067122.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-13T21:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67122",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067123.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-13T21:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67123",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067124.json:
```json
{
    "body": "Attachment [trac_7789.patch](tarball://root/attachments/some-uuid/ticket7789/trac_7789.patch) by @nathanncohen created at 2010-05-13 21:22:28\n\nDone.",
    "created_at": "2010-05-13T21:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67124",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7789.patch](tarball://root/attachments/some-uuid/ticket7789/trac_7789.patch) by @nathanncohen created at 2010-05-13 21:22:28

Done.



---

archive/issue_comments_067125.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-14T07:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67125",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067126.json:
```json
{
    "body": "Everything seems to be in order. Positive review it is.",
    "created_at": "2010-05-14T07:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67126",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Everything seems to be in order. Positive review it is.



---

archive/issue_comments_067127.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-07T04:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67127",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_008005.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-07T04:51:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7789#event-8005"
}
```
