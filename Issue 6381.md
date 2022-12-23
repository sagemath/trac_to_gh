# Issue 6381: bug in integral_points when rank is large

Issue created by migration from https://trac.sagemath.org/ticket/6381

Original creator: was

Original creation time: 2009-06-21 22:12:09

Assignee: was

I don't know if this would ever finish, but it probably shouldn't stop with the following error! (this is in sage-4.0.2 on sage.math):

```
wstein@sage:~/build/sage-4.0.2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: D=6611719866; E = EllipticCurve([0,0,0,-D^2,0])
sage: time E.integral_points()
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)
| Sage Version 4.0.2, Release Date: 2009-06-18                       |
| Type notebook() for the GUI, and license() for information.        |
/scratch/wstein/sage/temp/sage.math.washington.edu/21323/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/IPython/iplib.pyc in ipmagic(self, arg_s)
    951         else:
    952             magic_args = self.var_expand(magic_args,1)
--> 953             return fn(magic_args)
    954 
    955     def ipalias(self,arg_s):

/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/IPython/Magic.pyc in magic_time(self, parameter_s)
   1905         if mode=='eval':
   1906             st = clk()
-> 1907             out = eval(code,glob)
   1908             end = clk()
   1909         else:

/scratch/wstein/sage/temp/sage.math.washington.edu/21323/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in integral_points(self, mw_base, both_signs, verbose)
   5801         if disc > 0:
   5802             ##Points in egg have X(P) between e1 and e2 [X(P)=x(P)+b2/12]:
-> 5803             x_int_points = self.integral_x_coords_in_interval((e1-b2_12).ceil(), (e2-b2_12).floor()+1)
   5804             if verbose:
   5805                 print 'x-coords of points on compact component with ',(e1-b2_12).ceil(),'<=x<=',(e2-b2_12).floor()

/scratch/wstein/build/sage-4.0.2/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in integral_x_coords_in_interval(self, xmin, xmax)
   5466         `x`-coordinates of points on this curve.
   5467         """
-> 5468         return set([x for x  in range(xmin,xmax) if self.is_x_coord(x)])
   5469 
   5470     def integral_points(self, mw_base='auto', both_signs=False, verbose=False):

OverflowError: range() result has too many items
```


It might be better to use xrange, or say that the rank is too big, so the computation would never finish or something meaningful.

On 32-bit it fails in the same place but with a _different_ error:

```
...
TypeError: range() integer start argument expected, got sage.rings.integer.Integer.
```



---

Comment by cremona created at 2009-06-22 08:39:53

It should be pretty easy since the rank and gens are found very quickly.  The failure is simply that range() is used to loop over the integers between -D and 0 (to find the integral points on the egg) and D is too big.


---

Comment by cremona created at 2009-06-24 10:31:54

Applies to 4.0.2


---

Attachment

Patch fixes the problem.  I wrote a longer comment but it was lost when I added the patch and I'm not going to type it again!


---

Comment by davidloeffler created at 2009-07-20 20:29:46

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-07-20 20:29:46

Changing assignee from was to davidloeffler.


---

Comment by was created at 2009-07-21 04:33:51

Looks good to me.  Thanks!


---

Comment by mvngu created at 2009-07-22 18:26:33

When using Mercurial queue, one has to be careful about the commit message. I would manually edit the commit message of a patch before uploading it to the trac server. A number of folks who use Mercurial queue upload patches that have nonsensical commit messages.


---

Comment by mvngu created at 2009-07-23 08:02:56

Resolution: fixed


---

Comment by cremona created at 2009-07-23 17:58:28

Replying to [comment:5 mvngu]:
> When using Mercurial queue, one has to be careful about the commit message. I would manually edit the commit message of a patch before uploading it to the trac server. A number of folks who use Mercurial queue upload patches that have nonsensical commit messages.

Very sorry, I am one of these culprits.  I'll try to remember!
