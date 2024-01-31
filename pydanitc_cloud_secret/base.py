from dataclasses import dataclass

@dataclass
class GetSecret:
    key: str
    region: str
