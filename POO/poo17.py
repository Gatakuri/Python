# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...

class OtherError(Exception):
    ...

def throw():
    exception_ = MyError("a", "b", "c")
    exception_.add_note("Look the note 1")
    raise exception_

try:
    throw()
except (MyError, ZeroDivisionError) as error:
    print(error.args, error.__class__.__name__)
    print()
    exception_ = OtherError("I'll throw other error")
    exception_.add_note("One more note")
    # exception_.__notes__ += error.__notes__.copy()
    raise exception_
