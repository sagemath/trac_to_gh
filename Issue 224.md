# Issue 224: doc browser -- doesn't parse "notebook input notation"

Issue created by migration from https://trac.sagemath.org/ticket/224

Original creator: was

Original creation time: 2007-01-28 04:54:42

Assignee: boothby


```
Timothy clemens:
Why is some code just as on
http://sage.math.washington.edu:8100/doc_browser?/prog/?node43.html
non-excutable in that worksheet?
```


Because the doc parser doesn't know about "notebook input format",
ironically.


---

Comment by dorian created at 2007-09-08 21:43:23

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

Comment by was created at 2007-09-09 15:51:41

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

Comment by was created at 2007-10-21 02:38:40

I think this is intentional.


---

Comment by mhansen created at 2009-01-19 13:25:15

Resolution: invalid


---

Comment by mhansen created at 2009-01-19 13:25:15

I think this is intentional as well.  I'm closing this as invalid.
