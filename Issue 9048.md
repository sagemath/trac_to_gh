# Issue 9048: different behaviour of var in notebook and text version

Issue created by migration from https://trac.sagemath.org/ticket/9048

Original creator: zimmerma

Original creation time: 2010-05-25 19:59:01

Assignee: jason, was

CC:  eocansey@risc.jku.at

In the text version of Sage, `var('x');` does not print anything.
However, in the notebook, it prints `x`, even with the `;`
that should prevent output. This is quite annoying. Is there a reason for that?


---

Comment by jason created at 2010-05-26 03:46:21

Changed the title to identify the underlying issue.  Note that 1+2; also prints out something in the notebook, but not in the command line.

My guess is that it is a convention in ipython, since a semicolon does nothing in just plain python:


```
% sage -python
Python 2.6.4 (r264:75706, May  6 2010, 23:38:46) 
[GCC 4.2.1 (Apple Inc. build 5659)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+2;
3


```



---

Comment by zimmerma created at 2013-08-24 12:39:33

note sure what to do with this ticket. At least we can try to list all inconsistencies between the terminal version and the notebook:

* `1+2;` does not print anything in the terminal version, but does print something in the notebook

* `__` and `____` do not work in the notebook

* `automatic_names` does not work in the terminal version

Are there any other differences?

Paul


---

Comment by nbruin created at 2013-08-24 17:42:37

Replying to [comment:3 zimmerma]:
> * `1+2;` does not print anything in the terminal version, but does print something in the notebook
The printing in the notebook is a little more different than just that:

```
1;2;
```

prints

```
1
2
```

whereas

```
1
2
```

prints

```
2
```

and

```
(1
)
```

prints nothing, whereas

```
(1)
```

prints

```
1
```

i.e., it seems that all results from statements contained entirely on the last line of the cell are printed, regardless of semicolons, and no other results are. To me this seems a little arbitrary, but resolving this is probably something for the notebook.


---

Comment by zimmerma created at 2017-03-06 20:19:54

I've added `automatic_names` in the description as a reminder, since we write in our book about Sage (which is currently being translated to english) that `automatic_names` does not work in the terminal version.


---

Comment by embray created at 2019-07-14 09:20:46

automatic_names also doesn't work in the Jupyter Notebook. This was also discussed in #25837. I looked into this a bit à year ago, and it turns out the `automatic_names` implementation lives in sagenb. It needs to be moved into the main sage package, and will take some adjusting to integrate into the IPython terminal and Jupyter kernel interfaces.


---

Comment by embray created at 2019-07-14 09:22:09

I thought I also made a ticket specifically for this issue but I can't find it now, so maybe this is just the one.


---

Comment by kcrisman created at 2020-06-17 18:17:33

I've created #29888 for automatic_names in Jupyter.

This ticket can still be about differences between the terminal and Jupyter notebook, but probably should be updated for differences between that one and the terminal, not the sagenb and terminal.
