# Issue 6742: Stylesheets are not always loaded in Chrome

Issue created by migration from https://trac.sagemath.org/ticket/6742

Original creator: mpatel

Original creation time: 2009-08-14 05:26:01

Assignee: boothby

Start a local Sage notebook server and open a worksheet list or any worksheet in Chrome.  The HTML is rendered strangely, as if `main.css` has not been retrieved.  In particular, "Searching for Sage server..." is always visible at the top of a worksheet, as are the slide controls.

However, the "Edit," "Text," "Undo," "Share," and "Publish" pages, say, are rendered properly.

This happens in Chrome 2 on Windows XP when connecting to a Fedora 10 Linux Sage notebook server on the same subnet.

[This](http://code.google.com/p/chromium/issues/detail?id=4181) might be relevant.

Curiously, this *does not* happen with worksheets at `sagenb.org`.


---

Attachment

Serve main.css with MIME type text/css.


---

Comment by mpatel created at 2009-08-14 06:52:57

With the attached patch, the notebook server now serves `main.css` with the MIME type `text/css`.  This placates Chrome, which now renders worksheets and the worksheet list properly.

In particular, the Web Inspector's console no longer contains the line

```
Resource interpreted as stylesheet but transferred with MIME type text/plain.
```

about `main.css`.  There are a similar messages

```
Resource interpreted as script but transferred with MIME type text/plain.
Resource interpreted as other but transferred with MIME type text/x-javascript.
```

for `main.js` and the jsMath extensions.  It seems that WebKit / Chrome lets this pass, for now.


---

Comment by mhansen created at 2009-09-01 22:43:39

Looks good to me.  Yep, this should also be done for the javascript code that is served up by twisted.


---

Comment by mvngu created at 2009-09-02 05:15:57

Resolution: fixed
