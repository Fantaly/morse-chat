from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
"""
This module provides the database configuration and session management for the application.

- `SQLALCHEMY_DATABASE_URL`: The URL for the SQLite database.
- `engine`: The SQLAlchemy engine used to connect to the database.
- `SessionLocal`: The session factory used to create database sessions.
- `Base`: The base class for declarative models.
"""
