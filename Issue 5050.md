# Issue 5050: clean up how the percent directives at the top of cells are processed

archive/issues_005050.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5050\n\n",
    "created_at": "2009-01-22T06:31:45Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "clean up how the percent directives at the top of cells are processed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5050",
    "user": "@mwhansen"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/5050





---

archive/issue_comments_038480.json:
```json
{
    "body": "Attachment [trac_5050.patch](tarball://root/attachments/some-uuid/ticket5050/trac_5050.patch) by @mwhansen created at 2009-01-22 06:41:54",
    "created_at": "2009-01-22T06:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5050#issuecomment-38480",
    "user": "@mwhansen"
}
```

Attachment [trac_5050.patch](tarball://root/attachments/some-uuid/ticket5050/trac_5050.patch) by @mwhansen created at 2009-01-22 06:41:54



---

archive/issue_comments_038481.json:
```json
{
    "body": "Notes from Mike looking at this:\n\n* Docs for parse_percent_directives needs to give what is returned\n* is_html doesn't need to call parse_percent_directives\n* url_to_self should have at least one line of documentation besides the examples\n* %hide and %hideall can also be cleaned up from the html and html_in methods (maybe other places)",
    "created_at": "2009-01-22T15:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5050#issuecomment-38481",
    "user": "@jasongrout"
}
```

Notes from Mike looking at this:

* Docs for parse_percent_directives needs to give what is returned
* is_html doesn't need to call parse_percent_directives
* url_to_self should have at least one line of documentation besides the examples
* %hide and %hideall can also be cleaned up from the html and html_in methods (maybe other places)



---

archive/issue_comments_038482.json:
```json
{
    "body": "Attachment [trac_5050-2.patch](tarball://root/attachments/some-uuid/ticket5050/trac_5050-2.patch) by @mwhansen created at 2009-01-22 15:40:29",
    "created_at": "2009-01-22T15:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5050#issuecomment-38482",
    "user": "@mwhansen"
}
```

Attachment [trac_5050-2.patch](tarball://root/attachments/some-uuid/ticket5050/trac_5050-2.patch) by @mwhansen created at 2009-01-22 15:40:29



---

archive/issue_comments_038483.json:
```json
{
    "body": "One positive review.  It's probably important enough that at least one other person ought to review it as well.\n\nMike and I stepped through the changes, they all look good, and I tested for about 20 minutes with various combinations of the directives and things seemed to work.  I had one glitch, but I can't reproduce it.  I had a cell that looked like:\n\n\n```\n%hide\n%hideall\nprint \"hi\"\n```\n\n\nI closed the cell, reopened it, then deleted all output, then did a few more things I can't remember.  At one point, the cell changed to:\n\n\n```\n%hide\n%hid\n```\n\n\nIf we can't reproduce something like this, though, I give it a positive review.",
    "created_at": "2009-01-22T16:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5050#issuecomment-38483",
    "user": "@jasongrout"
}
```

One positive review.  It's probably important enough that at least one other person ought to review it as well.

Mike and I stepped through the changes, they all look good, and I tested for about 20 minutes with various combinations of the directives and things seemed to work.  I had one glitch, but I can't reproduce it.  I had a cell that looked like:


```
%hide
%hideall
print "hi"
```


I closed the cell, reopened it, then deleted all output, then did a few more things I can't remember.  At one point, the cell changed to:


```
%hide
%hid
```


If we can't reproduce something like this, though, I give it a positive review.



---

archive/issue_comments_038484.json:
```json
{
    "body": "In the above glitch, I mean to say that I closed the *worksheet*, reopened it, etc...",
    "created_at": "2009-01-22T16:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5050#issuecomment-38484",
    "user": "@jasongrout"
}
```

In the above glitch, I mean to say that I closed the *worksheet*, reopened it, etc...



---

archive/issue_comments_038485.json:
```json
{
    "body": "Applies cleanly to Sage 3.3.alpha0, passes doctests, and seems to be working when I test it out. This is on Intel OSX 10.5.",
    "created_at": "2009-01-22T16:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5050#issuecomment-38485",
    "user": "@rlmill"
}
```

Applies cleanly to Sage 3.3.alpha0, passes doctests, and seems to be working when I test it out. This is on Intel OSX 10.5.



---

archive/issue_comments_038486.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T02:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5050#issuecomment-38486",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038487.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T02:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5050#issuecomment-38487",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1
