# Issue 8897: units.mass.pound to units.mass.drachma broken

Issue created by migration from https://trac.sagemath.org/ticket/8897

Original creator: schilly

Original creation time: 2010-05-05 21:27:48

Assignee: burcin


```
sage: a = 170*units.mass.pound
sage: a.convert(units.mass.drachma)
```

gives

```
TypeError: unable to convert x (=kilogram) to an integer
```

despite 1 drachma is 0.00429234 kilograms.


---

Comment by aginiewicz created at 2012-08-09 11:28:21

Same is true for other units of mass or time, that contains tuples in unitdict:


```
sage: sage.symbolic.units.unitdict['mass']['obol']
"(0.000715380000000000,{'greek':1/6})"
sage: sage.symbolic.units.unitdict['mass']['drachma']
"(0.00429234000000000, {'greek':1})"
sage: sage.symbolic.units.unitdict['mass']['mina']   
"(0.429234000000000, {'greek':100})"
sage: sage.symbolic.units.unitdict['mass']['talent']
"(25.7540400000000, {'greek':6000})"
sage: sage.symbolic.units.unitdict['time']['sidereal_second']
"(0.997269566329086, {'sidereal':1})"
sage: sage.symbolic.units.unitdict['time']['sidereal_day']
"(86164.0905308330, {'sidereal':86400})"
```

all those result in same "unable to convert x to an integer", coming from:

```
sage: sage.symbolic.units.base_units(units.time.sidereal_second)
```

