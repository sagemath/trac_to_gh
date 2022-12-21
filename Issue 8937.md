# Issue 8937: Implementation of AES with different key sizes

Issue created by migration from Trac.

Original creator: amca01

Original creation time: 2010-05-09 05:00:43

Assignee: mvngu

Keywords: AES

This class implements the full Advanced Encryption Standard, as described in 

http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf 

It includes encryption with a 128 bit plaintext block, and keys of either 128, 196 or 256 bits, which are the only block and key sizes allowed by the standard.  It includes decryption by either the Inverse Cipher method, or the Equivalent Inverse Cipher method.  There are also methods to print out all the intermediate steps in either an encryption or decryption.

The various "layers": mixcolumns, shiftrows, subbytes and their inverses, are available to the user for experimentation.


---

Comment by amca01 created at 2010-05-09 23:17:49

Implementation of AES with different key sizes


---

Comment by amca01 created at 2010-05-11 22:38:14

Changing assignee from mvngu to amca01.


---

Attachment


---

Comment by kini created at 2011-06-12 15:05:33

Changing status from new to needs_info.


---

Comment by kini created at 2011-06-12 15:05:33

On lines 12 and 13 of your file, you say that this is already implemented in Sage. May I ask what the benefit of your code is over the current implementation, then?

By the way, if you would like to contribute code to Sage, please generate a patch file against the Mercurial repository in `$SAGE_ROOT/devel/sage/` . The code should be either added to an existing `.py` or `.pyx` file, or in a new `.py` or `.pyx` file, somewhere in `$SAGE_ROOT/devel/sage`, rather than in a `.sage` file.

I also notice that there is another version of `aes.sage` that you uploaded to the wiki page [TracTickets](TracTickets) (in fact that's how I came across this ticket). Can that one be ignored/deleted? It's older than the one you've uploaded to this ticket.


---

Comment by amca01 created at 2011-06-13 02:06:05

Replying to [comment:2 kini]:
> On lines 12 and 13 of your file, you say that this is already implemented in Sage. May I ask what the benefit of your code is over the current implementation, then?
> 
> By the way, if you would like to contribute code to Sage, please generate a patch file against the Mercurial repository in `$SAGE_ROOT/devel/sage/` . The code should be either added to an existing `.py` or `.pyx` file, or in a new `.py` or `.pyx` file, somewhere in `$SAGE_ROOT/devel/sage`, rather than in a `.sage` file.
> 
> I also notice that there is another version of `aes.sage` that you uploaded to the wiki page [TracTickets](TracTickets) (in fact that's how I came across this ticket). Can that one be ignored/deleted? It's older than the one you've uploaded to this ticket.

The main difference is that AES, as currently implemented in Martin Albrecht's SR class, is that AES is there treated as one of a number of cryptosystems with different parameters.  My implementation is much closer to the ISO standard in design, and allows the user to experiment with all aspects of the AES.
