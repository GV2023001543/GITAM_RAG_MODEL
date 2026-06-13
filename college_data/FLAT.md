## **DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING** 

## **DIGITAL NOTES** 

**ON** 

# **FORMAL LANGUAGES AND AUTOMATA THEORY** 

**R22A0510** 

**B.TECH IIYEAR–II SEM (R22) REGULATION** 

**(2023-24)** 

**Prepared by K.CHANDUSHA** 

**MALLAREDDY COLLEGE OF ENGINEERING &TECHNOLOGY (AutonomousInstitution–UGC,Govt.ofIndia)** Recognizedunder2(f)and12(B) ofUGC ACT1956 

(AffiliatedtoJNTUH,Hyderabad,ApprovedbyAICTE-AccreditedbyNBA&NAAC–‘A’GradeISO9001:2015Certified) 

Maisammaguda,Dhulapally(PostVia.Hakimpet),Secunderabad–500100,TelanganaState,India 

## **MALLA REDDY COLLEGE OF ENGINEERING & TECHNOLOGY** 

## **DEPARTMENT OF INFORMATION TECHNOLOGY** 

**II Year B.Tech IT – II Sem                                                                                            L    T /P/D    C** 

## **(R15A0506)FORMAL LANGUAGES AND AUTOMATA THEORY** 

## **Objectives:** 

- To teach the student to identify different formal language classes and their relationships 

- To teach the student the theoretical foundation for designing compilers. 

- To teach the student to use the ability of applying logical skills. 

- Teach the student to prove or disprove theorems in automata theory using its properties 

- To teach the student the techniques for information processing. 

- Understand the theory behind engineering applications. 

## **UNIT I:** 

**Fundamentals:** Strings, Alphabet, Language, Operations, Finite state machine, definitions, finite automaton model, acceptance of strings, and languages, FA, transition diagrams and Language recognizers. 

**Finite Automata:** Deterministic finite automaton, Non deterministic finite automaton and NFA with Є transitions - Significance, acceptance of languages. Conversions and Equivalence : Equivalence between NFA with and without Є transitions, NFA to DFA conversion, minimization of FSM, equivalence between two FSMs, Finite Automata with output- Moore and Melay machines. 

## **UNIT II:** 

**Regular Languages:** Regular sets, regular expressions, identity rules, Conversion finite Automata for a given regular expressions, Conversion of Finite Automata to Regular expressions. Pumping lemma of regular sets, closure properties of regular sets **(proofs not required).** 

## **UNIT III:** 

**Grammar Formalism:** Regular grammars-right linear and left linear grammars, equivalence between regular linear grammar and FA, inter conversion, Context free grammar, derivation trees, sentential forms. Right most and leftmost derivation of strings. 

**Context Free Grammars:** Ambiguity in context free grammars. Minimisation of Context Free Grammars. Chomsky normal form, Greibach normal form, Pumping Lemma for Context Free Languages. Enumeration of properties of CFL **(proofs omitted).** 

## **UNIT IV:** 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 2 

**Push Down Automata:** Push down automata, definition, model, acceptance of CFL, Acceptance by final state and acceptance by empty state and its equivalence. Equivalence of CFL and PDA, interconversion. **(Proofs not required)** . Introduction to DCFL and DPDA. LINEAR BOUNDED AUTOMATA(LBA):LBA,context sensitive grammars ,CS languages 

## **UNIT V:** 

**Turing Machine:** Turing Machine, definition, model, design of TM, Computable functions, recursively enumerable languages. Church’s hypothesis, counter machine, types of Turing machines (proofs not required). 

**Computability Theory:** Chomsky hierarchy of languages, linear bounded automata and context sensitive language, LR(0) grammar, decidability of, problems, Universal Turing Machine, undecidability of posts. Correspondence problem, Turing reducibility, Definition of P and NP problems, NP complete and NP hard problems. 

## **TEXT BOOKS:** 

1. “Introduction to Automata Theory Languages and Computation”. Hopcroft H.E. and Ullman J. D.  Pearson Education. 

2. Introduction to Theory of Computation - Sipser 2nd edition Thomson 

## **REFERENCE BOOKS:** 

1.  Introduction to Computer Theory, Daniel I.A. Cohen, John Wiley. 

2.  Introduction to languages and the Theory of Computation ,John C Martin, TMH 

3.  “Elements of Theory of Computation”, Lewis H.P. & Papadimition C.H. Pearson /PHI. 

4. Theory of Computer Science and Automata languages and computation -Mishra and Chandrashekaran, 2nd edition, PHI. 

5. Theory of Computation, By K.V.N. Sunitha and N.Kalyani 

## **Course Outcomes:** 

Student will have the ability to 

- Apply knowledge in designing or enhancing compilers. 

- Design grammars and automata (recognizers) for different language classes. 

