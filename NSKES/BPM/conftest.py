"""
В одном месте устанавливает ID сервера и bspid если нужно переключиться на другой сервер
ESTO - Тогучин
ESOR - Ордынск
ESBC - Чулым
ESKC - Коченево
"""

#bspids = [  'ESBP', 'ESBV', 'ESBH', 'ESBI', 'ESBM', 'ESBN', 'ESBO', 'ESBW', 'ESBJ', 'ESTO', 'ESOR', 'ESBC', 'ESBL',
#            'ESKC', 'ESBQ', 'ESBX', 'ESBD', 'ESBB', 'ESBZ', 'ESBS', 'ESBU', 'ESBY', 'ESBG', 'ESBR', 'ESBA', 'ESKU',
#            'ESTA', 'ESCH', 'ESCA', 'ESVE', 'ESUT', 'ESKK', 'ESB']

# server = '10.1.2.83/sirena'
server_test = '10.1.2.83/sirena'
server_ESOR ='{server}/sirena-ordynsk'
server_ESTO ='{server}/sirena-toguchin'
server_ESBS ='{server}/sirena-severnoe'
server_ESTA ='{server}/sirena-tatarsk'

server_test = '10.1.2.83'  # Для проверки 30 операции "Оплата" и 53 операция
server_test_ESOR = '10.1.2.83'    # Для проверки 30 операции "Оплата" и 53 оперция
server_test_ESBC = f'{server_test}/sirena-chulym'
server_test_ESTO = f'{server_test}/sirena-toguchin'
server_test_ESBI = f'{server_test}/sirena-berdsk'
server_test_ESBY = f'{server_test}/sirena-ubinskoe'
server_test_ESBB = f'{server_test}/sirena-kuybyshev'
server_test_ESCH = f'{server_test}/sirena-krasnozerskoe'
server_test_ESTA = f'{server_test}/sirena-tatarsk'

# bspids = ['ESB', 'ESTO', 'ESOR', 'ESBC']