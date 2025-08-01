from conf.db_session import create_session

from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

# 1 Aditivo Nutritivo
def insert_aditivo_nutritivo() -> None:
    print('Cadastrando Aditivo Nutritivo')

    nome: str = input('Digite o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Digite a fórmula química: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)

        session.commit()


# 2 Sabor
def insert_sador() -> None:
    
    nome: str = input('Digite um sabor de picole: ')

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)
        session.commit()

# 3 Tipo Embalagem
def insert_tipo_embalagem() -> None:
    nome: str = input('Digite um Tipo de Embalagem: ')
    te: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(te)
        session.commit()

# 4 Tipo Picole
def insert_tipo_picole() -> None:
    # nome: str = input('Digite um Tipo de Picolé: ')
    # tp: TipoPicole = TipoPicole(nome=nome)

    lista_tp = ['Leite', 'Água']

    with create_session() as session:
        for nome in lista_tp:
            tp = TipoPicole(nome=nome)
            session.add(tp)
        session.commit()
        return '...'

# 5 Ingredientes
def insert_ingrediente() -> None:
    nome: str = input('Digite o Ingrediente: ')
    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()

# 6 conservantes
def insert_conservantes() -> None:
    # nome: str = input('Digite o Conservante: ')
    # descricao: str = input('Digite uma descrição do conservante: ')

    # conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    conservante = [Conservante(nome='Ácido Cítrico', descricao='Chama'), 
                   Conservante(nome='Soda', descricao='Morte')]

    with create_session() as session:
        session.add_all(conservante)
        session.commit()

# 7 revendedores
def insert_revendedor() -> Revendedor:
    cnpj: str = input('Digite o cnpj: ')
    razao_social: str = input('Digite a razão social: ')
    contato: str = input('Digite o contato: ')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()
    return revendedor


if __name__ == '__main__':
    #insert_aditivo_nutritivo()

    #insert_sador()

    #insert_tipo_embalagem()

    #insert_tipo_picole()

    #insert_ingrediente()

    insert_conservantes()


    # rev = insert_revendedor()
    # print(rev)

    # print(f'ID: {rev.id}')