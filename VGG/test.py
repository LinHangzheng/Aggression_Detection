from VGG import *

if __name__ == '__main__':
    # get the work path
    path = os.getcwd()
    os.chdir(path)
    os.listdir(path)
    print (path) 

    # name list of all dataset 
    data_kind_list = ["Movie Dataset", "HockeyFights", "Surveillance Camera Fight Dataset", "youtube_fight"]
    train_data_kind = data_kind_list[0]
    test_data_kind = data_kind_list[3]
    data_kind_list = data_kind_list[:2]

    RUN_ALL = True # whether to train on all dataset
    L = 10 # 5 or 10

    if not RUN_ALL:
        h5_path = path + "/VGG/weights/weights_"+str(L)+"_"+train_data_kind+".best.hdf5"
    else:
        h5_path = path + "/VGG/weights/weights_"+str(L)+"_All.best.hdf5"

   
    test_file1, test_file2, test_file3 = preprocess(path,USE_NPY=True,RUN_ALL=False,data_kind=test_data_kind, data_list=data_kind_list,L=L)
    test_file = test_file1 + test_file2 + test_file3

    test_generator = npy_generator (test_file, 1,L)

		
    model = VGG_Model(L=L)
    model.load_weights(h5_path)
    model.test(test_generator, len(test_file))

    
