# new_exponentation
This program reduces the number of multiplications and achieves the same result by decreasing exponent into half and increasing base exponentially.

Eg: **8 ** 80**

the same result 8 ** 80 can be obtained using

8 ** 80 = 64 ** 40 = 4096 ** 20 ....

so the aim of this program is to sqauring the base, and halving the exponent on next iteration leads to achieve same result by dealing with large base.

Initially 8 ** 80              ----> 80 multiplications required
1st iteration = 64 ** 40       ----> 40 multiplications required
2nd iteration = 4096 ** 20     ----> 20 multiplications required
....


It we stop after 2nd iteration then,

total 2 + 2 + 20 = 24 multiplications required

first 2 is for squaring base each time: 8 * 8 = 64, 64 * 64 = 4096
second 2 is for halving power each time: 80 * (0.5) = 40, 40 * (0.5) = 20

atleast we need to calculate 4096 ** 20 this leads us to do multiply 4096, 20 times.
then here we need 20 multiplications so,

total 24 multiplications required


If we do normaly,

8 ** 80 ==> 80 multiplications
         ||
         ||
       \\\/// reduces to
        \\//
         \/
4096 ** 20  ==> 24 multiplications


This is done just to reduce the costly multiplication operations.
