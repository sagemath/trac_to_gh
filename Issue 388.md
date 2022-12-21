# Issue 388: bug in modular symbol projection function

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-06-22 11:25:44

Assignee: was


```
On 6/21/07, Mak Trifkovic <mak`@`math.uvic.ca> wrote:
> Hi William,
>
> I found an odd thing:
> -----------------------
> S=ModularSymbols(53,sign=1).cuspidal_subspace()[1];S
>
>         Modular Symbols subspace of dimension 3 of Modular Symbols space of
>         dimension 5 for Gamma_0(53) of weight 2 with sign 1 over Rational Field
>
> p=S.projection()
>
>
> S.basis()
>
>         ((1,33) - (1,37), (1,35), (1,49))
>
> for i in [0,1,2]: p(S.basis()[i])
>
>
> (1,35)
> (1,49)
> 0
> ------------------------------
> Shouldn't the projection onto a subspace restricted to that subspace be
> the identity?

Yes.  That's definitely a bug.  Thanks for finding it.
```



---

Comment by mabshoff created at 2007-08-28 11:47:05

This is still an issue with Sage 2.8.2. Maybe it is something for the next bug day:

```
[mabshoff`@`m940 sage-2.8.2]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2, Release Date: 2007-08-22                       |
| Type notebook() for the GUI, and license() for information.        |
sage: S=ModularSymbols(53,sign=1).cuspidal_subspace()[1];S
Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 5 for Gamma_0(53) of weight 2 with sign 1 over Rational Field
sage: p=S.projection()
sage: S.basis()
((1,33) - (1,37), (1,35), (1,49))
sage: for i in [0,1,2]: p(S.basis()[i])
....:
(1,35)
(1,49)
0
sage:
```

Cheers,

Michael


---

Comment by craigcitro created at 2007-09-01 07:42:18

This fixes the bug above. The problem was this: if M is the full space of modular symbols above, SS its cuspidal subspace, and S as above, then S is the 3rd component in the decomposition of M, but the second in the decomposition of SS. At some point, this led to an indexing problem, and the wrong rows of M.decomposition_matrix() were being used to create S.projection.

I fixed this as follows: since M has already been decomposed to get S, I simply use (M.decomposition()).index(S) to find out what the appropriate index is. I could be convinced that there's a more elegant way to do this.

I'm attaching the patch, but it's also available here:

http://sage.math.washington.edu/home/citro/patches/ticket_388.hg

-cc


---

Comment by craigcitro created at 2007-09-01 07:42:18

Changing assignee from was to craigcitro.


---

Comment by was created at 2007-09-01 18:12:07

Resolution: fixed


---

Attachment

looks good to me.
