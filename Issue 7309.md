# Issue 7309: SageNB -- Restructure /javascript/ to have /javascript/sage/

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-10-26 13:23:14

Assignee: boothby

CC:  was mpatel

The url layout serves `main.js` and `keyboard/` under `/javascript/`, yet serves everything else under its own directory -- `/javascript/jquery/`, `/javascript/sage3d`, etc. This patch moves `main.js` and `keyboard/` under `/javascript/sage/`.


---

Comment by timdumol created at 2009-10-26 13:25:44

Adds `/javascript/sage/` and updates `notebook_lib.js` and the html templates to use it.


---

Attachment


---

Comment by timdumol created at 2009-10-26 13:33:21

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-10-26 21:50:37

Fix TinyMCE init URL. See comment.  Apply only this patch.  Apply to sagenb repository.


---

Attachment

Version 2

 * Updates `tinymce.js`'s URL in `head.tmpl`.
 * Deletes `notebook.list_window.javascript()`.
 * Maps `sagenb/data/sage/js` to `/javascript/sage`.

Note: All of `sagenb/data/sage` is still accessible via `/java/sage`.

My original motivation for the admittedly unorthodox `/data/package` URLs for `package` in `[jsmath, jquery, sage, ...]` was that most non-trivial packages are a mix of HTML, CSS, images, JS, and/or Java, so it's better to group by package than by JS and Java, say.  But I did not realize the importance of the static-dynamic distinction, as you emphasized.  Two possibilities:

 * Serve `sagenb/data/package` as `/static/package`, since most of the files are static.
 * Serve a `package`'s dynamic files under `/javascript/package`, `/images/package`, `/css/package`, etc.
 * That is, serve
   * `main.js` from `/javascript/sage/main.js` and similarly for `keyboard`.
   * `main.css` from `/css/sage/main.css`.

Or:

 * Serve `sagenb/data/package` as `/something/package`, where `something` could be a better name than `data`.
 * Serve the dynamic files from the _same_ structure but overlaid virtually in `twist`.
 * That is, serve
   * `main.js` from `/something/sage/js/main.js` and similarly for `keyboard`.
   * `main.css` from `/something/sage/css/main.css`.

In either case, we could, I think, still use a fast separate server (e.g., [nginx](http://www.nginx.net/)) for the static files.  Or we could be explicit, e.g.,

```text/html
<script type="text/javascript" src="{% if static_server_url %}{{ static_server_url }}{% endif %}/[...]/jquery-1.3.2.min.js"></script>
<script type="text/javascript" src="{% if dynamic_server_url %}{{ dynamic_server_url }}{% endif %}/[...]/main.js"></script>
```

But I'm sure there are other options.  What do you think?


---

Comment by mpatel created at 2009-10-31 05:48:36

To the extent that it counts, my review is positive.


---

Comment by was created at 2009-11-11 19:32:24

Resolution: fixed


---

Comment by was created at 2009-11-11 19:32:24

merged into sagenb-0.4.2 (sage-4.2.1)


---

Comment by was created at 2009-11-11 19:32:43

(by the way mpatel gave it a positive-ish review, and I give it a positive review).
