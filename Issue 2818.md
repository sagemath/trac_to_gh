# Issue 2818: notebook -- document most functions in js.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-06 02:50:17

Assignee: boothby

This depends on #2813.


---

Attachment

+5!!!


---

Comment by mabshoff created at 2008-04-06 05:56:47

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
`@``@` -520,10 +652,16 `@``@` function get_cursor_position(cell) {
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

Comment by mabshoff created at 2008-04-06 06:18:42

Oops, as boothby just pointed out in IRC this depends on #2813.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-06 06:56:59

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-06 06:56:59

Resolution: fixed
