# Issue 6459: make it so control-shift-enter sends a blank line to tinymce

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-03 15:16:51

Assignee: boothby

CC:  jason


```
From Pat LeSmithe:

Control-enter is bound to spliteval_cell.  To make control-shift-enter, say, insert a line break, try augmenting notebook.py's tinyMCE.init()'s setup with some code ripped from the Safari plug-in:

     // Around line 1840 of sage/server/notebook/notebook.py
     setup : function(ed) {
         ed.onKeyDown.add(function(ed, e) {
             // Make ctrl-shift-enter insert a line break.  Copied from
the Safari plug-in.
             if (e.keyCode == 13 && e.shiftKey && e.ctrlKey) {
                 // Workaround for missing shift+enter support,
http://bugs.webkit.org/show_bug.cgi?id=16973
                 var dom = ed.dom, s = ed.selection, r = s.getRng(), br;

                 // Insert BR element
                 r.insertNode(br = dom.create('br'));

                 // Place caret after BR
                 r.setStartAfter(br);
                 r.setEndAfter(br);
                 s.setRng(r);

                 // Could not place caret after BR then insert an nbsp
entity and move the caret
                 if (s.getSel().focusNode == br.previousSibling) {

s.select(dom.insertAfter(dom.doc.createTextNode('\u00a0'), br));
                     s.collapse(1);
                 }

                 // Scroll to new position, scrollIntoView can't be
used due to bug: http://bugs.webkit.org/show_bug.cgi?id=16117
                 ed.getWin().scrollTo(0,
dom.getPos(s.getRng().startContainer).y);

                 tinymce.dom.Event.cancel(e);
             }
         });
         // Make shift-enter quit editing.  This is the "old" code.
         ed.onKeyDown.add(function(ed, e) {
             if (key_enter_shift(key_event(e))) {
                 $(ed.formElement).submit();
             }
         })
     }

This seems to work on Linux in Firefox, Opera, and the Qt 4.5 WebKit
demo browser (e.g., /usr/lib64/qt4/demos/browser/browser).
```




---

Attachment

Tested in Cr3, FF3.5, and O9 on Linux and Cr2, FF3.5, IE8, O9, and S4 on XP.


---

Comment by mpatel created at 2009-07-17 01:43:44

Replying to [comment:1 mpatel]:
> Tested in Cr3, FF3.5, and O9 on Linux and Cr2, FF3.5, IE8, O9, and S4 on XP.

Confirmed, in the course of reviewing the new TinyMCE spkg at #6143.


---

Comment by kcrisman created at 2009-08-25 20:42:57

This does make FF3.5 work with this on OSX.5.  Interestingly, this key-binding already worked in Safari 4 (and continues to now).  Also, Ctrl-Enter appears to have same effect as Enter currently, so it already does something different than in an evaluation cell - for what that's worth.

I can't give a full positive review because I don't have access to any other browsers, nor am I competent to make sure it doesn't introduce a nasty bug, but partial positive review.  The rest of a review should not be hard.


---

Comment by mpatel created at 2009-08-30 08:40:47

Unfortunately, neither the existing bindings nor the simple Ctrl-Enter combination work consistently across browsers and platforms.  But if Ctrl-Enter happens to work, that's great!

For what it's worth: The patch still works in the latest versions of the browsers I list above.  (Cr3 is now Cr4 on Linux.)


---

Comment by mpatel created at 2009-08-30 17:31:49

Tweaked and rebased against #6568. Apply only this patch.


---

Attachment

Version 2:
 * Applies to #6568.
 * Fixes a problem with inserting a blank line when text is selected.  I noticed this problem in Safari on Windows XP.  This also fixes a related problem in Opera on Windows XP and Linux.
 * Adds a few comments and dedents/indents.

I think this ticket should be reviewed again (sorry!), since I don't have access to a Mac machine.


---

Comment by kcrisman created at 2009-09-01 13:37:32

Still works on Mac.  I still think needs review by someone who understands javascript and someone other than author who uses non-Mac.  mpatel, maybe you can ping some of the people on the thread where "Pat LeSmithe" makes the comment in the ticket description?  This shouldn't be hard to review for them


---

Comment by mpatel created at 2009-10-15 20:12:33

Initialization code moved to tinymce.js.  Rebased for #7196.  Apply only this patch.


---

Attachment

Remark:  The TinyMCE developers are [emphatic](http://wiki.moxiecode.com/index.php/TinyMCE:FAQ#TinyMCE_produce_BR_elements_on_enter.2Freturn_instead_of_P_elements.3F) about using P elements instead of BR elements.  If the `control-shift-enter` feature is broken, breaks, or otherwise causes problems, we might instead follow their CSS suggestion, `p {margin:0; padding: 0;}`, inside rich text cells.


---

Comment by jason created at 2009-10-15 21:04:03

I think the issue here was making multi-paragraph list items.  Maybe we could just make it so that pressing control-shift-enter in a list makes a new paragraph inside of an <li>.

It really seems that there should be an easier way of doing this.  I guess we are hampered by shift-enter, ctrl-enter, and alt-enter having more global meaning.


---

Comment by mpatel created at 2009-10-16 07:25:23

On lists: I was working from [this sage-devel post](http://groups.google.com/group/sage-devel/msg/1f5658399f500c24).  The current patch should work inside lists, too. 

On simplicity:  I think many of TinyMCE's source lines are devoted to similar tricks, although they may well be far more effective.

Just let me know what I should do.


---

Comment by mpatel created at 2009-10-16 07:28:55

Replying to [comment:11 mpatel]:
> Just let me know what I should do.
In particular, a SageNB-rebased patch for #5447 will also touch `sagenb/data/sage/html/notebook/head.tmpl`.


---

Comment by was created at 2009-10-17 07:32:11

Resolution: fixed


---

Comment by was created at 2009-10-17 07:32:11

Emphatic positive review. 

This is awesome!

Merged into sagenb-3.0.2, hence sage-4.2.
