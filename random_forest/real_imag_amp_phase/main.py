# Importing modules
import funct as module
import pandas as pd
import numpy as np
import itertools 


Name =['Adiac','ArrowHead','Beef','BeetleFly','BirdChicken','Car','CBF','ChlorineConcentration','Coffee','Computers','CricketX','CricketY','CricketZ','DiatomSizeReduction','DistalPhalanxOutlineAgeGroup','DistalPhalanxOutlineCorrect','DistalPhalanxTW','Earthquakes','ECG200','ECG5000','ECGFiveDays','ElectricDevices','FaceAll','FaceFour','FacesUCR','FiftyWords','Fish','FordA','FordB','GunPoint','Ham','HandOutlines','Haptics','Herring','InlineSkate','ItalyPowerDemand','LargeKitchenAppliances','Lightning2','Lightning7','Mallat','Meat','MedicalImages','MiddlePhalanxOutlineAgeGroup','MiddlePhalanxOutlineCorrect','MiddlePhalanxTW','MoteStrain','NonInvasiveFetalECGThorax1','NonInvasiveFetalECGThorax2','OliveOil','OSULeaf','PhalangesOutlinesCorrect','Phoneme','Plane','ProximalPhalanxOutlineAgeGroup','ProximalPhalanxOutlineCorrect','ProximalPhalanxTW','RefrigerationDevices','ScreenType','ShapeletSim','ShapesAll','SmallKitchenAppliances','SonyAIBORobotSurface1','SonyAIBORobotSurface2','Strawberry','SwedishLeaf','Symbols','SyntheticControl','ToeSegmentation1','ToeSegmentation2','Trace','TwoLeadECG','TwoPatterns','UWaveGestureLibraryAll','UWaveGestureLibraryX','UWaveGestureLibraryY','UWaveGestureLibraryZ','Wafer','Wine','WordSynonyms','Worms','WormsTwoClass','Yoga','ACSF1','BME','Chinatown','Crop','DodgerLoopDay','DodgerLoopGame','DodgerLoopWeekend','EOGHorizontalSignal','EOGVerticalSignal','EthanolLevel','FreezerRegularTrain','FreezerSmallTrain','Fungi','GunPointAgeSpan','GunPointMaleVersusFemale','GunPointOldVersusYoung','HouseTwenty','InsectEPGRegularTrain','InsectEPGSmallTrain','MelbournePedestrian','MixedShapesSmallTrain','PigAirwayPressure','PigArtPressure','PigCVP','PowerCons','Rock','SemgHandGenderCh2','SemgHandMovementCh2','SemgHandSubjectCh2','SmoothSubspace','UMD']
l=['Adiac_TRAIN.arff','ArrowHead_TRAIN.arff','Beef_TRAIN.arff','BeetleFly_TRAIN.arff','BirdChicken_TRAIN.arff','Car_TRAIN.arff','CBF_TRAIN.arff','ChlorineConcentration_TRAIN.arff','Coffee_TRAIN.arff','Computers_TRAIN.arff','CricketX_TRAIN.arff','CricketY_TRAIN.arff','CricketZ_TRAIN.arff','DiatomSizeReduction_TRAIN.arff','DistalPhalanxOutlineAgeGroup_TRAIN.arff','DistalPhalanxOutlineCorrect_TRAIN.arff','DistalPhalanxTW_TRAIN.arff','Earthquakes_TRAIN.arff','ECG200_TRAIN.arff','ECG5000_TRAIN.arff','ECGFiveDays_TRAIN.arff','ElectricDevices_TRAIN.arff','FaceAll_TRAIN.arff','FaceFour_TRAIN.arff','FacesUCR_TRAIN.arff','FiftyWords_TRAIN.arff','Fish_TRAIN.arff','FordA_TRAIN.arff','FordB_TRAIN.arff','GunPoint_TRAIN.arff','Ham_TRAIN.arff','HandOutlines_TRAIN.arff','Haptics_TRAIN.arff','Herring_TRAIN.arff','InlineSkate_TRAIN.arff','ItalyPowerDemand_TRAIN.arff','LargeKitchenAppliances_TRAIN.arff','Lightning2_TRAIN.arff','Lightning7_TRAIN.arff','Mallat_TRAIN.arff','Meat_TRAIN.arff','MedicalImages_TRAIN.arff','MiddlePhalanxOutlineAgeGroup_TRAIN.arff','MiddlePhalanxOutlineCorrect_TRAIN.arff','MiddlePhalanxTW_TRAIN.arff','MoteStrain_TRAIN.arff','NonInvasiveFetalECGThorax1_TRAIN.arff','NonInvasiveFetalECGThorax2_TRAIN.arff','OliveOil_TRAIN.arff','OSULeaf_TRAIN.arff','PhalangesOutlinesCorrect_TRAIN.arff','Phoneme_TRAIN.arff','Plane_TRAIN.arff','ProximalPhalanxOutlineAgeGroup_TRAIN.arff','ProximalPhalanxOutlineCorrect_TRAIN.arff','ProximalPhalanxTW_TRAIN.arff','RefrigerationDevices_TRAIN.arff','ScreenType_TRAIN.arff','ShapeletSim_TRAIN.arff','ShapesAll_TRAIN.arff','SmallKitchenAppliances_TRAIN.arff','SonyAIBORobotSurface1_TRAIN.arff','SonyAIBORobotSurface2_TRAIN.arff','Strawberry_TRAIN.arff','SwedishLeaf_TRAIN.arff','Symbols_TRAIN.arff','SyntheticControl_TRAIN.arff','ToeSegmentation1_TRAIN.arff','ToeSegmentation2_TRAIN.arff','Trace_TRAIN.arff','TwoLeadECG_TRAIN.arff','TwoPatterns_TRAIN.arff','UWaveGestureLibraryAll_TRAIN.arff','UWaveGestureLibraryX_TRAIN.arff','UWaveGestureLibraryY_TRAIN.arff','UWaveGestureLibraryZ_TRAIN.arff','Wafer_TRAIN.arff','Wine_TRAIN.arff','WordSynonyms_TRAIN.arff','Worms_TRAIN.arff','WormsTwoClass_TRAIN.arff','Yoga_TRAIN.arff','ACSF1_TRAIN.arff','BME_TRAIN.arff','Chinatown_TRAIN.arff','Crop_TRAIN.arff','DodgerLoopDay_TRAIN.arff','DodgerLoopGame_TRAIN.arff','DodgerLoopWeekend_TRAIN.arff','EOGHorizontalSignal_TRAIN.arff','EOGVerticalSignal_TRAIN.arff','EthanolLevel_TRAIN.arff','FreezerRegularTrain_TRAIN.arff','FreezerSmallTrain_TRAIN.arff','Fungi_TRAIN.arff','GunPointAgeSpan_TRAIN.arff','GunPointMaleVersusFemale_TRAIN.arff','GunPointOldVersusYoung_TRAIN.arff','HouseTwenty_TRAIN.arff','InsectEPGRegularTrain_TRAIN.arff','InsectEPGSmallTrain_TRAIN.arff','MelbournePedestrian_TRAIN.arff','MixedShapesSmallTrain_TRAIN.arff','PigAirwayPressure_TRAIN.arff','PigArtPressure_TRAIN.arff','PigCVP_TRAIN.arff','PowerCons_TRAIN.arff','Rock_TRAIN.arff','SemgHandGenderCh2_TRAIN.arff','SemgHandMovementCh2_TRAIN.arff','SemgHandSubjectCh2_TRAIN.arff','SmoothSubspace_TRAIN.arff','UMD_TRAIN.arff']
l1=['Adiac_TEST.arff','ArrowHead_TEST.arff','Beef_TEST.arff','BeetleFly_TEST.arff','BirdChicken_TEST.arff','Car_TEST.arff','CBF_TEST.arff','ChlorineConcentration_TEST.arff','Coffee_TEST.arff','Computers_TEST.arff','CricketX_TEST.arff','CricketY_TEST.arff','CricketZ_TEST.arff','DiatomSizeReduction_TEST.arff','DistalPhalanxOutlineAgeGroup_TEST.arff','DistalPhalanxOutlineCorrect_TEST.arff','DistalPhalanxTW_TEST.arff','Earthquakes_TEST.arff','ECG200_TEST.arff','ECG5000_TEST.arff','ECGFiveDays_TEST.arff','ElectricDevices_TEST.arff','FaceAll_TEST.arff','FaceFour_TEST.arff','FacesUCR_TEST.arff','FiftyWords_TEST.arff','Fish_TEST.arff','FordA_TEST.arff','FordB_TEST.arff','GunPoint_TEST.arff','Ham_TEST.arff','HandOutlines_TEST.arff','Haptics_TEST.arff','Herring_TEST.arff','InlineSkate_TEST.arff','ItalyPowerDemand_TEST.arff','LargeKitchenAppliances_TEST.arff','Lightning2_TEST.arff','Lightning7_TEST.arff','Mallat_TEST.arff','Meat_TEST.arff','MedicalImages_TEST.arff','MiddlePhalanxOutlineAgeGroup_TEST.arff','MiddlePhalanxOutlineCorrect_TEST.arff','MiddlePhalanxTW_TEST.arff','MoteStrain_TEST.arff','NonInvasiveFetalECGThorax1_TEST.arff','NonInvasiveFetalECGThorax2_TEST.arff','OliveOil_TEST.arff','OSULeaf_TEST.arff','PhalangesOutlinesCorrect_TEST.arff','Phoneme_TEST.arff','Plane_TEST.arff','ProximalPhalanxOutlineAgeGroup_TEST.arff','ProximalPhalanxOutlineCorrect_TEST.arff','ProximalPhalanxTW_TEST.arff','RefrigerationDevices_TEST.arff','ScreenType_TEST.arff','ShapeletSim_TEST.arff','ShapesAll_TEST.arff','SmallKitchenAppliances_TEST.arff','SonyAIBORobotSurface1_TEST.arff','SonyAIBORobotSurface2_TEST.arff','Strawberry_TEST.arff','SwedishLeaf_TEST.arff','Symbols_TEST.arff','SyntheticControl_TEST.arff','ToeSegmentation1_TEST.arff','ToeSegmentation2_TEST.arff','Trace_TEST.arff','TwoLeadECG_TEST.arff','TwoPatterns_TEST.arff','UWaveGestureLibraryAll_TEST.arff','UWaveGestureLibraryX_TEST.arff','UWaveGestureLibraryY_TEST.arff','UWaveGestureLibraryZ_TEST.arff','Wafer_TEST.arff','Wine_TEST.arff','WordSynonyms_TEST.arff','Worms_TEST.arff','WormsTwoClass_TEST.arff','Yoga_TEST.arff','ACSF1_TEST.arff','BME_TRAIN.arff','Chinatown_TEST.arff','Crop_TEST.arff','DodgerLoopDay_TEST.arff','DodgerLoopGame_TEST.arff','DodgerLoopWeekend_TEST.arff','EOGHorizontalSignal_TEST.arff','EOGVerticalSignal_TEST.arff','EthanolLevel_TEST.arff','FreezerRegularTrain_TEST.arff','FreezerSmallTrain_TEST.arff','Fungi_TEST.arff','GunPointAgeSpan_TEST.arff','GunPointMaleVersusFemale_TEST.arff','GunPointOldVersusYoung_TEST.arff','HouseTwenty_TEST.arff','InsectEPGRegularTrain_TEST.arff','InsectEPGSmallTrain_TEST.arff','MelbournePedestrian_TEST.arff','MixedShapesSmallTrain_TEST.arff','PigAirwayPressure_TEST.arff','PigArtPressure_TEST.arff','PigCVP_TEST.arff','PowerCons_TEST.arff','Rock_TEST.arff','SemgHandGenderCh2_TEST.arff','SemgHandMovementCh2_TEST.arff','SemgHandSubjectCh2_TEST.arff','SmoothSubspace_TEST.arff','UMD_TEST.arff']
w = [3,0,0,7,6,1,11,0,0,12,10,17,5,0,0,1,0,6,0,1,0,14,3,2,12,6,4,1,1,0,0,0,2,5,14,0,94,6,5,0,0,20,0,0,3,1,1,1,0,7,0,14,5,0,1,2,8,17,3,4,15,0,0,0,2,8,6,8,5,3,4,4,4,4,4,6,1,0,9,9,7,7,4,4,0,0,1,1,1,1,2,1,1,0,0,3,0,4,33,11,1,1,7,1,1,11,3,0,1,1,3,1,6]
length = [176,251,470,512,512,577,128,166,286,720,300,300,300,345,80,80,80,512,96,140,136,96,131,350,131,270,463,500,500,150,431,2709,1092,512,1882,24,720,637,319,1024,448,99,80,80,80,84,750,750,570,427,80,1024,144,80,80,80,720,720,500,512,720,70,65,235,128,398,60,277,343,275,82,128,945,315,315,315,152,234,270,900,900,426,1460,128,24,46,288,288,288,1250,1250,1751,301,301,201,150,150,150,2000,601,601,24,1024,2000,2000,2000,144,2844,1500,1500,1500,15,150]
ed = []
dtw = []
cdtw = []
ans =[]


for i in range(len(l)):

    #Loading Datasets
    np_train,np_train_label = module.load_dataset(l[i])
    np_test,np_test_label = module.load_dataset(l1[i])

    #Fourier Transform
    fft_train = module.fourier_transform(np_train)
    fft_test =module.fourier_transform(np_test)


    #Deriving Real and Imaginary Values
    fft_train= module.real_imag_phase_amp(fft_train)
    fft_test= module.real_imag_phase_amp(fft_test)

    
    
    #Handling Nan Values
    fft_test=np.nan_to_num(fft_test)
    fft_train=np.nan_to_num(fft_train)

     #Logistic Regression
    ansx = module.random_forest(fft_train,fft_test,np_train_label,np_test_label)
    print(f'{i}:{1-ansx}')
    ans.append(float("{0:.4f}".format(1-ansx)))
result =   {
    "Name" : Name,
    "Random_Forest(error)"  : ans
}   
d = pd.DataFrame(result)
d.to_csv('result_random_forest(real_imag_phase_amp).csv')
