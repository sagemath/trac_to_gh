# Issue 3953: notebook -- make it so foo?? in the notebook shows the source code syntax highlighted

Issue created by migration from https://trac.sagemath.org/ticket/3953

Original creator: was

Original creation time: 2008-08-26 08:20:30

Assignee: boothby

Here's some relevant code by Gabriel Gellner -- a diff to server/support.py -- to this problem:

```
teragon-2:Downloads was$ diff ~/d/sage/sage/server/support.py support.py 
23a24,29
> from pygments import highlight
> from pygments.lexers import PythonLexer
> from pygments.formatters import HtmlFormatter
> 
> 
> 
218,220c224,228
<         src = sagedoc.format_src(src)
<         if not lineno is None:
<             src = "File: %s\nSource Code (starting at line %s):\n%s"%(filename, lineno, src)
---
>         #Slicing of the first 95 characters is a kluge to get rid of the doctype,
>         # really we should write our oun HtmlFormatter
>         src = highlight(src, PythonLexer(), HtmlFormatter(full=True))[94:]
>         #if not lineno is None:
>         #    src = "File: %s\nSource Code (starting at line %s):\n%s"%(filename, lineno, src)
```


This requires the pygments library to be installed. Also, the notebook will have to be
changed to not escape <'s etc. in the output of the source code window.  


---

Comment by mvngu created at 2009-08-12 16:35:53

Resolution: duplicate


---

Comment by mvngu created at 2009-08-12 16:35:53

This is a duplicate of #5653. Close it as per Mitesh Patel's suggestion.