- Apply knowledge in developing tools for language processing or text processing. 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 3 

## **MALLA REDDY COLLEGE OF ENGINEERING & TECHNOLOGY DEPARTMENT OF INFORMATION TECHNOLOGY** 

## **INDEX** 

|**S. No**|**Unit**|**Topic**|**Page no**|
|---|---|---|---|
|1|I|Strings, Alphabet, Language, Operations|6-9|
|2||Finite state machine,|10-15|
|3||Finite Automata: DFA**,**NFA,WithЄtransitions|16-21|
|4||Conversions and Equivalence :|22-27|
|5||NFA to DFA conversion, minimization of FSM,<br>equivalence between two FSMs|28-32|
|6||Finite Automata with output|46-52|
|7|II|Regular Languages**:**Conversion, Pumping lemma of<br>regular sets|53-58|
|8||Pumping lemma of regular sets|59-64|
|9||FA:RLG,LLG, Sentential forms|65-72|
|10|III|Context Free Grammars:CNF,GNF|73-93|
|11||Pumping Lemma for Context Free Languages.<br>Enumeration of properties of CFL|94-107|
|12|IV|Equivalence of CFL and PDA, inter conversion Push<br>Down Automata**,**LBA,CSL|108-112|
|13|V|Turing Machine: Church’s hypothesis, counter<br>machine, types of Turing machines|113-115|
|14||LR(0) grammar, decidability of, problems,UTM,P<br>and NP Problems|116-122|



FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 4 

## **MALLA REDDY COLLEGE OF ENGINEERING & TECHNOLOGY** 

## **DEPARTMENT OF INFORMATION TECHNOLOGY** 

UNIT-1 

Page 5 

FORMAL LANGUAGES AND AUTOMATA THEORY 

## After going through this chapter, you should be able to ungerstana : 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 6 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 7 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 8 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 9 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 10 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 11 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 12 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 13 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 14 

Page 15 

FORMAL LANGUAGES AND AUTOMATA THEORY 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 16 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 17 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 18 

**==> picture [131 x 34] intentionally omitted <==**

**----- Start of picture text -----**<br>
wi TT ET Ts}<br>**----- End of picture text -----**<br>


## : Model of FSM 

A finite state machine is represented by 6 - tuple (0,2,4,6 Ayqy) s Where 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 19 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 20 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 21 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 22 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 23 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 24 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 25 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 26 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 27 

**==> picture [56 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
Unit-II<br>**----- End of picture text -----**<br>


FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 28 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 29 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 30 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 31 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 32 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 33 

**==> picture [454 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
FORMAL LANGUAGES AND AUTOMATA THEORY  Page 34<br>**----- End of picture text -----**<br>


FORMAL LANGUAGES AND AUTOMATA THEORY Page 35 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 36 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 37 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 38 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 39 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 40 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 41 

UNIT-3 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 42 

**==> picture [212 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
FORMAL LANGUAGES AND AUTOMATA THEORY<br>**----- End of picture text -----**<br>


Page 43 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 44 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 45 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 46 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 47 

UNIT-3 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 48 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 49 

**==> picture [454 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
FORMAL LANGUAGES AND AUTOMATA THEORY  Page 50<br>**----- End of picture text -----**<br>


**==> picture [454 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
FORMAL LANGUAGES AND AUTOMATA THEORY  Page 51<br>**----- End of picture text -----**<br>


Page 52 

FORMAL LANGUAGES AND AUTOMATA THEORY 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 53 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 54 

Page 55 

FORMAL LANGUAGES AND AUTOMATA THEORY 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 56 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 57 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 58 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 59 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 60 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 61 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 62 

**UNIT-4** 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 63 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 64 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 65 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 66 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 67 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 68 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 69 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 70 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 71 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 72 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 73 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 74 

Page 75 

FORMAL LANGUAGES AND AUTOMATA THEORY 

## **UNIT-5** 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 76 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 77 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 78 

# FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 79 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 80 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 81 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 82 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 83 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 84 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 85 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 86 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 87 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 88 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 89 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 90 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 91 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 92 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 93 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 94 

Page 95 

FORMAL LANGUAGES AND AUTOMATA THEORY 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 96 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 97 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 98 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 99 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 100 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 101 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 102 

**==> picture [212 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
FORMAL LANGUAGES AND AUTOMATA THEORY<br>**----- End of picture text -----**<br>


Page 103 

# FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 104 

**==> picture [212 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
FORMAL LANGUAGES AND AUTOMATA THEORY<br>**----- End of picture text -----**<br>


Page 105 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 106 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 107 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 108 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 109 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 110 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 111 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 112 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 113 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 114 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 115 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 116 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 117 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 118 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 119 

FORMAL LANGUAGES AND AUTOMATA THEORY Page 120 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 121 

FORMAL LANGUAGES AND AUTOMATA THEORY 

Page 122 

