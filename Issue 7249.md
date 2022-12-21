# Issue 7249: switch the notebook's templating system to Jinja2

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2009-10-19 08:44:15

Assignee: boothby

CC:  mhansen mpatel ddrake

We should switch the notebook's templating system from Jinja to Jinja2. Jinja2, among other things, makes i18n much easier.


---

Comment by ddrake created at 2009-10-20 00:30:53

apply to sagenb repo


---

Attachment


---

Comment by ddrake created at 2009-10-20 00:32:11

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-10-24 19:09:31

#7269 should now include these changes.


---

Comment by timdumol created at 2009-12-19 12:17:59

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2009-12-19 12:17:59

#7269 no longer includes these changes. Refer to comment:25:ticket:7269.

Changes must be made to deal with unicode encoding/decoding before this can be reviewed.


---

Comment by ddrake created at 2009-12-22 04:55:38

Replying to [comment:3 timdumol]:
> #7269 no longer includes these changes. Refer to comment:25:ticket:7269.
> 
> Changes must be made to deal with unicode encoding/decoding before this can be reviewed.

At comment:24:ticket:7269 you say that we need Model-View-Presenter/Controller separation. How hard will that be? It sounds hard. :)  I've run into Unicode string problems while trying to internationalize the notebook, so I'd definitely like to do this if it's the right way to go about it.


---

Comment by timdumol created at 2009-12-22 05:19:25

MVC [1] separates the layers of the program into a model, which has the data; views, which are ways to present the data; and the controller/s, which control which data to show etc.

Currently the notebook serves as a model/controller and has some view functions mixed into it (`html_*`). Separating things will make things cleaner, and will make dealing with unicode easier: the view is presented with encoded byte strings, the controller deals with unicode strings, and data is retrieved from the model (db or filesystem) in encoded data which is converted to unicode strings.

Without this separation, one will need to check whether each string passed is an encoded byte string or a unicode string.

Separation will entail first removing the `html_*` functions, which in turn means restructuring the templates. I'll be working on that very soon.

[1] http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller


---

Comment by timdumol created at 2010-01-06 20:13:24

Converts much storage to unicode, and adds the necessary encoding for storage and networking. Uses jinja2 instead of jinja. Depends on #7835, #7786 and their dependencies.


---

Comment by timdumol created at 2010-01-06 20:14:01

Changing status from needs_work to needs_review.


---

Attachment

Hopefully this patch will do the trick and make i18n easier.


---

Attachment

Fix several doctests.  Replaces previous.


---

Comment by mpatel created at 2010-01-06 22:00:56

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2010-01-06 22:00:56

V3:

  * Fixes a number of doctests.
  * `iamges` --> `images` in `cell.py`.
  * `inpit_text = input_text.decode('utf-8', str)` --> `input_text = input_text.decode('utf-8', 'ignore')` in `cell.py`.

I'm not sure about the choice of `encode` / `decode` in some places.  Should we always `decode` instances of `str` and `encode` instances of `unicode`?  Could you please double-check the patch?  Also, would it be better to write and use a helper function to do the conversions?

Should the changes to `cell.html` be at #7786?  Isn't `div_wrap` a `boolean`?

Does the change to `Worksheet.preparse` belong at #7835?

If we're planning to use unicode "everywhere", even for the worksheet / cell _system_, should we also *consistently* cover the relevant methods (and examples for) in `worksheet.py` and elsewhere?

I apologize for my ignorance.


---

Comment by mpatel created at 2010-01-07 02:24:42

Rebased vs. #7835 v2, #7786 v8, etc.  Replaces previous.


---

Attachment

V3 (really) is rebased against the latest at #7835, #7786.  Besides consistently using UTF-8 for the cell/worksheet system, I'm curious about `Cell.__init__`, where `str`s are `encode`d, not `decode`d.  Again, I'm not very familiar with encodings, so I may well be wrong.  Thanks!


---

Comment by mpatel created at 2010-01-07 05:19:16

