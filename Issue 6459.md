# Issue 6459: make it so control-shift-enter sends a blank line to tinymce

archive/issues_006459.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jasongrout\n\n\n```\nFrom Pat LeSmithe:\n\nControl-enter is bound to spliteval_cell.  To make control-shift-enter, say, insert a line break, try augmenting notebook.py's tinyMCE.init()'s setup with some code ripped from the Safari plug-in:\n\n     // Around line 1840 of sage/server/notebook/notebook.py\n     setup : function(ed) {\n         ed.onKeyDown.add(function(ed, e) {\n             // Make ctrl-shift-enter insert a line break.  Copied from\nthe Safari plug-in.\n             if (e.keyCode == 13 && e.shiftKey && e.ctrlKey) {\n                 // Workaround for missing shift+enter support,\nhttp://bugs.webkit.org/show_bug.cgi?id=16973\n                 var dom = ed.dom, s = ed.selection, r = s.getRng(), br;\n\n                 // Insert BR element\n                 r.insertNode(br = dom.create('br'));\n\n                 // Place caret after BR\n                 r.setStartAfter(br);\n                 r.setEndAfter(br);\n                 s.setRng(r);\n\n                 // Could not place caret after BR then insert an nbsp\nentity and move the caret\n                 if (s.getSel().focusNode == br.previousSibling) {\n\ns.select(dom.insertAfter(dom.doc.createTextNode('\\u00a0'), br));\n                     s.collapse(1);\n                 }\n\n                 // Scroll to new position, scrollIntoView can't be\nused due to bug: http://bugs.webkit.org/show_bug.cgi?id=16117\n                 ed.getWin().scrollTo(0,\ndom.getPos(s.getRng().startContainer).y);\n\n                 tinymce.dom.Event.cancel(e);\n             }\n         });\n         // Make shift-enter quit editing.  This is the \"old\" code.\n         ed.onKeyDown.add(function(ed, e) {\n             if (key_enter_shift(key_event(e))) {\n                 $(ed.formElement).submit();\n             }\n         })\n     }\n\nThis seems to work on Linux in Firefox, Opera, and the Qt 4.5 WebKit\ndemo browser (e.g., /usr/lib64/qt4/demos/browser/browser).\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6459\n\n",
    "created_at": "2009-07-03T15:16:51Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "make it so control-shift-enter sends a blank line to tinymce",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6459",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @jasongrout


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



Issue created by migration from https://trac.sagemath.org/ticket/6459





---

archive/issue_comments_052099.json:
```json
{
    "body": "Attachment [trac_6459_tinymce_line_break.patch](tarball://root/attachments/some-uuid/ticket6459/trac_6459_tinymce_line_break.patch) by @qed777 created at 2009-07-11 11:33:51\n\nTested in Cr3, FF3.5, and O9 on Linux and Cr2, FF3.5, IE8, O9, and S4 on XP.",
    "created_at": "2009-07-11T11:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52099",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6459_tinymce_line_break.patch](tarball://root/attachments/some-uuid/ticket6459/trac_6459_tinymce_line_break.patch) by @qed777 created at 2009-07-11 11:33:51

Tested in Cr3, FF3.5, and O9 on Linux and Cr2, FF3.5, IE8, O9, and S4 on XP.



---

archive/issue_comments_052100.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> Tested in Cr3, FF3.5, and O9 on Linux and Cr2, FF3.5, IE8, O9, and S4 on XP.\n\nConfirmed, in the course of reviewing the new TinyMCE spkg at #6143.",
    "created_at": "2009-07-17T01:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52100",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:1 mpatel]:
> Tested in Cr3, FF3.5, and O9 on Linux and Cr2, FF3.5, IE8, O9, and S4 on XP.

Confirmed, in the course of reviewing the new TinyMCE spkg at #6143.



---

