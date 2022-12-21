# Issue 6853: [with patch, needs review] Templating tag typo

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-08-31 22:09:05

Assignee: boothby

CC:  timdumol

There is an incomplete closing script tag in `server/notebook/templates/notebook/head.tmpl`:

```
<script type="text/javascript" src="/javascript/sage3d.js"></script
```


I don't know if this actually affects any rendering engine.  I just noticed it when viewing the source for a worksheet page in Firefox.

This depends on #6568.



---

Attachment

Apply only this patch.


---

Comment by mpatel created at 2009-08-31 22:13:57

I'm not sure about why these lines appear in the patch:

```
-{% endmacro %}
\ No newline at end of file
+{% endmacro %}
```

These also appear in the new patch at #6459.


---

Comment by wjp created at 2009-09-01 19:39:16

Those lines mean the file that's being patched had no newline and the end of the file, but the new one does. (That's an improvement.)
In short, nothing to worry about.

Anyway, this patch applies (after #6568) and is clearly correct, so positive review.


---

Comment by mvngu created at 2009-09-03 08:16:57

Resolution: fixed
