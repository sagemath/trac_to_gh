# Issue 1122: error in libsingular -> givaro conversion for finite extension fields

archive/issues_001122.json:
```json
{
    "body": "Assignee: @malb\n\n\n```\n  Attached is a file with odd behavior.\n\n       p = a prime\n       n = a postive integer\n       q = p^n\n       K = GF(q)\n\n      f = x^3 + y^3 + z^3\n\n      points(f) -- returns list of poitns of f(x,y,z) == 0\n\n      The above works with p = 5, n = 2.  But points\n   crashes with p = 5, n = 3.  The error message is attached.\nI also did this:\n\nfor i in range(0,1953125):\n....:     bar.append(K.random_element)\n....:\nsage: len(bar)\n1953125\n\nThus I don't think SAGE ran out of memory.\n\nI am using SAGE 2.8.7 on a macbook pro, OS 10.5\n\nBest regards,\n\nJim\n\n\n\n\n\n<type 'exceptions.IndexError'>            Traceback (most recent call\nlast)\n\n/Volumes/jxxcarlson/_jc/_current/sage/<ipython console> in <module>()\n\n/Volumes/jxxcarlson/_jc/_current/sage/xgalois.py in points(f)\n     17     for yy in K:\n     18       for zz in K:\n---> 19         if f(xx,yy,zz) == Integer(0):\n     20           pts.append([xx,yy,zz])\n     21   return pts\n\n/Volumes/jxxcarlson/_jc/_current/sage/finite_field_givaro.pyx in\nfinite_field_givaro.FiniteField_givaroElement.__richcmp__()\n\n/Volumes/jxxcarlson/_jc/_current/sage/element.pyx in\nelement.Element._richcmp()\n\n/Volumes/jxxcarlson/_jc/_current/sage/element.pyx in\nelement.Element._richcmp_()\n\n/Volumes/jxxcarlson/_jc/_current/sage/element.pyx in\nelement.Element._richcmp()\n\n/Volumes/jxxcarlson/_jc/_current/sage/element.pyx in\nelement.Element._richcmp_c_impl()\n\n/Volumes/jxxcarlson/_jc/_current/sage/finite_field_givaro.pyx in\nfinite_field_givaro.FiniteField_givaroElement._cmp_c_impl()\n\n/Volumes/jxxcarlson/_jc/_current/sage/finite_field_givaro.pyx in\nfinite_field_givaro.FiniteField_givaro.log_to_int()\n\n<type 'exceptions.IndexError'>: n=126 must be < self.order()\n```\n\n\n\n```\n\np = 5\nn = 2\nq = p^n\nK.<a> = GF(q)\n\nR.<x,y,z> = PolynomialRing(K,3)\n\nf = x^3 + y^3 + z^3\n\ndef points(f):\n  pts = [ ]\n  for xx in K:\n    for yy in K:\n      for zz in K:\n        if f(xx,yy,zz) == 0:\n          pts.append([xx,yy,zz])\n  return pts\n\nfrob = lambda pt: map( lambda x: x^p, pt)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1122\n\n",
    "created_at": "2007-11-07T16:29:10Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "error in libsingular -> givaro conversion for finite extension fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1122",
    "user": "https://github.com/malb"
}
```
Assignee: @malb


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


Issue created by migration from https://trac.sagemath.org/ticket/1122





---

archive/issue_comments_006761.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-07T16:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1122#issuecomment-6761",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006762.json:
```json
{
    "body": "Attachment [libsinggiv.patch](tarball://root/attachments/some-uuid/ticket1122/libsinggiv.patch) by @malb created at 2007-11-07 16:30:38",
    "created_at": "2007-11-07T16:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1122#issuecomment-6762",
    "user": "https://github.com/malb"
}
```

Attachment [libsinggiv.patch](tarball://root/attachments/some-uuid/ticket1122/libsinggiv.patch) by @malb created at 2007-11-07 16:30:38



---

archive/issue_comments_006763.json:
```json
{
    "body": "Looks good; I guess the problem was overflow.",
    "created_at": "2007-11-20T15:35:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1122#issuecomment-6763",
    "user": "https://github.com/williamstein"
}
```

Looks good; I guess the problem was overflow.



---

archive/issue_comments_006764.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-20T15:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1122#issuecomment-6764",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006765.json:
```json
{
    "body": "Merged in 2.8.13.rc1.",
    "created_at": "2007-11-20T15:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1122#issuecomment-6765",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.13.rc1.
