# Issue 8141: Update font stacks, sans-serif and monospace, for SageNB pages

Issue created by migration from https://trac.sagemath.org/ticket/8141

Original creator: mpatel

Original creation time: 2010-02-01 06:23:42

Assignee: was

CC:  timdumol was

Font families (typefaces?) on rendered Sage Notebook pages.

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/533afb39f9f8220f).

Note: Server administrators can already save

```
http://server/css/main.css
```

to

```
DOT_SAGE/notebook.css
```

and edit the latter, according to taste.

Links:

 * http://www.codestyle.org/css/font-family/BuildBetterCSSFontStacks.shtml
 * http://safalra.com/web-design/typography/web-safe-fonts-myth/
 * http://unitinteractive.com/blog/2008/06/26/better-css-font-stacks/


---

Attachment

More consistent use of font stack mixins.  sagenb repository.


---

Comment by mpatel created at 2010-02-01 06:34:24

The main purpose of the patch is to use the SASS font stack mixins in `sagenb/sass/src/partials/_mixins.sass` throughout the notebook stylesheets.

I've replaced the original sans-serif stack

```
"Gill Sans", "Gill Sans MT", "Myriad Pro", Myriad, "Liberation Sans", "Nimbus Sans L", Tahoma, Geneva, "Helvetica Neue", Helvetica, Arial, sans-serif
```

with

```
'Arial', 'Helvetica', sans-serif
```

in an attempt to reproduce the pre-#7786 fonts.  But I don't have a strong opinion on what we should use.  Feel free to use other sets!


---

Comment by mpatel created at 2010-02-05 07:08:24

Changing status from new to needs_review.


---

Attachment

Don't override non-compute cells' fonts.  Replaces previous.


---

Comment by mhampton created at 2010-02-25 21:42:06

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2010-02-25 21:42:06

This seems to work well in sage-4.3.3.  Checked on firefox and safari and it looks good.  Positive review.


---

Comment by mpatel created at 2010-03-04 22:50:55

Resolution: fixed
