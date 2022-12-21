# Issue 3154: notebook -- spurious u0027's output

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-10 22:43:31

Assignee: boothby

In the notebook we have this, caused by _eval_cmd in worksheet.py:


```
%python 
2+2
print "'hi\'"
///

'hi\u0027
```



---

Attachment

Uses base64.b64en/decode instead.


---

Comment by timdumol created at 2010-01-17 00:31:32

Changing status from new to needs_review.


---

Comment by wjp created at 2010-01-17 21:44:47

I think using %r to handle escaping quotes would be cleaner than using intermediate base64. I'm attaching a new patch that does this.


---

Attachment


---

Comment by mpatel created at 2010-01-18 09:49:19

Can we also use `%r` instead of `base64`-encoding in

 * `sage.misc.preparser.load_wrap`
 * `sagenb.misc.support.automatic_name_filter`
 * `worksheet.Worksheet.preparse`

?


---

Comment by mpatel created at 2010-01-18 10:15:37

The second patch causes two SageNB doctest failures:

```python
File "/home/tmp/sagenb-0.5/src/sagenb/sagenb/notebook/worksheet.py", line 3695:
    sage: W.check_for_system_switching(c1.cleaned_input_text(), c1)
Expected:
    (True, u"print _support_.syseval(gap, ur*SymmetricGroup(5)*, '...')")
Got:
    (True, u"print _support_.syseval(gap, u'SymmetricGroup(5)', '/home/.sage/temp/chopin/5101/dir_2.sagenb/home/sage/0/cells/1')")
**********************************************************************
File "/home/tmp/sagenb-0.5/src/sagenb/sagenb/notebook/worksheet.py", line 3721:
    sage: W.check_for_system_switching(c1.cleaned_input_text(), c1)
Expected:
    (True, u"print _support_.syseval(gap, ur*SymmetricGroup(5)*, '...')")
Got:
    (True, "print _support_.syseval(gap, u'SymmetricGroup(5)', '/home/.sage/temp/chopin/5101/dir_2.sagenb/home/sage/0/cells/1')")

```

Does the latter reveal a [minor] problem with #7249?


---

Comment by timdumol created at 2010-01-18 11:10:31

Replying to [comment:3 mpatel]:
> Can we also use `%r` instead of `base64`-encoding in
> 
>  * `sage.misc.preparser.load_wrap`
>  * `sagenb.misc.support.automatic_name_filter`
>  * `worksheet.Worksheet.preparse`
> 
> ?
I believe so. I'd rather that be put in a new ticket though.

The attached patch should solve the mentioned doctest problems. Can't see how they're related to #7249 though.


---

Comment by timdumol created at 2010-01-18 18:31:34

Sorry, I forgot to attach the actual patch.


---

Comment by timdumol created at 2010-01-18 18:32:21

Fixes a few doctests and a unicode encoding issue.


---

Attachment

Rebase for minor "hunk" failure.  Replaces previous.


---

Comment by mpatel created at 2010-01-20 01:57:40

Changing status from needs_review to positive_review.


---

Attachment

Nice work!  V3 is just a rebase of V2.


---

Comment by timdumol created at 2010-01-20 03:45:39

Resolution: fixed


---

Comment by mpatel created at 2010-02-06 19:00:06

Rebased vs. SageNB 0.7.4.  Replaces previous.


---

Attachment


---

Comment by mpatel created at 2010-02-06 19:27:11

Changing status from closed to needs_work.


---

Comment by mpatel created at 2010-02-06 19:29:03

V4 is rebased against SageNB 0.7.4 (cf. #8051), but now several doctests fail, at least one of which I can't investigate lucidly right now.  I'll return to this soon.


---

Comment by mpatel created at 2010-02-06 19:47:20

I've reopened this ticket because its *not* in SageNB 0.7 (cf. #8051).   I mistakenly thought, per `hg log`, that I had merged it, but I really merged #4217, whose commit string refers to #3154.


---

Comment by mpatel created at 2010-02-09 05:18:19

Doctest fixes.  Replaces all previous.


---

Attachment

V5 is rebased for SageNB 0.7.4 and it includes several new doctest fixes.  Can someone review my changes?


---

Comment by mpatel created at 2010-02-09 05:24:16

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-03-19 05:10:14

Doctests pass, no regressions noted.


---

Comment by timdumol created at 2010-03-19 05:10:14

Changing status from needs_review to positive_review.
