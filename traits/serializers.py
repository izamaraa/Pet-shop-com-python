from rest_framework import serializers

class TraitSerializer(serializers.Serializer):
    # Modifique o serializer de traits para mostrar o campo id somente na saída.
    id= serializers.IntegerField(read_only=True)
    name= serializers.CharField()