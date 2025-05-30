"""
Testes para o módulo de identificação de cartões de crédito.
"""
import pytest
from src.credit_card_identifier import CreditCard, identify_card_brand


def test_valid_visa_card():
    """Testa identificação de cartão Visa válido."""
    card_number = "4532123456788901"
    assert identify_card_brand(card_number) == "VISA"


def test_valid_mastercard():
    """Testa identificação de cartão Mastercard válido."""
    card_number = "5412345678901234"
    assert identify_card_brand(card_number) == "MASTERCARD"


def test_valid_amex():
    """Testa identificação de cartão American Express válido."""
    card_number = "371234567890123"
    assert identify_card_brand(card_number) == "AMEX"


def test_invalid_card_number():
    """Testa número de cartão inválido."""
    card_number = "invalid_number"
    assert identify_card_brand(card_number) is None


def test_sanitize_card_number():
    """Testa limpeza do número do cartão."""
    card = CreditCard("4532-1234-5678-8901")
    assert card.number == "4532123456788901"


def test_card_with_spaces():
    """Testa número de cartão com espaços."""
    card_number = "4532 1234 5678 8901"
    assert identify_card_brand(card_number) == "VISA"


def test_empty_card_number():
    """Testa número de cartão vazio."""
    assert identify_card_brand("") is None


def test_luhn_algorithm():
    """Testa validação pelo algoritmo de Luhn."""
    # Número válido pelo algoritmo de Luhn
    valid_card = CreditCard("4532123456788901")
    assert valid_card.is_valid() is True

    # Número inválido pelo algoritmo de Luhn
    invalid_card = CreditCard("4532123456788902")
    assert invalid_card.is_valid() is False 