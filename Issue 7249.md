# Issue 7249: switch the notebook's templating system to Jinja2

archive/issues_007249.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  mhansen mpatel ddrake\n\nWe should switch the notebook's templating system from Jinja to Jinja2. Jinja2, among other things, makes i18n much easier.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7249\n\n",
    "created_at": "2009-10-19T08:44:15Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "switch the notebook's templating system to Jinja2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7249",
    "user": "ddrake"
}
```
Assignee: boothby

CC:  mhansen mpatel ddrake

We should switch the notebook's templating system from Jinja to Jinja2. Jinja2, among other things, makes i18n much easier.

Issue created by migration from https://trac.sagemath.org/ticket/7249





---

archive/issue_comments_060180.json:
```json
{
    "body": "apply to sagenb repo",
    "created_at": "2009-10-20T00:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60180",
    "user": "ddrake"
}
```

apply to sagenb repo



---

archive/issue_comments_060181.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-10-20T00:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60181",
    "user": "ddrake"
}
```

Attachment



---

archive/issue_comments_060182.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-20T00:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60182",
    "user": "ddrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060183.json:
```json
{
    "body": "#7269 should now include these changes.",
    "created_at": "2009-10-24T19:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60183",
    "user": "mpatel"
}
```

#7269 should now include these changes.



---

archive/issue_comments_060184.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-19T12:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60184",
    "user": "timdumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060185.json:
```json
{
    "body": "#7269 no longer includes these changes. Refer to comment:25:ticket:7269.\n\nChanges must be made to deal with unicode encoding/decoding before this can be reviewed.",
    "created_at": "2009-12-19T12:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60185",
    "user": "timdumol"
}
```

#7269 no longer includes these changes. Refer to comment:25:ticket:7269.

Changes must be made to deal with unicode encoding/decoding before this can be reviewed.



---

archive/issue_comments_060186.json:
```json
{
    "body": "Replying to [comment:3 timdumol]:\n> #7269 no longer includes these changes. Refer to comment:25:ticket:7269.\n> \n> Changes must be made to deal with unicode encoding/decoding before this can be reviewed.\n\nAt comment:24:ticket:7269 you say that we need Model-View-Presenter/Controller separation. How hard will that be? It sounds hard. :)  I've run into Unicode string problems while trying to internationalize the notebook, so I'd definitely like to do this if it's the right way to go about it.",
    "created_at": "2009-12-22T04:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60186",
    "user": "ddrake"
}
```

Replying to [comment:3 timdumol]:
> #7269 no longer includes these changes. Refer to comment:25:ticket:7269.
> 
> Changes must be made to deal with unicode encoding/decoding before this can be reviewed.

At comment:24:ticket:7269 you say that we need Model-View-Presenter/Controller separation. How hard will that be? It sounds hard. :)  I've run into Unicode string problems while trying to internationalize the notebook, so I'd definitely like to do this if it's the right way to go about it.



---

archive/issue_comments_060187.json:
```json
{
    "body": "MVC [1] separates the layers of the program into a model, which has the data; views, which are ways to present the data; and the controller/s, which control which data to show etc.\n\nCurrently the notebook serves as a model/controller and has some view functions mixed into it (`html_*`). Separating things will make things cleaner, and will make dealing with unicode easier: the view is presented with encoded byte strings, the controller deals with unicode strings, and data is retrieved from the model (db or filesystem) in encoded data which is converted to unicode strings.\n\nWithout this separation, one will need to check whether each string passed is an encoded byte string or a unicode string.\n\nSeparation will entail first removing the `html_*` functions, which in turn means restructuring the templates. I'll be working on that very soon.\n\n[1] http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller",
    "created_at": "2009-12-22T05:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60187",
    "user": "timdumol"
}
```

MVC [1] separates the layers of the program into a model, which has the data; views, which are ways to present the data; and the controller/s, which control which data to show etc.

Currently the notebook serves as a model/controller and has some view functions mixed into it (`html_*`). Separating things will make things cleaner, and will make dealing with unicode easier: the view is presented with encoded byte strings, the controller deals with unicode strings, and data is retrieved from the model (db or filesystem) in encoded data which is converted to unicode strings.

