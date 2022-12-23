# Issue 8123: Notebook inclusion of SVG files

Issue created by migration from https://trac.sagemath.org/ticket/8123

Original creator: nbruin

Original creation time: 2010-01-29 19:24:04

Assignee: was

CC:  mkoeppe

It seems that the notebook is close to serving "SVG" files in a way usable for SVG capable browser, but is not quite there:
If I try

```
sage: p = plot(x^2, -2, 2)
sage: p.save('xsquared.svg')
```

in the notebook, Firefox 3.5.2 gives me a "plugin needed" message and where the picture is supposed to be, I only get a placeholder.
If I save `xsquared.svg` and point my browser directly to it, firefox displays the picture, so Firefox 3.5.2 can understand the SVG produced. HTML code that succeeds in displaying the picture:

```
<html>
<body>
<object data="xsquared.svg">
</body>
</html>
```

So, it may be that the notebook simply needs to generate different HTML for including SVG files it finds. Alternatively, it may be a matter of serving the SVG file with the appropriate MIME type.


---

Comment by mpatel created at 2010-02-04 14:32:07

Try adding

```
image/svg+xml   svg svgz
```

to `/etc/mime.times`, then restarting the notebook server and the browser.  This works for me in Firefox 3.5.6 on 64-bit Fedora 10 Linux.


---

Comment by mpatel created at 2010-02-04 14:35:41

That should be `/etc/mime.types.`


---

Comment by mpatel created at 2010-02-04 14:47:01

Changing assignee from was to mpatel.


---

Comment by mpatel created at 2010-02-04 14:47:01

We may need to add `height` and `width` attributes for Opera and WebKit browsers.


---

Comment by mpatel created at 2010-02-04 14:47:12

Changing assignee from mpatel to was.


---

Comment by chapoton created at 2020-05-14 09:20:24

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-05-14 09:20:24

maybe we can also close this ancient ticket about the deprecated sagenb ?


---

Comment by kcrisman created at 2020-05-18 17:47:13

Could be worth checking out whether this works in Jupyter first - most of the other sagenb ones are definitely sagenb specific, but could be worth seeing whether 

```
sage: p = plot(x^2, -2, 2)
sage: p.save('xsquared.svg')
```

"works" as expected in Jupyter.  (I would hope all browsers would now support this though!)


---

Comment by dimpase created at 2020-07-31 12:03:21

It does work in jupyter. Closing.


---

Comment by dimpase created at 2020-07-31 12:03:21

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-14 15:43:16

Resolution: invalid
