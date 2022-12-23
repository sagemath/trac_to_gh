# Issue 4062: Problems with Eisenstein series code?

Issue created by migration from https://trac.sagemath.org/ticket/4062

Original creator: craigcitro

Original creation time: 2008-09-04 15:58:27

Assignee: craigcitro

This was reported to `sage-support`:


```
Hi,

When computing Eisenstein series with a given character, Sage may
return some forms with a wrong character.  The following lines show an
example of this:

sage: G = DirichletGroup(7)
sage: E = EisensteinForms(G[4]).eisenstein_series()
sage: E[0].character() == G[4]
False

The problem appears to be caused by the condition

 if chi*psi == eps:

in the function __find_eisen_chars in modular/modform/eis_series.py.
According to Miyake, _Modular Forms_, Lemma 7.1.1 (cited in a comment
in this function), it should be

 if chi == eps*psi:

Another bug is that Sage uses an incorrect formula to compute q-
expansions of Eisenstein series.  Here the origin of the problem seems
to be formula (5.3.1) in Stein, _Modular Forms: A Computational
Approach_, where the psi(n) should be replaced by its complex
conjugate (cf. Miyake, _Modular Forms_, Theorem 4.7.1 and the first
three lines of page 271).  The method __compute_general_case of the
class EisensteinSeries in modular/modform/element.py reproduces this
formula in the form

 v.append(sum([psi(n)*chi(m/n)*n**(k-1) for n in rings.divisors(m)]))

Here psi should be ~psi.

Thanks,

Peter Bruin
```



---

Attachment

This is a fix for the above problem. In fact, the fix was suggested by Peter Bruin, who originally reported the fix. Here's what he had to say:


```
The other possibility is to define E_{k,chi,psi} as the unique modular
form whose L-series equals L(s,chi) L(s-k+1,psi); this is the form
which Miyake considers in Theorem 4.7.1 (cf. E. Hecke, Math. Ann. 114
(1937), 316--351 [= Mathematische Werke, 672--707]).  Then the
formulas for the q-expansion as they are now in William Stein's book
and in Sage remain correct (i.e. without replacing psi by its
conjugate), and the change that should be made in this case (in the
book and in Sage) is to change the relation between chi, psi and the
character epsilon of E_{k,chi,psi} from

 chi = epsilon * psi

to

 chi * psi = epsilon.

This would mean that the comment (not the code!) in __find_eisen_chars
in eis_series.py should be changed (refer to Miyake's Theorem 4.7.1),
and that in the method called `character' of the class
EisensteinSeries in element.py, the line

 self.__character = self.__chi * (~self.__psi)

should be replaced by

 self.__character = self.__chi * self.__psi
```


The attached patch fixes this, and adds a few doctests to catch it in the future. Credit for the patch should also go to Peter.


---

Comment by craigcitro created at 2008-10-30 09:13:37

Changing status from new to assigned.


---

Comment by was created at 2008-10-30 16:29:23

Further remarks from craig:

```
I posted a fix for the Eisenstein series bug that was reported a
little bit ago. (Kevin, I'm cc'ing you because William said he
mentioned this bug to you, too.) The original poster was right: his
snippet of code takes a character chi, asks for a weight two
Eisenstein series f in M_k(Gamma_1(N), chi), and then asks for
f.character() -- and Sage says that it isn't chi! So that was the bug.
The fix he starts detailing in his original post is completely the
wrong direction -- he's somehow trying to correct the series to match
the character that's getting returned. He later realized that the
right fix was actually to change the character returned.
```


and from Kevin:

```
The only comment I had about the report was that it sounded to me that the poster had perhaps misunderstood the port of the theorem in Miyake to Sage---he seemed to be saying "this character should be replaced by its conjugate in several places", not realising that the notation in the sage code was that the character in the code sounded to me like it was by definition the conjugate of the character in Miyake.
```



---

Comment by davidloeffler created at 2008-11-03 16:02:23

Patch applies fine to 3.2.alpha1 and all doctests in sage/modular/modform pass. I've also evaluated some Eisenstein series numerically at various points in the upper half-plane to check that the forms that are being returned really do have the characters they're supposed to, and that does check out, which is reassuring.


---

Comment by mabshoff created at 2008-11-04 14:05:28

Merged in Sage 3.2.alpha3


---

Comment by mabshoff created at 2008-11-04 14:05:28

Resolution: fixed
