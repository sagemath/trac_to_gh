# Issue 5400: parser error

archive/issues_005400.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  mvngu\n\nUsing Sage 3.4.alpha0:\n\n\n```\nsage: RDF(e^(1j))\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1419, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1535, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1419, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1419, 0))\n\n(then a TypeError is thrown since I don't have an RDF value)\n\n```\n\n\nNow, of course, the above gives a TypeError, but there still shouldn't be the scary preparser error.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5400\n\n",
    "created_at": "2009-02-28T16:29:19Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "parser error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5400",
    "user": "https://github.com/jasongrout"
}
```
Assignee: cwitty

CC:  mvngu

Using Sage 3.4.alpha0:


```
sage: RDF(e^(1j))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1535, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))

(then a TypeError is thrown since I don't have an RDF value)

```


Now, of course, the above gives a TypeError, but there still shouldn't be the scary preparser error.


Issue created by migration from https://trac.sagemath.org/ticket/5400





---

archive/issue_comments_041614.json:
```json
{
    "body": "Trying this again:\n\n\n```\nsage: RDF(e^(1j))\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1419, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1535, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1419, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1419, 0))\n```\n",
    "created_at": "2009-02-28T16:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41614",
    "user": "https://github.com/jasongrout"
}
```

Trying this again:


```
sage: RDF(e^(1j))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1535, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))
```




---

archive/issue_comments_041615.json:
```json
{
    "body": "Changing assignee from cwitty to @robertwb.",
    "created_at": "2009-02-28T16:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41615",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from cwitty to @robertwb.



---

archive/issue_comments_041616.json:
```json
{
    "body": "Robert, I \"assigned\" you the bug because I don't know an easy way to CC you on the bug report, since you are likely the best person to look at this currently.",
    "created_at": "2009-02-28T16:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41616",
    "user": "https://github.com/jasongrout"
}
```

Robert, I "assigned" you the bug because I don't know an easy way to CC you on the bug report, since you are likely the best person to look at this currently.



---

archive/issue_comments_041617.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> Robert, I \"assigned\" you the bug because I don't know an easy way to CC you on the bug report, since you are likely the best person to look at this currently.\n\nI assume you know about the CC field, so what is the problem? \n\nMany account holders in trac are listed at http://trac.sagemath.org/sage_trac/wiki\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T16:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41617",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 jason]:
> Robert, I "assigned" you the bug because I don't know an easy way to CC you on the bug report, since you are likely the best person to look at this currently.

I assume you know about the CC field, so what is the problem? 

Many account holders in trac are listed at http://trac.sagemath.org/sage_trac/wiki

Cheers,

Michael



---

archive/issue_comments_041618.json:
```json
{
    "body": "The only CC option I have now with the new trac is to add myself.  It's not a text box anymore.",
    "created_at": "2009-02-28T16:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41618",
    "user": "https://github.com/jasongrout"
}
```

The only CC option I have now with the new trac is to add myself.  It's not a text box anymore.



---

archive/issue_comments_041619.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> The only CC option I have now with the new trac is to add myself.  It's not a text box anymore.\n\nOk, this is a permission issue with the new trac since I can CC anybody :) \n\nThis is now #5401.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T16:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41619",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 jason]:
> The only CC option I have now with the new trac is to add myself.  It's not a text box anymore.

Ok, this is a permission issue with the new trac since I can CC anybody :) 

This is now #5401.

Cheers,

Michael



---

archive/issue_comments_041620.json:
```json
{
    "body": "Hmm... this doesn't happen in 3.3. \n\nWhat does `sage: preparse('RDF(e^(1j))')` give you?",
    "created_at": "2009-02-28T22:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41620",
    "user": "https://github.com/robertwb"
}
```

Hmm... this doesn't happen in 3.3. 

What does `sage: preparse('RDF(e^(1j))')` give you?



---

