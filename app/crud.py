from sqlalchemy.orm import Session
from .models import Calculation

def evaluate_rpn(expression: str) -> float:
    """
    Évalue une expression mathématique en notation polonaise inversée (RPN).

    - Utilise une pile (stack) pour exécuter les opérations.
    - Prend en charge les opérateurs : `+`, `-`, `*`, `/`.
    - Vérifie si l'expression est bien formée.

    ### Paramètres :
    - **expression (str)** : L'expression en notation RPN (ex: `"3 4 +"`).

    ### Retourne :
    - **float** : Le résultat du calcul.

    ### Exceptions :
    - **ValueError** : Si l'expression est vide ou mal formée.
    - **ZeroDivisionError** : Si une division par zéro est détectée.
    """
    stack = []
    operators = {"+", "-", "*", "/"}

    tokens = expression.split()
    if not tokens:
        raise ValueError("L'expression est vide.")

    for token in tokens:
        if token in operators:
            if len(stack) < 2:
                raise ValueError(f"Opérateur {token} utilisé avec une pile insuffisante.")
            b, a = stack.pop(), stack.pop()
            if token == "/" and b == 0:
                raise ZeroDivisionError("Division par zéro détectée.")
            stack.append(eval(f"{a} {token} {b}"))
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Token invalide détecté : {token}")

    if len(stack) != 1:
        raise ValueError("Expression mal formée.")

    return stack[0]

def create_calculation(db: Session, expression: str):
    """
    Crée un enregistrement en base de données pour un calcul donné.

    - Évalue l'expression RPN et stocke le résultat.
    - Ajoute l'entrée dans la base de données.

    ### Paramètres :
    - **db (Session)** : Session SQLAlchemy active.
    - **expression (str)** : Expression en notation RPN à calculer.

    ### Retourne :
    - **Calculation** : Objet contenant l'expression et son résultat.

    ### Exceptions :
    - **ValueError** : Si l'expression est mal formée.
    - **ZeroDivisionError** : Si une division par zéro est détectée.
    """
    result = evaluate_rpn(expression)
    calc = Calculation(expression=expression, result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    return calc

def get_all_calculations(db: Session):
    """
    Récupère tous les calculs enregistrés en base de données.

    ### Paramètres :
    - **db (Session)** : Session SQLAlchemy active.

    ### Retourne :
    - **list[Calculation]** : Liste des calculs stockés.
    """
    return db.query(Calculation).all()