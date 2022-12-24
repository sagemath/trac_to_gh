# Issue 2578: bug in bernoulli_polynomial

archive/issues_002578.json:
```json
{
    "body": "Assignee: was\n\nCC:  mhansen\n\n\nI wanted to verify that Sage could symbolically compute the derivative\nof Bn(x), the nth Bernoulli polynomial in (x): Dx[Bn(x)]=n*Bn-1(x).\nThe following code causes Sage to lockup:\n\n```\nBn = bernoulli_polynomial(x,n)\n```\n\n\nThe command \"bernpoly(x,n)\" in Maxima does not lock up but Maxima\nwill not compute symbolically.\n\n\n```\nsage: B3 = bernoulli_polynomial(x,3)\nsage: B4 = bernoulli_polynomial(x,4)\nsage: DxB4 = diff(B4,x)\nsage: print expand(DxB4-4*B3)\n                                      0\nsage: Bn = bernoulli_polynomial(x,n)\nTraceback (most recent call last):\n...\nKeyboardInterrupt\n>>>\n>>>\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2578\n\n",
    "created_at": "2008-03-17T23:29:04Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "bug in bernoulli_polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2578",
    "user": "was"
}
```
Assignee: was

CC:  mhansen


I wanted to verify that Sage could symbolically compute the derivative
of Bn(x), the nth Bernoulli polynomial in (x): Dx[Bn(x)]=n*Bn-1(x).
The following code causes Sage to lockup:

```
Bn = bernoulli_polynomial(x,n)
```


The command "bernpoly(x,n)" in Maxima does not lock up but Maxima
will not compute symbolically.


```
sage: B3 = bernoulli_polynomial(x,3)
sage: B4 = bernoulli_polynomial(x,4)
sage: DxB4 = diff(B4,x)
sage: print expand(DxB4-4*B3)
                                      0
sage: Bn = bernoulli_polynomial(x,n)
Traceback (most recent call last):
...
KeyboardInterrupt
>>>
>>>
```



Issue created by migration from https://trac.sagemath.org/ticket/2578





---

archive/issue_comments_017631.json:
```json
{
    "body": "I forgot to define (n) as a variable in the above session.\nNow, Sage does not lockup but instead gives the traceback.\n\n\n```\nvar('y,x,n')\ny = bernoulli_polynomial(x,n)\n\nException (click to the left for traceback):\n...\nNameError: name 'bernpoly' is not defined\n\nTraceback (most recent call last):\n File \"<stdin>\", line 1, in <module>\n File \"/home/server2/sage_notebook/worksheets/5463/24/code/18.py\",\nline 7, in <module>\n   y = bernoulli_polynomial(x,n)\n File \"/usr/local/sage/local/lib/python2.5/site-packages/sympy/\nplotting/\", line 1, in <module>\n\n File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/\ncombinat/combinat.py\", line 1806, in bernoulli_polynomial\n   return sage_eval(maxima.eval(\"bernpoly(x,%s)\"%n), {'x':x})\n File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/misc/\nsage_eval.py\", line 110, in sage_eval\n   return eval(p, sage.all.__dict__, locals)\n File \"<string>\", line 1, in <module>\nNameError: name 'bernpoly' is not defined\n```\n",
    "created_at": "2008-03-17T23:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2578#issuecomment-17631",
    "user": "was"
}
```

I forgot to define (n) as a variable in the above session.
Now, Sage does not lockup but instead gives the traceback.


```
var('y,x,n')
y = bernoulli_polynomial(x,n)

Exception (click to the left for traceback):
...
NameError: name 'bernpoly' is not defined

Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/home/server2/sage_notebook/worksheets/5463/24/code/18.py",
line 7, in <module>
   y = bernoulli_polynomial(x,n)
 File "/usr/local/sage/local/lib/python2.5/site-packages/sympy/
plotting/", line 1, in <module>

 File "/usr/local/sage/local/lib/python2.5/site-packages/sage/
combinat/combinat.py", line 1806, in bernoulli_polynomial
   return sage_eval(maxima.eval("bernpoly(x,%s)"%n), {'x':x})
 File "/usr/local/sage/local/lib/python2.5/site-packages/sage/misc/
sage_eval.py", line 110, in sage_eval
   return eval(p, sage.all.__dict__, locals)
 File "<string>", line 1, in <module>
NameError: name 'bernpoly' is not defined
```




---

archive/issue_comments_017632.json:
```json
{
    "body": "Since combinat.py is involved I am CCind Mike Hansen :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T09:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2578#issuecomment-17632",
    "user": "mabshoff"
}
```

Since combinat.py is involved I am CCind Mike Hansen :)

Cheers,

Michael



---

archive/issue_comments_017633.json:
```json
{
    "body": "Oh, and definitely not invalid.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T09:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2578#issuecomment-17633",
    "user": "mabshoff"
}
```

Oh, and definitely not invalid.

Cheers,

Michael



---

archive/issue_comments_017634.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2009-01-23T09:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2578#issuecomment-17634",
    "user": "craigcitro"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_017635.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T09:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2578#issuecomment-17635",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017636.json:
```json
{
    "body": "The attached patch rewrites `bernoulli_polynomial` to avoid Maxima completely. This gives roughly a factor of 10 speedup.\n\nUnfortunately, the originial request doesn't quite make sense -- `bernoulli_polynomial(x,n)` for `n` a symbolic variable would have to return a polynomial of variable degree. As it stands, we don't have any sort of \"symbolic sum\" to use for that kind of thing. I did add the formula for the `n`th Bernoulli polynomial to the docstring, though.",
    "created_at": "2009-01-23T09:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2578#issuecomment-17636",
    "user": "craigcitro"
}
```

The attached patch rewrites `bernoulli_polynomial` to avoid Maxima completely. This gives roughly a factor of 10 speedup.

Unfortunately, the originial request doesn't quite make sense -- `bernoulli_polynomial(x,n)` for `n` a symbolic variable would have to return a polynomial of variable degree. As it stands, we don't have any sort of "symbolic sum" to use for that kind of thing. I did add the formula for the `n`th Bernoulli polynomial to the docstring, though.



---

archive/issue_comments_017637.json:
```json
{
    "body": "Attachment [trac-2578.patch](tarball://root/attachments/some-uuid/ticket2578/trac-2578.patch) by was created at 2009-01-23 10:34:38\n\npositive review;\n\nit could be optimized by using horner's rule",
    "created_at": "2009-01-23T10:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2578#issuecomment-17637",
    "user": "was"
}
```

Attachment [trac-2578.patch](tarball://root/attachments/some-uuid/ticket2578/trac-2578.patch) by was created at 2009-01-23 10:34:38

positive review;

it could be optimized by using horner's rule



---

archive/issue_comments_017638.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T10:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2578#issuecomment-17638",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_017639.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T10:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2578#issuecomment-17639",
    "user": "mabshoff"
}
```

Resolution: fixed
