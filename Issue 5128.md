# Issue 5128: matplotlib Graphics() wrapper

Issue created by migration from https://trac.sagemath.org/ticket/5128

Original creator: jason

Original creation time: 2009-01-29 11:56:58

Assignee: was

CC:  niles

This provides an easy way to make a matplotlib image and combine it with other Graphics() objects:


```
class Matplotlib_Primitive(GraphicPrimitive):
    """
    Primitive class that initializes the
    matrix_plot graphics type 
    """
    def __init__(self, artist, options=None):
        self.artist = artist
        GraphicPrimitive.__init__(self, options)        

    def get_minmax_data(self):
        """
        Returns a dictionary with the bounding box data.
                
        EXAMPLES:
            sage: m = matrix_plot(matrix([[1,3,5,1],[2,4,5,6],[1,3,5,7]]))[0]
            sage: list(sorted(m.get_minmax_data().items()))
            [('xmax', 4), ('xmin', 0), ('ymax', 3), ('ymin', 0)]

        """
        return dict(zip(['xmin', 'xmax', 'ymax', 'ymin'], self.artist.get_extent()))

    def _allowed_options(self):
        return {}

    def _repr_(self):
        return "MatrixPlot defined by a %s x %s data grid"%(self.xy_array_row, self.xy_array_col)

    def _render_on_subplot(self, subplot):
        subplot.add_artist(self.artist)

def matplotlib_plot(mat):
    from sage.plot.plot import Graphics
    g = Graphics()
    g.add_primitive(Matplotlib_Primitive(mat))
    return g
```


Example use:


```
A=random_matrix(RDF,100)
A.numpy()
import pylab
import numpy
B=A.numpy().astype(float)
im = pylab.imshow(B/numpy.max(B),  origin='upper',alpha=0.6)
matplotlib_plot(im)+polygon([[0,10],[10,0],[20,40]])
```



This just needs to be put in a file in the plot/ directory and an entry added to all.py.


---

Comment by jason created at 2009-01-29 11:57:23

And the documentation should be updated, of course.


---

Comment by jason created at 2009-02-05 22:01:01

Something doesn't work in the above patch.  I need to figure out how to get the extents of any matplotlib image passed in.  Is there an easy way to that information?


---

Attachment


---

Comment by jason created at 2009-02-24 09:48:40

This makes things a little better, but not much.  Currently, you can add an axes object.  Note that the doctests involving hist are wrong.


---

Comment by kcrisman created at 2009-09-17 15:09:39

What still needs to be done on this?  It would be really good to get this functionality in now that #5448 is merged, so that other tickets could use it.  Am I correct that currently there is no way to create a Sage graphics object from a mpl one - the process is one direction only?


---

Comment by jason created at 2009-09-17 16:50:24

Replying to [comment:4 kcrisman]:
> What still needs to be done on this?  It would be really good to get this functionality in now that #5448 is merged, so that other tickets could use it.  Am I correct that currently there is no way to create a Sage graphics object from a mpl one - the process is one direction only?

That's correct.  This ticket is the other direction.


---

Attachment

apply instead of previous patch.


---

Comment by jason created at 2009-09-17 19:10:37

apply instead of previous patches


---

Attachment

I've attached another iteration.  I've also posted to the matplotlib users mailing list about the problems in the above patch.


---

Comment by jason created at 2009-09-26 03:22:16

The matplotlib thread is here: http://thread.gmane.org/gmane.comp.python.matplotlib.general/19547

It sounds like we'll probably have to wait until someone (one of us??) volunteers to help on the matplotlib side.


---

Comment by ddrake created at 2010-11-19 03:07:16

On [sage-support](https://groups.google.com/group/sage-support/browse_thread/thread/376720116dd0506e), Karl-Dieter asked me to comment about an issue this ticket might solve. That thread concerns using SageTeX to plot matplotlib graphics -- if this ticket does indeed allow one to easily convert mpl objects to Sage graphics objects, then yes, it will solve the problem in that thread. 

(Note, though, that I think I described a much more general solution there -- albeit one that will require some setup code every time you want to use it.)


---

Comment by niles created at 2011-01-18 18:00:31

cc me!


---

Comment by niles created at 2011-01-18 18:00:31

Changing keywords from "" to "matplotlib, Graphics".


---

Comment by niles created at 2011-01-18 18:16:58

This is related to #10656, which asks for functionality to convert a `GraphicsArray()` object to a `Graphics()` object.

By the way, is this ticket still waiting for something to happen with matplotlib, or is it in working order?


---

Comment by jason created at 2011-01-18 18:32:01

As far as I know, we're stalled waiting for something to happen to matplotlib first.


---

Comment by kcrisman created at 2021-07-23 13:26:05

> The matplotlib thread is here: http://thread.gmane.org/gmane.comp.python.matplotlib.general/19547
This server is not only down, the replacement news.gmane.io is not exactly obvious how to access this one any more.  I _think_ that this is the discussion in question: https://discourse.matplotlib.org/t/saving-images-using-pure-matplotlib-in-sage-cuts-off-the-bottom-part-and-produces-corrupt-file/12286/7 or possibly https://discourse.matplotlib.org/t/saving-an-axes-to-draw-in-a-different-figure/12185

See also https://groups.google.com/g/sage-support/c/N2cgEW3QUG4 for a SageTeX point of view.

> It sounds like we'll probably have to wait until someone (one of us??) volunteers to help on the matplotlib side.
I wonder what the current state of the art is.
