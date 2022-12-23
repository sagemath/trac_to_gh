# Issue 4622: Bug in variety()

Issue created by migration from https://trac.sagemath.org/ticket/4622

Original creator: SimonKing

Original creation time: 2008-11-26 13:57:39

Assignee: malb

Keywords: variety triang.lib

Reported by Alex Raichev at http://groups.google.com/group/sage-support/browse_thread/thread/39b5eeeddebd1910

Slightly simplifying Alex's example, we have

```
sage: R.<w,z>= PolynomialRing(QQ,2,order='lex')
sage: F= 19 -20*z -20*w +5*z^2 +14*z*w +5*w^2 -2*z^2*w -2*z*w^2 +z^2*w^2
sage: G= (w*z-1)*F
sage: I=ideal([G]+G.gradient())
sage: I=ideal(I.groebner_basis())
sage: I
Ideal (w^2 - 2*w - 17/5*z^4 + 434/25*z^3 - 817/25*z^2 + 672/25*z - 179/25, w*z - w + 33/28*z^4 - 433/70*z^3 + 869/70*z^2 - 839/70*z + 641/140, z^5 - 27/5*z^4 + 56/5*z^3 - 56/5*z^2 + 27/5*z - 1) of Multivariate Polynomial Ring in w, z over Rational Field
sage: I.variety()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
```


I repeat the command `I.variety()`, because then the Traceback provides one bit more of information:

```
sage: I.variety()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/Projekte/Cohom/CAS/fullBens/src/<ipython console> in <module>()

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.pyc in variety(self, ring)
   1528         P = self.ring()
   1529         if ring is not None: P = P.change_ring(ring)
-> 1530         T = self.triangular_decomposition('singular:triangLfak')
   1531
   1532         V = []

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.pyc in triangular_decomposition(self, algorithm, singular)
    777             Tbar = Ibar.triangL()
    778         elif algorithm == "singular:triangLfak":
--> 779             Tbar = Ibar.triangLfak()
    780         elif algorithm == "singular:triangM":
    781             Tbar = Ibar.triangM()

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, *args, **kwds)
   1248
   1249     def __call__(self, *args, **kwds):
-> 1250         return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)
   1251
   1252     def help(self):

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in function_call(self, function, args, kwds)
   1168
   1169         return self.new("%s(%s)"%(function, ",".join([s.name() for s in args]+
-> 1170                                                      ['%s=%s'%(key,value.name()) for key, value in kwds.items()])))
   1171
   1172     def call(self, function_name, *args, **kwds):

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in new(self, code)
   1028
   1029     def new(self, code):
-> 1030         return self(code)
   1031
   1032     ###################################################################

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in __call__(self, x, type)
    591             x = str(x)[1:-1]
    592
--> 593         return SingularElement(self, type, x, False)
    594
    595

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in __init__(self, parent, type, value, is_name)
   1007             except (RuntimeError, TypeError, KeyboardInterrupt), x:
   1008                 self._session_number = -1
-> 1009                 raise TypeError, x
   1010         else:
   1011             self._name = value

TypeError: Singular error:
// ** redefining zerlegt
   ? wrong range[2] in ideal/module(1)
   ? error occurred in triang.lib::Erw_ggt_oT line 509: `parameter poly f; parameter  poly g; parameter  int v; parameter  ideal T;  `
   ? wrong type declaration. type 'help poly;'
   ? leaving triang.lib::Erw_ggt_oT
   ? `f` is undefined
   ? error occurred in triang.lib::Erw_ggt_oT line 511: `    poly p1 = f;`
   ? expected poly-expression. type 'help poly;'
   ? leaving triang.lib::Erw_ggt_oT
   skipping text from `;` error at token `)`
   ? leaving triang.lib::invertieren_oT
   ? leaving triang.lib::normieren_oT
   ? leaving triang.lib::Erw_ggt_oT
   ? leaving triang.lib::invertieren_oT
   ? leaving triang.lib::invertieren
   ? leaving triang.lib::triangLbas
   ? leaving triang.lib::triangLfak
```


Some observations:
 * There is a slight inconvenience, but not yet a bug: Singular apparently defines a name `zerlegt` and does not properly kill it. The following line in the Traceback only occurs when running `I.variety()` for the second time.

```
TypeError: Singular error:
// ** redefining zerlegt
```


 * The Traceback continues

```
   ? wrong range[2] in ideal/module(1)
   ? error occurred in triang.lib::Erw_ggt_oT line 509: `parameter poly f; parameter  poly g; parameter  int v; parameter  ideal T;  `
   ? wrong type declaration. type 'help poly;'
```

  hence, it looks like it was tried to address the second generator of an ideal or module in Singular, in order to assign it to either `f` or `g` to the arguments of the function `Erw_ggt_oT` in `triang.lib` -- which failed since the ideal or module only has a single generator.

 * Does that error come from a bug in Sage or a bug in Singular's `triang.lib`? It seems to me it is in `triang.lib`, since the Traceback ends with

