# Issue 8738: @interact matrix input control ignores label

Issue created by migration from https://trac.sagemath.org/ticket/8738

Original creator: was

Original creation time: 2010-04-21 17:05:43

Assignee: jason, was

Try this interact:

```
@interact
def f(M = ("matrix ", random_matrix(QQ,3,4)), n=("an int", 5)):
    print "The echelon form of the above matrix is:"
    print M.echelon_form()
```


The first input control should be labeled "matrix", but it isn't.  Whoever added the matrix control for `@`interact, somehow did it in a way that breaks control labels. 


---

Comment by jason created at 2010-04-21 19:39:18

I added the matrix control.  I had no idea that you could pass a tuple of ("label", control), so it's likely that it broke from ignorance.  Thanks for pointing out this feature!


---

Comment by jason created at 2010-04-21 19:54:27

I don't have a development copy of sagenb right now (it'd be nice of the local/lib/python2.6/site-packages/sagenb.../sagenb/notebook directory contained the mercurial repository so we could easily just change things and make a patch, without having to go get the spkg, extract it, install it with the develop option, etc.)

However, to fix this, just change line 3750 of interact.py from:

```
        C = input_grid(default.nrows(), default.ncols(), default=default.list(), to_value=default.parent())

```



to


```
        C = input_grid(default.nrows(), default.ncols(), default=default.list(), to_value=default.parent(), label=label)

```


I have a comment about the design feature.  I notice from the code that this sets a default value *sometimes* (depending on the control):


```
@interact
def f(n=(2,[1,2,3,4,5])):
    print n
```


However, this does *not set the default, because the first spot is overloaded to mean "label" and "default value", and "label" takes precedence:


```
@interact
def f(n=("b",["a","b","c"])):
    print n
```


I think this interplay and double-meaning of the first argument confuses things too much.


---

Comment by kcrisman created at 2014-12-10 21:02:10

This is fixed by that very code in upstream https://github.com/sagemath/sagenb/pull/299 - we don't take care of the ambiguity, though!  I wonder what Sage cell and SMC do with that?


---

Comment by kcrisman created at 2014-12-18 02:54:34

This would then be fixed in #10057, as this was merged.


---

Comment by kcrisman created at 2014-12-18 02:54:34

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-12-24 09:48:35

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2014-12-24 09:48:35

Fixed by #10057.


---

Comment by vbraun created at 2015-01-13 01:22:33

Resolution: fixed