Without this separation, one will need to check whether each string passed is an encoded byte string or a unicode string.

Separation will entail first removing the `html_*` functions, which in turn means restructuring the templates. I'll be working on that very soon.

[1] http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller



---

archive/issue_comments_060188.json:
```json
{
    "body": "Converts much storage to unicode, and adds the necessary encoding for storage and networking. Uses jinja2 instead of jinja. Depends on #7835, #7786 and their dependencies.",
    "created_at": "2010-01-06T20:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60188",
    "user": "timdumol"
}
```

Converts much storage to unicode, and adds the necessary encoding for storage and networking. Uses jinja2 instead of jinja. Depends on #7835, #7786 and their dependencies.



---

archive/issue_comments_060189.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-06T20:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60189",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060190.json:
```json
{
    "body": "Attachment\n\nHopefully this patch will do the trick and make i18n easier.",
    "created_at": "2010-01-06T20:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60190",
    "user": "timdumol"
}
```

Attachment

Hopefully this patch will do the trick and make i18n easier.



---

archive/issue_comments_060191.json:
```json
{
    "body": "Attachment\n\nFix several doctests.  Replaces previous.",
    "created_at": "2010-01-06T21:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60191",
    "user": "mpatel"
}
```

Attachment

Fix several doctests.  Replaces previous.



---

archive/issue_comments_060192.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-06T22:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60192",
    "user": "mpatel"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060193.json:
```json
{
    "body": "V3:\n\n* Fixes a number of doctests.\n* `iamges` --> `images` in `cell.py`.\n* `inpit_text = input_text.decode('utf-8', str)` --> `input_text = input_text.decode('utf-8', 'ignore')` in `cell.py`.\n\nI'm not sure about the choice of `encode` / `decode` in some places.  Should we always `decode` instances of `str` and `encode` instances of `unicode`?  Could you please double-check the patch?  Also, would it be better to write and use a helper function to do the conversions?\n\nShould the changes to `cell.html` be at #7786?  Isn't `div_wrap` a `boolean`?\n\nDoes the change to `Worksheet.preparse` belong at #7835?\n\nIf we're planning to use unicode \"everywhere\", even for the worksheet / cell *system*, should we also **consistently** cover the relevant methods (and examples for) in `worksheet.py` and elsewhere?\n\nI apologize for my ignorance.",
    "created_at": "2010-01-06T22:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60193",
    "user": "mpatel"
}
```

V3:

* Fixes a number of doctests.
* `iamges` --> `images` in `cell.py`.
* `inpit_text = input_text.decode('utf-8', str)` --> `input_text = input_text.decode('utf-8', 'ignore')` in `cell.py`.

I'm not sure about the choice of `encode` / `decode` in some places.  Should we always `decode` instances of `str` and `encode` instances of `unicode`?  Could you please double-check the patch?  Also, would it be better to write and use a helper function to do the conversions?

Should the changes to `cell.html` be at #7786?  Isn't `div_wrap` a `boolean`?

Does the change to `Worksheet.preparse` belong at #7835?

If we're planning to use unicode "everywhere", even for the worksheet / cell *system*, should we also **consistently** cover the relevant methods (and examples for) in `worksheet.py` and elsewhere?

I apologize for my ignorance.



---

archive/issue_comments_060194.json:
```json
{
    "body": "Rebased vs. #7835 v2, #7786 v8, etc.  Replaces previous.",
    "created_at": "2010-01-07T02:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60194",
    "user": "mpatel"
}
```

Rebased vs. #7835 v2, #7786 v8, etc.  Replaces previous.



---

archive/issue_comments_060195.json:
```json
{
    "body": "Attachment\n\nV3 (really) is rebased against the latest at #7835, #7786.  Besides consistently using UTF-8 for the cell/worksheet system, I'm curious about `Cell.__init__`, where `str`s are `encode`d, not `decode`d.  Again, I'm not very familiar with encodings, so I may well be wrong.  Thanks!",
    "created_at": "2010-01-07T02:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60195",
    "user": "mpatel"
}
```

Attachment

