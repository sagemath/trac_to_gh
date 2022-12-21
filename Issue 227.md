# Issue 227: sagex: should use NULL instead of 0

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-28 20:27:53

Assignee: was


```
  While I understand that it's best for the Pyrex code to be the main
reference, and for the C code to be re-generated at compilation
time, I can see situations where that won't happen - for example if
gcc is an admin-supported compiler, and thus part of some automated
build system, by pyrexc is not. The generated C might then be used
as the reference, and portions could be extracted and used elsewhere,
perhaps without proper prototyping. Or perhaps there is some new
version of a library, and the functions you are using are no longer
declared in the header files you've included - this would be picked up
by pyrexc, but not by the automated gcc build system.
 
  Now suppose that you have some function that takes a pointer, and
the generated code passes it a 0 instead of a NULL. In the absence
of a prototype, the 0 is an integer by default, whereas NULL is a void *.
Suppose further that you're compiling on a platform on which integers
and pointers have different storage sizes, which is becoming more
common as memory sizes increase while integers are often left at
32 bits. This scenario would lead to corruption of the stack, in a way
that will be hard to find - especially if you aren't aware of the storage
size mismatch - though easy to fix.
 
  While it is somebody else's stupid mistake that causes the problem,
it is my code that would get a bad reputation as a result.
 
  I do realize that this is a pedantic point here, but there is a difference
between 0 and NULL, and there is a "correct" way to do this, and since
Pyrex already recognizes that NULL is a special case, the least it could
do would be to preserve it.
 
Thanks.
 
On 1/26/07, Greg Ewing <greg.ewing`@`canterbury.ac.nz> wrote:
> Adapted Cat wrote:
> > Even though NULL is a reserved word in Pyrex, the generated C
> > code uses 0.
> >
> > Could the NULL be preserved in the C code, please?
>  
> Why? The only situation I know of where it could make
> a difference is if you were using old K&R-style function
> headers, which Pyrex doesn't.
>  
> > Also, it seems that there is no way to declare a C array pre-filled
> > with directly in Pyrex.
>  
> That's true. It's on my list, but it doesn't have a
> very high priority at the moment.
>  
> --
> Greg
>  
>  
 
_______________________________________________
Pyrex mailing list
Pyrex`@`lists.copyleft.no
http://lists.copyleft.no/mailman/listinfo/pyrex
```



---

Comment by was created at 2007-08-18 23:29:16

Changing type from defect to enhancement.


---

Comment by was created at 2007-08-18 23:29:16

Changing component from algebraic geometry to packages.


---

Comment by was created at 2007-08-29 02:09:25

This input code

```
%cython

cdef void* bar():
    return NULL
```


generates this output code

```
static void (*__pyx_f_61_home_was_sage_notebook_worksheets_admin_34_code_sage4_spyx_0_bar(void)) {
  void (*__pyx_r);

  /* "/home/was/.sage/temp/ubuntu/32525/spyx/_home_was_sage_notebook_worksheets_admin_34_code_sage4_spyx/_home_was_sage_not
ebook_worksheets_admin_34_code_sage4_spyx_0.pyx":7
 * include "cdefs.pxi"
 * cdef void* bar():
 *     return NULL             # <<<<<<<<<<<<<<
 */
  __pyx_r = NULL;
  goto __pyx_L0;

  __pyx_L0:;
  return __pyx_r;
}
```


So this issue is fixed.


---

Comment by was created at 2007-08-29 02:09:30

Resolution: fixed
