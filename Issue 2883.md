# Issue 2883: notebook -- typing in safari is sluggish!

Issue created by migration from https://trac.sagemath.org/ticket/2883

Original creator: boothby

Original creation time: 2008-04-11 23:30:44

Assignee: boothby

Typing in the current version of the notebook in Safari is significantly slower than typing on an Apple IIe running Windows Vista.  Fix it!


---

Attachment


---

Comment by was created at 2008-04-12 04:06:12

This patch is impossible to apply.  It has this line in it

```
@@ -790,6 +794,29 @@ function resize_all_cells() {
```

which is the only mention of the resize_all_cells function.  So it
depends on some other patch you didn't provide.


---

Comment by boothby created at 2008-04-12 06:50:42

Sorry, this depends on #2882


---

Comment by mabshoff created at 2008-04-13 00:37:01

I am getting rejects against my merge tree:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha4/devel/sage$ patch -p1 --dry-run < trac_2883-resize-flood.patch
patching file sage/server/notebook/cell.py
Hunk #1 FAILED at 646.
1 out of 1 hunk FAILED -- saving rejects to file sage/server/notebook/cell.py.rej
patching file sage/server/notebook/js.py
```

Please rebase against my merge tree alpah4 in the usual place.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-13 02:01:17


```
[03:19] <mabshoff> wstein-2901: the reject for #2883 is the following:
[03:20] <mabshoff> it is: onKeyUp    = 'return cell_input_resize(this);'
[03:20] <mabshoff> the patch expects: onKeyUp    = 'return cell_input_resize(%s);' 
[03:20] <mabshoff> And it want to replace it with: onKeyUp    = 'return input_keyup(%s, event);' 
[03:20] <wstein-2901> mabshoff -- it should be this.
[03:20] <wstein-2901> "this"
[03:20] <wstein-2901> Oh, I see.
[03:20] <wstein-2901> hmm.
[03:21] <wstein-2901> It should be: onKeyUp    = 'return input_keyup(%s, event);'
[03:21] <mabshoff> ok.
[03:21] <mabshoff> wstein-2901: merging it like that then
```



---

Comment by mabshoff created at 2008-04-13 02:03:06

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-13 02:03:06

Resolution: fixed
