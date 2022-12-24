# Issue 224: doc browser -- doesn't parse "notebook input notation"

archive/issues_000224.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nTimothy clemens:\nWhy is some code just as on\nhttp://sage.math.washington.edu:8100/doc_browser?/prog/?node43.html\nnon-excutable in that worksheet?\n```\n\n\nBecause the doc parser doesn't know about \"notebook input format\",\nironically.\n\nIssue created by migration from https://trac.sagemath.org/ticket/224\n\n",
    "created_at": "2007-01-28T04:54:42Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "doc browser -- doesn't parse \"notebook input notation\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/224",
    "user": "was"
}
```
Assignee: boothby


```
Timothy clemens:
Why is some code just as on
http://sage.math.washington.edu:8100/doc_browser?/prog/?node43.html
non-excutable in that worksheet?
```


Because the doc parser doesn't know about "notebook input format",
ironically.

Issue created by migration from https://trac.sagemath.org/ticket/224





---

archive/issue_comments_000998.json:
```json
{
    "body": "This ticket might actually be two questions.\n\n\n#### First, why does the doc browser not parse notebook input formatting?\nParsing \"notebook input format\" by the doc browser can be implemented very easily; but should it?\n\nIn the Programming guide: 5. Writing Optimized Compiled Code: A simple loop example: Sum of Squares, the example assumes the reader is not using an interactive tutorial, thus, the explicit explanation of notebook input notation would be confusing because the { and } braces would never actually be visible to the user; also, there would be an evaluable input cell with the content \"INPUT TEXT\" and corresponding output cell with \"OUTPUT TEXT\" which would return a Syntax Error upon an actual evaluation.\n\nPossible solutions are:\n- Re-write the relevant documentation with explanations of notebook notation removed where ever you really want the docHTMLprocessor to make an example cell.\n- OR, Leave it unevaluatable for the purpose of showing how the notebook works.\n\n#### Second, why are some code block examples not converted into cells?\nCode example blocks (<div class=\"verbatim\">) that don't begin with \"sage:\" are not parsed into cells because sometimes these examples really should not be cells (e.g. ref/module-sage.combinat.combinat.html; the parts that start \"INPUT:\")\n\nThis could be fixed by refining the dochtmlprocessor rules for what should be input.\n\n\nReplying to [ticket:224 was]:\n> {{{\n> Timothy clemens:\n> Why is some code just as on\n> http://sage.math.washington.edu:8100/doc_browser?/prog/?node43.html\n> non-excutable in that worksheet?\n> }}}\n> \n> Because the doc parser doesn't know about \"notebook input format\",\n> ironically.",
    "created_at": "2007-09-08T21:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/224#issuecomment-998",
    "user": "dorian"
}
```

This ticket might actually be two questions.


#### First, why does the doc browser not parse notebook input formatting?
Parsing "notebook input format" by the doc browser can be implemented very easily; but should it?

In the Programming guide: 5. Writing Optimized Compiled Code: A simple loop example: Sum of Squares, the example assumes the reader is not using an interactive tutorial, thus, the explicit explanation of notebook input notation would be confusing because the { and } braces would never actually be visible to the user; also, there would be an evaluable input cell with the content "INPUT TEXT" and corresponding output cell with "OUTPUT TEXT" which would return a Syntax Error upon an actual evaluation.

Possible solutions are:
- Re-write the relevant documentation with explanations of notebook notation removed where ever you really want the docHTMLprocessor to make an example cell.
- OR, Leave it unevaluatable for the purpose of showing how the notebook works.

#### Second, why are some code block examples not converted into cells?
Code example blocks (<div class="verbatim">) that don't begin with "sage:" are not parsed into cells because sometimes these examples really should not be cells (e.g. ref/module-sage.combinat.combinat.html; the parts that start "INPUT:")

This could be fixed by refining the dochtmlprocessor rules for what should be input.


Replying to [ticket:224 was]:
> {{{
> Timothy clemens:
> Why is some code just as on
> http://sage.math.washington.edu:8100/doc_browser?/prog/?node43.html
> non-excutable in that worksheet?
> }}}
> 
> Because the doc parser doesn't know about "notebook input format",
> ironically.



---

archive/issue_comments_000999.json:
```json
{
    "body": "Could we do the following:\n\n  a verbatim environment with both ` and ` in it is converted to a notebook cell,\n  unless %nocell appears in the previous line?  In the vast majority of cases, in the\n  long run, we'll want verbatim cells with {{{'s to be converted directly to notebook cells.\n\nE.g., where below the {{ should be thought of as {{{:\n\n\n```\nThis is how to write notebook mode:\n%nocell\n\\begin{verbatim}\n{{\n2+2\n///\n4\n}}\n\\end{verbatim}\n```\n",
    "created_at": "2007-09-09T15:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/224#issuecomment-999",
    "user": "was"
}
```

Could we do the following:

  a verbatim environment with both ` and ` in it is converted to a notebook cell,
  unless %nocell appears in the previous line?  In the vast majority of cases, in the
  long run, we'll want verbatim cells with {{{'s to be converted directly to notebook cells.

E.g., where below the {{ should be thought of as {{{:


```
This is how to write notebook mode:
%nocell
\begin{verbatim}
{{
2+2
///
4
}}
\end{verbatim}
```




---

archive/issue_comments_001000.json:
```json
{
    "body": "I think this is intentional.",
    "created_at": "2007-10-21T02:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/224#issuecomment-1000",
    "user": "was"
}
```

I think this is intentional.



---

archive/issue_comments_001001.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-19T13:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/224#issuecomment-1001",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_001002.json:
```json
{
    "body": "I think this is intentional as well.  I'm closing this as invalid.",
    "created_at": "2009-01-19T13:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/224#issuecomment-1002",
    "user": "mhansen"
}
```

I think this is intentional as well.  I'm closing this as invalid.
