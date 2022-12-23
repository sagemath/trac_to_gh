# Issue 6460: contentEditable cells

Issue created by migration from https://trac.sagemath.org/ticket/6460

Original creator: mpatel

Original creation time: 2009-07-03 18:28:23

Assignee: boothby

Experiments with new cell representations.  See, e.g.,

[wysiwyg mathematics](http://groups.google.com/group/sage-devel/browse_thread/thread/da578e3918f08709/da54258f1783b874?#da54258f1783b874)

[A variation on Rado's graph editor](http://groups.google.com/group/sage-devel/browse_thread/thread/0eea3e7faf475db6/e5e6be6e89d2c8b0?#e5e6be6e89d2c8b0)



---

Attachment

The new version should work in FF 3/3.5.  Nearly all of the changes are cosmetic.  See the code for details.  I didn't address the problems with iframes, since it's likely we'll go with another approach.


---

Comment by mpatel created at 2009-07-04 14:45:13

External window


---

Attachment

For what it's worth, I've attached an [attachment:graphed_ext.tbz2 example] that launches Rado's graph editor in a new, potentially reusable window, from a notebook cell.  Suggested directions:

 * Put `graphed_ext.html` and `processing.editor.min.js` in `$SAGE_ROOT/local/notebook/javascript/`.  I haven't edited the enclosed [Processing](http://processingjs.org/reference) library, but it may be different from Rado's latest.
 * Load `graphed.txt` as a worksheet.  The serialization code is from Rado's recent post about his elegant inline editor for the notebook.
 * Try, e.g., `g = graphs.CubeGraph(4)`, followed by `graph_editor(g, 'g_mod')`, say.  A pop-up blocker may complain.  I just allowed pop-ups from `localhost`.
 * See, e.g., [this link](http://www.w3schools.com/HTMLDOM/met_win_open.asp) for various window options.  To open the editor in a tab, check the browser settings for overrides and use `var win = window.open(url, name);` with the appropriate `url` and some `name`.  Different names will yield separate windows (or tabs).  The browser's security policy may prevent some actions, e.g., re-establishing client-side connections to reloaded parent worksheets.

It may be better to make some server-side changes.  Again, this is just an example.

A possible extension is the ability to keep a list of graphs in the new window and edit and export them in a random-access fashion --- a graph browser, perhaps.  Another is sharing an editor among multiple open worksheets.  The work on tearing out docstrings is somewhat related (cf. #6001).

Feel free to ask questions and make suggestions, though I'm a bit JavaScripted out just now...


---

Comment by mpatel created at 2009-08-04 03:25:10

The proper ticket for an interactive graph editor in Sage is actually #1321.  Sorry!


---

Comment by mpatel created at 2009-11-14 06:09:57

I think the scope here is too wide.  Please close this ticket.


---

Comment by mhansen created at 2009-11-15 14:16:20

Resolution: invalid
