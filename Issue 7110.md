# Issue 7110: [with patch, needs review] SageNB -- Port #4046, #6459, #6694, #6865, #6939

archive/issues_007110.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  timdumol was jason mhampton kcrisman mvngu\n\nKeywords: sagenb notebook\n\nPrimary authors and reviewers are at listed at\n\n* #4046\n* #6459\n* #6694\n* #6865\n* #6939\n\nSee #6983 for instructions on getting sagenb.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7110\n\n",
    "created_at": "2009-10-04T13:52:04Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch, needs review] SageNB -- Port #4046, #6459, #6694, #6865, #6939",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7110",
    "user": "mpatel"
}
```
Assignee: boothby

CC:  timdumol was jason mhampton kcrisman mvngu

Keywords: sagenb notebook

Primary authors and reviewers are at listed at

* #4046
* #6459
* #6694
* #6865
* #6939

See #6983 for instructions on getting sagenb.

Issue created by migration from https://trac.sagemath.org/ticket/7110





---

archive/issue_comments_058926.json:
```json
{
    "body": "Attachment [trac_7110-sagenb_ports.patch](tarball://root/attachments/some-uuid/ticket7110/trac_7110-sagenb_ports.patch) by mpatel created at 2009-10-04 14:52:11\n\nPort/merge/base #4046, #6459, #6694, #6865, #6939 for sagenb.",
    "created_at": "2009-10-04T14:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7110#issuecomment-58926",
    "user": "mpatel"
}
```

Attachment [trac_7110-sagenb_ports.patch](tarball://root/attachments/some-uuid/ticket7110/trac_7110-sagenb_ports.patch) by mpatel created at 2009-10-04 14:52:11

Port/merge/base #4046, #6459, #6694, #6865, #6939 for sagenb.



---

archive/issue_comments_058927.json:
```json
{
    "body": "Apart from rebasing existing patches, I've rearranged some files:\n\n* Moved `sagenb/data/templates/*_lib.js` to `sagenb/data/javascript/sage/*.js`.\n* Moved TinyMCE initialization code to `sagenb/data/javascript/sage/tinymce.js`.\n* Updated affected HTML templates.\n* On `notebook_lib.js`'s template macros:\n  * `SAGE_URL`: \"Replaced\" with [this URL](http://www.math.union.edu/~dpvc/jsMath/users/welcome.html) for now.  The [existing link](http://sage.math.washington.edu/sage/jsmath) is broken.\n  * `KEY_CODES`: \"Moved,\" in `twist.py`, to `javascript/sage/keys.js`.  They're still generated dynamically.\n\nHowever:\n\n* `notebook.js` and friends are now static, so they're not sent through `compress.JavaScriptCompressor`.  It may be much better to use the [YUI compressor](http://developer.yahoo.com/yui/compressor/).\n* There are two versions of `sage3d.js`.  Can we move one or both (after renaming) to `javascript/sage3d` or `javascript/sage/`?\n* jsMath initialization is not yet in `javascript/sage/jsmath.js`.  I'll do this at #4714.\n* A rebased jQuery / UI upgrade (cf. #5447) will move `farbtastic` to `jquery/plugins`.\n* Do we use `zorn`?\n* Perhaps we should organize `data/` differently.  By package?  Examples: `highlight` and `sage`, templates and images included.",
    "created_at": "2009-10-04T15:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7110#issuecomment-58927",
    "user": "mpatel"
}
```

Apart from rebasing existing patches, I've rearranged some files:

* Moved `sagenb/data/templates/*_lib.js` to `sagenb/data/javascript/sage/*.js`.
* Moved TinyMCE initialization code to `sagenb/data/javascript/sage/tinymce.js`.
* Updated affected HTML templates.
* On `notebook_lib.js`'s template macros:
  * `SAGE_URL`: "Replaced" with [this URL](http://www.math.union.edu/~dpvc/jsMath/users/welcome.html) for now.  The [existing link](http://sage.math.washington.edu/sage/jsmath) is broken.
  * `KEY_CODES`: "Moved," in `twist.py`, to `javascript/sage/keys.js`.  They're still generated dynamically.

However:

* `notebook.js` and friends are now static, so they're not sent through `compress.JavaScriptCompressor`.  It may be much better to use the [YUI compressor](http://developer.yahoo.com/yui/compressor/).
* There are two versions of `sage3d.js`.  Can we move one or both (after renaming) to `javascript/sage3d` or `javascript/sage/`?
* jsMath initialization is not yet in `javascript/sage/jsmath.js`.  I'll do this at #4714.
* A rebased jQuery / UI upgrade (cf. #5447) will move `farbtastic` to `jquery/plugins`.
* Do we use `zorn`?
* Perhaps we should organize `data/` differently.  By package?  Examples: `highlight` and `sage`, templates and images included.



---

archive/issue_comments_058928.json:
```json
{
    "body": "Attachment [trac_7110-sagenb_ports_v2.patch](tarball://root/attachments/some-uuid/ticket7110/trac_7110-sagenb_ports_v2.patch) by mpatel created at 2009-10-04 17:28:00\n\nv2: converted missed \"main.js\" in notebook.py.  Apply only this patch.",
    "created_at": "2009-10-04T17:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7110#issuecomment-58928",
    "user": "mpatel"
}
```

Attachment [trac_7110-sagenb_ports_v2.patch](tarball://root/attachments/some-uuid/ticket7110/trac_7110-sagenb_ports_v2.patch) by mpatel created at 2009-10-04 17:28:00

v2: converted missed "main.js" in notebook.py.  Apply only this patch.



---

archive/issue_comments_058929.json:
```json
{
    "body": "Patch v2 takes care of `\"main.js\"` in `notebook.list_javascript_window()`, although this function is currently unused, it seems.",
    "created_at": "2009-10-04T17:30:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7110#issuecomment-58929",
    "user": "mpatel"
}
```

Patch v2 takes care of `"main.js"` in `notebook.list_javascript_window()`, although this function is currently unused, it seems.



---

archive/issue_comments_058930.json:
```json
{
    "body": "For #5447, here are the SageNB patches:\n\n* http://sage.math.washington.edu/home/mpatel/trac/7110/trac_5447-sagenb_jquery_upgrade_part_A.patch\n* http://sage.math.washington.edu/home/mpatel/trac/7110/trac_5447-sagenb_jquery_upgrade_part_B.patch\n* http://sage.math.washington.edu/home/mpatel/trac/7110/trac_5447-sagenb_jquery_upgrade_part_C.patch\n\nPlease apply all three patches in lexicographical order ***after*** the [attachment:trac_7110-sagenb_ports_v2.patch patch above].",
    "created_at": "2009-10-04T19:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7110#issuecomment-58930",
    "user": "mpatel"
}
```

For #5447, here are the SageNB patches:

* http://sage.math.washington.edu/home/mpatel/trac/7110/trac_5447-sagenb_jquery_upgrade_part_A.patch
* http://sage.math.washington.edu/home/mpatel/trac/7110/trac_5447-sagenb_jquery_upgrade_part_B.patch
* http://sage.math.washington.edu/home/mpatel/trac/7110/trac_5447-sagenb_jquery_upgrade_part_C.patch

Please apply all three patches in lexicographical order ***after*** the [attachment:trac_7110-sagenb_ports_v2.patch patch above].



---

archive/issue_comments_058931.json:
```json
{
    "body": "Attachment [trac_7110-sagenb_ports_minimal.patch](tarball://root/attachments/some-uuid/ticket7110/trac_7110-sagenb_ports_minimal.patch) by mpatel created at 2009-10-11 13:38:22\n\nMinimal rebase of #4046, #6694, #6865, #6939 for SageNB.  Apply only this patch.",
    "created_at": "2009-10-11T13:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7110#issuecomment-58931",
    "user": "mpatel"
}
```

Attachment [trac_7110-sagenb_ports_minimal.patch](tarball://root/attachments/some-uuid/ticket7110/trac_7110-sagenb_ports_minimal.patch) by mpatel created at 2009-10-11 13:38:22

Minimal rebase of #4046, #6694, #6865, #6939 for SageNB.  Apply only this patch.



---

archive/issue_comments_058932.json:
```json
{
    "body": "The latest patch is just a minimal rebase of #4046, #6694, #6865, and #6939 for SageNB.",
    "created_at": "2009-10-11T13:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7110#issuecomment-58932",
    "user": "mpatel"
}
```

The latest patch is just a minimal rebase of #4046, #6694, #6865, and #6939 for SageNB.



---

archive/issue_comments_058933.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-11T19:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7110#issuecomment-58933",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058934.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-11T19:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7110#issuecomment-58934",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_058935.json:
```json
{
    "body": "I merged this into the official sagenb repo and pushed it.  And it works very nicely!",
    "created_at": "2009-10-11T19:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7110#issuecomment-58935",
    "user": "was"
}
```

I merged this into the official sagenb repo and pushed it.  And it works very nicely!
