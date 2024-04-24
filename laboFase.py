import easyocr

reader = easyocr.Reader(['pt'])

results = reader.readtext('Placa1.jpg', paragraph=False)

for result in results:
    print(f'Texto: {result[0]}\n'
          f'posicao: {result[1]}\n')