archive/issue_comments_041621.json:
```json
{
    "body": "This is not a preparsing bug. \n\n\n```\nsage: a = sage: a = e^1j; a\n e^(1.0*I)\nsage: RDF(a)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1088, 0))\n...\n```\n",
    "created_at": "2009-02-28T22:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41621",
    "user": "https://github.com/robertwb"
}
```

This is not a preparsing bug. 


```
sage: a = sage: a = e^1j; a
 e^(1.0*I)
sage: RDF(a)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1088, 0))
...
```




---

archive/issue_comments_041622.json:
```json
{
    "body": "Good point with your test.  The tokenizing statement made me think it was the preparser.",
    "created_at": "2009-03-01T03:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41622",
    "user": "https://github.com/jasongrout"
}
```

Good point with your test.  The tokenizing statement made me think it was the preparser.



---

archive/issue_comments_041623.json:
```json
{
    "body": "This gives the correct error now. \n\n\n```\nsage: RDF(e^(1j))\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"parent.pyx\", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)\n  File \"coerce_maps.pyx\", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 5834, in _real_double_\n    return self._convert(field)\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 5718, in _convert\n    return typ(g)\n  File \"parent.pyx\", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)\n  File \"coerce_maps.pyx\", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 5834, in _real_double_\n    return self._convert(field)\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 5712, in _convert\n    fops = [typ(op) for op in self._operands]\n  File \"parent.pyx\", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)\n  File \"coerce_maps.pyx\", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 5834, in _real_double_\n    return self._convert(field)\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 5712, in _convert\n    fops = [typ(op) for op in self._operands]\n  File \"parent.pyx\", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)\n  File \"coerce_maps.pyx\", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 4839, in _real_double_\n    return R(self._obj)\n  File \"parent.pyx\", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)\n  File \"coerce_maps.pyx\", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/functions/constants.py\", line 973, in _real_double_\n    raise TypeError\nTypeError\n\n```\n",
    "created_at": "2009-05-18T21:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41623",
    "user": "https://github.com/robertwb"
}
```

This gives the correct error now. 


```
sage: RDF(e^(1j))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)
  File "coerce_maps.pyx", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5834, in _real_double_
    return self._convert(field)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5718, in _convert
    return typ(g)
  File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)
  File "coerce_maps.pyx", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5834, in _real_double_
    return self._convert(field)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5712, in _convert
    fops = [typ(op) for op in self._operands]
  File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)
  File "coerce_maps.pyx", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5834, in _real_double_
    return self._convert(field)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5712, in _convert
    fops = [typ(op) for op in self._operands]
  File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)
  File "coerce_maps.pyx", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 4839, in _real_double_
    return R(self._obj)
  File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)
  File "coerce_maps.pyx", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/functions/constants.py", line 973, in _real_double_
    raise TypeError
TypeError

```




---

archive/issue_comments_041624.json:
```json
{
    "body": "Right now it gives?:\n\n\n```\nsage: RDF(e^(1j))\n[...]\n/home/timdumol/sage-4.3.1.alpha0/local/lib/python2.6/site-packages/sage/rings/complex_number.so in sage.rings.complex_number.ComplexNumber.__float__ (sage/rings/complex_number.c:7209)()\n\nTypeError: can't convert complex to float; use abs(z)\n```\n\n\nThis seems to be the right error. Should this be closed?",
    "created_at": "2010-01-18T01:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41624",
    "user": "https://github.com/TimDumol"
}
```

Right now it gives?:


```
sage: RDF(e^(1j))
[...]
/home/timdumol/sage-4.3.1.alpha0/local/lib/python2.6/site-packages/sage/rings/complex_number.so in sage.rings.complex_number.ComplexNumber.__float__ (sage/rings/complex_number.c:7209)()

