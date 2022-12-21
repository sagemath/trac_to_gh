# Issue 375: biopython spkg installer hangs in SAGE 2.5.3

Issue created by migration from Trac.

Original creator: Jondice

Original creation time: 2007-05-23 16:00:46

Assignee: was

When installing the biopython-1.43 spkg in SAGE 2.5.3 the installer hangs at:

copying mx/COPYRIGHT -> /usr/local/sage/local/lib/python2.5/site-packages/mx
copying mx/LICENSE -> /usr/local/sage/local/lib/python2.5/site-packages/mx
running install_egg_info
Writing /usr/local/sage/local/lib/python2.5/site-packages/egenix_mx_base-2.0.6-py2.5.egg-info
running install



---

Comment by Jondice created at 2007-05-23 16:02:58

Changing priority from minor to major.


---

Comment by Jondice created at 2007-05-24 02:12:04

Changing priority from major to minor.


---

Comment by Jondice created at 2007-05-24 02:12:04

This seems to be a buffering issue, just pressing enter a few times helps ...


---

Comment by was created at 2007-08-10 20:17:44

It's still important to fix this.


```
>> biopython install:
>>
> This is a known problem.  We are trying to find a hack to get
> around it,
> but nobody has found one yet.  I believe if you just hit return a few
> times when it appears to "hang", then it will contiue fine to the end
> of the build.

Indeed, that works quite nicely. I think I've got everything that is
likely to build on OSX, except for the open question about Axiom.

Many thanks
```



---

Comment by mabshoff created at 2007-11-03 12:04:18

Resolution: fixed


---

Comment by mabshoff created at 2007-11-03 12:04:18

Fixed by William and me when we fixed up the new biopython-1.44.spkg

Cheers,

Michael
