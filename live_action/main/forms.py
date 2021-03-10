from .models import Activity
from django import forms
from .activity_choices import CHOICES


class FilterForm(forms.Form):
    type = forms.ChoiceField(label='Вид спорта:',
                             choices=CHOICES)
    season = forms.ChoiceField(label='Сезон:',
                               choices=(('0', 'Зима'), ('1', 'Весна'),
                                        ('2', 'Лето'), ('3', 'Осень'),
                                        ('4', 'Любой')))
    enviroment_chars = forms.ChoiceField(label='Окружение:',
                                         choices=(('0', 'Природа'), ('1', 'Курорт'),
                                                  ('2', 'Город')))  # 0-wild lands,..,2-city
    extreme = forms.ChoiceField(label='Экстримальность:', choices=(('0', 'Низкая'), ('1', 'Средняя'), ('2', 'Высокая')))


class GoalForm(forms.Form):
    activity_id = forms.CharField(max_length=50)
