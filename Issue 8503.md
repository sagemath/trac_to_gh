# Issue 8503: broken multiline input in sage notebook

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2010-03-11 23:20:44

Assignee: was

CC:  chapoton

Multiline input like

```
8+\
2
```

which works in command line does not work in notebook and returns error.

Jason at [sage-notebook](http://groups.google.cz/group/sage-notebook/browse_thread/thread/9ee2472e1857edcb) wrote

```
Does it have to do with the preparser?  Note:

sage: preparse("1+\\n2")
'Integer(1)+ * BackslashOperator() * n2'

Maybe on the command line, ipython joins the two lines before the
preparser gets to it, but that doesn't happen in the notebook? 
```


And further:

```
plot(x,\
(x,-2,2))
```

does not produce the plot.


---

Comment by kcrisman created at 2014-12-10 21:40:05

Not the preparser.  For some reason, about the time this was reported, someone added `sage` and `python` to this list in `sagenb/notebook/worksheet.py`.

```
 #Handle line continuations: join lines that end in a backslash
#_except_ in LaTeX mode.
if cell_system not in ['latex', 'sage', 'python']:
I = I.replace('\\\n','')
```

Note from Robert's email

```

A=solve(\
sin(x),\
x)
A
```


```
plot(x,\
(x,-2,\
2)).show()
```

both work.

See https://github.com/sagemath/sagenb/issues/301


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-09-03 08:57:50

Resolution: invalid
