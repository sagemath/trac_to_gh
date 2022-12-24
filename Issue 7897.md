# Issue 7897: Macaulay2 interface update/improvement for version 1.3.1

archive/issues_007897.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: Macaulay2, interface\n\nThese patches change the prompt detection/stripping and update doctests to cause no errors with Macaulay2 1.3.1.\n\nImprovements/fixes achieved:\n- examples in Macaulay2 documentation (which include input prompts) do not break the interaction with Sage;\n- empty/whitespace/comment lines can be executed;\n- multiline commands can be executed;\n- stripping output prompts will not cut error messages if they occur (e.g. the first call \"help Thing\" currently shows some errors in Macaulay2).\n\nThis is done by:\n- changing input and input continuation prompts;\n- starting with a big line number to make all output labels of the same width;\n- making sure that only output labels and spaces are stripped from the output.\n\nSide effects / Remaining issues:\n- \"restart\" command of Macaulay2 is handled separately when it is called like \"macaulay2.restart()\" since we need to repeat prompt adjustments;\n- this command cannot be used in the string code passed to Macaulay2, since it will cause a lock. Since this should not cause loss of data (if the user intentionally tried to restart Macaulay2), I think this is OK. Correct checking of all the code for \"restart\" in it would involve also checking if it is inside string constants. \n\nThese patches make tickets #7882 and #7888 unnecessary.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7897\n\n",
    "created_at": "2010-01-11T20:53:30Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Macaulay2 interface update/improvement for version 1.3.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7897",
    "user": "@novoselt"
}
```
Assignee: @williamstein

Keywords: Macaulay2, interface

These patches change the prompt detection/stripping and update doctests to cause no errors with Macaulay2 1.3.1.

Improvements/fixes achieved:
- examples in Macaulay2 documentation (which include input prompts) do not break the interaction with Sage;
- empty/whitespace/comment lines can be executed;
- multiline commands can be executed;
- stripping output prompts will not cut error messages if they occur (e.g. the first call "help Thing" currently shows some errors in Macaulay2).

This is done by:
- changing input and input continuation prompts;
- starting with a big line number to make all output labels of the same width;
- making sure that only output labels and spaces are stripped from the output.

Side effects / Remaining issues:
- "restart" command of Macaulay2 is handled separately when it is called like "macaulay2.restart()" since we need to repeat prompt adjustments;
- this command cannot be used in the string code passed to Macaulay2, since it will cause a lock. Since this should not cause loss of data (if the user intentionally tried to restart Macaulay2), I think this is OK. Correct checking of all the code for "restart" in it would involve also checking if it is inside string constants. 

These patches make tickets #7882 and #7888 unnecessary.

Issue created by migration from https://trac.sagemath.org/ticket/7897





---

archive/issue_comments_068683.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-11T20:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7897#issuecomment-68683",
    "user": "@novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068684.json:
```json
{
    "body": "I changed my mind about importance of \"restart\" command in the middle of the code after seeing a talk today. So the patch is rewritten to allow it everywhere. All doctests still pass with both patches applied.",
    "created_at": "2010-01-12T02:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7897#issuecomment-68684",
    "user": "@novoselt"
}
```

I changed my mind about importance of "restart" command in the middle of the code after seeing a talk today. So the patch is rewritten to allow it everywhere. All doctests still pass with both patches applied.



---

archive/issue_comments_068685.json:
```json
{
    "body": "Attachment [trac_7897_macaulay2_doctests_update.patch](tarball://root/attachments/some-uuid/ticket7897/trac_7897_macaulay2_doctests_update.patch) by @novoselt created at 2010-02-01 04:36:00",
    "created_at": "2010-02-01T04:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7897#issuecomment-68685",
    "user": "@novoselt"
}
```

Attachment [trac_7897_macaulay2_doctests_update.patch](tarball://root/attachments/some-uuid/ticket7897/trac_7897_macaulay2_doctests_update.patch) by @novoselt created at 2010-02-01 04:36:00



---

archive/issue_comments_068686.json:
```json
{
    "body": "Renamed patches and commit messages to follow conventions. Apply both patches starting with \"trac_7897\"",
    "created_at": "2010-02-01T04:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7897#issuecomment-68686",
    "user": "@novoselt"
}
```

Renamed patches and commit messages to follow conventions. Apply both patches starting with "trac_7897"



---

archive/issue_comments_068687.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-07-09T01:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7897#issuecomment-68687",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_068688.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-09T01:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7897#issuecomment-68688",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068689.json:
```json
{
    "body": "Also apply #5467 and #7915.",
    "created_at": "2010-07-09T01:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7897#issuecomment-68689",
    "user": "@mwhansen"
}
```

Also apply #5467 and #7915.



---

archive/issue_comments_068690.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T03:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7897#issuecomment-68690",
    "user": "@qed777"
}
```

Resolution: fixed
