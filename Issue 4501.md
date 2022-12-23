# Issue 4501: preparser does not know about python notation for complex numbers

archive/issues_004501.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: 1j\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     Integer(1)j\n               ^\nSyntaxError: invalid syntax\n```\n\n\nbut in python:\n\n\n```\nsage: preparser(False)\nsage: 1j\n1j\nsage: type(1j)\n<type 'complex'>\n```\n\n\nNote that this does work now:\n\n\n```\nsage: 1rj\n1j\nsage: 1rj == complex('j')\nTrue\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4501\n\n",
    "created_at": "2008-11-12T16:57:58Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "preparser does not know about python notation for complex numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4501",
    "user": "jason"
}
```
Assignee: somebody


```
sage: 1j
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(1)j
               ^
SyntaxError: invalid syntax
```


but in python:


```
sage: preparser(False)
sage: 1j
1j
sage: type(1j)
<type 'complex'>
```


Note that this does work now:


```
sage: 1rj
1j
sage: 1rj == complex('j')
True
```




Issue created by migration from https://trac.sagemath.org/ticket/4501





---

archive/issue_comments_033335.json:
```json
{
    "body": "According to [http://docs.python.org/reference/lexical_analysis.html#id7](http://docs.python.org/reference/lexical_analysis.html#id7), python supports imaginary numbers being declared as:\n\nimagnumber ::=  (floatnumber | intpart) (\"j\" | \"J\")",
    "created_at": "2008-11-12T17:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33335",
    "user": "jason"
}
```

According to [http://docs.python.org/reference/lexical_analysis.html#id7](http://docs.python.org/reference/lexical_analysis.html#id7), python supports imaginary numbers being declared as:

imagnumber ::=  (floatnumber | intpart) ("j" | "J")



---

archive/issue_comments_033336.json:
```json
{
    "body": "\n```\n[10:57] <mhansen> jason-: I don't have time to make a patch now, but the following two lines around line 805 in sage/misc/preparser.py are the correct fix if we want 1j to return a <type 'complex'>:\n[10:57] <mhansen>                 elif i < len(line) and line[i] == 'j':\n[10:57] <mhansen>                     pass\n[10:57] <jason-> I can make a quick patch\n[10:57] <jason-> It needs to support \"J\"\n[10:57] <jason-> and also work for floating numbers too\n[10:58] <jason-> and then there's the issue of if we want to construct Sage complex numbers instead of python complex numbers\n```\n",
    "created_at": "2008-11-12T17:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33336",
    "user": "jason"
}
```


```
[10:57] <mhansen> jason-: I don't have time to make a patch now, but the following two lines around line 805 in sage/misc/preparser.py are the correct fix if we want 1j to return a <type 'complex'>:
[10:57] <mhansen>                 elif i < len(line) and line[i] == 'j':
[10:57] <mhansen>                     pass
[10:57] <jason-> I can make a quick patch
[10:57] <jason-> It needs to support "J"
[10:57] <jason-> and also work for floating numbers too
[10:58] <jason-> and then there's the issue of if we want to construct Sage complex numbers instead of python complex numbers
```




---

archive/issue_comments_033337.json:
```json
{
    "body": "and the next line:\n\n\n```\n[10:58] <mhansen> Just change == \"j\" to in 'jJ'\n```\n",
    "created_at": "2008-11-12T17:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33337",
    "user": "jason"
}
```

and the next line:


```
[10:58] <mhansen> Just change == "j" to in 'jJ'
```




---

archive/issue_comments_033338.json:
```json
{
    "body": "I think 1j should be a Sage complex number.",
    "created_at": "2008-11-12T18:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33338",
    "user": "robertwb"
}
```

I think 1j should be a Sage complex number.



---

archive/issue_comments_033339.json:
```json
{
    "body": "> I think 1j should be a Sage complex number. \n\nAnd I think it should return a Python complex number. :-)",
    "created_at": "2008-11-13T01:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33339",
    "user": "was"
}
```

> I think 1j should be a Sage complex number. 

And I think it should return a Python complex number. :-)



---

archive/issue_comments_033340.json:
```json
{
    "body": "Your reasoning (that the userbase for this feature is almost entirely numeric users) has convinced me.",
    "created_at": "2008-11-13T02:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33340",
    "user": "robertwb"
}
```

Your reasoning (that the userbase for this feature is almost entirely numeric users) has convinced me.



---

archive/issue_comments_033341.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-24T11:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33341",
    "user": "robertwb"
}
```

Resolution: duplicate



---

archive/issue_comments_033342.json:
```json
{
    "body": "See #5079",
    "created_at": "2009-01-24T11:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33342",
    "user": "robertwb"
}
```

See #5079
