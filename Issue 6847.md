# Issue 6847: Auto-generate and insert images into the documentation

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-08-30 13:00:09

Assignee: tba

CC:  eviatarbach

Currently, images included in the Sage documentation must be generated separately from the docbuild process itself (cf. #6685).  For the sake of consistency, convenience, testing, etc., we should have an option to automate this process, particularly for the reference manual.

Please see the discussion at #6685.



---

Comment by mpatel created at 2009-08-30 13:35:19

The file [doc/users/transforms_tutorial.rst](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/doc/users/transforms_tutorial.rst?view=markup) from [matplotlib's](http://matplotlib.sourceforge.net/index.html) [trunk](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/) includes:

```
.. plot:: pyplots/annotate_transform.py
```

and

```
.. plot::
   :include-source:

   import numpy as np
   import matplotlib.pyplot as plt

   x = np.arange(0, 10, 0.005)
   y = np.exp(-x/2.) * np.sin(2*np.pi*x)

   fig = plt.figure()
   ax = fig.add_subplot(111)
   ax.plot(x, y)
   ax.set_xlim(0, 10)
   ax.set_ylim(-1, 1)

   plt.show()
```

Possible [output](http://matplotlib.sourceforge.net/users/transforms_tutorial.html).  Elsewhere, I've seen

```
.. plot:: pyplots/tex_demo.py
   :include-source:
```

I think the `:include-[`](../tree/master/`) option includes the formatted source before the image in "place" of a link to the plain-text source.


---

Comment by mpatel created at 2009-08-30 14:40:23

For the `plot` directive's implementation, see [plot_directive.py](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/lib/matplotlib/sphinxext/plot_directive.py?view=markup).

Other goodies:

 * Formatted [examples](http://matplotlib.sourceforge.net/examples/index.html) with code and plots.  See [gen_rst.py](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/doc/sphinxext/gen_rst.py?view=markup).
 * Plot [gallery](http://matplotlib.sourceforge.net/gallery.html).  See [gen_gallery.py](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/doc/sphinxext/gen_gallery.py?view=markup).

To check out the trunk:
 * `svn co http://matplotlib.svn.sourceforge.net/svnroot/matplotlib/trunk/matplotlib/ matplotlib`


---

Comment by chapoton created at 2016-08-08 14:00:48

this is now working


---

Comment by chapoton created at 2016-08-08 14:00:48

Changing status from new to needs_review.


---

Comment by chapoton created at 2016-08-08 14:01:04

Changing status from needs_review to positive_review.


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix
