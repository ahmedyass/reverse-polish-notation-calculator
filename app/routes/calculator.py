from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import CalculationCreate, CalculationResponse
from ..crud import create_calculation

router = APIRouter()

@router.post("/calculate", response_model=CalculationResponse)
def calculate(expression_data: CalculationCreate, db: Session = Depends(get_db)):
    """
    Calcule le résultat d'une expression en notation polonaise inversée (RPN).

    - Prend en entrée une expression mathématique sous forme RPN.
    - Effectue le calcul et enregistre le résultat en base de données.
    - Retourne l'expression et son résultat.

    ### Paramètres :
    - **expression_data (CalculationCreate)** : Expression en notation RPN.

    ### Réponses :
    - **200** : Retourne l'expression avec son résultat.
    - **400** : Erreur de calcul (ex: division par zéro, expression invalide).
    - **500** : Erreur interne du serveur.

    ### Exemple de requête :
    ```json
    {
        "expression": "5 3 +"
    }
    ```

    ### Exemple de réponse :
    ```json
    {
        "id": 1,
        "expression": "5 3 +",
        "result": 8,
        "created_at": "2024-03-30T12:00:00"
    }
    ```
    """
    try:
        calculation = create_calculation(db, expression_data.expression)
        return calculation
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Erreur : division par zéro.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Erreur : {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erreur interne du serveur.")
