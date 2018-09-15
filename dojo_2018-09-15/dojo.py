def converte_romano(numero):
    if not isinstance(numero, int):
        raise ValueError("Somente inteiros são permitidos")
    if numero < 0:
        return "-" + converte_romano(-numero)
    valores_romanos = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
    ]
    for v, r in valores_romanos:
        if numero >= v:
            return r + converte_romano(numero - v)
    return "I" * numero


import pytest

def test_onze():
    assert converte_romano(11) == 'XI'

def test_treze():
    assert converte_romano(13) == 'XIII'

def test_vinte():
    assert converte_romano(20) == 'XX'

def test_vinte_e_um():
    assert converte_romano(21) == 'XXI'

def test_vinte_e_dois():
    assert converte_romano(22) == 'XXII'

def test_trinta():
    assert converte_romano(30) == 'XXX'

def test_trinta_e_tres():
    assert converte_romano(33) == 'XXXIII'

def test_cinquenta():
    assert converte_romano(50) == 'L'

def test_cem():
    assert converte_romano(100) == 'C'

def test_duzentos():
    assert converte_romano(200) == 'CC'

def test_quinhentos():
    assert converte_romano(500) == 'D'

def test_menos_um():
    assert converte_romano(-1) == "-I"

def test_meio():
    with pytest.raises(ValueError):
        assert converte_romano(.5)

tabela_romanos = [
    (0, ''),
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
    (9, 'IX'),
    (10, 'X'),
    (12, 'XII'),
    (14, 'XIV'),
    (15, 'XV'),
    (16, 'XVI'),
    (17, 'XVII'),
    (18, 'XVIII'),
    (19, 'XIX'),
    (23, 'XXIII'),
    (24, 'XXIV'),
    (25, 'XXV'),
    (26, 'XXVI'),
    (27, 'XXVII'),
    (28, 'XXVIII'),
    (29, 'XXIX'),
    (42, 'XLII'),
    (47, 'XLVII'),
    (60, 'LX'),
    (90, 'XC'),
    (390, 'CCCXC'),
    (442, 'CDXLII'),
    (460, 'CDLX'),
    (520,'DXX'),
    (890,'DCCCXC'),
    (900, 'CM'),
    (1000, 'M'),
    (1001, 'MI'),
    (1002, 'MII'),
    (1003, 'MIII'),
    (1010, 'MX'),
    (1100, 'MC'),
    (2999, 'MMCMXCIX'),
    (3000, 'MMM'),
    (3960, 'MMMCMLX'),
    (3999, 'MMMCMXCIX'),
]

@pytest.mark.parametrize("entrada, esperado", tabela_romanos)
def test_tabela(entrada, esperado):
    assert converte_romano(entrada) == esperado