TypeError: can't convert complex to float; use abs(z)
```


This seems to be the right error. Should this be closed?



---

archive/issue_comments_041625.json:
```json
{
    "body": "I hate the fact that \n\n\n```\nsage: RR(CC(-1))\n-1.00000000000000\n```\n\n\nbut\n\n\n```\nsage: RDF(CDF(-1))\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"parent.pyx\", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:5007)\n  File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3109)\n  File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:3000)\n  File \"real_double.pyx\", line 540, in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5553)\n  File \"complex_double.pyx\", line 808, in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:6628)\nTypeError: can't convert complex to float; use abs(z)\n```\n",
    "created_at": "2010-01-18T19:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41625",
    "user": "https://github.com/robertwb"
}
```

I hate the fact that 


```
sage: RR(CC(-1))
-1.00000000000000
```


but


```
sage: RDF(CDF(-1))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:5007)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3109)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:3000)
  File "real_double.pyx", line 540, in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5553)
  File "complex_double.pyx", line 808, in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:6628)
TypeError: can't convert complex to float; use abs(z)
```




---

archive/issue_comments_041626.json:
```json
{
    "body": "Replying to [comment:12 robertwb]:\n> I hate the fact that \n> \n> {{{\n> sage: RR(CC(-1))\n> -1.00000000000000\n> }}}\n> \n> but\n> \n> {{{\n> sage: RDF(CDF(-1))\n> ------------------------------------------------------------\n> Traceback (most recent call last):\n>   File \"<ipython console>\", line 1, in <module>\n>   File \"parent.pyx\", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:5007)\n>   File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3109)\n>   File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:3000)\n>   File \"real_double.pyx\", line 540, in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5553)\n>   File \"complex_double.pyx\", line 808, in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:6628)\n> TypeError: can't convert complex to float; use abs(z)\n> }}}\n\nThat problem should be a different ticket.\n\nThis ticket should be closed.",
    "created_at": "2010-05-04T15:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41626",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:12 robertwb]:
> I hate the fact that 
> 
> {{{
> sage: RR(CC(-1))
> -1.00000000000000
> }}}
> 
> but
> 
> {{{
> sage: RDF(CDF(-1))
> ------------------------------------------------------------
> Traceback (most recent call last):
>   File "<ipython console>", line 1, in <module>
>   File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:5007)
>   File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3109)
>   File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:3000)
>   File "real_double.pyx", line 540, in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5553)
>   File "complex_double.pyx", line 808, in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:6628)
> TypeError: can't convert complex to float; use abs(z)
> }}}

That problem should be a different ticket.

This ticket should be closed.



---

archive/issue_comments_041627.json:
```json
{
    "body": "The CDF float conversion problem is now #8869",
    "created_at": "2010-05-04T15:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41627",
    "user": "https://github.com/jasongrout"
}
```

The CDF float conversion problem is now #8869



---

archive/issue_comments_041628.json:
```json
{
    "body": "The issue for this ticket is fixed.  This ticket should be closed.",
    "created_at": "2010-05-11T20:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41628",
    "user": "https://github.com/jasongrout"
}
```

The issue for this ticket is fixed.  This ticket should be closed.



---

archive/issue_comments_041629.json:
```json
{
    "body": "Close as fixed:\n\n\n```\n[mvngu@sage ~]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: RR(CC(-1))\n-1.00000000000000\nsage: RDF(CDF(-1))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.4.1, Release Date: 2010-05-02                       |\n| Type notebook() for the GUI, and license() for information.        |\n/home/mvngu/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/real_double.so in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5541)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/complex_double.so in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:6510)()\n\nTypeError: can't convert complex to float; use abs(z)\n```\n",
    "created_at": "2010-05-11T21:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed:


```
[mvngu@sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: RR(CC(-1))
-1.00000000000000
sage: RDF(CDF(-1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.4.1, Release Date: 2010-05-02                       |
| Type notebook() for the GUI, and license() for information.        |
/home/mvngu/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/real_double.so in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5541)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/complex_double.so in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:6510)()

TypeError: can't convert complex to float; use abs(z)
```




---

archive/issue_comments_041630.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-11T21:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5400#issuecomment-41630",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_005657.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-11T21:01:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5400",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5400#event-5657"
}
```
