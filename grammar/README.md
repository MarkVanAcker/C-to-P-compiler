README PROJECT COMPILERS



Vooruitgang: 

- Grammatica is volledig om alle verplichte onderdelen te kunnen ondersteunen (tot zover we weten en getest hebben). Ook ondersteunen we als optionele keuzes for loops, const en comparison operators (momenteel maar dit zou nog kunnen uitbreiden).
		
- Van de Parse Tree wordt een Abstrat Syntax Tree gegenereerd die de essentiele informatie bevat voor een semantische analyse.

- Symbol Table klasse is geschreven en doet wat we willen. Deze bestaat uit een boomstructuur van zijn eigen type en vormt zo de verschillende scopes. Momenteel worden er alleen
declaraties van de global scope toegevoegd.

- Semantische analyse, deze werkt alleen nog maar in de global scope en controleert de types van de variabelen.



Build:

- Met het commando : 'python3 build.py' in de C folder



Testcases:

- Met het commando : 'python3 runtests.py' in de C folder
- Output in zit in de test folder.
- Testfiles hebben vanzelfsprekende namen en testen vooral die functionaliteit.

			



Gemaakt door: Mark Van Acker, Jesse Smits