V3 (really) is rebased against the latest at #7835, #7786.  Besides consistently using UTF-8 for the cell/worksheet system, I'm curious about `Cell.__init__`, where `str`s are `encode`d, not `decode`d.  Again, I'm not very familiar with encodings, so I may well be wrong.  Thanks!



---

archive/issue_comments_060196.json:
```json
{
    "body": "According to the [Python Unicode HOWTO](http://docs.python.org/dev/howto/unicode.html#reading-and-writing-unicode-data), we can use the [codecs.open](http://docs.python.org/library/codecs.html#codecs.open) to read from (decode) and write to (encode) files transparently.",
    "created_at": "2010-01-07T05:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60196",
    "user": "mpatel"
}
```

According to the [Python Unicode HOWTO](http://docs.python.org/dev/howto/unicode.html#reading-and-writing-unicode-data), we can use the [codecs.open](http://docs.python.org/library/codecs.html#codecs.open) to read from (decode) and write to (encode) files transparently.



---

archive/issue_comments_060197.json:
```json
{
    "body": "Replying to [comment:7 mpatel]:\n> V3:\n> \n>   * Fixes a number of doctests.\n>   * `iamges` --> `images` in `cell.py`.\n>   * `inpit_text = input_text.decode('utf-8', str)` --> `input_text = input_text.decode('utf-8', 'ignore')` in `cell.py`.\n> \n> I'm not sure about the choice of `encode` / `decode` in some places.  Should we always `decode` instances of `str` and `encode` instances of `unicode`?  Could you please double-check the patch?  Also, would it be better to write and use a helper function to do the conversions?\n> \n\nSure, and yes.\n\n> Should the changes to `cell.html` be at #7786?  Isn't `div_wrap` a `boolean`?\n\ndiv_wrap is a boolean. The div_wrap_ and wrap_ variables are workarounds to limitations present in Jinja2 but not in Jinja, so no, it's not for #7786.\n> \n> Does the change to `Worksheet.preparse` belong at #7835?\n\nSince this particular ticket is for Jinja2, which requires unicode, no. #7835 only replaces functionality that was previously present.\n\n> \n> If we're planning to use unicode \"everywhere\", even for the worksheet / cell *system*, should we also **consistently** cover the relevant methods (and examples for) in `worksheet.py` and elsewhere?\n\nYes, unicode functionality should be doctested.\n\n> \n> I apologize for my ignorance.",
    "created_at": "2010-01-10T06:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60197",
    "user": "timdumol"
}
```

Replying to [comment:7 mpatel]:
> V3:
> 
>   * Fixes a number of doctests.
>   * `iamges` --> `images` in `cell.py`.
>   * `inpit_text = input_text.decode('utf-8', str)` --> `input_text = input_text.decode('utf-8', 'ignore')` in `cell.py`.
> 
> I'm not sure about the choice of `encode` / `decode` in some places.  Should we always `decode` instances of `str` and `encode` instances of `unicode`?  Could you please double-check the patch?  Also, would it be better to write and use a helper function to do the conversions?
> 

Sure, and yes.

> Should the changes to `cell.html` be at #7786?  Isn't `div_wrap` a `boolean`?

div_wrap is a boolean. The div_wrap_ and wrap_ variables are workarounds to limitations present in Jinja2 but not in Jinja, so no, it's not for #7786.
> 
> Does the change to `Worksheet.preparse` belong at #7835?

Since this particular ticket is for Jinja2, which requires unicode, no. #7835 only replaces functionality that was previously present.

> 
> If we're planning to use unicode "everywhere", even for the worksheet / cell *system*, should we also **consistently** cover the relevant methods (and examples for) in `worksheet.py` and elsewhere?

Yes, unicode functionality should be doctested.

> 
> I apologize for my ignorance.



---

archive/issue_comments_060198.json:
```json
{
    "body": "Also, don't apologize for any supposed ignorance please. We're all ignorant.",
    "created_at": "2010-01-10T06:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60198",
    "user": "timdumol"
}
```

Also, don't apologize for any supposed ignorance please. We're all ignorant.



---

archive/issue_comments_060199.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-16T08:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60199",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060200.json:
```json
{
    "body": "The new patch fixes the styling of the worksheet listing page and adds two new functions in `sage.misc.misc`: `encoded_str` and `unicode_str` for encoding and decoding strings automatically.",
    "created_at": "2010-01-16T08:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60200",
    "user": "timdumol"
}
```

The new patch fixes the styling of the worksheet listing page and adds two new functions in `sage.misc.misc`: `encoded_str` and `unicode_str` for encoding and decoding strings automatically.



---

archive/issue_comments_060201.json:
```json
{
    "body": "Attachment\n\nFixes the styling of the worksheet listing page.",
    "created_at": "2010-01-16T23:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60201",
    "user": "timdumol"
}
```

Attachment

Fixes the styling of the worksheet listing page.



---

archive/issue_comments_060202.json:
```json
{
    "body": "This is the new patch queue:\n\n\n```\ntrac_7650-sagenb_doctesting_v6.patch\ntrac_7650-reviewer.patch\ntrac_7648-missing_indent.patch\ntrac_7663-rstrip_prompt.patch\ntrac_7847-empty-trash-no-referer.patch\ntrac_7786-template-jinja-idiomatic.patch\ntrac_7863-declare_vars_aux_js_v2.patch\ntrac_7874-typeset_interact_labels.patch\ntrac_7858-key_binding_vars_v2.patch\ntrac_7666-alphanumeric_cell_ids_B5.patch\ntrac_7666-reviewer.patch\ntrac_7835-preparsing-unicode_v2.patch\ntrac_7249_jinja2_v5.patch\n```\n",
    "created_at": "2010-01-17T21:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60202",
    "user": "timdumol"
}
```

This is the new patch queue:


```
trac_7650-sagenb_doctesting_v6.patch
trac_7650-reviewer.patch
trac_7648-missing_indent.patch
trac_7663-rstrip_prompt.patch
trac_7847-empty-trash-no-referer.patch
trac_7786-template-jinja-idiomatic.patch
trac_7863-declare_vars_aux_js_v2.patch
trac_7874-typeset_interact_labels.patch
trac_7858-key_binding_vars_v2.patch
trac_7666-alphanumeric_cell_ids_B5.patch
trac_7666-reviewer.patch
trac_7835-preparsing-unicode_v2.patch
trac_7249_jinja2_v5.patch
```




---

archive/issue_comments_060203.json:
```json
{
    "body": "Rebase on a new patch set.",
    "created_at": "2010-01-18T00:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60203",
    "user": "timdumol"
}
```

Rebase on a new patch set.



---

archive/issue_comments_060204.json:
```json
{
    "body": "Attachment\n\nAdded an 'ignore' errors directive to `unicode_string`",
    "created_at": "2010-01-18T01:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60204",
    "user": "timdumol"
}
```

Attachment

Added an 'ignore' errors directive to `unicode_string`



---

archive/issue_comments_060205.json:
```json
{
    "body": "In `notebook.py`, should `hunk = encoded_str(hunk)` be `hunk = unicode_str(hunk)`?\n\nIn `Cell.__init__`, can we simplify `self.set_input_text(str(input).replace('\\r',''))`?\n\nIn `twist.py`, do we need to call `unicode_str` on the incoming input?  The constructors and `set_input_text` do this.",
    "created_at": "2010-01-18T07:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60205",
    "user": "mpatel"
}
```

In `notebook.py`, should `hunk = encoded_str(hunk)` be `hunk = unicode_str(hunk)`?

In `Cell.__init__`, can we simplify `self.set_input_text(str(input).replace('\r',''))`?

In `twist.py`, do we need to call `unicode_str` on the incoming input?  The constructors and `set_input_text` do this.



---

archive/issue_comments_060206.json:
```json
{
    "body": "Also, evaluating `print '\u00e9'` raises\n\n```python\n          File \"/home/tmp/sagenb-0.5/src/sagenb/sagenb/notebook/twist.py\", line 1281, in render\n            cell.set_input_text(input_text)\n          File \"/home/tmp/sagenb-0.5/src/sagenb/sagenb/notebook/cell.py\", line 1270, in set_input_text\n            input = unicode_str(input)\n          File \"/home/tmp/sagenb-0.5/src/sagenb/sagenb/misc/misc.py\", line 441, in unicode_str\n            return unicode(str(obj), encoding, 'ignore')\n        exceptions.UnicodeEncodeError: 'ascii' codec can't encode character u'\\xe9' in position 7: ordinal not in range(128)\n\n```\n",
    "created_at": "2010-01-18T07:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60206",
    "user": "mpatel"
}
```

Also, evaluating `print 'é'` raises

```python
          File "/home/tmp/sagenb-0.5/src/sagenb/sagenb/notebook/twist.py", line 1281, in render
            cell.set_input_text(input_text)
          File "/home/tmp/sagenb-0.5/src/sagenb/sagenb/notebook/cell.py", line 1270, in set_input_text
            input = unicode_str(input)
          File "/home/tmp/sagenb-0.5/src/sagenb/sagenb/misc/misc.py", line 441, in unicode_str
            return unicode(str(obj), encoding, 'ignore')
        exceptions.UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 7: ordinal not in range(128)

