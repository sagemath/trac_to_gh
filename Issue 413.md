# Issue 413: saving non-evaluated cells

archive/issues_000413.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nOn 8/6/07, Ted Kosan <ted.kosan@gmail.com> wrote:\n> I am in the process of developing a standard format that typical\n> students can follow when using the Sage notebook.  Part of this\n> pattern consists of creating cells which contain only comments, like\n> the description of a problem that is being solved.  Since comments are\n> not executable code, a person would not normally think to press\n> <shift><enter> in these cells.\n> \n> Unfortunately, if text is entered into a cell without pressing\n> <shift><enter>, this text is lost even after the \"Save\" or \"Save and\n> close\" buttons are pressed.\n> \n> Can the behavior of these buttons be changed so that all text in all\n> cells is saved when they are pressed?\n\nYes, definitely.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/413\n\n",
    "created_at": "2007-08-09T07:45:41Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "saving non-evaluated cells",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/413",
    "user": "was"
}
```
Assignee: boothby


```
On 8/6/07, Ted Kosan <ted.kosan@gmail.com> wrote:
> I am in the process of developing a standard format that typical
> students can follow when using the Sage notebook.  Part of this
> pattern consists of creating cells which contain only comments, like
> the description of a problem that is being solved.  Since comments are
> not executable code, a person would not normally think to press
> <shift><enter> in these cells.
> 
> Unfortunately, if text is entered into a cell without pressing
> <shift><enter>, this text is lost even after the "Save" or "Save and
> close" buttons are pressed.
> 
> Can the behavior of these buttons be changed so that all text in all
> cells is saved when they are pressed?

Yes, definitely.
```


Issue created by migration from https://trac.sagemath.org/ticket/413





---

archive/issue_comments_002038.json:
```json
{
    "body": "\n```\nI think actually whenever text in any cell has changed and\n\n   (1) the cell looses focus, or\n   (2) the user clicks \"save\",\n\nthen the contents of that cell should be sent back to the server.\nI hate entering a little comment at the top of an input\ncell before a 20-second computation, and having to re-run\nthe computation just to record the comment. \n```\n",
    "created_at": "2007-08-09T07:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/413#issuecomment-2038",
    "user": "was"
}
```


```
I think actually whenever text in any cell has changed and

   (1) the cell looses focus, or
   (2) the user clicks "save",

then the contents of that cell should be sent back to the server.
I hate entering a little comment at the top of an input
cell before a 20-second computation, and having to re-run
the computation just to record the comment. 
```




---

archive/issue_comments_002039.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-17T04:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/413#issuecomment-2039",
    "user": "boothby"
}
```

Resolution: duplicate



---

archive/issue_comments_002040.json:
```json
{
    "body": "duplicated by #1590",
    "created_at": "2008-03-17T04:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/413#issuecomment-2040",
    "user": "boothby"
}
```

duplicated by #1590
