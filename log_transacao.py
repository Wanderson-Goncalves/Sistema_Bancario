from datetime import datetime
import pytz

def log_transacao(func):
    def wrapper(*args, **kwargs):
      funcao = func(*args, **kwargs)
       # Obtendo o horário atual no UTC
      data_utc = datetime.now(pytz.utc)
        
        #  Definindo o fuso horário para "America/Sao_Paulo"
      fuso_horario_sao_paulo = pytz.timezone("America/Sao_Paulo")
        
        #Convertendo p horário UTC para o fuso horário especificado
      horario_sao_paulo = data_utc.astimezone(fuso_horario_sao_paulo)
        
      print(f"\n####\t {horario_sao_paulo.strftime('%d/%m/%Y %H:%M:%S')}\t ####")

      return funcao
    return wrapper
        
        