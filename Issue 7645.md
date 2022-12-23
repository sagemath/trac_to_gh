# Issue 7645: 'set -e' used inappropriately in python-2.6.2.p4

Issue created by migration from https://trac.sagemath.org/ticket/7645

Original creator: drkirkby

Original creation time: 2009-12-10 00:17:47

Assignee: GeorgSWeber

CC:  was mhansen

The following is one more example of where trying to build Sage on an uncommon platform (HP-UX) discovers bugs which affect *all* platforms. This is yet one more justification of why it is desirable to POSIX compatible portable code and check Sage on many platforms.  

As you can see below, python does not build on my HP C3600 running HP-UX 11i, but we have no clue whatsoever why. Normally Sage would give some clue, but here there is none. 

```
python-2.6.2.p4/src/Tools/world/README
python-2.6.2.p4/src/Tools/world/world
Finished extraction
****************************************************
Host system
uname -a:
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.3.3.tar.gz/gcc-4.3.3/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.3.3 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.3.3 (GCC) 
****************************************************

real	0m0.111s
user	0m0.050s
sys	0m0.040s
sage: An error occurred while installing python-2.6.2.p4
```


The reason no error message is generated, is due to the inappropriate use of 


```
set -e
```


in the spkg-install script. The package python-2.6.2.p4 has in spkg-install


```
# This tells Bash to exit the script if any statement returns 
# a non-true value.
set -e

# PATCH

cp patches/ctypes__init__.py src/Lib/ctypes/__init__.py
if [ $? -ne 0 ]; then
    echo "Error copying patched ctypes"
    exit 1
fi

cp patches/locale.py src/Lib/
if [ $? -ne 0 ]; then
    echo "Error copying patched locale.py"
    exit 1
fi

```


It should be noted that 'set -e' causes any failure to result in the script exiting *immediately* with a non-zero exit code. Since the script has exited, no further processing takes place - even the code which checks for an error! 

I've cc'ed the ticket to Mike and William, as they are listed as package maintainers. 


Dave 


---

Comment by jdemeyer created at 2013-05-19 13:05:58

Old version, no longer relevant.


---

Comment by jdemeyer created at 2013-05-19 13:05:58

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-19 13:06:03

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-21 07:24:31

Resolution: invalid
