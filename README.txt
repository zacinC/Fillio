Ova aplikacija funkcioniše kao personalni asistent koji omogućava korisnicima interkaciju na društvenim mrežama i drugim vidovima 
komunikacije. Koristeći vještačku inteligenciju, analizira primljenje poruke korisnika i generiše odgovore prilagođene njihovim potrebama. 
Na taj način, korisnicima se pruža mogućnost da izbjegnu ručno odgovaranje na sve poruke, što značajno doprinosi poboljšanju njihove produktivnosti 
i uštedi vremena. Osim pružanja odgovora, aplikacija nudi i opciju dobijanja rezimea dugih poruka, omogućavajući brži pregled njihovog sadržaja. 
Usljed ovih funkcionalnosti i mogućnosti primjene na gotovo sve platforme za komunikaciju, aplikacija je izuzetno fleksibilna i korisna za širok spektar korisnika, 
bilo da je riječ o privatoj ili poslovnoj upotrebi.


Pregled tehnologije:
- Programski jezik: Python3
- Alati za razvoj: Visual Studio Code, Git
- Biblioteke:
	- OpenAI: omogućava komunikaciju sa OPENAI API-jem,
	- PyAutoGUI: omogućava automatizaciju računarskih aktivnosti (upravljanje mišem, tastaturom i pronalaženje elemenata na ekranu),
	- Pyperclip: omogućava sprovođenje različitih funkcija nad elementima u clipboard-u (privremenoj memoriji),
	- Tkinter: omogućava kreiranje korisničkog interfejsa (GUI),
	- PIL: omogućava manipulaciju slika, uključujući njihovo učitavanje i prilagođavanje formata,
	- PyTesseract: omogućava prepoznavanje teksta na slikama primjenom OCR (Optical Character Recognition),
	- Keyboard: omogućava simuliranje radnji na tastaturi.


User manual:

1. Pokretanje aplikacije i floating button:
	- Nakon pokretanja aplikacije, primijetićete pojavu malog floating button-a na ekranu
	- Floating button se može pomjerati po ekranu koristeći kombinaciju "Ctrl + lijevi klik miša", kako biste prilagodili njegovu poziciju u skladu sa 
	  Vašim željama i potrebama.

2. Izbor poruke za generisanje odgovora:
	- Kada primite poruku za koju želite generisani odgovor, pritisnite floating button na ekranu.

3. Odabir opcije za generisanje odgovora:
	- Nakon pritiska floating button-a, pojaviće se korisnički interfejs sa opcijama.
	- Opcije su označene sljedećim slovima:
		-R: Odbijanje (Rejection),
		-S: Rezime poruke (Shortly summarized),
		-A: Prihvatanje (Acception),
		-E: Izbjegavanje (Excuse)
	- Odaberite željenu opciju klikom na odgovarajuće slovo.

4. Označavanje željene poruke:
	- Nakon odabira opcije, otvoriće se screenshot prozor.
	- Označite željenu poruku tako što ćete je selektovati.

5. Pregled generisanog odgovora:
	- Nakon označavanja poruke, generisani odgovor će se automatski pojaviti u polju za slanje poruka.
	- Pregledajte generisani odgovor i provjerite da li odgovara vašim potrebama.

6. Proslijeđivanje odgovora:
	- Ukoliko je odgovor u redu, pošaljite ga pritiskom na dugme za slanje poruka.
