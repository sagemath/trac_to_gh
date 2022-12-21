# Issue 4146: rgbcolor bug bites pdfs, casting to int solves it

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-09-18 19:50:34

Assignee: was

Keywords: pdf, save, graphics, text, rgbcolor

Colored text breaks pdf saves.  PNG saves and show() work fine.  

It seems to be fixed by forcing the rgbcolor into ints, i.e. rgbcolor = (int(1),int(0),int(0)) works fine.

Here's an example:

```
t1 = text('Hi, this is a bug',(1,1), rgbcolor = (1,0,0))
t1.save(DATA+'bugplot.pdf')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/mh/sagetest-notebook/worksheets/admin/73/code/7.py", line 6, in <module>
    t1.save(DATA+\u0027bugplot.pdf\u0027)
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1605, in save
    canvas.print_figure(filename, dpi=dpi)
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/matplotlib/backend_bases.py", line 1310, in print_figure
    **kwargs)
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/matplotlib/backend_bases.py", line 1204, in print_pdf
    return pdf.print_pdf(*args, **kwargs)
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/matplotlib/backends/backend_pdf.py", line 1864, in print_pdf
    self.figure.draw(renderer)
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/matplotlib/figure.py", line 759, in draw
    for a in self.axes: a.draw(renderer)
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/matplotlib/axes.py", line 1523, in draw
    a.draw(renderer)
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/matplotlib/text.py", line 329, in draw
    ismath=self.is_math_text(line))
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/matplotlib/backends/backend_pdf.py", line 1428, in draw_text
    self.check_gc(gc, gc._rgb)
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/matplotlib/backends/backend_pdf.py", line 1191, in check_gc
    if delta: self.file.output(*delta)
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/matplotlib/backends/backend_pdf.py", line 451, in output
    self.write(fill(map(pdfRepr, data)))
  File "/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/matplotlib/backends/backend_pdf.py", line 182, in pdfRepr
    % type(obj)
TypeError: Don't know a PDF representation for <type 'sage.rings.integer.Integer'> objects.
```



---

Comment by shumow created at 2009-01-23 10:28:32

William suggested that this probably got fixed in matplotlib as pdf rendering got more mature/stable/done and/or less experimental.


---

Comment by shumow created at 2009-01-23 10:28:32

Resolution: worksforme
