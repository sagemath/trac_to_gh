# Issue 7309: SageNB -- Restructure /javascript/ to have /javascript/sage/

archive/issues_007309.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was mpatel\n\nThe url layout serves `main.js` and `keyboard/` under `/javascript/`, yet serves everything else under its own directory -- `/javascript/jquery/`, `/javascript/sage3d`, etc. This patch moves `main.js` and `keyboard/` under `/javascript/sage/`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7309\n\n",
    "created_at": "2009-10-26T13:23:14Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "SageNB -- Restructure /javascript/ to have /javascript/sage/",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7309",
    "user": "timdumol"
}
```
Assignee: boothby

CC:  was mpatel

The url layout serves `main.js` and `keyboard/` under `/javascript/`, yet serves everything else under its own directory -- `/javascript/jquery/`, `/javascript/sage3d`, etc. This patch moves `main.js` and `keyboard/` under `/javascript/sage/`.

Issue created by migration from https://trac.sagemath.org/ticket/7309





---

archive/issue_comments_061040.json:
```json
{
    "body": "Adds `/javascript/sage/` and updates `notebook_lib.js` and the html templates to use it.",
    "created_at": "2009-10-26T13:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7309#issuecomment-61040",
    "user": "timdumol"
}
```

Adds `/javascript/sage/` and updates `notebook_lib.js` and the html templates to use it.



---

archive/issue_comments_061041.json:
```json
{
    "body": "Attachment [trac_7309-javascript-sage.patch](tarball://root/attachments/some-uuid/ticket7309/trac_7309-javascript-sage.patch) by timdumol created at 2009-10-26 13:25:56",
    "created_at": "2009-10-26T13:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7309#issuecomment-61041",
    "user": "timdumol"
}
```

Attachment [trac_7309-javascript-sage.patch](tarball://root/attachments/some-uuid/ticket7309/trac_7309-javascript-sage.patch) by timdumol created at 2009-10-26 13:25:56



---

archive/issue_comments_061042.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-26T13:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7309#issuecomment-61042",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061043.json:
```json
{
    "body": "Fix TinyMCE init URL. See comment.  Apply only this patch.  Apply to sagenb repository.",
    "created_at": "2009-10-26T21:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7309#issuecomment-61043",
    "user": "mpatel"
}
```

Fix TinyMCE init URL. See comment.  Apply only this patch.  Apply to sagenb repository.



---

archive/issue_comments_061044.json:
```json
{
    "body": "Attachment [trac_7309-javascript-sage_v2.patch](tarball://root/attachments/some-uuid/ticket7309/trac_7309-javascript-sage_v2.patch) by mpatel created at 2009-10-26 22:46:11\n\nVersion 2\n\n* Updates `tinymce.js`'s URL in `head.tmpl`.\n* Deletes `notebook.list_window.javascript()`.\n* Maps `sagenb/data/sage/js` to `/javascript/sage`.\n\nNote: All of `sagenb/data/sage` is still accessible via `/java/sage`.\n\nMy original motivation for the admittedly unorthodox `/data/package` URLs for `package` in `[jsmath, jquery, sage, ...]` was that most non-trivial packages are a mix of HTML, CSS, images, JS, and/or Java, so it's better to group by package than by JS and Java, say.  But I did not realize the importance of the static-dynamic distinction, as you emphasized.  Two possibilities:\n\n* Serve `sagenb/data/package` as `/static/package`, since most of the files are static.\n* Serve a `package`'s dynamic files under `/javascript/package`, `/images/package`, `/css/package`, etc.\n* That is, serve\n  * `main.js` from `/javascript/sage/main.js` and similarly for `keyboard`.\n  * `main.css` from `/css/sage/main.css`.\n\nOr:\n\n* Serve `sagenb/data/package` as `/something/package`, where `something` could be a better name than `data`.\n* Serve the dynamic files from the *same* structure but overlaid virtually in `twist`.\n* That is, serve\n  * `main.js` from `/something/sage/js/main.js` and similarly for `keyboard`.\n  * `main.css` from `/something/sage/css/main.css`.\n\nIn either case, we could, I think, still use a fast separate server (e.g., [nginx](http://www.nginx.net/)) for the static files.  Or we could be explicit, e.g.,\n\n```text/html\n<script type=\"text/javascript\" src=\"{% if static_server_url %}{{ static_server_url }}{% endif %}/[...]/jquery-1.3.2.min.js\"></script>\n<script type=\"text/javascript\" src=\"{% if dynamic_server_url %}{{ dynamic_server_url }}{% endif %}/[...]/main.js\"></script>\n```\n\nBut I'm sure there are other options.  What do you think?",
    "created_at": "2009-10-26T22:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7309#issuecomment-61044",
    "user": "mpatel"
}
```

Attachment [trac_7309-javascript-sage_v2.patch](tarball://root/attachments/some-uuid/ticket7309/trac_7309-javascript-sage_v2.patch) by mpatel created at 2009-10-26 22:46:11

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
* Serve the dynamic files from the *same* structure but overlaid virtually in `twist`.
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

archive/issue_comments_061045.json:
```json
{
    "body": "To the extent that it counts, my review is positive.",
    "created_at": "2009-10-31T05:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7309#issuecomment-61045",
    "user": "mpatel"
}
```

To the extent that it counts, my review is positive.



---

archive/issue_comments_061046.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-11T19:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7309#issuecomment-61046",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_061047.json:
```json
{
    "body": "merged into sagenb-0.4.2 (sage-4.2.1)",
    "created_at": "2009-11-11T19:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7309#issuecomment-61047",
    "user": "was"
}
```

merged into sagenb-0.4.2 (sage-4.2.1)



---

archive/issue_comments_061048.json:
```json
{
    "body": "(by the way mpatel gave it a positive-ish review, and I give it a positive review).",
    "created_at": "2009-11-11T19:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7309#issuecomment-61048",
    "user": "was"
}
```

(by the way mpatel gave it a positive-ish review, and I give it a positive review).
