"""
Módulo para identificação de bandeiras de cartões de crédito.
"""
import re
from typing import Optional


class CreditCard:
    """Classe que representa um cartão de crédito e suas características."""

    BRAND_PATTERNS = {
        'VISA': r'^4[0-9]{12}(?:[0-9]{3})?$',
        'MASTERCARD': r'^5[1-5][0-9]{14}$',
        'AMEX': r'^3[47][0-9]{13}$',
        'DINERS': r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
        'DISCOVER': r'^6(?:011|5[0-9]{2})[0-9]{12}$',
        'JCB': r'^(?:2131|1800|35\d{3})\d{11}$',
        'ELO': r'^(4011|431274|438935|451416|457393|4576|457631|457632|504175|627780|636297|636368|636369)'
    }

    def __init__(self, number: str):
        """
        Inicializa um novo objeto CreditCard.

        Args:
            number (str): Número do cartão de crédito
        """
        self.number = self._sanitize_number(number)
        self.brand = self._identify_brand()

    @staticmethod
    def _sanitize_number(number: str) -> str:
        """
        Remove caracteres não numéricos do número do cartão.

        Args:
            number (str): Número do cartão com possíveis caracteres especiais

        Returns:
            str: Número do cartão apenas com dígitos
        """
        return re.sub(r'[^0-9]', '', number)

    def _identify_brand(self) -> Optional[str]:
        """
        Identifica a bandeira do cartão com base no seu número.

        Returns:
            Optional[str]: Nome da bandeira do cartão ou None se não for identificada
        """
        if not self.is_valid():
            return None

        for brand, pattern in self.BRAND_PATTERNS.items():
            if re.match(pattern, self.number):
                return brand
        return None

    def is_valid(self) -> bool:
        """
        Verifica se o número do cartão é válido usando o algoritmo de Luhn.

        Returns:
            bool: True se o cartão for válido, False caso contrário
        """
        if not self.number.isdigit():
            return False

        digits = [int(d) for d in self.number]
        checksum = 0
        is_odd = True

        for i in range(len(digits) - 1, -1, -1):
            d = digits[i]
            if is_odd:
                d *= 2
                if d > 9:
                    d -= 9
            checksum += d
            is_odd = not is_odd

        return checksum % 10 == 0


def identify_card_brand(card_number: str) -> Optional[str]:
    """
    Função auxiliar para identificar a bandeira de um cartão de crédito.

    Args:
        card_number (str): Número do cartão de crédito

    Returns:
        Optional[str]: Nome da bandeira do cartão ou None se não for identificada
    """
    card = CreditCard(card_number)
    return card.brand


if __name__ == '__main__':
    # Exemplos de uso
    test_numbers = [
        '4532123456788901',  # Visa
        '5412345678901234',  # Mastercard
        '371234567890123',   # American Express
        'invalid_number',    # Número inválido
    ]

    for number in test_numbers:
        brand = identify_card_brand(number)
        print(f'Número: {number}')
        print(f'Bandeira: {brand if brand else "Não identificada/Inválida"}\n') 