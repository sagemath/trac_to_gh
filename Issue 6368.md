# Issue 6368: shift-tab in the notebook should go back 4 spaces instead of going to the previous input cell

archive/issues_006368.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  timdumol\n\nRight now, in the notebook, usually shift-tab goes back to the previous input cell.  Since tab goes forward 4 spaces (or if text is highlighted, indents it), and shift-tab unindents highlighted text, it would by far make the most sense if shift-tab when no text is highlighted just goes back 4 spaces.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6368\n\n",
    "created_at": "2009-06-20T15:27:19Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "shift-tab in the notebook should go back 4 spaces instead of going to the previous input cell",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6368",
    "user": "was"
}
```
Assignee: boothby

CC:  timdumol

Right now, in the notebook, usually shift-tab goes back to the previous input cell.  Since tab goes forward 4 spaces (or if text is highlighted, indents it), and shift-tab unindents highlighted text, it would by far make the most sense if shift-tab when no text is highlighted just goes back 4 spaces.

Issue created by migration from https://trac.sagemath.org/ticket/6368





---

archive/issue_comments_050937.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T02:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6368#issuecomment-50937",
    "user": "acleone"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050938.json:
```json
{
    "body": "Attachment\n\nShould I add any Selenium tests?",
    "created_at": "2010-01-20T02:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6368#issuecomment-50938",
    "user": "acleone"
}
```

Attachment

Should I add any Selenium tests?



---

archive/issue_comments_050939.json:
```json
{
    "body": "Nice work!\n\n* This works as expected in Cr4, FF3.5.7, & S4 on Windows XP and Cr4 & FF3.5.6 on Linux.\n* In O10 on XP and Linux, shift-tab for non-empty selections was already broken and is still broken.\n* In IE8 on XP, auto-indentation and tab/shift-tab were already broken and they still are.\n\nWe can make new tickets for the latter two.  It seems that a given browser behaves more consistently across platforms than different browsers on a given platform, but it would be great to get feedback on various browsers on Mac OS.  Usually, we test what we can, e.g., the locally available combinations, ourselves and receive more varied data from the field (alphas, rcs, and releases).\n\nOn the Se tests:  Please feel free to try!  In my experience, Se does not handle at least some keys (e.g., TAB) consistently across browsers.  So far, we've tested mostly in Firefox.  It's relatively easy to set up Se Grid to test other browsers.  But I've found getting the Se tests to pass in more than one browser is a tedious affair.  Moreover, the results are very sensitive to seemingly innocuous changes in HTML, etc.  Nevertheless, we should refine and extend our suite to cover more notebook functions.",
    "created_at": "2010-01-20T05:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6368#issuecomment-50939",
    "user": "mpatel"
}
```

Nice work!

* This works as expected in Cr4, FF3.5.7, & S4 on Windows XP and Cr4 & FF3.5.6 on Linux.
* In O10 on XP and Linux, shift-tab for non-empty selections was already broken and is still broken.
* In IE8 on XP, auto-indentation and tab/shift-tab were already broken and they still are.

We can make new tickets for the latter two.  It seems that a given browser behaves more consistently across platforms than different browsers on a given platform, but it would be great to get feedback on various browsers on Mac OS.  Usually, we test what we can, e.g., the locally available combinations, ourselves and receive more varied data from the field (alphas, rcs, and releases).

On the Se tests:  Please feel free to try!  In my experience, Se does not handle at least some keys (e.g., TAB) consistently across browsers.  So far, we've tested mostly in Firefox.  It's relatively easy to set up Se Grid to test other browsers.  But I've found getting the Se tests to pass in more than one browser is a tedious affair.  Moreover, the results are very sensitive to seemingly innocuous changes in HTML, etc.  Nevertheless, we should refine and extend our suite to cover more notebook functions.



---

archive/issue_comments_050940.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T05:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6368#issuecomment-50940",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050941.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T01:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6368#issuecomment-50941",
    "user": "mpatel"
}
```

Resolution: fixed
