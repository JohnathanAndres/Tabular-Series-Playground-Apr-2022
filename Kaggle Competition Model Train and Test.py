{
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import tensorflow as tf
    import keras
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.layers import LSTM
   }
  
  {
   
    X_test = pd.read_csv('test.csv')
    X_train=pd.read_csv('train.csv')
    Y_train=pd.read_csv('train_labels.csv'
   
  },
  {
    sequence_0=X_train.loc[X_train['sequence']==0]
    sequence_1=X_train.loc[X_train['sequence']==1]
    Features=['sensor_00','sensor_01','sensor_02','sensor_03','sensor_04','sensor_05','sensor_06','sensor_07','sensor_08','sensor_09','sensor_10','sensor_11','sensor_12']
   
  },
    
    {
    
    XTrain=np.empty((100,60,16))
    i=0
    for i in range(100):
        sequence=[np.array(traincsv.loc[traincsv['sequence']==i])]
        XTrain+=sequence
    
    XTrain.shape
   
  },
    {
    YTrain=train_labelscsv['state']
    YTrain=YTrain[:100]
    YTrain.shape
   
  },
  {
   
    XTest=np.empty((100,60,16))
    
    for i in range(100):
        sequence_1=[np.array(testcsv.loc[testcsv['sequence']==i])]
        XTest+=sequence
    XTest.shape
   
  }
      
{
 #This is where I am going to construct the model
   model = Sequential()
   model.add(LSTM(100, input_shape=(60,16)))
   model.add(Dense(100, activation='relu'))
   model.add(Dense(1, activation='sigmoid'))
   model.compile( loss='binary_crossentropy',optimizer='adam',metrics=[tf.keras.metrics.AUC()])               
   history=model.fit(XTrain,YTrain,epochs=10,batch_size=20)

 }
    loss_over_epoch_train=[.7139,.6944,.6957,.6998,.6939,.6985,.6948,.6946,.6943,.6946]
    auc_over_epoch_train=[0.4432,.4799,.4846,.4838,.4802,.4747,.4736,.4723,.4719,.4754]
 {
  #Validation 
  plt.plot(list(range(0,60)),np.array(sequence_0[Feature]))
  
  
  print(history.history)
  plt.plot(range(len(history.history["loss"])),history.history["loss"],label="Training Loss")
  plt.plot(range(len(history.history["auc_3"])),history.history["auc_3"],label="AUC ROC")
  plt.legend()
  
  
  
  
  
  
  
  }