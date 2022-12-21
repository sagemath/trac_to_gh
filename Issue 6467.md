# Issue 6467: all primitive roots modulo n

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-07-05 18:11:29

Assignee: was

CC:  kcrisman

Keywords: primitive roots, generators mod n

For a fixed positive integer n, compute a list of all the primitive roots modulo n. Sage currently can compute one primitive root modulo n, but not all of them.


---

Comment by mvngu created at 2009-07-05 18:24:38

The patch `trac_6467.patch` adds two functions to `sage/rings/arith.py` for calculating all the primitive roots modulo a fixed integer n:
 1. `primitive_roots()` --- Return all the generators for the multiplicative group of integers modulo a positive integer n. Where n is a positive composite integer, the function uses a naive method that is inefficient, since I do not know of a better method. If n is a positive prime integer, then use the function `primitive_roots_prime()`.
 1. `primitive_roots_prime()` --- Return all the generators for the multiplicative group of integers modulo a positive prime p. Again, this uses an inefficient method since I'm not aware of a better way.


---

Comment by mvngu created at 2009-07-05 18:36:11

based on Sage 4.1.rc0


---

Attachment

I'm not totally convinced by this. 

- The function `primitive_roots_prime` shouldn't be exported to the global namespace. At present *everything* in sage/rings/arith is exported, which (to me) suggests moving the innards of this function to methods of the IntegerModRing class.

- There is already a method `IntegerRing_class.multiplicative_group_is_cyclic()` which you can use to find out if a primitive root exists -- I fixed a bug in it not long back. Asking for a primitive root and then catching the exception if one isn't found is a bit ugly, besides being much slower.

- For a prime modulus p, you take a primitive root g, then compute g<sup>k</sup> for each k in 1...phi(p). It would be more efficient to have a variable that is initialised to 1 and then multiplied by g (mod p) each time, avoiding the separate power_mod call. 

- The algorithm in the composite case can be *massively* improved using two simple observations: (1) there are no primitive roots mod n unless n is < 8, an odd prime power, or twice an odd prime power; and (2) if n is an odd prime power then g is a primitive root mod p<sup>k</sup> if and only if it's a primitive root mod p (and g is a primitive root mod 2 * p<sup>k</sup> iff g is a primitive root mod p and g is odd).

(At a rough guess your current algorithm is running in time about N^{3/2} times a power of log; this observation will speed it up to N * power of log.)

David


---

Comment by davidloeffler created at 2009-07-14 10:45:36

Oops, by `IntegerRing_class.multiplicative_group_is_cyclic()` I meant `IntegerModRing_generic.multiplicative_group_is_cyclic()`, in `sage.rings.integer_mod_ring`. Sorry.
