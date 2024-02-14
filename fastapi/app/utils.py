from passlib.context import  CryptContext


pwd_context = CryptContext(schemes=["bcrypt"],  deprecated="auto")

def generate_hash(string : str):
    return pwd_context.hash(string)

def login(hashed_password : str, password : str):
    return pwd_context.verify(password, hashed_password)