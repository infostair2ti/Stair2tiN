products = [
    {
        'Nombre': 'Zapatos XYZ',
        'Código de barras': '8569741233658',
        'Fabricante': 'Deportes XYZ',
        'Categoría': 'Zapatos',
        'Género': 'Masculino',
    },
    {
        'Nombre': 'Zapatos ABC',
        'Código de barras': '7452136985471',
        'Fabricante': 'Deportes XYZ',
        'Categoría': 'Zapatos',
        'Género': 'Femenino'
    },
    {    
        'Nombre': 'Camisa DEF',
        'Código de barras': '5236412896324',
        'Fabricante': 'Deportes XYZ',
        'Categoría': 'Camisas',
        'Género': 'Masculino'
    },
    {
        'Nombre': 'Zapatos ABC',
        'Código de barras': '7452136985471',
        'Fabricante': 'Deportes XYZ',
        'Categoría': 'Zapatos',
        'Género': 'Femenino'
    },
    {
        'Nombre': 'Camisa DEF',
        'Código de barras': '5236412896324',
        'Fabricante': 'Deportes XYZ',
        'Categoría': 'Camisas',
        'Género': 'Masculino'
    },{
        'Nombre': 'Bolso KLM',
        'Código de barras': '5863219635478',
        'Fabricante': 'Carteras Hi-Fashion',
        'Categoría': 'Bolsos',
        'Género': 'Femenino'
    }
]

def group_by(products):
    data = {}

    for product in products:
        maker = product.get('Fabricante','')
        category = product.get('Categoría','')
        gender = product.get('Género','')

        if maker not in data:
            data[maker] = {}

        if category not in data[maker]:
            data[maker][category] = {}

        if gender not in data[maker][category]:
            data[maker][category][gender] = []

        data[maker][category][gender].append(product)

    return data

if __name__ == "__main__":
    print("Point D")
    resultado = group_by(products)
    print(resultado)