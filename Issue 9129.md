# Issue 9129: sqrt memory leaks

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-06-03 13:00:22

Assignee: AlexGhitza

CC:  robertwb malb craigcitro mderickx was burcin jpflori

cf http://groups.google.com/group/sage-support/browse_thread/thread/8c18b2b91004c35a#:

```
sage: m = get_memory_usage()
sage: while True:
    a = ZZ(randint(2^400,2^800)).sqrt()
    print get_memory_usage(m)
```

I noticed another sqrt-related memory leak:

```
sage: cat leak.sage
for i in range(10^6):
   Mod(2^32+1,3).sqrt()
   if i % 10000 == 0:
      print i, get_memory_usage()
sage: load leak.sage
0 947.37109375
10000 970.4375
20000 993.8671875
30000 1017.25
40000 1040.734375
50000 1064.19921875
...
```

This leaks about 23Mb per 10^^4 loops, thus about 2.3Kb per loop!


---

Comment by rlm created at 2010-07-08 12:02:36

I've run valgrind with a clean startup and quit:

http://sage.math.washington.edu/home/rlmill/sage-clean.mem.log

and with an execution of the following loop:

```
for i in range(1000):
    if i%50 == 0:
        print i
    a = ZZ(randint(2^400,2^800)).sqrt()
    b = Mod(2^32+1,3).sqrt()
```


http://sage.math.washington.edu/home/rlmill/sage-sqrt.mem.log

Of particular importance are lines 18757, 16971, 16915, 16831, etc. (Just search through for "definitely")


---

Comment by zimmerma created at 2010-07-08 12:13:59

thanks Robert, however your file is not accessible (neither from the web nor from sage.math).
Paul


---

Comment by rlm created at 2010-07-08 12:17:19

Fixed.


---

Comment by zimmerma created at 2010-07-08 13:01:09

with the following code in Sage 4.4.4:

```
for i in range(10^4):
   a=Mod(2^32+1,3).sqrt()
```

valgrind says:

```
==6861== 5,312,296 bytes in 9,911 blocks are possibly lost in loss record 6,212\
 of 6,212
==6861==    at 0x4A0515D: malloc (vg_replace_malloc.c:195)
==6861==    by 0x4D1E1B8: _PyObject_GC_Malloc (gcmodule.c:1351)
==6861==    by 0x4D1E2AD: _PyObject_GC_NewVar (gcmodule.c:1383)
==6861==    by 0x4C78F80: PyFrame_New (frameobject.c:642)
==6861==    by 0x4CF0324: PyEval_EvalCodeEx (ceval.c:2755)
==6861==    by 0x4C7997A: function_call (funcobject.c:524)
==6861==    by 0x4C4EA72: PyObject_Call (abstract.c:2492)
==6861==    by 0x4C5F0DE: instancemethod_call (classobject.c:2579)
==6861==    by 0x4C4EA72: PyObject_Call (abstract.c:2492)
==6861==    by 0x4CE9022: PyEval_CallObjectWithKeywords (ceval.c:3575)
==6861==    by 0x1E356FA6: __pyx_pf_4sage_9structure_7factory_13UniqueFactory__\
_call__ (factory.c:877)
==6861==    by 0x4C4EA72: PyObject_Call (abstract.c:2492)
==6861==    by 0x4CAD893: slot_tp_call (typeobject.c:5378)
==6861==    by 0x4C4EA72: PyObject_Call (abstract.c:2492)
==6861==    by 0x1BCC2AC6: __pyx_pf_4sage_5rings_12finite_rings_11integer_mod_1\
9IntegerMod_abstract_sqrt (integer_mod.c:6959)
==6861==    by 0x4C4EA72: PyObject_Call (abstract.c:2492)
==6861==    by 0x4CE9022: PyEval_CallObjectWithKeywords (ceval.c:3575)
==6861==    by 0x4C6926B: methoddescr_call (descrobject.c:246)
==6861==    by 0x4C4EA72: PyObject_Call (abstract.c:2492)
==6861==    by 0x4CE9022: PyEval_CallObjectWithKeywords (ceval.c:3575)
==6861==    by 0x1BCA21A8: __pyx_pf_4sage_5rings_12finite_rings_11integer_mod_1\
4IntegerMod_int_sqrt (integer_mod.c:18128)
==6861==    by 0x4CEEEDE: PyEval_EvalFrameEx (ceval.c:3706)
==6861==    by 0x4CF0B44: PyEval_EvalCodeEx (ceval.c:2968)
==6861==    by 0x4CF0C11: PyEval_EvalCode (ceval.c:522)
==6861==    by 0x4CF0287: PyEval_EvalFrameEx (ceval.c:4401)
```

