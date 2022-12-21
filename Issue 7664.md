# Issue 7664: Make sure latex doesn't do weird things with R output

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-12-11 20:11:23

Assignee: tbd

CC:  jason iandrus

Keywords: latex, R, jsmath

jsmath doesn't understand output from R, so you have to turn off typesetting for it to work.  E.g., it doesn't know what to do with this table which results from R output - I guess it's really a latex() problem.

```
sage: r.data('Cars93')
[1] "sage0"
sage: a._latex_()

% latex.default(sage3, file = "") 
%
\begin{table}[!tbp]
 \begin{center}
 \begin{tabular}{l}\hline\hline
\multicolumn{1}{c}{}\tabularnewline
\hline
sage0\tabularnewline
\hline
\end{tabular}

\end{center}

\end{table}
```



---

Comment by jason created at 2009-12-11 22:00:43

Can R latex its own expressions?

If not, we might explore the rpy2 interface a bit more to get the data into python formats.

Also, when evaluating in the R system, we ought to enclose things in a div that tells jsmath "Hands off!"


---

Comment by kcrisman created at 2009-12-14 15:50:45

Replying to [comment:2 jason]:
> Can R latex its own expressions?

Apparently using the Hmisc package.  From our own doctests in r.py:

```
    def _latex_(self):
        r"""
        Return LaTeX representation of this R object.

        This calls the \code{latex} command in R.

        OUTPUT:
           a latex expression (basically a string)
        
        EXAMPLES:
            sage: latex(r(2))  #optional requires the Hmisc R package
            2
        """
        self._check_valid()
        P = self.parent()
        # latex is in Hmisc, this is currently not part of Sage's R!!!
        try:
            P.library('Hmisc')
        except ImportError:
            raise RuntimeError, "The R package 'Hmisc' is required for R to LaTeX conversion, but it is not available."
        return LatexExpr(P.eval('latex(%s, file="");'%self.name()))

```


Note that this requires the package 'survival', which is also recommended but not currently in Sage.

Anyway, I checked some more and apparently the problem is that jsmath doesn't understand the latex output created by Hmisc - namely, it doesn't know what a table is, nor center, nor tabular.

So maybe if EMBEDDED_MODE=True, we should have a thing that strips out all that other stuff and just puts in the stuff in the middle.  Incidentally, the output in the optional doctest above is incorrect, we get

```
% latex.default(sage0, file = "") 
%
\begin{table}[!tbp]
 \begin{center}
 \begin{tabular}{r}\hline\hline
\multicolumn{1}{c}{}\tabularnewline
\hline
$2$\tabularnewline
\hline
\end{tabular}

\end{center}

\end{table}

```

so maybe this was with a previous version of Hmisc.

Or we could even strip out those things and replace them with equivalent HTML stuff when EMBEDDED_MODE is true.


---

Comment by kcrisman created at 2011-11-20 01:19:41

Changing keywords from "latex, R, jsmath" to "latex, R, jsmath, r-project".


---

Comment by iandrus created at 2013-08-20 19:10:59

FWIW, this affects sage-mode in Emacs when typesetting output as well.
