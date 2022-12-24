# Issue 3069: notebook -- typeset checkbox doesn't work after save/reload

archive/issues_003069.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n\n\nOn Wed, Apr 30, 2008 at 11:36 AM, John H Palmieri <jhpalmieri64@gmail.com> wrote:\n> \n>  This is with Sage 3.0, Firefox 2.0.0.14, linux.\n>  \n>  If I check the little \"Typeset\" box at the top of the notebook, save\n>  and quit the notebook, then re-enter it, the box is still checked, but\n>  my output is not typeset.  If I uncheck it and then check it again, it\n>  works.\n>  \n>  Can anyone else reproduce this?\n>  \n\nI've seen this.  I consider it a bug.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3069\n\n",
    "created_at": "2008-04-30T18:45:08Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- typeset checkbox doesn't work after save/reload",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3069",
    "user": "was"
}
```
Assignee: boothby


```


On Wed, Apr 30, 2008 at 11:36 AM, John H Palmieri <jhpalmieri64@gmail.com> wrote:
> 
>  This is with Sage 3.0, Firefox 2.0.0.14, linux.
>  
>  If I check the little "Typeset" box at the top of the notebook, save
>  and quit the notebook, then re-enter it, the box is still checked, but
>  my output is not typeset.  If I uncheck it and then check it again, it
>  works.
>  
>  Can anyone else reproduce this?
>  

I've seen this.  I consider it a bug.

```


Issue created by migration from https://trac.sagemath.org/ticket/3069





---

archive/issue_comments_021181.json:
```json
{
    "body": "Attachment [sage-3069.patch](tarball://root/attachments/some-uuid/ticket3069/sage-3069.patch) by was created at 2008-05-11 08:40:38",
    "created_at": "2008-05-11T08:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3069#issuecomment-21181",
    "user": "was"
}
```

Attachment [sage-3069.patch](tarball://root/attachments/some-uuid/ticket3069/sage-3069.patch) by was created at 2008-05-11 08:40:38



---

archive/issue_comments_021182.json:
```json
{
    "body": "I've checked it on a Mac with Safari and Firefox, and also on a linux box with Firefox.  Looks good.",
    "created_at": "2008-05-13T19:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3069#issuecomment-21182",
    "user": "jhpalmieri"
}
```

I've checked it on a Mac with Safari and Firefox, and also on a linux box with Firefox.  Looks good.



---

archive/issue_comments_021183.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-13T19:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3069#issuecomment-21183",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_021184.json:
```json
{
    "body": "Hi,\n\nthis is now how things work around here. If you review the patch and give it a positive review you should change the summary. Only when the patch is actually merged the release manager closes the ticket. \n\nErgo: reopened.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-13T19:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3069#issuecomment-21184",
    "user": "mabshoff"
}
```

Hi,

this is now how things work around here. If you review the patch and give it a positive review you should change the summary. Only when the patch is actually merged the release manager closes the ticket. 

Ergo: reopened.

Cheers,

Michael



---

archive/issue_comments_021185.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-05-13T19:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3069#issuecomment-21185",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_021186.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-05-13T19:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3069#issuecomment-21186",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_021187.json:
```json
{
    "body": "To make the first sentence understandable: \"now->not\" :)\n\nCheers,\n\nMichael",
    "created_at": "2008-05-13T19:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3069#issuecomment-21187",
    "user": "mabshoff"
}
```

To make the first sentence understandable: "now->not" :)

Cheers,

Michael



---

archive/issue_comments_021188.json:
```json
{
    "body": "Behaves well for me, both on a Mac (Safari and Firefox) and on a linux box (Firefox).  Code looks good.",
    "created_at": "2008-05-13T19:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3069#issuecomment-21188",
    "user": "jhpalmieri"
}
```

Behaves well for me, both on a Mac (Safari and Firefox) and on a linux box (Firefox).  Code looks good.



---

archive/issue_comments_021189.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T18:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3069#issuecomment-21189",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021190.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-17T18:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3069#issuecomment-21190",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha1
