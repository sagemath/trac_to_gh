# Issue 6507: [with patch, needs review] doc sidebar toggle

Issue created by migration from https://trac.sagemath.org/ticket/6507

Original creator: mpatel

Original creation time: 2009-07-10 11:05:10

Assignee: tba

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8c8fe7c5d0c0f725/4807f5553bdbd6b0#4807f5553bdbd6b0) for an early version.


---

Attachment

The new toggle highlights itself on mouse-over, runs the length of the content, auto-resizes itself, uses cookies, and should work in the live, static, and offline documentation in most browsers.  This includes Firefox, Opera, and the Qt WebKit demo browser on Linux.  Chromium, it seems, does not yet let offline pages set cookies, but more polish is on order.


---

Comment by timdumol created at 2009-07-27 09:16:25

I applied the patch on r12658 (Sage 4.1). There do not appear to be any differences in the UI.


---

Comment by mpatel created at 2009-07-27 09:57:06

Can you be more specific, e.g., about the browser and OS?  Did you rebuild the HTML documentation?

I should add that I don't have access to a machine running Mac OS.  It would be useful to know how it fares in multiple Mac OS browsers in all three scenarios (live, fast static, offline).

But first, we should try to get it working on some machine other than mine.

(In applying the patch, I got this warning:

```
Hunk #1 succeeded at 9 with fuzz 1 (offset -1 lines).
```

This is just a consequence of #6512.)


---

Comment by mpatel created at 2009-09-02 10:50:28

Apart from the "fuzz" mentioned above, the patch still appears to work for me.  I'm changing the summary to WPNR, but please let me know...


---

Comment by timdumol created at 2009-09-22 15:40:20

Works as advertised after a doc rebuild. Positive review.


---

Comment by mvngu created at 2009-09-23 02:43:47

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:44:47

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
