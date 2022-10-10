
from rest_framework import serializers

class GroupSerializer(serializers.Serializer):
    # Modifique o serializer de groups para mostrar o campo id somente na saída.
    id = serializers.IntegerField(read_only=True)
    name= serializers.CharField()
    scientific_name= serializers.CharField()


