# Issue 4607: double backslash not properly handled in latex mode

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2008-11-25 00:05:55

Assignee: boothby

CC:  p.a.rombouts@home.nl

from [public bug collection](http://spreadsheets.google.com/pub?key=pCwvGVwSMxTzT6E2xNdo5fA):

Normally a double backslash '\\' forces a new line in LaTeX. However, when I type the following in a notebook input cell:

```
%latex
First line.\\
Second line.
```

the output looks like this:

```
      First line.line.
```


----

After a little fiddling, I discovered this effect can be achieved using three backslashes instead of two, but this is not correct behavior.
I first discovered this problem when I tried to render something like this in a sage notebook:

```
%latex
\[\theta(x)=\begin{cases}
0 & (x<0) \\
1 & (x\ge 0)
\end{cases}\]
```

The '1' is missing in the rendered output. The desired output can be obtained by using triple backslashes, but as I noted before, the is not correct behavior.

----

probably just needs proper escaping.



---

Comment by mhansen created at 2009-01-20 10:23:26

Resolution: duplicate


---

Comment by mhansen created at 2009-01-20 10:23:26

This is a duplicate of #3201.  I'll try to have the fix here in the next few days.
