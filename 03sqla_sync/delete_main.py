from typing import Optional

from conf.db_session import create_session

from models.revendedor import Revendedor
from models.picole import Picole

def deletar_picole(id_picole : int) -> None:
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f'Picole com o id {id_picole} não encontrado')

def deletar_revendedor(id_revendedor : int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f'Revendedor com id {id_revendedor} não encontrado')
    
def select_filtro_revendedor(id_revendedor : int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            print(f'ID: {revendedor.id}')
            print(f'Razão Social: {revendedor.razao_social}')

        else:
            print(f'Não foi encontrado revendedor com id {id_revendedor}')

if __name__ == "__main__":
    from update_main import select_filtro_picole

    # id_picole = 3

    # select_filtro_picole(id_picole)
    # deletar_picole(id_picole)

    # select_filtro_picole(id_picole)

    id_revendedor_nv = 3
    id_revendedor_v = 2

    select_filtro_revendedor(id_revendedor_v)

    deletar_revendedor(id_revendedor_v)

    select_filtro_revendedor(id_revendedor_v)