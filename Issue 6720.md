# Issue 6720: make it easy to use sage from matlab

archive/issues_006720.json:
```json
{
    "body": "Assignee: @williamstein\n\nFrom Josh Kantor\n\n```\nIt was easier to work on a matlab python bridge just writing pure python C/api code.  I have a file matpy.c in my home directory on sage.math.\nOn sage.math if you start matlab and do\n\n>> mex -v -I/usr/local/sage/local/include/python2.5 matpy.c /usr/lib/libpython2.5.so.1\n\nThen you can do\n\n>> matpy(pythonfilename, pythonfunc, v1,v2,...,vn)\n\nThe function pythonfunc in pythonfilename will be called with arguments v1,v2,..,v_n which are matlab matrices or vectors, converted to python lists of lists.\n\n\nBefore starting matlab you may need to do\n\nexport PYTHONPATH= <current directory path>\n\nto make sure it sees files in the current directory.\n\nCurrently it doesn't process return values and of course its just a prototype.\n\n                                                                                   Josh Kantor\n```\n\nIncluding at an example or something based on the above could be very useful for some people.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6720\n\n",
    "created_at": "2009-08-09T21:04:16Z",
    "labels": [
        "component: interfaces: optional"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "make it easy to use sage from matlab",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6720",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

From Josh Kantor

```
It was easier to work on a matlab python bridge just writing pure python C/api code.  I have a file matpy.c in my home directory on sage.math.
On sage.math if you start matlab and do

>> mex -v -I/usr/local/sage/local/include/python2.5 matpy.c /usr/lib/libpython2.5.so.1

Then you can do

>> matpy(pythonfilename, pythonfunc, v1,v2,...,vn)

The function pythonfunc in pythonfilename will be called with arguments v1,v2,..,v_n which are matlab matrices or vectors, converted to python lists of lists.


Before starting matlab you may need to do

export PYTHONPATH= <current directory path>

to make sure it sees files in the current directory.

Currently it doesn't process return values and of course its just a prototype.

                                                                                   Josh Kantor
```

Including at an example or something based on the above could be very useful for some people.

Issue created by migration from https://trac.sagemath.org/ticket/6720





---

archive/issue_comments_055041.json:
```json
{
    "body": "For a toy example of how to use this, consider a file test.py containing \n\n```\ndef random_func(l):\n    f=open(\"log.out\",'w')\n    f.write(str(l))\n    return l\n```\n\nAt your shell execute \n\n```\n$export PYTHONPATH=<path to current directory>\n```\nThen start matlab, then run (I am assuming you have put matpy.c in your current directory also)\n\n```\n>> mex -v -I/usr/local/sage/local/include/python2.5 matpy.c /usr/lib/libpython2.5.so.1\n```\nYou should get two warnings and no errors.\n\nThe first time you do this you may need to do \n\n```\n>> mex -setup\n```\nand choose the option that uses gcc.\n\n\nCreate some matrix and call random_func with it.\n\n```\n>> m=[1 2 3; 4 5 6; 7 8 9];\n>> matpy('test','random_func',m)\n```\nNow random_func should have written the string representation of m as a list of lists to log.out (transposed because matlab stores in fortran order).",
    "created_at": "2009-08-12T18:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6720#issuecomment-55041",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

For a toy example of how to use this, consider a file test.py containing 

```
def random_func(l):
    f=open("log.out",'w')
    f.write(str(l))
    return l
```

At your shell execute 

```
$export PYTHONPATH=<path to current directory>
```
Then start matlab, then run (I am assuming you have put matpy.c in your current directory also)

```
>> mex -v -I/usr/local/sage/local/include/python2.5 matpy.c /usr/lib/libpython2.5.so.1
```
You should get two warnings and no errors.

The first time you do this you may need to do 

```
>> mex -setup
```
and choose the option that uses gcc.


Create some matrix and call random_func with it.

```
>> m=[1 2 3; 4 5 6; 7 8 9];
>> matpy('test','random_func',m)
```
Now random_func should have written the string representation of m as a list of lists to log.out (transposed because matlab stores in fortran order).



---

archive/issue_comments_055042.json:
```json
{
    "body": "Changing component from interfaces to interfaces: optional.",
    "created_at": "2015-06-23T13:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6720#issuecomment-55042",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from interfaces to interfaces: optional.
