# Issue 1590: notebook -- change it so changes are saved even in cells that aren't evaluated

archive/issues_001590.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n> On Dec 18, 12:51pm, pgdoyle <> wrote:\n> > Changes to my Sage notebooks are not always getting saved. I'm\n> > running Sage 2.9 from Firefox 2.0.0.11 on Mac OS 10.4.11 on a PowerMac\n> > G5.\n> \n> I've tried this now on with Safari instead of Firefox, and on a Linux\n> box instead of the Mac.  And it appears to me that in every case,\n> changes to any cell that doesn't get evaluated just get discarded when\n> you `Save & close'.  Now, I would think that this could be fixed,\n> because after all the notebook knows how to `Evaluate All', which must\n> require it to inform itself about all edits that have been done to\n> cells in the worksheet.  But, if for some reason this can't be fixed,\n> then I think users ought to be warned, because I don't think it will\n> be clear (it certainly wasn't to me) that unless you are careful to\n> evaluate any cell you change or any new cell you enter, you'll lose\n> your work.\n\nThe current behavior is not a bug and is exactly the way we designed\nit to work.  That said, I *do* want to change the implementation\nso that any time a cell is changed and the cursor leaves the cell\nor \"save & close\" is clicked, the changed version is sent back to the\nserver.  I think Tom Boothby has argued against this,\nwhich is why it hasn't happened already.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1590\n\n",
    "created_at": "2007-12-23T07:09:35Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "notebook -- change it so changes are saved even in cells that aren't evaluated",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1590",
    "user": "was"
}
```
Assignee: boothby


```
> On Dec 18, 12:51pm, pgdoyle <> wrote:
> > Changes to my Sage notebooks are not always getting saved. I'm
> > running Sage 2.9 from Firefox 2.0.0.11 on Mac OS 10.4.11 on a PowerMac
> > G5.
> 
> I've tried this now on with Safari instead of Firefox, and on a Linux
> box instead of the Mac.  And it appears to me that in every case,
> changes to any cell that doesn't get evaluated just get discarded when
> you `Save & close'.  Now, I would think that this could be fixed,
> because after all the notebook knows how to `Evaluate All', which must
> require it to inform itself about all edits that have been done to
> cells in the worksheet.  But, if for some reason this can't be fixed,
> then I think users ought to be warned, because I don't think it will
> be clear (it certainly wasn't to me) that unless you are careful to
> evaluate any cell you change or any new cell you enter, you'll lose
> your work.

The current behavior is not a bug and is exactly the way we designed
it to work.  That said, I *do* want to change the implementation
so that any time a cell is changed and the cursor leaves the cell
or "save & close" is clicked, the changed version is sent back to the
server.  I think Tom Boothby has argued against this,
which is why it hasn't happened already.
```


Issue created by migration from https://trac.sagemath.org/ticket/1590





---

archive/issue_comments_010122.json:
```json
{
    "body": "This was implemented some time before the notebook went to Twisted.  I'll try to do it again...",
    "created_at": "2008-01-02T23:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1590#issuecomment-10122",
    "user": "boothby"
}
```

This was implemented some time before the notebook went to Twisted.  I'll try to do it again...



---

archive/issue_comments_010123.json:
```json
{
    "body": "This one slipped through the cracks...",
    "created_at": "2008-03-16T18:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1590#issuecomment-10123",
    "user": "boothby"
}
```

This one slipped through the cracks...



---

archive/issue_comments_010124.json:
```json
{
    "body": "REVIEW:\n\n1. It works!\n\n2. This line is lame:\n\n```\n       if ctx.args.has_key('save_only'): \n```\n\ninstead you should test that the save_only key is there *and* equal to '1'. \nSince it would be very reasonable to write query code someday with save_only=0,\nand it would be mysteriously buggy. \n\n3. When 2 is fixed I recommend this for inclusion in Sage.",
    "created_at": "2008-03-16T20:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1590#issuecomment-10124",
    "user": "was"
}
```

REVIEW:

1. It works!

2. This line is lame:

```
       if ctx.args.has_key('save_only'): 
```

instead you should test that the save_only key is there *and* equal to '1'. 
Since it would be very reasonable to write query code someday with save_only=0,
and it would be mysteriously buggy. 

3. When 2 is fixed I recommend this for inclusion in Sage.



---

archive/issue_comments_010125.json:
```json
{
    "body": "Attachment [1590-autosave.patch](tarball://root/attachments/some-uuid/ticket1590/1590-autosave.patch) by boothby created at 2008-03-16 21:33:50",
    "created_at": "2008-03-16T21:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1590#issuecomment-10125",
    "user": "boothby"
}
```

Attachment [1590-autosave.patch](tarball://root/attachments/some-uuid/ticket1590/1590-autosave.patch) by boothby created at 2008-03-16 21:33:50



---

archive/issue_comments_010126.json:
```json
{
    "body": "Merged in Sage 2.10.4.final",
    "created_at": "2008-03-17T04:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1590#issuecomment-10126",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.final



---

archive/issue_comments_010127.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-17T04:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1590#issuecomment-10127",
    "user": "mabshoff"
}
```

Resolution: fixed