archive/issue_comments_052101.json:
```json
{
    "body": "This does make FF3.5 work with this on OSX.5.  Interestingly, this key-binding already worked in Safari 4 (and continues to now).  Also, Ctrl-Enter appears to have same effect as Enter currently, so it already does something different than in an evaluation cell - for what that's worth.\n\nI can't give a full positive review because I don't have access to any other browsers, nor am I competent to make sure it doesn't introduce a nasty bug, but partial positive review.  The rest of a review should not be hard.",
    "created_at": "2009-08-25T20:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52101",
    "user": "https://github.com/kcrisman"
}
```

This does make FF3.5 work with this on OSX.5.  Interestingly, this key-binding already worked in Safari 4 (and continues to now).  Also, Ctrl-Enter appears to have same effect as Enter currently, so it already does something different than in an evaluation cell - for what that's worth.

I can't give a full positive review because I don't have access to any other browsers, nor am I competent to make sure it doesn't introduce a nasty bug, but partial positive review.  The rest of a review should not be hard.



---

archive/issue_comments_052102.json:
```json
{
    "body": "Unfortunately, neither the existing bindings nor the simple Ctrl-Enter combination work consistently across browsers and platforms.  But if Ctrl-Enter happens to work, that's great!\n\nFor what it's worth: The patch still works in the latest versions of the browsers I list above.  (Cr3 is now Cr4 on Linux.)",
    "created_at": "2009-08-30T08:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52102",
    "user": "https://github.com/qed777"
}
```

Unfortunately, neither the existing bindings nor the simple Ctrl-Enter combination work consistently across browsers and platforms.  But if Ctrl-Enter happens to work, that's great!

For what it's worth: The patch still works in the latest versions of the browsers I list above.  (Cr3 is now Cr4 on Linux.)



---

archive/issue_comments_052103.json:
```json
{
    "body": "Tweaked and rebased against #6568. Apply only this patch.",
    "created_at": "2009-08-30T17:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52103",
    "user": "https://github.com/qed777"
}
```

Tweaked and rebased against #6568. Apply only this patch.



---

