from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DB_URL = f"postgresql://postgres:botjyudHjSdsRTlfUeUWWXbopTefACBw@mainline.proxy.rlwy.net:41024/railway"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
