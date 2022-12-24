# Issue 7963: Downloading multiple worksheets does not work

archive/issues_007963.json:
```json
{
    "body": "Assignee: was\n\nCC:  timdumol jason\n\nI do the following:\n\n1. Start the notebook with `notebook()`\n2. click the checkboxes next to a few worksheets\n3. hit the \"Download\" button\n\nand I get an error:\n\n\n```\nThe resource /download_worksheets?filenames=admin/77___S_A_G_E___admin/76___S_A_G_E___admin/75___S_A_G_E___&sep=___S_A_G_E___ cannot be found.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7963\n\n",
    "created_at": "2010-01-17T10:18:51Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Downloading multiple worksheets does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7963",
    "user": "jason"
}
```
Assignee: was

CC:  timdumol jason

I do the following:

1. Start the notebook with `notebook()`
2. click the checkboxes next to a few worksheets
3. hit the "Download" button

and I get an error:


```
The resource /download_worksheets?filenames=admin/77___S_A_G_E___admin/76___S_A_G_E___admin/75___S_A_G_E___&sep=___S_A_G_E___ cannot be found.
```


Issue created by migration from https://trac.sagemath.org/ticket/7963





---

archive/issue_comments_069482.json:
```json
{
    "body": "I think this is a matter of\n\n```diff\n--- a/sagenb/data/sage/js/notebook_lib.js\n+++ b/sagenb/data/sage/js/notebook_lib.js\n@@ -1515,7 +1515,7 @@ function download_worksheets_button() {\n     /*\n     Downloads the set of checked worksheets as a zip file.\n     */\n-    window.location.replace(\"/download_worksheets?filenames=\" +\n+    window.location.replace(\"/download_worksheets.zip?filenames=\" +\n                             checked_worksheet_filenames() + \"&sep=\" + SEP);\n }\n```\n\nbut I haven't posted a patch, since #7908 and some of its dependencies make a lot of changes to `notebook_lib.js`.",
    "created_at": "2010-01-17T15:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7963#issuecomment-69482",
    "user": "mpatel"
}
```

I think this is a matter of

```diff
--- a/sagenb/data/sage/js/notebook_lib.js
+++ b/sagenb/data/sage/js/notebook_lib.js
@@ -1515,7 +1515,7 @@ function download_worksheets_button() {
     /*
     Downloads the set of checked worksheets as a zip file.
     */
-    window.location.replace("/download_worksheets?filenames=" +
+    window.location.replace("/download_worksheets.zip?filenames=" +
                             checked_worksheet_filenames() + "&sep=" + SEP);
 }
```

but I haven't posted a patch, since #7908 and some of its dependencies make a lot of changes to `notebook_lib.js`.



---

archive/issue_comments_069483.json:
```json
{
    "body": "Adds mpatel's suggested fix.",
    "created_at": "2010-01-19T08:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7963#issuecomment-69483",
    "user": "timdumol"
}
```

Adds mpatel's suggested fix.



---

archive/issue_comments_069484.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T08:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7963#issuecomment-69484",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069485.json:
```json
{
    "body": "Attachment [trac_7963-download-multiple-worksheets.patch](tarball://root/attachments/some-uuid/ticket7963/trac_7963-download-multiple-worksheets.patch) by timdumol created at 2010-01-19 08:58:00\n\nThis adds what mpatel suggested.",
    "created_at": "2010-01-19T08:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7963#issuecomment-69485",
    "user": "timdumol"
}
```

Attachment [trac_7963-download-multiple-worksheets.patch](tarball://root/attachments/some-uuid/ticket7963/trac_7963-download-multiple-worksheets.patch) by timdumol created at 2010-01-19 08:58:00

This adds what mpatel suggested.



---

archive/issue_comments_069486.json:
```json
{
    "body": "Thanks for making a patch!  It works for me, but I'm not sure I should review this by myself.",
    "created_at": "2010-01-20T04:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7963#issuecomment-69486",
    "user": "mpatel"
}
```

Thanks for making a patch!  It works for me, but I'm not sure I should review this by myself.



---

archive/issue_comments_069487.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-20T06:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7963#issuecomment-69487",
    "user": "acleone"
}
```

LGTM.



---

archive/issue_comments_069488.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T06:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7963#issuecomment-69488",
    "user": "acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069489.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T01:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7963#issuecomment-69489",
    "user": "mpatel"
}
```

Resolution: fixed
