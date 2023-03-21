from dataclasses import dataclass


@dataclass
class RegisterInputEntity:
    username: str
    password: str


@dataclass
class RegisterResponseEntity:
    user_id: int
