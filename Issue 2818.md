# Issue 2818: notebook -- document most functions in js.py

archive/issues_002818.json:
```json
{
    "body": "Assignee: boothby\n\nThis depends on #2813.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2818\n\n",
    "created_at": "2008-04-06T02:50:17Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "notebook -- document most functions in js.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2818",
    "user": "@williamstein"
}
```
Assignee: boothby

This depends on #2813.

Issue created by migration from https://trac.sagemath.org/ticket/2818





---

archive/issue_comments_019350.json:
```json
{
    "body": "Attachment [trac-2818-part1.patch](tarball://root/attachments/some-uuid/ticket2818/trac-2818-part1.patch) by boothby created at 2008-04-06 05:38:50\n\n+5!!!",
    "created_at": "2008-04-06T05:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2818#issuecomment-19350",
    "user": "boothby"
}
```

Attachment [trac-2818-part1.patch](tarball://root/attachments/some-uuid/ticket2818/trac-2818-part1.patch) by boothby created at 2008-04-06 05:38:50

+5!!!



---

archive/issue_comments_019351.json:
```json
{
    "body": "No dice:\n\n```\nhg import trac_2818-part1.patch\napplying trac_2818-part1.patch\npatching file sage/server/notebook/js.py\nHunk #7 FAILED at 651\nHunk #8 succeeded at 615 with fuzz 1 (offset -54 lines).\n1 out of 12 hunks FAILED -- saving rejects to file sage/server/notebook/js.py.rej\nabort: patch failed to apply\n```\n\nThe rejected hunk:\n\n```\n--- js.py\n+++ js.py\n@@ -520,10 +652,16 @@ function get_cursor_position(cell) {\n }\n\n function set_cursor_position(cell, n) {\n-    /* Move the cursor position in the cell to position n.\n+    /*\n+    Move the cursor position in the cell to position n.\n+\n+    WARNING: Does nothing when n is 0 on Opera at present.\n+\n     INPUT:\n         cell -- an actual cell in the DOM, returned by get_cell\n         n -- a non-negative integer\n+    OUTPUT:\n+        changes the position of the cursor.\n     */\n     if (browser_op && !n) {\n         // program around a \"bug\" in opera where using this\n```\n\n\nSo: am I missing a patch or does this need a rebase?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T05:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2818#issuecomment-19351",
    "user": "mabshoff"
}
```

No dice:

```
hg import trac_2818-part1.patch
applying trac_2818-part1.patch
patching file sage/server/notebook/js.py
Hunk #7 FAILED at 651
Hunk #8 succeeded at 615 with fuzz 1 (offset -54 lines).
1 out of 12 hunks FAILED -- saving rejects to file sage/server/notebook/js.py.rej
abort: patch failed to apply
```

The rejected hunk:

```
--- js.py
+++ js.py
@@ -520,10 +652,16 @@ function get_cursor_position(cell) {
 }

 function set_cursor_position(cell, n) {
-    /* Move the cursor position in the cell to position n.
+    /*
+    Move the cursor position in the cell to position n.
+
+    WARNING: Does nothing when n is 0 on Opera at present.
+
     INPUT:
         cell -- an actual cell in the DOM, returned by get_cell
         n -- a non-negative integer
+    OUTPUT:
+        changes the position of the cursor.
     */
     if (browser_op && !n) {
         // program around a "bug" in opera where using this
```


So: am I missing a patch or does this need a rebase?

Cheers,

Michael



---

archive/issue_comments_019352.json:
```json
{
    "body": "Oops, as boothby just pointed out in IRC this depends on #2813.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T06:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2818#issuecomment-19352",
    "user": "mabshoff"
}
```

Oops, as boothby just pointed out in IRC this depends on #2813.

Cheers,

Michael



---

archive/issue_comments_019353.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T06:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2818#issuecomment-19353",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_019354.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T06:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2818#issuecomment-19354",
    "user": "mabshoff"
}
```

Resolution: fixed
