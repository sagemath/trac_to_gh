# Issue 7789: Improve the arguments for the default type of a variable in MixedIntegerLinearProgram

archive/issues_007789.json:
```json
{
    "body": "Assignee: jkantor\n\nThe help of MixedIntegerLinearProgram.new_variable shows a way to define a default type for new variables, but it uses the argument vtype and pre-defined constants (MixedIntegerLinearProgram.__INTEGER for example) which is really ugly.\n\nWe should accept things like :\n\n```\np.new_variable(boolean=True)\n```\n\nor\n\n\n```\np.new_variable(type=\"boolean\")\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7789\n\n",
    "created_at": "2009-12-29T18:14:06Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Improve the arguments for the default type of a variable in MixedIntegerLinearProgram",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7789",
    "user": "ncohen"
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

archive/issue_comments_067225.json:
```json
{
    "body": "Here it is !",
    "created_at": "2010-01-16T16:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67225",
    "user": "ncohen"
}
```

Here it is !



---

archive/issue_comments_067226.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T16:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67226",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067227.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67227",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_067228.json:
```json
{
    "body": "I think this needs more examples.",
    "created_at": "2010-04-03T13:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67228",
    "user": "wdj"
}
```

I think this needs more examples.



---

archive/issue_comments_067229.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-03T13:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67229",
    "user": "wdj"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067230.json:
```json
{
    "body": "I just updated the patch to add 2 lines of test .. I am sorry but I do not really know which kind of examples you expect there... :-/ \n\nPlease tell me and I'll add them immediately !!\n\nNathann",
    "created_at": "2010-04-03T19:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67230",
    "user": "ncohen"
}
```

I just updated the patch to add 2 lines of test .. I am sorry but I do not really know which kind of examples you expect there... :-/ 

Please tell me and I'll add them immediately !!

Nathann



---

archive/issue_comments_067231.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-03T19:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67231",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067232.json:
```json
{
    "body": "You current code allows `real=True` and `binary=True` and will quietly make a choice.",
    "created_at": "2010-05-06T16:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67232",
    "user": "malb"
}
```

You current code allows `real=True` and `binary=True` and will quietly make a choice.



---

archive/issue_comments_067233.json:
```json
{
    "body": "Fixed !",
    "created_at": "2010-05-06T17:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67233",
    "user": "ncohen"
}
```

Fixed !



---

archive/issue_comments_067234.json:
```json
{
    "body": "Few comments:\n\nI think parameter 'name' should be documented. I couldn't find out any place where changing this parameter would affect at all. Also show() method lists 'binary' type variables as boolean variables, which I find bit ugly. Fixing that might be out of scope of this ticket though, as 'binary' is used extensively in code and documentation.\n\nI'm not native English speaker so I might be wrong here, but I think this: \"An exception is raised when two types are required\" at the documentation should maybe say something like \"An exception is raised when two types are _supplied_\".",
    "created_at": "2010-05-13T20:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67234",
    "user": "jsyri"
}
```

Few comments:

I think parameter 'name' should be documented. I couldn't find out any place where changing this parameter would affect at all. Also show() method lists 'binary' type variables as boolean variables, which I find bit ugly. Fixing that might be out of scope of this ticket though, as 'binary' is used extensively in code and documentation.

I'm not native English speaker so I might be wrong here, but I think this: "An exception is raised when two types are required" at the documentation should maybe say something like "An exception is raised when two types are _supplied_".



---

archive/issue_comments_067235.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-13T20:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67235",
    "user": "jsyri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067236.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-13T20:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67236",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067237.json:
```json
{
    "body": "Sounds comments... Updated ! :-)\n\nNathann",
    "created_at": "2010-05-13T20:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67237",
    "user": "ncohen"
}
```

Sounds comments... Updated ! :-)

Nathann



---

archive/issue_comments_067238.json:
```json
{
    "body": "Unfortunately indentation at documentation for 'name' is off by one, so one more update required :-( Otherwise everything seems fine. I'm running doctest now, and if they come clean it'll get positive review after that last fix.",
    "created_at": "2010-05-13T21:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67238",
    "user": "jsyri"
}
```

Unfortunately indentation at documentation for 'name' is off by one, so one more update required :-( Otherwise everything seems fine. I'm running doctest now, and if they come clean it'll get positive review after that last fix.



---

archive/issue_comments_067239.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-13T21:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67239",
    "user": "jsyri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067240.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-13T21:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67240",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067241.json:
```json
{
    "body": "Attachment [trac_7789.patch](tarball://root/attachments/some-uuid/ticket7789/trac_7789.patch) by ncohen created at 2010-05-13 21:22:28\n\nDone.",
    "created_at": "2010-05-13T21:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67241",
    "user": "ncohen"
}
```

Attachment [trac_7789.patch](tarball://root/attachments/some-uuid/ticket7789/trac_7789.patch) by ncohen created at 2010-05-13 21:22:28

Done.



---

archive/issue_comments_067242.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-14T07:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67242",
    "user": "jsyri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067243.json:
```json
{
    "body": "Everything seems to be in order. Positive review it is.",
    "created_at": "2010-05-14T07:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67243",
    "user": "jsyri"
}
```

Everything seems to be in order. Positive review it is.



---

archive/issue_comments_067244.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-07T04:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7789#issuecomment-67244",
    "user": "mhansen"
}
```

Resolution: fixed
