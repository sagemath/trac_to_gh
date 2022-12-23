# Issue 7361: implement is_regular() for a graph

Issue created by migration from https://trac.sagemath.org/ticket/7361

Original creator: AlexGhitza

Original creation time: 2009-10-31 14:11:02

Assignee: rlm

Keywords: graph regular

The attached patch implements a method that checks whether a graph is regular.



---

Comment by AlexGhitza created at 2009-10-31 14:14:27

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-10-31 20:30:47

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-10-31 20:30:47

There is not necessarily a vertex named 0 in the graph, in which case the first line of your patch does not do what you want...

What you could try is something like that :

```
it=self.degree_iterator()
k=it.next()
for i in it:
   if i!=k:
       return False
return True
```


Besides, if you want your docstring to be "formally" correct, here are a few remarks :
The first line of the docstring should describe in a few words what the function does. In your case : "Tests whether the graph is regular" or simething similar should do.

Two lines later, you explain a bit more in details what it does if necessary.

You can create an INPUT: section to describe the parameters of your method.

Besides : when you want something to be written through LaTeX, like u_1 or \sum_{x=0}^\infty , you have to write it like that :

```
`u_1`
or
`\sum_{x=0}^\infty`
```

When you want a word to be understood a a python keyword, like the name of a variable, or the values True/False, you add two times this sign :

```
``True``
``False``
```


And this is all I can think of for the moment :-)

Nathann


---

Attachment

Thanks for looking at this.  I have replaced the patch with a new one incorporating your comments.


---

Comment by AlexGhitza created at 2009-11-01 02:43:37

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-11-01 08:13:48

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-11-01 08:13:48

Now it looks perfect to me :-)

Positive review, and thank you for your work !!!

Nathann


---

Comment by mhansen created at 2009-11-02 04:27:46

Resolution: fixed
