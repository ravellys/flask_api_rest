from typing import List
import pandas as pd


def calcular_imc(peso: float, altura: float) -> float:
    return peso / altura ** 2


def get_estatisticas(imcs: List[dict]) -> dict:
    df = pd.DataFrame(imcs)
    return df.describe().to_dict()
