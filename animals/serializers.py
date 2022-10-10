

from rest_framework import serializers
from groups.models import Group
from groups.serializers import GroupSerializer
from traits.models import Trait
from traits.serializers import TraitSerializer
from .models import Animal, Options
import math

class AnimalSerializer(serializers.Serializer):
    # Modifique o serializer de animals para mostrar o campo id somente na saída.
    id= serializers.IntegerField(read_only=True)
    name= serializers.CharField()
    age= serializers.IntegerField()
    weight= serializers.FloatField()
    sex= serializers.ChoiceField(choices=Options.choices, default= Options.DEFAULT,)
    # Modifique o serializer de animals para retornar também as informações de group e traits associadas ao animal.
    group= GroupSerializer()
    traits= TraitSerializer(many=True)
    # pode receber mais de um 
    
    age_to_human_years= serializers.SerializerMethodField(read_only=True)

    def get_age_to_human_years(self, obj:Animal)->float:
        human_age= 16*math.log(obj.age)+31
        return round(human_age,1)

    def create(self,validated_data):
        group_Unique= validated_data.pop("group")
        # pegando id e guardando
        trait_unique= validated_data.pop("traits")
        # peganod model e vendo os objetos dentro, se ele ja tiver no objeto ele pega e mostra na tela se noa tiver ele cria comeca na posicao 0
        group_find= Group.objects.get_or_create(**group_Unique)[0]
        # group_find, _ = Group.objects.get_or_create(**group_Unique)
        #pegando um animal e crianod um grupo
        animal= Animal.objects.create(**validated_data,group=group_find)
        for trait in trait_unique:
            new_trait=Trait.objects.get_or_create(**trait)[0]
            animal.traits.add(new_trait)
        return animal    

    def update(self,instance:Animal,validated_data:dict)->Animal:
        dict_not_edit={"sex","group","traits"}
        for key, value in validated_data.items():
            if key in dict_not_edit:
                raise KeyError({f'{key}': f'You can not update {key} property.'})
            setattr(instance,key,value)
        instance.save()
        return instance    
