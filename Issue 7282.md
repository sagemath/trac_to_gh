# Issue 7282: port jinja to install on cygwin

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-25 01:28:02

Assignee: tbd

Right now the jinja spkg segfaults when being installed on cygwin.  


---

Comment by was created at 2009-10-25 01:30:26

NOTE:  I discovered that if I comment out the lines 

```
#from hashlib import sha1
#try:
    #from hashlib import sha1
    #raise ImportError
#except ImportError:
#    from sha import new as sha1
```

in jinja/loaders.py then `python setup.py build` doesn't segfault, though
installing does.  However, I can copy the build/lib*/jinja directory over to 
site-packages by hand and it seems to work.   

Similar remarks apply to Sphinx.


---

Comment by mhansen created at 2009-10-26 07:35:57

We really should try to make sure that there are no problems with hashlib since it's a very common module.


---

Comment by mhansen created at 2009-10-27 15:11:43

The problem occurs somewhere with the optional speedups extension.  We can (temporarily) work around this by doing 


```
python setup.py --without-speedups install
```


on Cygwin.


---

Comment by mhansen created at 2009-10-27 15:19:41

Also, once jinja2 is installed as above, Sphinx installs without a problem.


---

Comment by mhansen created at 2010-02-17 11:28:24

This currently builds fine with Cygwin 1.7


---

Comment by mhansen created at 2010-02-17 11:28:24

Resolution: invalid
