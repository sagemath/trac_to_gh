# Issue 6318: optional doctest failure -- axiom interface -- something doesn't work

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 14:46:39

Assignee: tbd

CC:  awebb


```
sage -t -long --optional devel/sage/sage/interfaces/sage0.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/sage0.py", line 252:
    sage: sage0(axiom(x^2+1)) #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[5]>", line 1, in <module>
        sage0(axiom(x**Integer(2)+Integer(1))) #optional - axiom###line 252:
    sage: sage0(axiom(x^2+1)) #optional - axiom
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1026, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1050, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "sage_object.pyx", line 310, in sage.structure.sage_object.SageObject._axiom_ (sage/structure/sage_object.c:3875)
      File "expression.pyx", line 404, in sage.symbolic.expression.Expression._interface_ (sage/symbolic/expression.cpp:3275)
      File "sage_object.pyx", line 248, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2716)
      File "sage_object.pyx", line 315, in sage.structure.sage_object.SageObject._axiom_init_ (sage/structure/sage_object.c:3969)
      File "expression.pyx", line 443, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3536)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/symbolic/expression_conversions.py", line 401, in __init__
        self.relation_symbols = interface._relation_symbols()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1139, in _relation_symbols
        return dict([(operator.eq, self._equality_symbol()), (operator.ne, "!="),
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1105, in _equality_symbol
        raise NotImplementedError
    NotImplementedError
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_sage0.py
	 [8.0 s]
```



---

Comment by was created at 2009-06-16 14:55:32

Here's another optional doctest failure in the sage/axiom/fricas interface:

```
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/rings/integer_mod_ring.py", line 301:
    sage: fricas(Z7) #optional - fricas
Expected:
    IntegerMod(7)
Got:
    IntegerMod 7
**********************************************************************
2 items had failures:
   2 of   4 in __main__.example_6
```



---

Comment by was created at 2009-06-16 14:58:09

Another axiom/fricas failure:

```
sage -t -long --optional devel/sage/sage/rings/integer_mod.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/rings/integer_mod.pyx", line 415:
    sage: aa.type()          #optional - fricas
Expected:
    IntegerMod(15)
Got:
    IntegerMod 15
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_13
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_integer_mod.py
	 [9.0 s]
```



---

Comment by was created at 2009-06-16 15:09:06

More failures:

```
sage -t -long --optional devel/sage/sage/interfaces/fricas.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/fricas.py", line 61:
    sage: F.type()                              # optional - fricas
Expected:
    Factored(Polynomial(Integer))
Got:
    Factored Polynomial Integer
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/fricas.py", line 84:
    sage: print fricas.eval('factor(x^5 - y^5)')   # optional - fricas
Expected:
               4      3    2 2    3     4
    - (y - x)(y  + x y  + x y  + x y + x )    Type: Factored(Polynomial(Integer))
Got:
                 4      3    2 2    3     4

      - (y - x)(y  + x y  + x y  + x y + x )

                                                                                                                                                                                                                 Type: Factored Polynomial Integer

    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/fricas.py", line 129:
    sage: a = fricas(x+2); a  #optional - fricas
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[18]>", line 1, in <module>
        a = fricas(x+Integer(2)); a  #optional - fricas###line 129:
    sage: a = fricas(x+2); a  #optional - fricas
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1026, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1050, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "sage_object.pyx", line 321, in sage.structure.sage_object.SageObject._fricas_ (sage/structure/sage_object.c:4113)
      File "expression.pyx", line 404, in sage.symbolic.expression.Expression._interface_ (sage/symbolic/expression.cpp:3275)
      File "sage_object.pyx", line 248, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2716)
      File "sage_object.pyx", line 324, in sage.structure.sage_object.SageObject._fricas_init_ (sage/structure/sage_object.c:4164)
    TypeError: _interface_init_() takes exactly one argument (0 given)
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/fricas.py", line 131:
    sage: a.subst(x=3)       #optional - fricas
Expected:
    5
Got:
         +-+

      29\|2  + 41
**********************************************************************
1 items had failures:
   4 of  21 in __main__.example_0
***Test Failed*** 4 failures.

```



---

Comment by was created at 2009-06-16 15:16:24

More failures:

