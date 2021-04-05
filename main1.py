# importing the necessary dependencies
import pickle
import argparse
import numpy as np

if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-g", "--GREScore", required=True, help="GRE Score")
    ap.add_argument("-t", "--TOFFELScore", required=True, help="TOFFEL Score")
    ap.add_argument("-u", "--UniversityRating", required=True, help="University Rating")
    ap.add_argument("-s", "--SOP", required=True, help="SOP")
    ap.add_argument("-l", "--LOR", required=True, help="LOR")
    ap.add_argument("-c", "--CGPA", required=True, help="CGPA")
    ap.add_argument("-r", "--Research", choices=["0","1"],
                    required=True, help="Research value (0/1)")

    # args = vars(ap.parse_args())
    args = ap.parse_args()

    try:
        GRE = float(args.GREScore)
        TOFFEL = float(args.TOFFELScore)
        University= float(args.UniversityRating)
        SOP = float(args.SOP)
        LOR = float(args.LOR)
        CGPA = float(args.CGPA)
        Research = float(args.Research)



        filename = 'finalized_model.pickle'
        loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
        # predictions using the loaded model file
        prediction = loaded_model.predict([[GRE,TOFFEL,University,SOP,LOR,CGPA,Research]])
        print('Your chance of Admission is', np.round(100 * prediction,2))
        # showing the prediction results in a UI
        #return render_template('results.html', prediction=round(100 * prediction[0]))

    except Exception as e:
        print('The Exception message is: ', e)
        #return 'something is wrong'




