# Issue 9531: spkg-check for gsl does not cause an exit on errors.

Issue created by migration from https://trac.sagemath.org/ticket/9531

Original creator: drkirkby

Original creation time: 2010-07-17 16:39:59

Assignee: drkirkby

The `spkg-check` file for [GNU Scientific Library (GSL)](http://www.gnu.org/software/gsl/) consists of:


```/usr/bin/env bash

cd src

make check

if [ $? -ne 0 ]; then
   echo "Error: make check for GSL failed"
fi
```


so the Sage build does not exit if `make check` fails. This is in contrast to virtually all other `spkg-check` files, where they would have:


```
make check

if [ $? -ne 0 ]; then
   echo "Error: make check for GSL failed"
   exit 1
fi

```


The version of GSL in Sage happens to be almost 3 years old too. 

Dave 


---

Comment by drkirkby created at 2010-07-18 22:16:33

I've created #9533 to update the version of GSL and to fix the spkg-check issues at the same time. When #9533 is merged, this ticket can be closed.


---

Comment by mpatel created at 2010-08-15 02:03:03

I'm closing this as a "duplicate" of #9533.


---

Comment by mpatel created at 2010-08-15 02:03:03

Resolution: duplicate