```
sage -t -long --optional devel/sage/sage/interfaces/axiom.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 152:
    sage: a = axiom(x+2); a  #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[18]>", line 1, in <module>
        a = axiom(x+Integer(2)); a  #optional - axiom###line 152:
    sage: a = axiom(x+2); a  #optional - axiom
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1026, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1050, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "sage_object.pyx", line 310, in sage.structure.sage_object.SageObject._axiom_ (sage/structure/sage_object.c:3875)
      File "expression.pyx", line 404, in sage.symbolic.expression.Expression._interface_ (sage/symbolic/expression.cpp:3275)
      File "sage_object.pyx", line 248, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2716)
      File "sage_object.pyx", line 315, in sage.structure.sage_object.SageObject._axiom_init_ (sage/structure/sage_object.c:3969)
      File "expression.pyx", line 443, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3536)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/symbolic/expression_conversions.py", line 401, in __init__
        self.relation_symbols = interface._relation_symbols()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1139, in _relation_symbols
        return dict([(operator.eq, self._equality_symbol()), (operator.ne, "!="),
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1105, in _equality_symbol
        raise NotImplementedError
    NotImplementedError
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 154:
    sage: a.subst(x=3)       #optional - axiom
Expected:
    5
Got:
         +-+
      29\|2  + 41
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 551:
    sage: f = axiom(x+2) #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[2]>", line 1, in <module>
        f = axiom(x+Integer(2)) #optional - axiom###line 551:
    sage: f = axiom(x+2) #optional - axiom
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1026, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1050, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "sage_object.pyx", line 310, in sage.structure.sage_object.SageObject._axiom_ (sage/structure/sage_object.c:3875)
      File "expression.pyx", line 404, in sage.symbolic.expression.Expression._interface_ (sage/symbolic/expression.cpp:3275)
      File "sage_object.pyx", line 248, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2716)
      File "sage_object.pyx", line 315, in sage.structure.sage_object.SageObject._axiom_init_ (sage/structure/sage_object.c:3969)
      File "expression.pyx", line 443, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3536)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/symbolic/expression_conversions.py", line 401, in __init__
        self.relation_symbols = interface._relation_symbols()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1139, in _relation_symbols
        return dict([(operator.eq, self._equality_symbol()), (operator.ne, "!="),
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1105, in _equality_symbol
        raise NotImplementedError
    NotImplementedError
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 552:
    sage: f(2)           #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[3]>", line 1, in <module>
        f(Integer(2))           #optional - axiom###line 552:
    sage: f(2)           #optional - axiom
    NameError: name 'f' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 613:
    sage: axiom(x+2).type()  #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[2]>", line 1, in <module>
        axiom(x+Integer(2)).type()  #optional - axiom###line 613:
    sage: axiom(x+2).type()  #optional - axiom
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1026, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1050, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "sage_object.pyx", line 310, in sage.structure.sage_object.SageObject._axiom_ (sage/structure/sage_object.c:3875)
      File "expression.pyx", line 404, in sage.symbolic.expression.Expression._interface_ (sage/symbolic/expression.cpp:3275)
      File "sage_object.pyx", line 248, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2716)
      File "sage_object.pyx", line 315, in sage.structure.sage_object.SageObject._axiom_init_ (sage/structure/sage_object.c:3969)
      File "expression.pyx", line 443, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3536)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/symbolic/expression_conversions.py", line 401, in __init__
        self.relation_symbols = interface._relation_symbols()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1139, in _relation_symbols
        return dict([(operator.eq, self._equality_symbol()), (operator.ne, "!="),
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1105, in _equality_symbol
        raise NotImplementedError
    NotImplementedError
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 704:
    sage: latex(a)       #optional - axiom
Expected:
    \frac{1}{2}
Got:
     1 \over 2   
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 761:
    sage: a = axiom(x^2+1); a     #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[2]>", line 1, in <module>
        a = axiom(x**Integer(2)+Integer(1)); a     #optional - axiom###line 761:
    sage: a = axiom(x^2+1); a     #optional - axiom
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1026, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1050, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "sage_object.pyx", line 310, in sage.structure.sage_object.SageObject._axiom_ (sage/structure/sage_object.c:3875)
      File "expression.pyx", line 404, in sage.symbolic.expression.Expression._interface_ (sage/symbolic/expression.cpp:3275)
      File "sage_object.pyx", line 248, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2716)
      File "sage_object.pyx", line 315, in sage.structure.sage_object.SageObject._axiom_init_ (sage/structure/sage_object.c:3969)
      File "expression.pyx", line 443, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3536)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/symbolic/expression_conversions.py", line 401, in __init__
        self.relation_symbols = interface._relation_symbols()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1139, in _relation_symbols
        return dict([(operator.eq, self._equality_symbol()), (operator.ne, "!="),
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1105, in _equality_symbol
        raise NotImplementedError
    NotImplementedError
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 764:
    sage: a.unparsed_input_form() #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[3]>", line 1, in <module>
        a.unparsed_input_form() #optional - axiom###line 764:
    sage: a.unparsed_input_form() #optional - axiom
    NameError: name 'a' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 767:
    sage: a = fricas(x^2+1)       #optional - fricas
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[4]>", line 1, in <module>
        a = fricas(x**Integer(2)+Integer(1))       #optional - fricas###line 767:
    sage: a = fricas(x^2+1)       #optional - fricas
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1026, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1050, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "sage_object.pyx", line 321, in sage.structure.sage_object.SageObject._fricas_ (sage/structure/sage_object.c:4113)
      File "expression.pyx", line 404, in sage.symbolic.expression.Expression._interface_ (sage/symbolic/expression.cpp:3275)
      File "sage_object.pyx", line 248, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2716)
      File "sage_object.pyx", line 324, in sage.structure.sage_object.SageObject._fricas_init_ (sage/structure/sage_object.c:4164)
    TypeError: _interface_init_() takes exactly one argument (0 given)
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 768:
    sage: a.unparsed_input_form() #optional - fricas
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[5]>", line 1, in <module>
        a.unparsed_input_form() #optional - fricas###line 768:
    sage: a.unparsed_input_form() #optional - fricas
    NameError: name 'a' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 836:
    sage: a = axiom(x^2 + 1)   #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_25[17]>", line 1, in <module>
        a = axiom(x**Integer(2) + Integer(1))   #optional - axiom###line 836:
    sage: a = axiom(x^2 + 1)   #optional - axiom
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1026, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1050, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "sage_object.pyx", line 310, in sage.structure.sage_object.SageObject._axiom_ (sage/structure/sage_object.c:3875)
      File "expression.pyx", line 404, in sage.symbolic.expression.Expression._interface_ (sage/symbolic/expression.cpp:3275)
      File "sage_object.pyx", line 248, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2716)
      File "sage_object.pyx", line 315, in sage.structure.sage_object.SageObject._axiom_init_ (sage/structure/sage_object.c:3969)
      File "expression.pyx", line 443, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3536)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/symbolic/expression_conversions.py", line 401, in __init__
        self.relation_symbols = interface._relation_symbols()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1139, in _relation_symbols
        return dict([(operator.eq, self._equality_symbol()), (operator.ne, "!="),
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1105, in _equality_symbol
        raise NotImplementedError
    NotImplementedError
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 837:
    sage: a.type()             #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_25[18]>", line 1, in <module>
        a.type()             #optional - axiom###line 837:
    sage: a.type()             #optional - axiom
    AttributeError: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'type'
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 839:
    sage: a.sage()             #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_25[19]>", line 1, in <module>
        a.sage()             #optional - axiom###line 839:
    sage: a.sage()             #optional - axiom
    AttributeError: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'sage'
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 841:
    sage: _.parent()           #optional - axiom
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_25[20]>", line 1, in <module>
        _.parent()           #optional - axiom###line 841:
    sage: _.parent()           #optional - axiom
    AttributeError: 'sage.rings.real_mpfr.RealField' object has no attribute 'parent'
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/axiom.py", line 403:
    sage: axiom.get(a.name())          #optional - axiom
Expected:
    '     +-+\r\r\n  29\\|2  + 41'
Got:
    '     +-+\r\n  29\\|2  + 41'
**********************************************************************
7 items had failures:
   2 of  21 in __main__.example_0
   2 of   4 in __main__.example_16
   1 of   3 in __main__.example_18
   1 of   6 in __main__.example_22
   4 of   6 in __main__.example_24
   4 of  23 in __main__.example_25
   1 of   6 in __main__.example_9
***Test Failed*** 15 failures.
For whitespace errors, see the file /hom
```



