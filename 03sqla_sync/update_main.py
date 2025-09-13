from conf.db_session import create_session

from models.sabor import Sabor
from models.picole import Picole

def update_sabor(id_sabor: int, novo_nome: str) -> None:
    with create_session() as session:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sabor:
            sabor.nome = novo_nome

            session.commit()
        else:
            print(f'Não existe sabor com o id: {id_sabor}')

def select_filtro_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            print(f'ID: {picole.id}')
            print(f'Sabor: {picole.sabor.nome}')
        else:
            print('Não existe picole com o id informado')

                                                # se não passar nada o valor padrão será None
def update_picole(id_picole: int, novo_preco: float, novo_sabor: int = None):
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            picole.preco = novo_preco
            # se quisermos podemos alterar o sabor também
            if novo_sabor: # se o valor for fornecido faz a alteração
                picole.id_sabor = novo_sabor
        session.commit()


if __name__ == '__main__':
    from select_main import select_filtro_sabor

    # id_sabor = 2

    # select_filtro_sabor(id_sabor = id_sabor)

    # update_sabor(id_sabor = id_sabor, novo_nome='Melancia')

    # select_filtro_sabor(id_sabor = id_sabor)

    id_picole = 4
    novo_preco = 10.0
    novo_sabor = 2

    select_filtro_picole(id_picole=id_picole)

    update_picole(id_picole=id_picole, novo_preco=novo_preco, novo_sabor=novo_sabor)

    select_filtro_picole(id_picole=id_picole)