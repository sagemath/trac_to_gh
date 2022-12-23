# Issue 372: singular interface memory leaks

Issue created by migration from https://trac.sagemath.org/ticket/372

Original creator: was

Original creation time: 2007-05-20 22:36:12

Assignee: michel v


```
On 5/20/07, Michel <michel.vandenbergh@uhasselt.be> wrote:
>
> While doing "singular.interact()" I see that lots and lots
> of variables (named: sage*) are being defined in the singular
> interface.
> Basically for every intermediate result and then some.
> I have not looked in detail but are these variables recycled when the
> corresponding python object goes out of scope?

They are not reused.  The code is there in interfaces/singular.py,
but it's not used right now because everything I tried to reuse
or clear variables in Singular resulted in all kinds of problems,
probably partly because Singular is somewhat statically typed.
I've always meant to look into this again.   In the other interfaces
(which are all dynamically typed) variables are recycled when they
aren't used anymore.

> Otherwise this is a memory leak (these variables usual contain
> polynomials).

Indeed.   Please feel free to work on fixing this.

```



---

Comment by was created at 2007-05-31 15:10:21

Resolution: fixed
