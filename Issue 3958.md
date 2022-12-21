# Issue 3958: interact gives "unterminated string literal" in the browser

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-08-26 17:12:49

Assignee: itolkov

try:


```
`@`interact
def _(a=range_slider(-1,1),b=range_slider(-1,1),c=slider(-1,1),d=slider(-1,1)):
    pass
```

A browser error and a "truncated output" error result.  The resulting interact also is missing labels and the "c" slider.



---

Comment by itolkov created at 2008-08-27 00:37:29

This should be fixed with #3854.


---

Comment by mhansen created at 2008-08-27 00:46:14

This is fixed with #3854 applied.


---

Comment by mhansen created at 2008-08-27 00:46:14

Resolution: fixed