Does it say something to somebody fluent in Pyrex?


---

Comment by rlm created at 2010-07-08 13:03:16

Possibly lost means that the garbage collector is being lazy and is by Python design. You need to look at the line numbers I highlighted in the above files, which are "definitely lost."


---

Comment by zimmerma created at 2010-07-08 13:18:11

Replying to [comment:4 rlm]:
> Fixed.

not quite:

```
-rwx--x--x 1 rlmill rlmill 1219074 2010-07-08 04:58 sage-sqrt.mem.log
```



---

Comment by rlm created at 2010-07-08 13:21:49

sorry... jetlag


---

Comment by zimmerma created at 2010-07-08 13:37:11

Replying to [comment:2 rlm]:
> Of particular importance are lines 18757, 16971, 16915, 16831, etc. (Just search through for "definitely")

those lines seem to indicate the problem lies in the Singular and/or GINAC interface. Any specialist of those interfaces out there?


---

Comment by rlm created at 2010-08-01 11:52:11

Replying to [comment:9 zimmerma]:
> those lines seem to indicate the problem lies in the Singular and/or GINAC interface.

I'm not so sure about this. Let's pick on this particular leak:


```
==25238== 5,320 (1,680 direct, 3,640 indirect) bytes in 35 blocks are definitely lost in loss record 17,325 of 18,340
==25238==    at 0x4C22FEB: malloc (vg_replace_malloc.c:207)
==25238==    by 0x13642E4C: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:29882)
==25238==    by 0x4EC2232: type_call (typeobject.c:731)
==25238==    by 0x4E6CC77: PyObject_Call (abstract.c:2492)
==25238==    by 0x218F6E2B: __pyx_f_4sage_4libs_8singular_8singular_si2sa_ZZ(snumber*, sip_sring*) (singular.cpp:3084)
==25238==    by 0x21902F6D: __pyx_f_4sage_4libs_8singular_8singular_si2sa(snumber*, sip_sring*, _object*) (singular.cpp:5483)
==25238==    by 0x2084D51E: __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular_coefficients(_object*, _object*) (multi_polynomial_libsingular.cpp:27385)
==25238==    by 0x4E6CC77: PyObject_Call (abstract.c:2492)
==25238==    by 0x20858DB0: __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular_gcd(_object*, _object*, _object*) (multi_polynomial_libsingular.cpp:24344)
==25238==    by 0x4E6CC77: PyObject_Call (abstract.c:2492)
==25238==    by 0x4F01D15: PyEval_CallObjectWithKeywords (ceval.c:3575)
==25238==    by 0x4E87C25: methoddescr_call (descrobject.c:246)
==25238==    by 0x4E6CC77: PyObject_Call (abstract.c:2492)
==25238==    by 0x4F01D15: PyEval_CallObjectWithKeywords (ceval.c:3575)
==25238==    by 0xF9E2BB9: __Pyx_PyEval_CallObjectWithKeywords (element.c:26384)
==25238==    by 0xF9D7B3C: __pyx_pf_4sage_9structure_7element_16NamedBinopMethod___call__ (element.c:19673)
==25238==    by 0x4E6CC77: PyObject_Call (abstract.c:2492)
==25238==    by 0x15AF691C: __pyx_f_4sage_5rings_22fraction_field_element_20FractionFieldElement__add_ (fraction_field_element.c:5090)
==25238==    by 0xF9BE0A1: __pyx_pf_4sage_9structure_7element_11RingElement___add__ (element.c:10804)
==25238==    by 0x4E6CF6D: binary_op1 (abstract.c:917)
==25238==    by 0x4E6D41F: PyNumber_Add (abstract.c:1157)
==25238==    by 0x4F0611A: PyEval_EvalFrameEx (ceval.c:1189)
==25238==    by 0x4F0A1C0: PyEval_EvalCodeEx (ceval.c:2968)
==25238==    by 0x4F0A291: PyEval_EvalCode (ceval.c:522)
==25238==    by 0x4F1E371: PyImport_ExecCodeModuleEx (import.c:675)
```


