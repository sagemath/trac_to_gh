# Issue 643: notebook -- fix space issues with the top bar.

archive/issues_000643.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nOn 9/12/07, Marshall Hampton <hamptonio@gmail.com> wrote:\n>\n> I am very happy that the new notebook is more secure, and so I first\n> want to thank everyone who worked on it.\n>\n> There is one thing that bothers me a lot: I treasure my screen real\n> estate, and there is a large (about 1\") gap between the useful stuff\n> in the outer frame (the file menu, use/edit/text/etc) and the frame\n> with the cells.  Is there a way to shrink that?\n>\n\nYes, by appropriately rewriting some of the css that defines the page\nin sage/notebook/server/css.py.\nI wish somebody would do that and send me a patch.\n\nNote that if you just shrink the space on your machine, it will actually\ncompletely cover up all the controls on the top on many other machines.\nIt's very very system dependent.  Having extra space is the only reasonable\nsolution until somebody sits down and does this right.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/643\n\n",
    "created_at": "2007-09-12T18:56:16Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- fix space issues with the top bar.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/643",
    "user": "was"
}
```
Assignee: boothby


```
On 9/12/07, Marshall Hampton <hamptonio@gmail.com> wrote:
>
> I am very happy that the new notebook is more secure, and so I first
> want to thank everyone who worked on it.
>
> There is one thing that bothers me a lot: I treasure my screen real
> estate, and there is a large (about 1") gap between the useful stuff
> in the outer frame (the file menu, use/edit/text/etc) and the frame
> with the cells.  Is there a way to shrink that?
>

Yes, by appropriately rewriting some of the css that defines the page
in sage/notebook/server/css.py.
I wish somebody would do that and send me a patch.

Note that if you just shrink the space on your machine, it will actually
completely cover up all the controls on the top on many other machines.
It's very very system dependent.  Having extra space is the only reasonable
solution until somebody sits down and does this right.
```


Issue created by migration from https://trac.sagemath.org/ticket/643





---

archive/issue_comments_003318.json:
```json
{
    "body": "timothy clemans wrote this example, which seems to be a good idea -- it uses javascript",
    "created_at": "2007-09-12T22:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3318",
    "user": "was"
}
```

timothy clemans wrote this example, which seems to be a good idea -- it uses javascript



---

archive/issue_comments_003319.json:
```json
{
    "body": "Attachment [example.html](tarball://root/attachments/some-uuid/ticket643/example.html) by mhansen created at 2007-09-21 03:54:13",
    "created_at": "2007-09-21T03:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3319",
    "user": "mhansen"
}
```

Attachment [example.html](tarball://root/attachments/some-uuid/ticket643/example.html) by mhansen created at 2007-09-21 03:54:13



---

archive/issue_comments_003320.json:
```json
{
    "body": "Attachment [643.patch](tarball://root/attachments/some-uuid/ticket643/643.patch) by mhansen created at 2007-09-21 03:54:40",
    "created_at": "2007-09-21T03:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3320",
    "user": "mhansen"
}
```

Attachment [643.patch](tarball://root/attachments/some-uuid/ticket643/643.patch) by mhansen created at 2007-09-21 03:54:40



---

archive/issue_comments_003321.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T04:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3321",
    "user": "TimothyClemans"
}
```

Resolution: fixed



---

archive/issue_comments_003322.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-21T04:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3322",
    "user": "TimothyClemans"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_003323.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-21T04:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3323",
    "user": "TimothyClemans"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_003324.json:
```json
{
    "body": "This doesn't work for me at all.\n\nsee attached screenshot in ubuntu 7.04 linux.",
    "created_at": "2007-09-21T05:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3324",
    "user": "was"
}
```

This doesn't work for me at all.

see attached screenshot in ubuntu 7.04 linux.



---

archive/issue_comments_003325.json:
```json
{
    "body": "http://sage.math.washington.edu/tmp/snapshot1.png",
    "created_at": "2007-09-21T05:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3325",
    "user": "was"
}
```

http://sage.math.washington.edu/tmp/snapshot1.png



---

archive/issue_comments_003326.json:
```json
{
    "body": "Attachment [643.2.patch](tarball://root/attachments/some-uuid/ticket643/643.2.patch) by TimothyClemans created at 2007-09-21 15:38:46\n\nadded resize fix",
    "created_at": "2007-09-21T15:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3326",
    "user": "TimothyClemans"
}
```

Attachment [643.2.patch](tarball://root/attachments/some-uuid/ticket643/643.2.patch) by TimothyClemans created at 2007-09-21 15:38:46

added resize fix



---

archive/issue_comments_003327.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> http://sage.math.washington.edu/tmp/snapshot1.png\n\nOk I think I found what happened. I added the div before the last table in the top bar. It is kind of confusing since it is in _html_body instead of html_worksheet_topbar. I'll fix that and upload patch 3.",
    "created_at": "2007-09-21T15:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3327",
    "user": "TimothyClemans"
}
```

Replying to [comment:5 was]:
> http://sage.math.washington.edu/tmp/snapshot1.png

Ok I think I found what happened. I added the div before the last table in the top bar. It is kind of confusing since it is in _html_body instead of html_worksheet_topbar. I'll fix that and upload patch 3.



---

archive/issue_comments_003328.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2007-09-21T18:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3328",
    "user": "was"
}
```

Changing status from reopened to new.



---

archive/issue_comments_003329.json:
```json
{
    "body": "Changing assignee from boothby to was.",
    "created_at": "2007-09-21T18:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3329",
    "user": "was"
}
```

Changing assignee from boothby to was.



---

archive/issue_comments_003330.json:
```json
{
    "body": "Attachment [643.3.patch](tarball://root/attachments/some-uuid/ticket643/643.3.patch) by was created at 2007-09-21 18:56:54",
    "created_at": "2007-09-21T18:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3330",
    "user": "was"
}
```

Attachment [643.3.patch](tarball://root/attachments/some-uuid/ticket643/643.3.patch) by was created at 2007-09-21 18:56:54



---

archive/issue_comments_003331.json:
```json
{
    "body": "I made some changes to improve the notebook.  Could people try out my patch and see if it breaks / does anything stupid on other browsers?\n\nIt looks like there is a fair amount of cleaning up to do.",
    "created_at": "2007-10-03T06:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3331",
    "user": "mhansen"
}
```

I made some changes to improve the notebook.  Could people try out my patch and see if it breaks / does anything stupid on other browsers?

It looks like there is a fair amount of cleaning up to do.



---

archive/issue_comments_003332.json:
```json
{
    "body": "Attachment [css.patch](tarball://root/attachments/some-uuid/ticket643/css.patch) by mhansen created at 2007-10-03 06:50:29",
    "created_at": "2007-10-03T06:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3332",
    "user": "mhansen"
}
```

Attachment [css.patch](tarball://root/attachments/some-uuid/ticket643/css.patch) by mhansen created at 2007-10-03 06:50:29



---

archive/issue_comments_003333.json:
```json
{
    "body": "Attachment [toggle.2.patch](tarball://root/attachments/some-uuid/ticket643/toggle.2.patch) by mhansen created at 2007-10-04 06:57:24\n\nAccidental upload",
    "created_at": "2007-10-04T06:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3333",
    "user": "mhansen"
}
```

Attachment [toggle.2.patch](tarball://root/attachments/some-uuid/ticket643/toggle.2.patch) by mhansen created at 2007-10-04 06:57:24

Accidental upload



---

archive/issue_comments_003334.json:
```json
{
    "body": "Attachment [toggle.patch](tarball://root/attachments/some-uuid/ticket643/toggle.patch) by was created at 2007-10-04 19:02:45",
    "created_at": "2007-10-04T19:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3334",
    "user": "was"
}
```

Attachment [toggle.patch](tarball://root/attachments/some-uuid/ticket643/toggle.patch) by was created at 2007-10-04 19:02:45



---

archive/issue_comments_003335.json:
```json
{
    "body": "Please post one patch bundle, so I know what to actually apply.",
    "created_at": "2007-10-13T06:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3335",
    "user": "was"
}
```

Please post one patch bundle, so I know what to actually apply.



---

archive/issue_comments_003336.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T06:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3336",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_003337.json:
```json
{
    "body": "Very nice!",
    "created_at": "2007-10-13T06:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/643#issuecomment-3337",
    "user": "was"
}
```

Very nice!
