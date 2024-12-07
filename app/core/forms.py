import re

from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


VALID_URL_PATTERN = r"^(https:\/\/(yadi\.sk|disk\.yandex\.ru)\/d\/)[A-Za-z0-9_-]+(&path=\/[A-Za-z0-9а-яА-ЯёЁ_/ +-]+)?$"


class SearchForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Search')

    def validate_url(self, url):
        is_valid = re.match(VALID_URL_PATTERN, url.data)
        if not is_valid:
            raise ValidationError('Please enter a valid public Yandex Disk URL.')
