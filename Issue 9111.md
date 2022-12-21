# Issue 9111: modular decomposition

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-06-01 21:53:58

Assignee: jason, ncohen, rlm

Using the C code written by Thierry de Montgolfier and available there :
http://www.liafa.jussieu.fr/~fm/algos/index.html

We now have a Graph.modular_decomposition function available in Sage !

Nathann


---

Comment by mhansen created at 2010-06-01 23:42:20

From that webpage, it says that the code is only available for non-commercial use.


---

Comment by ncohen created at 2010-06-01 23:54:46

yesyesyes, it should be licensed under the GPL very soon :-)

Fabrice de Montgolfer is away for something like a week, and then it should be done :-)

Nathann


---

Comment by jason created at 2010-06-02 22:33:06

Changing status from new to needs_work.


---

Comment by jason created at 2010-06-02 22:33:06

A couple of comments:

1. Why is modular_decomposition.c included in the patch?

2. The comment at the top of modular_decomposition.pyx indicates it is a copy of code, but is it rather a Cython interface to C code?

3. It wouldn't hurt to give a very brief explanation of what a modular decomposition of a graph is in the docstrings


---

Comment by jason created at 2010-06-02 22:36:31

And 4. This functionality is cool!


---

Comment by ncohen created at 2010-06-03 11:49:58

Hello !

1. Because I wasn't paying attention

2. I mean by this that the lines of the code building the graph according to the format used in the .c file, along with the ones reading the decomposition once it is computed, can be found in the .c files too. I copied those and Cythonized them, but the "real" code is still contained in the .c file.

3. Indeed.

4. I think so, too ! Especially in C, and in mlog(n) :-)

I will update the patch once the software is "officially" GPL2, which could mean next week.

Nathann


---

Comment by ncohen created at 2010-06-20 19:26:42

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-06-20 19:26:42

Here it is ! With a brand-new GPL2 licence, thanks to Fabien de Montgolfier ! :-)

Nathann


---

Attachment


---

Comment by rlm created at 2010-06-21 21:39:10

Replying to [comment:5 ncohen]:
> 2. I mean by this that the lines of the code building the graph according to the format used in the .c file, along with the ones reading the decomposition once it is computed, can be found in the .c files too. I copied those and Cythonized them, but the "real" code is still contained in the .c file.

Can you make this a bit more clear in the documentation? (Please, in a new patch on top of attachment:trac_9111-doc-edits.patch to avoid conflict with the other patch.)

It seems like there should be more thorough documentation of the idea of modular decomposition. Perhaps a chapter, or at least a chunk, for the reference manual, or a guided tour or something? I don't want to block this from getting merged because of this, but maybe in a future ticket?

I'm happy with this patch in that it passes its tests and the docs look good, but I'd be much more comfortable with a second reviewer, since I'm not very familiar with modular decompositions. I can certainly offer half of a positive review, though.


---

Comment by ncohen created at 2010-06-22 07:16:16

Here is a bit more of documentation, if it pleases you :-)

I also added a reference to a freely-downloadable survey, just in case !

Nathann


---

Attachment


---

Comment by rlm created at 2010-07-18 09:42:30


```
sage -t -long sage/graphs/modular_decomposition/modular_decomposition.pyx
**********************************************************************
Error: TAB character found.

	 [4.5 s]
```



---

Comment by rlm created at 2010-07-18 09:42:30

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-07-19 01:54:15

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-07-19 01:54:15

Here it is !! The "tab" characters were not at the beginning but at the end of some lines... some unlucky copy/paste :-)

Nathann


---

Attachment


---

Comment by rlm created at 2010-07-19 08:41:04

Apply in the following order:

```


trac_9111.patch
trac_9111-doc-edits.patch
trac_9111-doc_addition.patch

```



---

Comment by rlm created at 2010-07-19 08:41:04

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-07-19 08:43:36

Great !! Thank youuuuuu ! :-)

Nathann


---

Comment by mpatel created at 2010-07-21 02:48:04

Resolution: fixed
