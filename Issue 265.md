# Issue 265: Coercion of maxima float with positive exponent to python float

archive/issues_000265.json:
```json
{
    "body": "Assignee: was\n\nHere is the output:\n\n\nsage: maxima(\"1.7e-17\")\n 1.7E-17\n\nsage: float (_)\n 1.6999999999999999e-17\n\nsage: maxima(\"1.7e+17\")\n 1.7E + 17\n\nsage: float (_)\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/home/greg/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/maxima.py in __float__(self)\n   1267 \n   1268     def __float__(self):\n-> 1269         return float(str(self.numer()))\n   1270 \n   1271     def __len__(self):\n\n<type 'exceptions.ValueError'>: invalid literal for float(): 1.7E + 17\n\nIssue created by migration from https://trac.sagemath.org/ticket/265\n\n",
    "created_at": "2007-02-15T22:39:39Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Coercion of maxima float with positive exponent to python float",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/265",
    "user": "gvanuxem"
}
```
Assignee: was

Here is the output:


sage: maxima("1.7e-17")
 1.7E-17

sage: float (_)
 1.6999999999999999e-17

sage: maxima("1.7e+17")
 1.7E + 17

sage: float (_)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/greg/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/maxima.py in __float__(self)
   1267 
   1268     def __float__(self):
-> 1269         return float(str(self.numer()))
   1270 
   1271     def __len__(self):

<type 'exceptions.ValueError'>: invalid literal for float(): 1.7E + 17

Issue created by migration from https://trac.sagemath.org/ticket/265





---

archive/issue_comments_001250.json:
```json
{
    "body": "Changing component from algebraic geometry to interfaces.",
    "created_at": "2007-02-15T22:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/265#issuecomment-1250",
    "user": "gvanuxem"
}
```

Changing component from algebraic geometry to interfaces.



---

archive/issue_comments_001251.json:
```json
{
    "body": "this works fine in sage-2.8.1.",
    "created_at": "2007-08-18T19:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/265#issuecomment-1251",
    "user": "was"
}
```

this works fine in sage-2.8.1.



---

archive/issue_comments_001252.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T19:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/265#issuecomment-1252",
    "user": "was"
}
```

Resolution: fixed
