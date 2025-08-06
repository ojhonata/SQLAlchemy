from conf.db_session import create_session

from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole

# 1 Aditivo Nutritivo
def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastrando sabor')

    print('Cadastrando Aditivo Nutritivo')

    nome: str = input('Digite o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Digite a fórmula química: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()

        return an


# 2 Sabor
def insert_sador() -> None:
    print('Cadastrando sabor')
    
    nome: str = input('Digite um sabor de picole: ')

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)
        session.commit()

# 3 Tipo Embalagem
def insert_tipo_embalagem() -> None:
    print('Cadastrando tipo de embalagem')
    # nome: str = input('Digite um Tipo de Embalagem: ')
    te = [TipoEmbalagem(nome='Plástico')]

    with create_session() as session:
        session.add_all(te)
        session.commit()

# 4 Tipo Picole
def insert_tipo_picole() -> None:
    print('Cadastrando tipo picole')
    # nome: str = input('Digite um Tipo de Picolé: ')
    # tp: TipoPicole = TipoPicole(nome=nome)

    lista_tp = ['Leite', 'Água']

    with create_session() as session:
        for nome in lista_tp:
            tp = TipoPicole(nome=nome)
            session.add(tp)
        session.commit()
        return tp

# 5 Ingredientes
def insert_ingrediente() -> Ingrediente:
    print('Cadastrando ingredientes')

    #ingredientes = [Ingrediente(nome='Açúcar')]

    nome: str = input('Digite o Ingrediente: ')
    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()

        return ingrediente
    print('Ingredientes cadastrados!')

# 6 conservantes
def insert_conservante() -> Conservante:
    print('Cadastrando Conservantes')

    nome: str = input('Digite o Conservante: ')
    descricao: str = input('Digite uma descrição do conservante: ')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    # conservante = [Conservante(nome='Ácido Cítrico', descricao='Chama'), 
    #                Conservante(nome='Soda', descricao='Morte')]

    with create_session() as session:
        session.add(conservante)
        session.commit()

        return conservante

# 7 revendedores
def insert_revendedor() -> Revendedor:
    print('Cadastrando Revendedor')
    cnpj: str = input('Digite o cnpj: ')
    razao_social: str = input('Digite a razão social: ')
    contato: str = input('Digite o contato: ')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()
        return revendedor

# 8 Lotes
def insert_lote() -> Lote:
    print('Cadastrando Lote')

    id_tipo_picole: int = input('Digite o id do tipo de picolé: ')
    quantidade: int = input('Digite a quantidade: ')

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
    #lotes: Lote = [Lote(id_tipo_picole=1, quantidade=3)]

    with create_session() as session:
        session.add(lote)
        session.commit()
        return lote

# 9 Notas Fiscais
def insert_nota_fiscal() -> NotaFiscal:
    # notas_fiscais: NotaFiscal = [NotaFiscal(valor=12.50, numero_serie='55555', descricao='compra de um produto', id_revendedor=1)]
    print('Cadastrando NF')

    valor: float = input('Digite o valor da NF: ')
    numero_serie: str = input('Digite o número de serie: ')
    descricao: str = input('Digite a descrição: ')

    rev = insert_revendedor()
    id_revendedor = rev.id

    nf: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)

    lote1 = insert_lote()
    nf.lotes.append(lote1)

    with create_session() as session:
        session.add(nf)
        session.commit()
        return nf

def insert_picole() -> None:
    print('Cadastrando Picolé')

    preco: float = input('Digite o preço do picolé: ')
    id_sabor: int = input('Informa o id do sabor: ')
    id_tipo_embalagem: int = input('Informe o id do tipo de embalagem: ')
    id_tipo_picole: int = input('Informe o id do tipo de picolé: ')

    picole: Picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)

    ingrediente1 = insert_ingrediente()
    picole.ingredientes.append(ingrediente1)

    conservante1 = insert_conservante()
    picole.conservantes.append(conservante1)

    aditivos_nutritivos1 = insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(aditivos_nutritivos1)

    with create_session() as session:
        session.add(picole)
        session.commit()
    
        print('Picole cadastrado')
        print(f'Preço: {picole.preco}')
        print(f'Sabor: {picole.sabor.nome}')
        print(f'Tipo de picolé: {picole.tipo_picole.nome}')
        print(f'Tipo embalagem {picole.tipo_embalagem.nome}')
        print(f'Ingrediente: {picole.ingredientes}')


if __name__ == '__main__':
    #insert_aditivo_nutritivo()

    #insert_sador()

    # insert_tipo_embalagem()

    # insert_tipo_picole()

    #insert_ingrediente()

    # insert_conservante()

    # rev = insert_revendedor()
    # print(rev)

    # print(f'ID: {rev.id}')

    # lote = insert_lote()
    # print(lote)

    # nota_fiscals = insert_nota_fiscal()
    # print(nota_fiscals)

    insert_picole()