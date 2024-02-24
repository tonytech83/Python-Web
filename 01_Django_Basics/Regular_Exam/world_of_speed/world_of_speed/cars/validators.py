from django.core.exceptions import ValidationError


def validate_car_year(value, min_year=1999, max_year=2030):
    if not (min_year <= value <= max_year):
        raise ValidationError(f'Year must be between {min_year} and {max_year}!')
