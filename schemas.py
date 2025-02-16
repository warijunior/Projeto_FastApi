# Importa a classe BaseModel do Pydantic, que é usada para validação de dados
from pydantic import BaseModel


# Classe base para o modelo de dados da Empresa
class EmpresaBase(BaseModel):
    """Modelo base para a criação e manipulação de dados de uma empresa."""

    # Atributos da empresa
    nome: str  # Nome da empresa
    cnpj: str  # CNPJ da empresa
    endereco: str  # Endereço da empresa
    email: str  # Email da empresa
    telefone: str  # Telefone da empresa


# Classe para criar uma nova empresa, herda de EmpresaBase
class EmpresaCreate(EmpresaBase):
    """Modelo para a criação de uma nova empresa."""
    pass  # Não adiciona novos atributos, apenas herda os da classe base


# Classe que representa uma empresa existente, herda de EmpresaBase
class Empresa(EmpresaBase):
    """Modelo que representa uma empresa existente, incluindo seu ID."""

    id: int  # ID da empresa (gerado pelo banco de dados)

    class Config:
        """Configurações adicionais para o modelo."""
        from_attributes = True  # Permite a criação de instâncias a partir de atributos


# Classe base para o modelo de dados da Obrigação Acessória
class ObrigacaoAcessoriaBase(BaseModel):
    """Modelo base para a criação e manipulação de dados de uma obrigação acessória."""

    # Atributos da obrigação acessória
    nome: str  # Nome da obrigação
    periodicidade: str  # Periodicidade da obrigação (mensal, trimestral, etc.)
    empresa_id: int  # ID da empresa associada (chave estrangeira)


# Classe para criar uma nova obrigação acessória, herda de ObrigacaoAcessoriaBase
class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    """Modelo para a criação de uma nova obrigação acessória."""
    pass  # Não adiciona novos atributos, apenas herda os da classe base


# Classe que representa uma obrigação acessória existente, herda de ObrigacaoAcessoriaBase
class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    """Modelo que representa uma obrigação acessória existente, incluindo seu ID."""

    id: int  # ID da obrigação acessória (gerado pelo banco de dados)

    class Config:
        """Configurações adicionais para o modelo."""
        from_attributes = True  # Permite a criação de instâncias a partir de atributos