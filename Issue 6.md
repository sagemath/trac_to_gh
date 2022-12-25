# Issue 6: PowerSeriesRing(QQ, 10) crashes SAGE

archive/issues_000006.json:
```json
{
    "body": "Assignee: somebody\n\nPowerSeriesRing(QQ, 10) crashes SAGE:\n\nTraceback (most recent call last):\n    PowerSeriesRing(QQ, 10)\n  File \"/home/server/\", line 1, in ?\n    \n  File \"/sage/local/lib/python2.4/site-packages/sage/rings/power_series_ring.py\",\nline 44, in PowerSeriesRing\n    R = PowerSeriesRing_over_field(base_ring, name, default_prec)\n  File \"/sage/local/lib/python2.4/site-packages/sage/rings/power_series_ring.py\",\nline 171, in __init__\n    PowerSeriesRing_generic.__init__(self, base_ring, name, default_prec)\n  File \"/sage/local/lib/python2.4/site-packages/sage/rings/power_series_ring.py\",\nline 63, in __init__\n    self.__generator = self.__power_series_class(self, [0,1], check=True,\nis_gen=True)\n  File\n\"/sage/local/lib/python2.4/site-packages/sage/rings/power_series_ring_element.py\",\nline 506, in __init__\n    f = R(f, check=check)\n  File \"/sage/local/lib/python2.4/site-packages/sage/rings/multi_polynomial_ring.py\",\nline 481, in __call__\n    c = self.base_ring()(x)\n  File \"/sage/local/lib/python2.4/site-packages/sage/rings/rational_field.py\", line\n155, in __call__\n    return sage.rings.rational.Rational(x, base)\n  File \"rational.pyx\", line 105, in rational.Rational.__init__\n  File \"rational.pyx\", line 183, in rational.Rational.__set_value\nTypeError: Unable to coerce [0, 1] (<type 'list'>) to Rational\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6\n\n",
    "created_at": "2006-09-12T01:11:15Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "PowerSeriesRing(QQ, 10) crashes SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/6





---

archive/issue_comments_000020.json:
```json
{
    "body": "Fixed\n\n```\ndef PowerSeriesRing(base_ring, name=None, default_prec=20):\n    \"\"\"\n    EXAMPLES:\n        sage: R = PowerSeriesRing(QQ); R\n        Power Series Ring in x over Rational Field\n\n        sage: S = PowerSeriesRing(QQ, 'y'); S\n        Power Series Ring in y over Rational Field\n        \n        sage: R = PowerSeriesRing(QQ, 10)\n        Traceback (most recent call last):\n        ...\n        TypeError: variable name must be a string or None\n\n        sage: S = PowerSeriesRing(QQ, default_prec = 15); S\n        Power Series Ring in x over Rational Field\n        sage: S.default_prec()\n        15\n    \"\"\"\n    #global _objsPowerSeriesRing\n    #key = (base_ring, name, default_prec)\n    #if _objsPowerSeriesRing.has_key(key):\n    #    x = _objsPowerSeriesRing[key]()\n    #    if x != None: return x\n\n    if not (name is None or isinstance(name, str)):\n        raise TypeError, \"variable name must be a string or None\"\n        \n                  \n    if isinstance(base_ring, field.Field):\n        R = PowerSeriesRing_over_field(base_ring, name, default_prec)\n    elif isinstance(base_ring, integral_domain.IntegralDomain):\n        R = PowerSeriesRing_domain(base_ring, name, default_prec)\n    elif isinstance(base_ring, commutative_ring.CommutativeRing):\n        R = PowerSeriesRing_generic(base_ring, name, default_prec)\n    else:\n        raise TypeError, \"base_ring must be a commutative ring\"\n    #_objsPowerSeriesRing[key] = weakref.ref(R)\n    return R\n```\n",
    "created_at": "2006-10-15T17:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6#issuecomment-20",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_000021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-15T17:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6#issuecomment-21",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
