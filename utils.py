from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Leo', idade='44')
    db_session.add(pessoa)
    db_session.commit()
    #db_session.save()
    print(pessoa)


def consulta():
    pessoa = Pessoas.query.all()
    #print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Leo').first()
    
    

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Leo').first()
    pessoa.idade = 31
    pessoa.save()

if __name__ == '__main__':
    insere_pessoas()
    consulta()
    altera_pessoa
    
