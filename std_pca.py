import numpy as np
import cv2
import csv
import code

def csv_to_array(csv_file):
	'''
	[opearation]
	'''
	vector_list = list()
	id_list = list()

	csv_reader = open(csv_file, 'r')
	whole_data = csv_reader.readlines()
	count = 0

	for data in whole_data:
		data = data[:-1] # remove /n at the end
		data = data.split(',')
		vector_list.append(data[2:]) # matrix.flatten()
		id_list.append(data[0])
		count+=1
		if (count % 100 ==0):
			print('csv_to_array:', count)

	data_array = np.array(vector_list) # Conversion into numpy array

	return id_list, data_array

def standardization(matrix):
	'''
    [operation]
        - standardize the given row-vector
	'''
	print('Standardization')
	from sklearn import preprocessing
	# .fit() tests if the matrix is suitable for pre-processing
	scaler = preprocessing.StandardScaler().fit(matrix)
	# Actual transformation step.
	std_train_matrix = scaler.transform(matrix)

	return std_train_matrix

def pca(matrix):
	'''
	[operation]
		- Reduce the variables(features) through PCA
		  e.g. 100x100 (10000) features will be reduced to 8 features.
	'''
	from sklearn.decomposition import PCA
	print('PCA working')
	pca = PCA(n_components=8, svd_solver='randomized', whiten=True).fit(matrix)
	pca_matrix = pca.transform(matrix)

	return pca_matrix

if __name__ == '__main__':

    id_list, matrix = csv_to_array(file)
    std_matrix = standardization(matrix)
    pca_matrix = pca(std_matrix)
	pca_list = list(pca_matrix)
    # objective = 39152 x 8 matrix into 2447 x 128 matrix

    cuts = 16 # 16 cuts of MRI images per patient

    new_list = list()
    id_sorted = list()
    position_count = 0
    new_row = list()

    for number, rows in enumerate(pca_matrix):
    	print(list(rows))

    	print('Rearrangement:', number)
    	natural_number = number + 1
    	cut_count = 0

    	if natural_number % 16 == 0:
    		id_sorted.append(id_list[number])
    		new_list.append(new_row)
    		new_row = list()
    	else:
    		#code.interact(local=dict(globals(), **locals()))
    		new_row += list(rows)
			
	print(new_array[0])

	csv = open('pca_reconstruct.csv', 'w')
	for i in range(len(new_list)):
	    csv.write(str(id_sorted[i]) + ',' + str(new_list[i]) + '\n')

	csv.close()
