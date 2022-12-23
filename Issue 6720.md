# Issue 6720: make it easy to use sage from matlab

Issue created by migration from https://trac.sagemath.org/ticket/6720

Original creator: was

Original creation time: 2009-08-09 21:04:16

Assignee: was

From Josh Kantor

```
It was easier to work on a matlab python bridge just writing pure python C/api code.  I have a file matpy.c in my home directory on sage.math.
On sage.math if you start matlab and do

>> mex -g -I/usr/local/sage/local/include/python2.5 matpy.c /usr/lib/libpython2.5.so.1

Then you can do

>> matemb(pythonfilename, pythonfunc, v1,v2,...,vn)

The function pythonfunc in pythonfilename will be called with arguments v1,v2,..,v_n which are matlab matrices or vectors, converted to python lists of lists.


Before starting matlab you may need to do

export PYTHONPATH= <current directory path>

to make sure it sees files in the current directory.

Currently it doesn't process return values and of course its just a prototype.

                                                                                   Josh Kantor
```


Including at an example or something based on the above could be very useful for some people.


---

Comment by jkantor created at 2009-08-12 18:56:22

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

Comment by jdemeyer created at 2015-06-23 13:49:26

Changing component from interfaces to interfaces: optional.
