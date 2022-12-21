# Issue 5049: show(mathematica('2/3')) doesn't work

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-21 12:07:18

Assignee: was

If you do

```
show(mathematica('2/3'))
```


in the notebook, you get no output.  Since latex(mathematica(...)) works great, this is stupid. 


---

Comment by mhansen created at 2009-01-21 18:40:25

This is because the show method is written to deal only with images:


```
    def show(self, filename=None, ImageSize=600):
        """
        Show a mathematica plot in the Sage notebook.

        EXAMPLES:
            sage: P = mathematica('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathematica
            sage: show(P)                                        # optional - mathematica
            sage: P.show(ImageSize=800)                          # optional - mathematica
        """
        P = self._check_valid()
        if filename is None:
            filename = graphics_filename()
        orig_dir = P.eval('Directory[]').strip()
        P.chdir(os.path.abspath("."))
        s = 'Export["%s", %s, ImageSize->%s]'%(filename, self.name(), ImageSize)
        P.eval(s)
        P.chdir(orig_dir)
```



---

Comment by mhansen created at 2009-06-05 01:02:34

This was fixed by #5916.


---

Comment by mhansen created at 2009-06-05 01:02:34

Resolution: fixed
