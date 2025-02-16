# Importa as bibliotecas necessárias do SQLAlchemy e outras
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a URL de conexão do banco de dados a partir das variáveis de ambiente
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o mecanismo de conexão com o banco de dados usando a URL fornecida
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe base para os modelos do SQLAlchemy
Base = declarative_base()