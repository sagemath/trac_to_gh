# Issue 954: Make sure compiler is C99 capable

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-21 03:43:10

Assignee: mabshoff

Keywords: gcc, flint, C99

Flint requires C99 capable compilers. gcc 3.4.x and later are, but gcc 3.3 and earlier are not. There are still a number of those older compilers around, so error out early right away with an understandable error message to avoid bug reports with flint compiling to fail.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-21 03:43:23

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-28 11:56:07

At least for gcc we can probably use

```
gcc -dumpversion
```


Cheers,

Michael


---

Comment by was created at 2007-11-03 22:35:41

This can't be written using python, so...
maybe in perl?


---

Comment by jkantor created at 2007-11-04 01:18:38

perl script to test gcc version


---

Attachment

I wrote a perl script to test if gcc version is greater than or equal to 3.4.0. 
It exits 0 if this is the case and 1 otherwise. 

The flint spkg-install should be easily modified to run this script and test the exit code and
take appropriate action. I didn't know what the desired behavior was so I didn't do this yet.


---

Comment by jkantor created at 2007-11-04 01:34:05

More specifically adding this to the top of the flint spkg-install should be enough


```
./test_gcc_version.pl
if [ $? -ne 0 ]; then
   echo "GCC version less than 3.4.0"
   echo "Flint will not be able to compile successfully"
   exit 1
fi
```



---

Comment by rlm created at 2007-12-20 21:32:01

Merged in 1.9.1 alpha2


---

Comment by rlm created at 2007-12-20 21:32:01

Resolution: fixed


---

Comment by rlm created at 2007-12-20 21:32:26

rather 2.9.1 alpha2...
