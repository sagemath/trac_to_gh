# Issue 9252: documentation errors in tutorial

Issue created by migration from https://trac.sagemath.org/ticket/9252

Original creator: wjlaffin

Original creation time: 2010-06-17 08:03:23

Assignee: wjlaffin

CC:  kcrisman embray tscrim

$'s are not escaped, multilines appear wrong, etc.

patch to appear shortly


---

Attachment


---

Comment by wjlaffin created at 2010-06-17 23:07:53

Changing status from new to needs_work.


---

Comment by wjlaffin created at 2010-06-17 23:07:53

Whops. Forgot to test that. Disregard the first one.


---

Attachment


---

Comment by wjlaffin created at 2010-06-17 23:23:46

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-06-18 00:40:13

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-06-18 00:40:13

I don't think this works with the static documentation; the backslashes that you've inserted are visible there.


---

Comment by wjlaffin created at 2010-06-18 04:13:21

Replying to [comment:3 jhpalmieri]:
> I don't think this works with the static documentation; the backslashes that you've inserted are visible there.

When you(or really anyone) says "static version" do they mean the pdf's? Would I be able to see them with 

```
sage -docbuild tutorial pdf
```

?

On that note, where is the code that adds the $$=latex hack to the documentation? Maybe I can just patch that a little instead.

What about the literal blocks that are meant for the interactive shell? 'sage:' always gets turned into a cell, so I needed to add some kind of header in the literal block (a bad hack) to get it to print correctly in the live-help.

Thanks for looking at my patch!


---

Comment by jhpalmieri created at 2010-06-18 05:13:10

Replying to [comment:4 wjlaffin]:
> When you(or really anyone) says "static version" do they mean the pdf's? 

No, the html version.  From the command line, execute "tutorial()", or from the notebook click the "Help" button and then the button for "Fast Static Versions of the Documentation".  Then click on the word "Tutorial".  Or open the file SAGE_ROOT/devel/sage/doc/output/html/en/tutorial/index.html in your web browser.

> On that note, where is the code that adds the $$=latex hack to the documentation? Maybe I can just patch that a little instead.
> 
> What about the literal blocks that are meant for the interactive shell? 'sage:' always gets turned into a cell, so I needed to add some kind of header in the literal block (a bad hack) to get it to print correctly in the live-help.

Some of this is in sage/sage/misc/sagedoc.py (e.g., `process_dollars`).  See also SAGE_ROOT/devel/sage/doc/common/conf.py.

It looks like the conversion from the html file to the "live" version of the docs is in the notebook code: SAGE_ROOT/local/lib/python/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/docHTMLProcessor.py, it looks like.  Since you're dealing with differences between the static and the live versions, you may need to look there.


---

Comment by chapoton created at 2019-05-10 18:15:07

Changing status from needs_work to needs_info.


---

Comment by chapoton created at 2019-05-10 18:15:07

obsolete, probably ?


---

Comment by jhpalmieri created at 2019-05-17 17:14:20

Changing status from needs_info to positive_review.


---

Comment by jhpalmieri created at 2019-05-17 17:14:20

Yes, I think so. Let's close it.


---

Comment by chapoton created at 2019-05-22 19:51:59

Resolution: invalid
