# Issue 3244: [with patch, needs review] add support for inner plethysms of symmetric functions

Issue created by migration from https://trac.sagemath.org/ticket/3244

Original creator: mhansen

Original creation time: 2008-05-17 20:45:56

Assignee: mhansen

CC:  jbandlow sage-combinat




---

Comment by jbandlow created at 2008-05-22 18:51:58

For the most part this looks really good!  However, before I can give this a positive review, I have two requests for improvement.

1.  Currently

sage: S = SFASchur(QQ); S([]).inner_plethysm(S([2,1]))

blows up. However, in general, S([]).inner_plethysm(S[p]), for p a partition of n, should return S([n]).

2. The doc string currently contains examples, but no explanation.  I propose the following doc for inner_plethysm:

Inner plethysm is a bilinear product on the ring of symmetric functions.  The result of f.inner_plethysm(g) on the Schur functions f = S(la), g = S(mu) can be interpreted as follows.  Setting n = mu.size(), the function g can be thought of as the character of an irreducible representation, $\rho$, of the symmetric group $S_n$.  Let N be the dimension of this representation.  If the number of parts of la is greater then N, then f.inner_plethysm(g) = 0 by definition.  Otherwise, we can interpret f as the character of an irreducible $GL_N$ representation, call it $\sigma$.  Now $\sigma \circ \rho$ is an $S_n$ representation and, by definition, the character of this representation is f.inner_plethysm(g).

REFERENCES:
    King, R. "Branching rules for $GL_m \supset \Sigma_n $ and the evaluation of inner plethysms." J. Math. Phys. 15, 258 (1974)


---

Comment by mhansen created at 2008-05-22 20:15:35

Changing status from new to assigned.


---

Attachment

I updated the patch to address your concerns.  Note that inner plethysm isn't bilinear, but only linear in the first argument.

(I also updated 2144 to have this patch.)


---

Comment by jbandlow created at 2008-05-22 21:45:01

Yes, of course you are right, bilinear is not correct, I have updated doc below.  More troubling to me is that I am now getting:

sage: S = SFASchur(QQ); f = S([2,1])
sage: S([]).inner_plethysm(f)
2*s[3]

According to my reference the answer should be s[3].  Am I wrong about this?

New suggested doc:
            Retuns the inner plethysm of self with x.
            
            The result of f.inner_plethysm(g) is linear in f and linear in
            "homogeneous pieces" of g.  So, to describe this function, we assume
            without loss that f is some Schur function S(la) and g is a
            homogeneous symmetric function of degree n. The function g can be
            thought of as the character of an irreducible representation, rho,
            of the symmetric group S_n. Let N be the dimension of this
            representation. If the number of parts of la is greater then N, then
            f.inner_plethysm(g) = 0 by definition.  Otherwise, we can interpret f
            as the character of an irreducible GL_N representation, call it
            sigma. Now sigma circ rho is an S_n representation and, by
            definition, the character of this representation is
            f.inner_plethysm(g).


---

Attachment

This looks good to me now.  Nice work, Mike.


---

Comment by mabshoff created at 2008-05-25 14:13:41

Merged in Sage 3.0.3.alpha0


---

Comment by mabshoff created at 2008-05-25 14:13:41

Resolution: fixed
