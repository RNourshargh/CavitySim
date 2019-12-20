# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:19:33 2019

@author: bjs697
"""
import numpy as np
import os
import glob


class octoscope:
    
    def saveData(folder,fileStart,fileStop,skipLines=0,headerSize=15):
        """
        Loads the saved CSV data from the octoscope (Yokogawa DLM4000)
        
        Parameters
        ----------
            folder : file, str 
                The full path of the folder where the data files are
            
            fileStart : number
                Which file should be loaded from. For first file, use 0
            
            fileStop : number
                Last file to load +1
            
            skipLines : number, optional
                Additional lines to skip in the data, not the header
                
            headerSize : number, optional
                Change the header size, may be useful for different scope data. Not recommended.
            
            
        Returns
        -------
        print : 'Saved data to folder X' 
        
        Data is saved to new file in folder location, as dataXXX.npy where XXX is the original file name
        
        Format of Data is [row,column,channelNo], column[0] is time, column[1] is voltage.
        
        """
        path = folder+os.sep
        file_names = os.listdir(folder)
        file_names.sort()
        file_names = file_names[fileStart:fileStop]

        
        for i, file in enumerate(file_names):
            settings = {}
            settings_start = 0  # Line numbers for settings
            settings_end = headerSize
            f = open(path+file)
            for i, line in enumerate(f.readlines()):
                if i in range(settings_start, settings_end + 1):
                    line = line.strip('\n').split(',')
                    settings[line[0]] = line[1:]        
            timeRes = np.array(settings['"HResolution"           ']).astype(float)
            blockSize = np.array(settings['"BlockSize"             ']).astype(int)
            voltageOffset = np.array(settings['"HOffset"               ']).astype(float)
            noChannels = len(timeRes)
            
            
            fileData = np.loadtxt(path+file,delimiter=',',skiprows=headerSize+skipLines,usecols=list(np.arange(1,1+noChannels)))
            data = np.zeros((blockSize[0],2,noChannels))
            for i in range(noChannels):
                data[:,0,i] = np.arange(0,blockSize[i]*timeRes[i],timeRes[i])
                if noChannels == 1:
                    data[:,1,i] = fileData[:]-voltageOffset[i]
                else:
                    data[:,1,i] = fileData[:,i]-voltageOffset[i]
                
            np.save(path+'data'+file[:-4], data)
        print("Saved data to folder "+folder)
        
        def loadData(folder,fileStart,fileStop):
            path = folder+os.sep
            file_names = glob.glob(path+'*.npy')
            file_names.sort()
            file_names = file_names[fileStart:fileStop]
            for i, file in enumerate(file_names):    
                temp = np.load(file)
                if i==0:
                    data = np.zeros((np.shape(temp)[0],np.shape(temp)[1],len(file_names)))
                data[:,:,i] = temp[:,:,0]
            
            return data