On line 3842 of `multi_polynomial_libsingular.pyx`, we have:

```
        if _ring.ringtype != 0:
            if _ring.ringtype == 4:
                P = self._parent.change_ring(RationalField())
                res = P(self).gcd(P(right))
                coef = sage.rings.integer.GCD_list(self.coefficients() + right.coefficients())   <--------------------
                return self._parent(coef*res)
```


The calls to `.coefficients()` are creating the integers which are not freed. Here is the definition of that function:


```
        cdef poly *p
        cdef ring *r
        r = (<MPolynomialRing_libsingular>self._parent)._ring
        if r!=currRing: rChangeCurrRing(r)
        base = (<MPolynomialRing_libsingular>self._parent)._base
        p = self._poly
        coeffs = list()
        while p:
            coeffs.append(si2sa(p_GetCoeff(p, r), r, base))
            p = pNext(p)
        return coeffs
```


Looks innocent enough... `si2sa` ends up calling:


```
cdef Integer si2sa_ZZ(number *n, ring *_ring):
    ...
    cdef Integer z
    z = Integer()
    z.set_from_mpz(<__mpz_struct*>n)
    return z
```


I really don't see where any of this could be going wrong. I think it has to do with the fast integer creation functions. Sage has a pool of allocated Integer objects. The `integer_pool_count` seems to go up and down randomly, staying in the low range. From one loop to the next, in the original poster's first example, it goes 9, 8, 11, 10, ...

I think that the experts for this memory pool need to step up to the plate...


---

Comment by mderickx created at 2010-11-02 17:15:23

I just tried the second leak in 4.6 on OS X 10.6.4 and the results are:


```
for i in range(10^6):
   t=Mod(2^32+1,3).sqrt()
   if i % 10000 == 0:
      print i, get_memory_usage()
```


```
0 243.6796875
10000 243.6796875
20000 243.6796875
30000 243.6796875
40000 243.6796875
50000 243.6796875
60000 243.6796875
70000 243.6796875
80000 243.6796875
90000 243.6796875
100000 243.6796875
110000 243.6796875
120000 243.6796875
130000 243.6796875
140000 243.6796875
150000 243.6796875
160000 243.6796875
170000 243.6796875
```

After which I interupted the loop since I concluded the leak was no longer there. Can the person who reported this check it on his own machine?


---

Comment by mderickx created at 2010-11-02 17:31:12

The first reported memory leak is still there, but note that you don't need the extemely large random integers i the example to expose the leak. All you need is a non square integer.

Doing the example only with squares in the interval 2!^400 till 2!^800:


```
m = get_memory_usage()
i=0
while True:
    i+=1
    a = ZZ(randint(2^200,2^400)^2).sqrt()
    if i%1000==0:
        print get_memory_usage(m)
```


```
0.0
0.0
0.0
0.0
```

The example using 2 as my favorite non square integer:


```
m = get_memory_usage()
i=0
while True:
    i+=1
    a = 2.sqrt()
    if i%1000==0:
        print get_memory_usage(m)
```

{{{	
0.76953125
1.26953125
2.01953125
2.51953125
3.01953125
3.76953125
4.26953125
5.01953125
6.51953125
}}}


---

Comment by mderickx created at 2010-11-02 19:04:06

I dived a bit deeper into the source code to see what is actually going on and I found that in the end the symbolic ring sqrt function is the one where things go wrong. It's not the general symbolic ring framework since other symbolic ring functions dont misbehave.

```
functions=['arccos', 'arccosh',
'arcsin', 'arcsinh', 'arctan', 'arctanh', 'cos', 'cosh', 'exp', 'log', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
for function in functions:
    print function
    a=SR(2)
    m = get_memory_usage()
    for i in xrange(10000):
        b=a.__getattribute__(function)()
    print get_memory_usage(m)
```

arccos
0.0
arccosh
0.0
arcsin
0.0
arcsinh
0.0
arctan
0.0
arctanh
0.0
cos
0.0
cosh
0.0
exp
0.0
log
0.0
sin
0.0
sinh
0.0
sqrt
7.03125
tan
0.0
tanh
0.0