archive/issue_comments_052104.json:
```json
{
    "body": "Attachment [trac_6459_tinymce_line_break_v2.patch](tarball://root/attachments/some-uuid/ticket6459/trac_6459_tinymce_line_break_v2.patch) by @qed777 created at 2009-08-30 17:46:40\n\nVersion 2:\n* Applies to #6568.\n* Fixes a problem with inserting a blank line when text is selected.  I noticed this problem in Safari on Windows XP.  This also fixes a related problem in Opera on Windows XP and Linux.\n* Adds a few comments and dedents/indents.\n\nI think this ticket should be reviewed again (sorry!), since I don't have access to a Mac machine.",
    "created_at": "2009-08-30T17:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52104",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6459_tinymce_line_break_v2.patch](tarball://root/attachments/some-uuid/ticket6459/trac_6459_tinymce_line_break_v2.patch) by @qed777 created at 2009-08-30 17:46:40

Version 2:
* Applies to #6568.
* Fixes a problem with inserting a blank line when text is selected.  I noticed this problem in Safari on Windows XP.  This also fixes a related problem in Opera on Windows XP and Linux.
* Adds a few comments and dedents/indents.

I think this ticket should be reviewed again (sorry!), since I don't have access to a Mac machine.



---

archive/issue_comments_052105.json:
```json
{
    "body": "Still works on Mac.  I still think needs review by someone who understands javascript and someone other than author who uses non-Mac.  mpatel, maybe you can ping some of the people on the thread where \"Pat LeSmithe\" makes the comment in the ticket description?  This shouldn't be hard to review for them",
    "created_at": "2009-09-01T13:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52105",
    "user": "https://github.com/kcrisman"
}
```

Still works on Mac.  I still think needs review by someone who understands javascript and someone other than author who uses non-Mac.  mpatel, maybe you can ping some of the people on the thread where "Pat LeSmithe" makes the comment in the ticket description?  This shouldn't be hard to review for them



---

archive/issue_comments_052106.json:
```json
{
    "body": "Initialization code moved to tinymce.js.  Rebased for #7196.  Apply only this patch.",
    "created_at": "2009-10-15T20:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52106",
    "user": "https://github.com/qed777"
}
```

Initialization code moved to tinymce.js.  Rebased for #7196.  Apply only this patch.



---

archive/issue_comments_052107.json:
```json
{
    "body": "Attachment [trac_6459_tinymce_line_break_v3.patch](tarball://root/attachments/some-uuid/ticket6459/trac_6459_tinymce_line_break_v3.patch) by @qed777 created at 2009-10-15 20:23:53\n\nRemark:  The TinyMCE developers are [emphatic](http://wiki.moxiecode.com/index.php/TinyMCE:FAQ#TinyMCE_produce_BR_elements_on_enter.2Freturn_instead_of_P_elements.3F) about using P elements instead of BR elements.  If the `control-shift-enter` feature is broken, breaks, or otherwise causes problems, we might instead follow their CSS suggestion, `p {margin:0; padding: 0;}`, inside rich text cells.",
    "created_at": "2009-10-15T20:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52107",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6459_tinymce_line_break_v3.patch](tarball://root/attachments/some-uuid/ticket6459/trac_6459_tinymce_line_break_v3.patch) by @qed777 created at 2009-10-15 20:23:53

Remark:  The TinyMCE developers are [emphatic](http://wiki.moxiecode.com/index.php/TinyMCE:FAQ#TinyMCE_produce_BR_elements_on_enter.2Freturn_instead_of_P_elements.3F) about using P elements instead of BR elements.  If the `control-shift-enter` feature is broken, breaks, or otherwise causes problems, we might instead follow their CSS suggestion, `p {margin:0; padding: 0;}`, inside rich text cells.



---

archive/issue_comments_052108.json:
```json
{
    "body": "I think the issue here was making multi-paragraph list items.  Maybe we could just make it so that pressing control-shift-enter in a list makes a new paragraph inside of an <li>.\n\nIt really seems that there should be an easier way of doing this.  I guess we are hampered by shift-enter, ctrl-enter, and alt-enter having more global meaning.",
    "created_at": "2009-10-15T21:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52108",
    "user": "https://github.com/jasongrout"
}
```

I think the issue here was making multi-paragraph list items.  Maybe we could just make it so that pressing control-shift-enter in a list makes a new paragraph inside of an <li>.

It really seems that there should be an easier way of doing this.  I guess we are hampered by shift-enter, ctrl-enter, and alt-enter having more global meaning.



---

archive/issue_comments_052109.json:
```json
{
    "body": "On lists: I was working from [this sage-devel post](http://groups.google.com/group/sage-devel/msg/1f5658399f500c24).  The current patch should work inside lists, too. \n\nOn simplicity:  I think many of TinyMCE's source lines are devoted to similar tricks, although they may well be far more effective.\n\nJust let me know what I should do.",
    "created_at": "2009-10-16T07:25:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52109",
    "user": "https://github.com/qed777"
}
```

On lists: I was working from [this sage-devel post](http://groups.google.com/group/sage-devel/msg/1f5658399f500c24).  The current patch should work inside lists, too. 

On simplicity:  I think many of TinyMCE's source lines are devoted to similar tricks, although they may well be far more effective.

Just let me know what I should do.



---

archive/issue_comments_052110.json:
```json
{
    "body": "Replying to [comment:11 mpatel]:\n> Just let me know what I should do.\nIn particular, a SageNB-rebased patch for #5447 will also touch `sagenb/data/sage/html/notebook/head.tmpl`.",
    "created_at": "2009-10-16T07:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52110",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:11 mpatel]:
> Just let me know what I should do.
In particular, a SageNB-rebased patch for #5447 will also touch `sagenb/data/sage/html/notebook/head.tmpl`.



---

archive/issue_events_006699.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-10-17T07:32:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6459#event-6699"
}
```



---

archive/issue_comments_052111.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-17T07:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52111",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_052112.json:
```json
{
    "body": "Emphatic positive review. \n\nThis is awesome!\n\nMerged into sagenb-3.0.2, hence sage-4.2.",
    "created_at": "2009-10-17T07:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6459#issuecomment-52112",
    "user": "https://github.com/williamstein"
}
```

Emphatic positive review. 

This is awesome!

Merged into sagenb-3.0.2, hence sage-4.2.
