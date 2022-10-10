
from django.test import TestCase
from animals.models import Animal
from traits.models import Trait
from groups.models import Group

class TestTraits(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        data={
            "name":"teste",
            "scientific_name":"teste",
        }
        cls.group=Group.objects.create(**data)

        trait_teste_1={"name":"trait_teste_1"}
        trait_teste_2={"name":"trait_teste_2"}

       
        cls.criando_variavel_1 =Trait.objects.get_or_create(**trait_teste_1)[0]

       

        cls.criando_variavel_2 =Trait.objects.get_or_create(**trait_teste_2)[0]

        cls.name = "Casco duro"

        cls.traits_1 = Trait.objects.create(
            name = cls.name
        )
        cls.traits_2 = Trait.objects.create(
            **{
                "name":"Casco branco"
            }
        )

        cls.animal_1 = Animal.objects.create(
            **{
                "name": "tartaruga",
                "age": 200,
                "weight": 30,
                "sex":"Femea"
            }
        )
        cls.animals = Animal.objects.all()

        cls.scientific_name="teste"

        cls.group_1 = Group.objects.create(
            name = cls.name,
            scientific_name = cls.scientific_name
        )
        

    def test_group_wrong_max_length(self):
        max_nome=20
        max_scientific_name=50
        nome_grupo_atual= Group._meta.get_field("name").max_length
        nome_scientific_name = Group._meta.get_field("scientific_name").max_length
        saida=f'Model de group name deve possuir ate {max_nome} caracteres, e esta recebendo {nome_grupo_atual} '
        saida2=f'Model de group deve possuir ate {max_scientific_name} caracteres, e esta recebendo {nome_scientific_name} '

        self.assertEqual(max_nome, nome_grupo_atual,msg=saida)
        self.assertEqual(max_scientific_name, nome_scientific_name, msg=saida2)

    def test_traits_wrong_max_length(self):
        max_name=20  
        nome_trait_atual= Trait._meta.get_field("name").max_length
        saida= f"model de trait deve possuir ate {max_name} e esta recebendo {nome_trait_atual}"
        self.assertEqual(max_name, nome_trait_atual,msg=saida)

    # def test_animals_age_wrong(self):
    #       data={
    #         "name":"animal",
    #         "age":"11",
    #       }

    #       animal= Animal(**data, group=self.group)
    #       self.assertEqual(TypeError, animal.full_clean)
        

    def test_animal_group_relations(self):
        self.animal_1.group = self.group_1
        self.animal_1.save()
        self.assertIs(self.animal_1.group,self.group_1)
        self.assertIs(1,len(self.group_1.animals.all()))


    def test_animal_traits_relations(self):
        self.animal_1.traits.add(self.traits_1)
        self.animal_1.save()
        self.assertEqual(self.animal_1.traits.first(),self.traits_1)
        self.assertEqual(self.traits_1.animals.first(),self.animal_1)    


