# Issue 2591: too much printing on sage -br

Issue created by migration from https://trac.sagemath.org/ticket/2591

Original creator: craigcitro

Original creation time: 2008-03-19 06:26:07

Assignee: mabshoff

So this happened recently -- maybe with the Debian packaging, though maybe I'm wrong -- and it's annoying. When you do a sage -br, you see the following:


```
running install_scripts
changing mode of /sage/local/bin/changelog to 755
changing mode of /sage/local/bin/check-use-debian.pl to 755
changing mode of /sage/local/bin/compat to 755
changing mode of /sage/local/bin/control to 755
changing mode of /sage/local/bin/control.in to 755
changing mode of /sage/local/bin/dsage_server.py to 755
changing mode of /sage/local/bin/dsage_setup.py to 755
changing mode of /sage/local/bin/dsage_worker.py to 755
changing mode of /sage/local/bin/rules to 755
changing mode of /sage/local/bin/sage to 755
changing mode of /sage/local/bin/sagemath.install to 755
changing mode of /sage/local/bin/spkg-debian-maybe to 755
running install_data
running install_egg_info
Removing /sage/local/lib/python2.5/site-packages/sage-0.0.0-py2.5.egg-info
Writing /sage/local/lib/python2.5/site-packages/sage-0.0.0-py2.5.egg-info
```


What's with all the changing mode stuff? Can we get rid of that? I'm much more concerned with the fact that it *prints* stuff than the fact that it's changing some permissions. 

-cc


---

Comment by mabshoff created at 2008-03-19 07:24:29

This is a dupe of #2262 and is indeed cause by the recent addition of Debian packaging.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-19 07:24:29

Resolution: duplicate