---

Attachment


---

Comment by awebb created at 2009-06-21 13:48:53

Adding an __init__ method to the FriCAS class should clear up a few issues.


---

Attachment


---

Comment by awebb created at 2009-06-27 12:00:53

Most changes were in the axiom.py and fricas.py files in the interfaces. 
Changes:
 * init method for FriCAS class should call fricas instead of axiom
 * expected output from fricas changed for some things e.g. Tuple PositiveInteger ==> Tuple(PositiveInteger)
 * fix fricas_init in sage_object
 * add equality symbol


---

Comment by mvngu created at 2009-07-12 12:10:08

See also ticket #6517 for an spkg of FriCAS 1.0.7.


---

Comment by awebb created at 2009-07-24 06:44:38

This patch assumes a separate Fricas and Axiom. Axiom was tested using an installed system axiom. I may have not understood something but fricas no longer provides an 'axiom' script. That is, it not longer pretends to be axiom. 

My reading of this thread is that the name axiom is not to used for fricas.
http://trac.sagemath.org/sage_trac/ticket/5111

This thread points out a deviation where fricas is now different then axiom.
http://groups.google.com/group/fricas-devel/browse_thread/thread/86bff34da5720955#

Adam


---

Comment by awebb created at 2009-07-24 16:58:28

Just to clarify. My understanding is that the name Axiom is only for Axiom for copyright reasons and Sage now uses Fricas. As the two programs diverge it seems unreasonable to have an 'axiom' script' point to fricas. However, I may be totally confused about this. 

Adam


---

Comment by awebb created at 2009-11-14 13:55:48

I ran the doctests for axiom.py and fricas.py using axiom (compiled from source -July 2009), and fricas 1.0.8 (from #6517). All tests passed on sage 4.2.1.alpha0.  

Adam


---

Comment by mhansen created at 2009-11-20 05:39:12

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-20 05:39:12

Looks good to me.


---

Comment by mhansen created at 2009-11-20 05:40:04

Resolution: fixed
