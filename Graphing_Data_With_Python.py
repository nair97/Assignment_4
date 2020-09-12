#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 05:54:28 2020

@author: meerarakesh09
"""
#import modules
import numpy as np
import matplotlib.pyplot as plt

def read_data(inFileName):
    #to access the data from txt
    plotData = np.genfromtxt(inFileName, names=True)
    return plotData

def plot_data( plotData, outFileName ):
    '''Uses matplotlib module to generate a single page figure with three 
    panels.  Accepts the data structure from read_data and the name of an
    outputfile, and generates a PDF file with the figure.'''

    #to set the size of the figures
    plt.figure(figsize = (10,7))
     
    # to subplot 3 plots in same plot
    plt.subplot(3,1,1)
    
    # include Mean, Max, Min in black, red and blue for top plot Streamflow(cfs)
    plt.plot(plotData['Year'], plotData['Mean'], color = 'black', label = 'Mean' )
    plt.plot(plotData['Year'], plotData['Max'], color = 'red', label = 'Max')
    plt.plot(plotData['Year'], plotData['Min'], color = 'blue', label = 'Min')
    
    #label x and y axis for top plot
    plt.xlabel('Year')
    plt.ylabel('Streamflow(cfs)')
    
    #plot legend
    plt.legend(loc='upper right')
    
    #middle plot TqMean (%)
    plt.subplot(3,1,2)
    plt.plot(plotData['Year'], plotData['Tqmean']*100,'gs')
    
    #label x and y axis for middle plot
    plt.xlabel('Year')
    plt.ylabel('Tqmean (%)')
    
    #bottom plot RB index (ratio)
    plt.subplot(3,1,3)
    plt.plot(plotData['Year'], plotData['RBindex'],"g^")
    
    #label x and y axis for bottom plot
    plt.xlabel('Year')
    plt.ylabel('RBindex (ratio)')
    
    # save output as PDF
    plt.savefig(outFileName)
    plt.close()
    
# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
    
if __name__ == '__main__':
     '''Use this part of the program to prompt the user for the name of the 
    datafile to print, and then read in the contents of that file, and produce
    a plot matching the assignment requirements.'''
    
    print('Enter any file : Tippecanoe_River_at_Ora.Annual_Metrics.txt or Wildcat_Creek_at_Lafayette.Annual_Metrics.txt\n')
    inFileName = str(input())
    print('Enter any file :Tippecanoe_River_at_Ora.Annual_Metrics.pdf or Wildcat_Creek_at_Lafayette.Annual_Metrics.pdf\n')           
    outFileName = str(input())

    plotData = read_data(inFileName)  
    plot_data(plotData, outFileName)

    
    
    
    