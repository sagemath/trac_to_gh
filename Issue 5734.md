# Issue 5734: Bring doctests of modular/modsym/manin_symbols.py up to 100%

Issue created by migration from https://trac.sagemath.org/ticket/5734

Original creator: cremona

Original creation time: 2009-04-10 16:09:32

Assignee: mabshoff

CC:  davidloeffler mtaranes

Keywords: modular symbols

As of 3.4.1.rc1, we have

```
SCORE /home/jec/sage-3.4.1.rc1/devel/sage-main/sage/modular/modsym/manin_symbols.py: 2% (2 of 68)

Missing documentation:
	 * is_ManinSymbol(x):
	 * __init__(self, weight, list):
	 * __cmp__(self, right):
	 * __getitem__(self, n):
	 * __len__(self):
	 * apply(self, j, X):
	 * apply_S(self, j):
	 * apply_I(self, j):
	 * apply_T(self, j):
	 * apply_TT(self, j):
	 * manin_symbol_list(self):
	 * manin_symbol(self, i):
	 * normalize(self, x):
	 * weight(self):
	 * __init__(self, level, weight, syms):
	 * apply_T(self, j):
	 * apply_TT(self, j):
	 * level(self):
	 * normalize(self, x):
	 * __init__(self, level, weight):
	 * __repr__(self):
	 * __init__(self, level, weight):
	 * __repr__(self):
	 * __init__(self, group, weight):
	 * __repr__(self):
	 * __init__(self, character, weight):
	 * __repr__(self):
	 * apply_T(self, j):
	 * apply_TT(self, j):
	 * character(self):
	 * level(self):
	 * normalize(self, x):
	 * __init__(self, level, weight):
	 * __repr__(self):
	 * apply_T(self, j):
	 * apply_TT(self, j):
	 * level(self):
	 * normalize(self, x):
	 * tuple(self):
	 * __get_i(self):
	 * __get_u(self):
	 * __get_v(self):
	 * _repr_(self):
	 * _latex_(self):
	 * __cmp__(self, other):
	 * __mul__(self, matrix):
	 * copy(self):
	 * parent(self):
	 * weight(self):
	 * _print_polypart(i, j):


Missing doctests:
	 * index(self, x):
	 * apply_S(self, j):
	 * apply_I(self, j):
	 * apply(self, j, m):
	 * apply_S(self, j):
	 * apply_I(self, j):
	 * index(self, x):
	 * apply_S(self, j):
	 * apply_I(self, j):
	 * apply_J(self, j):
	 * apply(self, j, m):
	 * __init__(self, parent, t):
	 * apply(self, a,b,c,d):
	 * lift_to_sl2z(self, N):
	 * endpoints(self, N=None):
	 * modular_symbol_rep(self):
```

and I think I might have the right background to fix this!


---

Comment by cremona created at 2009-04-13 12:07:45

David, I thought you might like this one too (when I have done it)  -J


---

Attachment

The patch touches only sage/modular/modsym/manin_symbols.py, based on 3.4.1.rc2.

```
----------------------------------------------------------------------
sage/modular/modsym/manin_symbols.py
SCORE sage/modular/modsym/manin_symbols.py: 100% (59 of 59)
----------------------------------------------------------------------
```


I also fixed some small bugs in functions which did not seem to be used, removed (by commenting out) a class `x__ManinSymbolList_gamma1` which was not used, and implemented a slightly more sensible cmp() function for class ManinSymbol (which used to return 1 for any two distinct symbols).  All doctests in sage/modular pass, and I also checked quite thoroughly through the resulting reference manual page, which also looks good.

Review please!


---

Comment by davidloeffler created at 2009-04-15 13:30:51

apply over previous patch


---

Attachment

This looks great: applies fine to 3.4.1.rc2, all doctests pass, and documentation builds happily.

I've made a few slight adjustments to the formatting (mainly enforcing a consistent convention that INPUT: is always followed by a bulleted list and OUTPUT: never is, which was true for most but not all of the new doctests), and I've added an x == loads(dumps(x)) doctest for each of the classes that are actually intended for direct use. (There was a loads(dumps()) test in the file already, so sage -coverage didn't protest, but it was commented out, and it was for a different class anyway.)

John: if you're happy with the changes I've made, feel free to change this to "positive review".


---

Comment by cremona created at 2009-04-15 14:16:08

I am happy.  Thanks for going through this carefully.   I also think that the conventions to be followed in these new-style docstrings should be written down somewhere!


---

Comment by mabshoff created at 2009-04-15 19:57:14

Merged both patches in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 19:57:14

Resolution: fixed
