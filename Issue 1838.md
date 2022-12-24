# Issue 1838: [with patch] comma in latex lists need a trailing space

archive/issues_001838.json:
```json
{
    "body": "Assignee: cwitty\n\nnormally, after writing a \",\" follows a space. latex needs this explicitly as \"\\,\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/1838\n\n",
    "created_at": "2008-01-18T21:45:02Z",
    "labels": [
        "misc",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch] comma in latex lists need a trailing space",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1838",
    "user": "@haraldschilly"
}
```
Assignee: cwitty

normally, after writing a "," follows a space. latex needs this explicitly as "\,"

Issue created by migration from https://trac.sagemath.org/ticket/1838





---

archive/issue_comments_011634.json:
```json
{
    "body": "Attachment [latex-lists-and-tables-with-a-space-after-the-comma.diff](tarball://root/attachments/some-uuid/ticket1838/latex-lists-and-tables-with-a-space-after-the-comma.diff) by @haraldschilly created at 2008-01-18 21:45:50",
    "created_at": "2008-01-18T21:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1838#issuecomment-11634",
    "user": "@haraldschilly"
}
```

Attachment [latex-lists-and-tables-with-a-space-after-the-comma.diff](tarball://root/attachments/some-uuid/ticket1838/latex-lists-and-tables-with-a-space-after-the-comma.diff) by @haraldschilly created at 2008-01-18 21:45:50



---

archive/issue_comments_011635.json:
```json
{
    "body": "This seems strange -- I never use explicit spaces (\"\\,\") in latex, preferring the system to do the layout as it sees best.  Is this really necessary?\n\nAlso, I can't believe this doesn't touch lots of doctests throughout the system.  It also has no doctests.",
    "created_at": "2008-01-22T18:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1838#issuecomment-11635",
    "user": "@ncalexan"
}
```

This seems strange -- I never use explicit spaces ("\,") in latex, preferring the system to do the layout as it sees best.  Is this really necessary?

Also, I can't believe this doesn't touch lots of doctests throughout the system.  It also has no doctests.



---

archive/issue_comments_011636.json:
```json
{
    "body": "well, i just thought this could be an easy fix without dependencies. i don't know where the doctests for latex expressions are, i have to look at them.\n\nlatex doesn't do it the right way. it just does what it is told to do but has no intelligence and white space is ignored inside formulas. that's why packages like amsmath redefine a lot, or introduce new commands for rather normal things (dots, triple integrals, ...). they all do a lot of \"intelligent\" white space management. an also well known example are matrices, where it defines the pmatrix environment. there all the spacings are corrected with negative spaces. or you need a \"\\;\" after the inner part before the \"dx\" when you type an integral. \n\nso, you have to do something but it's not crucial. trusting latex doesn't do the job.",
    "created_at": "2008-01-22T20:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1838#issuecomment-11636",
    "user": "@haraldschilly"
}
```

well, i just thought this could be an easy fix without dependencies. i don't know where the doctests for latex expressions are, i have to look at them.

latex doesn't do it the right way. it just does what it is told to do but has no intelligence and white space is ignored inside formulas. that's why packages like amsmath redefine a lot, or introduce new commands for rather normal things (dots, triple integrals, ...). they all do a lot of "intelligent" white space management. an also well known example are matrices, where it defines the pmatrix environment. there all the spacings are corrected with negative spaces. or you need a "\;" after the inner part before the "dx" when you type an integral. 

so, you have to do something but it's not crucial. trusting latex doesn't do the job.



---

archive/issue_comments_011637.json:
```json
{
    "body": "I don't think the \"right way\" is well defined--without the explicit space there is a bit more space after a comma than before, but just barely, and I think it looks fine. \n\nUnless things look really bad, I think we should error on the side of producing the cleanest, simplest latex--as something to avoid just look at the state of auto-generated HTML that tries to be faithful to a given WYSIWYG editor.",
    "created_at": "2008-01-23T04:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1838#issuecomment-11637",
    "user": "@robertwb"
}
```

I don't think the "right way" is well defined--without the explicit space there is a bit more space after a comma than before, but just barely, and I think it looks fine. 

Unless things look really bad, I think we should error on the side of producing the cleanest, simplest latex--as something to avoid just look at the state of auto-generated HTML that tries to be faithful to a given WYSIWYG editor.



---

archive/issue_comments_011638.json:
```json
{
    "body": "I don't think we want this patch at all.  While LaTeX does sometimes need some help with spacing, I've never heard of this being one of the problem cases.  Since Nick, Robert, and I agree (I think), I'm closing this bug as invalid for now.\n\nFeel free to reopen it if you get some more support for your position (like an example that looks a lot better with the spacing than without, or a style guide that requires the spacing).",
    "created_at": "2008-01-29T00:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1838#issuecomment-11638",
    "user": "cwitty"
}
```

I don't think we want this patch at all.  While LaTeX does sometimes need some help with spacing, I've never heard of this being one of the problem cases.  Since Nick, Robert, and I agree (I think), I'm closing this bug as invalid for now.

Feel free to reopen it if you get some more support for your position (like an example that looks a lot better with the spacing than without, or a style guide that requires the spacing).



---

archive/issue_comments_011639.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-01-29T00:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1838#issuecomment-11639",
    "user": "cwitty"
}
```

Resolution: invalid
