# Issue 1124: ModularSymbol.complement crashes on full subspaces

Issue created by migration from Trac.

Original creator: syazdani

Original creation time: 2007-11-07 18:07:46

Assignee: was

Keywords: zero_subspace

Here is a bug in modular symbols code:
{{{ 
sage: M=ModularSymbols(11,2,1)
sage: M.complement()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/net/mathserv/1/home/syazdani/research/programs/<ipython console> in <module>()

/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/ambient_module.py in complement(self)
     96         Return the largest Hecke-stable complement of this space.
     97         """
---> 98         return self.zero_subspace()
     99
    100     def decomposition_matrix(self):

<type 'exceptions.AttributeError'>: 'ModularSymbolsAmbient_wt2_g0' object has no attribute 'zero_subspace'
}}}

The problem is that zero_subspace is not implemented. Although zero_submodule is.
One possible fix is to change self.zero_subspace to self.zero_submodule(). That's the included patch.


---

Comment by syazdani created at 2007-11-07 18:08:17

trivial patch


---

Attachment

[with patch]


---

Comment by mabshoff created at 2007-11-07 18:19:33

Changing priority from trivial to major.


---

Comment by syazdani created at 2007-11-07 18:25:45

Added doctest for complement. Both patches should be applied.


---

Attachment


---

Comment by was created at 2007-11-18 03:55:34

** "I have reviewed this patch and it agree with it."


---

Comment by mabshoff created at 2007-11-18 14:22:25

Merged in 2.8.13.alpha0.


---

Comment by mabshoff created at 2007-11-18 14:22:25

Resolution: fixed
