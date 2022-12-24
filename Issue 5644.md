# Issue 5644: make it so escape make the introspection window in the notebook disappear

archive/issues_005644.json:
```json
{
    "body": "Assignee: boothby\n\nthis was *the* most commonly requested features during Math 480B\n\nIssue created by migration from https://trac.sagemath.org/ticket/5644\n\n",
    "created_at": "2009-03-30T21:39:54Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "make it so escape make the introspection window in the notebook disappear",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5644",
    "user": "was"
}
```
Assignee: boothby

this was *the* most commonly requested features during Math 480B

Issue created by migration from https://trac.sagemath.org/ticket/5644





---

archive/issue_comments_044077.json:
```json
{
    "body": "See comment.",
    "created_at": "2009-04-18T09:01:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5644#issuecomment-44077",
    "user": "mpatel"
}
```

See comment.



---

archive/issue_comments_044078.json:
```json
{
    "body": "Attachment [trac_5644_esc_kills_introspect.patch](tarball://root/attachments/some-uuid/ticket5644/trac_5644_esc_kills_introspect.patch) by mpatel created at 2009-04-18 09:17:56\n\nThe attached patch seems to work in Firefox 3 without breaking other functions.  I'm not sure about the purpose of\n\n```\n            if(browser_op) { focus_delay(id,true); }\n```\n\nAlthough I haven't copied this to the new conditional clause, the patch works in Opera 9, too.\n\nBy the way, I think the `halt_introspection();` statement just before the new code is unnecessary, since `handle_replacement_controls()` calls it before returning `true`.  But the patch leaves this alone.",
    "created_at": "2009-04-18T09:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5644#issuecomment-44078",
    "user": "mpatel"
}
```

Attachment [trac_5644_esc_kills_introspect.patch](tarball://root/attachments/some-uuid/ticket5644/trac_5644_esc_kills_introspect.patch) by mpatel created at 2009-04-18 09:17:56

The attached patch seems to work in Firefox 3 without breaking other functions.  I'm not sure about the purpose of

```
            if(browser_op) { focus_delay(id,true); }
```

Although I haven't copied this to the new conditional clause, the patch works in Opera 9, too.

By the way, I think the `halt_introspection();` statement just before the new code is unnecessary, since `handle_replacement_controls()` calls it before returning `true`.  But the patch leaves this alone.



---

archive/issue_comments_044079.json:
```json
{
    "body": "To clarify:  This patch works for a \"TAB\" introspection window but not for a \"SHIFT-ENTER\" introspection window.  The latter is placed in cell_output_* instead of introspect_div_*, which is more difficult to make disappear, at least for me.\n\nBecause of this, I've changed this ticket's status to \"needs work.\"  The TAB-only patch may be enough for some users.",
    "created_at": "2009-04-18T11:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5644#issuecomment-44079",
    "user": "mpatel"
}
```

To clarify:  This patch works for a "TAB" introspection window but not for a "SHIFT-ENTER" introspection window.  The latter is placed in cell_output_* instead of introspect_div_*, which is more difficult to make disappear, at least for me.

Because of this, I've changed this ticket's status to "needs work."  The TAB-only patch may be enough for some users.



---

archive/issue_comments_044080.json:
```json
{
    "body": "On \"SHIFT-ENTER\" introspection: If you're feeling adventurous, replace the new lines in the patch with these:\n\n```\n    } else if((introspect_id == id) && introspection_loaded) {\n        if(key_close_helper(e)) {\n            halt_introspection();\n            return false; //otherwise, keep going\n        }\n    } else {\n        output_html = get_element('cell_output_html_'+id);\n        pre0 = output_html.getElementsByTagName('pre')[0];\n        if (pre0 && (pre0.getAttribute('class') === 'introspection') && key_close_helper(e)) {\n            output_html.removeChild(pre0);\n            return false; //otherwise, keep going\n        }\n```\n\nNote: This doesn't tell the server about any changes!  I don't know exactly how this plays out in practice.",
    "created_at": "2009-04-18T13:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5644#issuecomment-44080",
    "user": "mpatel"
}
```

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

archive/issue_comments_044081.json:
```json
{
    "body": "Ultimately, perhaps it's better to \"unify\" the treatment of introspection windows.  That is, should the notebook place both TAB and SHIFT-ENTER results in a cell's dedicated `introspect_div_*`?  Then binding ESC to `halt_introspection()` should be enough. This may also simplify related code (e.g., see #6001).\n\nAt first glance, which is all I can muster right now, notebook treats TABS and SHIFT-ENTER differently enough that this is not a trivial change.",
    "created_at": "2009-05-07T00:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5644#issuecomment-44081",
    "user": "mpatel"
}
```

Ultimately, perhaps it's better to "unify" the treatment of introspection windows.  That is, should the notebook place both TAB and SHIFT-ENTER results in a cell's dedicated `introspect_div_*`?  Then binding ESC to `halt_introspection()` should be enough. This may also simplify related code (e.g., see #6001).

At first glance, which is all I can muster right now, notebook treats TABS and SHIFT-ENTER differently enough that this is not a trivial change.



---

archive/issue_comments_044082.json:
```json
{
    "body": "A first take at \"unification:\" Replace the end of `js.py`'s `set_output_text()` with something like\n\n```\n    if(introspect_id == id) {\n        if (status == 'd') {\n            introspection_loaded = true;\n            introspection_text = introspect_html;\n        }\n        update_introspection_text();\n    } else if(introspect_html != '') {\n        introspect_id = id;\n        introspection_loaded = true;\n        introspection_text = introspect_html;\n        update_introspection_text();\n/*\n        cell_output.innerHTML = '';\n        cell_output_nowrap.innerHTML = '';\n        cell_output_html.innerHTML = introspect_html;\n        if (contains_jsmath(introspect_html)) {\n            try {\n                jsMath.ProcessBeforeShowing(cell_output_html);\n            } catch(e) {\n                cell_output.innerHTML = jsmath_font_msg + cell_output_html.innerHTML;\n            }\n        }\n*/\n    } else {\n        introspect_id = id;\n        introspection_loaded = true;\n        introspection_text = '';\n        update_introspection_text();\n    }\n```\n\nProbably, it's *far* better to eliminate all global variables, starting with those related to introspection.  This would\n* Make it easier to understand, maintain, and modify the code.\n* Permit independent (i.e., non-interfering) introspection windows for different cells.\n* Help with ticket #6001.\nTo be continued...",
    "created_at": "2009-05-23T23:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5644#issuecomment-44082",
    "user": "mpatel"
}
```

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

Probably, it's *far* better to eliminate all global variables, starting with those related to introspection.  This would
* Make it easier to understand, maintain, and modify the code.
* Permit independent (i.e., non-interfering) introspection windows for different cells.
* Help with ticket #6001.
To be continued...



---

archive/issue_comments_044083.json:
```json
{
    "body": "It's likely that #6855 will subsume this ticket.",
    "created_at": "2009-12-03T11:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5644#issuecomment-44083",
    "user": "mpatel"
}
```

It's likely that #6855 will subsume this ticket.



---

archive/issue_comments_044084.json:
```json
{
    "body": "#7666 subsumes this ticket.  Please close this ticket when that one merges.",
    "created_at": "2010-01-18T05:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5644#issuecomment-44084",
    "user": "mpatel"
}
```

#7666 subsumes this ticket.  Please close this ticket when that one merges.



---

archive/issue_comments_044085.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5644#issuecomment-44085",
    "user": "timdumol"
}
```

Resolution: duplicate
