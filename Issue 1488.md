# Issue 1488: [with easy patch] fix output of symbolic vectors

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-13 18:10:04

Assignee: was


```


On Dec 13, 2007 9:39 AM, pgdoyle <petergrantdoyle`@`gmail.com> wrote:
> 
> The vector v2 doesn't display properly in the attached Sage output.
> Or rather, the free module element v2.
> (Should I be worried that I got a free module element when I expected
> a vector, or will everything work out for the best?)

Vectors are elements of "free modules" :-).    The "vector" command is just
a command to create vectors. 

The output of vectors with symbolic entries is crap, as you illustrate below. 
I've fixed this:

    

> 
> Cheers,
> 
> Peter
> -----------------------------------
> sage: v1=vector([1/2,1/2])
> sage: v1
> (1/2, 1/2)
> sage: type(v1)
> <type 'sage.modules.vector_rational_dense.Vector_rational_dense'>
> sage: v2=vector([x/(2*x),x/(2*x)])
> sage: v2
> (                                       1
>                                        -
> 
> 2,                                        1
>                                        -
>                                        2)
> sage: type(v2)
> <type
> 'sage.modules.free_module_element.FreeModuleElement_generic_dense'>
> sage: type(v2[1])
> <class 'sage.calculus.calculus.SymbolicArithmetic'>
```



---

Attachment


---

Comment by malb created at 2007-12-13 18:14:56

looks good.


---

Comment by mabshoff created at 2007-12-14 05:13:16

Merged in 2.9.alpha7.


---

Comment by mabshoff created at 2007-12-14 05:13:16

Resolution: fixed
