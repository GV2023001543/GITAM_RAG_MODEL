## **DIGITAL NOTES ON** 

## **DIGITAL LOGIC DESIGN** 

# **B.TECH II YEAR - I SEM (2018-19)** 

## **DEPARTMENT OF INFORMATION TECHNOLOGY** 

## **MALLA REDDY COLLEGE OF ENGINEERING & TECHNOLOGY (Autonomous Institution – UGC, Govt. of India)** 

(Affiliated to JNTUH, Hyderabad, Approved by AICTE - Accredited by NBA & NAAC – ‘A’ Grade - ISO 9001:2015 Certified) Maisammaguda, Dhulapally (Post Via. Hakimpet), Secunderabad – 500100, Telangana State, INDIA. 

## **MALLA REDDY COLLEGE OF ENGINEERING & TECHNOLOGY** ~~a~~ **DEPARTMENT OF INFORMATION TECHNOLOGY** 

## **(SYLLABUS)** 

## **OBJECTIVES** 

This course provides in-depth knowledge of switching theory and the logic design techniques of digital circuits, which is the basis for design of any digital circuit. The course objectives are: 

- To learn basic techniques for the design of digital circuits and fundamental concepts used in the design of digital systems. 

- To understand common forms of number representation in digital electronic circuits and to be able to convert between different representations. 

- To implement simple logical operations using combinational logic circuits 

- To design combinational logic circuits, sequential logic circuits. 

- To impart to student the concepts of sequential circuits, enabling them to analyze sequential systems in terms of state machines. 

- To implement synchronous state machines using flip-flops. 

## **UNIT -I:** 

## **Number System and Boolean Algebra :** 

Number Systems, Base Conversion Methods, Complements of Numbers, Codes- Binary Codes, Binary Coded Decimal Code and its Properties, Unit Distance Codes, Error Detecting and Correcting Codes. 

Digital Logic Gates(AND,NAND,OR,NOR,EX-OR,EX-NOR), Properties of XOR Gates, Universal Gates, Basic Theorems and Properties, Switching Functions, Canonical and Standard Form. 

## **UNIT -II:** 

## **Minimization Techniques:** 

Introduction, The minimization with theorems, The Karnaugh Map Method, Three, Four and Five variable K- Maps, Prime and Essential Implications, Don’t Care Map Entries, Using the Maps for Simplifying, Quine-McCluskey Method, Multilevel NAND/NOR realizations. 

## **UNIT -III:** 

## **Combinational Circuits:** 

Design Procedure – Half Adder, Full Adder, Half Subtractor, Full Subtractor, Parallel Binary Adder, Parallel binary subtractor, Binary Multiplier, Multiplexers/DeMultiplexers, decoder, Encoder, Code Converters, Magnitude Comparator. 

classification of sequential circuits, The binary cell, The S-R-Latch Flip-Flop The D-Latch Flip-Flop, The “Clocked T” Flip-Flop, The “ Clocked J-K” Flip-Flop, Design of a Clocked Flip-Flop, Timing and Triggering Consideration. 

## **UNIT -IV:** 

## **Sequential Circuits:** 

Introduction, Basic Architectural Distinctions between Combinational and Sequential circuits, Latches,Flip-Flops, SR,JK,D,T and Master slave, characteristic Tables and equations, Conversion from one type of Flip-Flop to another, 

Counters - Design of Single Mode Counter, Ripple Counter, Ring Counter, Shift Register, Ring counter using Shift Register 

## **UNIT -V:** 

## **Memory Devices:** 

Clasification of memories – ROM : ROM organization, PROM, EPROM,EEPROM, RAM: RAM organization, Write operation, Read operation, Static RAM , Programmable Logic Devices: Programmable Logic Array(PLA),Programmable Array Logic, Implementaion of Combinational Logic circuits using ROM,PLA,PAL. 

## **TEXT BOOKS:** 

**1. Digital Design- Morris Mano, PHI, 3rd Edition.** 

**2. Switching Theory and Logic Design-A. Anand Kumar, PHI, 2[nd ] Edition.** 

**3. Switching and Finite Automata Theory- Zvi Kohavi & Niraj K. Jha, 3rd Edition, Cambridge.** 

## **REFERENCE BOOKS:** 

1. Introduction to Switching Theory and Logic Design – Fredriac J. Hill, Gerald R. Peterson, 3rd Ed,John Wiley & Sons Inc. 

2. Digital Fundamentals – A Systems Approach – Thomas L. Floyd, Pearson, 2013. 

3. Switching Theory and Logic Design – Bhanu Bhaskara –Tata McGraw Hill Publication, 2012 

4. Fundamentals of Logic Design- Charles H. Roth, Cengage LEanring, 5th, Edition, 2004. 

5. Digital Logic Applications and Design- John M. Yarbrough, Thomson Publications, 2006. 6. Digital Logic and State Machine Design – Comer, 3rd, Oxford, 2013. 

## **OUTCOMES** 

Upon completion of the course, student should possess the following skills: 

- Be able to manipulate numeric information in different forms 

- Be able to manipulate simple Boolean expressions using the theorems and postulates of Boolean algebra and to minimize combinational functions. 

- Be able to design and analyze small combinational circuits and to use standard combinational functions to build larger more complex circuits. 

- Be able to design and analyze small sequential circuits and to use standard sequential functions to build larger more complex circuits. 

## **MALLA REDDY COLLEGE OF ENGINEERING & TECHNOLOGY** 

## **DEPARTMENT OF INFORMATION TECHNOLOGY** 

## **INDEX** 

|||**INDEX**||
|---|---|---|---|
|**S. No**|**Unit**|**Topic**|**Page no**|
|**1**|**I**|**NUMBERS SYSTEMS AND BOOLEAN ALGEBRA**|**01 **|
|**2**|**II**|**MINIMIZATION TECHNIQUES**|**39**|
|**3**|**III**|**COMBINATIONAL CIRCUITS**|**60**|
|**4**|**IV**|**SEQUENTIAL CIRCUITS**|**89**|
|**5**|**V**|**MEMORY DEVICES**|**119**|



## **MALLA REDDY COLLEGE OF ENGINEERING & TECHNOLOGY** 

## **DEPARTMENT OF INFORMATION TECHNOLOGY** 

## **UNIT - 1** 

## **NUMBER SYSTEMS & BOOLEAN ALGEBRA** 

- Introduction about digital system 

- Philosophy of number systems 

- Complement representation of negative numbers 

- Binary arithmetic 

- Binary codes 

- Error detecting & error correcting codes 

- Hamming codes 

## **INTRODUCTION ABOUT DIGITAL SYSTEM** 

A Digital system is an interconnection of digital modules and it is a system that manipulates discrete elements of information that is represented internally in the binary form. 

Now a day’s digital systems are used in wide variety of industrial and consumer products such as automated industrial machinery, pocket calculators, microprocessors, digital computers, digital watches, TV games and signal processing and so on. 

## **Characteristics of Digital systems** 

- Digital systems manipulate discrete elements of information. 

- Discrete elements are nothing but the digits such as 10 decimal digits or 26 letters of alphabets and so on. 

- Digital systems use physical quantities called signals to represent discrete elements. 

- In digital systems, the signals have two discrete values and are therefore said to be binary. 

- A signal in digital system represents one binary digit called a bit. The bit has a value either 0 or 1. 

Analog systems vs Digital systems 

Analog system process information that varies continuously i.e; they process time varying signals that can take on any values across a continuous range of voltage, current or any physical parameter. 

Digital systems use digital circuits that can process digital signals which can take either 0 or 1 for binary system. 

**==> picture [117 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 0 14 0 14. time<br>**----- End of picture text -----**<br>


Advantages of Digital system over Analog system 

## 1. Ease of programmability 

The digital systems can be used for different applications by simply changing the program without additional changes in hardware. 

## 2. Reduction in cost of hardware 

The cost of hardware gets reduced by use of digital components and this has been possible due to advances in IC technology. With ICs the number of components that can be placed in a given area of Silicon are increased which helps in cost reduction. 

## 3.High speed 

Digital processing of data ensures high speed of operation which is possible due to advances in Digital Signal Processing. 

## 4. High Reliability 

Digital systems are highly reliable one of the reasons for that is use of error correction codes. 

## 5. Design is easy 

The design of digital systems which require use of Boolean algebra and other digital techniques is easier compared to analog designing. 

## 6. Result can be reproduced easily 

Since the output of digital systems unlike analog systems is independent of temperature, noise, humidity and other characteristics of components the reproducibility of results is higher in digital systems than in analog systems. 

## **Disadvantages of Digital Systems** 

- Use more energy than analog circuits to accomplish the same tasks, thus producing more heat as well. 

- Digital circuits are often fragile, in that if a single piece of digital data is lost or misinterpreted the meaning of large blocks of related data can completely change. 

- Digital computer manipulates discrete elements of information by means of a binary code. 

- Quantization error during analog signal sampling. 

## **NUMBER SYSTEM** 

Number system is a basis for counting varies items. Modern computers communicate and operate with binary numbers which use only the digits 0 &1. Basic number system used by humans is Decimal number system. 

For Ex: Let us consider decimal number 18. This number is represented in binary as 10010. 

We observe that binary number system take more digits to represent the decimal number. For large numbers we have to deal with very large binary strings. So this fact gave rise to three new number systems. 

- i) Octal number systems 

- ii) Hexa Decimal number system 

- iii) Binary Coded Decimal number(BCD) system 

To define any number system we have to specify 

- Base of the number system such as 2,8,10 or 16. 

- The base decides the total number of digits available in that number system. 

- First digit in the number system is always zero and last digit in the number system is always base-1. 

## **Binary number system:** 

The binary number has a radix of 2. As r = 2, only two digits are needed, and these are 0 and 1. In binary system weight is expressed as power of 2. 

The left most bit, which has the greatest weight is called the Most Significant Bit (MSB). And the right most bit which has the least weight is called Least Significant Bit (LSB). 

For Ex: **1001.012 = [ ( 1 ) × 2[3] ] + [ ( 0 ) × 2[2] ] + [ ( 0 ) × 2[1] ] + [ ( 1 ) × 2[0] ] + [ ( 0 ) × 2[-1] ] + [ ( 1 ) × 2[2 ] ] 1001.012 = [ 1 × 8 ] + [ 0 × 4 ] + [ 0 × 2 ] + [ 1 × 1 ] + [ 0 × 0.5 ] + [ 1 × 0.25 ] 1001.012 = 9.2510** 

## **Decimal Number system** 

The decimal system has ten symbols: 0,1,2,3,4,5,6,7,8,9. In other words, it has a base of 10. 

## **Octal Number System** 

Digital systems operate only on binary numbers. Since binary numbers are often very long, two shorthand notations, octal and hexadecimal, are used for representing large binary numbers. Octal systems use a base or radix of 8. It uses first eight digits of decimal number system. Thus it has digits from 0 to 7. 

## **Hexa Decimal Number System** 

The hexadecimal numbering system has a base of 16. There are 16 symbols. The decimal digits 0 to 9 are used as the first ten digits as in the decimal system, followed by the letters A, B, C, D, E and F, which represent the values 10, 11,12,13,14 and 15 respectively. 

|**Decima**<br>**l**|**Binar**<br>**y**|**Octal**|**Hexadeci**<br>**mal**|
|---|---|---|---|
|**0**|**0000**|**0**|**0**|
|**1**|**0001**|**1**|**1**|
|**2**|**0010**|**2**|**2**|
|**3**|**0011**|**3**|**3**|
|**4**|**0100**|**4**|**4**|
|**5**|**0101**|**5**|**5**|
|**6**|**0110**|**6**|**6**|
|**7**|**0111**|**7**|**7**|
|**8**|**1000**|**10**|**8**|
|**9**|**1001**|**11**|**9**|
|**10**|**1010**|**12**|**A**|
|**11**|**1011**|**13**|**B**|
|**12**|**1100**|**14**|**C**|
|**13**|**1101**|**15**|**D**|
|**14**|**1110**|**16**|**E**|
|**15**|**1111**|**17**|**F**|



## **Number Base conversions** 

The human beings use decimal number system while computer uses binary number system. Therefore it is necessary to convert decimal number system into its equivalent binary. 

i) Binary to octal number conversion ii) Binary to hexa decimal number conversion 

iii) Octal to binary Conversion 

iv) Hexa to binary conversion 0100 1111 1101 v) Octal to Decimal conversion Ex: convert 4057.068 to octal =4x8[3] +0x8[2] +5x8[1] +7x8[0] +0x8[-1] +6x8[-2] =2048+0+40+7+0+0.0937 

=2095.093710 

vi) Decimal to Octal Conversion 

Ex: convert 378.9310  to octal 

**37810 to octal** : Successive division: 

**==> picture [97 x 106] intentionally omitted <==**

=5728 

0.9310 to octal : 0.93x8=7.44 0.44x8=3.52 ↓ 0.53x8=4.16 0.16x8=1.28 =0.73418 

378.9310=572.73418 vii) Hexadecimal to Decimal Conversion Ex: 5C716 to decimal 

**==> picture [143 x 39] intentionally omitted <==**

=14710 

viii) Decimal to Hexadecimal Conversion Ex: 2598.67510 

**==> picture [89 x 81] intentionally omitted <==**

0.67510=0.675x16 -- 10.8 

= 0.800x16  -- 12.8 ↓ = 0.800x16 -- 12.8 = 0.800x16 -- 12.8 =0.ACCC16 

## 2598.67510 = A26.ACCC16 

## ix) Octal to hexadecimal conversion: 

The simplest way is to first convert the given octal no. to binary & then the binary no. to hexadecimal. 

## Ex: 756.6038 

|7<br>111<br>0001<br>1|5|6|.|6|0|3|
|---|---|---|---|---|---|---|
||101|110|.|110|000|011|
||1110|1110|.|1100|0001|1000|
||E|E|.|C|1|8|



## x) Hexadecimal to octal conversion: 

First convert the given hexadecimal no. to binary & then the binary no. to octal. 

## Ex: B9F.AE16 

|B|9|F|.|A|E|||
|---|---|---|---|---|---|---|---|
|1011|1001|1111|.|1010|1110|||
|101|110|011|111|.|101|011|100|
|5|6|3|7|.|5|3|4|



**=5637.534** 

## **Complements:** 

In digital computers to simplify the subtraction operation & for logical manipulation complements are used. There are two types of complements used in each radix system. 

i) The radix complement or r’s complement ii) The diminished radix complement or (r-1)’s complement 

## **Representation of signed no.s binary arithmetic in computers:** 

- Two ways of rep signed no.s 

   1. Sign Magnitude form 

   2. Complemented form 

- Two complimented forms 

   1. 1‘s compliment form 2. 2‘s compliment form 

Advantage of performing subtraction by the compliment method is reduction in the hardware.( instead of addition & subtraction only adding ckt‘s are needed.) 

- i.e, subtraction is also performed by adders only. 

Instead of subtracting one no. from other the compliment of the subtrahend is added to minuend. In sign magnitude form, an additional bit called the sign bit is placed in front of the no. If the sign bit is 0, the no. is +ve, If it is a 1, the no is _ve. 

