from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Policy:
    policy_id: str
    transaction_date: datetime
    total_premium: float
    total_claims: float
    province: str
    postal_code: str
    vehicle_type: str
    gender: str
    make: str

@dataclass
class Client:
    client_id: str
    gender: str
    province: str
    postal_code: str

@dataclass
class Claim:
    claim_id: str
    amount: float
    date: datetime
