from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def download_from_drive(folder_name):
	gauth = GoogleAuth()
	print("Establishing Connection with Google Drive ....")
	drive = GoogleDrive(gauth)

	file_list = drive.ListFile(
		{'q': "'{}' in parents and trashed=false".format('1rnheo0nFGC4uOqeZszq29fC1CrLCQtsX')}).GetList()

	for i, file in enumerate(sorted(file_list, key=lambda x: x['title']), start=1):
		print('Downloading from GDrive .... {} ....  ({}/{})'.format(file['title'], i, len(file_list)))
		filename = folder_name + "/" + file['title']
		file.GetContentFile(filename)

	print("\n--------  Download Completed !!  --------\n")
