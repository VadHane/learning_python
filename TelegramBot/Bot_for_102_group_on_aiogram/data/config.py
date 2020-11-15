from database import fetchall

BOT_TOKEN = '1430787728:AAF9TxnmKInB6n8Bl-r7MndahQc223a9-cE'

_ADMINS_ID = fetchall('admins', 'id_user')
ADMINS_ID = [643559378]
USER_ID = []
_USER_ID = fetchall('users', 'id_user')
for element in _USER_ID:
    USER_ID.append(int(element[0]))

for element in _ADMINS_ID:
    ADMINS_ID.append(int(element[0]))