```




---

archive/issue_comments_060207.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T07:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60207",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060208.json:
```json
{
    "body": "Nice catches. Here's a patch to fix them.",
    "created_at": "2010-01-18T07:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60208",
    "user": "timdumol"
}
```

Nice catches. Here's a patch to fix them.



---

archive/issue_comments_060209.json:
```json
{
    "body": "Adds the suggested fixes by mpatel.",
    "created_at": "2010-01-18T08:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60209",
    "user": "timdumol"
}
```

Adds the suggested fixes by mpatel.



---

archive/issue_comments_060210.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-18T08:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60210",
    "user": "timdumol"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_060211.json:
```json
{
    "body": "Attachment\n\nWoops! Sorry, accidentally put it to positive review. You should be the one, if ever.",
    "created_at": "2010-01-18T08:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60211",
    "user": "timdumol"
}
```

Attachment

Woops! Sorry, accidentally put it to positive review. You should be the one, if ever.



---

archive/issue_comments_060212.json:
```json
{
    "body": "Upon saving and quitting a worksheet that contains an evaluated `print `\u00e9`` cell, I see\n\n```python\nworksheet.py:1924: exceptions.UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal\n```\n\n\nWhat about the `unicode_str`s in `twist.py`?  I'm just wondering why we need them.\n\nMinor: It appears we can just call `encoded_str` in `sage_inspect.py`.\n\nAlso, can you slip some Unicode characters into the Se and/or doctests, so that we can detect potential regressions?",
    "created_at": "2010-01-18T08:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60212",
    "user": "mpatel"
}
```

Upon saving and quitting a worksheet that contains an evaluated `print `é`` cell, I see

```python
worksheet.py:1924: exceptions.UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
```


What about the `unicode_str`s in `twist.py`?  I'm just wondering why we need them.

Minor: It appears we can just call `encoded_str` in `sage_inspect.py`.

Also, can you slip some Unicode characters into the Se and/or doctests, so that we can detect potential regressions?



---

archive/issue_comments_060213.json:
```json
{
    "body": "I'm pretty sure that that warning is unavoidable (has to do with upgrading from non-unicode to unicode). The `unicode_str`s are there just out of paranoia. Nice catch with the sage_inspect.py thing. I'll update the tests now.",
    "created_at": "2010-01-18T09:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60213",
    "user": "timdumol"
}
```

I'm pretty sure that that warning is unavoidable (has to do with upgrading from non-unicode to unicode). The `unicode_str`s are there just out of paranoia. Nice catch with the sage_inspect.py thing. I'll update the tests now.



---

archive/issue_comments_060214.json:
```json
{
    "body": "Attachment\n\nAdds the requested doctests and Se tests and the cleanup on `sage_inspect.py`",
    "created_at": "2010-01-18T10:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60214",
    "user": "timdumol"
}
```

Attachment

Adds the requested doctests and Se tests and the cleanup on `sage_inspect.py`



---

archive/issue_comments_060215.json:
```json
{
    "body": "This new patch should add the requested tests.",
    "created_at": "2010-01-18T10:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60215",
    "user": "timdumol"
}
```

This new patch should add the requested tests.



---

archive/issue_comments_060216.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-18T10:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60216",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060217.json:
```json
{
    "body": "Fixes a problem with text cells with unicode contents.",
    "created_at": "2010-01-19T04:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60217",
    "user": "timdumol"
}
```

Fixes a problem with text cells with unicode contents.



---

archive/issue_comments_060218.json:
```json
{
    "body": "Attachment\n\nTest fix, drop pdb.  Replaces previous.",
    "created_at": "2010-01-19T11:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60218",
    "user": "mpatel"
}
```

Attachment

Test fix, drop pdb.  Replaces previous.



---

archive/issue_comments_060219.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T11:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60219",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060220.json:
```json
{
    "body": "Attachment\n\nV7 fixes a failed doctest in `cell.py` (line 138) and removes `import pdb; pdb.set_trace()` from `test_worksheet_list.py`.",
    "created_at": "2010-01-19T11:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60220",
    "user": "mpatel"
}
```

Attachment

V7 fixes a failed doctest in `cell.py` (line 138) and removes `import pdb; pdb.set_trace()` from `test_worksheet_list.py`.



---

archive/issue_comments_060221.json:
```json
{
    "body": "On the non-ASCII Unicode characters which may break docbuilds, please see #8000.",
    "created_at": "2010-01-19T16:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60221",
    "user": "mpatel"
}
```

On the non-ASCII Unicode characters which may break docbuilds, please see #8000.



---

archive/issue_comments_060222.json:
```json
{
    "body": "Sphinx raises\n\n```\nreading sources... [100%] sagenb/notebook/worksheet\nSphinx error:\n'utf8' codec can't decode bytes in position 420-422: invalid data\n```\n\nThe \"invalid\" data appears to be `u'\\xe4'` in line 695 (or so) of `worksheet.py`:\n\n```python\n            u'\\u03ab\\xe4\\u013b\\u01be\\u1e40\\u0411'                               \n```\n\nV8 just makes the docstring raw (`\"\"\"` --> `r\"\"\"`).  I've added `'\u0422\u0435\u043e\u0440\u0438\u044f \u0447\u0438\u0441\u0435\u043b'`, partly for fun.",
    "created_at": "2010-01-19T19:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60222",
    "user": "mpatel"
}
```

Sphinx raises

```
reading sources... [100%] sagenb/notebook/worksheet
Sphinx error:
'utf8' codec can't decode bytes in position 420-422: invalid data
```

The "invalid" data appears to be `u'\xe4'` in line 695 (or so) of `worksheet.py`:

```python
            u'\u03ab\xe4\u013b\u01be\u1e40\u0411'                               
