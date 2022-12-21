# Issue 8947: pretty printing of vectors over callable symbolic rings

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-05-11 06:25:01

Assignee: jason, was

CC:  rbeezer was robertwb

This patch makes vectors of callable symbolic rings print nicer, in the form arguments mapsto vector


```
sage: f(x,y)=[3*x,e^x,2*x*y]
sage: f
(x, y) |--> (3*x, e^x, 2*x*y)
```




---

Comment by jason created at 2010-05-11 06:27:20

Changing status from new to needs_work.


---

Comment by jason created at 2010-05-11 06:27:20

Doctests need to be fixed up.


---

Attachment


---

Comment by jason created at 2010-05-11 18:04:23

The doctests depend on a patch in 4.4.2.alpha0.

I think the right way to change printing for a vector over callable symbolic expressions is to subclass as I did in the patch and override the _repr_ and _latex_ methods.  Can was or robertwb comment on this?


---

Comment by jason created at 2010-05-11 18:04:23

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-05-11 18:09:00

#5506 adds some further ideas about what to do about this class.


---

Comment by robertwb created at 2010-05-11 18:20:57

Yep, that's the way to do it. The code looks good, but I only glanced at it quickly haven't tested it.


---

Comment by rbeezer created at 2010-05-19 04:08:52

Hi Jason,

Nice patch.

1.  Do you think this should be called "free_module_element_callable_symbolic_dense"?  Technically these don't have to be vectors, and they do have entries over a ring?  Yes, that's an unwieldy name.  ;-)  Just asking.

2.  Do you want to add it into the documentation, doesn't seem to be included when I build the docs?

3.  Docstring for _latex_ looks like it has an indentation problem that needs fixing.

Running tests right now.

Rob


---

Comment by jason created at 2010-05-19 04:17:43

Replying to [comment:6 rbeezer]:
> Hi Jason,
> 
> Nice patch.
> 
> 1.  Do you think this should be called "free_module_element_callable_symbolic_dense"?  Technically these don't have to be vectors, and they do have entries over a ring?  Yes, that's an unwieldy name.  ;-)  Just asking.

Well, Sage thinks that it is a field:


```

sage: f(x,y)=x^2+y                             
sage: R=f.parent()
sage: R 
Callable function ring with arguments (x, y)
sage: R.is_field()
True
```



> 
> 2.  Do you want to add it into the documentation, doesn't seem to be included when I build the docs?
> 
> 3.  Docstring for _latex_ looks like it has an indentation problem that needs fixing.

Looks like (2) and (3) both probably need to be fixed.


---

Comment by jason created at 2010-05-19 04:17:51

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2010-05-19 04:29:29

Replying to [comment:7 jason]:

> Callable function ring with arguments (x, y)
> sage: R.is_field()
> True

And I trusted the _repr_ output?

Failing a few tests, in the obvious way, in 

```
/sage/dev/devel/sage-main/sage/symbolic/expression.pyx
/sage/dev/devel/sage-main/sage/calculus/calculus.py
```


(and not done testing).


---

Comment by rbeezer created at 2010-05-19 05:29:34

On 4.4.2.rc0 I get the following failures.  The one for R is totally unrelated I believe, the others I saw are just the obvious differences in format for functions involved in this patch.


```
The following tests failed:

        sage -t  devel/sage-main/sage/symbolic/expression.pyx # 4 doctests failed
        sage -t  devel/sage-main/sage/calculus/calculus.py # 2 doctests failed   
        sage -t  devel/sage-main/sage/interfaces/r.py # 1 doctests failed        
        sage -t  devel/sage-main/sage/modules/free_module_element.pyx # 3 doctests failed

```



---

Attachment

apply on top of previous patches


---

Comment by jason created at 2010-06-01 22:10:46

Okay, the doctest issues you mentioned should all be fixed now.


---

Comment by jason created at 2010-06-01 22:10:46

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-06-02 04:02:22

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-06-02 04:02:22

sage/calculus, sage/modules, sage/symbolic directories pass all tests, and documentation for `vector_callable_symbolic_dense` looks good.

Positive review.


---

Comment by mpatel created at 2010-07-20 08:20:13

Resolution: fixed
