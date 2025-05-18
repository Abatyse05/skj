League Project

Funkce

Správa hráčů (jméno, přezdívka, tým, kategorie)
Správa týmů (včetně přiřazené ligy a kategorie)
Evidence lig (název, sezóna, odměna)
Historie působení hráčů v týmech
Vzájemně propojené datové modely
REST API pomocí [Django Ninja](https://django-ninja.dev/)
Stylováno pomocí [Bootstrap 5](https://getbootstrap.com/)

Jak spustit projekt

1. Klonuj repozitář

bash
git clone https://github.com/Abatyse05/skj.git
cd skj

Vytvoř virtuální prostředí

python -m venv venv
venv\Scripts\activate 

3. Instaluj závislosti

pip install -r requirements.txt

4. Proveď migrace a spusť vývojový server

python manage.py migrate
python manage.py runserver


Stránka	Popis

/	              Hlavní stránka
/players/	      Seznam hráčů
/teams/	        Seznam týmů
/ligues/	      Seznam lig
/history/	      Historie působení hráčů
/admin/        	Django administrace
/api/docs      	REST API dokumentace



REST API

http://127.0.0.1:8000/api/docs











