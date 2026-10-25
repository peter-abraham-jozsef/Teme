Funcția 1 — genereaza_individ(graf, start, stop)
Primește: graful, nodul de start, nodul de destinație.
Face: pornește de la start, alege random un vecin nevizitat, adaugă la drum, repetă până ajunge la stop sau se blochează.
Returnează: lista de noduri (drumul) — validă sau moartă.

Asta e „generarea random" din Pasul 0. O vei refolosi și la imigranți și la mutație (regenerare coadă).

Funcția 2 — calculeaza_cost(graf, drum, stop)
Primește: graful, un drum, destinația.
Face: dacă drumul nu se termină cu stop → returnează 1.000.000. Altfel, însumă greutățile muchiilor consecutive.
Returnează: costul (număr).

Asta e „fitness-ul" din Pasul 1. Simplă, dar centrală — toate celelalte funcții o apelează.

Funcția 3 — genereaza_populatie(graf, start, stop, N)
Primește: graful, start, stop, dimensiunea populației N.
Face: apelează genereaza_individ de N ori.
Returnează: listă de N drumuri.

Pasul 0. Trivial — doar un for.

Funcția 4 — selectie_turneu(populatie, graf, stop, k)
Primește: populația, graful, stop, dimensiunea turneului k (ex: 3).
Face: alege random k indivizi, calculează costul fiecăruia, returnează pe cel cu costul minim.
Returnează: un individ (un drum).

Pasul 2. O apelezi de N ori ca să obții N părinți.

Funcția 5 — crossover_segment(p1, p2, graf, stop)
Primește: doi părinți, graful, stop.
Face: găsește nodurile comune, alege un punct de tăiere comun, lipește prefixul lui p1 cu sufixul lui p2. Verifică validitatea muchiilor.
Returnează: un copil valid (sau None dacă nu găsește punct valid — atunci reîncerci sau repari).

Pasul 3. Dacă e prea complicat cu noduri comune, folosește repair-based: prefix din p1 până la un punct random, apoi genereaza_individ din ultimul nod până la stop. Mai simplu și funcționează mereu.

Funcția 6 — muteaza(drum, graf, stop, rata)
Primește: un drum, graful, stop, rata de mutație.
Face: cu probabilitate rata, alege un nod random din drum, taie acolo, regenerează coada cu genereaza_individ. Verifică validitatea.
Returnează: drumul (mutat sau nemutat).

Pasul 4. Apelezi pentru fiecare copil.

Funcția 7 — generatie_noua(populatie, graf, start, stop, N, rata_mutatie, k_turneu)
Primește: populația curentă și toți parametrii.
Face:

Calculează costul fiecărui individ.

Găsește cel mai bun (elitism — îl copiezi).

Selectează N părinți prin turneu.

Pereche (p1, p2) → crossover → copil.

Aplică mutație pe fiecare copil.

Adaugă 1-2 imigranți random.

Returnează generația nouă: elită + copii + imigranți.

Pasul 5. Asta e inima GA-ului — funcția care leagă tot.

Funcția 8 — ruleaza_ga(graf, start, stop, ...) — bucla principală
Primește: graful, start, stop, și hiperparametrii.
Face:

Generează populația inițială.

Pentru fiecare generație:

Aplică generatie_noua.

Calculează costul optim.

Verifică criteriul de oprire (200 generații SAU 20 generații fără îmbunătățire).

Returnează cel mai bun drum găsit + costul + istoricul costurilor.

Asta e „main"-ul. Doar un for cu condiție de oprire.