I'm not able to figure out which code get's called from the symbolic ring part on, since the internal working of the symbolic ring is a bit to complex for me.
Ie. the source code of SR(2).sqrt is

```
return new_Expression_from_GEx(self._parent,
                g_hold2_wrapper(g_power_construct, self._gobj, g_ex1_2, hold))
```

And new_Expression_from_GEx doesn't have any documentation or whatsoever.


---

Comment by zimmerma created at 2010-11-02 19:55:16

I confirm the second leak seems to be fixed now (tried with Sage 4.6 on Fedora and 4.5.2 on
Ubuntu).

The first one is still present in Sage 4.6.

Paul


---

Comment by zimmerma created at 2010-11-02 20:44:52

the problem seems to be in the power function. With Sage 4.6:

```
sage: a=SR(2)
sage: m = get_memory_usage()
sage: for i in xrange(10000):
....:     b=a.__pow__(1/3)
....:     
sage: print get_memory_usage(m)
11.953125
```

Paul


---

Comment by zimmerma created at 2010-11-03 17:31:38

William, Burcin, the memory leaks seems to be in the `g_pow` call at line 2458 of
`symbolic/expression.pyx` (in sage 4.6).

I guess the `g_pow` function is a wrapper to Ginac (from file `libs/ginac/decl.pxi`)
but I could see no occurrence of pow in `c_lib/include/ginac_wrap.h`.

Please can you help?

Paul


---

Comment by burcin created at 2010-11-03 17:54:59

I don't have time to check now, but the `pow()` method of `numeric` objects should be called in this case. You can see the code here:

http://pynac.sagemath.org/hg/file/b233d9dadcfa/ginac/numeric.cpp#l297

There is nothing that immediately catches my eye there.

To experiment, you'll need a pynac development environment:

http://wiki.sagemath.org/pynac/start


---

Comment by burcin created at 2010-11-03 17:57:36

Sorry for the spam, but is the problem still there with the patch at #8659 applied?


---

Comment by zimmerma created at 2010-11-03 18:24:38

Replying to [comment:18 burcin]:
> Sorry for the spam, but is the problem still there with the patch at #8659 applied?

yes, but the leak seems to be smaller:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 8659
sage: a=SR(2)
sage: m = get_memory_usage()
sage: for i in xrange(10000):
....:     b=a.__pow__(1/3)
sage: print get_memory_usage(m)
4.4140625
```

instead of `11.703125` without the #8659 patch.
| Sage Version 4.6, Release Date: 2010-10-30                         |
| Type notebook() for the GUI, and license() for information.        |
Paul


---

Comment by zimmerma created at 2012-01-11 19:36:47

I added some print-statements in `pynac-0.2.3.p0/src/ginac/numeric.cpp` as follows:

```
  Number_T pow(const Number_T& base, const Number_T& exp) {
    std::cerr << "enter pow, base=" << base << " exp=" << exp << "\n";
    verbose("pow");
    if (base.t != exp.t) {
      Number_T a, b;
      std::cerr << "coerce\n";
      coerce(a, b, base, exp);
      return pow(a,b);
    }
    switch (base.t) {
    case DOUBLE:
      std::cerr << "double\n";
      return std::pow(base.v._double, exp.v._double);
    case LONG:
      // TODO: change to use GMP!                                               
      std::cerr << "long\n";
      return std::pow((double)base.v._long, (double)exp.v._long);
    case PYOBJECT:
      std::cerr << "PYOBJECT\n";
      if PyInt_Check(base.v._pyobject) {
          PyObject* o = Integer(PyInt_AsLong(base.v._pyobject));
          PyObject* r = PyNumber_Power(o, exp.v._pyobject, Py_None);
          std::cerr << "PyInt_Check\n";
          Py_DECREF(o);
          return r;
      }
      return PyNumber_Power(base.v._pyobject, exp.v._pyobject, Py_None);
    default:
      stub("invalid type: pow Number_T");
    }
  }
