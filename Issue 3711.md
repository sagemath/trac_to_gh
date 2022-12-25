# Issue 3711: notebook -- folder of worksheets not properly saved

archive/issues_003711.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n\n\nOn Wed, Jul 23, 2008 at 1:35 AM, John H Palmieri <jhpalmieri64@gmail.com> wrote:\n>\n> On Jul 11, 3:21 pm, John H Palmieri <jhpalmier...@gmail.com> wrote:\n>> Since upgrading to Sage 3.0.4 on my intel Mac, when I enter the\n>> notebook, my Sage worksheet list shows all of the worksheets I've ever\n>> worked on.  If I mark some to be archived or some to be deleted, it\n>> has a short-term effect: the worksheets disappear from the \"Active\"\n>> list.  This does not last, though: the next time I start the notebook,\n>> the worksheets are back in the active list.\n>\n> This also happens on my linux box (although I am able to successfully\n> empty the trash there).  It's quite annoying to have something like 50\n> worksheets listed, instead of the half a dozen I want marked as\n> \"Active\".\n>\n>> Also, if I mark some worksheets to be deleted, click \"Trash\" to view\n>> the list of those worksheets, then click \"Empty Trash\", I get a\n>> warning about how this will permanently delete the items, etc.  I\n>> click \"Continue\" and am taken back to the list of Active worksheets,\n>> but if I click \"Trash\", I see the old list: the trash has not been\n>> emptied.\n\nI can replicate this.\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3711\n\n",
    "created_at": "2008-07-23T00:21:00Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "notebook -- folder of worksheets not properly saved",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3711",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby


```


On Wed, Jul 23, 2008 at 1:35 AM, John H Palmieri <jhpalmieri64@gmail.com> wrote:
>
> On Jul 11, 3:21 pm, John H Palmieri <jhpalmier...@gmail.com> wrote:
>> Since upgrading to Sage 3.0.4 on my intel Mac, when I enter the
>> notebook, my Sage worksheet list shows all of the worksheets I've ever
>> worked on.  If I mark some to be archived or some to be deleted, it
>> has a short-term effect: the worksheets disappear from the "Active"
>> list.  This does not last, though: the next time I start the notebook,
>> the worksheets are back in the active list.
>
> This also happens on my linux box (although I am able to successfully
> empty the trash there).  It's quite annoying to have something like 50
> worksheets listed, instead of the half a dozen I want marked as
> "Active".
>
>> Also, if I mark some worksheets to be deleted, click "Trash" to view
>> the list of those worksheets, then click "Empty Trash", I get a
>> warning about how this will permanently delete the items, etc.  I
>> click "Continue" and am taken back to the list of Active worksheets,
>> but if I click "Trash", I see the old list: the trash has not been
>> emptied.

I can replicate this.

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/3711





---

archive/issue_comments_026287.json:
```json
{
    "body": "Attachment [trac_3711.patch](tarball://root/attachments/some-uuid/ticket3711/trac_3711.patch) by @mwhansen created at 2008-09-07 23:58:47",
    "created_at": "2008-09-07T23:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3711#issuecomment-26287",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3711.patch](tarball://root/attachments/some-uuid/ticket3711/trac_3711.patch) by @mwhansen created at 2008-09-07 23:58:47



---

archive/issue_comments_026288.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2008-09-08T00:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3711#issuecomment-26288",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_026289.json:
```json
{
    "body": "I add a selenium doctest for this (test_3711) which can be found at http://sage.math.washington.edu/home/mhansen/sage_selenium/test_notebook.py",
    "created_at": "2008-09-08T00:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3711#issuecomment-26289",
    "user": "https://github.com/mwhansen"
}
```

I add a selenium doctest for this (test_3711) which can be found at http://sage.math.washington.edu/home/mhansen/sage_selenium/test_notebook.py



---

archive/issue_comments_026290.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-08T00:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3711#issuecomment-26290",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026291.json:
```json
{
    "body": "I didn't run the selenium doctest, but I did various file operations to make sure that the bug was resolved and that some new bug didn't pop up.",
    "created_at": "2008-09-08T11:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3711#issuecomment-26291",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I didn't run the selenium doctest, but I did various file operations to make sure that the bug was resolved and that some new bug didn't pop up.



---

archive/issue_comments_026292.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-09T00:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3711#issuecomment-26292",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_comments_026293.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-09T00:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3711#issuecomment-26293",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
