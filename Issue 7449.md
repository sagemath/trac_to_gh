# Issue 7449: Some doc request hangs sage eating all memory.

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-11-12 21:49:17

Assignee: mvngu

CC:  hivert nthiery

Keywords: doc

If I type

```
sage: MS = MatrixSpace(QQ,6,6,sparse=True); MS
Full MatrixSpace of 6 by 6 sparse matrices over Rational Field
sage: MS?
```

Then sage hangs eating all the memory. I don't have the less idea why it happens with `MatrixSpace`. I didn't try very hard but I can't manage any other request with the same effect. I checked that this is not a problem of installation on my computer: It happens as well on boxen. Though, on the contrary to my own computer, I didn't check that it effectively eat all the memory on boxen ;-)

Cheers,

Florent
  


---

Comment by was created at 2009-11-13 06:43:02

I can confirm this bug on the command line.  However, not interestingly that it does *not* happen in the Sage notebook.  So it is an Ipython bug.

http://wstein.org/home/wstein/patches/trac_7449.png


---

Comment by hivert created at 2009-11-13 08:07:31

Replying to [comment:1 was]:
> I can confirm this bug on the command line.  However, not interestingly that it does *not* happen in the Sage notebook.  So it is an Ipython bug.
> 
> http://wstein.org/home/wstein/patches/trac_7449.png

So what should we do ? Try to figure out a smaller file that triggers the problem and report to the ipython community ? I've no idea how to debug ipython. Any better suggestion ?


---

Comment by was created at 2009-11-16 17:25:45

Fernando Perez solved the problem:

```

On Mon, Nov 16, 2009 at 2:31 AM, Fernando Perez
<> wrote:
> The fact that Ctrl-C cleanly stops the crazy loop *without* a
> KeyboardInterrupt makes me think that ipython is trying to introspect
> the MS object and some C code is going into a mad loop (otherwise we'd
> see the Python signal handler showing a traceback).  Do you have any
> other bugs related to this type of object that sound along those
> lines?

Half-right. IPython is swallowing the kbd interrupt, but the bug is in
sage, it's the fact that len(MS) never returns:

sage: MS = MatrixSpace(QQ,6,6,sparse=True); MS
Full MatrixSpace of 6 by 6 sparse matrices over Rational Field
sage: len(MS)
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/home/fperez/ipython/repo/kernel-config-lp/docs/<ipython console> in <module>()

/opt/sage/local/lib/python2.6/site-packages/sage/structure/parent.so
in sage.structure.parent.Parent.__len__
(sage/structure/parent.c:5533)()

/opt/sage/local/lib/python2.6/site-packages/sage/structure/parent.so
in sage.structure.parent.Parent.list (sage/structure/parent.c:4995)()

/opt/sage/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc
in __iter__(self)
   751             while True:
   752                 for iv in
sage.combinat.integer_vector.IntegerVectors(weight,
number_of_entries):
--> 753                     yield self(entries=[base_elements[i] for i
in iv], rows=True)
   754
   755                 weight += 1

/opt/sage/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc
in __call__(self, entries, coerce, copy, rows)
   371             copy = False
   372         elif self.__is_sparse and isinstance(entries, (list, tuple)):
--> 373             entries = list_to_dict(entries, self.__nrows,
self.__ncols, rows=rows)
   374             coerce = True
   375             copy = False

/opt/sage/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc
in list_to_dict(entries, nrows, ncols, rows)
  1240                 d[(row,col)] = x
  1241             else:
-> 1242                 d[(col,row)] = x
  1243     return d
  1244

/opt/sage/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.pyc
in my_sigint(x, n)
     7
     8 def my_sigint(x, n):
----> 9     raise KeyboardInterrupt
    10
    11 def my_sigfpe(x, n):

KeyboardInterrupt:


It seems that the ms object implements __len__, but this function
never returns.  It's just that ipython was calling len() on it.

Cheers,

f
```



---

Comment by was created at 2009-11-16 17:26:32

Changing status from new to needs_review.


---

Attachment


---

Comment by hivert created at 2009-11-16 17:55:24

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2009-11-16 17:55:24

Replying to [comment:3 was]:

> It seems that the ms object implements __len__, but this function
> never returns.  It's just that ipython was calling len() on it.

Good remark ! This indicate that there should be a generic test in the base category `Objects()` checking that for the current object `__len__` is either not defined either returns a correct `int` object or else raise an exception. Any other behavior (loop, returning a sage Integer or any fancy object should be reported as an error).

Those bugs seems therefore catchable by `TestSuite` if the object correctly inherits from the good category. I'll try it.

Otherwise positive review.

Cheers,

Florent


---

Comment by mhansen created at 2009-11-17 06:05:10

Resolution: fixed
