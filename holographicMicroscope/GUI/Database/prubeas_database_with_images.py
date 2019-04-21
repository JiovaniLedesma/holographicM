#****************************************************************************************
# 		Módulos importados
#****************************************************************************************
import sqlite3
import os.path
from os import listdir, getcwd, remove
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc as sp
# from cv2 import *
import shutil
import time


#****************************************************************************************
# 		List files
#****************************************************************************************
def get_picture_list(rel_path):
	abs_path = os.path.join(os.getcwd(), rel_path)
	print('abs_path = ', abs_path)
	dir_files = os.listdir(abs_path)
	return dir_files

# picture_list = get_picture_list('img')
# print(picture_list)

#****************************************************************************************
# 		Create picture database
#****************************************************************************************
def create_or_open_db(db_file):
	db_is_new = not os.path.exists(db_file)
	conn = sqlite3.connect(db_file)
	if db_is_new:
		print('Creating schema')
		sql = '''create table if not exists PICTURES(
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		PICTURE BLOB,
		TYPE TEXT,
		FILE_NAME TEXT);'''
		conn.execute(sql) # shortcut for conn.cursor().execute(sql)
	else:
		print('Schema exists\n')
	return conn

def insert_picture(conn, picture_file):
	with open(picture_file, 'rb') as input_file:
		ablob = input_file.read()
		base = os.path.basename(picture_file)
		afile, ext = os.path.splitext(base)
		sql = '''INSERT INTO PICTURES
		(PICTURE, TYPE, FILE_NAME)
		VALUES(?, ?, ?);'''
		conn.execute(sql, [sqlite3.Binary(ablob), ext, afile])
		conn.commit()

#****************************************************************************************
# 		INSERT A IMAGE ON DATABASE
#****************************************************************************************
# 			EXAMPLE
#****************************************************************************************
# conn = create_or_open_db('picture_db.sqlite')
# picture_file = '/home/dark_fire/Documentos/Projects/Holographic microscope/holographicM/holographicMicroscope/GUI/img/SAO.jpg'
# insert_picture(conn, picture_file)
# conn.close()

#****************************************************************************************
# 		CREATING Schema
#****************************************************************************************
def extract_picture(cursor, picture_id):
	sql = 'SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = :id'
	param = {'id': picture_id}
	cursor.execute(sql, param)
	ablob, ext, afile = cursor.fetchone()
	filename = afile + ext
	with open(filename, 'wb') as output_file:
		output_file.write(ablob)
	return filename, afile

#****************************************************************************************
# 		EXAMPLE
#****************************************************************************************
conn = create_or_open_db('picture_db.sqlite')
cur = conn.cursor()
filename, name = extract_picture(cur, 2)
cur.close()
conn.close()
img = sp.imread(filename)
# img = imread(filename)
#********************************************************
# 		CON OPEN CV
#********************************************************
# W = 600
# height, width, depth = img.shape
# x, y = img.shape[1], img.shape[0]
# imgScale = W/width
# newX, newY = x*imgScale, y*imgScale
# img = resize(img, (int(newX), int(newY)))
# img = imshow("my image", img)
# waitKey()
#********************************************************
# 		CON PLOTS
#********************************************************
plt.imshow(img)
plt.axis('equal')
plt.show()


# move_file_to_folder(filename, 'Imagenes de DB')
os.mkdir('Imagenes de DB')
shutil.move('filename', './Imagenes de DB')



# os.remove(filename)
#****************************************************************************************