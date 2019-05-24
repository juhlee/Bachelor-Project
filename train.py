from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score, roc_curve, auc
import numpy as np
import code

def csv_to_array(csv_file):

    global label_dict

    csv_reader = open(csv_file, 'r')
    label_lines = csv_reader.readlines()

    label_dict = dict()

    # CLASS.CSV processing
    for line in label_lines:
        id, label = line.strip().split(',')[0], int(line.strip().split(',')[1])

        if label < 2:
            label_dict[id] = '0'
        elif 2 <= label <= 6:
            label_dict[id] = '1'
        else:
            label_dict[id] = '99'

    csv_reader.close()

    return label_dict

def pca_process(pca_csv):

    # PCA.csv file processing
    pca_reader = open(pca_csv, 'r')
    pca_lines = pca_reader.readlines()

    X_train, y_train = [],[]

    for line in pca_lines:
        # Removing '\n' at the end
        line = line.strip().replace('[', '').replace(']', '').split(',')
        id = line[0] # '1', '2' ... '2643'
        vector = list(line[1:]) # '[row_vector 'str']'
        vector = [float(i) for i in vector]

        X_train.append(vector)
        global label_dict
        y_train.append(int(label_dict[id]))

    return X_train, y_train

def plot_roc_curve(fpr, tpr, alg):
    import matplotlib.pyplot as plt
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve of '+ alg)
    plt.legend()
    plt.show()

if __name__ == '__main__':

    data_array = csv_to_array('class.csv')
    X_train, y_train = pca_process('pca_reconstruct_original.csv')
    X_train1, y_train1 = pca_process('pca_reconstruct_original.csv')
    '''
    X_train = X_train + X_train1
    y_train = y_train + y_train1
    '''
    # Dividing into test and train datasets
    # 'Cross validation' = a function that averages different training result of different combinations of train-and-test dataset.
    # Code exists! -> sklearn website visit.
    # Adaboost and KNN =>
    from sklearn.model_selection import train_test_split
    from sklearn import datasets
    from sklearn import svm

    # Cross-validation
    X_train, X_test, y_train, y_test = train_test_split(
        X_train, y_train, test_size = 0.2, random_state = 0
    )

    classifier_1 = AdaBoostClassifier()
    classifier_1.fit(X_train, y_train)
    # Add KNN classifier

    classifier_2 = KNeighborsClassifier()
    classifier_2.fit(X_train, y_train)

    y_pred = classifier_1.predict(X_test)
    y_pred2 = classifier_2.predict(X_test)

    Ada_Result = classification_report(y_pred, y_test)
    Ada_scores = roc_auc_score(y_pred, y_test)
    KNN_result = classification_report(y_pred2, y_test)
    KNN_scores = roc_auc_score(y_pred2, y_test)

    code.interact(local=dict(globals(), **locals()))

    # Compute ROC curve and ROC area for each class
    print(Ada_Result)
    print(KNN_result)
    fpr, tpr, thresh = roc_curve(y_test, y_pred)
    plot_roc_curve(fpr, tpr, 'Adaboost with augmented data')
    print('ada', auc(fpr, tpr))
    print('accuracy_')
    fpr, tpr, thres = roc_curve(y_test, y_pred2)
    plot_roc_curve(fpr, tpr, 'KNN with original data')
    print('KNN', auc(fpr, tpr))

    '''
    # Accuracy
    from sklearn.metrics import confusion_matrix

    # Adaboost
    cm_ada = confusion_matrix(y_test, y_pred)
    cm_knn = confusion_matrix(y_test, y_pred2)

    cm_ada = cm_ada.astype('float') / cm_ada.sum(axis=1)[:, np.newaxis]
    cm_knn = cm_knn.astype('float') / cm_knn.sum(axis=1)[:, np.newaxis]

    print('Adaboost original', cm_ada.diagonal())
    print('KNN augmented', cm_knn.diagonal())
    '''