**==> picture [326 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
Ex:<br>0  1  0  1  0  0  1<br>↓<br>Sign bit  =+41 magnitude<br>↑<br>1  1  0  1  0  0  1<br>= -41<br>Note: manipulation is necessary to add a +ve no to a –ve no<br>**----- End of picture text -----**<br>


## **Representation of signed no.s using 2’s or 1’s complement method:** 

If the no. is +ve, the magnitude is rep in its true binary form & a sign bit 0 is placed in front of the MSB.I f the no is _ve , the magnitude is rep in its 2‘s or 1‘s compliment form &a sign bit 1 is placed in front of the MSB. 

## Ex: 

|Given no.|Sign magform|2‘s compform|1‘s compform|
|---|---|---|---|
|01101|+13|+13|+13|
|010111|+23|+23|+23|
|10111|-7|-7|-8|
|1101010|-42|-22|-21|



## **Special case in 2’s comp representation:** 

Whenever a signed no. has a 1 in the sign bit & all 0‘s for the magnitude bits, the decimal equivalent is -2[n ] , where n is the no of bits in the magnitude . Ex: 1000= -8 & 10000=-16 

## **Characteristics of 2’s compliment no.s:** 

Properties: 

1. There is one unique zero 

2. 2‘s comp of 0 is 0 

3. The leftmost bit can‘t be used to express a quantity . it is a 0 no. is +ve. 

4. For an n-bit word which includes the sign bit there are (2[n-1] -1) +ve integers, 2[n-1 ] –ve integers & one 0 , for a total of 2[n ] uniquestates. 

5. Significant information is containd in the 1‘s of the +ve no.s & 0‘s of the _ve no.s 

6. A _ve no. may be converted into a +ve no. by finding its 2‘s comp. 

## **Signed binary numbers:** 

|Decimal|Sign 2‘s compform|Sign 1‘s compform|Sign magform|
|---|---|---|---|
|+7|0111|0111|0111|
|+6|0110|0110|0110|
|+5|0101|0101|0101|
|+4|0100|0100|0100|
|+3|0011|0011|0011|
|+2|0010|0010|0010|
|+1|0011|0011|0011|
|+0|0000|0000|0000|



|-0|--|1111|1000|
|---|---|---|---|
|-1|1111|1110|1001|
|-2|1110|1101|1010|
|-3|1101|1100|1011|
|-4|1100|1011|1100|
|-5|1011|1010|1101|
|-6|1010|1001|1110|
|-7|1001|1000|1111|
|8|1000|--|--|



## **Methods of obtaining 2’s comp of a no:** 

- In 3 ways 

   1. By obtaining the 1‘s comp of the given no. (by changing all 0‘s to 1‘s & 1‘s to 0‘s) & then adding 1. 

   2. By subtracting the given n bit no N from 2[n] 

3. Starting  at  the  LSB  ,  copying  down  each  bit  upto & including the first 1 bit encountered , and complimenting the remaining bits. 

Ex: Express -45 in 8 bit 2‘s comp form 

+45 in 8 bit form is 00101101 

**I method** : 1‘s comp of 00101101 & the add 1 00101101 11010010 +1 _ _ _ _ _ _ _ _ _ _ 11010011 is 2‘s comp form **II method:** 

Subtract the given no. N from 2[n ] 2[n ] = 100000000 Subtract 45= -00101101 +1 _ _ _ 11010011 is 2‘s comp **III** method: Original no: 00101101 Copy up to First 1 bit 1 Compliment remaining : 1101001 bits 11010011 

**Ex:** 

-73.75 in 12 bit 2‘compform 

I method 

01001001.1100 10110110.0011 +1 

## 10110110.0100 is 2‘s 

II method: 2[8 ] = 100000000.0000 

Sub 73.75=-01001001.1100 

10110110.0100 is 2‘s comp 

III method : Orginalno :  01001001.1100 Copy up to 1‘st bit 100 Comp the remaining bits: 10110110.0 

10110110.0100 

**2’s compliment Arithmetic:** 

- The 2‘s comp system is used to rep –ve no.s using modulus arithmetic . The word length of a computer is fixed. i.e, if a 4 bit no. is added to another 4 bit no  . the result will be only of 4 bits. Carry if any , from the fourth bit will overflow called the Modulus arithmetic. 

Ex:1100+1111=1011 

- In the 2‘s compl subtraction, add the 2‘s comp of the subtrahend to the minuend . If there is a carry out , ignore it , look at the sign bit  I,e, MSB of the sum term .If  the MSB  is  a 0, the result is positive.& it is in true binary form. If the MSB is a ` ( carry in or no carry at all) the result is negative.& is in its 2‘s comp form. Take its 2‘s comp to find its magnitude in binary. 

**Ex:** Subtract 14 from 46 using 8 bit 2‘s comp arithmetic: 

+14 = 00001110 -14 = 11110010 2‘s comp +46 = 00101110 -14 =+11110010 2‘s comp form of -14 

-32 (1)00100000 ignore carry 

Ignore carry , The MSB is 0 . so the result is +ve. & is in normal binary form. So the result is +00100000=+32. 

**EX:** Add -75 to +26 using 8 bit 2‘s comp arithmetic 

+75 = 01001011 -75 =10110101 2‘s comp +26 = 00011010 2‘s comp form of -75 -75 =+10110101 -49 11001111 No carry 

No carry , MSB is a 1, result is _ve & is in 2‘s comp. The magnitude is 2‘s comp of 11001111. i.e, 00110001 = 49. so result is -49 

**Ex:** add -45.75 to +87.5 using 12 bit arithmetic 

+87.5 = 01010111.1000 

-45.75=+11010010.0100 

-41.75 (1)00101001.1100 ignore carry MSB is 0, result is +ve. =+41.75 

## **1’s compliment of n number:** 

• It is obtained by simply complimenting each bit of the no,.& also , 1‘s comp of a no, is subtracting each bit of the no. form 1.This complemented value rep the – ve of the original no. One of the difficulties of using 1‘s comp is  its rep o f zero. Both 00000000 & its 1‘s comp 11111111 rep zero. 

• The 00000000 called +ve zero& 11111111 called –ve zero. Ex: -99 & -77.25 in 8 bit 1‘s comp +99 = 01100011 -99 = 10011100 

+77.25 = 01001101.0100 -77.25 = 10110010.1011 

## **1’s compliment arithmetic:** 

In 1‘s comp subtraction, add the 1‘s comp of the subtrahend to the minuend. If there is a 

carryout , bring the carry around & add it to the LSB called the **end around carry.** Look at the sign bit (MSB) . If this is a 0, the result is +ve & is in true binary. If the MSB is a 1 ( carry or no carry ), the result is –ve & is in its is comp form .Take its 1‘s comp to get the magnitude inn binary. 

Ex: Subtract 14 from 25 using 8 bit 1‘s EX: ADD -25 to +14 

25 = 00011001 +14 = 00001110 -45 = 11110001 -25 =+11100110 +11 (1)00001010 -11 11110100 

+1 

00001011 

No carry MSB =1 result=-ve=-1110 

MSB is a 0 so result is +ve (binary ) 

=+1110 

## **Binary codes** 

Binary codes are codes which are represented in binary system with modification from the original ones. 

Weighted Binary codes 

Non Weighted Codes 

Weighted binary codes are those which obey the positional weighting principles, each position of the number represents a specific weight. The binary counting sequence is an example. 

## **Reflective Code** 

A code is said to be reflective when code for 9 is complement for the code for 0, and 

so is for 8 and 1 codes, 7 and 2, 6 and 3, 5 and 4. Codes 2421, 5211, and excess-3 are reflective, whereas the 8421 code is not. 

## **Sequential Codes** 

A code is said to be sequential when two subsequent codes, seen as numbers in binary representation, differ by one. This greatly aids mathematical manipulation of data. The 8421 and Excess-3 codes are sequential, whereas the 2421 and 5211 codes are not. 

## **Non weighted codes** 

Non weighted codes are codes that are not positionally weighted. That is, each position within the binary number is not assigned a fixed value. Ex: Excess-3 code 

## **Excess-3 Code** 

Excess-3 is a non weighted code used to express decimal numbers. The code derives its name from the fact that each binary code is the corresponding 8421 code plus 0011(3). 

## **Gray Code** 

The gray code belongs to a class of codes called minimum change codes,  in which only one bit in the code changes when moving from one code to the next. The Gray code is non-weighted code, as the position of bit does not contain any weight. The gray code is a reflective digital code which has the special property that any two subsequent numbers codes differ by only one bit. This is also called a unit- distance code. In digital Gray code has got a special place. 

## **Binary to Gray Conversion** 

Gray Code MSB is binary code MSB. 

- Gray Code MSB-1 is the XOR of binary code MSB and MSB-1. 

- MSB-2 bit of gray code is XOR of MSB-1 and MSB-2 bit of binary code. 

- MSB-N bit of gray code is XOR of MSB-N-1 and MSB-N bit of binary code. 

## **8421 BCD code ( Natural BCD code):** 

Each decimal digit 0 through 9 is coded by a 4 bit binary no. called natural binary codes. Because of the 8,4,2,1 weights attached to it. It is a weighted code & also sequential . it is useful for mathematical operations. The advantage of this code is its case of conversion to & from decimal. It is less efficient than the pure binary, it require more bits. 

Ex: 14→1110 in binary 

## But as 0001 0100 in 8421 ode. 

The disadvantage of the BCD code is that , arithmetic operations are more complex than they are in pure binary . There are 6 illegal combinations 1010,1011,1100,1101,1110,1111 in these codes, they are not part of the 8421 BCD code system . The disadvantage of 8421 code is, the rules of binary addition 8421 no, but only to the individual 4 bit groups. 

## **BCD Addition:** 

It is individually adding the corresponding digits of the decimal no,s expressed in 4 bit binary groups starting from the LSD . If there is no carry & the sum term is not an illegal code , no correction is needed .If there is a carry out of one group to the next group or if the sum term is an illegal code then 610(0100) is added to the sum term of that group & the resulting carry is added to the next group. 

## Ex: Perform decimal additions in 8421 code 

(a)25+13 

In BCD 25= 0010 0101 In BCD +13  =+0001 0011 

38 0011 1000 

No carry , no illegal code .This is the corrected sum 

(b). 679.6 + 536.8 679.6 = 0110 0111 1001 .0110 in BCD +536.8 = +0101 0011 0010 .1000 in BCD _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 1216.4 1011 1010 0110 . 1110 illegal codes +0110 + 0011 +0110 . + 0110 add 0110 to each (1)0001 (1)0000 (1)0101 . (1)0100 propagate carry **/ / / /** +1 +1 +1 +1 0001 0010 0001 0110 . 0100 1 2 1 6 . 4 

## **BCD Subtraction:** 

Performed by subtracting the digits of each 4 bit group of the subtrahend the digits from the corresponding 4- bit group of the minuend in binary starting from the LSD . if there is no borrow from the next group , then 610(0110)is subtracted from the difference term of this group. 

(a)38-15 

In BCD 38= 0011 1000 In BCD -15 = -0001 0101 

23 0010 0011 No borrow, so correct difference. 

.(b) 206.7-147.8 

206.7 = 0010 0000 0110 . 0111 in BCD -147.8 = -0001  0100 0111 . 0110 in BCD _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 58.9 0000 1011 1110 . 1111 borrows are present -0110 -0110 . -0110 subtract 0110 0101 1000 . 1001 

## **BCD Subtraction using 9’s & 10’s compliment methods:** 

Form the 9‘s & 10‘s compliment of the decimal subtrahend & encode that no. in the 8421 code . the resulting BCD no.s are then added. 

EX: 305.5 – 168.8 

305.5  = 305.5 -168.8= +83.1 9‘s comp of -168.8 _ _ (1)136.6 +1 end around carry **136.7** corrected difference 305.510 = 0011 0000 0101 . 0101 +831.110 = +1000 0011 0001 . 0001 9‘s comp of 16 8.8 in BCD _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ +1011 0011 0110 . 0110 1011 is illegal code +0110 add 0110 (1)0001 0011 0110 . 0110 +1 End around carry 0001 0011 0110 . 0111 = 136.7 

## **Excess three(xs-3)code:** 

It is a non-weighted BCD code .Each binary codeword is the corresponding 8421 codeword plus 0011(3).It is a sequential code & therefore , can be used for arithmetic operations..It is a self-complementing code.s o the subtraction by the method of compliment addition is more direct in xs-3 code than that in 8421 code. The xs-3 code has six invalid states 0000,0010,1101,1110,1111.. It has interesting properties when used in addition & subtraction. 

## **Excess-3 Addition:** 

Add the xs-3 no.s by adding the 4 bit groups in each column starting from the LSD. If there is no carry starting from the addition of any of the 4-bit groups , subtract 0011 from the sum term of those groups ( because when 2 decimal digits are added in xs-3 & there is no carry , result in xs-6). If there is a carry out, add 0011 to the sum term of those groups( because when there is a carry, the invalid states are skipped and the result is normal binary). 

**==> picture [397 x 184] intentionally omitted <==**

**----- Start of picture text -----**<br>
EX:  37  0110  1010<br>+28  +0101  1011<br>    _ _  _ _ _ _ _  _ _ _<br>65  1011  (1)0101 carry generated<br>+1  propagate carry<br> _ _ _ _ _ _<br>1100  0101  add 0011 to correct 0101 &<br>-0011  +0011  subtract 0011 to correct 1100<br> _ _ _ _ _ _ _ _<br>1001  1000  =6510<br>**----- End of picture text -----**<br>


**Excess -3 (XS-3) Subtraction:** 

Subtract the xs-3 no.s by subtracting each 4 bit group of the subtrahend from the corresponding 4 bit group of the minuend starting form the LSD .if there is no borrow from the next 4-bit group add 0011 to the difference term of such groups (because when decimal digits are subtracted in xs-3 & there is no borrow , result is normal binary). I f there is a borrow , subtract 0011 from the differenceterm(b coz taking a borrow is equivalent to adding six invalid states , result is in xs-6) 

Ex: 267-175 

267 = 0101 1001 1010 -175= -0100 1010 1000 _ _ _ _ _ _ _ _ 0000 1111 0010 +0011 -0011  +0011 0011   1100 +0011 =9210 

**Xs-3 subtraction using 9’s & 10’s compliment methods:** Subtraction is performed by the 9‘s compliment or 10‘s compliment Ex:687-348 The subtrahend (348) xs -3 code & its compliment are: 

|||||9‘s comp of 348 =|9‘s comp of 348 =|651|651|||
|---|---|---|---|---|---|---|---|---|---|
|||||Xs-3 code of 348 = 0110 0111 1011||||||
|||||1‘s comp of 348 in xs-3 = 1001 1000|||||0100|
|||||Xs=3 code of 348 in xs=3 = 1001 1000 0100||||||
|||687|||687|||||
|||-348||→|+651 9‘s compl of 348|||||
|||339|||(1)338|||||
||||||+1 end around carry|||||
||||||_|||||
||||||339||corrected difference in decimal|||
|||1001|||1011||1010||687 in xs-3|
|||+1001|||1000||0100||1‘s comp 348 in xs-3|
||||_|<br>_ _ _ _ _ _ _||_ _||||
|||_ (1)0010 (1)0011<br>1110 carry generated||||||||
|**⁄⁄**||||||||||
||+1|||+1|||||propagate carry|
|||_ _ _ _|_|_ _ _ _|_ _ _ _ _ _-|||||
||(1)0011|||0010|1110|||||
||||||||+1||end around carry|
|||_ _ _ _|_|_ _ _ _|_ _ _ _ _|||||
|||0011|||0011||1111||(correct 1111 by sub0011 and|
|||+0011|||+0011||+0011||correct both groups of 0011 by|
||||_|_ _|_ _ _ _|_|_   _|adding|0011)|
||||||_ _|||||
|||0110|||0110||1100||corrected diff in xs-3 = 33010|



## **The Gray code (reflective –code):** 

Gray code is a non-weighted code & is not suitable for arithmetic operations. It is not a BCD code . It is a cyclic code because successive code words in this code differ in one  bit position only i.e, it is a unit distance code.Popular of the unit distance code.It is also a reflective code i.e,both reflective & unit distance. The n least significant bits for 2[n ] through 2[n+1] -1 are the mirror images of thosr for 0 through 2[n] -1.An N bit gray code can be obtained by reflecting an N- 1 bit code about an axis at the end of the code, & putting the MSB of 0 above the axis & the MSB of 1 below the axis. 

Reflection of gray codes: 

||||GrayCode|GrayCode|GrayCode||||Decimal||4 bit binary|
|---|---|---|---|---|---|---|---|---|---|---|---|
||1 bit||2 bit||3 bit||4 bit|||||
||0<br>1||00<br>01||000<br>001||0000<br>0001||0<br>1||0000<br>0001|
||||11<br>10||011<br>010||0011<br>0010||2<br>3||0010<br>0011|
||||||110<br>111<br>101||0110<br>0111<br>0101||4<br>5<br>6<br>7||0100<br>0101<br>0110<br>0111|
||||||110||0100|||||
|||||||||||||
|||||||1100<br>1101<br>1111<br>1110<br>1010<br>1011<br>1001<br>1000||8<br>9<br>10<br>11<br>12<br>13<br>14<br>15||1000<br>1001<br>1010<br>1011<br>1100<br>1101<br>1110<br>1111||



Binary codes block diagram 

**Error – Detecting codes:** When binary data is transmitted & processed,it is susceptible to noise that can alter or distort its contents. The 1‘s may get changed to 0‘s & 1‘s .because digital systems must be accurate to the digit, error can pose a problem. Several schemes have been devised to detect the occurrence of a single bit error in a binary word, so that whenever such an error occurs the concerned binary word can be corrected & retransmitted. 

**Parity:** The simplest techniques for detecting errors is that of adding an extra bit known as parity bit to each word being transmitted.Two types of parity **:** Oddparity **,** evenparity forodd parity, the parity bit is set to a ‗0‘ or a ‗1‘ at the transmitter such that the total no. of 1 bit in the word including the parity bit is an odd no.For even parity, the parity bit is set to a ‗0‘ or a ‗1‘ at the transmitter such that the parity bit is an even no. 

|Decimal|8421 code|Oddparity|Evenparity|
|---|---|---|---|
|0|0000|1|0|
|1|0001|0|1|
|2|0010|0|1|
|3|0011|1|0|
|4|0100|0|1|
|5|0100|1|0|
|6|0110|1|0|
|7|0111|0|1|
|8|1000|0|1|
|9|1001|1|0|



When the digit data is received . a parity checking circuit generates an error signal if the total no of 1‘s is even in an odd parity system or odd in an even parity system. This parity check can always detect a single bit error but cannot detect 2 or more errors with in the same word.Odd parity is used more often than even parity does not detect the situation. Where all 0‘s are created by a short ckt or some other fault condition. 

Ex: Even parity scheme 

(a)  10101010  (b)  11110110 (c)10111001 

Ans: 

- (a) No. of 1‘s in the word is even  is 4 so there is no error 

- (b) No. of 1‘s in the word is even  is 6 so there is no error 

- (c) No. of 1‘s in the word is odd is 5 so there is error 

Ex: odd parity 

(a)10110111 (b) 10011010 (c)11101010 

Ans: 

- (a) No. of 1‘s in the word is even is 6 so word has  error 

- (b) No. of 1‘s in the word is even  is 4 so word has error 

- (c) No. of 1‘s in the word is odd is 5 so there is no error 

## **Checksums:** 

Simple parity can‘t detect two errors within the same word. To overcome this, use a sort of 2 dimensional parity. As each word is transmitted, it is added to the sum of the previously transmitted words, and the sum retained at the transmitter end. At the end of transmission, the sum called the check sum. Up to that time sent to the receiver. The receiver can check its sum with the transmitted sum. If the two sums are the same, then no errors were detected at the receiver end. If there is an error, the receiving location can ask for retransmission of the entire data, used in teleprocessing systems. 

## **Block parity:** 

Block of data shown is create the row & column parity bits for the data using odd parity. The parity bit 0 or 1 is added column wise & row wise such that the total no. of 1‘s in each column & row including the data bits & parity bit is odd as 

|Data|Paritybit||data|
|---|---|---|---|
|10110|0||10110|
|10001|1||10001|
|10101|0||10101|
|00010|0||00010|
|11000|1||11000|
|00000|1||00000|
|11010|0||11010|



## **Error –Correcting Codes:** 

A code is said to be an error –correcting code, if the code word can always be deduced from an erroneous word. For a code to be a single bit error correcting code, the  minimum distance of that code must be three. The minimum distance of that code is the smallest no. of bits by which any two code words must differ. A code with minimum distance of 3 can‘t only correct single bit errors but also detect ( can‘t correct) two  bit  errors, The  key to error correction is that it must be possible to detect & locate erroneous that it must be possible to detect & locate erroneous digits. If the location of an error has been determined. Then by complementing the erroneous digit, the message can be corrected , error correcting , code is the Hamming code , In this , to each group of m information or message or data bits, K parity checking bits denoted by P1,P2,----------pk located at positions 2[k-1 ] from left are added to form an (m+k) bit code word. To correct the error, k parity checks are performed on selected digits of each code word, & the position of the error bit is located by forming an error word, & the error bit is then complemented. The k bit error word is generated by putting a 0 or a 1 in the 2[k-1] th position depending upon whether the check for parity involving the parity bit Pk is satisfied or not.Error positions & their corresponding values : 

|Error Position|For 15 bit code<br>C4C3C2C1|For 12 bit code<br>C4C3C2C1|For 7 bit code<br>C3C2C1|
|---|---|---|---|
|0|0 0 0 0|0 0 0 0|0 0 0|
|1|0 0 0 1|0 0 0 1|0 0 1|
|2|0 0 1 0|0 0 1 0|0 1 0|
|3|0 0 1 1|0 0 1 1|0 1 1|
|4|0 1 0 0|0 1 0 0|1 0 0|
|5|0 1 0 1|0 1 0 1|1 0 1|
|6|0   1 1 0|0   1 1 0|1 1 0|
|7|0   1 1 1|0   1 1 1|1 1 1|
|8|1   0   0<br>0|1   0   0<br>0||
|9|1   0 0 1|1   0 0 1||
|10|1   0 1 0|1   0 1 0||
|11|1   0 1 1|1   0 1 1||
|12|1   1 0<br>0|1   1 0<br>0||
|13|1 1 0<br>1|||
|14|1 1 1<br>0|||
|15|1 1<br>1<br>1|||



## **7-bit Hamming code:** 

To transmit four data bits, 3 parity bits located at positions 2[0 ] 21&2[2 ] from left are added to make a 7 bit codeword which is then transmitted. 

The word format 

P1 P2 D3 P4 D5 D6 D7 

D—Data bits P- 

Parity bits 

|Decimal Digit|For BCD<br>P1P2D3P4D5D6D7|For Excess-3<br>P1P2D3P4D5D6D7|
|---|---|---|
|0|0 0   0 0   0  0<br>0|1 0   0 0   0  1<br>1|
|1|1 1   0 1   0  0<br>1|1 0   0 1   1  0<br>0|
|2|0 1   0 1   0  1<br>1|0 1 0   0  1  0<br>1|
|3|1 0   0 0   0  1<br>1|1 1   0 0   1  1 0|
|4|1 0   0 1   1  0<br>0|0 0   0 1   1 1 1|
|5|0 1 0   0  1  0<br>1|1 1   1 0   0 0 0|
|6|1 1   0 0   1  1 0|0 0   1 1   0 0 1|
|7|0 0   0 1   1 1 1|1 0   1 1 0 1 0|
|8|1 1   1 0   0 0 0|0 1   1 0 0<br>1 1|
|9|0 0   1 1   0 0 1|0<br>1   1 1 1 0 0|



Ex: Encode the data bits 1101 into the 7 bit even parity Hamming Code The bit pattern is 

P1P2D3P4D5D6D7 

**==> picture [94 x 10] intentionally omitted <==**

Bits 1,3,5,7 (P1 111) must have even parity, so P1 =1 Bits 2, 3, 6, 7(P2 101) must have even parity, so P2 =0 Bits 4,5,6,7 (P4 101)must have even parity, so P4 =0 The final code is 1010101 

EX: Code word is 1001001 

Bits 1,3,5,7 (C1 1001) →no error →put a 0 in the 1‘s position→C1=0 Bits 2, 3, 6, 7(C2 0001)) → error →put a 1 in the 2‘s position→C2=1 Bits 4,5,6,7 (C4 1001)) →no error →put a 0 in the 4‘s position→C3=0 

**15-bit Hamming Code:** It transmit 11 data bits, 4 parity bits located 2[0 ] 2[1 ] 2[2 ] 2[3] Word format is 

P1 P2 D3 P4 D5 D6 D7 P8 D9 D10 D11 D12 D13 D14 D15 

**12-Bit Hamming Code:** It transmit 8 data bits, 4 parity bits located at position 2[0 ] 2[1 ] 2[2 ] 2[3] Word format is 

P1 P2 D3 P4 D5 D6 D7 P8 D9 D10 D11 D12 

## **Alphanumeric Codes:** 

These codes are used to encode the characteristics of alphabet in addition to the decimal digits. It is used for transmitting data between computers & its I/O device such as printers, keyboards & video display terminals.Popular modern alphanumeric codes are ASCII code & EBCDIC code. 

## **Digital Logic Gates** 

Boolean functions are expressed in terms of AND, OR, and NOT operations, it is easier to implement a Boolean function with these type of gates. 

## **Properties of XOR Gates** 

- XOR (also ) : the “not-equal” function 

- XOR(X,Y) = X  Y = X’Y + XY’ 

- Identities: 

   - X  0 = X 

   - X  1 = X’ 

   - X  X = 0 

**==> picture [66 x 10] intentionally omitted <==**

- Properties: 

   - X  Y = Y  X 

   - (X  Y)  W = X  ( Y  W) 

## **Universal Logic Gates** 

NAND and NOR gates are called Universal gates. All fundamental gates (NOT, AND, OR) can be realized by using either only NAND or only NOR gate. A universal gate provides flexibility and offers enormous advantage to logic designers. 

## **NAND as a Universal Gate** 

NAND Known as a “universal” gate because ANY digital circuit can be implemented with NAND gates alone. 

To prove the above, it suffices to show that AND, OR, and NOT can be implemented using NAND gates only. 

**Boolean Algebra:** In 1854, George Boole developed an algebraic system now called Boolean algebra. In 1938, Claude E. Shannon introduced a two‐valued Boolean algebra called switching algebra that represented the properties of bistable electrical switching circuits. For the formal definition of Boolean algebra, we shall employ the postulates formulated by E. V. Huntington in 1904. 

Boolean algebra is a system of mathematical logic. It is an algebraic system consisting of the set of elements (0, 1), two binary operators called OR, AND, and one unary operator NOT. It is the basic mathematical tool in the analysis and synthesis of switching circuits. It is a way to express logic functions algebraically. 

Boolean algebra, like any other deductive mathematical system, may be defined with aset of elements, a set of operators, and a number of unproved axioms or postulates. A _set_ of elements is anycollection of objects having a common property. If **S** is a set and _**x**_ and _**y**_ are certain objects, then **x** Î **S** denotes that _**x**_ is a member of the set **S** , and _**y**_ Ï **S** denotes that _**y**_ is not an element of **S** . A set with adenumerable number of elements is specified by braces: **A** = {1,2,3,4}, _i.e._ the elements of set **A** are thenumbers 1, 2, 3, and 4. A _binary operator_ defined on a set S of elements is a rule that assigns to each pair ofelements from S a unique element from S._ Example: In _a_ * _b=c_ , we say that * is a binary operator if it specifies a rule for finding _c_ from the pair ( _a_ , _b_ )and also if _a_ , _b_ , _c_ Î S. 

## **Axioms and laws of Boolean algebra** 

Axioms or Postulates of Boolean algebra are a set of logical expressions that we accept without proof and upon which we can build a set of useful theorems. 

||AND Operation|OR Operation|NOT Operation|
|---|---|---|---|
|Axiom1 :|0.0=0|0+0=0|0=1|
|Axiom2:|0.1=0|0+1=1|1=0|
|Axiom3:|1.0=0|1+0=1||
|Axiom4:|1.1=1|1+1=1||



|**AND Law**|**OR Law**|
|---|---|
|Law1: A.0=0 (Null law)|Law1: A+0=A|
|Law2: A.1=A (Identity law)|Law2: A+1=1|
|Law3: A.A=A (Impotence law)|Law3: A+A=A (Impotence law)|



**CLOSURE:** The Boolean system is _closed_ with respect to a binary operator if for every pair of Boolean values,it produces a Boolean result. For example, logical AND is closed in the Boolean system because it accepts only Boolean operands and produces only Boolean results. 

_ A set _S_ is closed with respect to a binary operator if, for every pair of elements of _S_ , the binary operator specifies a rule for obtaining a unique element of _S_ . 

_ For example, the set of natural numbers N = {1, 2, 3, 4, … 9} is closed with respect to the binary operator plus (+) by the rule of arithmetic addition, since for any _a_ , _b_ Î N we obtain a unique _c_ Î N by the operation _a_ + _b_ = c. 

## **ASSOCIATIVE LAW:** 

A binary operator * on a set _S_ is said to be associative whenever ( _x * y_ ) * _z_ = _x_ * ( _y_ * _z_ ) for all _x_ , _y_ , _z_ Î S, forall Boolean values x, y and z. 

## **COMMUTATIVE LAW:** 

A binary operator * on a set _S_ is said to be commutative whenever x _* y_ = _y_ * _x_ for all _x_ , _y_ , _z_ є S 

## **IDENTITY ELEMENT:** 

A set _**S**_ is said to have an identity element with respect to a binary operation * on S if there exists an element _e є_ S with the property _e * x_ = _x_ * _e_ = _x_ for every _x_ є S 

## **BASIC IDENTITIES OF BOOLEAN ALGEBRA** 

- _Postulate 1(Definition)_ : A Boolean algebra is a closed algebraic system containing a set _K_ of two or more 

- elements and the two operators · and + which refer to logical AND and logical OR • _x + 0 = x_ 

- _x_ · _0 = 0_ 

- _x + 1 = 1_ 

- _x_ · _1 = 1_ 

- _x + x = x_ 

- _x · x = x_ 

- _x + x’ = x_ 

- _x · x’ = 0_ 

- _x + y = y + x_ 

- _xy = yx_ 

- _x + ( y + z ) = ( x + y ) + z_ 

- _x (yz) = (xy) z_ 

- _x ( y + z ) = xy + xz_ 

- _x + yz = ( x + y )( x + z)_ 

- _( x + y )’ = x’ y’_ 

- _( xy )’ = x’ + y’_ 

• _(x’)’ = x_ 

## **DeMorgan's Theorem** 

**(a)** ( _a + b_ )' = _a_ ' _b_ ' 

**(b)** ( _ab_ )' = _a_ ' + _b_ ' 

## **Generalized DeMorgan's Theorem** 

(a) ( _a + b + … z_ )' = _a_ ' _b_ ' _… z_ ' 

(b) ( _a.b … z_ )' = _a_ ' _+ b_ ' _+ … z_ ‘ 

## **Basic Theorems and Properties of Boolean algebra Commutative law** 

Law1: A+B=B+A Law2: A.B=B.A **Associative law** Law1: A + (B +C) = (A +B) +C Law2: A(B.C) = (A.B)C **Distributive law** Law1:  A.(B + C) = AB+ AC Law2: A + BC = (A + B).(A +C) 

## **Absorption law** 

Law1: A +AB =A Law2: A(A +B) = A Solution: A(1+B) Solution: A.A+A.B A A+A.B A(1+B) A 

## **Consensus Theorem** 

Theorem1. AB+ A’C + BC = AB + A’C Theorem2. (A+B). (A’+C).(B+C) =(A+B).( A’+C) 

The BC term is called the consensus term and is redundant. The consensus term is formed from a PAIR OF TERMS in which a variable (A) and its complement (A’) are present; the consensus term is formed by multiplying the two terms and leaving out the selected variable and its complement 

## Consensus Theorem1 Proof: 

## AB+A’C+BC=AB+A’C+(A+A’)BC =AB+A’C+ABC+A’BC 

=AB(1+C)+A’C(1+B) 

= AB+ A’C 

## **Principle of Duality** 

Each postulate consists of two expressions statement one expression is transformed into the ⋅ other by interchanging the operations (+) and ( ) as well as the identity elements 0 and 1. Such expressions are known as duals of each other. 

If some equivalence is proved, then its dual is also immediately true. 

If we prove: ( x.x )+(x’+x’)=1, then we have by duality: ( x + x ) ⋅ (x’.x’)=0 

The Huntington postulates were listed in pairs and designated by part (a) and part (b) in below table. 

**Table for Postulates and Theorems of Boolean algebra Part-A Part-B** ~~rs~~ A+0=A A.0=0 ~~rs~~ A+1=1 A.1=A ~~rs~~ A+A=A (Impotence law) A.A=A (Impotence law) A+ A =1 A. A =0 ~~PePo a~~ A =A  (double inversion law) -- **Commutative law:** A+B=B+A A.B=B.A ~~rs~~ **Associative law** : A + (B +C) = (A +B) +C A(B.C) = (A.B)C ~~rs~~ **Distributive law** : A.(B + C) = AB+ AC A + BC = (A + B).(A +C) ~~e~~ **Absorption law** : A +AB =A ~~s~~ A(A +B) = A **DeMorgan Theorem:** ~~ee~~ (A+B) = A[̅   ] . B (A.B) = = A[̅   ] + B **Redundant Literal Rule:** A+ A . B=A+B A.( A A+B)=AB **Consensus Theorem:** AB+ A’C + BC = AB + A’C (A+B). (A’+C).(B+C) =(A+B).( A’+C) ~~Po Re~~ 

## **Boolean Function** 

Boolean algebra is an algebra that deals with binary variables and logic operations. 

A Boolean function described by an algebraic expression consists of binary variables, the constants 0 and 1, and the logic operation symbols. 

For a given value of the binary variables, the function can be equal to either 1 or 0. 

F(vars) = _expression_ 

Set of binary Variables Operators (+, •, ‘) Constants (0, 1) Groupings (parenthesis) Variables Consider an example for the Boolean function 

F1 = x + y’z 

The function F1 is equal to 1 if x is equal to 1 or if both y’ and z are equal to 1. F1 is equal to 0 otherwise. The complement operation dictates that when y’ = 1, y = 0. Therefore, F1 = 1 if x = 1 or if y = 0 and z = 1. 

A Boolean function expresses the logical relationship between binary variables and is evaluated by determining the binary value of the expression for all possible values of the variables. 

A Boolean function can be represented in a truth table. The number of rows in the truth table is 2[n] , where n is the number of variables in the function. The binary combinations for the truth table are obtained from the binary numbers by counting from 0 through 2[n ] - 1. 

## Truth Table for F1 

|x|y|z|F1|||
|---|---|---|---|---|---|
|0|0|0|0|||
|0|0|1|1|||
|0|1|0|0|||
|0|1|1|0|||
|1|0|0|1|||
|1|0|1|1|||
|1|1|0|1|Gate Implementation of F1 = x + y’z|Gate Implementation of F1 = x + y’z|
|1|1|1|1|||



## **Note:** 

Q: Let a function F() depend on n variables. How many rows are there in the truth table of F() ? A: 2[n ] rows, since there are 2[n ] possible binary patterns/combinations for the n variables. 

## Truth Tables 

- Enumerates all possible combinations of variable values and the corresponding function value 

- Truth tables for some arbitrary functions 

F1(x,y,z), F2(x,y,z), and F3(x,y,z) are shown to the below. 

|x<br>~~PE~~|y<br>~~PE~~|z<br>~~PE~~|F1<br>~~PE~~|F2<br>~~PE~~|F3<br>~~PE~~|
|---|---|---|---|---|---|
|0<br>~~PE~~|0<br>~~PE~~|0<br>~~PE~~|0<br>~~PE~~|1<br>~~PE~~|1<br>~~PE~~|
|0<br>~~PE~~|0<br>~~PE~~|1<br>~~PE~~|0<br>~~PE~~|0<br>~~PE~~|1<br>~~PE~~|



|0|1|0|0|0|1|
|---|---|---|---|---|---|
|0|1|1|0|1|1|
|1|0|0|0|1|0|
|1|0|1|0|1|0|
|1|1|0|0|0|0|
|1|1|1|1|0|1|



- Truth table: a unique representation of a Boolean function 

- If two functions have identical truth tables, the functions are equivalent (and viceversa). 

- Truth tables can be used to prove equality theorems. 

- However, the size of a truth table grows exponentially with the number of variables involved, hence unwieldy. This motivates the use of Boolean Algebra. 

## **Boolean expressions-NOT unique** 

Unlike truth tables, expressions epresenting 

a Boolean function are NOT unique. 

- Example: 

      - F(x,y,z) = x’•y’•z’ + x’•y•z’ + 

         - x•y•z’ 

      - G(x,y,z) = x’•y’•z’ + y•z’ 

- The corresponding truth tables for 

   - F() and G() are to the right. They are identical. 

- Thus, F() = G() 

|x|y|z|F|G|
|---|---|---|---|---|
|0|0|0|1|1|
||||||
|0|0|1|0|0|
|0|1|0|1|1|
||||||
|0|1|1|0|0|
|1|0|0|0|0|
|1|0|1|0|0|
|1|1|0|1|1|
||||||
|1|1|1|0|0|



## **Algebraic Manipulation (Minimization of Boolean function)** 

- Boolean algebra is a useful tool for simplifying digital circuits. 

- Why do it? Simpler can mean cheaper, smaller, faster. 

- Example: Simplify F = x’yz + x’yz’ + xz. 

   - F= x’yz + x’yz’ + xz 

   - = x’y(z+z’) + xz 

   - = x’y•1 + xz 

= x’y + xz 

- Example: Prove 

x’y’z’ + x’yz’ + xyz’ = x’z’ + yz’ 

- **Proof:** 

x’y’z’+ x’yz’+ xyz’ 

- = x’y’z’ + x’yz’ + x’yz’ + xyz’ 

- = x’z’(y’+y) + yz’(x’+x) 

- = x’z’•1 + yz’•1 

- = x’z’ + yz’ 

## **Complement of a Function** 

   - The complement of a function is derived by interchanging (• and +), and (1 and 0), and complementing each variable. 

   - Otherwise, interchange 1s to 0s in the truth table column showing F. 

- The _complement_ of a function IS NOT THE SAME as the _dual_ of a function. 

- Example 

   - Find G(x,y,z), the complement of F(x,y,z) = xy’z’ + x’yz 

Ans: G = F’ = (xy’z’ + x’yz)’ 

- = (xy’z’)’ • (x’yz)’ _DeMorgan_ 

- = (x’+y+z) • (x+y’+z’) _DeMorgan_ again 

**Note:** The complement of a function can also be derived by finding the function’s _dual,_ and then complementing all of the literals 

## **Canonical and Standard Forms** 

We need to consider formal techniques for the simplification of Boolean functions. Identical functions will have exactly the same canonical form. 

- Minterms and Maxterms 

- Sum-of-Minterms and Product-of- Maxterms 

- Product and Sum terms 

- Sum-of-Products (SOP) and Product-of-Sums (POS) 

## **Definitions** 

**Literal:** A variable or its complement 

**Product term:** literals connected by • 

**Sum term:** literals connected by + 

**Minterm:** a product term in which all the variables appear exactly once, either complemented or uncomplemented. 

**Maxterm:** a sum term in which all the variables appear exactly once, either complemented or uncomplemented. 

**Canonical form:** Boolean functions expressed as a sum of Minterms or product of Maxterms are said to be in canonical form. 

## **Minterm** 

- Represents exactly one combination in the truth table. 

- Denoted by mj, where j is the decimal equivalent of the minterm’s corresponding binary combination (bj). 

- A variable in mj is complemented if its value in bj is 0, otherwise is uncomplemented. 

Example: Assume 3 variables (A, B, C), and j=3. Then, bj = 011 and its corresponding minterm is  denoted by mj = A’BC 

## **Maxterm** 

- Represents exactly one combination in the truth table. 

- Denoted by _Mj_ , where _j_ is the decimal equivalent of the maxterm’s corresponding binary combination _(bj_ ) _._ 

- A variable in _Mj_ is complemented if its value in _bj_ is 1, otherwise is uncomplemented. 

Example: Assume 3 variables (A, B, C), and _j_ =3. Then, b _j_ = 011 and its corresponding maxterm is denoted by M _j_ = A+B’+C’ 

## **Truth Table notation for Minterms and Maxterms** 

- Minterms and Maxterms are easy to denote using a truth table. 

- Example: Assume 3 variables x,y,z (order is fixed) 

|x|y|z|Minterm|Maxterm|
|---|---|---|---|---|
|0|0|0|x’y’z’ = m0|x+y+z = M0|
|0|0|1|x’y’z = m1|x+y+z’ = M1|
|0|1|0|x’yz’ = m2|x+y’+z = M2|
|0|1|1|x’yz = m3|x+y’+z’= M3|
|1|0|0|xy’z’ = m4|x’+y+z = M4|
|1|0|1|xy’z = m5|x’+y+z’ = M5|
|1|1|0|xyz’ = m6|x’+y’+z = M6|
|1|1|1|xyz = m7|x’+y’+z’ = M7|



## **Canonical Forms** 

- Every function F() has two canonical forms: 

   - Canonical Sum-Of-Products (sum of minterms) 

   - Canonical Product-Of-Sums (product of maxterms) 

Canonical Sum-Of-Products: 

The minterms included are those mj such that F( ) = 1 in row j of the truth table for F( ). Canonical Product-Of-Sums: 

The maxterms included are those Mj such that F( ) = 0 in row j of the truth table for F( ). 

## **Example** 

Consider a Truth table for f1(a,b,c) at right The canonical sum-of-products form for f1 is f1(a,b,c) = m1 + m2 + m4 + m6 = a’b’c + a’bc’ + ab’c’ + abc’ The canonical product-of-sums form for f1 is f1(a,b,c) = M0 • M3 • M5 • M7 = (a+b+c)•(a+b’+c’)• (a’+b+c’)•(a’+b’+c’). 

- Observe that: mj = Mj’ 

|a|b|c|f1|
|---|---|---|---|
|0|0|0|0|
|0|0|1|1|
|0|1|0|1|
|0|1|1|0|
|1|0|0|1|
|1|0|1|0|
|1|1|0|1|
|1|1|1|0|



## **Shorthand: ∑ and ∏** 

- f1(a,b,c) = ∑ m(1,2,4,6), where ∑ indicates that this is a sum-of-products form, and m(1,2,4,6) indicates that the minterms to be included are m1, m2, m4, and m6. 

- f1(a,b,c) = ∏ M(0,3,5,7), where ∏ indicates that this is a product-of-sums form, and M(0,3,5,7) indicates that the maxterms to be included are M0, M3, M5, and M7. 

- Since mj = Mj’ for any _j_ , 

   - ∑ m(1,2,4,6) = ∏ M(0,3,5,7) = f1(a,b,c) 

- 

## **Conversion between Canonical Forms** 

- Replace ∑ with ∏ (or _vice versa_ ) and replace those _j’_ s that appeared in the original form with those that do not. 

   - Example: 

f1(a,b,c)= a’b’c + a’bc’ + ab’c’ + abc’ 

- = m1 + m2 + m4 + m6 

- = ∑(1,2,4,6) 

- = ∏(0,3,5,7) 

- = (a+b+c)•(a+b’+c’)•(a’+b+c’)•(a’+b’+c’) 

## **Standard Forms** 

Another way to express Boolean functions is in standard form. In this configuration, the terms that form the function may contain one, two, or any number of literals. 

There are two types of standard forms: the sum of products and products of sums. 

The sum of products is a Boolean expression containing AND terms, called product terms, with one or more literals each. The sum denotes the ORing of these terms. An example of a function expressed as a sum of products is 

## F1 = y’ + xy + x’yz’ 

The expression has three product terms, with one, two, and three literals. Their sum is, in effect, an OR operation. 

A product of sums is a Boolean expression containing OR terms, called sum terms. Each term may have any number of literals. The product denotes the ANDing of these terms. An example of a function expressed as a product of sums is 

## F2 = x(y’ + z)(x’ + y + z’) 

This expression has three sum terms, with one, two, and three literals. The product is an AND operation. 

## **Conversion of SOP from standard to canonical form** 

## **Example-1** . 

## Express the Boolean function F = A + B’C as a sum of minterms. 

Solution: The function has three variables: A, B, and C. The first term A is missing two variables; therefore, A = A(B + B’) = AB + AB’ 

This function is still missing one variable, so 

A = AB(C + C’) + AB’ (C + C’) 

= ABC + ABC’ + AB’C + AB’C’ 

The second term B’C is missing one variable; hence, 

B’C = B’C(A + A’) = AB’C + A’B’C 

Combining all terms, we have 

F = A + B’C 

= ABC + ABC’ + AB’C + AB’C’+ A’B’C 

But AB’C appears twice, and according to theorem (x + x = x), it is possible to remove one of those occurrences. Rearranging the minterms in ascending order, we finally obtain 

F = A’B’C + AB’C + AB’C + ABC’ + ABC 

= m1 + m4 + m5 + m6 + m7 

When a Boolean function is in its sum‐of‐minterms form, it is sometimes convenient to express the function in the following brief notation: 

F(A, B, C) = ∑m (1, 4, 5, 6, 7) 

## **Example-2.** 

Express the Boolean function F = xy + x’z as a product of maxterms. 

Solution: First, convert the function into OR terms by using the distributive law: 

F = xy + x’z = (xy + x’)(xy + z) 

= (x + x’)(y + x’)(x + z)(y + z) 

= (x’+ y)(x + z)(y + z) 

The function has three variables: x, y, and z. Each OR term is missing one variable; therefore, 

x’+ y = x’ + y + zz’ = (x’ + y + z)(x’ + y + z’) 

x + z = x + z + yy’ = (x + y + z)(x + y’ + z) y + z = y + z + xx’ = (x + y + z)(x’ + y + z) 

Combining all the terms and removing those which appear more than once, we finally obtain 

F = (x + y + z)(x + y’ + z)(x’ + y + z)(x’ + y + z) 

F= M0M2M4M5 

A convenient way to express this function is as 

follows: F(x, y, z) = πM(0, 2, 4, 5) 

The product symbol, π, denotes the ANDing of maxterms; the numbers are the indices of the maxterms of the function. 

## **Unit-II** 

## **Minimization Techniques** 

## **Two-variable k-map:** 

A two-variable k-map can have 2[2] =4 possible combinations of the input variables A and B. Each  of  these  combinations,     ,    B,A     ,AB(in  the  SOP  form)  is  called  a  minterm. The minterm may be represented in terms of their decimal designations – m0 for     , m1 for B,m2 for A and m3 for AB, assuming that A represents the MSB.  The letter m stands for minterm and the subscript represents the decimal designation of the minterm. The presence or absence of a minterm in the expression indicates that the output of the logic circuit assumes logic 1 or logic 0 level for that combination of input variables. 

The expression f= ,+ B+A  +AB , it can  be expressed using min 

term as F= m0+m2+m3=∑m(0,2,3) 

Using Truth Table: 

|Minterm|Inputs<br>A<br>B|Output<br>F|
|---|---|---|
|0|0<br>0|1|
|1|0<br>1|0|
|2|1<br>0|1|
|3|1<br>1|1|



A 1 in the output contains that particular minterm in its sum and a 0 in that column indicates that the particular mintermdoes not appear in the expression for output . this information can also be indicated by a two-variable k-map. 

## **Mapping of SOP Expresions** : 

A two-variable k-map has 22=4 squares .These squares are called cells. Each square on the k- map represents a unique minterm. The minterm designation of the squares are placed in any square, indicates that the corresponding minterm does output expressions. And a 0 or no entry in any square indicates that the corresponding minterm does not appear in the expression for output. 

The minterms of a two-variable k-map 

The mapping of the expressions =∑m(0,2,3)is 

k-map of ∑m(0,2,3) 

**EX** : Map the expressions f= B+A 

F= m1+m2=∑m(1,2)The k-map is 

## **Minimizations of SOP expressions** : 

To minimize Boolean expressions given in the SOP form by using the k-map, look for adjacent adjacent squares having 1‘s minterms adjacent to each other, and combine them to form larger squares to eliminate some variables. Two squares are said to be adjacent to each other, if their minterms differ in only one variable. (i.e,    B & A    differ only in one variable. so they may be combined to form a 2-square to eliminate the variable B.similarly all other. 

The necessary condition for adjacency of minterms is that their decimal designations must differ by a power of 2. A minterm can be combined with any number of minterms adjacent to it to form larger squares. Two minterms which are adjacent to each other can be combined to form a bigger square called a 2-square or a pair. This eliminates one variable – the variable that is not common to both the minterms. For EX: 

m0 and m1 can be combined to yield, 

**==> picture [123 x 11] intentionally omitted <==**

)= m0 and m2 can be combined to yield, 

**==> picture [168 x 12] intentionally omitted <==**

m1 and m3 can be combined to yield, 

f3= m1+m3= B+AB=B( + )=B 

m2 and m3 can be combined to yield, 

f4 = m2+m3=A +AB=A(B+ )=A 

m0 ,m1 ,m2 and m3 can be combined to yield, 

**==> picture [100 x 88] intentionally omitted <==**

f1= f2= f3=B f4=A f5=1 

The possible minterm groupings in a two-variable k-map. 

Two 2-squares adjacent to each other can be combined to form a 4-square. A 4-square eliminates 2 variables. A 4-square is called a quad. To read the squares on the map after minimization, consider only those variables which remain constant through the square, and ignore the variables which are varying. Write the non complemented variable if the variable is remaining constant as a 1, and the complemented variable if the variable is remaining constant as a 0, and write the variables as a product term. In the above figure f1 read as , because, along the square , A remains constant as a 0, that is , as , where as B is changing from 0 to 1. 

**EX:** Reduce the minterm f= +A  +AB using mapping Expressed in terms of minterms, the given expression is F=m0+m1+m2+ m3=m∑(0,1,3)& the figure shows the k-map for f and its reduction . In one 2-square, A is constant as a 0 but B varies from a 0 to a 1, and in the other 2- square, B is constant as a 1 but A varies from a 0 to a 1. So, the reduced expressions is +B. 

It requires two gate inputs for realization as f=   +B (k-map in SOP form, and logic diagram.) 

The main criterion in the design of a digital circuit is that its cost should be as low as possible. For that the expression used to realize that circuit must be minimal.Since the cost is proportional to number of gate inputs in the circuit in the circuit, an expression is considered minimal only if it corresponds to the least possible number of gate inputs. & there is no guarantee for that k-map in SOP is the real minimal. To obtain real minimal expression, obtain the minimal expression both in SOP & POS form form by using k-maps and take the minimal of these two minimals. 

The 1‘s on the k-map indicate the presence of minterms in the output expressions, where as the 0s indicate the absence of minterms .Since the absence of a minterm in the SOP expression means the presense of the corresponding maxterm in the POS expression of the same .when a SOP expression is plotted on the k-map, 0s or no entries on the k-map represent the maxterms. To obtain the minimal expression in the POS form, consider the 0s on the k-map and follow the procedure used for combining 1s. Also, since the absence of a maxterm in the POS expression means the presence of the corresponding minterm in the SOP expression of the same , when a POS expression is plotted on the k-map, 1s or no entries on the k-map represent the minterms. 

## **Mapping of POS expressions:** 

Each sum term in the standard POS expression is called a maxterm. A function in two variables (A, B) has four possible maxterms, A+B,A+ , +B, + 

. They are represented as M0, M1, M2, and M3respectively. The uppercase letter M stands for maxterm and its subscript denotes the decimal designation of that maxterm obtained by treating the non-complemented variable as a 0 and the complemented variable as a 1 and putting them side by side for reading the decimal equivalent of the binary number so formed. 

For mapping a POS expression on to the k-map, 0s are placed in the squares corresponding to the maxterms which are presented in the expression an d1s are placed in the squares corresponding to the maxterm which are not present in the expression. The decimal designation of the squares of the squares for maxterms is the same as that for the minterms. A two-variable k-map & the associated maxterms are asthe maxterms of a two-variable k-map 

The possible maxterm groupings in a two-variable k-map 

## **Minimization of POS Expressions:** 

To obtain the minimal expression in POS form, map the given POS expression on to the K-map and combine the adjacent 0s into as large squares as possible. Read the squares putting the complemented variable if its value remains constant as a 1 and the non-complemented variable if its value remains constant as a 0 along the entire square ( ignoring the variables which do not remain constant throughout the square) and then write them as a sum term. 

Various maxterm combinations and the corresponding reduced expressions are shown in figure. In this f1 read as A because A remains constant as a 0 throughout the square and B changes from a 0 to a 1. f2 is read as B‘ because B remains constant along the square as a 1 and A changes from a 0 to a 1. f5 

Is read as a 0 because both the variables are changing along the square. 

## **Ex:** Reduce the expression f=(A+B)(A+B‘)(A‘+B‘) using mapping. 

The given expression in terms of maxterms is f=πM(0,1,3). It requires two gates inputs for realization of the reduced expression as 

F=AB‘ 

K-map in POS form and logic diagram 

In this given expression ,the maxterm M2 is absent. This is indicated by a 1 on the k-map. The corresponding SOP expression is ∑m2 or AB‘. This realization is the same as that for the POS form. 

## **Three-variable K-map:** 

A function in three variables (A, B, C) expressed in the standard SOP form can have eight possible combinations: A B C , AB C,A BC ,A BC,AB C ,AB C,ABC , and ABC. Each one of these combinations designate d by m0,m1,m2,m3,m4,m5,m6, and m7, respectively, is called a minterm. A is the MSB of the minterm designator and C is the LSB. 

In the standard POS  form,  the  eight  possible  combinations  are:A+B+C,  A+B+C  , A+B +C,A+B + C ,A + B+ C,A + B + C ,A + B + C,A + B + C . Each oneof these combinations designated by M0, M1, M2, M3, M4, M5, M6, and M7respectively is called a maxterm. A is the MSB of the maxterm designator and C is the LSB. 

A three-variable k-map has, therefore, 8(=2[3] ) squares or cells, and each square on the map represents a minterm or maxterm as shown in figure. The small number on the top right corner of each cell indicates the minterm or maxterm designation. 

The three-variable k-map. 

The binary numbers along the top of the map indicate the condition of B and C for each column. The binary number along the left side of the map against each row indicates the condition of A for that row. For example, the binary number 01 on top of the second column in fig indicates that the variable B appears in complemented form and the variable C in noncomplemented form in all the minterms in that column. The binary number 0 on the left of the first row indicates that the variable A appears in complemented form in all the minterms in that row, the binary numbers along the top of the k-map are not in normal binary order. They are, infact, in the Gray code. This is to ensure that twophysically adjacent squares are really adjacent, i.e., their minterms or maxterms differ by only one variable. 

Ex: Map the expression f=:       C+         +        +        +ABC 

In   the   given   expression   ,   the   minterms   are  :        C=001=m1 ; =101=m5; =010=m2; 

=110=m6;ABC=111=m7. 

So the expression is f=∑m(1,5,2,6,7)= ∑m(1,2,5,6,7). The corresponding k-map is 

K-map in SOP form 

Ex: Map the expression f= (A+B+C),( + + ) ( + + )(A + + )( + + ) 

In the given expression the maxterms are :A+B+C=000=M0; + + =101=M5; + + = 111=M7; A + + =011=M3; + + =110=M6. 

So the expression is f = π M (0,5,7,3,6)= π M (0,3,5,6,7). The mapping of the expression is 

K-map in POS form. 

## **Minimization of SOP and POS expressions:** 

For reducing the Boolean expressions in SOP (POS) form plotted on the k-map, look at the 1s (0s) present on the map. These represent the minterms (maxterms). Look for the minterms (maxterms) adjacent to each other, in order to combine them into larger squares. Combining of adjacent squares in a k-map containing 1s (or 0s) for the purpose of simplification of a SOP (or POS)expression is called _looping_ . Some of the minterms (maxterms) may have many adjacencies. Always start with the minterms (maxterm) with the least number of adjacencies and try to form as large as large a square as possible. The larger must form a geometric square or rectangle. They can be formed even by wrapping around, but cannot be formed by using diagonal configurations. Next consider the minterm (maxterm) with next to the least number of adjacencies and form as large a square as possible. Continue this till all the minterms (maxterms) are taken care of . A minterm (maxterm) can be part of any number of squares if it is helpful in reduction. Read the minimal expression from the k-map, corresponding to the squares formed. There can be more than one minimal expression. 

Two squares are said to be adjacent to each other (since the binary designations along the top of the map and those along the left side of the map are in Gray code), if they are physically adjacent to each other, or can be made adjacent to each other by wrapping around. For squares to be combinable into bigger squares it is essential but not sufficient that their minterm designations must differ by a power of two. 

General procedure to simplify the Boolean expressions: 

1. Plot the k-map and place 1s(0s) corresponding to the minterms (maxterms) of the SOP (POS) expression. 

2. Check the k-map for 1s(0s) which are not adjacent to any other 1(0). They are isolated minterms(maxterms) . They are to be read as they are because they cannot be combined even into a 2-square. 

3. Check for those 1s(0S) which are adjacent to only one other 1(0) and make them pairs (2 squares). 

4. Check for quads (4 squares) and octets (8 squares) of adjacent 1s (0s) even if they contain some 1s(0s) which have already been combined. They must geometrically form a square or a rectangle. 

5. Check for any 1s(0s) that have not been combined yet and combine them into bigger squares if possible. 

6. Form the minimal expression by summing (multiplying) the product the product (sum) terms of all the groups. 

## **Reading the K-maps:** 

While reading the reduced k-map in SOP (POS) form, the variable which remains constant as 0 along the square is written as the complemented (non-complemented) variable and the one which remains constant as 1 along the square is written as non-complemented (complemented) variable and the term as a product (sum) term. All the product (sum) terms are added (multiplied). 

Some possible combinations of minterms and the corresponding minimal expressions readfrom the k-maps are shown in fig: Here f6 is read as 1, because along the 8-square no variable remains constant. F5  is read as      , because, along the 4-square formed by0,m1,m2     and m3 , the variables B and C are changing, and A remains constant as a 0. Algebraically, 

**==> picture [94 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
f5= m0+m1+m2+m3<br>**----- End of picture text -----**<br>


**==> picture [140 x 79] intentionally omitted <==**

**----- Start of picture text -----**<br>
=         +      C+         +<br>=       (    +C)+    B(C+ )<br>=       +  B<br>=    (   +B)=<br>**----- End of picture text -----**<br>


f3  is read as   +    ,  because in the 4-square formed by m0,m2,m6, and m4, the variable A and  B are changing , where as the variable C remains constant as a 0. So it is read as . In the 4-square formed by m0, m1, m4, m5, A and C are changing but B remains constant as a 0. So it is read as . So, the resultant expression for f3 is the sum of these two, i.e., + . 

f1 is read as       +       +       ,because in the 2-square formed by m0 and m4 , A is changing from a 0 to a 1. Whereas B and C remain constant as a 0. So it s read as          . In the     2-square formed by m0 and m1, C is changing from a 0 to a 1, whereas A and B remain constant as a 0. So it is read as     .In the 2-square formed  by m0 and m2   , B is changing from a 0 to    a 1 whereas A and C remain  constant  as  a  0.  So,  it  is  read  as  .   Therefore,   the   resultant   SOP expression is 

**+** + 

Some possible maxterm groupings and the corresponding minimal POS expressions read from the k-map are 

In this figure, along the 4-square formed by M1, M3, M7, M5, A and B are changing from a 0 to a 1, where as C remains constant as a 1. SO it  is read as   . Along the 4-squad formed by   M3, M2, M7, and M6, variables A and C are changing from a 0 to a 1. But B remains constant as a 1. So it is read as   . The minimal expression is the product of these two terms , i.e., f1 = (  )(   ).also in this figure, along the 2-square formed by M4 and M6 , variable B is changing from a 0 to a 1, while variable A remains constant as a 1 and variable C remains constant as a 0.    SO, read  it as 

+C. Similarly, the 2-square formed by M7 andM6 is read as   +    , while the 2-square  formed by M2 and M6 is read as +C. The minimal expression is the product of these sum terms, i.e, f2 =( + ) **+(** + )+( +C) 

**Ex** :Reduce the expression f=∑m(0,2,3,4,5,6) using mapping and implement it in AOI logic as well as in NAND logic.The Sop k-map and its reduction , and the implementation of the minimal expression using AOI logic and the corresponding NAND logic are shown in figures below 

In SOP k-map, the reduction is done as: 

1. m5 has only one adjacency m4 , so combine m5 and m4 into a square. Along this 2-square A remains constant as 1 and B remains constant as 0 but C varies from 0 to 1. So read it as A . 

2. m3 has only one adjacency m2 , so combine m3 and m2 into a square. Along this 2-square A remains constant as 0 and B remains constant as 1 but C varies from 1 to 0. So read it as B. 

3. m6 can form a 2-square with m2 and m4 can form a 2-square with m0, but observe that by wrapping the map from left to right m0, m4 ,m2 ,m6 can form a 4-square. Out of these m2 andm4 have already been combined but they can be utilized again. So make it. Along this 4-square, A is changing from 0 to 1 and B is also changing from 0 to 1 but C is remaining constant as 0. so read it as . 

4. Write all the product terms in SOP form. So the minimal SOP expression is 

fmin= **k-map AOI logic NAND logic** 

## **Four variable k-maps:** 

Four variable k-map expressions can have 2[4] =16 possible combinations of input variables such as             ,             ,------------ABCD with minterm  designations m0,m1 -------------------- m15 respectively in SOP form  & A+B+C+D, A+B+C+      ,----------     +      +     + with maxterms M0,M1, --------- 

-M15 respectively in POS form. It has 2[4] =16 squares or cells.The binary number designations of rows & columns are in the gray code. Here follows 01 & 10 follows 11 called Adjacency ordering. 

SOP form POS form 

EX: 

## **Five variable k-map:** 

Five variable k-map can have 2[5] =32 possible combinations of input variable as 

,             E,--------ABCDE  with  minterms  m0,  m1-----m31 respectively in  SOP & A+B+C+D+E,   A+B+C+           ,----------     +       +     +       + with maxterms M0,M1, ----------M31 respectively in POS form. It has 2[5] =32 squares or cells of the k-map are divided into 2 blocks of 

16 squares each.The left block represents minterms from m0 to m15 in which A is a 0, and the right block represents minterms from m16 to m31 in which A is 1.The 5-variable k-map may contain 2-squares, 4-squares , 8-squares , 16-squares or 32-squares involving these two blocks. Squares are also considered adjacent in these two blocks, if when superimposing one block on top of another, the squares coincide with one another. 

Grouping s is 

Ex: F=∑m(0,1,4,5,6,13,14,15,22,24,25,28,29,30,31) is SOP 

POS is F=πM(2,3,7,8,9,10,11,12,16,17,18,19,20,21,23,26,27) 

The real minimal expression is the minimal of the SOP and POS forms. 

The reduction is done as 

1. There is no isolated 1s 

2. M12 can go only with m13. Form a 2-square which is read as A‘BCD‘ 

3. M0 can go with m2,m16 and m18 . so form a 4-square which is read as B‘C‘E‘ 

4. M20,m21,m17 and m16 form a 4-square which is read as AB‘D‘ 

5. M2,m3,m18,m19,m10,m11,m26 and m27 form an 8-square which is read as C‘d 

6. Write all the product terms in SOP form. 

So the minimal expression is 

Fmin= A‘BCD‘+B‘C‘E‘+AB‘D‘+C‘D(16 inputs) 

In the POS k-map ,the reduction is done as: 

   1. There are no isolated 0s 

3. 

- 4.M8 

5. M28 

## 6.M30 

7. Sum terms in POS form. So the minimal expression in POS is 

Fmin= A‘BcD‘+B‘C‘E‘+AB‘D‘+C‘D 

## **Six variable k-map:** 

Six variable k-map can have 2[6] =64 combinations as                  ,                ,-----------ABCDEF with minterms m0, m1-----m63 respectively in SOP & (A+B+C+D+E+F), ---------- ( +    +     +     + +    ) with maxterms M0,M1, -----------M63    respectively in POS form. It has 2[6] =64 squares or cells of the k-map are divided into 4 blocks of 16 squares each. 

Some possible groupings in a six variable k-map 

**Don’t care combinations:** For certain input combinations, the value of the output is unspecified either because the input combinations are invalid or because the precise value of the output is of no consequence. The combinations for which the value of experiments are not specified are called don‘t care combinations are invalid or because the precise value of the output is of no consequence. The combinations for which the value of expressions is not specified are called don‘t care combinations or Optional Combinations, such expressions stand incompletely specified. The output is a don‘t care for these invalid combinations. 

Ex:In XS-3 code system, the binary states 0000, 0001, 0010,1101,1110,1111 are unspecified. & never occur called don‘t cares. 

A standard SOP expression with don‘t cares can be converted into a standard POS form by keeping the don‘t cares as they are & writing the missing minterms of the SOP form as the maxterms of the POS form viceversa. 

Don‘t cares denoted by ‗X‘ or ‗φ‘ 

Ex:f=∑m(1,5,6,12,13,14)+d(2,4) 

Or f=π M(0,3,7,9,10,11,15).πd(2,4) 

SOP minimal form fmin=       +B  + 

POS minimal form fmin=(B+D)( +B)( +D) 

= + + + + ( + 

## **Prime implicants, Essential Prime implicants, Redundant prime implicants:** 

Each square or rectangle made up of the bunch of adjacent minterms is called a subcube. Each of these subcubes is called a Prime implicant (PI). The PI which contains at leastone which cannot be covered by any other prime implicants is called as Essential Prime implicant (EPI).The PI whose each 1 is covered at least by one EPI is called a Redundant Prime implicant (RPI). A PI which is neither an EPI nor a RPI is called a Selective Prime implicant (SPI). 

The function has unique MSP comprising EPI is 

## F(A,B,C,D)= CD+ABC+A D + B 

The RPI ‗BD‘ may be included without changing the function but the resulting expression would not be in minimal SOP(MSP) form. 

Essential and Redundant Prime Implicants 

F(A,B,C,D)=∑m(0,4,5,10,11,13,15) SPI are marked by dotted squares, shows MSP form of a function need not be unique. 

Essential and Selective Prime Implicants 

Here, the MSP form is obtained by including two EPI‘s & selecting a set of SPI‘s to cover remaining uncovered minterms 5,13,15. & these can be covered as 

(A) (4,5) &(13,15) ---------- B +ABD 

(B) (5,13) & (13,15) -------- B D+ABD 

(C) (5,13) & (15,11) ------- B D+ACD 

F(A,B,C,D)= +A C---------EPI‘s + B +ABD 

(OR) F(A,B,C,D)=         +A  C---------EPI‘s + B   D+ABD (OR) F(A,B,C,D)=         +A  C---------EPI‘s + B   D+ACD 

**False PI’s Essential False PI’s, Redundant False PI’s & Selective False PI’s:** 

The maxterms are called falseminterms. The PI‘s is obtained by using the maxterms are called False PI‘s (FPI). The FPI which contains at least one ‗0‘ which can‘t be covered by only other FPI is called an Essential False Prime implicant (ESPI) 

F(A,B,C,D)= ∑m(0,1,2,3,4,8,12) 

=π M(5,6,7,9,10,11,13,14,15) 

Fmin= ( + )( + )( + )( + ) 

All the FPI, EFPI‘s as each of them contain atleast one ‗0‘ which can‘t be covered by any other FPI 

**==> picture [83 x 18] intentionally omitted <==**

**----- Start of picture text -----**<br>
lof] of} — errs<br>**----- End of picture text -----**<br>


Essential False Prime implicants 

Consider Function F(A,B,C,D)= π M(0,1,2,6,8,10,11,12) 

Essential and Redundant False Prime Implicants 

## **Mapping when the function is not expressed in minterms (maxterms):** 

An expression in k-map must be available as a sum (product) of minterms (maxterms). However if not so expressed, it is not necessary to expand the expression algebraically into its minterms (maxterms). Instead, expansion into minterms (maxterms) can be accomplished in the process of entering the terms of the expression on the k-map. 

## **Limitations of Karnaugh maps:** 

- Convenient as long as the number of variables does not exceed six. 

- Manual technique, simplification process is heavily dependent on the human abilities. 

## **Quine-Mccluskey Method:** 

It also known as _Tabular method._ It is more systematic method of minimizing expressions of even larger number of variables. It is suitable for hand computation as well as computation by machines i.e., programmable. . The procedure is based on repeated application of the combining theorem. 

PA+P =P (P is set of literals) on all adjacent pairs of terms, yields the set of all PI‘s from which a minimal sum may be selected. 

Consider expression 

∑m(0,1,4,5)= + C+A +A C 

First, second terms & third, fourth terms can be combined 

( + )+ (C+ )= +A 

Reduced to 

= (    +    ) 

The same result can be obtained by combining m0& m4 & m1&m5 in first step & resulting terms in the second step . 

Procedure: 

- Decimal Representation 

- Don‘t cares 

- PI chart 

- EPI 

- Dominating Rows & Columns 

- Determination of Minimal expressions in comples cases. 

Branching Method: 

Comparing the terms of index 0 with the terms of index | of column 1, m,(0000) is combined with m, (0001) to yield 0, 1 (1), i.e. 000-. This is recorded in column 2 and 0000 and 0001 are checked offin column 1. m,(0000) is combined with m,(1000) to yield 0, 8 (8), i.e. — 000. This is recorded in column 2 and 1000 is checked off in column 1. Note that 0000 of column | has already been checked off. No more combinations of terms of index 0 and index 1 are possible. So, draw a line below the last combination of these groups, i.e. below 0, 8 (8), — 000 in column 2. Now 0, 1 (1), ne. 000 - and 0, 8 (8), ie. — 000 are the terms in the first group of column 2. Comparing the terms of index | with the terms of index 2 in column 1, m,(0001) is combined with m,(1001) to yield 1,9 (8), i.e. — O01. This is recorded in column 2 and 1001 is checked off in column | because 0001 has already been checked off. m,(1000) is combined with m,(1001) to yield 8,9 (1), i.e. 100 —-. This is recorded in column 2. 1000 and 1001 of column 1 have already been checked off. So, no need to check them off again. No more combinations of terms of index | and index 2 are possible. So, draw a line below the last combination of these groups, i.e. 8,9 (1), -— 001 in column 2. Now 1, 9 (8), ie.—001 and 8, 9 (1), i.e. 100- are the terms in the second group of column 2. Similarly, comparing the terms of index 2 with the terms of index 3 in column 1, m,(0110) and m,(O0111) yield 6, 7 (1), ic. O11-. Record it in column 2 and check off 6(0110) and 7(O111). m,(0110) and m, (1110) yield 6, 14 (8), i.e. -110. Record it in column 2 and check off 6(0110) and 14(1110). m,(1001) and m,,(1101) yield 9, 13 (4), i.c. 1-01. Record it in column 2 and check off 9(1001) and 13(1101). - So, 6, 7 (1), i.e. O11-, and 6, 14 (8), ie. -110 and 9, 13 (4), i.e. 1-O1 are the terms in group 3 of column 2. Drawa line at the end of 9, 13 (4), i.e. 1-O1. Also, comparing the terms of index 3 with the terms of index 4 in column 1, m,(O111) and m, (1111) yield 7, 15 (8), i.e. -111. Record it in column 2 and check off 7(O111) and 15(1111). m,,(1101) and m,,(1111) yield 13, 15 (2), i.e. 11-1. Record it in column 2 and check off 13 and 15. m,,(1110) and m, (1111) yield 14, 15 (1), i.e. 111-. Record it in column 2 and check off 14 and 15. So, 7, 15 (8), ic. -111, and 13, 15 (2), ic. 11-1 and 14, 15 (1), i.e. 111- are the terms in group4 of column 2, Column 2 is completed now. 

EX: 

The non-combinable terms P, Q, R, 5 and T are recorded as prime implicants. P+ 5,7, 13,15 (2,8)=X1X1=BD 

(Literals with weights 2 and 8, ic. C and A are deleted. The lowest minterm is m,(5 = 4 + 1). So, literals with weights 4 and |, i.e. B and D are present in non-complemented form. So, read it as BD.) Q 38,9, 12,13(1,4)=1X0X=ACG (Literals with weights | and 4, i.e. D and B are deleted. The lowest minterm is m,. So, literal with weight 8 is present in non-complemented form and literal with weight 2 is present in complemented form. So, read it as AC.) 

R > 2,3,6,7(1,4)=0X1X=AC 

(Literals with weights | and 4, i.e. D and B are deleted. The lowest minterm is m,. So, literal with weight 2 is present in non-complemented form and literal with weight 8 is present in complemented form. So, read it as AC.) 

§231,5,9,13(4,8)=XX0O1=CD 

(Literals with weights 4 and 8, i.e. B and A are deleted. The lowest minterm is m,. So, literal with weight 1 is present in non-complemented form and literal with weight 2 is present in complemented form. So, read it as CD.) 

T>1,3,5,7(2,4)=0XX1=AD 

|(Literals with weights 2 and 4, i.e. C and B are deleted. The lowest minterm is 1. So, literal with|
|---|
|weight | ispresent innon-complemented formand literal withweight8 ispresent incomplemented|
|form. So, read it as AD.)|
|The prime implicant chart ofthe expression|
|f=ZX m(1, 2, 3, 5, 6, 7, 8, 9, 12, 13, 15)|
|is as shown inTable 3.5. Itconsistsof 11 columnscorresponding tothe numberofmintermsand5|
|rowscorresponding to the prime implicants P,Q, R, S, andTgenerated. Row R contains fourxs at|
|the intersections with columns 2, 3, 6, and 7, because these minterms are covered by the prime|
|implicant R.A row is said tocover thecolumns in which it has xs.The problem now is to select a|
|minimal subset of prime implicants, such that each column contains at least one x in the rows|
|corresponding totheselected subsetand the total numberofliterals intheprime implicants selected|
|is as small as possible. These requirements guarantee that the number of unions of the selected|
|primeimplicants isequal totheoriginalnumberofmintermsandthat,nootherexpression containing|
|fewer literals can be found.|
|Table 3.5<br>Example 3.30: Prime implicant chart|
|ee<br>oe ee ee ee<br>ae oe oe ae|
|1<br>2<br>3<br>5<br>6<br>7<br>8<br>9<br>12<br>13<br>15|
|*P<br>— 5,7,13, 15 (2, 8)<br>x<br>x<br>x<br>x|
|*Q —> 8,9,<br>12, 13(1,4)<br>x<br>x<br>x<br>x|
|*R =<br>2,3, 6,7 (1, 4)<br>x<br>x<br>x<br>x|
|S—<br>1,5, 9, 13 (4, 8)<br>a<br>x<br>x<br>x|
|T—<br>1,3,5,7(2,4)<br>x<br>x<br>x<br>x|



In the prime implicant chart of Table 3.5, m, and m, are covered by R only. So, R is an essential prime implicant. So, check off all the minterms covered by it, i.e. m,, m,, m,, and m,. Q is also an essential prime implicant because only Q covers m, and m,,. Check off all the minterms covered by it, i.e. my, my, m,,, and m,,. P is also an essential prime implicant, because m,, is covered only by P. So check off m,,, m,, m,, and m,, covered by it. Thus, only minterm | is not covered. Either rowS or row T can cover it and both have the same number of literals. Thus, two minimal expressions are possible. 

P+Q+R+S=BD+AC+AC+CD or P+Q+R+T=BD+AC+AC+AD 

## **UNIT-III** 

## **COMBINATIONAL CIRCUITS** 

## **Combinational Logic** 

- Logic circuits for digital systems may be combinational or sequential. 

- A combinational circuit consists of input variables, logic gates, and output variables. 

For n input variables,there are 2[n ] possible combinations of binary input variables .For each possible input Combination ,there is one and only one possible output combination.A combinational circuit can be described by m Boolean functions one for each output variables.Usually the input s comes from flip-flops and outputs goto flip-flops. 

## **Design Procedure:** 

1. The problem is stated 

2. The number of available input variables and required output variables is 

- determined. 3.The input and output variables are assigned lettersymbols. 

- 4.The truth table that defines the required relationship between inputs and outputs is derived. 

- 5.The simplified Boolean function for each output is obtained. 

## **Adders:** 

Digital computers perform variety of information processing tasks,the one is arithmetic operations.And the most basic arithmetic operation is the addition of two binary digits.i.e, 4 basic possible operations are: 

0+0=0,0+1=1,1+0=1,1+1=10 

The first three operations produce a sum whose length is one digit, but when augends and addend bits are equal to 1,the binary sum consists of two digits.The higher significant bit of this result is called a carry.A combinational circuit that performs the addition of two bits is called a halfadder. One that performs the addition of 3 bits (two significant bits & previous carry) is called a full adder.& 2 half adder can employ as a full-adder. 

**The Half Adder** : A Half Adder is a combinational circuit with two binary inputs (augends and addend bits and two binary outputs (sum and carry bits.) It adds the two inputs (A and B) and produces the sum (S) and the carry (C) bits. It is an arithmetic operation of addition of two single bit words. 

The Sum(S) bit and the carry (C) bit, according to the rules of binary addition, the sum (S) is the X-OR of A and B ( It represents the LSB of the sum). Therefore, 

**==> picture [48 x 10] intentionally omitted <==**

The carry (C) is the AND of A and B (it is 0 unless both the inputs are 1).Therefore, 

C=AB 

A half-adder can be realized by using one X-OR gate and one AND gate a 

Logic diagrams of half-adder 

NAND LOGIC: 

NOR Logic: 

## **The Full Adder:** 

A Full-adder is a combinational circuit that adds two bits and a carry and outputs a sum bit and a carry bit. To add two binary numbers, each having two or more bits, the LSBs can be added by using a half-adder. The carry resulted from the addition of the LSBs is carried over to the next significant column and added to the two bits in that column. So, in the second and higher columns, the two data bits of that column and the carry bit generated from the addition in the previous column need to be added. 

The full-adder adds the bits A and B and the carry from the previous column called the carry-in Cin and outputs the sum bit S and the carry bit called the carry-out Cout . The variable S gives the value of the least significant bit of the sum. The variable Cout gives the output carry.The 

eight rows under the input variables designate all possible combinations of 1s and 0s that these variables may have. The 1s and 0s for the output variables are determined from the arithmetic sum of the input bits. When all the bits are 0s , the output is 0. The S output is equal to 1 when only 1 input is equal to 1 or when all the inputs are equal to 1. The Cout has a carry of 1 if two or three inputs are equal to 1. 

From the truth table, a circuit that will produce the correct sum and carry bits in response to every possible combination of A,B and Cin is described by 

## _S_ = _ABCin_ + _ABCin_ + _ABCin_ + _ABCin_ 

_Cout_ = ~~_AB_~~ _Cin_ + _AB_ ~~_C_~~ _in_ + _ABCin_ ~~+~~ ~~_A_~~ _BCin_ 

and 

_S_ = _A_  _B_  _Cin_ 

_Cout_ = _ACin_ + _BCin_ + _AB_ 

The sum term of the full-adder is the X-OR of A,B, and Cin, i.e, the sum bit the modulo sum of the data bits in that column and the carry from the previous column. The  logic diagram of the full-adder using two X-OR gates and two AND gates (i.e, Two half adders) and one OR gate is 

**==> picture [11 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cy<br>**----- End of picture text -----**<br>


Even though a full-adder can be constructed using two half-adders, the disadvantage is that the bits must propagate through several gates in accession, which makes the total propagation delay greater than that of the full-adder circuit using AOI logic. 

The Full-adder neither can also be realized using universal logic, i.e., either only NAND gates or only NOR gates as 

NAND Logic: 

NOR Logic: 

## **Subtractors:** 

The subtraction of two binary numbers may be accomplished by taking the complement of the subtrahend and adding it to the minuend. By this, the subtraction operation becomes an addition operation and instead of having a separate circuit for subtraction, the adder itself can be used to perform subtraction. This results in reduction of hardware. In subtraction, each subtrahend bit of the number is subtracted from its corresponding significant minuend bit to form a difference bit. If the minuend bit is smaller than the subtrahend bit, a 1 is borrowed from the next significant position., that has been borrowed must be conveyed to the next higher pair of bits by means of a signal coming out (output) of a given stage and going into (input) the next higher stage. 

## **The Half-Subtractor:** 

A Half-subtractor is a combinational circuit that subtracts one bit from the other and produces the difference. It also has an output to specify if a 1 has been borrowed. . It is used to subtract the LSB of the subtrahend from the LSB of the minuend when one binary number is subtracted from the other. 

A Half-subtractor is a combinational circuit with two inputs A and B and two outputs d and b. d indicates the difference and b is the output signal generated that informs the next stage that a 1 has been borrowed. When a bit B is subtracted from another bit A, a difference bit (d) and a borrow bit (b) result according to the rules given as 

The output borrow b is a 0 as long as A≥B. It  is a 1 for A=0 and B=1. The d output is the result of the arithmetic operation2b+A-B. 

A circuit that produces the correct difference and borrow bits in response to every possible combination of the two 1-bit numbers is , therefore , 

d=A𝐵+𝐴 AGB and b=𝐴 B 

That is, the difference bit is obtained by X-OR ing the two inputs, and the borrow bit is obtained by ANDing the complement of the minuend with the subtrahend.Note that logic for this exactly the same as the logic for output S in the half-adder. 

A half-substractor can also be realized using universal logic either using only NAND gates or using NOR gates as: 

NAND Logic: 

NOR Logic: 

## **The Full-Subtractor** : 

The half-subtractor can be only for LSB subtraction. IF there is a borrow during the subtraction of the LSBs, it affects the subtraction in the next higher column; the subtrahend bit is subtracted from the minuend bit, considering the borrow from that column used for the subtraction in the preceding column. Such a subtraction is performed by a full-subtractor. It subtracts one bit (B) from another bit (A) , when already there is a borrow bi from this column for the subtraction in the preceding column, and outputs the difference bit (d) and the borrow bit(b) required from the next d and b. The two outputs present the difference and output borrow. The 1s and 0s for the output variables are determined from the subtraction of A-B-bi. 

From the truth table, a circuit that will produce the correct difference and borrow bits in response to every possiblecombinations of A,B and bi is 

A full-subtractor can be realized using X-OR gates and AOI gates as 

The full subtractor can also be realized using universal logic either using only NAND gates or using NOR gates as: 

NAND Logic: 

NOR Logic: 

33 

## **Binary Parallel Adder:** 

A binary parallel adder is a digital circuit that adds two binary numbers in parallel form and produces the arithmetic sum of those numbers in parallel form. It consists of full adders connected in a chain , with the output carry from each full-adder connected to the input carry of the next full-adder in the chain. 

The interconnection of four full-adder (FA) circuits to provide a 4-bit parallel adder. The augends bits of A and addend bits of B are designated by subscript numbers from right to left, with subscript 1 denoting the lower –order bit. The carries are connected in a chain through the full-adders. The input carry to the adder is Cin and the output carry is C4. The S output generates the required sum bits. When the 4-bit full-adder circuit is enclosed within an IC package, it has four terminals for the augends bits, four terminals for the addend bits, four terminals for the sum bits, and two terminals for the input and output carries. AN n-bit parallel adder requires n-full adders. It can be constructed from 4-bit, 2-bit and 1-bit full adder ICs by cascading several packages. The output carry from one package must be connected to the input carry of the one with the next higher –order bits. The 4-bit full adder is a typical example of an MSI function. 

## **Ripple carry adder:** 

In the parallel adder, the carry –out of each stage is connected to the carry-in of the next stage. The sum and carry-out bits of any stage cannot be produced, until sometime after the carry-in of that stage occurs. This is due to the propagation delays in the logic circuitry, 

34 

which lead to a time delay in the addition process. The carry propagation delay for each fulladder is the time between the application of the carry-in and the occurrence of the carry-out. 

The 4-bit parallel adder, the sum (S1) and carry-out (C1) bits given by FA1 are not valid, until after the propagation delay of FA1. Similarly, the sum S2 and carry-out (C2) bits given by FA2 are not valid until after the cumulative propagation delay of two full adders (FA1 and FA2) , and so on. At each stage ,the sum bit is not valid until after the carry bits in all the preceding stages are valid. Carry bits must propagate or ripple through all stages before the most significant sum bit is valid. Thus, the total sum (the parallel output) is not valid until after the cumulative delay of all the adders. 

The parallel adder in which the carry-out of each full-adder is the carry-in to the next most significant adder is called a ripple carry adder.. The greater the number of bits that a ripple carry adder must add, the greater the time required for it to perform a valid addition. If two numbers are added such that no carries occur between stages, then the add time is simply the propagation time through a single full-adder. 

## **4- Bit Parallel Subtractor:** 

The subtraction of binary numbers can be carried out most conveniently by means of complements , the subtraction A-B can be done by taking the 2‘s complement of B and adding it to A . The 2‘s complement can be obtained by taking the 1‘s complement and adding 1 to the least significant pair of bits. The 1‘s complement can be implemented with inverters as 

## **Binary-Adder Subtractor:** 

A 4-bit adder-subtractor, the addition and subtraction operations are combined into one circuit with one common binary adder. This is done by including an X-OR gate with each full-adder. The mode input M controls the operation. When M=0, the circuit is an adder, and when M=1, the circuit becomes a subtractor. Each X-OR gate receives input M and one of the Ped=B inputs of B. When M=0, .The full-adder receives the value of B , the input carry is 0 

35 

and the circuit performs   A+B. when BRel=B' and C1=1. The B inputs are complemented  and a 1 is through the input carry. The circuit performs the operation A plus the 2‘s complement of B. 

## **The Look-Ahead –Carry Adder:** 

In parallel-adder,the speed with which an addition can be performed is governed by the time required for the carries to propagate or ripple through all of the stages of the adder. The look-ahead carry adder speeds up the process by eliminating this ripple carry delay. It examines all the input bits simultaneously and also generates the carry-in bits for all the stages simultaneously. 

The method of speeding up the addition process is based on the two additional functions of the full-adder, called the carry generate and carry propagate functions. 

Consider one full adder stage; say the nth stage of a parallel adder as shown in fig. we know that is made by two half adders and that the half adder contains an X-OR gate to produce the sum and an AND gate to produce the carry. If both the bits An and Bn are 1s, a carry has to be generated in this stage regardless of whether the input carry Cin is a 0 or a 1. This is called generated carry, expressed as Gn= An.Bn which has to appear at the output through the OR gate as shown in fig. 

Thereis another possibility of producing a carry out. X-OR gate inside the half-adder 

at the  input   produces an intermediary sum bit- call it Pn   –which is  expressed  as . Next Pn and Cn are added using the X-OR gate inside the second half adder to produce the final 

36 

> sum bit  and 5,=P,@C, where P, =A, @B, and  output carryC0= Pn.Cn=( A @B, )Cn which becomes carry for the (n+1) thstage. 

Consider the case of both Pn and Cn being 1. The input carry Cn has to be propagated to the output only if Pn is 1. If Pn is 0, even if Cn is 1, the and gate in the second half-adder will inhibit Cn . the carry out of the nth stage is 1 when either Gn=1 or Pn.Cn =1 or both Gn and Pn.Cn are equal to 1. 

For the final sum and carry outputs of the nth stage, we get the following Boolean 

expressions. 

Observe the recursive nature of the expression for the output carry at the nth stage which becomes the input carry for the (n+1)st stage .it is possible to express the output carry of a higher significant stage is the carry-out of the previous stage. 

Based on these , the expression for the carry-outs of various full adders are as follows, 

Observe that the final output carry is expressed as a  function of the input variables in SOP form. Which is two level AND-OR or equivalent NAND-NAND form. Observe that the full look-ahead scheme requires the use of OR gate with (n+1) inputs and AND gates with number of inputs varying from 2 to (n+1). 

37 

## **2’s complement Addition and Subtraction using Parallel Adders:** 

**M** ost modern computers use the 2‘s complement system to represent negative numbers and to perform subtraction operations of signed numbers can be performed using only the addition operation ,if we use the 2‘s complement form to represent negative numbers. 

The circuit shown can perform both addition and subtraction in the 2‘s complement. This adder/subtractor circuit is controlled by the control signal ADD/SUB‘. When the ADD/SUB‘ level is HIGH, the circuit performs the addition of the numbers stored in registers A and B. When the ADD/Sub‘ level is LOW, the circuit subtract the number in register B from the number in register A. The operation is: 

When ADD/SUB‘ is a 1: 

1. AND gates 1,3,5 and 7 are enabled , allowing B0,B1,B2and B3 to pass to the OR gates 9,10,11,12 . AND gates 2,4,6 and 8 are disabled , blocking B0‘,B1‘,B2‘, and B3‘ from reaching the OR gates 9,10,11 and 12. 

2. The two levels B0 to B3 pass through the OR gates to the 4-bit parallel adder, to be added to the bits A0 to A3. The sum appears at the output S0 to S3 

3. Add/SUB‘ =1 causes no carry into the adder. 

## When ADD/SUB‘ is a 0: 

1. AND gates 1,3,5 and 7 are disabled , allowing B0,B1,B2and B3 from reaching the OR gates 9,10,11,12 . AND gates 2,4,6 and 8 are enabled , blocking B0‘,B1‘,B2‘, and B3‘ from reaching the OR gates. 

38 

2. The two levels B0‘ to B3‘ pass through the OR gates to the 4-bit parallel adder, to be added to the bits A0 to A3.The C0 is now 1.thus the number in register B is converted to its 2‘s complement form. 

3. The difference appears at the output S0 toS3. 

Adders/Subtractors used for adding and subtracting signed binary numbers. In computers , the output is transferred into the register A (accumulator) so that the result of the addition or subtraction always end up stored in the register A This is accomplished by applying a transfer pulse to the CLK inputs of register A. 

## **Serial Adder:** 

A serial adder is used to add binary numbers in serial form. The two binary numbers to be added serially are stored in two shift registers A and B. Bits are added one pair at a time through a single full adder (FA) circuit as shown. The carry out of the full-adder is transferred to a D flipflop. The output of this flip-flop is then used as the carry input for the  next  pair of significant bits. The sum bit from the S output of the full-adder could be transferred to a third shift register. By shifting the sum into A while the bits of A are shifted out, it is possible to use one register for storing both augend and the sum bits. The serial input register B can be used to transfer a new binary number while the addend bits are shifted out during the addition. 

The operation of the serial adder is: 

Initially register A holds the augend, register B holds the addend and the carry flip-flop is cleared to 0. The outputs (SO) of A and B provide a pair of significant bits for the full-adder at x and y. The shift control enables both registers and carry flip-flop , so, at the clock pulse both registers are shifted once to the right, the sum bit from S enters the left most flip-flop of A , and the output carry is transferred into flip-flop Q . The shift control enables the registers for a number of clock pulses equal to the number of bits of the registers. For each succeeding clock pulse a new sum bit is transferred to A, a new carry is transferred to Q, and both registers are shifted once to the right. This process continues until the shift control is disabled. Thus the addition is accomplished by passing each pair of bits together with the previous carry through a single full adder circuit and transferring the sum, one bit at a time, into register A. 

39 

Initially, register A and the carry flip-flop are cleared to 0 and then the first number is added from B. While B is shifted through the full adder, a second number is transferred to it through its serial input. The second number is then added to the content of register A while a third number is transferred serially into register B. This can be repeated to form the addition of two, three, or more numbers and accumulate their sum in register A. 

## **Difference between Serial and Parallel Adders:** 

The parallel adder registers with parallel load, whereas the serial adder uses shift registers. The number of full adder circuits in the parallel adder is equal to the number of bits in the binary numbers, whereas the serial adder requires only one full adder circuit and a carry flipflop. Excluding the registers, the parallel adder is a combinational circuit, whereas the serial adder is a sequential circuit. The sequential circuit in the serial adder consists of a full-adder and a flip-flop that stores the output carry. 

## **BCD Adder:** 

The BCD addition process: 

1. Add the 4-bit BCD code groups for each decimal digit position using ordinary binary addition. 

2. For those positions where the sum is 9 or less, the sum is in proper BCD form and no correction is needed. 

3. When the sum of two digits is greater than 9, a correction of 0110 should be added to that sum, to produce the proper BCD result. This will produce a carry to be added to the next decimalposition. 

A BCD adder circuit must be able to operate in accordance with the above steps. In other words, the circuit must be able to do the following: 

1. Add two 4-bit BCD code groups, usingstraight binaryaddition. 

40 

2. Determine, if the sum of this addition is greater than 1101 (decimal 9); if it is , add 0110 (decimal 6) to this sum and generate a carry to the next decimalposition. 

The first requirement is easily met by using a 4- bit binary parallel adder such as the 74LS83 IC .For example , if the two BCD code groups A3A2A1A0and B3B2B1B0 are applied to a 4-bit parallel adder, the adder will output S4S3S2S1S0 , where S4 is actually C4 , the carry –out of the MSB bits. 

The sum outputs S4S3S2S1S0 can range anywhere from 00000 to 100109when both the BCD code groups are 1001=9). The circuitry for a BCD adder must include the logic needed to detect whenever the sum is greater than 01001, so that the correction can be added in. Those cases , where the sum is greater than 1001 are listed as: 

Let us define a logic output X that will go HIGH only when the sum is greater than 01001 (i.e, for the cases in table). If examine these cases ,see that X will be HIGH for either of the following conditions: 

1. Whenever S4 =1(sum greater than15) 

2. Whenever S3 =1 and either S2 or S1 or both are 1 (sum 10 to 15) 

This condition can be expressedas 

X=S4+S3(S2+S1) 

Whenever X=1, it is necessary to add the correction factor 0110 to the sum bits, and to generate a carry. The circuit consists of three basic parts. The two BCD code groups A3A2A1A0 and B3B2B1B0 are added together in the upper 4-bit adder, to produce the sum S4S3S2S1S0. The logic gates shown implement the expression for X. The lower 4-bit adder will add the correction 0110 to the sum bits, only when X=1, producing the final BCD sum output represented by ∑3∑2∑1∑0. The X is also the carry-out that is produced when the sum is greater than 01001. When X=0, there is no carry and no addition of 0110. In such cases, ∑3∑2∑1∑0= S3S2S1S0. 

41 

Two or more BCD adders can be connected in cascade when two or more digit decimal numbers are to be added. The carry-out of the first BCD adder is connected as the carry-in of the second BCD adder, the carry-out of the second BCD adder is connected as the carry-in of the third BCD adder and so on. 

## **EXCESS-3(XS-3) ADDER:** 

To perform Excess-3 additions, 

1. Add two xs-3 codegroups 

2. If carry=1, add 0011(3) to the sum of those two codegroups 

   - If carry =0, subtract 0011(3) i.e., add 1101 (13 in decimal) to the sum of those two code groups. 

Ex: Add 9 and 5 

1100 9 in Xs-3 +1000 5 in xs-3 ___ _ _ __ 1 0100 there is a carry +0011 0011 add 3 to each group ------------------0100 0111 14 in xs-3 (1) (4) 

## **EX:** 

Implementation of xs-3 adder using 4-bit binary adders is shown. The augend (A3 A2A1A0) and addend (B3B2B1B0) in xs-3 are added using the 4-bit parallel adder. If the carry is a 1, then 0011(3) is added to the sum bits S3S2S1S0 of the upper adder in the lower 4-bit parallel 

42 

adder. If the carry is a 0, then 1101(3) is added to the sum bits (This is equivalent to subtracting 0011(3) from the sum bits. The correct sum in xs-3 is obtained 

## **Excess-3 (XS-3) Subtractor:** 

To perform Excess-3 subtraction, 

1. Complement thesubtrahend 

2. Add the complemented subtrahend to theminuend. 

3. If carry =1, result is positive. Add 3 and end around carry to the result . Ifcarry=0, the result is negative. Subtract 3, i.e, and take the 1‘s complement of the result. 

Ex: Perform 9-4 1100 9 in xs-3 +1000 Complement of 4 n Xs-3 -------(1) 0100 There is a carry +0011 Add 0011(3) -----------0111 1 End around carry -----------1000 5 in xs-3 

The minuend and the 1‘s complement of the subtrahend in xs-3 are added in the upper 4- bit parallel adder. If the carry-out from the upper adder is a 0, then 1101 is added to the sum bits of the upper adder in the lower adder and the sum bits of the lower adder are complemented to get the result. If the carry-out from the upper adder is a 1, then 3=0011 is added to the sum bits of the lower adder and the sum bits of the lower adder give the result. 

## **Binary Multipliers:** 

In binary multiplication by the paper and pencil method, is modified somewhat in digital machines because a binary adder can add only two binary numbers at a time. In a binary multiplier, instead of adding all the partial products at the end, they are added two at a time and their sum accumulated in a register (the accumulator register). In addition, when the multiplier bit is a 0,0s are not written down and added because it does not affect the final result. Instead, the multiplicand is shifted left by one bit. 

The multiplication of 1110 by 1001 using this processis Multiplicand 1110 Multiplier 1001 1110 The LSB of the multiplier is a 1; write down the multiplicand; shift the multiplicand one position to the left (1 1 1 0 0 ) 1110 The second multiplier bit is a 0; write down the previous result  1110; shift the multiplicand to the left again (1 1 1 0 0 0) 

43 

+1110000 

The fourth multiplier bit is a 1 write down the new multiplicand add it to the first partial product to obtain the final product. 

1111110 

This multiplication process can be performed by the serial multiplier circuit , which multiplies two 4-bit numbers to produce an 8-bit product. The circuit consists of following elements 

**X register** : A 4-bit shift register that stores the multiplier --- it will shift right on the falling edge of the clock. Note that 0s are shifted in from the left. 

**B register** : An 8-bit register that stores the multiplicand; it will shift left on the falling  edge of the clock. Note that 0s are shifted in from the right. 

**A register:** An 8-bit register, i.e, the accumulator that accumulates the partial products. **Adder:** An 8-bit parallel adder that produces the sum of A and B registers. The adder outputs S7 through S0 are connected to the D inputs of the accumulator so that the sum can be transferred to the accumulator only when a clock pulse gets through the AND gate. 

The circuit operation can be described by going through each step in the multiplication of 1110 by 1001. The complete process requires 4 clock cycles. 

**1. Before the first clock pulse** _:_ Prior to the occurrence of the first clock pulse, the register A is loaded with 00000000, the register B with the multiplicand 00001110, and the register X with the multiplier 1001. Assume that each of these registers is loaded using its asynchronous inputs(i.e., PRESET and CLEAR). The output of the adder will be the sum of A and B,i.e., 00001110. 

**2. First Clock pulse** _:_ Since the LSB of the multiplier (X0) is a 1, the first clock pulse gets through the AND gate and its positive going transition transfers the sum outputs into the accumulator. The subsequent negative going transition causes the X and B registers to shift right and left, respectively. This produces a new sum of A andB. 

**3. Second Clock Pulse:** The second bit of the original multiplier is now in X0 . Since this bit is a 0, the second clock pulse is inhibited from reaching the accumulator. Thus, the sum outputs are not transferred into the accumulator and the number in the accumulator does not change. The negative going transition of the clock pulse will again shift the X and B registers. Again a new sum is produced. 

**4. Third Clock Pulse** :The third bit of the original multiplier is now in X0;since this bit is a 0, the third clock pulse is inhibited from reaching the accumulator. Thus, the sum outputs are not transferred into the accumulator and the number in the accumulator does not change. The negative going transition of the clock pulse will again shift the X and B registers. Again a new sum is produced. 

**5. Fourth Clock Pulse:** The last bit of the original multiplier is now in X0 , and since it is a 1, the positive going transition of the fourth pulse transfers the sum into the accumulator. The accumulator now holds the final product. The negative going transition of the clock pulse shifts X and B again. Note that, X is now 0000, since all the multiplier bits have been shifted out. 

## **Code converters:** 

The availability of a large variety of codes for the same discrete elements of information results in the use of different codes by different digital systems. It is sometimes necessary to use the output of one system as the input to another. A conversion circuit must be 

44 

inserted between the two systems if each uses different codes for the same information. Thus a 

code converter is a logic circuit whose inputs are bit patterns representing  numbers  (or character) in one cod and whose outputs are the corresponding representation  in a different code. Code converters are usually multiple output circuits. 

To convert from binary code A to binary code B, the input lines must supply the bit combination of elements as specified by code A and the output lines must generate the corresponding bit combination of code B. A combinational circuit performs this transformation by means of logic gates. 

For example, a binary –to-gray code converter has four binary input lines B4, B3,B2,B1 and four gray code output lines G4,G3,G2,G1. When the input is 0010, for instance, the output should be 0011 and so forth. To design a code converter, we use a code table treating it as a truth table to express each output as a Boolean algebraic function of all the inputs. 

In this example, of binary –to-gray code conversion, we can treat the binary to the gray code table as four truth tables to derive expressions for G4, G3, G2, and G1. Each of these four expressions would, in general, contain all the four input variables B4, B3,B2,and B1. Thus,this code converter is actually equivalent to four logic circuits, one for each of the truth tables. 

The logic expression derived for the code converter can be simplified using the usual techniques, including ‗don‘t cares‘ if present. Even if the input is an unweighted code, the same cell numbering method which we used earlier can be used, but the cell numbers --must correspond to the input combinations as if they were an 8-4-2-1 weighted code. s 

## **Design of a 4-bit binary to gray code converter:** 

45 

## Design of a 4-bit gray to Binary code converter: 

46 

**Design of a 4-bit BCD to XS-3 code converter:** 

47 

## **Design of a BCD to gray code converter:** 

**Design of a SOP circuit to Detect the Decimal numbers 5 through 12 in a 4-bit gray code Input:** 

**Design of a SOP circuit to detect the decimal numbers 0,2,4,6,8 in a 4-bit 5211 BCD code input:** 

48 

**Design of a Combinational circuit to produce the 2’s complement of a 4-bit binary number:** 

## **Comparators:** 

49 

## **1. Magnitude Comparator:** 

## **1- bit Magnitude Comparator:** 

50 

## **4- Bit MagnitudeComparator** : 

51 

## **IC Comparator:** 

## ENCODERS: 

## **Octal to Binary Encoder:** 

Decimal to BCD Encoder: 

## **Tristate bus system:** 

In digital electronics **three-state** , **tri-state** , or **3-state** logic allows an output port to assume a high impedance state in addition to the 0 and 1 logic levels, effectively removing the output from the circuit. 

This allows multiple circuits to share the same output line or lines (such as a bus which cannot listen to more than one device at a time). 

Three-state outputs are implemented in many registers, bus drivers, and flip-flops in the 7400 and 4000 series as well as in other types, but also internally in many integrated circuits. Other typical uses are internal and external buses in microprocessors, computer memory, and peripherals. Many devices are controlled by an active-low input called OE (Output Enable)  which dictates whether the outputs should be held in a high-impedance state or drive their respective loads (to either 0- or 1- level). 

**UNIT-IV** 

## **SEQUENTIAL CIRCUITS** 

## **The Basic Latch** 

- **Basic latch** is a feedback connection of two NOR gates or two NAND gates 

- It can store one bit of information 

It can be set to 1 using the _S_ input and reset to 0 using the _R_ input 

## **The Gated Latch** 

- **Gated latch** is a basic latch that includes input gating and a control signal 

- The latch retains its existing state when the control input is equal to 0 

- Its state may be changed when the control signal is equal to 1. In our discussion we referred to 

   - the control input as the clock 

- We consider two types of gated latches: 

      - **Gated SR latch** uses the _S_ and _R_ inputs to set the latch to 1 or reset it to 0, respectively. 

      - **Gated D latch** uses the _D_ input to force the latch into a state that has the samelogic value as the _D_ input. 

## **Gated S/R Latch** 

## **Gated D Latch** 

## **Setup and Hold Times** 

- Setup Time tsu 

The minimum time that the input signal must be stable prior to the edge of the clock signal. 

- Hold Time th 

The minimum time that the input signal must be stable after the edge of the clock signal. 

## **Flip-Flops** 

- A **flip-flop** is a storage element based on the gated latch principle 

- It can have its output state changed only on the edge of the controlling clock signal 

- We consider two types: 

- **Edge-triggered flip-flop** is affected only by the input values present when theactive edge of the clock occurs 

- **Master-slave flip-flop** is built with two gatedlatches 

- The master stage is active during half of the clock cycle, and the slave stage is active 

   - during the other half. 

- The output value of the flip-flop changes on the edge of the clock that activates the transfer into the slave stage. 

## **Master-Slave D Flip-Flop** 

**A Positive-Edge-Triggered D Flip-Flop** 

## **Master-Slave D Flip-Flop with** _**Clear**_ **and** _**Preset**_ 

## **T Flip-Flop** 

**Excitation Tables** 

**Conversions of flip-flops** 

## **Sequential Circuit Design** 

- Steps in the design process for sequential circuits 

- State Diagrams and State Tables Examples 

- Steps in Design of a Sequential Circuit 

   - 1. Specification – A description of the sequential circuit. Should include a detailing of the inputs, the outputs, and the operation. Possibly assumes that you have knowledge of digital system basics. 

   - 2. Formulation: Generate a state diagram and/or a state table from the statement of the problem. 

   - 3. State Assignment: From a state table assign binary codes to thestates. 

   - 4. Flip-flop Input Equation Generation: Select the type of flip-flop for the circuit and generate the needed input for the required state transitions 

   - 5. Output Equation Generation: Derive output logic equations for generation of the output from the inputs and current state. 

   - 6. Optimization: Optimize the input and output equations. Today, CAD systems are typically used for this in real systems. 

   - 7. Technology Mapping: Generate a logic diagram of the circuit using ANDs, ORs, Inverters, and F/Fs. 

   - 8. Verification: Use a HDL to verify the design 

## **Registers and Counters** 

- An _n_ -bit register is a cascade of _n_ flip-flops and can store an _n_ -bit binary data 

- A counter can count occurrences of events and can generate timing intervals for control purposes 

## **A Simple Shift Register** 

**Parallel-Access Shift Register** 

## **Counters** 

- Counters are a specific type of sequential circuit. 

- Like registers, the state, or the flip-flop values themselves, serves as the “output.” 

- The output value increases by one on each clock cycle. 

- After the largest value, the output “wraps around” back to 0. 

- Using two bits, we’d get something like this: 

|Present State|Next State|
|---|---|
|||
|A<br>B|A<br>B|
|||
|||
|0<br>0|0<br>1|
|0<br>1|1<br>0|
|1<br>0|1<br>1|
|||
|1<br>1|0<br>0|



## **Benefits of counters** 

- Counters can act as simple clocks to keep track of “time.” • 

   - You may need to record how many times something has 

happened. 

   - How many bits have been sent or received? 

   - How many steps have been performed in some computation? 

- All processors contain a program counter, or PC. 

   - Programs consist of a list of instructions that are to be executed one after another (for the most part). 

   - The PC keeps track of the instruction currently being executed. 

   - The PC increments once on each clock cycle, and the next program instruction is then executed. 

## **A Three-Bit Up-Counter** 

Q1 is connected to clk, Q2 and Q3 are clocked by Q’ of the preceding stage (hence called asynchronous or ripple counter 

\ 

## **A Three-Bit Down-Counter** 

## **Shift registers:** 

In digital circuits, a **shift register** is a cascade of flip-flops sharing the same clock, in which the output of each flip-flop is connected to the "data" input of the next flip-flop in the chain, resulting in a circuit that shifts by one position the "bit array" stored in it, _shifting in_ the data present at its input and _shifting out_ the last bit in the array, at each transition of the clock input. More generally, a **shift register** may be multidimensional, such that its "data in" and stage outputs are themselves bit arrays: this is implemented simply by running several shift registers of the same bit-length in parallel. 

Shift registers can have both parallel and serial inputs and outputs.  These are often configured as **serial-in, parallel-out** (SIPO) or as **parallel-in, serial-out** (PISO). There are also types that have both serial and parallel input and types with serial and parallel output. There are also **bidirectional** shift registers which allow shifting in both directions: L→R or R→L. The serial input and last output of a shift register can also be connected to create a **circular shift register** 

Shift registers are a type of logic circuits closely related to counters. They are basically for the storage and transfer of digital data. 

## **Buffer register:** 

The buffer register is the simple set of registers. It is simply stores the binary word. The buffer may be controlled buffer. Most of the buffer registers used D Flip-flops. 

## **Figure: logic diagram of 4-bit buffer register** 

The figure shows a 4-bit buffer register. The binary word to be stored is applied to the data terminals. On the application of clock pulse, the output word becomes the same as the word applied at the terminals. i.e., the input word is loaded into the register by the application of clock pulse. 

When the positive clock edge arrives, the stored word becomes: 

Q4Q3Q2Q1=X4X3X2X1 

Q=X 

## **Controlled buffer register:** 

If goes LOW, all the FFs are RESET and the output becomes, Q=0000. 

When is HIGH, the register is ready for action. LOAD is the control input. When LOAD is HIGH, the data bits X can reach the D inputs of FF‘s. 

Q4Q3Q2Q1=X4X3X2X1 

Q=X 

When load is low, the X bits cannot reach the FF‘s. 

## **Data transmission in shift registers:** 

A number of ff‘s connected together such that data may be shifted into and shifted out of them is called shift register. data may be shifted into or out of the register in serial form or in parallel form. There are four basic types of shift registers. 

1. Serial in, serial out, shift right, shift registers 

2. Serial in, serial out, shift left, shift registers 

3. Parallel in, serial out shift registers 

4. Parallel in, parallel out shift registers 

## **Serial IN, serial OUT, shift right, shift left register:** 

The logic diagram of 4-bit serial in serial out, right shift register with four stages. The register can store four bits of data. Serial data is applied at the input D of the first FF. the Q output of the first FF is connected to the D input of another FF. the data is outputted from the Q terminal  of the last FF. 

When serial data is transferred into a register, each new bit is clocked into the first FF at the positive going edge of each clock pulse. The bit that was previously stored by the first FF is transferred to the second FF. the bit that was stored by the Second FF is transferred to the third FF. 

## **Serial-in, parallel-out, shift register:** 

In this type of register, the data bits are entered into the register serially, but the data stored in the register is shifted out in parallel form. 

Once the data bits are stored, each bit appears on its respective output line and all bits are available simultaneously, rather than on a bit-by-bit basis with the serial output. The serial-in, parallel out, shift register can be used as serial-in, serial out, shift register if the output is taken from the Q terminal of the last FF. 

## **Parallel-in, serial-out, shift register:** 

For a parallel-in, serial out, shift register, the data bits are entered simultaneously into their respective stages on parallel lines, rather than on a bit-by-bit basis on one line as with serial data bits are transferred out of the register serially. On a bit-by-bit basis over a single line. 

There are four data lines A,B,C,D through which the data is entered into the register in parallel form. The signal shift/ load allows the data to be entered in parallel form into the register and the data is shifted out serially from terminalQ4 

## **Parallel-in, parallel-out, shift register** 

In a parallel-in, parallel-out shift register, the data is entered into the register in parallel form, and also the data is taken out of the register in parallel form. Data is applied to the D input terminals of the FF‘s. When a clock pulse is applied, at the positive going edge of the pulse, the D inputs are shifted into the Q outputs of the FFs. The register now stores the data. The stored data is available instantaneously for shifting out in parallel form. 

## **Bidirectional shift register:** 

A bidirectional shift register is one which the data bits can be shifted from left to right or from right to left. A fig shows the logic diagram of a 4-bit serial-in, serial out, bidirectional shift register. Right/left is the mode signal, when right /left is a 1, the logic circuit works as a shift-register.the bidirectional operation is achieved by using the mode signal and two NAND gates and one OR gate for each stage. 

A HIGH on the right/left control input enables the AND gates G1, G2, G3 and G4 and disables the AND gates G5,G6,G7 and G8, and the state of Q output of each FF is passed through the gate to the D input of the following FF. when a clock pulse occurs, the data bits are then effectively shifted one place to the right. A LOW on the right/left control inputs enables the AND gates G5, G6, G7 and G8 and disables the And gates G1, G2, G3 and G4 and the Q output of each FF is passed to the D input of the preceding FF. when a clock pulse occurs, the data bits are then effectively shifted one place to the left. Hence, the circuit works as a bidirectional shift register 

## **Figure: logic diagram of a 4-bit bidirectional shift register** 

## **Universal shift register:** 

A register is capable of shifting in one direction only is a unidirectional shift register. One that can shift both directions is a bidirectional shift register. If the register has both shifts and parallel load capabilities, it is referred to as a universal shift registers. Universal shift register is a bidirectional register, whose input can be either in serial form or in parallel form and whose output also can be in serial form or I parallel form. 

The most general shift register has the following capabilities. 

1. A clear control to clear the register to 0 

2. A clock input to synchronize the operations 

3. A shift-right control to enable the shift-right operation and serial input and output lines associated with the shift-right 

4. A shift-left control to enable the shift-left operation and serial input and output lines associated with the shift-left 

5. A parallel loads control to enable a parallel transfer and the n input lines associated with the parallel transfer 

6. N parallel output lines 

7. A control state that leaves the information in the register unchanged in the presence of the clock. 

A universal shift register can be realized using multiplexers. The below fig shows the logic diagram of a 4-bit universal shift register that has all capabilities. It consists of 4 D flip-flops and four multiplexers. The four multiplexers have two common selection inputs s1 and s0. Input 0 in each multiplexer is selected when S1S0=00, input 1 is selected when S1S0=01 and input 2 is selected when S1S0=10 and input 4 is selected when S1S0=11. The selection inputs control the mode of operation of the register according to the functions entries. When S1S0=0, the present value of the register is applied to the D inputs of flip-flops. The condition forms a path from the output of each flip-flop into the input of the same flip-flop. The next clock edge transfers into each flip-flop the binary value it held previously, and no change of state occurs. When S1S0=01, terminal 1 of the multiplexer inputs have a path to the D inputs of the flip-flop. This causes a shift-right operation, with serial input transferred into flip-flopA4. When S1S0=10, a shift left operation results with the other serial input going into flip-flop A1. Finally when S1S0=11, the binary information on the parallel input lines is transferred into the register simultaneously during the next clock cycle 

**Figure: logic diagram 4-bit universal shift register** 

## **Function table for theregister** 

|**mode control**|**mode control**|**mode control**|
|---|---|---|
|**S0 S1 re**|**S0 S1 re**|**S0 S1 register operation**|
||||
|0|0|No change|
|0|1|Shift Right|
|1|0|Shift left|
|1|1|Parallel load|



## **Counters:** 

**Counter** is  a  device  which  stores  (and  sometimes  displays)  the  number  of  times particular event or process has occurred, often in relationship to a clock signal. A Digital counter is a set of flip flops whose state change in response to pulses applied at the input to the counter. Counters may be asynchronous counters or synchronous counters. Asynchronous counters are also called ripple counters 

In electronics counters can be implemented quite easily using register-type circuits  such  as the flip-flops and a wide variety of classifications exist: 

- Asynchronous (ripple) counter – changing state bits are used as clocks to subsequent state flip-flops 

- Synchronous counter – all state bits change under control of a singleclock 

- Decade counter – counts through ten states per stage 

- Up/down counter – counts both up and down, under command of a control input 

- Ring counter – formed by a shift register with feedback connection in a ring 

- Johnson counter – a _twisted_ ring counter 

- Cascaded counter Modulus counter. 

Each is useful for different applications. Usually, counter circuits are digital in nature, and count in natural binary Many types of counter circuits are available as digital building blocks, for example a number of chips in the 4000 series implement different counters. 

Occasionally there are advantages to using a counting sequence other than the natural binary sequence such as the binary coded decimal counter, a linear feed-back shift  register counter, or a gray-code counter. 

Counters are useful for digital clocks and timers, and in oven timers, VCR clocks, etc. 

## **Asynchronous counters:** 

An asynchronous (ripple) counter is a single JK-type flip-flop, with its J (data) input fed from its own inverted output. This circuit can store one bit, and hence can count from zero to one before it overflows (starts over from 0). This counter will increment once for every clock cycle and takes two clock cycles to overflow, so every cycle it will alternate between a transition from 0 to 1 and a transition from 1 to 0. Notice that this creates a new clock with a 50% duty cycle at exactly half the frequency of the input clock. If this output is then used as the clock signal for a similarly arranged D flip-flop (remembering to invert the output to the input), one will get another 1 bit counter that counts half as fast. Putting them together yields a two-bit counter: 

## **Two-bit ripple up-counter using negative edge triggered flip flop:** 

Two bit ripple counter used two flip-flops. There are four possible states from 2 – bit upcounting I.e. 00, 01, 10 and 11. 

· The counter is initially assumed to be at a state 00 where the outputs of the tow flip-flops are noted as Q1Q0. Where Q1 forms the MSB and Q0 forms the LSB. 

· For the negative edge of the first clock pulse, output of the first flip-flop FF1 toggles its state. Thus Q1 remains at 0 and Q0 toggles to 1 and the counter state are now read as 01. 

· During the next negative edge of the input clock pulse FF1 toggles and Q0 = 0. The output Q0 being a clock signal for the second flip-flop FF2 and the present transition acts as a negative edge for FF2 thus toggles its state Q1 = 1. The counter state is now read as 10. 

· For the next negative edge of the input clock to FF1 output Q0 toggles to 1. But this transition from 0 to 1 being a positive edge for FF2 output Q1 remains at 1. The counter state is now read as 11. 

· For the next negative edge of the input clock, Q0 toggles to 0. This transition from 1 to 0 acts as a negative edge clock for FF2 and its output Q1 toggles to 0. Thus the starting state 00 is attained. Figure shown below 

**Two-bit ripple down-counter using negative edge triggered flip flop:** 

A 2-bit down-counter counts in the order 0,3,2,1,0,1…….,i.e, 00,11,10,01,00,11 …..,etc. the above fig. shows ripple down counter, using negative edge triggered J-K FFs and its timing diagram. 

- For down counting, Q1‘ of FF1 is connected to the clock of Ff2. Let initially all the FF1 toggles, so, Q1 goes from a 0 to a 1 and Q1‘ goes from a 1 to a 0. 

- The negative-going signal at Q1‘ is applied to the clock input of FF2, toggles Ff2 and, therefore, Q2 goes from a 0 to a 1.so, after one clock pulse Q2=1 and Q1=1, I.e., the state of the counter is 11. 

- At the negative-going edge of the second clock pulse, Q1 changes from a 1 to a 0 and Q1‘ from a 0 to a 1. 

- This positive-going signal at Q1‘ does not affect FF2 and, therefore, Q2 remains at a 1. Hence , the state of the counter after second clock pulse is 10 

- At the negative going edge of the third clock pulse, FF1 toggles. So Q1, goes from a 0 to a 1 and Q1‘ from 1 to 0. This negative going signal at Q1‘ toggles FF2 and, so, Q2 changes from 1 to 0, hence, the state of the counter after the third clock pulse is 01. 

- At the negative going edge of the fourth clock pulse, FF1 toggles. So Q1, goes from a 1 to a 0 and Q1‘ from 0 to 1. . This positive going signal at Q1‘ does not affect FF2 and, so, Q2 remains at 0, hence, the state of the counter after the fourth clock pulse is 00. 

## **Two-bit ripple up-down counter using negative edge triggered flip flop:** 

## **Figure: asynchronous 2-bit ripple up-down counter using negative edge triggered flip flop:** 

- As the name indicates an up-down counter is a counter which can count both in upward and downward directions. An up-down counter is also called a forward/backward counter or a bidirectional counter. So, a control signal or a mode signal M is required to choose the direction of count. When M=1 for up counting, Q1 is transmitted to clock of FF2 and when M=0 for down counting, Q1‘ is transmitted to clock of FF2. This is achieved by using two AND gates and one OR gates. The external clock signal is applied to FF1. 

- Clock signal to FF2= (Q1.Up)+(Q1‘. Down)= Q1m+Q1‘M‘ 

## **Design of Asynchronous counters:** 

To design a asynchronous counter, first we write the sequence , then tabulate the values of reset signal R for various states of the counter and obtain the minimal expression for R and R‘ using K-Map or any other method. Provide a feedback such that R and R‘ resets all the FF‘s after the desired count 

## **Design of a Mod-6 asynchronous counter using T FFs:** 

A mod-6 counter has six stable states 000, 001, 010, 011, 100, and 101. When the sixth clock pulse is applied, the counter temporarily goes to 110 state, but immediately resets to 000 because  of the  feedback  provided.  it  is ―divide  by-6-counter‖,  in the  sense  that  it  divides  the input clock frequency by 6.it requires three FFs, because the smallest value of n satisfying the conditionN≤2[n] is n=3; three FFs can have 8 possible states, out of which only six are utilized and the remaining two states 110and 111, are invalid. If initially the counter is in 000 state, then after the sixth clock pulse, it goes to 001, after the second clock pulse, it goes to 010, and so on. 

**After s** ixth clock pulse it goes to 000. For the design, write the truth table with present state outputs Q3, Q2 and Q1 as the variables, and reset R as the output and obtain an expression for R in terms of Q3, Q2, and Q1that decides the feedback into be provided. From the truth table, R=Q3Q2. For active-low Reset, R‘ is used. The reset pulse is of very short duration, of the order of nanoseconds and it is equal to the propagation delay time of the NAND gate used. The expression for R can also be determined as follows. 

R=0 for 000 to 101, R=1 for 110, and R=X=for111 

Therefore, 

R=Q3Q2Q1‘+Q3Q2Q1=Q3Q2 

The logic diagram and timing diagram of Mod-6 counter is shown in the above fig. 

The truth table is as shown in below. 

|After|States|States|||
|---|---|---|---|---|
|pulses|Q3|Q2|Q1|R|
|0|0|0|0|0|
|1|0|0|1|0|
|2|0|1|0|0|
|3|0|1|1|0|
|4|1|0|0|0|
|5|1|0|1|0|
|6|1|1|0|1|
||0|0|0|0|
|7|0|0|0|0|



## **Design of a mod-10 asynchronous counter using T-flip-flops:** 

A mod-10 counter is a decade counter. It also called a BCD counter or a divide-by-10 counter. It requires four flip-flops (condition 10 ≤2[n] is n=4). So, there are 16 possible states, out of which ten are valid and remaining six are invalid. The counter has ten stable state, 0000 through 1001, i.e., it counts from 0 to 9. The initial state is 0000 and after nine clock pulses it goes to 1001. When the tenth clock pulse is applied, the counter goes to state 1010 temporarily, but because of the feedback provided, it resets to initial state 0000. So, there will be a glitch in the waveform of Q2. The state 1010 is a temporary state for which the reset signal R=1, R=0 for 0000 to 1001, and R=C for 1011 to 1111. 

The count table and the K-Map for reset are shown in fig. from the K-Map R=Q4Q2. So, feedback is provided from second and fourth FFs. For active –HIGH reset, Q4Q2 is applied to the clear terminal. For active-LOW reset 4 2 is connected isof all Flip=flops. 

|After|Count|Count|||
|---|---|---|---|---|
|pulses|Q4|Q3|Q2|Q1|
|0|0|0|0|0|
|1|0|0|0|1|
|2|0|0|1|0|
|3|0|0|1|1|
|4<br>5|0<br>0|1<br>0|0<br>0|0<br>1|
|6|0|1|1|0|
|7|0|1|1|1|
|8|1|0|0|0|
|9|0|1|0|1|
|10|0|0|0|0|



## **Synchronous counters:** 

Asynchronous counters are serial counters. They are slow because each FF can change state only if all the preceding FFs have changed their state. if the clock frequency is very high, the asynchronous counter may skip some of the states. This problem is overcome in synchronous counters or parallel counters. Synchronous counters are counters in which all the flip flops are triggered simultaneously by the clock pulses Synchronous counters have a common clock pulse applied simultaneously to all flipflops.) A 2 -Bit Synchronous Binary Counter 

## **Design of synchronous counters:** 

For a systematic design of synchronous counters. The following procedure is used. 

**Step 1:** State Diagram: draw the state diagram showing all the possible states state diagram which also be called nth transition diagrams, is a graphical means of depicting the sequence of states through which the counter progresses. 

**Step2:** number of flip-flops: based on the description of the problem, determine the required number n of the flip-flops- the smallest value of n is such that the number of states N≤2[n] --- and the desired counting sequence. 

**Step3:** choice of flip-flops excitation table: select the type of flip-flop to be used and write the excitation table. An excitation table is a table that lists the present state (ps) , the next state(ns) and required excitations. 

**Step4** : minimal expressions for excitations: obtain the minimal expressions for the excitations of the FF using K-maps drawn for the excitation of the flip-flops in terms of the present states and inputs. 

**Step5** : logic diagram: draw a logic diagram based on the minimal expressions 

## **Design of a synchronous 3-bit up-down counter using JK flip-flops:** 

**Step1:** determine the number of flip-flops required. A 3-bit counter requires three FFs. It has 8 states (000,001,010,011,101,110,111) and all the states are valid. Hence no don‘t cares. For selecting up and down modes, a control or mode signal M is required. When the mode signal M=1 and counts down when M=0. The clock signal is applied to all the FFs simultaneously. 

**Step2:** draw the state diagrams: the state diagram of the 3-bit up-down counter is drawn as 

**Step3:** select the type of flip flop and draw the excitation table: JK flip-flops are selected and the excitation table of a 3-bit up-down counter using JK flip-flops is drawn as shown in fig. 

|PS|||mode|NS|||required excitations|required excitations|required excitations|required excitations|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Q3|Q2|Q1|M|Q3|Q2|Q1|J3|K3|J2|K2|J1|K1|
|0|0|0|0|1|1|1|1|x|1|x|1|x|
|0|0|0|1|0|0|1|0|x|0|x|1|x|
|0|0|1|0|0|0|0|0|x|0|x|x|1|
|0|0|1|1|0|1|0|0|x|1|x|x|1|
|0|1|0|0|0|0|1|0|x|x|1|1|x|
|0|1|0|1|0|1|1|0|x|x|0|1|x|
|0|1|1|0|0|1|0|0|x|x|0|x|1|
|0|1|1|1|1|0|0|1|x|x|1|x|1|
|1|0|0|0|0|1|1|x|1|1|x|1|x|
|1|0|0|1|1|0|1|x|0|0|x|1|x|
|1|0|1|0|1|0|0|x|0|0|x|x|1|
|1|0|1|1|1|1|0|x|0|1|x|x|1|
|1|1|0|0|1|0|1|x|0|x|1|1|x|
|1|1|0|1|1|1|1|x|0|x|0|1|x|
|1|1|1|0|1|1|0|x|0|x|0|x|1|
|1|1|1|1|0|0|0|x|1|x|1|x|1|



**Step4:** obtain the minimal expressions: From the excitation table we can conclude that J1=1 and K1=1, because all the entries for J1and K1 are either X or 1. The K-maps for J3, K3,J2 and K2 based on the excitation table and the minimal expression obtained from them are shown in fig. 

**==> picture [154 x 85] intentionally omitted <==**

**----- Start of picture text -----**<br>
00 01  11  10<br>Q3Q2  Q1M<br>1<br>1<br>X<br>X X X<br>X X X X<br>**----- End of picture text -----**<br>


**Step5:** draw the logic diagram: a logic diagram using those minimal expressions can be drawn as shown in fig. 

## **Design of a synchronous modulo-6 gray cod counter:** 

**Step 1:** the number of flip-flops: we know that the counting sequence for a modulo-6 gray code counter is 000, 001, 011, 010, 110, and 111. It requires n=3FFs (N≤2[n] , i.e., 6≤2[3] ). 3 FFs can have 8 states. So the remaining two states 101 and 100 are invalid. The entries for excitation corresponding to invalid states are don‘t cares. 

**Step2:** the state diagram: the state diagram of the mod-6 gray code converter is drawn as shown in fig. 

**Step3:** type of flip-flop and the excitation table: T flip-flops are selected and the excitation table of the mod-6 gray code counter using T-flip-flops is written as shown in fig. 

|**PS**|**PS**||**NS**|**NS**||**required**<br>**excitations**|**required**<br>**excitations**|**required**<br>**excitations**|
|---|---|---|---|---|---|---|---|---|
|**Q3 **|**Q2 **|**Q1 **|**Q3 **|**Q2 **|**Q1 **|**T3**|**T2**|**T1**|
|0|0|0|0|0|1|0|0|1|
|0|0|1|0|1|1|0|1|0|
|0|1|1|0|1|0|0|0|1|
|0|1|0|1|1|0|1|0|0|
|1|1|0|1|1|1|0|0|1|
|1|1|1|0|0|0|1|1|1|



**Step4:** The minimal expressions: the K-maps for excitations of FFs T3,T2,and T1 in terms of outputs of FFs Q3,Q2, and Q1, their minimization and the minimal expressions for excitations obtained from them are shown if fig 

**Step5:** the logic diagram: the logic diagram based on those minimal expressions is drawn as shown in fig. 

## **Design of a synchronous BCD Up-Down counter using FFs:** 

**Step1:** the number of flip-flops: a BCD counter is a mod-10 counter has 10 states (0000 through 1001) and so it requires n=4FFs(N≤2[n] ,, i.e., 10≤2[4] ). 4 FFS can have 16 states. So out of 16 states, six states (1010 through 1111) are invalid. For selecting up and down mode, a control or mode signal M is required. , it counts up when M=1 and counts down when M=0. The clock signal is applied to all FFs. 

**Step2:** the state diagram: The state diagram of the mod-10 up-down counter is drawn as shown in fig. 

**Step3:** types of flip-flops and excitation table: T flip-flops are selected and the excitation table of the modulo-10 up down counter using T flip-flops is drawn as shown in fig. 

The remaining minterms are don‘t cares(∑d(20,21,22,23,24,25,26,37,28,29,30,31)) from the excitation table we can see that T1=1 and the expression for T4,T3,T2 are asfollows. T4=∑m(0,15,16,19)+d(20,21,22,23,24,25,26,27,28,29,30,31) T3=∑m(7,15,16,8)+d(20,21,22,23,24,25,26,27,28,29,30,31) T2=∑m(3,4,7,8,11,12,15,16)+d(20,21,22,23,24,25,26,27,28,29,30,31) 

|**PS**||||**mode**|**NS**||||**required excitations**|**required excitations**|**required excitations**|**required excitations**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Q4 **|**Q3 **|**Q2 **|**Q1 **|**M**|**Q4 **|**Q3 **|**Q2 **|**Q1 **|**T4**|**T3**|**T2**|**T1**|
|0|0|0|0|0|1|0|0|1|1|0|0|1|
|0|0|0|0|1|0|0|0|1|0|0|0|1|
|0|0|0|1|0|0|0|0|0|0|0|0|1|
|0|0|0|1|1|0|0|1|0|0|0|1|1|
|0|0|1|0|0|0|0|0|1|0|0|1|1|
|0|0|1|0|1|0|0|1|1|0|0|0|1|
|0|0|1|1|0|0|0|1|0|0|0|0|1|
|0|0|1|1|1|0|1|0|0|0|1|1|1|
|0|1|0|0|0|0|0|1|1|0|1|1|1|
|0|1|0|0|1|0|1|0|1|0|0|0|1|
|0|1|0|1|0|0|1|0|0|0|0|0|1|
|0|1|0|1|1|0|1|1|0|0|0|1|1|
|0|1|1|0|0|0|1|0|1|0|0|1|1|
|0|1|1|0|1|0|1|1|1|0|0|0|1|
|0|1|1|1|0|0|1|1|0|0|0|0|1|
|0|1|1|1|1|1|0|0|0|1|1|1|1|
|1|0|0|0|0|0|1|1|1|1|1|1|1|
|1|0|0|0|1|1|0|0|1|0|0|0|1|
|1|0|0|1|0|1|0|0|0|0|0|0|1|
|1|0|0|1|1|0|0|0|0|1|0|0|1|



**Step4:** The minimal expression: since there are 4 state variables and a mode signal, we require 5 variable kmaps. 20 conditions of Q4Q3Q2Q1M are valid and the remaining 12 combinations are invalid. So the entries for excitations corresponding to those invalid combinations are don‘t cares. Minimizing K-maps for T2 we get 

T 2= Q4Q1‘M+Q4‘Q1M+Q2Q1‘M‘+Q3Q1‘M‘ 

**Step5:** the logic diagram: the logic diagram based on the above equation is shown in fig. 

## **Shift register counters:** 

One of the applications of shift register is that they can be arranged to form several types of counters. The most widely used shift register counter is ring counter as well as the twisted ring counter. 

**Ring counter:** this is the simplest shift register counter. The basic ring counter using D flipflops is shown in fig. the realization of this counter using JK FFs. The Q output of each stage is connected to the D flip-flop connected back to the ring counter. 

**FIGURE: logic diagram of 4-bit ring counter using D flip-flops** 

Only a single 1 is in the register and is made to circulate around the register as long as clock pulses are applied. Initially the first FF is present to a 1. So, the initial state is 1000, i.e., Q1=1, Q2=0,Q3=0,Q4=0. After each clock pulse, the contents of the register are shifted to the right by one bit and Q4 is shifted back to Q1. The sequence repeats after four clock pulses. The number 

of distinct states in the ring counter, i.e., the mod of the ring counter is equal to number of FFs used in the counter. An n-bit ring counter can count only n bits, where as n-bit ripple counter can count 2[n] bits. So, the ring counter is uneconomical compared to a ripple counter but has advantage of requiring no decoder, since we can read the count by simply noting which FF is set. Since it is entirely a synchronous operation and requires no gates external FFs, it has the further advantage of being very fast. 

## **Timing diagram:** 

## **Twisted Ring counter (Johnson counter):** 

This counter is obtained from a serial-in, serial-out shift register by providing feedback from the inverted output of the last FF to the D input of the first FF. the Q output of each is connected to the D input of the next stage, but the Q‘ output of the last stage is connected to the D input of the first stage, therefore, the name twisted ring counter. This feedback arrangement produces a unique sequence of states. 

The logic diagram of a 4-bit Johnson counter using D FF is shown in fig. the realization of the same using J-K FFs is shown in fig.. The state diagram and the sequence table are shown in figure. The timing diagram of a Johnson counter is shown in figure. 

Let initially all the FFs be reset, i.e., the state of the counter be 0000. After each clock pulse, the level of Q1 is shifted to Q2, the level of Q2to Q3, Q3 to Q4 and the level of Q4‘to Q1 and the sequences given in fig. 

Figure: Johnson counter with JK flip-flops 

**==> picture [115 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
Figure: timing diagram<br>**----- End of picture text -----**<br>


## **UNIT- V** 

## **MEMORY** 

Memory structures are crucial in digital design. – ROM, PROM, EPROM, RAM, SRAM, (S)DRAM, RDRAM,.. 

- ➢ All memory structures have an address bus and a data bus – Possibly other control signals to control output etc. •E.g. 4 Bit Address bus with 5 Bit Data Bus ADDR DOUT 

There are two types of memories that are used in digital systems: 

- Random-access memory(RAM): perform both the write and read operations. 

`o` Read-only memory(ROM): perform only the read operation. 

The read-only memory is a programmable logic device. Other such units are the programmablelogic array(PLA), the programmable array logic(PAL), and the field-programmable gatearray(FPGA). 

## Random-Access Memory: 

A memory unit stores binary information in groups of bits called words. 

• byte = 8 bits 

• word = 2 bytes 

The communication between a memory and its environment is achieved through data input andoutput lines, address selection lines, and control lines that specify the direction oftransfer. 

In random-access memory, the word locations may be thought of as being separated in space, with each word occupying one particular location. 

In sequential-access memory, the information stored in some medium is not immediately accessible, but is available only certain intervals of time. A magnetic disk or tape unit is of this type. 

In a random-access memory, the access time is always the same regardless of the particular locationof the word. 

~~In a sequential-access memory, the time it takes to access a word depends on the position of the word~~ with respect to the reading head position; therefore, theaccess time is variable. 

## **Static RAM** 

SRAM consists essentially of internal latches that store the binaryinformation. 

The stored information remains valid as long as power is applied to the unit. 

SRAM is easier to use and has shorter read and write cycles. 

Low density, low capacity, high cost, high speed, high power consumption. 

## **Dynamic RAM** 

DRAM stores the binary information in the form of electric charges oncapacitors. 

The capacitors are provided inside the chip by MOS transistors. 

The capacitors tends to discharge with time and must be periodically recharged by refreshing the dynamic memory. 

DRAM offers reduced power consumption and larger storage capacity in a single memorychip. High density, high capacity, low cost, low speed, low power consumption. 

Memory decoding 

The equivalent logic of a binary cell that stores one bit of information is shown below. 

- Read/Write = 0, select = 1, input data to S-R latch 

- Read/Write = 1, select = 1, output data from S-R latch 

## Programmable Logic Array: 

   - The decoder in PROM is replaced by an array of AND gates that can be programmed to generate any product term of the input variables. 

   - The product terms are then connected to OR gates to provide the sum of products forthe required Boolean functions. 

- ➢ The output is inverted when the XOR input is connected to 1 (since x⊕1 = x’). The output 

   - doesn’t change and connect to 0 (since x⊕0 = x). 

## F1 = 

## AB’+AC+A’BC’ 

## F2 = (AC+BC)’ 

## **Implement the following two Boolean functions with a PLA:** 

- **F1(A, B, C) = ∑(0, 1, 2, 4)** 

- **F2(A, B, C) = ∑(0, 5, 6, 7)** 

= Both the true and complement of the functions are simplified in sum of products. 

=m 

We can find the same terms from the group terms of the functions of F,, F4’,F5 and F,’ which will make the minimum terms. 

Fl = (AB + AC + BC)’ F2 = AB+AC+A’B’C’ 

## PLA programmingtable 

||||Outputs|Outputs|
|---|---|---|---|---|
||Product|Inputs|(c)|(T)|
|AB|1|11<br>-|1|1|
|AC|2|1-1|1|1|
|BC|3|—~<br>11|1|-|
|ARC|4|00<br>0|-|1|



Fig. 7-15 Solution toExample7-2 

A— 

s—{3 

oe efHT By CCBBAA' | oe _s} Dr 

