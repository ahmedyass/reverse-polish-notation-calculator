from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Calculation

router = APIRouter()

@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    """
    Récupère l'historique des calculs enregistrés.

    - Retourne une liste de tous les calculs stockés en base de données.

    ### Réponses :
    - **200** : Retourne la liste des calculs effectués.
    - **500** : Erreur interne du serveur.

    ### Exemple de réponse :
    ```json
    [
        {
            "id": 1,
            "expression": "5 3 +",
            "result": 8,
            "created_at": "2024-03-30T12:00:00"
        },
        {
            "id": 2,
            "expression": "10 2 /",
            "result": 5,
            "created_at": "2024-03-30T12:05:00"
        }
    ]
    ```
    """
    return db.query(Calculation).all()
