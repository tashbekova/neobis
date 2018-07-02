from rest_framework import serializers
from snippets.models import Task,, LANGUAGE_CHOICES, STYLE_CHOICES

class TaskSerializer(serializers.Serilizer):
    {
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=False, allow_blank=True, max_length=100)
    description=serializers.CharField(max_length=200)
    category = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    logo=serializers.URLField()
    "contacts": [
        {
            "type": "PHONE",
            "value": "0770 792 299"
        },
        {
            "type": "FACEBOOK",
            "value": "https://www.facebook.com/english.zone.kg/"
        },
        {
            "type": "EMAIL",
            "value": "ezone.kg@gmail.com"
        }
    ],
    "branches": [
        {
            "address": "Manas 58/ Aini - right next to the Manas university",
            "address": "Manas 58/ Aini - right next to the Manas universit",
            "latitude": "42.847971",
            "longitude": "74.586733"
},
{
            "address": "Бишкек, Юг-2 дом 15а Советская/Горького",
            "latitude": "42.8586017",
            "longitude": "74.6068425"
        }
    ]
}
