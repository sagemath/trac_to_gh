# Issue 3897: bug in local_information due to the lack of residue_field for ZZ

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2008-08-19 15:19:07

Assignee: was

CC:  alexghitza


```
E = EllipticCurve([1,1])
E.local_information(3)
```


yields


```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/local/pmzcw/prog/sage-3.1.1/<ipython console> in <module>()

/hades/staff/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py in local_information(self, P, proof)
    375         if isinstance(P, RingElement):
    376             P = self.base_ring().ideal(P)
--> 377         return self.integral_model()[0]._tate(P, proof)
    378
    379     def local_minimal_model(self, P, proof = None):

/hades/staff/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py in _tate(self, P, proof)
    517         OK = K.maximal_order()
    518         t = verbose("Running Tate's algorithm with P = %s"%P, level=1)
--> 519         F = OK.residue_field(P)
    520         p = F.characteristic()
    521         if P.is_principal():

AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has no attribute 'residue_field'
```


The problem is that ZZ has no object residue_field, while number rings have. Either one should add this function or write local_information separately for curves over QQ.


---

Comment by cremona created at 2008-09-09 17:41:54

I am fixing this now....


---

Attachment

OK, so the patch 3897-residue-fields-ZZ.patch implements residue fields for ZZ.  ALong the way there were quite a few smallish fixes needed in related things, and while I was immersed in number_field.py etc I added a whole lot of docstrings and doctests there.

This applies to 3.1.2.rc1 AFTER the patches for #1951 which are related (they also relate to residue fields).

After this has been accepted (after revision if necessary, of course!)  then we can start to work on the original problem: I know that local_information() still does not work for curves defined over Q.  

Chris:  I have started going through all the functions for elliptic curve over Q vs. curves over number fields, to make everything as consistent as possible.  These residue field extensions will help.


---

Comment by AlexGhitza created at 2008-09-21 00:22:22

apply after 3897-residue-fields-ZZ.patch


---

Attachment

Looks good.  There were a few typos which are fixed in 3897-minor.patch.


---

Comment by AlexGhitza created at 2008-09-21 00:27:22

Oops!  I take that back.  I noticed that there is no doctest checking if the reported bug was fixed, and running that example still does not work (although in a new way).  I'll see if I can track down what's happening.


---

Comment by cremona created at 2008-09-21 10:41:33

Replying to [comment:6 AlexGhitza]:
> Oops!  I take that back.  I noticed that there is no doctest checking if the reported bug was fixed, and running that example still does not work (although in a new way).  I'll see if I can track down what's happening.

Alex: this patch is intended only to fix the residue field for ZZ issue;  now I have done that I am still working on getting local information to work properly.  So this is really two tickets.

Could we merge and close this one and open a new one for the local info problem?  Or put the ZZ residue fields into a new patch which can be closed right away, with a cross-reference from this one?


---

Comment by cremona created at 2008-09-22 18:00:19

OK, despite my previous remark I have finished and the 3rd patch (to be applied after previous) sorts out the original issue.   More than that:
    * function _tidy_model() was wrong and has been fixed
    * New file ell_local_data.py defines a new class EllipticCurveLocalData which does the work; code moved to here from ell_number_field (especially the _tate() function implementing Tate's algorithm)
    * A few functions added to integer.pyx and rational.pyx so as to allow common code for QQ and other number fields.
    * Now all functions in ell_number_field.py work on curves defined over QQ in a consistent way.
    * Over QQ, new algorithm option "generic" in conductor() uses the generic number field code (slower, but shows consistency).


---

Comment by AlexGhitza created at 2008-09-23 06:58:26

John,

This is good stuff.  Unfortunately, your patch does not contain your new file ell_local_data.py.  I think you probably forgot to add it to the hg repository before exporting your patch.  You should go to devel/sage/sage and do "hg add schemes/elliptic_curves/ell_local_data.py", then refresh your patch 3897-local_data.patch and re-upload it to trac.


---

Attachment

OK, I've done that.  I'm still getting used to the "hg q" way of doing things, which doesn't have a commit stage -- so while I think the patch is correctly identified as due to me, there is not (I think) the usual one-line description.

Enjoy.


---

Comment by AlexGhitza created at 2008-09-23 08:56:49

Positive review.  I added another small patch deprecating local_information (since John's last patch renames it to local_data without any comment).  Apply all the patches in sequence.


For the record: at the moment, writing any function that deals with number fields involves one of the following unpleasant steps 1) write special code to deal with QQ or 2) add functionality to QQ so that it pretends to be a number field.  This leads to code duplication and obfuscation.  Also, whenever a bug is fixed or a feature is added to number fields, one has to remember to do the same with QQ.  Very sad!

Looking at this situation, it feels very much like QQ should inherit from rings.number_field.NumberField_absolute rather than the current rings.number_field_base.NumberField.  This appears to be difficult to do because of circular imports; I've been thinking about the issue and hope to come up with at least some solution that will allow us to truly treat number fields and QQ on an equal footing.


---

Comment by mabshoff created at 2008-09-23 09:48:52

Alex,

the deprecated routine should still call the new function, i.e. a warning is issues, but the code still works.

Cheers,

Michael


---

Attachment

Replying to [comment:12 mabshoff]:
> Alex,
> 
> the deprecated routine should still call the new function, i.e. a warning is issues, but the code still works.
> 
> Cheers,
> 
> Michael

I added a line to do that.  Trac would not let me replace Alex's, but it is a replacement.


---

Comment by mabshoff created at 2008-09-23 10:24:53

Merged all four patches in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-23 10:24:53

Resolution: fixed


---

Comment by was created at 2008-09-23 15:42:58

"Looking at this situation, it feels very much like QQ should inherit from rings.number_field.NumberField?_absolute rather than the current rings.number_field_base.NumberField?. This appears to be difficult to do because of circular imports; I've been thinking about the issue and hope to come up with at least some solution that will allow us to truly treat number fields and QQ on an equal footing. "

The original intention was that any functionality that could be implemented
in a way that is common to both NumberField_absolute and QQ, should
be implemented in rings.number_field.NumberField.  Maybe you should just
move *all* such functionality up there?  If it can't be implemented there,
how will it make sense for QQ?

At least that was how the thinking went a year ago in the original implementation.
This may have turned out to be completely wrong.  Keep at it until you find
the right solution.


---

Comment by cremona created at 2008-09-23 16:01:09

I think William is probably right, but still I'm glad that these patches have been merged before we tried to solve everything!  The one I did implementing residue fields for ZZ was rather similar.  But that's now done!


---

Comment by AlexGhitza created at 2008-09-23 22:37:50

William,

I'm glad you commented on this.  That's exactly the path I had chosen to follow (after discussing it with Craig), so it's good to have confirmation from someone involved in the original design decision.
