# Issue 3568: optimize sage startup -- don't import twisted.web2 until needed

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-06 19:54:38

Assignee: boothby

BEFORE

```
teragon-2:databases was$ sage -startuptime |grep -i web2
           twisted.web2: 0.106 (twist)
            twisted.python: 0.004 (twisted.web2)
            twisted._version: 0.001 (twisted.web2)
            twisted.web2._version: 0.000 (twisted.web2)
            cgi: 0.004 (twisted.web2)
            twisted.internet: 0.011 (twisted.web2)
            twisted.persisted: 0.001 (twisted.web2)
            zope.interface.adapter: 0.001 (twisted.web2)
            calendar: 0.002 (twisted.web2)
            twisted.internet.defer: 0.000 (twisted.web2)
            twisted.internet.interfaces: 0.000 (twisted.web2)
             twisted.web2.stream: 0.000 (OpenSSL)
             twisted.web2.filter.range: 0.001 (OpenSSL)
             twisted.web2.responsecode: 0.000 (OpenSSL)
             twisted.web2.channel.cgi: 0.001 (OpenSSL)
             twisted.web2.channel.scgi: 0.000 (OpenSSL)
              twisted.web2.channel: 0.000 (twisted.web2.channel.scgi)
             twisted.web2.channel.http: 0.002 (OpenSSL)
             twisted.web2.channel.fastcgi: 0.000 (OpenSSL)
0.106 twisted.web2 (twist)
```


This is on os x with disk caching.




---

Comment by was created at 2008-07-06 20:08:09

AFTER (also, apply #3560):


```
teragon-2:notebook was$ sage -startuptime |grep web2
teragon-2:notebook was$ 
```


And if you apply #3560 maybe something like this:

```
teragon-2:notebook was$ sage -startuptime |grep notebook
      notebook.all: 0.005 (sage.server.all)
       notebook_object: 0.003 (notebook.all)
        run_notebook: 0.002 (notebook_object)
         getpass: 0.001 (run_notebook)
       sagetex: 0.000 (notebook.all)
       interact: 0.002 (notebook.all)
```



---

Attachment


---

Comment by mhansen created at 2008-07-06 20:13:40

+1


---

Comment by was created at 2008-07-06 21:23:35

This got a positive review (see above).

Actually this breaks all the new doctests in worksheet.py that assume that that server.notebook
has been imported.  The fix will be to write a function that imports sage.server.notebook and
makes a sample notebook; this will be even cleaner actually. I'll attach this soon.


---

Attachment


---

Attachment


---

Comment by ncalexan created at 2008-08-10 21:35:00

I had some doctest problems with 3.0.6, due to not importing a module, that are now fixed.

Apply only `3568-was-notebook-startup-and-test-object.patch`}.

All credit to was.


---

Comment by mabshoff created at 2008-08-11 04:17:49

For some reason this patch causes massive doctest failures:

```
        sage -t -long devel/sage/sage/server/notebook/cell.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/real_double.pyx # 0 doctests failed
        sage -t -long devel/sage/sage/misc/session.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/weight_space.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/type_reducible.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/type_dual.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/type_G.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/type_F.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/type_E.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/type_A.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/root_space.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/ambient_space.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/dynkin_diagram.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/root_system.py # 3 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/cartan_type.py # 2 doctests failed
        sage -t -long devel/sage/sage/combinat/crystals/tensor_product.py # 4 doctests failed
        sage -t -long devel/sage/sage/combinat/crystals/spins.py # 2 doctests failed
        sage -t -long devel/sage/sage/combinat/crystals/letters.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/weyl_group.py # 2 doctests failed
        sage -t -long devel/sage/sage/combinat/root_system/weyl_characters.py # 4 doctests failed
```


Cheers,

Michael


---

Comment by mhansen created at 2009-01-19 22:31:07

Resolution: duplicate


---

Comment by mhansen created at 2009-01-19 22:31:07

This is a dupe of #4671 which has been merged.
