# Issue 7915: Improve TAB-completion in Macaulay2

archive/issues_007915.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: Macaulay2, interface, TAB-completion\n\nThere are the following problems with the current TAB-completion in Macaulay2:\n* it is slow and there is a special function which creates the list of commands and stores it in file for future use;\n* this function prints a message which is not visible in the notebook and it looks like the notebook stopped responding;\n* new objects defined by user or introduced by loaded packages do not appear in this static list;\n* TAB-completion for Macaulay2 objects shows the same list of more than 1000 names as for Macaulay2 sessions, most of the stuff in this list cannot be applied to the given object.\n\nThe attached patch changes trait_names functions so that\n* functions for building command lists execute reasonably fast for interaction (0.2-0.6 second on my machine);\n* both lists for an interpreter session and for objects in it are computed dynamically on each call and take into account loaded and created names;\n* only methods which can take an object as the first argument are shown for objects;\n* execution time for \"sage -t --optional macaulay2.py\" dropped from 3 minutes (which was really annoying me for the last 5 days) to 30 seconds. \n\nNew problem (doesn't need much attention, I think):\n* shortcuts like \"gens\" for \"generators\" are not displayed in both lists because of the way they are defined in Macaulay2, this is likely to be fixed in the next release (of Macaulay2).\n\nRemaining problem (to be addressed later):\n* Macaulay2 convention is to put \"the important argument\" last, so a useful function \"f\" will not be displayed in TAB-completion for \"x\" if it should be called like \"f(7, x)\" in Macaulay2. Since the default call corresponding to Sage command \"x.f(7)\" is \"f(x, 7)\", this is actually correct and \"f\" should not be listed. However, it may be useful to have an option to translate all calls of the form \"x.f(...)\" in Sage to \"f(..., x)\" in Macaulay2.\n\nPatches from #7897 are a prerequisite for this one.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7915\n\n",
    "created_at": "2010-01-13T04:24:27Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Improve TAB-completion in Macaulay2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7915",
    "user": "@novoselt"
}
```
Assignee: @williamstein

Keywords: Macaulay2, interface, TAB-completion

There are the following problems with the current TAB-completion in Macaulay2:
* it is slow and there is a special function which creates the list of commands and stores it in file for future use;
* this function prints a message which is not visible in the notebook and it looks like the notebook stopped responding;
* new objects defined by user or introduced by loaded packages do not appear in this static list;
* TAB-completion for Macaulay2 objects shows the same list of more than 1000 names as for Macaulay2 sessions, most of the stuff in this list cannot be applied to the given object.

The attached patch changes trait_names functions so that
* functions for building command lists execute reasonably fast for interaction (0.2-0.6 second on my machine);
* both lists for an interpreter session and for objects in it are computed dynamically on each call and take into account loaded and created names;
* only methods which can take an object as the first argument are shown for objects;
* execution time for "sage -t --optional macaulay2.py" dropped from 3 minutes (which was really annoying me for the last 5 days) to 30 seconds. 

New problem (doesn't need much attention, I think):
* shortcuts like "gens" for "generators" are not displayed in both lists because of the way they are defined in Macaulay2, this is likely to be fixed in the next release (of Macaulay2).

Remaining problem (to be addressed later):
* Macaulay2 convention is to put "the important argument" last, so a useful function "f" will not be displayed in TAB-completion for "x" if it should be called like "f(7, x)" in Macaulay2. Since the default call corresponding to Sage command "x.f(7)" is "f(x, 7)", this is actually correct and "f" should not be listed. However, it may be useful to have an option to translate all calls of the form "x.f(...)" in Sage to "f(..., x)" in Macaulay2.

Patches from #7897 are a prerequisite for this one.

Issue created by migration from https://trac.sagemath.org/ticket/7915





---

archive/issue_comments_068875.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-13T04:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7915#issuecomment-68875",
    "user": "@novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068876.json:
```json
{
    "body": "Attachment [macaulay2_improved_tab.patch](tarball://root/attachments/some-uuid/ticket7915/macaulay2_improved_tab.patch) by @novoselt created at 2010-01-13 04:25:09",
    "created_at": "2010-01-13T04:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7915#issuecomment-68876",
    "user": "@novoselt"
}
```

Attachment [macaulay2_improved_tab.patch](tarball://root/attachments/some-uuid/ticket7915/macaulay2_improved_tab.patch) by @novoselt created at 2010-01-13 04:25:09



---

archive/issue_comments_068877.json:
```json
{
    "body": "Attachment [trac_7915_macaulay2_tab_completion.patch](tarball://root/attachments/some-uuid/ticket7915/trac_7915_macaulay2_tab_completion.patch) by @novoselt created at 2010-02-01 04:47:04",
    "created_at": "2010-02-01T04:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7915#issuecomment-68877",
    "user": "@novoselt"
}
```

Attachment [trac_7915_macaulay2_tab_completion.patch](tarball://root/attachments/some-uuid/ticket7915/trac_7915_macaulay2_tab_completion.patch) by @novoselt created at 2010-02-01 04:47:04



---

archive/issue_comments_068878.json:
```json
{
    "body": "Changed the patch name and the commit message to contain the ticket number.",
    "created_at": "2010-02-01T04:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7915#issuecomment-68878",
    "user": "@novoselt"
}
```

Changed the patch name and the commit message to contain the ticket number.



---

archive/issue_comments_068879.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-09T01:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7915#issuecomment-68879",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068880.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-07-09T01:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7915#issuecomment-68880",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_068881.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T03:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7915#issuecomment-68881",
    "user": "@qed777"
}
```

Resolution: fixed
