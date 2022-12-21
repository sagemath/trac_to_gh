# Issue 4202: latex derivatives of symbolic functions nicely

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-09-26 21:41:59

Assignee: burcin

This patch makes it so that symbolic functions attempt to call maxima to get a latex representation before printing out the default functionname(arguments) notation.


Here is some Sage code that did derivative printing.  I post it here since this code tries to intelligently print partials versus total derivatives, while maxima's seems to only print total derivative "d"s.  If there is interest, we can include this as part of the _latex_ function.

```
        if self._f._name == 'diff':
            if len(self._args[0].variables())==1:
                d_latex = "d"
            else:
                d_latex = "\\partial"

            variables = [(self._args[2*i+1]._latex_(), self._args[2*i+2]) 
                         for i in xrange((len(self._args)-1)/2)]
            variables_latex = ''.join([d_latex+var if power==1 else d_latex+var+"^%r"%power
                                       for var,power in variables])


            order = sum([power for var,power in variables])
            if order == 1:
                order_latex = ""
            else:
                order_latex = "^%r"%order
        
            return "\\frac{%s%s}{%s}(%s)"%(d_latex,
                                              order_latex,
                                              variables_latex,
                                              self._args[0]._latex_())
```




---

Attachment

Nice job.  Looks good to me.


---

Comment by mabshoff created at 2008-09-27 00:53:48

Resolution: fixed


---

Comment by mabshoff created at 2008-09-27 00:53:48

Merged in Sage 3.1.3.alpha2
