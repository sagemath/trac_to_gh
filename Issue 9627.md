# Issue 9627: converting from symbolic ring to int is broken,

Issue created by migration from Trac.

Original creator: syazdani

Original creation time: 2010-07-28 20:33:03

Assignee: robertwb

CC:  katestange mjo

Here is simple example:

```
sage: h = 3^64;
sage: int(h)==int(SR(h))
FALSE
```

Looking a bit deeper into this, it seems that the first 100 bits are correct, and after that int(SR(h)) is just zeroes. (As a side note, the conversion to ZZ works without a problem.)



---

Comment by tornaria created at 2010-07-28 21:01:11

Changing status from new to needs_work.


---

Comment by tornaria created at 2010-07-28 21:01:11

Yikes!

```
    def __int__(self):
        """
        EXAMPLES::
        
            sage: int(sin(2)*100)
            90
            sage: int(log(8)/log(2))
            3
        """
        #FIXME: can we do better?
        return int(self.n(prec=100))
```


Can we just change that to

```
        return int(self._integer_())
```

?


---

Comment by tornaria created at 2010-07-28 21:12:58

OTOH,

```
sage: ZZ(log(8)/log(2))
...
TypeError: unable to convert x (=log(8)/log(2)) to an integer
```

but

```
sage: int(log(8)/log(2))  
3
```


OTOH, `int(sin(2)*100)` is not equal to 90... not an integer anyway... What's the expected meaning of `int(x)`?


---

Comment by tornaria created at 2010-07-28 21:12:58

Changing component from coercion to symbolics.


---

Comment by cwitty created at 2010-08-03 00:22:33

Pure Python implements int() of a float as truncating toward zero:

```
>>> int(3.14159)
3
>>> int(-3.14159)
-3
>>> int(2.71828)
2
>>> int(-2.71828)
-2
```

I think in general we've implemented int() on real numbers of various types as truncating toward zero to follow this precedent.


---

Comment by tornaria created at 2010-08-03 01:31:03

Something like this may work:

```
def SR_int(x):
    """
    sage: SR_int(sin(2)*100)
    90
    sage: SR_int(-sin(2)*100)
    -90
    sage: SR_int(log(8)/log(2))
    3
    sage: SR_int(-log(8)/log(2))
    -3
    sage: SR_int(SR(3^64)) == 3^64
    True
    sage: SR_int(SR(10^100)) == 10^100
    True
    sage: SR_int(SR(10^100+10^-100)) == 10^100
    True
    sage: SR_int(SR(10^100-10^-100)) == 10^100 - 1
    True

    sage: SR_int(sqrt(-1))
    ...
    ValueError: math domain error
    sage: SR_int(x)
    ...
    ValueError: math domain error
    """
    try:
        if x in RR:
            ## truncate toward zero
            y = floor(abs(x))
            if parent(y) is ZZ:
                return int(ZZ(sign(x) * y))
    except:
        pass
    raise ValueError, "math domain error"
```


Note that `floor(log(8)/log(2))` takes about 1s to complete, which means `SR_int(log(8)/log(2))` is waaay slower than `int(log(8)/log(2)`. But this is at the cost of `int(x)` being incorrect when `x` is very close to an integer (cf. `int(SR(10<sup>20-10</sup>-20))`).

OTOH, `(log(8)/log(2)).full_simplify()` takes 35ms to give `3`, so it may be worth revisiting the `floor()` strategy. Opens a can of worms, I guess...

----

I won't turn the snippet above into a patch, if somebody likes it and wants to produce a patch, go ahead.


---

Comment by burcin created at 2012-05-22 22:41:54

Changing status from needs_work to positive_review.


---

Comment by burcin created at 2012-05-22 22:41:54

#12968 has a patch with a positive review which fixes this. We should close this as a duplicate.


---

Comment by jdemeyer created at 2012-06-19 13:29:25

Resolution: duplicate
