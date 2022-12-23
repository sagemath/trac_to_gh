# Issue 8033: add a README.txt for the graph_editor, to encourage development

Issue created by migration from https://trac.sagemath.org/ticket/8033

Original creator: was

Original creation time: 2010-01-21 22:54:04

Assignee: was

CC:  rkirov


```
Hi,

The new graph editor in sage by Rado is AWESOME.  One can try it
easily at http://sagenb.org by typing:

 g = graphs.CompleteGraph(10)
 graph_editor(g)

The actual source code is at

  local/lib/python/site-packages/sagenb-0.6-py2.6.egg/sagenb/data/graph_editor/

It would be *GREAT* if there were a README.txt file in that directory
that explained what all the js files actually are, something about how
the graph editor works, where the code that does spring layout
dynamically is located, etc.   I looked at the code for five minutes
and couldn't deduce answers to any of those questions.

So, could somebody familiar with the graph editor write something and
post a patch.  Or just respond to this email with what would go in a
README.txt?   I have two undergrads who might want to work on that
code, but it would help a lot of there were some docs.

```



---

Comment by was created at 2010-01-21 22:55:21

And here is the content (from Mitesh Patel):

```
The main files are

       a. sage/graphs/graph_editor.py
       b. graph_editor.html
       c. graph_editor.js
       d. processing.editor.min.js

Evaluating graph_editor(G) (see (a)) in an input cell generates
code/markup for an inline frame, which the notebook inserts into the
corresponding output cell.  The iframe loads (b) as its content.  In
turn, (b) draws in jQuery / UI, the layout algorithms in (c), and the
HTML5 canvas rendering engine in (d).

According to

       http://trac.sagemath.org/sage_trac/ticket/1321#comment:31

Rado adapted (d) from a project called Processing.js

http://processingjs.org/
http://processingjs.org/reference
http://processingjs.org/download

whose original and minified source files are

       e. processing.js
       f. processing.min.js

To make it somewhat easier to understand the differences between (f) and
(d), I put (d) through a JS "beautifier"

       http://jsbeautifier.org/

The result is

       g. processing.editor.js

But I decided not to give the same treatment to (e) and attempt to make
a concise diff.
```



---

Comment by rkirov created at 2010-01-22 08:00:11

contains README.TXT


---

Comment by rkirov created at 2010-01-22 08:01:05

Changing status from new to needs_review.


---

Attachment

Added a small file README.txt that has a summary of how the graph_editor works. Comments are welcome.


---

Comment by mpatel created at 2010-01-24 21:51:51

Various changes.  Replaces previous.  sagenb repo.


---

Attachment

I've attached an update with some changes.  Feel free to make further changes!


---

Comment by mpatel created at 2010-01-24 22:07:28

Just a quick thought: Using `$(window).load(...` instead of `$(document).ready(...` in `graph_editor.js` might resolve the "mouse_out" problem mentioned at the bottom of `graph_editor.py`.


---

Comment by mpatel created at 2010-02-05 01:11:37

Hi Rado -- If this looks good to you, we can change the status to "positive review."


---

Comment by rkirov created at 2010-02-07 04:46:13

Changing status from needs_review to positive_review.


---

Comment by rkirov created at 2010-02-07 04:46:13

definitively, its ready to be merged.


---

Comment by mpatel created at 2010-02-10 18:32:23

Resolution: fixed
