# Issue 5644: make it so escape make the introspection window in the notebook disappear

Issue created by migration from https://trac.sagemath.org/ticket/5644

Original creator: was

Original creation time: 2009-03-30 21:39:54

Assignee: boothby

this was *the* most commonly requested features during Math 480B


---

Comment by mpatel created at 2009-04-18 09:01:37

See comment.


---

Attachment

The attached patch seems to work in Firefox 3 without breaking other functions.  I'm not sure about the purpose of

```
            if(browser_op) { focus_delay(id,true); }
```

Although I haven't copied this to the new conditional clause, the patch works in Opera 9, too.

By the way, I think the `halt_introspection();` statement just before the new code is unnecessary, since `handle_replacement_controls()` calls it before returning `true`.  But the patch leaves this alone.


---

Comment by mpatel created at 2009-04-18 11:54:16

To clarify:  This patch works for a "TAB" introspection window but not for a "SHIFT-ENTER" introspection window.  The latter is placed in cell_output_* instead of introspect_div_*, which is more difficult to make disappear, at least for me.

Because of this, I've changed this ticket's status to "needs work."  The TAB-only patch may be enough for some users.


---

Comment by mpatel created at 2009-04-18 13:42:42

On "SHIFT-ENTER" introspection: If you're feeling adventurous, replace the new lines in the patch with these:

```
    } else if((introspect_id == id) && introspection_loaded) {
        if(key_close_helper(e)) {
            halt_introspection();
            return false; //otherwise, keep going
        }
    } else {
        output_html = get_element('cell_output_html_'+id);
        pre0 = output_html.getElementsByTagName('pre')[0];
        if (pre0 && (pre0.getAttribute('class') === 'introspection') && key_close_helper(e)) {
            output_html.removeChild(pre0);
            return false; //otherwise, keep going
        }
```

Note: This doesn't tell the server about any changes!  I don't know exactly how this plays out in practice.


---

Comment by mpatel created at 2009-05-07 00:39:16

Ultimately, perhaps it's better to "unify" the treatment of introspection windows.  That is, should the notebook place both TAB and SHIFT-ENTER results in a cell's dedicated `introspect_div_*`?  Then binding ESC to `halt_introspection()` should be enough. This may also simplify related code (e.g., see #6001).

At first glance, which is all I can muster right now, notebook treats TABS and SHIFT-ENTER differently enough that this is not a trivial change.


---

Comment by mpatel created at 2009-05-23 23:39:43

A first take at "unification:" Replace the end of `js.py`'s `set_output_text()` with something like

```
    if(introspect_id == id) {
        if (status == 'd') {
            introspection_loaded = true;
            introspection_text = introspect_html;
        }
        update_introspection_text();
    } else if(introspect_html != '') {
        introspect_id = id;
        introspection_loaded = true;
        introspection_text = introspect_html;
        update_introspection_text();
/*
        cell_output.innerHTML = '';
        cell_output_nowrap.innerHTML = '';
        cell_output_html.innerHTML = introspect_html;
        if (contains_jsmath(introspect_html)) {
            try {
                jsMath.ProcessBeforeShowing(cell_output_html);
            } catch(e) {
                cell_output.innerHTML = jsmath_font_msg + cell_output_html.innerHTML;
            }
        }
*/
    } else {
        introspect_id = id;
        introspection_loaded = true;
        introspection_text = '';
        update_introspection_text();
    }
```

Probably, it's _far_ better to eliminate all global variables, starting with those related to introspection.  This would
 * Make it easier to understand, maintain, and modify the code.
 * Permit independent (i.e., non-interfering) introspection windows for different cells.
 * Help with ticket #6001.
To be continued...


---

Comment by mpatel created at 2009-12-03 11:18:29

It's likely that #6855 will subsume this ticket.


---

Comment by mpatel created at 2010-01-18 05:49:36

#7666 subsumes this ticket.  Please close this ticket when that one merges.


---

Comment by timdumol created at 2010-01-19 03:04:30

Resolution: duplicate
