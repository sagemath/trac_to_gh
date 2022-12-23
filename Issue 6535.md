# Issue 6535: add environ variables to "sage -pkg" script so don't get OS X metatfiles

Issue created by migration from https://trac.sagemath.org/ticket/6535

Original creator: was

Original creation time: 2009-07-15 06:11:16

Assignee: mabshoff

Many spkg's have tons of `._` files in them since the spkg's were made on OS X.  To fix this we just have to set two environment variables. 


```
Marshall Hampton notes the following:

Helpful post on avoiding this:

http://norman.walsh.name/2008/02/22/tar

...upshot is that one should add

export COPYFILE_DISABLE=true

to your profile if using leopard, or

COPY_EXTENDED_ATTRIBUTES_DISABLE=true

if using tiger or previous stuff (I don't think many sage developers
are using something pre-tiger at this point though).
```



---

Comment by kcrisman created at 2012-06-01 18:44:45

Huh, this is cool!  Although Jeroen and other release managers have been pretty good about marking such spkgs 'needs work' lately, does anyone know if this is still valid?


---

Comment by jdemeyer created at 2013-05-16 07:58:34

Resolution: invalid


---

Comment by jdemeyer created at 2013-05-16 07:58:34

As far as I know, all the instances of `.DS_Store` files currently in Sage actually come from upstream packages. So adding these environment variables wouldn't make a difference.
