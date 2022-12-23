# Issue 7683: sphinx reference manual documentation has a *major* issues: in some cases the input parameters to functions are completely omitted causing great confusion!

Issue created by migration from https://trac.sagemath.org/ticket/7683

Original creator: was

Original creation time: 2009-12-15 02:01:17

Assignee: mvngu

See

http://sagemath.org/doc/reference/sage/rings/integer.html#sage.rings.integer.Integer.jacobi

Notice that the input parameter b is simply totally omitted from the function signature. In sharp contrast, if you type

```
sage: a = 5
sage: a.jacobi(<tab>
```

in the notebook, then you'll see the correct sphinx-rendered documentation *with* the other input argument.  This is very bad and confusing for some users who trust reference manuals, especially because evidently the use of INPUT/OUTPUT blocks to describe parameters of functions is not being used nearly as much as it should be (there will be another ticket about that).




---

Comment by jhpalmieri created at 2009-12-15 02:54:13

Is this only with .pyx files, or are there problems with .py files, too?  A random search through a few files suggests that it's only .pyx files (and perhaps all .pyx files) which cause problems.  I don't know what this means, but maybe someone can figure it out.


---

Comment by mhansen created at 2009-12-15 03:58:52

The problem is that Sphinx needs to use the functions in sage.misc.sageinspect to get the function signature as inspect.getargspec doesn't work with Cython modules.


---

Attachment


---

Attachment


---

Comment by mhansen created at 2009-12-15 10:09:08

I've attached a patch for the Sage library which uses the new spkg at http://sage.math.washington.edu/home/mhansen/sphinx-0.6.3.p3.spkg .  The changes in this spkg are at sphinx-0.6.3.p3.patch .


---

Comment by mhansen created at 2009-12-15 10:09:08

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-12-15 17:46:47

It looks good to me, and I understand the general principle behind the patch, but not necessarily the details.  (For instance, and this has more to do with Sphinx than the patch, why is essentially the same code repeated four times?)

The output seems to fix the complaint, too.  Is this worth reporting to the Sphinx people as a suggested addition to their code?


---

Comment by jhpalmieri created at 2009-12-15 17:46:47

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2009-12-15 17:49:02

Replying to [comment:5 jhpalmieri]:
> It looks good to me, and I understand the general principle behind the patch, but not necessarily the details.  (For instance, and this has more to do with Sphinx than the patch, why is essentially the same code repeated four times?)

(Well, twice, not four times, but still.)


---

Comment by mhansen created at 2009-12-15 17:54:34

One place is for methods and the other is for functions.  

I sent Georg a message about it, but I haven't heard back from him.  I'll try to push this upstream


---

Comment by was created at 2009-12-15 18:44:00

I also give this a positive review.  I tested the code and also read it, and it makes sense to me and works.


---

Comment by mhansen created at 2009-12-16 02:23:29

Resolution: fixed
