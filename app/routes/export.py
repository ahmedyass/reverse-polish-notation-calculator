from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
from fastapi.responses import FileResponse
from ..database import get_db
from ..crud import get_all_calculations
import os

router = APIRouter()

@router.get("/export", response_class=FileResponse)
def export_calculations(db: Session = Depends(get_db)):
    """
    Exporte l'historique des calculs en fichier CSV.

    - Récupère tous les calculs stockés en base de données.
    - Génère un fichier CSV contenant les expressions, les résultats et la date de création.
    - Retourne le fichier CSV en téléchargement.

    ### Réponses :
    - **200** : Retourne le fichier `calculations.csv`.
    - **404** : Aucun calcul trouvé dans la base de données.

    ### Exemple de réponse :
    ```csv
    expression,result,created_at
    "5 3 +",8,"2024-03-30 12:00:00"
    "10 2 /",5,"2024-03-30 12:05:00"
    ```
    """
    calculations = get_all_calculations(db)
    
    if not calculations:
        raise HTTPException(status_code=404, detail="Aucune donnée à exporter")

    df = pd.DataFrame([
        {"expression": c.expression, "result": c.result, "created_at": c.created_at} 
        for c in calculations
    ])
    
    file_path = "calculations.csv"
    df.to_csv(file_path, index=False)

    return FileResponse(file_path, filename="calculations.csv", media_type="text/csv")