```

Then it seems that for inexact powers that function is called twice for SR input:

```
sage: SR(2).__pow__(1/2)
enter pow, base=2 exp=1/2
PYOBJECT
enter pow, base=2 exp=1/2
PYOBJECT
sqrt(2)
```

but for exact powers only once:

```
sage: SR(4).__pow__(1/2)
enter pow, base=4 exp=1/2
PYOBJECT
2
```


For Integer input we get:

```
sage: Integer(2).__pow__(1/2)
enter pow, base=2 exp=1/2
PYOBJECT
sqrt(2)
sage: Integer(4).__pow__(1/2)
2
```


For ZZ input we get:

```
sage: ZZ(2).__pow__(1/2)
enter pow, base=2 exp=1/2
PYOBJECT
sqrt(2)
sage: ZZ(4).__pow__(1/2)
2
```

In all cases there is no memory leak for exact powers, but there is for inexact powers.
Thus I strongly suspect some special code that detects exact powers, but where is it?

Paul


---

Comment by zimmerma created at 2012-01-11 19:57:18

Changing keywords from "" to "sd35.5".


---

Comment by burcin created at 2012-02-15 16:46:01

Replying to [comment:20 zimmerma]:

> In all cases there is no memory leak for exact powers, but there is for inexact powers.
> Thus I strongly suspect some special code that detects exact powers, but where is it?

The `__pow__` method of rational numbers. :) When computing `2^(1/2)`, `Integer.__pow__` delegates the operation to `Rational.__pow__`. If the result is not exact, `Rational.__pow__` returns a symbolic expression.

This should really be tested with the patch at #8659, which eliminates the need to call `Number_T::pow()` twice. Even with that patch, the leak is still there however.


---

Comment by zimmerma created at 2012-06-22 14:05:17

I updated the description.

Paul

PS: it seems the "stopgaps" were deleted, but I don't know which value it was...


---

Comment by zimmerma created at 2013-08-23 12:07:04

update with Sage 5.11, the memory leaks is still there:

```
+--------------------------------------------------------------------+
+--------------------------------------------------------------------+
sage: m = get_memory_usage()
sage: i=0
sage: while True:
....:         i+=1
....:         a = 2.sqrt()
....:         if i%1000==0:
....:                 print get_memory_usage(m)
....:         
0.18359375
0.18359375
0.18359375
0.546875
0.8203125
1.5859375
1.96875
2.34765625
2.734375
3.50390625
```

Paul


---

Comment by ryan created at 2014-01-31 06:07:20

I'm not sure what the current status of work on this ticket is, but I have noticed that
the following functions do not exhibit the demonstrated memory leak.


```
def memleaksr(n, x, p=1/2):
    m = get_memory_usage()
    one_half = SR(.5)
    for i in xrange(n):
        a = SR(x)^one_half
        if(i % 1000 == 0):
            print get_memory_usage(m)
```




```
def memleakonehalf(n, x, p=1/2):
    m = get_memory_usage()

    for i in xrange(n):
        a = SR(x) ** 1/2
        if(i % 1000 == 0):
            print get_memory_usage(m)
