# Issue 389: bug in mpfi C library

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-06-22 11:30:37

Assignee: somebody

There is a bug in the mpfi C library for interval arithmetic, which leads to an infinite loop in SAGE:


```
wonder if there is something wrong with the interval cosine
calculation?  cos seems to loop forever on [-1 .. +1].  Try this:

sage: x = RealInterval(-1.1,1.1)
sage: x.cos()
[0.453596121425577307 .. 1.00000000000000000]
sage: x = RealInterval(-1.0,1.0)
sage: x.cos()
---------------------------------------------------------------------------
<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call
last)

/files/home/nholtz/<ipython console> in <module>()

------



Just as a followup, in case anyone cares ...

The problem is definitely in libmpfi, as I can duplicate
the infinite loop problem in computing mpfi_cos([-1.0,1.0]) in C.

I have notified the maintainers of libmpfi, and we'll see what
happens.

neal

On Jun 19, 11:16 am, neal <nho...`@`docuweb.ca> wrote:
> I wonder if there is something wrong with the interval cosine
> calculation?  cos seems to loop forever on [-1 .. +1].  Try this:
```



---

Comment by mabshoff created at 2007-08-19 06:10:11

The following code reproduces the problem:

```
#include "mpfi.h"

int main()
{
    mpfi_t SinX,X;
    mpfi_init(X);
    mpfi_init(SinX);
    mpfr_set_si (&(X->left), -1, GMP_RNDN);
    mpfr_set_ui (&(X->right), 1, GMP_RNDN);
    mpfi_cos (SinX, X);

}
```

A bug has been open since 2007-01-17 09:22 at the mpfi bug tracker. See 
http://gforge.inria.fr/tracker/index.php?func=detail&aid=1868&group_id=157&atid=709

To quote the bug report:
> [this bug was mentioned to me by Sylvain Chevillard]
>
> The internal mpfi_cmp_sym_pi function loops when z=0 and y=-x
> in mpfi-1.3.4-RC3.

Cheers,

Michael


---

Attachment

There is a new MPFI spkg at http://sage.math.washington.edu/home/cwitty/mpfi-1.3.4-rc3.p9.spkg that fixes this (it also includes a minor fix from Paul Zimmerman, for mpfi_ui_sub()).

The attached patch adds a doctest for the new package.  With the old spkg, the doctest will loop forever; with the new spkg, it works.


---

Comment by mabshoff created at 2007-11-02 19:41:14

Resolution: fixed


---

Comment by mabshoff created at 2007-11-02 19:41:14

applied to 2.8.11.rc2, spkg updated.
