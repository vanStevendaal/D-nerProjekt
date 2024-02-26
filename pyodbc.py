import pyodbc
from funktionen import daten_inkonsistenz
# Verbindungsdaten
server = 'sc-db-server.database.windows.net'
database = 'supplychain' # Setze den Namen deiner Datenbank hier ein
username = 'rse'
password = 'Pa$$w0rd'
# Verbindungsstring
conn_str = (
f'DRIVER={{ODBC Driver 17 for SQL Server}};'
f'SERVER={server};'
f'DATABASE={database};'
f'UID={username};'
f'PWD={password}'
)

# Verbindung herstellen
conn = pyodbc.connect(conn_str)
output_list =[]
# Cursor erstellen
cursor = conn.cursor()
transport_id = input("Geben sie ihre Transport_ID ein " )
# SQL-Statement ausführen
cursor.execute('SELECT * FROM coolchain WHERE transportid = ?', transport_id)

zeitstempel=[zeit[5] for zeit in cursor]   

print(zeitstempel)

# Ergebnisse ausgeben

for row in cursor:
    print(row)
    output_list.append(row)

# Verbindung schließen
cursor.close()
conn.close()