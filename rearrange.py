file = 'patients_all.csv'

def rearrangement(file):

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

    csv = open('pca_reconstruct.csv', 'w')

    for i in range(len(new_list)):
    	csv.write(str(id_sorted[i]) + ',' + str(new_list[i]) + '\n')

    csv.close()

if __name__ == '__main__':

    rearrangement('patients_pca_both.csv')