```
   ? leaving triang.lib::Erw_ggt_oT
   ? `f` is undefined
   ? error occurred in triang.lib::Erw_ggt_oT line 511: `    poly p1 = f;`
   ? expected poly-expression. type 'help poly;'
   ? leaving triang.lib::Erw_ggt_oT
   skipping text from `;` error at token `)`
   ? leaving triang.lib::invertieren_oT
   ? leaving triang.lib::normieren_oT
   ? leaving triang.lib::Erw_ggt_oT
   ? leaving triang.lib::invertieren_oT
   ? leaving triang.lib::invertieren
   ? leaving triang.lib::triangLbas
   ? leaving triang.lib::triangLfak
}}} 
  and AFAIK only `triangLfak` is directly called by Sage, the rest (in particular the failing call of `Erw_ggt_oT`) happens internally in `triang.lib`.

But even if it is a Singular issue, Michael Abshoff asked me to post it here, so I did.


---

Comment by mabshoff created at 2008-11-28 00:35:34

Another, simpler example by Alex:

```
---------------------------------------------------------------------- 
---------------------------------------------------------------------- 
sage: R.<w>= PolynomialRing(QQ,1) 
sage: H=w 
sage: I= ideal(H); I 
Ideal (w) of Multivariate Polynomial Ring in w over Rational Field 
sage: I.variety() 
--------------------------------------------------------------------------- 
TypeError                                 Traceback (most recent call 
last) 
/Users/arai021/<ipython console> in <module>() 
/Applications/sage/local/lib/python2.5/site-packages/sage/rings/ 
polynomial/multi_polynomial_ideal.pyc in variety(self, ring) 
   1528         P = self.ring() 
   1529         if ring is not None: P = P.change_ring(ring) 
-> 1530         T = self.triangular_decomposition 
('singular:triangLfak') 
   1531 
   1532         V = [] 
/Applications/sage/local/lib/python2.5/site-packages/sage/rings/ 
polynomial/multi_polynomial_ideal.pyc in triangular_decomposition 
(self, algorithm, singular) 
    740         P = self.ring() 
    741 
--> 742         is_groebner = self.basis_is_groebner() 
    743 
    744         # make sure to work w.r.t. 'lex' 
/Applications/sage/local/lib/python2.5/site-packages/sage/rings/ 
polynomial/multi_polynomial_ideal.pyc in basis_is_groebner(self, 
singular) 
   1237         self.ring()._singular_().set_ring() 
   1238 
-> 1239         F = singular( self.gens(), "module" ) 
   1240         LTF = singular( [f.lt() for f in self.gens()] , 
"module" ) 
   1241 
/Applications/sage/local/lib/python2.5/site-packages/sage/interfaces/ 
singular.pyc in __call__(self, x, type) 
    591             x = str(x)[1:-1] 
    592 
--> 593         return SingularElement(self, type, x, False) 
    594 
    595 
/Applications/sage/local/lib/python2.5/site-packages/sage/interfaces/ 
singular.pyc in __init__(self, parent, type, value, is_name) 
   1007             except (RuntimeError, TypeError, 
KeyboardInterrupt), x: 
   1008                 self._session_number = -1 
-> 1009                 raise TypeError, x 
   1010         else: 
   1011             self._name = value 
TypeError: Singular error: 
   ? error occurred in STDIN line 23: `module sage4=w,;` 
   ? expected module-expression. type 'help module;' 
   ? last reserved name was `module` 
 error at token `;` 
```



---

Comment by mabshoff created at 2008-12-01 00:42:47

Simon,

please make the summary of tickets more descriptive.

Cheers,

Michael


---

Comment by malb created at 2009-08-25 19:27:25

This seems to be fixed in (at least) 4.1.1. Simon, can you confirm this?


---

Comment by SimonKing created at 2009-08-25 21:29:37

Replying to [comment:3 malb]:
> This seems to be fixed in (at least) 4.1.1. Simon, can you confirm this?

With Sage 4.1, in the "simpler" example, I get

```
sage: sage: R.<w>= PolynomialRing(QQ,1)
sage: sage: H=w
sage: sage: I= ideal(H); I
Ideal (w) of Multivariate Polynomial Ring in w over Rational Field
sage: sage: I.variety()
verbose 0 (1744: multi_polynomial_ideal.py, variety) Warning: falling back to very slow toy implementation.
[{w: 0}]
```

which seems to be correct, or at least it doesn't crash. 

The original example works as well:

```
sage: R.<w,z>= PolynomialRing(QQ,2,order='lex')
sage: F= 19 -20*z -20*w +5*z^2 +14*z*w +5*w^2 -2*z^2*w -2*z*w^2 +z^2*w^2
sage: G= (w*z-1)*F
sage: I=ideal([G]+G.gradient())
sage: I=ideal(I.groebner_basis())
sage: I
Ideal (w^2 - 2*w - 17/5*z^4 + 434/25*z^3 - 817/25*z^2 + 672/25*z - 179/25, w*z - w + 33/28*z^4 - 433/70*z^3 + 869/70*z^2 - 839/70*z + 641/140, z^5 - 27/5*z^4 + 56/5*z^3 - 56/5*z^2 + 27/5*z - 1) of Multivariate Polynomial Ring in w, z over Rational Field
sage: I.variety()
[{z: 1, w: 1}]
```


So, yes, the crash seems fixed since at least Sage 4.1, probably when Singular was upgraded.


---

Comment by malb created at 2009-08-25 22:38:03

Resolution: fixed
