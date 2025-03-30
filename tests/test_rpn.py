import pytest
from app.crud import evaluate_rpn

def test_valid_rpn_expressions():
    assert evaluate_rpn("3 4 +") == 7
    assert evaluate_rpn("10 2 /") == 5
    assert evaluate_rpn("5 1 2 + 4 * + 3 -") == 14
    assert evaluate_rpn("2 3 * 4 +") == 10

def test_invalid_rpn_expressions():
    with pytest.raises(ValueError, match="L'expression est vide."):
        evaluate_rpn("")
    
    with pytest.raises(ValueError, match="Token invalide détecté"):
        evaluate_rpn("3 4 &")

    with pytest.raises(ValueError, match="Opérateur \+ utilisé avec une pile insuffisante."):
        evaluate_rpn("+")

    with pytest.raises(ZeroDivisionError, match="Division par zéro détectée."):
        evaluate_rpn("10 0 /")

    with pytest.raises(ValueError, match="Expression mal formée."):
        evaluate_rpn("3 4 5 +")
