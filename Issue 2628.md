# Issue 2628: Literate notebook

archive/issues_002628.json:
```json
{
    "body": "Assignee: boothby\n\nA key advantage of notebook interfaces over the command-line is that they can allow for literate programming, that is, interspersing of formated text and code.  Literate programming  allows the user to explore their ideas both in theory and code simultaneously, and is particularly useful in mathematics were writing comments in pure ASCII is cumbersome and distracting.   Moreover, literate notebooks can be used as record of a computation (e.g. as the basis for an appendix to a paper), as an interactive tutorial for Sage, or for education (e.g. a calculus notebook using the \"interact\" feature to explore quadric surfaces).   Both Mathematica and Maple have extensive literate programming features. \n\nA simple way to provide this in Sage would be to have input cells of type \"%latex\" and \"%html\" behave as follows.  \n\n1) After (successfully) evaluating such a cell, the input would be hidden and only the output would be shown.  This output would be shifted to the left compared to where it is now so that the Sage input/output is indented relative to the text.  \n\n2) To edit, the user would (double?) click on the output and the input box would reappear.  \n\nSee the attached files for an example worksheet with mock-up of output.\n\nOverlap with SageTeX:\n\nDan Drake's excellent SageTeX also provides literate programming for Sage.   In practice, this is rather different than what is proposed here.   In particular, SageTeX is awkward to use to write Sage code in compared to the notebook because because of the multi-step (latex/sage/latex) process.   The strength of SageTeX is the quality of the final output and the fact that you have the whole of LaTeX to work with.   It would be nice if the notebook was able to export a SageTeX file.  (cf. Ticket #66)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2628\n\n",
    "created_at": "2008-03-21T15:42:05Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Literate notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2628",
    "user": "@NathanDunfield"
}
```
Assignee: boothby

A key advantage of notebook interfaces over the command-line is that they can allow for literate programming, that is, interspersing of formated text and code.  Literate programming  allows the user to explore their ideas both in theory and code simultaneously, and is particularly useful in mathematics were writing comments in pure ASCII is cumbersome and distracting.   Moreover, literate notebooks can be used as record of a computation (e.g. as the basis for an appendix to a paper), as an interactive tutorial for Sage, or for education (e.g. a calculus notebook using the "interact" feature to explore quadric surfaces).   Both Mathematica and Maple have extensive literate programming features. 

A simple way to provide this in Sage would be to have input cells of type "%latex" and "%html" behave as follows.  

1) After (successfully) evaluating such a cell, the input would be hidden and only the output would be shown.  This output would be shifted to the left compared to where it is now so that the Sage input/output is indented relative to the text.  

2) To edit, the user would (double?) click on the output and the input box would reappear.  

See the attached files for an example worksheet with mock-up of output.

Overlap with SageTeX:

Dan Drake's excellent SageTeX also provides literate programming for Sage.   In practice, this is rather different than what is proposed here.   In particular, SageTeX is awkward to use to write Sage code in compared to the notebook because because of the multi-step (latex/sage/latex) process.   The strength of SageTeX is the quality of the final output and the fact that you have the whole of LaTeX to work with.   It would be nice if the notebook was able to export a SageTeX file.  (cf. Ticket #66)



Issue created by migration from https://trac.sagemath.org/ticket/2628





---

archive/issue_comments_018059.json:
```json
{
    "body": "Mockup",
    "created_at": "2008-03-21T15:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2628#issuecomment-18059",
    "user": "@NathanDunfield"
}
```

Mockup



---

archive/issue_comments_018060.json:
```json
{
    "body": "Attachment [literate_notebook.png](tarball://root/attachments/some-uuid/ticket2628/literate_notebook.png) by @NathanDunfield created at 2008-03-21 15:46:54\n\n\"Source\" for mockup",
    "created_at": "2008-03-21T15:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2628#issuecomment-18060",
    "user": "@NathanDunfield"
}
```

Attachment [literate_notebook.png](tarball://root/attachments/some-uuid/ticket2628/literate_notebook.png) by @NathanDunfield created at 2008-03-21 15:46:54

"Source" for mockup



---

archive/issue_comments_018061.json:
```json
{
    "body": "Attachment [notebook.txt](tarball://root/attachments/some-uuid/ticket2628/notebook.txt) by @garyfurnish created at 2008-03-21 16:34:49",
    "created_at": "2008-03-21T16:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2628#issuecomment-18061",
    "user": "@garyfurnish"
}
```

Attachment [notebook.txt](tarball://root/attachments/some-uuid/ticket2628/notebook.txt) by @garyfurnish created at 2008-03-21 16:34:49



---

archive/issue_comments_018062.json:
```json
{
    "body": "In a sage-dev thread where folks also requested this feature, William pointed out the following work-around:\n\nHave you ever tried clicking the blue edit button in the upper right side of the screen?  It gives you a plain text representation  of the worksheet.  You can enter arbitrary HTML between the  cells (the !` `), and it appears looking more professional  when you click the \"Save and Use\" button.   In fact, internally  all the text between subsequent !` ` compute cells *is*  a TextCell.  There is also one bonus -- if you put math in $'s or $$'s, it will get typeset as mathematics.",
    "created_at": "2008-04-03T12:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2628#issuecomment-18062",
    "user": "@NathanDunfield"
}
```

In a sage-dev thread where folks also requested this feature, William pointed out the following work-around:

Have you ever tried clicking the blue edit button in the upper right side of the screen?  It gives you a plain text representation  of the worksheet.  You can enter arbitrary HTML between the  cells (the !` `), and it appears looking more professional  when you click the "Save and Use" button.   In fact, internally  all the text between subsequent !` ` compute cells *is*  a TextCell.  There is also one bonus -- if you put math in $'s or $$'s, it will get typeset as mathematics.



---

archive/issue_comments_018063.json:
```json
{
    "body": "I think this can probably be closed since TinyMCE (at #4705) was added.",
    "created_at": "2009-01-19T13:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2628#issuecomment-18063",
    "user": "@mwhansen"
}
```

I think this can probably be closed since TinyMCE (at #4705) was added.



---

archive/issue_comments_018064.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-19T13:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2628#issuecomment-18064",
    "user": "@mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_018065.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-19T13:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2628#issuecomment-18065",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018066.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-22T09:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2628#issuecomment-18066",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_018067.json:
```json
{
    "body": "I put a link on #66 back to this ticket.  I think we can close this now as being fixed by TinyMCE.",
    "created_at": "2009-01-22T09:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2628#issuecomment-18067",
    "user": "@mwhansen"
}
```

I put a link on #66 back to this ticket.  I think we can close this now as being fixed by TinyMCE.
