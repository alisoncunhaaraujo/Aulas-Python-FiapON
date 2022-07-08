usuarios = {}
print(usuarios)

usuarios = {
    "chaves": ["Chaves do 8", "24/06/2022", "Recep)_01"],
    "quico":  ["Quico das Flores", "20/06/2022", "Raiox_03"]
}
print(usuarios)

usuarios["florinda"] = ["Dona Florinda", ["Dona Florinda"], "24/06/2022, Raiox_01"]
print(usuarios)

print("########################-----########################")
print(usuarios.get("quico"))
print("########################-----########################")