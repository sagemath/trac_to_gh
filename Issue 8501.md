# Issue 8501: find_root evaluates by plugging an equation into the function

archive/issues_008501.json:
```json
{
    "body": "Assignee: jkantor\n\nWith 4.3.3:\n\n```\nsage: f1=0.6*x\nsage: f2=0.045*x^2 - 1.44*x + 8.64\nsage: def k(x):\n...       print x\n...       if 5<=x<=8:\n...           return f1(x=x)\n...       elif 8<=x<=13:\n...           return f2(x=x)\n...       else:\n...           raise ValueError, \"Called with impossible value: %s\"%x\n...\nsage: find_root(lambda x:k(x)-55,5,10)\n5.0\n10.0\n6.90983005625\n8.09016994375\n6.1803398875\n6.63093253165711 == 6.68257664471270\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_198.py\", line 9, in <module>\n    exec compile(ur'open(\"___code___.py\",\"w\").write(\"# -*- coding: utf-8 -*-\\n\" + _support_.preparse_worksheet_cell(base64.b64decode(\"ZmluZF9yb290KGxhbWJkYSB4OmsoeCktNTUsNSwxMCk=\"),globals())+\"\\n\"); execfile(os.path.abspath(\"___code___.py\"))' + '\\n', '', 'single')\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmp1LUqkk/___code___.py\", line 3, in <module>\n    exec compile(ur'find_root(lambda x:k(x)-_sage_const_55 ,_sage_const_5 ,_sage_const_10 )' + '\\n', '', 'single')\n  File \"\", line 1, in <module>\n    \n  File \"/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.py\", line 92, in find_root\n    val, s = find_maximum_on_interval(f, a, b)\n  File \"/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.py\", line 122, in find_maximum_on_interval\n    minval, x = find_minimum_on_interval(lambda z: -f(z), a=a, b=b, tol=tol, maxfun=maxfun)\n  File \"/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.py\", line 181, in find_minimum_on_interval\n    xmin, fval, iter, funcalls = scipy.optimize.fminbound(f, a, b, full_output=1, xtol=tol, maxfun=maxfun)\n  File \"/home/grout/sage/local/lib/python2.6/site-packages/scipy/optimize/optimize.py\", line 1256, in fminbound\n    fu = func(x,*args)\n  File \"/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.py\", line 122, in <lambda>\n    minval, x = find_minimum_on_interval(lambda z: -f(z), a=a, b=b, tol=tol, maxfun=maxfun)\n  File \"\", line 1, in <lambda>\n    \n  File \"/tmp/tmpzDC3MH/___code___.py\", line 12, in k\n    raise ValueError, \"Called with impossible value: %s\"%x\nValueError: Called with impossible value: 6.63093253165711 == 6.68257664471270\n```\n\n\nNote that the last evaluation was a symbolic equation, something == something.  That of course breaks the function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8501\n\n",
    "created_at": "2010-03-11T20:56:29Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "find_root evaluates by plugging an equation into the function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8501",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jkantor

With 4.3.3:

```
sage: f1=0.6*x
sage: f2=0.045*x^2 - 1.44*x + 8.64
sage: def k(x):
...       print x
...       if 5<=x<=8:
...           return f1(x=x)
...       elif 8<=x<=13:
...           return f2(x=x)
...       else:
...           raise ValueError, "Called with impossible value: %s"%x
...
sage: find_root(lambda x:k(x)-55,5,10)
5.0
10.0
6.90983005625
8.09016994375
6.1803398875
6.63093253165711 == 6.68257664471270
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_198.py", line 9, in <module>
    exec compile(ur'open("___code___.py","w").write("# -*- coding: utf-8 -*-\n" + _support_.preparse_worksheet_cell(base64.b64decode("ZmluZF9yb290KGxhbWJkYSB4OmsoeCktNTUsNSwxMCk="),globals())+"\n"); execfile(os.path.abspath("___code___.py"))' + '\n', '', 'single')
  File "", line 1, in <module>
    
  File "/tmp/tmp1LUqkk/___code___.py", line 3, in <module>
    exec compile(ur'find_root(lambda x:k(x)-_sage_const_55 ,_sage_const_5 ,_sage_const_10 )' + '\n', '', 'single')
  File "", line 1, in <module>
    
  File "/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.py", line 92, in find_root
    val, s = find_maximum_on_interval(f, a, b)
  File "/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.py", line 122, in find_maximum_on_interval
    minval, x = find_minimum_on_interval(lambda z: -f(z), a=a, b=b, tol=tol, maxfun=maxfun)
  File "/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.py", line 181, in find_minimum_on_interval
    xmin, fval, iter, funcalls = scipy.optimize.fminbound(f, a, b, full_output=1, xtol=tol, maxfun=maxfun)
  File "/home/grout/sage/local/lib/python2.6/site-packages/scipy/optimize/optimize.py", line 1256, in fminbound
    fu = func(x,*args)
  File "/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.py", line 122, in <lambda>
    minval, x = find_minimum_on_interval(lambda z: -f(z), a=a, b=b, tol=tol, maxfun=maxfun)
  File "", line 1, in <lambda>
    
  File "/tmp/tmpzDC3MH/___code___.py", line 12, in k
    raise ValueError, "Called with impossible value: %s"%x
ValueError: Called with impossible value: 6.63093253165711 == 6.68257664471270
```


Note that the last evaluation was a symbolic equation, something == something.  That of course breaks the function.

Issue created by migration from https://trac.sagemath.org/ticket/8501