```


From what I understand, 
2.sqrt() calls the sqrt() method of the Integer class.
sqrt() 
eventually sage.functions.other._do_sqrt() is called.  If _do_sqrt is passed a precision argument, everything works fine.  The memory leak seems to occur when no precision is set.  Something about the variable one_half in _do_sqrt() seems to throw a kink in things.

Recap: If any precision is set, then there is no memory leak (2.sqrt(prec=52) == no memory leak)


---

Comment by zimmerma created at 2014-01-31 07:52:46

the second example in the description still does a memory leak with Sage 6.0:

```
┌────────────────────────────────────────────────────────────────────┐
│ Sage Version 6.0, Release Date: 2013-12-17                         │
│ Type "notebook()" for the browser-based notebook interface.        │
│ Type "help()" for help.                                            │
└────────────────────────────────────────────────────────────────────┘
sage: m = get_memory_usage()
sage: i=0
sage: while True:
....:         i+=1
....:         a = 2.sqrt()
....:         if i%1000==0:
....:                 print get_memory_usage(m)
....:         
0.0
0.0
0.0
0.58984375
0.84375
1.234375
1.7421875
2.3828125
2.76171875
3.1484375
3.66796875
4.3203125
4.703125
5.08984375
5.4765625
6.23828125
```

The fact that it works with `prec` does not help for this ticket, which deals with exact square root.


---

Comment by ryan created at 2014-01-31 19:07:18

Yes, 2.sqrt() does still have a memory leak in 6.0

You're right, I wasn't thinking.  2.sqrt() returns a symbolic expression.  My examples return a real number.


---

Comment by mmezzarobba created at 2014-02-15 11:56:22

I investigated a bit, and I believe there's a `Py_DECREF(restuple)` missing in Pynac's `GiNaC::power::eval`, around line 590 of `power.cpp`.


---

Comment by zimmerma created at 2014-02-15 16:43:03

well done! Does it solve the memory leak?

Paul


---

Comment by mmezzarobba created at 2014-02-15 17:36:03

Replying to [comment:32 zimmerma]:
> well done! Does it solve the memory leak?

I think it would, but I didn't actually try to fix it.


---

Comment by mmezzarobba created at 2014-02-21 10:38:50

See also:

http://hg.pynac.org/pynac/issue/19/memory-leak-in-power-eval


---

Comment by vbraun created at 2014-03-19 05:23:47

Implemented at https://bitbucket.org/vbraun/pynac/commits/4c798d4cb4b50532fc525ad652d7f0db79eb08c1

With the patch it still leaks but much slower

```
:sage: m = get_memory_usage()
:sage: i=0
:sage: while True:
:....:         i+=1
:....:         a = 2.sqrt()
:....:         if i%1000==0:
:....:                 print get_memory_usage(m)
:....:         
:--
0.0
0.0
0.0
0.0
0.0
0.0
0.25
0.25
0.25
0.25
0.25
0.5
0.5
0.5
0.5
0.5
0.5
0.875
0.875
0.875
0.875
1.00390625
1.28515625
```



---

Comment by vbraun created at 2014-03-19 18:20:19

Fixed another leak at https://bitbucket.org/vbraun/pynac/commits/598291652f2fc645f2d2f150b39040af07eb6554

Now the above script does not leak any more...


---

Comment by zimmerma created at 2014-03-19 22:02:41

well done Volker! Just a pity it took 4 years to fix that issue...

Paul


---

Comment by vbraun created at 2014-03-20 01:51:31

Feel free to file the upstream bug report faster next time ;-)


---

Comment by zimmerma created at 2014-03-20 09:02:20

> Feel free to file the upstream bug report faster next time ;-) 

the problem is that I had no idea in which upstream component the leak was (or in Sage), and I had no idea how to search where the leak was.

If you can give some information how we can do this in similar cases, it would be very helpful.

Paul


---

Comment by vbraun created at 2014-03-20 14:06:52

Changing status from new to needs_review.


---

Comment by vbraun created at 2014-03-20 14:06:52

Will be fixed by the pynac update at #14780


---

Comment by mmezzarobba created at 2014-03-22 07:08:19

Replying to [comment:40 zimmerma]:
> If you can give some information how we can do this in similar cases, it would be very helpful.

Fwiw, I used the `objgraph` module to see what kind of objects were being leaked. It turned out to be triples similar to those returned by `pynac.pyx`:`py_rational_power_parts`—the hardest part was probably to discover that function, but the observation that the leak occurred specifically for non-square integers helped.


---

Comment by mmezzarobba created at 2014-03-22 07:12:46

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2014-03-22 08:31:41

could we add a small doctest checking that the leak is gone?

Paul


---

Comment by vbraun created at 2014-03-22 14:39:34

Changing status from positive_review to needs_review.


---

Comment by vbraun created at 2014-03-22 14:39:34

Please review, then.
----
New commits:


---

Comment by git created at 2014-03-22 14:41:31

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmezzarobba created at 2014-04-11 09:37:11

Changing status from needs_review to positive_review.


---

Comment by mmezzarobba created at 2014-04-11 09:37:11

Changing priority from critical to major.


---

Comment by mmezzarobba created at 2014-04-11 09:37:11

lgtm. Paul, please complain if you disagree, since you were the one who asked for a regression test!


---

Comment by zimmerma created at 2014-04-11 09:50:29

> please complain if you disagree

I agree, thank you to everybody!


---

Comment by vbraun created at 2014-04-13 19:33:30

Resolution: fixed
