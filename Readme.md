# 2DMI20-Software-Security
It belongs to course 2DMI20 - Software Security. This course is offered at TU/e and aimed at students of mathematics and computer science.


Objectives
The purpose of this course is to become familiar with how system vulnerabilities arise on the software layer and how to protect against them.


At the end of the course, the students

- have a deep understanding of the fundamental limitations in software security and based on that can argue about the feasibility and effectiveness of practical techniques to find weaknesses.
- understand the fundamental root causes of software errors and the costs of the techniques to find them.
- should know and understand the most important security weaknesses in practice as well as effective techniques to avoid them. These techniques range from a defensive choice of programming language to analytic techniques like static code analysis, fuzzing, and formal verification.
- should be able to apply countermeasures appropriately to mitigate weaknesses.
- use a wholistic approach (7+1 kingdoms) to finding security weaknesses that covers all aspects of a system and use that to decompose complex application scenarios..
- come up with original solutions to weaknesses.  


This course consistst of a series of lectures that focus on the most important ideas in Software Security. Correspondingly the focus is on concepts and not practical application. This course is not a lab.

Background knowledge in cryptography is helpful.
Content
‘Cryptography is typically bypassed, not penetrated', Adi Shamir famously said. In fact most security problems are not due to weak cryptography but happen when systems get implemented in software.
Bugs are common in all kinds of software, but in the adversarial setting of security, software attackers may be able to cause bugs like buffer overflows that otherwise happen with negligible probability simply because they can craft the input that the system operates on. Such bugs cannot be found with regular testing methods. This course covers software insecurity as well as software security, because it is necessary to understand the attack side in order to build defenses.
 
On the attack side the course covers typical implementation errors such as memory corruption and web attacks and how they can be exploited.


Some root causes for software insecurity are choice of language, lack of testing (permanent beta's), but also underspecified system descriptions.
 
On the defense side static code analysis and  fuzzing has shown some success in finding security issues -- but cannot provide guarantees about the absence of errors. Stronger tools with such guarantees are formal verification of the code.
