import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class SimplyPasswordValidator:
    def validate(self, password, user=None):
        errors = []

        if not re.findall('[0-9]', password):
            errors.append(
                _("La contraseña debe de tener al menos un numero")
            )
        
        if len(password) < 6:
            errors.append(
                _('La contraseña debe de tener al menos 6 caracteres')
            )
        if errors:
            raise ValidationError(errors)

    def get_help_text(self):
        return _(
            "La contraseña debe de tener al menos un numero y 6 digitos."
        )
    