According to the [Python Unicode HOWTO](http://docs.python.org/dev/howto/unicode.html#reading-and-writing-unicode-data), we can use the [codecs.open](http://docs.python.org/library/codecs.html#codecs.open) to read from (decode) and write to (encode) files transparently.


---

Comment by timdumol created at 2010-01-10 06:13:16

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
> If we're planning to use unicode "everywhere", even for the worksheet / cell _system_, should we also *consistently* cover the relevant methods (and examples for) in `worksheet.py` and elsewhere?

Yes, unicode functionality should be doctested.

> 
> I apologize for my ignorance.


---

Comment by timdumol created at 2010-01-10 06:13:52

Also, don't apologize for any supposed ignorance please. We're all ignorant.


---

Comment by timdumol created at 2010-01-16 08:40:57

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-01-16 08:40:57

The new patch fixes the styling of the worksheet listing page and adds two new functions in `sage.misc.misc`: `encoded_str` and `unicode_str` for encoding and decoding strings automatically.


---

Attachment

Fixes the styling of the worksheet listing page.


---

Comment by timdumol created at 2010-01-17 21:47:36

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

Comment by timdumol created at 2010-01-18 00:44:01

Rebase on a new patch set.


---

Attachment

Added an 'ignore' errors directive to `unicode_string`


---

Comment by mpatel created at 2010-01-18 07:35:59

In `notebook.py`, should `hunk = encoded_str(hunk)` be `hunk = unicode_str(hunk)`?

In `Cell.__init__`, can we simplify `self.set_input_text(str(input).replace('\r',''))`?

In `twist.py`, do we need to call `unicode_str` on the incoming input?  The constructors and `set_input_text` do this.


---

Comment by mpatel created at 2010-01-18 07:51:07

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

Comment by timdumol created at 2010-01-18 07:58:00

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-18 07:58:00

Nice catches. Here's a patch to fix them.


---

Comment by timdumol created at 2010-01-18 08:00:05

Adds the suggested fixes by mpatel.


---

Comment by timdumol created at 2010-01-18 08:19:14

Changing status from positive_review to needs_work.


---

Attachment

Woops! Sorry, accidentally put it to positive review. You should be the one, if ever.


---

Comment by mpatel created at 2010-01-18 08:57:05

Upon saving and quitting a worksheet that contains an evaluated `print `é`` cell, I see

```python
worksheet.py:1924: exceptions.UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
```


What about the `unicode_str`s in `twist.py`?  I'm just wondering why we need them.

Minor: It appears we can just call `encoded_str` in `sage_inspect.py`.

Also, can you slip some Unicode characters into the Se and/or doctests, so that we can detect potential regressions?


---

Comment by timdumol created at 2010-01-18 09:25:31

I'm pretty sure that that warning is unavoidable (has to do with upgrading from non-unicode to unicode). The `unicode_str`s are there just out of paranoia. Nice catch with the sage_inspect.py thing. I'll update the tests now.


---

Attachment

Adds the requested doctests and Se tests and the cleanup on `sage_inspect.py`


---

Comment by timdumol created at 2010-01-18 10:55:12

This new patch should add the requested tests.


---

Comment by timdumol created at 2010-01-18 10:55:12

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-01-19 04:30:35

Fixes a problem with text cells with unicode contents.


---

Attachment

Test fix, drop pdb.  Replaces previous.


---

Comment by mpatel created at 2010-01-19 11:31:54

Changing status from needs_review to positive_review.


---

Attachment

V7 fixes a failed doctest in `cell.py` (line 138) and removes `import pdb; pdb.set_trace()` from `test_worksheet_list.py`.


---

Comment by mpatel created at 2010-01-19 16:31:41

On the non-ASCII Unicode characters which may break docbuilds, please see #8000.


---

Comment by mpatel created at 2010-01-19 19:03:22

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

Attachment

Make `Worksheet.name`'s docstring raw, for Sphinx.  Replaces previous.


---

Comment by mpatel created at 2010-01-19 19:18:15

It may be better to make the docstrings unicode strings.  V9 does this, but I can't attach it right now:

```
Trac detected an internal error:
    IOError: [Errno 28] No space left on device
```



---

Attachment

Make the docstrings unicode strings.  Replaces previous.


---

Comment by timdumol created at 2010-01-19 20:01:39

The review patches look good. Nice work. I must say, the reviewing of this patch is real messy.


---

Comment by mpatel created at 2010-01-25 00:50:48

Resolution: fixed