```

V8 just makes the docstring raw (`"""` --> `r"""`).  I've added `'Теория чисел'`, partly for fun.



---

archive/issue_comments_060223.json:
```json
{
    "body": "Attachment\n\nMake `Worksheet.name`'s docstring raw, for Sphinx.  Replaces previous.",
    "created_at": "2010-01-19T19:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60223",
    "user": "mpatel"
}
```

Attachment

Make `Worksheet.name`'s docstring raw, for Sphinx.  Replaces previous.



---

archive/issue_comments_060224.json:
```json
{
    "body": "It may be better to make the docstrings unicode strings.  V9 does this, but I can't attach it right now:\n\n```\nTrac detected an internal error:\n    IOError: [Errno 28] No space left on device\n```\n",
    "created_at": "2010-01-19T19:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60224",
    "user": "mpatel"
}
```

It may be better to make the docstrings unicode strings.  V9 does this, but I can't attach it right now:

```
Trac detected an internal error:
    IOError: [Errno 28] No space left on device
```




---

archive/issue_comments_060225.json:
```json
{
    "body": "Attachment\n\nMake the docstrings unicode strings.  Replaces previous.",
    "created_at": "2010-01-19T19:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60225",
    "user": "mpatel"
}
```

Attachment

Make the docstrings unicode strings.  Replaces previous.



---

archive/issue_comments_060226.json:
```json
{
    "body": "The review patches look good. Nice work. I must say, the reviewing of this patch is real messy.",
    "created_at": "2010-01-19T20:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60226",
    "user": "timdumol"
}
```

The review patches look good. Nice work. I must say, the reviewing of this patch is real messy.



---

archive/issue_comments_060227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7249#issuecomment-60227",
    "user": "mpatel"
}
```

Resolution: fixed
