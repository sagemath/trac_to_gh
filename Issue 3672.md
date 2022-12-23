# Issue 3672: wrong hg repository url in documentation

Issue created by migration from https://trac.sagemath.org/ticket/3672

Original creator: schilly

Original creation time: 2008-07-18 09:58:05

Assignee: tba

** in `http://www.sagemath.org/doc/html/prog/node72.html` - last line
 * here:

```
/sage/doc$ grep -r "sagemath.org/sage//hg" *
prog/node31.html:cd "/home/jaap/sage/devel/doc" &amp;&amp; hg pull -u http://sagemath.org/sage//hg//doc-main
prog/node31.html:pulling from http://sagemath.org/sage//hg//doc-main
prog/node31.html:cd "/home/jaap/sage/devel/doc" &amp;&amp; hg bundle  tmphg http://sagemath.org/sage//hg//doc-main
```

 * ... and probably elsewhere, too:

replace `http://sagemath.org/sage/[/]hg` -> `http://hg.sagemath.org/` or `http://www.sagemath.org/hg/` (and probably a trailing "`sage-main`" in node31.html)

[backref: posting in sage-devel by bill hart](http://groups.google.com/group/sage-devel/msg/43f43fe73c851d44)


---

Comment by ddrake created at 2009-04-22 07:10:29

I think with the transition to Sphinx-based documentation (3.4) this has been fixed.


---

Comment by ddrake created at 2009-04-22 07:10:29

Resolution: fixed


---

Comment by ddrake created at 2009-04-22 07:11:38

In fact, I checked in the current Developer's Guide, and it's *definitely* fixed.
