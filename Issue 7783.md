# Issue 7783: 3d graphics (viewed with jmol) do not work from the command line on OS X 10.6 sage-4.3

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-29 06:28:44

Assignee: was


```
sage: sphere()
```


doesn't work.  The same from the Sage notebook works fine. 


---

Comment by was created at 2009-12-29 07:30:40

Actually, all command line 3d graphics are broken in sage-4.3.   I just tried on one of the linux binaries and found this too:


```
wstein`@`ubuntu910-64:/tmp/wstein/farm/sage-4.3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: !sage-native-execute local/bin/jmol
Jmol.jar not found
```

| Sage Version 4.3, Release Date: 2009-12-24                         |
| Type notebook() for the GUI, and license() for information.        |
This is yet more fallout from changing the sagenb to use setuptools instead of distutils. The problem is that the jmol script says this:
{{{#!/bin/sh
JMOL_HOME="$SAGE_LOCAL/lib/python/site-packages/sagenb/data/jmol"
...
```


However, look at site-packages now:

```
...
sagenb-0.4.8-py2.6.egg
...
```


Doing this makes the problem disappear:

```
$  cd sage-4.3/local/lib/python/site-packages
$  ln -s sagenb-0.4.8-py2.6.egg/sagenb .
```



---

Comment by was created at 2009-12-29 07:30:55

Changing priority from critical to blocker.


---

Comment by was created at 2009-12-29 07:55:24

Changing status from new to needs_review.


---

Attachment

Apply this patch alone to the sagenb repo. Updates scripts to use pkg_resources to look for sagenb.


---

Attachment

Apply this patch alone to the sage scripts repo. Adds a script that uses pkg_resources to find the location of a given package.


---

Comment by timdumol created at 2009-12-29 08:43:00

Unfortunately the solution in sagenb_7783.patch does not play well with `setup.py develop`. Any changes made to the packages in that mode will not be propagated. These two new patches use `pkg_resources` to find the location of the sagenb package.


---

Comment by was created at 2009-12-29 09:13:49

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-29 09:13:49

Your solution is better in the long run.  

Positive review. 

**IMPORTANT NOTE TO Release MANAGER**

Apply trac_7783-sage-scripts.patch then 

```
chmod +x local/bin/sage-pypkg-location 
```


!!

I have applied trac_7783-sagenb-scripts.patch to the official sagenb repo and merged it into sagenb-0.4.9.


---

Comment by mhansen created at 2010-01-03 20:44:33

Resolution: fixed
