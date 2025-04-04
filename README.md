# Calculatrice en Notation Polonaise Inverse (NPI)

Ce projet est une application **React (Vite) + FastAPI** qui permet de calculer des expressions en **Notation Polonaise Inverse (RPN)**, d'afficher l'historique des calculs et d'exporter les données au format CSV.

## Fonctionnalités
- **Calculatrice RPN :** Entrez une expression en notation polonaise inverse et obtenez le résultat.  
- **Historique :** Affichez la liste des calculs effectués.  
- **Exportation CSV :** Téléchargez l'historique sous forme de fichier CSV.  
- **Interface moderne :** Utilisation de *React, Vite, TailwindCSS*.  
- **API REST :** Développée avec *FastAPI*.  
- **Base de données PostgreSQL :** Stocke l'historique des calculs.  
- **Déploiement avec Docker :** Tout est orchestré avec *Docker Compose*.  

## Architecture du projet
```
reverse-polish-notation-calculator/
├── app/                    # API FastAPI
│   ├── crud.py             # Opérations CRUD pour la base de données
│   ├── database.py         # Connexion à la base de données
│   ├── main.py             # Point d'entrée FastAPI
│   ├── models.py           # Modèles SQLAlchemy
│   ├── routes/             # Routes API (calculs, historique, export)
│   ├── schemas.py          # Schémas Pydantic
│   ├──Dockerfile           # Dockerfile pour le backend
│   ├──requirements.txt     # Dépendances Python
│
├── tests/                  # Tests unitaires du backend
│
│── frontend/               # Interface utilisateur React
│   ├── src/
│   │   ├── components/     # Composants UI (Calculator, History, Export)
│   │   ├── pages/          # Pages React
│   │   ├── api/            # Fonctions pour appeler l'API
│   │   ├── App.tsx         # Composant principal
│   │   ├── main.tsx        # Point d'entrée React
│   ├── Dockerfile          # Dockerfile pour le frontend
│   ├── package.json        # Dépendances React
│
│── docker-compose.yml      # Orchestration Docker (frontend, backend, DB)
│── README.md               # Documentation
```

## Installation et Exécution avec Docker
**1. Clonez le projet :**  
```sh
git clone https://github.com/ahmedyass/reverse-polish-notation-calculator.git
cd reverse-polish-notation-calculator
```

**2. Lancez l'application avec Docker Compose :**  
```sh
docker compose up -d --build
```

**3. Accédez à l'application :**  
- Frontend (React) : <http://localhost:3000>  
- API (FastAPI) : <http://localhost:8000/docs> (Swagger UI)  

## Technologies utilisées
<table> 
    <tr>
        <td align="center"><img src="https://cdn.worldvectorlogo.com/logos/react-2.svg" width="50"/><br>React</td>
        <td align="center"><img src="https://vitejs.dev/logo.svg" width="50"/><br>Vite</td>
        <td align="center"><img src="https://cdn.worldvectorlogo.com/logos/tailwindcss.svg" width="50"/><br>TailwindCSS</td>
        <td align="center"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="50"/><br>FastAPI</td>
        <td align="center"><img src="https://cdn.worldvectorlogo.com/logos/postgresql.svg" width="50"/><br>PostgreSQL</td>
        <td align="center"><img src="https://cdn.worldvectorlogo.com/logos/docker.svg" width="50"/><br>Docker</td> 
    </tr> 
</table>

- **Backend :** FastAPI, SQLAlchemy, Pydantic  
- **Base de données :** PostgreSQL  
- **Frontend :** React (Vite), TypeScript, TailwindCSS  
- **Outils :** Docker, Docker Compose

## Exécution des tests unitaires
```sh
pytest -v
```

- **pytest :** Lance tous les tests dans le répertoire courant (tests/).
- **-v (verbose) :** Affiche plus de détails sur les tests exécutés.

### Génération d'un rapport de couverture de code
```sh
pytest --cov=app --cov-report=html
```

- **--cov=app :** Analyse la couverture de code pour le module `app/`
- **--cov-report=html :** Génère un rapport HTML détaillé de la couverture de code dans un dossier `htmlcov/`.

> Ouvrez `htmlcov/index.html` dans votre navigateur pour voir les résultats.

> Dans certains cas, `pytest` peut ne pas reconnaître correctement vos modules. Vous pouvez explicitement définir `PYTHONPATH` pour résoudre ce problème.

```sh
export PYTHONPATH=$(pwd)
PYTHONPATH=$(pwd) pytest -v
```
