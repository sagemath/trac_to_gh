# Issue 9477: jmol shows a black screen in the notebook, it works fine in the reference manual

Issue created by migration from Trac.

Original creator: olazo

Original creation time: 2010-07-11 22:24:13

Assignee: olazo

Keywords: jmol

I get the following error message in the log of my notebook when I try to show a 3d plot with jmol:


```
script compiler ERROR: se esperaba una instrucción
----line 1 command 1 of /home/admin/0/cells/30/sage0-size500.jmol?1278886612:
          >>>> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"> <<<<
ERROR en guión: script compiler ERROR: se esperaba una instrucción
----line 1 command 1 of /home/admin/0/cells/30/sage0-size500.jmol?1278886612:
          >>>> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"> <<<<
eval ERROR: 
----line 1 command 1:
         script >> "/home/admin/0/cells/30/sage0-size500.jmol?1278886612" <<
```


Jmol loads, and shows a black screen instead of the actual plot.

If I try the exact same plot in the cells in the reference manual, the plot shows perfectly and no error message appears in the log.

This seems to me rather like the opposite to #3167 in which things worked fine in the notebook but not in the help


---

Comment by olazo created at 2010-07-11 22:46:22

It may be important to mention that the following command does not popup a jmol window in the command line:


```
sage: a=point3d([0,0,0])
sage: a.show()
```


But, if I use:


```
sage: a.export_jmol('/home/oscar/point')
```


a zip file containing a SCRIPT file appears there, and I can use:


```
sage: !java -jar /home/cwitty/sage-4.4.4/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol/Jmol.jar}}}

to make jmol open in my desktop, and I can then use it to open the SCRIPT file, and it shows the point just fine.


---

Comment by kcrisman created at 2014-05-28 00:42:45

Oscar, can you verify whether this is still happening for you?   Given how much the notebook has changed in the meantime it might be hard to track this down, and it looks like something akin to #3167 [is back](https://github.com/sagemath/sagenb/issues/179).  I think this would be worth closing unless we have more information.


---

Comment by olazo created at 2014-05-28 01:06:03

Replying to [comment:5 kcrisman]:
> Oscar, can you verify whether this is still happening for you?   Given how much the notebook has changed in the meantime it might be hard to track this down, and it looks like something akin to #3167 [is back](https://github.com/sagemath/sagenb/issues/179).  I think this would be worth closing unless we have more information.

This no longer happens to me. I am currently using sage version 5.0 (though I expect it to be safe to assume that sage 6 won't make the problem come back). If I remember correctly this had to do more with the implementation of java in firefox than with jmol or sage at all. I think I fixed this by using the privative version of the java plugin for firefox. However, icedtea works just fine now that I use a more recent version of it. I suggest this ticket to be closed. Cheers!


---

Comment by kcrisman created at 2014-05-28 15:22:25

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-05-28 15:22:25

Thanks!  Very helpful.


---

Comment by kcrisman created at 2014-05-28 15:22:32

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-05-29 11:08:00

Resolution: fixed
