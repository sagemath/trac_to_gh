# Issue 7501: notebook -- include codemirror in sage

archive/issues_007501.json:
```json
{
    "body": "Assignee: boothby\n\nAfter an extensive evaluation, we all decided that codemirror http://marijn.haverbeke.nl/codemirror/ is the best Javascript code editor to include in Sage.  It's faster and more robust than editarea.  Initially, we will include it *only* for editing `Data --> file`, then maybe later adapt it for input cells. \n\nSee this screenshot:  http://wstein.org/home/wstein/patches/codemirror.png\n\nIssue created by migration from https://trac.sagemath.org/ticket/7501\n\n",
    "created_at": "2009-11-20T09:20:21Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "notebook -- include codemirror in sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7501",
    "user": "was"
}
```
Assignee: boothby

After an extensive evaluation, we all decided that codemirror http://marijn.haverbeke.nl/codemirror/ is the best Javascript code editor to include in Sage.  It's faster and more robust than editarea.  Initially, we will include it *only* for editing `Data --> file`, then maybe later adapt it for input cells. 

See this screenshot:  http://wstein.org/home/wstein/patches/codemirror.png

Issue created by migration from https://trac.sagemath.org/ticket/7501





---

archive/issue_comments_063403.json:
```json
{
    "body": "Attachment [sagenb_7501-part2.patch](tarball://root/attachments/some-uuid/ticket7501/sagenb_7501-part2.patch) by was created at 2009-11-20 09:25:27",
    "created_at": "2009-11-20T09:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63403",
    "user": "was"
}
```

Attachment [sagenb_7501-part2.patch](tarball://root/attachments/some-uuid/ticket7501/sagenb_7501-part2.patch) by was created at 2009-11-20 09:25:27



---

archive/issue_comments_063404.json:
```json
{
    "body": "Positive review to William's patch, as a proof-of-concept patch.\n\nIn the end, codemirror gets included on every page---that shouldn't be.",
    "created_at": "2009-11-20T09:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63404",
    "user": "jason"
}
```

Positive review to William's patch, as a proof-of-concept patch.

In the end, codemirror gets included on every page---that shouldn't be.



---

archive/issue_comments_063405.json:
```json
{
    "body": "For the next step:  these people apparently worked on an autocompletion function:\n\nhttp://groups.google.com/group/codemirror/browse_frm/thread/37a078e69b26a213#",
    "created_at": "2009-11-20T11:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63405",
    "user": "jason"
}
```

For the next step:  these people apparently worked on an autocompletion function:

http://groups.google.com/group/codemirror/browse_frm/thread/37a078e69b26a213#



---

archive/issue_comments_063406.json:
```json
{
    "body": "I can rebase this and try to include it in SageNB 0.7.x (cf. #8051) or, perhaps, 0.8.",
    "created_at": "2010-02-04T05:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63406",
    "user": "mpatel"
}
```

I can rebase this and try to include it in SageNB 0.7.x (cf. #8051) or, perhaps, 0.8.



---

archive/issue_comments_063407.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-02-05T07:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63407",
    "user": "mpatel"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_063408.json:
```json
{
    "body": "See the description for links to rebased patches.  I've adjusted line numbers' style so they line up with the lines in the editor.",
    "created_at": "2010-02-05T16:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63408",
    "user": "mpatel"
}
```

See the description for links to rebased patches.  I've adjusted line numbers' style so they line up with the lines in the editor.



---

archive/issue_comments_063409.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-05T16:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63409",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063410.json:
```json
{
    "body": "I should have said that the \"rebased\" patches are actually new.  It seem easier to do this given the extent of changes to SageNB since the original patches were made.  Also, the original set\n\n* Includes `codemirror.js` on every page.\n* Refers to `parsesage.js` and `sage/css/pythoncolors.css`, which seem to be missing.  The new patches just use CodeMirror's Python parser and style.\n* Does not align the automatic line numbers with lines of text in the editor.\n\nPart A just adds CodeMirror to the repository.  Part B configures it for the data file page.",
    "created_at": "2010-02-07T12:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63410",
    "user": "mpatel"
}
```

I should have said that the "rebased" patches are actually new.  It seem easier to do this given the extent of changes to SageNB since the original patches were made.  Also, the original set

* Includes `codemirror.js` on every page.
* Refers to `parsesage.js` and `sage/css/pythoncolors.css`, which seem to be missing.  The new patches just use CodeMirror's Python parser and style.
* Does not align the automatic line numbers with lines of text in the editor.

Part A just adds CodeMirror to the repository.  Part B configures it for the data file page.



---

archive/issue_comments_063411.json:
```json
{
    "body": "Replying to [comment:7 mpatel]:\n>  * Includes `codemirror.js` on every page.\n\nOr more pages than necessary, at least.",
    "created_at": "2010-02-07T12:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63411",
    "user": "mpatel"
}
```

Replying to [comment:7 mpatel]:
>  * Includes `codemirror.js` on every page.

Or more pages than necessary, at least.



---

archive/issue_comments_063412.json:
```json
{
    "body": "Has any of this been tested on Solaris?",
    "created_at": "2010-02-22T00:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63412",
    "user": "drkirkby"
}
```

Has any of this been tested on Solaris?



---

archive/issue_comments_063413.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-22T00:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63413",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_063414.json:
```json
{
    "body": "Replying to [comment:9 drkirkby]:\n> Has any of this been tested on Solaris? \nI haven't.  But if you have a spare moment, please test the patches and let us know!  \n\nNote: CodeMirror runs entirely in the browser.",
    "created_at": "2010-02-22T00:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63414",
    "user": "mpatel"
}
```

Replying to [comment:9 drkirkby]:
> Has any of this been tested on Solaris? 
I haven't.  But if you have a spare moment, please test the patches and let us know!  

Note: CodeMirror runs entirely in the browser.



---

archive/issue_comments_063415.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-22T00:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63415",
    "user": "mpatel"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_063416.json:
```json
{
    "body": "I would never have enough time to test individuals patches. But William is keen a Solaris port is completed very soon and if things don't get checked, then it hampers that port. \n\nDave",
    "created_at": "2010-02-22T01:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63416",
    "user": "drkirkby"
}
```

I would never have enough time to test individuals patches. But William is keen a Solaris port is completed very soon and if things don't get checked, then it hampers that port. 

Dave



---

archive/issue_comments_063417.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-19T16:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63417",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063418.json:
```json
{
    "body": "Looks ok to me, and it is extremely unlikely that this can have any negative effect on *any* platform, since, as Mitesh said, it's totally in the browser.",
    "created_at": "2010-03-19T16:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63418",
    "user": "timdumol"
}
```

Looks ok to me, and it is extremely unlikely that this can have any negative effect on *any* platform, since, as Mitesh said, it's totally in the browser.



---

archive/issue_comments_063419.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-04T04:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7501#issuecomment-63419",
    "user": "timdumol"
}
```

Resolution: fixed
