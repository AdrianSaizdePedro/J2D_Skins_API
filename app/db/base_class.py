from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import DeclarativeBase


@as_declarative
class Base(DeclarativeBase):
    id: Any
    __name__: str

    # Generate __tablename__ automatically as the name of the class
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    