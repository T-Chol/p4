class Config:
    """Base configuration."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sclateshow.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False