# Conhecendo os métodos: upper(), lower() e title()
curso = "linguagem pYthon"

print(curso.upper() + ", " + curso.lower() + ", " + curso.title())


# Conhecendo os métodos: strip(), lstrip() e rstrip()
curso = "   Python   Três   "

print(curso.strip() + ", " + curso.lstrip() + ", " + curso.rstrip() + "ENDofLINE")


# Conhecendo os métodos: center() e join()
curso = "Python"

print(curso.center(10, "#") + " | " + ".".join(curso) + " | " + "XZ".join(curso))
