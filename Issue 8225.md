# Issue 8225: %time now hugely broken in sagenb-0.7.4 (sage-4.3.2)

archive/issues_008225.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\n\nOn Tue, Feb 9, 2010 at 1:22 PM, finotti <luis.finotti@gmail.com> wrote:\n> Dear all,\n>\n> Cells starting with \"%time\" stopped working with 4.3.2.  (It works\n> with 4.3.1.)  Is it no long supported or is it a bug? (time still\n> works with the command line.)\n>\n> Running on Linux 32-bit, ubuntu binary.\n>\n> Thanks,\n```\n\nWow, what a horrible, horrible regression!   Indeed, I've confirmed that what happens is that doing %time causes the notebook to hang forever, and be pretty broken thereafter.   Ouch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8225\n\n",
    "created_at": "2010-02-10T01:39:34Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "%time now hugely broken in sagenb-0.7.4 (sage-4.3.2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8225",
    "user": "was"
}
```
Assignee: was


```


On Tue, Feb 9, 2010 at 1:22 PM, finotti <luis.finotti@gmail.com> wrote:
> Dear all,
>
> Cells starting with "%time" stopped working with 4.3.2.  (It works
> with 4.3.1.)  Is it no long supported or is it a bug? (time still
> works with the command line.)
>
> Running on Linux 32-bit, ubuntu binary.
>
> Thanks,
```

Wow, what a horrible, horrible regression!   Indeed, I've confirmed that what happens is that doing %time causes the notebook to hang forever, and be pretty broken thereafter.   Ouch.

Issue created by migration from https://trac.sagemath.org/ticket/8225





---

archive/issue_comments_072628.json:
```json
{
    "body": "Attachment [trac_8225-timeit_notebook.patch](tarball://root/attachments/some-uuid/ticket8225/trac_8225-timeit_notebook.patch) by mpatel created at 2010-02-14 03:22:26\n\nFix `%time` and `%timeit`.  sagenb repo.",
    "created_at": "2010-02-14T03:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8225#issuecomment-72628",
    "user": "mpatel"
}
```

Attachment [trac_8225-timeit_notebook.patch](tarball://root/attachments/some-uuid/ticket8225/trac_8225-timeit_notebook.patch) by mpatel created at 2010-02-14 03:22:26

Fix `%time` and `%timeit`.  sagenb repo.



---

archive/issue_comments_072629.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-14T03:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8225#issuecomment-72629",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072630.json:
```json
{
    "body": "I can confirm that this patch fixes the problem with `%time` on 4.3.3, and `%timeit` also works, but doesn't work as it does on the command line -- there, `%timeit` runs multiple loops and so on. Is that how `%timeit` has always worked in the notebook?\n\nI don't know this particular code very well, but the patch appears to fix the problem and seems okay. So consider this a quite weak positive review.",
    "created_at": "2010-02-23T06:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8225#issuecomment-72630",
    "user": "ddrake"
}
```

I can confirm that this patch fixes the problem with `%time` on 4.3.3, and `%timeit` also works, but doesn't work as it does on the command line -- there, `%timeit` runs multiple loops and so on. Is that how `%timeit` has always worked in the notebook?

I don't know this particular code very well, but the patch appears to fix the problem and seems okay. So consider this a quite weak positive review.



---

archive/issue_comments_072631.json:
```json
{
    "body": "I think `%timeit` has worked that way in the notebook.  See [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/4346a582d393916c/a21fa13cb5d54ff7?q=timeit+group:sage-devel+notebook#).  The worksheet I mentioned is now [here](http://www.sagenb.org/home/pub/1518/).",
    "created_at": "2010-02-23T07:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8225#issuecomment-72631",
    "user": "mpatel"
}
```

I think `%timeit` has worked that way in the notebook.  See [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/4346a582d393916c/a21fa13cb5d54ff7?q=timeit+group:sage-devel+notebook#).  The worksheet I mentioned is now [here](http://www.sagenb.org/home/pub/1518/).



---

archive/issue_comments_072632.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T18:55:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8225#issuecomment-72632",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072633.json:
```json
{
    "body": "Remove assignee was.",
    "created_at": "2010-03-07T00:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8225#issuecomment-72633",
    "user": "mhansen"
}
```

Remove assignee was.



---

archive/issue_comments_072634.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-09T04:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8225#issuecomment-72634",
    "user": "mpatel"
}
```

Resolution: fixed
