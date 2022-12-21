# Issue 9540: Testing whether a Gaussian integer is in ZZ is extremely slow

Issue created by migration from Trac.

Original creator: fredrik.johansson

Original creation time: 2010-07-18 16:28:32

Assignee: AlexGhitza


```
sage: x = 5
sage: y = 3/5
sage: z = (5+I).pyobject()
sage: z.parent()
Number Field in I with defining polynomial x^2 + 1
sage: %timeit x in ZZ
625 loops, best of 3: 103 ns per loop
sage: %timeit y in ZZ
625 loops, best of 3: 7.19 µs per loop
sage: %timeit z in ZZ
625 loops, best of 3: 381 µs per loop

```


By extension, this massively affects performance of the ._is_integer() method for symbolic expressions containing complex numbers.


---

Comment by kcrisman created at 2013-05-10 16:20:35

See also #7545.


---

Comment by kedlaya created at 2016-05-07 05:19:26

By way of comparison:

```
sage: %timeit z in ZZ
The slowest run took 7.79 times longer than the fastest. This could mean that an intermediate result is being cached.
10000 loops, best of 3: 58 µs per loop
sage: %timeit z.is_integer() #should return the same answer
The slowest run took 82.03 times longer than the fastest. This could mean that an intermediate result is being cached.
10000000 loops, best of 3: 72.7 ns per loop
```



---

Comment by tscrim created at 2016-05-07 12:26:02

`ZZ.__contains__` is the default `Parent.__contains__`, and as such, checks by seeing if `z` can convert into itself. However, what is interesting is the difference between `y` and `z`. Both have a Python `_integer_` in a Cython file. I am wondering if it has to do with the difference in the conversion maps between their respective parents:

```
sage: ZZ.convert_map_from(y.parent())
Generic map:
  From: Rational Field
  To:   Integer Ring
sage: ZZ.convert_map_from(z.parent())
Conversion via _integer_ method map:
  From: Number Field in I with defining polynomial x^2 + 1
  To:   Integer Ring
```

However, there are a lot more computations done for `z` than for `y`:

```
sage: %prun y in ZZ
         2 function calls in 0.000 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
sage: %prun z in ZZ
         32 function calls in 0.000 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 polynomial_ring.py:299(_element_constructor_)
        1    0.000    0.000    0.000    0.000 polynomial_ring_constructor.py:50(PolynomialRing)
        1    0.000    0.000    0.000    0.000 rings.py:708(__getitem__)
        1    0.000    0.000    0.000    0.000 number_field.py:4871(gen)
        2    0.000    0.000    0.000    0.000 re.py:230(_compile)
        1    0.000    0.000    0.000    0.000 {sage.structure.category_object.normalize_names}
        1    0.000    0.000    0.000    0.000 rings.py:827(normalize_arg)
        1    0.000    0.000    0.000    0.000 polynomial_ring_constructor.py:497(_single_variate)
        2    0.000    0.000    0.000    0.000 {method 'sub' of '_sre.SRE_Pattern' objects}
        1    0.000    0.000    0.000    0.000 polynomial_ring_constructor.py:482(_get_from_cache)
        2    0.000    0.000    0.000    0.000 re.py:148(sub)
       10    0.000    0.000    0.000    0.000 {isinstance}
        1    0.000    0.000    0.000    0.000 rational_field.py:233(_repr_option)
        2    0.000    0.000    0.000    0.000 {sage.structure.element.is_Element}
        1    0.000    0.000    0.000    0.000 {sage.rings.ring.is_Ring}
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

Note: the first time this is run, there are more computations for both of them likely due to creating the conversion and checking if there is a coercion. In a fresh session:

```
sage: y = 3/5
sage: z = (5+I).pyobject()
sage: %time y in ZZ
CPU times: user 171 µs, sys: 30 µs, total: 201 µs
Wall time: 195 µs
False
sage: %time z in ZZ
CPU times: user 1.02 ms, sys: 0 ns, total: 1.02 ms
Wall time: 485 µs
False
```



---

Comment by mmezzarobba created at 2021-04-11 13:07:27

The conversion from `QQ` to `ZZ` actually bypasses the `_integer_` method: instead, it uses `sage.rational.Q_to_Z` (discovered as the canonical section of the coercion in the reverse direction). No such fast conversion is implemented for quadratic number field elements.


---

Comment by saraedum created at 2022-08-22 09:44:07

Conversely, the conversion from the integers to the Gaussian integers, also is somewhat slow, see #34408.
