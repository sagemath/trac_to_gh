# Issue 6: PowerSeriesRing(QQ, 10) crashes SAGE

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-09-12 01:11:15

Assignee: somebody

PowerSeriesRing(QQ, 10) crashes SAGE:

Traceback (most recent call last):
    PowerSeriesRing(QQ, 10)
  File "/home/server/", line 1, in ?
    
  File "/sage/local/lib/python2.4/site-packages/sage/rings/power_series_ring.py",
line 44, in PowerSeriesRing
    R = PowerSeriesRing_over_field(base_ring, name, default_prec)
  File "/sage/local/lib/python2.4/site-packages/sage/rings/power_series_ring.py",
line 171, in __init__
    PowerSeriesRing_generic.__init__(self, base_ring, name, default_prec)
  File "/sage/local/lib/python2.4/site-packages/sage/rings/power_series_ring.py",
line 63, in __init__
    self.__generator = self.__power_series_class(self, [0,1], check=True,
is_gen=True)
  File
"/sage/local/lib/python2.4/site-packages/sage/rings/power_series_ring_element.py",
line 506, in __init__
    f = R(f, check=check)
  File "/sage/local/lib/python2.4/site-packages/sage/rings/multi_polynomial_ring.py",
line 481, in __call__
    c = self.base_ring()(x)
  File "/sage/local/lib/python2.4/site-packages/sage/rings/rational_field.py", line
155, in __call__
    return sage.rings.rational.Rational(x, base)
  File "rational.pyx", line 105, in rational.Rational.__init__
  File "rational.pyx", line 183, in rational.Rational.__set_value
TypeError: Unable to coerce [0, 1] (<type 'list'>) to Rational



---

Comment by was created at 2006-10-15 17:27:47

Fixed

```
def PowerSeriesRing(base_ring, name=None, default_prec=20):
    """
    EXAMPLES:
        sage: R = PowerSeriesRing(QQ); R
        Power Series Ring in x over Rational Field

        sage: S = PowerSeriesRing(QQ, 'y'); S
        Power Series Ring in y over Rational Field
        
        sage: R = PowerSeriesRing(QQ, 10)
        Traceback (most recent call last):
        ...
        TypeError: variable name must be a string or None

        sage: S = PowerSeriesRing(QQ, default_prec = 15); S
        Power Series Ring in x over Rational Field
        sage: S.default_prec()
        15
    """
    #global _objsPowerSeriesRing
    #key = (base_ring, name, default_prec)
    #if _objsPowerSeriesRing.has_key(key):
    #    x = _objsPowerSeriesRing[key]()
    #    if x != None: return x

    if not (name is None or isinstance(name, str)):
        raise TypeError, "variable name must be a string or None"
        
                  
    if isinstance(base_ring, field.Field):
        R = PowerSeriesRing_over_field(base_ring, name, default_prec)
    elif isinstance(base_ring, integral_domain.IntegralDomain):
        R = PowerSeriesRing_domain(base_ring, name, default_prec)
    elif isinstance(base_ring, commutative_ring.CommutativeRing):
        R = PowerSeriesRing_generic(base_ring, name, default_prec)
    else:
        raise TypeError, "base_ring must be a commutative ring"
    #_objsPowerSeriesRing[key] = weakref.ref(R)
    return R
```



---

Comment by was created at 2006-10-15 17:27:47

Resolution: fixed
