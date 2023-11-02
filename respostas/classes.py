class Professor:
  def __init__(self, nome):
      self.nome = nome
      self.disciplinas = []

  def adicionar_disciplina(self, disciplina):
      self.disciplinas.append(disciplina)

  def listar_disciplinas(self):
      print(f"Professor {self.nome} ensina as seguintes disciplinas:")
      for disciplina in self.disciplinas:
          print(disciplina.nome)
        
class Disciplina:
  def __init__(self, nome, professor):
      self.nome = nome
      self.professor = professor
      self.atividades = {}

  def adicionar_atividade(self, nome_atividade, data):
      if data not in self.atividades:
          self.atividades[data] = nome_atividade
          print(f"Atividade '{nome_atividade}' dia {data} para disciplina {self.nome}")
      else:
          print(f"Já existe uma atividade em {data} para a disciplina {self.nome}")

  def listar_atividades(self):
      print(f"Atividades da disciplina {self.nome}:")
      for data, atividade in self.atividades.items():
          print(f"{data}: {atividade}")

class Atividade:
  def __init__(self, nome, data):
      self.nome = nome
      self.data = data
      self.disciplina = None

  def __str__(self):
      return f"{self.nome} ({self.data})"
