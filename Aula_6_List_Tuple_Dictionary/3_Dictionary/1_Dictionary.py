# utiliza uma associação chave/valor

paises = { "Brasil":"Brasilia", "Uruguai":"Montevideu" , "Espanha":"Madrid" }


print(paises)

capital = paises["Uruguai"]

print(capital)

paises["Italia"] = "Quarai"

print(paises)

paises["Italia"] = "Roma"

print(paises)

#eliminar elemento

del paises["Brasil"]

print(paises)


#exemplo


superficies   = {"Brasil":[25,1000,2258,11002,3668,1000], "Italia":[25885,778,889,500]}

print(superficies["Brasil"])


# funções

print(paises.keys())

print(paises.values())

















