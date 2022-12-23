# Issue 7668: Play waveforms directly, like in Mathematica

Issue created by migration from https://trac.sagemath.org/ticket/7668

Original creator: kcrisman

Original creation time: 2009-12-11 20:26:54

Assignee: was

CC:  jason chapoton

This was requested by a participant at the first Sage Education Day.  I'm putting this in notebook but I really can't think of any appropriate component.


---

Comment by mhampton created at 2009-12-11 20:59:04

This would not be terribly hard to do using the python wave module.  See this interact for a basic demo:

http://wiki.sagemath.org/interact/misc#Hearingatrigonometricidentity

It would be good to wrap this functionality in a more user-friendly command.


---

Comment by jason created at 2009-12-11 21:56:36

Also, don't forget about


---

Comment by jason created at 2009-12-11 21:57:44

I meant to say about the scipy signal processing stuff, but then thought better about it.

I think this would fit well into a widget framework to represent objects in the notebook.


---

Comment by kcrisman created at 2013-05-08 01:48:43

Here is another nice example of this - [this ask.sagemath](http://ask.sagemath.org/question/2542/sound-how-is-it-done) question as well as [this sage-devel discussion](https://groups.google.com/forum/?fromgroups=#!topic/sage-devel/3-Y1RUFkq14).


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by chapoton created at 2020-09-01 15:50:16

Resolution: invalid


---

Comment by kcrisman created at 2020-09-01 21:34:33

Changing status from closed to new.


---

Comment by kcrisman created at 2020-09-01 21:34:33

Resolution changed from invalid to 


---

Comment by kcrisman created at 2020-09-01 21:34:33

This could conceivably be implemented in Jupyter as well.


---

Comment by kcrisman created at 2020-09-01 21:34:46

(And it certainly fits the Sage mission statement.)


---

Comment by jason created at 2020-09-01 22:37:40

And arguably works already in Jupyter: https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.Audio

This is used in one of the most popular ipywidgets examples: https://github.com/jupyter-widgets/ipywidgets/blob/master/docs/source/examples/Beat%20Frequencies.ipynb


---

Comment by kcrisman created at 2020-09-01 23:05:37

Changing component from notebook to documentation.


---

Comment by kcrisman created at 2020-09-01 23:05:37

Nice! Wow, I wasn't expecting a reply from one of the core Jupyter developers ;-) though I guess he WAS one of the original people on this ticket :-)

Maybe this ticket can then just be adding this to a likely place in the documentation.
