# Issue 1122: error in libsingular -> givaro conversion for finite extension fields

Issue created by migration from https://trac.sagemath.org/ticket/1122

Original creator: malb

Original creation time: 2007-11-07 16:29:10

Assignee: malb


```
  Attached is a file with odd behavior.

       p = a prime
       n = a postive integer
       q = p^n
       K = GF(q)

      f = x^3 + y^3 + z^3

      points(f) -- returns list of poitns of f(x,y,z) == 0

      The above works with p = 5, n = 2.  But points
   crashes with p = 5, n = 3.  The error message is attached.
I also did this:

for i in range(0,1953125):
....:     bar.append(K.random_element)
....:
sage: len(bar)
1953125

Thus I don't think SAGE ran out of memory.

I am using SAGE 2.8.7 on a macbook pro, OS 10.5

Best regards,

Jim





<type 'exceptions.IndexError'>            Traceback (most recent call
last)

/Volumes/jxxcarlson/_jc/_current/sage/<ipython console> in <module>()

/Volumes/jxxcarlson/_jc/_current/sage/xgalois.py in points(f)
     17     for yy in K:
     18       for zz in K:
---> 19         if f(xx,yy,zz) == Integer(0):
     20           pts.append([xx,yy,zz])
     21   return pts

/Volumes/jxxcarlson/_jc/_current/sage/finite_field_givaro.pyx in
finite_field_givaro.FiniteField_givaroElement.__richcmp__()

/Volumes/jxxcarlson/_jc/_current/sage/element.pyx in
element.Element._richcmp()

/Volumes/jxxcarlson/_jc/_current/sage/element.pyx in
element.Element._richcmp_()

/Volumes/jxxcarlson/_jc/_current/sage/element.pyx in
element.Element._richcmp()

/Volumes/jxxcarlson/_jc/_current/sage/element.pyx in
element.Element._richcmp_c_impl()

/Volumes/jxxcarlson/_jc/_current/sage/finite_field_givaro.pyx in
finite_field_givaro.FiniteField_givaroElement._cmp_c_impl()

/Volumes/jxxcarlson/_jc/_current/sage/finite_field_givaro.pyx in
finite_field_givaro.FiniteField_givaro.log_to_int()

<type 'exceptions.IndexError'>: n=126 must be < self.order()
```



```

p = 5
n = 2
q = p^n
K.<a> = GF(q)

R.<x,y,z> = PolynomialRing(K,3)

f = x^3 + y^3 + z^3

def points(f):
  pts = [ ]
  for xx in K:
    for yy in K:
      for zz in K:
        if f(xx,yy,zz) == 0:
          pts.append([xx,yy,zz])
  return pts

frob = lambda pt: map( lambda x: x^p, pt)
```



---

Comment by malb created at 2007-11-07 16:30:38

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2007-11-20 15:35:13

Looks good; I guess the problem was overflow.


---

Comment by mabshoff created at 2007-11-20 15:50:54

Resolution: fixed


---

Comment by mabshoff created at 2007-11-20 15:50:54

Merged in 2.8.13.rc1.
