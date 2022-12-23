# Issue 5726: RDF quotes -- docstring bug (possibly cython issue)

Issue created by migration from https://trac.sagemath.org/ticket/5726

Original creator: was

Original creation time: 2009-04-09 16:58:20

Assignee: tba


```
sage: RDF.random_element?
...
Definition: RDF.random_element(min='-1', max='1')
```

Notice the stupid quotes around -1 and 1, which are very confusing!


---

Comment by was created at 2009-04-09 19:53:37

In the notebook definition is wrong in at least two ways:

```
sage: factor?
Definition:  factor(n, proof, int_, algorithm, verbose, **kwds)
```

but it should be

```
Definition:     factor(n, proof=None, int_=False, algorithm='pari', verbose=0, **kwds)
```

which it *is* in the command line. 

On the command line, cython code *never* gets a function "Definition".


---

Attachment


---

Comment by jhpalmieri created at 2009-08-24 16:49:34

The problems lie in sage.misc.sageinspect.

The issue with `factor` is a one-line fix -- see the patch.  ("defaults" was missing from the return value of the function `sage_getargspec`.)

The issue with `RDF.random_element` is a cython one.  To get the arguments of a Cython function, as far as I can tell, the source code is scanned and parsed, so _everything_ is a string.  The default arguments are therefore returned as strings.  See the function `_sage_getargspec_cython` -- the examples even demonstrate this.  I don't have a good idea for a simple fix yet.  Since this is a separate issue, the first patch can be reviewed, and if we don't find a quick fix for the Cython issue, we can open a new ticket just for that.


---

Comment by timdumol created at 2009-08-30 19:18:17

Applied the patch. Doctests pass, and the default arguments now appear. Nice work.

As for the Cython issue, perhaps using `repr(eval(argument))` will work. Output as string if the output starts and ends with quotes, and output without quotes for any other result.


---

Comment by jhpalmieri created at 2009-08-30 21:40:01

Replying to [comment:4 timdumol]:
> As for the Cython issue, perhaps using `repr(eval(argument))` will work. Output as string if the output starts and ends with quotes, and output without quotes for any other result.

Good idea.  See #6848.


---

Comment by mvngu created at 2009-08-31 04:45:51

Resolution: fixed
