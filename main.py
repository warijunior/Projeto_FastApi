from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas

# Inicializa a aplicação FastAPI
app = FastAPI()

# Cria as tabelas no banco de dados com base nos modelos definidos
Base.metadata.create_all(bind=engine)


def get_db():
    """
    Função para obter uma sessão do banco de dados.
    Esta função é usada como uma dependência nas rotas.
    """
    # Cria uma nova sessão do banco de dados
    db_session = SessionLocal()
    try:
        yield db_session  # Retorna a sessão para uso na rota
    finally:
        db_session.close()  # Fecha a sessão após o uso


@app.post("/empresas/", response_model=schemas.Empresa)
def criar_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    """
    Endpoint para criar uma nova empresa.

    Parâmetros:
    - empresa: Dados da empresa a ser criada (modelo de entrada).
    - db: Sessão do banco de dados (injetada automaticamente).

    Retorna:
    - A empresa criada.
    """
    # Cria uma nova instância de Empresa com os dados fornecidos
    nova_empresa = models.Empresa(**empresa.dict())

    # Adiciona a nova empresa à sessão do banco de dados
    db.add(nova_empresa)

    # Comita as mudanças no banco de dados
    db.commit()

    # Atualiza a instância da empresa com os dados do banco (incluindo o ID gerado)
    db.refresh(nova_empresa)

    return nova_empresa  # Retorna a empresa criada


@app.get("/empresas/{empresa_id}", response_model=schemas.Empresa)
def obter_empresa(empresa_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para obter uma empresa pelo ID.

    Parâmetros:
    - empresa_id: ID da empresa a ser obtida.
    - db: Sessão do banco de dados (injetada automaticamente).

    Retorna:
    - A empresa correspondente ao ID fornecido.
    """
    # Consulta a empresa no banco de dados pelo ID
    empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()

    # Verifica se a empresa foi encontrada
    if empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")

    return empresa  # Retorna a empresa encontrada


@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoria)
def criar_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    """
    Endpoint para criar uma nova obrigação acessória.

    Parâmetros:
    - obrigacao: Dados da obrigação a ser criada (modelo de entrada).
    - db: Sessão do banco de dados (injetada automaticamente).

    Retorna:
    - A obrigação acessória criada.
    """
    # Cria uma nova instância de ObrigacaoAcessoria com os dados fornecidos
    nova_obrigacao = models.ObrigacaoAcessoria(**obrigacao.dict())

    # Adiciona a nova obrigação à sessão do banco de dados
    db.add(nova_obrigacao)

    # Comita as mudanças no banco de dados
    db.commit()

    # Atualiza a instância da obrigação com os dados do banco (incluindo o ID gerado)
    db.refresh(nova_obrigacao)

    return nova_obrigacao  # Retorna a obrigação criada


@app.get("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def obter_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para obter uma obrigação acessória pelo ID.

    Parâmetros:
    - obrigacao_id: ID da obrigação a ser obtida.
    - db: Sessão do banco de dados (injetada automaticamente).

    Retorna:
    - A obrigação acessória correspondente ao ID fornecido.
    """
    # Consulta a obrigação no banco de dados pelo ID
    obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()

    # Verifica se a obrigação foi encontrada
    if obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")

    return obrigacao  # Retorna a obrigação