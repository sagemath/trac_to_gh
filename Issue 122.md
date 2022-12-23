# Issue 122: some minor issues with some build procedures in packages (noted by Mike Rubinstein)

Issue created by migration from https://trac.sagemath.org/ticket/122

Original creator: was

Original creation time: 2006-10-09 08:13:29

Assignee: was


```
Hi william. Here are the two funny things I noticed
on Friday:
 
In sage-1.4/spkg/build/mpfr-20060930/spkg-install
 
there are a couple of options given to ./configure that are specific to
NTL and don't seem to have anything to do with mpfr, namely:
 
NTL_GMP_LIP=on NTL_STD_CXX=on
 
-------------------------------------------
In sage-1.4/spkg/build/gmp-4.2.1/spkg-install
 
I'm not sure what the --build=none-apple-darwin option is good for.
I got gmp to compile fine on my PowerBook G4 without it.
You have:
 
           # I learned this from
           # http://www.mail-archive.com/clamav-users@lists.clamav.net/msg22183.html
           #  -- William Stein, 2006-04-06
           # It's perhaps weird that this is needed on the powerpc, but it is...
           SAGE_CONF_OPTS="--build=none-apple-darwin --enable-shared --disable-static"
```



---

Comment by was created at 2006-10-15 18:48:49

Resolution: fixed
