# Issue 3160: change is_planar for graphs to return bool

archive/issues_003160.json:
```json
{
    "body": "Assignee: rlm\n\n\n```\n+1 on making this change. It's very unusual for an is_ function to\nreturn anything but a bool :)\n- Hide quoted text -\n\nOn Sun, May 11, 2008 at 11:34 AM, Robert Miller <rlmillster@gmail.com> wrote:\n>\n>>  On the other hand, that Jerin was confused maybe strongly suggests\n>>  you might want to change the is_planar function to return True or\n>>  False, and have another function or a flag to get the nonplanar\n>>  subgroup.  In most of Sage foo.is_*() returns True or False, so maybe\n>>  is_planar() is confusing, especially from a readability point of view.\n>\n> I think I agree. The default behavior should be True/False, and an\n> option to return the present tuple should be available.\n>\n>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3160\n\n",
    "created_at": "2008-05-11T19:00:51Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "change is_planar for graphs to return bool",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3160",
    "user": "was"
}
```
Assignee: rlm


```
+1 on making this change. It's very unusual for an is_ function to
return anything but a bool :)
- Hide quoted text -

On Sun, May 11, 2008 at 11:34 AM, Robert Miller <rlmillster@gmail.com> wrote:
>
>>  On the other hand, that Jerin was confused maybe strongly suggests
>>  you might want to change the is_planar function to return True or
>>  False, and have another function or a flag to get the nonplanar
>>  subgroup.  In most of Sage foo.is_*() returns True or False, so maybe
>>  is_planar() is confusing, especially from a readability point of view.
>
> I think I agree. The default behavior should be True/False, and an
> option to return the present tuple should be available.
>
>
```


Issue created by migration from https://trac.sagemath.org/ticket/3160





---

archive/issue_comments_021922.json:
```json
{
    "body": "Attachment [3160-bool-is-planar.patch](tarball://root/attachments/some-uuid/ticket3160/3160-bool-is-planar.patch) by ekirkman created at 2008-05-12 16:18:44",
    "created_at": "2008-05-12T16:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3160#issuecomment-21922",
    "user": "ekirkman"
}
```

Attachment [3160-bool-is-planar.patch](tarball://root/attachments/some-uuid/ticket3160/3160-bool-is-planar.patch) by ekirkman created at 2008-05-12 16:18:44



---

archive/issue_comments_021923.json:
```json
{
    "body": "-1 point for not testing before submitting!",
    "created_at": "2008-05-12T16:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3160#issuecomment-21923",
    "user": "rlm"
}
```

-1 point for not testing before submitting!



---

archive/issue_comments_021924.json:
```json
{
    "body": "Attachment [3160-docs.patch](tarball://root/attachments/some-uuid/ticket3160/3160-docs.patch) by mabshoff created at 2008-05-12 18:46:30\n\nMerged both patches in Sage 3.0.2.alpha1",
    "created_at": "2008-05-12T18:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3160#issuecomment-21924",
    "user": "mabshoff"
}
```

Attachment [3160-docs.patch](tarball://root/attachments/some-uuid/ticket3160/3160-docs.patch) by mabshoff created at 2008-05-12 18:46:30

Merged both patches in Sage 3.0.2.alpha1



---

archive/issue_comments_021925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-12T18:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3160#issuecomment-21925",
    "user": "mabshoff"
}
```

Resolution: fixed
