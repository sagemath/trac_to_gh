# Issue 1891: remove workaround when Pari > 2.3.3 is released

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-01-23 11:25:28

Assignee: craigcitro

To fix trac #1083, I added a workaround due to a bug in Pari. The code is fixed in their svn version, but it's unlikely that we'll see a new release terribly soon. However, when one comes along, someone should go to sage/rings/number_field/number_field.py and undo the following patch:

-        g = self.__rnf.rnfeltabstorel(pari(f))
+        if self.__K.degree() == 1:
+            g = -1*self.__rnf[0][0]*f[1] + f[0]
+        else:
+            g = self.__rnf.rnfeltabstorel(pari(f))

Or, if whoever is updating the pari spkg sends me an email, I'll take care of this.


---

Comment by mpatel created at 2010-02-02 05:12:17

Is this already fixed?  According to

```sh
$ grep rnfeltabstorel `find -name \*.py\*`
./libs/pari/gen.pyx:    def rnfeltabstorel(self, x):
./rings/number_field/number_field_rel.py:        poly_xy = self.pari_rnf().rnfeltabstorel( self(element)._pari_() )
./rings/number_field/maps.py:        g = self.__rnf.rnfeltabstorel(pari(f))
```

But I don't see nearby code similar to that in the description.  However, I'm definitely not an expert.


---

Comment by craigcitro created at 2010-02-02 18:46:53

Well, the workaround is for the case where the degree of the relative number field is one, and it's definitely still present -- several of us fought with that code just a few weeks ago. So I think we still need this ticket.


---

Comment by mpatel created at 2010-02-02 20:58:45

Oops!  I apologize.  Time for me to read a book...


---

Comment by lftabera created at 2010-06-24 15:24:22

Is this still valid?


```
sage: gp.version()
((2, 3, 5), 'GP/PARI CALCULATOR Version 2.3.5 (released)')
```



---

Comment by craigcitro created at 2010-06-25 04:12:15

Resolution: wontfix


---

Comment by craigcitro created at 2010-06-25 04:12:15

Well, I don't think this ticket is valid anymore -- but not because Pari fixed the issue. Does anyone know if this works in Pari unstable (2.4.x)?
