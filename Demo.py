import PyPDF2
import openai

# Configurar sua chave de API do OpenAI
openai.api_key = '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'

# Função para ler o texto de um arquivo PDF
def ler_pdf(nome_arquivo):
    texto = ""
    with open(nome_arquivo, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for pagina_num in range(len(pdf_reader.pages)):
            pagina = pdf_reader.pages[pagina_num]
            texto += pagina.extract_text()
    return texto

# Função para resumir o texto usando a API do ChatGPT
def resumir_texto(texto):
    resposta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=texto,
        max_tokens=50,  # Ajuste o número de tokens desejado para o resumo
        n=1,
        stop=None,
        temperature=0.7
    )
    return resposta.choices[0].text.strip()

# Nome do arquivo PDF que você deseja ler e resumir
nome_arquivo_pdf = 'Teste.pdf'

# Ler o texto do arquivo PDF
texto_pdf = ler_pdf(nome_arquivo_pdf)

# Resumir o texto
resumo = resumir_texto(texto_pdf)

# Criar um novo arquivo PDF com o resumo
novo_nome_arquivo_pdf = 'Resumo.pdf'
with open(novo_nome_arquivo_pdf, 'wb') as novo_pdf_file:
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(PyPDF2.PdfPage())
    pdf_writer.getPage(0).mergePage(PyPDF2.PdfFileReader(text=resumo).getPage(0))
    pdf_writer.write(novo_pdf_file)

print(f"O resumo foi salvo no arquivo '{novo_nome_arquivo_pdf}'")
