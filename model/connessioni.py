from dataclasses import dataclass

from model.artObject import ArtObject


@dataclass
class Connessione:
    v1: ArtObject #qui si potevano inserire interi (object_id)
    v2: ArtObject
    peso: int

    def __str__(self):
        return f"Arco: {self.v1.object_id} - {self.v2.object_id} - peso: {self.peso}"

