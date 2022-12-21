# Issue 9762: Metrology module (a different implementation of the units module)

Issue created by migration from Trac.

Original creator: cousteau

Original creation time: 2010-08-18 18:49:10

Assignee: burcin

CC:  kini

Keywords: units, SI, metrology

This is a module that implements physical units in a more convenient way than the already existing units module: instead of creating separate variables for each unit, it creates an object containing the value, the dimension (mass, length, time...) as a list, and the units as an expression, plus the conversion factor. 

It includes an easy-to-use function to create units from a string, implements `SI` prefixes and has a nice `LaTeX` output.

TO DO: Add more units (there are currently only 74, plus 13 constants), review the documentation and code in case it doesn't follow the Sage style, modify sage/symbolic/all.py to include this module (adding "import metrology" causes Sage to throw exceptions when starting).


---

Attachment

Creates the metrology.py file, but doesn't edit the corresponding all.py


---

Comment by cousteau created at 2010-08-18 19:00:03

The metrology.py file itself, in case it's preferred


---

Attachment

Example of usage, Pi theorem


---

Comment by cousteau created at 2010-08-18 19:02:29

Changing status from new to needs_review.


---

Attachment


---

Comment by burcin created at 2011-05-10 12:20:13

This needs more work as stated in the ticket description and seen by the fact that not all functions included have doctests.

I don't think it makes sense to have 2 different units modules. I suppose the goal here is to replace the existing one at some point. Is the functionality here a clear extension of the existing one? Is there anything that the current module does that this will not be able to do? (I never used the units module.)

Besides the questions of functionality, here are a few things I noticed when I read the patch:

 * The `Units` class should derive from `SageObject`.
 * I don't think introducing a function named `U` to the top level namespace is appropriate. Users which need this functionality so often can define such a shortcut in their initialization file.


---

Comment by burcin created at 2011-05-10 12:20:13

Changing status from needs_review to needs_work.


---

Comment by cousteau created at 2011-05-10 21:41:04

As burcin said, the idea was to have this as a replacement for the current units module, without removing the old one. (Another idea was to call it units2, but that looked kind of ugly)

Making `Units` derive from `SageObject` might be a good idea; however I didn't know much about Sage (nor do I now, actually) so I didn't consider this possibility. Maybe a Units ring could be made too.

The `U()` function was called this way so one could create units conveniently, like

```python
from metrology import U
length = U("1 m")
```

However, it's not necessary to have this function on the top level namespace, and Python guidelines usually suggest something like

```python
import metrology
length = metrology.U("1 m")
```


As for advantages/disadvantages, well, I don't remember them all, but here's a rough list:

### Pros

* Create units from a text string, including multiples and fractions.
* LaTeX representation of units.
* Abstraction of units, as (value, unit !SI value, unit dimmensions), which allows to know the mass-length-time decomposition of the magnitude.
* `0 * 1m = 0 m`, not just `0`. Also, it's possible to convert from 0 degrees Celsius to Fahrenheit, which is impossible with the current `units` module.

### Cons

* `Units` is a class written from scratch, with all operations (`__add__()`, `__mul__()`...) coded explicitly.
* Interoperability with other data types (for example, a matrix of units) might be messy.
* The `units` module has a pretty nice documentation for each unit, not present in this module.
* It's very incomplete, missing a lot of units.


---

Comment by cousteau created at 2011-05-10 21:50:42

(Apparently I forgot the space before each "*", resulting on a bad formatting. Since comments cannot be edited, I'll put the points again here for better readability)

*Pros*

 * Create units from a text string, including multiples and fractions.
 * LaTeX representation of units.
 * Abstraction of units, as (value, unit SI value, unit dimmensions), which allows to know the mass-length-time decomposition of the magnitude.
 * `0 * 1m = 0 m`, not just `0`. Also, it's possible to convert from 0 degrees Celsius to Fahrenheit, which is impossible with the current `units` module.

*Cons*

 * `Units` is a class written from scratch, with all operations (`__add__()`, `__mul__()`...) coded explicitly.
 * Interoperability with other data types (for example, a matrix of units) might be messy.
 * The `units` module has a pretty nice documentation for each unit, not present in this module.
 * It's very incomplete, missing a lot of units.
