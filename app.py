from google_drive import GoogleDrive


client_secrets_file = 'drive.json'
drive = GoogleDrive(client_secret_file=client_secrets_file)
drive.authenticate()
