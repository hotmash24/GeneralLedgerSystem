# custom_filters.py

from django import template

register = template.Library()

def amount_to_words(amount):
    # Define the conversion logic here (you can use any library or custom code)

    # For demonstration purposes, I'm providing a simple example
    # You can replace this with a more comprehensive conversion function

    # Sample conversion function (use your own logic)
    units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    def words(n):
        if 10 <= n < 20:
            return teens[n - 10]
        elif n < 10:
            return units[n]
        else:
            return tens[n // 10 - 2] + ('' if n % 10 == 0 else '-' + units[n % 10])

    # Split the amount into whole and decimal parts (if applicable)
    whole_part, decimal_part = str(amount).split('.')
    whole_part = int(whole_part)
    decimal_part = int(decimal_part) if decimal_part else 0

    # Convert the whole part to words
    words_whole = words(whole_part)

    # Convert the decimal part to words (optional)
    words_decimal = words(decimal_part) if decimal_part else ''

    # Combine the whole and decimal parts (optional)
    amount_in_words = f"{words_whole} dollars and {words_decimal} cents" if words_decimal else f"{words_whole} dollars"

    return amount_in_words

register.filter('amount_to_words', amount_to_words)
