import pandas as pd

file_path2 = "especificaciones2.xlsx"
df2 = pd.read_excel(file_path2)
specifications = []
for index, row in df2.iterrows():
    name = row["name"]
    brand = row["brand"]
    measure = row["measure"]
    materials = row["materials"]
    color = row["color"]
    style = row["style"]
    guarantee = row["guarantee"]
    country = row["country"]
    observations = row["observations"]
    specifications.append(
        {
            "name": name,
            "specs": {
                "brand": brand,
                "Medidas": measure,
                "Materiales": materials,
                "Color": color,
                "Estilo": style,
                "Garantía": guarantee,
                "Pais de Origen": country,
                "Observaciones": observations,
            },
        }
    )
specs = [
    ["Medidas", 37, "Texto"],
    ["Materiales", 34, "Texto"],
    ["Color", 452, "Combo"],
    ["Estilo", 35, "Texto"],
    ["Garantía", 30, "Texto"],
    ["Pais de Origen", 31, "Radio"],
    ["Observaciones", 32, "Texto"],
]


def buscar_clave_en_lista(diccionarios, clave):
    for diccionario in diccionarios[:1]:
        name = diccionario["name"]

        if name == clave:
            print(f"{name} == {clave}")
            return diccionario
        else:
            return None


file_path = "pobre_juan.xlsx"
df = pd.read_excel(file_path)

result = []
ids = []
counter = 0

for index, row in df.iterrows():
    id = row["id"]
    nombre = row["nombre"]
    seller = row["seller"]
    if id not in ids:
        my_dict = None
        for s in specifications:
            name = s["name"]
            if name == seller:
                my_dict = s

        counter += 1
        ids.append(id)
        for spec in specs:
            new_dict = {
                "id": id,
                "name": nombre,
                "seller": seller,
                "spec": spec[0],
                "spec_id": spec[1],
                "spec_type": spec[2],
            }

            if my_dict is not None:
                value = my_dict["specs"]
                value = value.get(spec[0], None)
                new_dict["value"] = value

            result.append(new_dict)


df = pd.DataFrame(result)
file_path = "output.xlsx"
df.to_excel(file_path, index=False)