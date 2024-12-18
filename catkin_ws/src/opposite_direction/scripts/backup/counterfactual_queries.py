#!/usr/bin/env python3

import sys
from re import search
import csv
from counterfactuals.counterfactualprogram import CounterfactualProgram
import aspmc.config as config
from aspmc.main import logger as aspmc_logger
import itertools
import time

global program_files
global program_str
global program 
global cBN_file

def load_program(cBN):
    global program_files, program_str, program, cBN_file

    cBN_file = cBN
    program_files = []
    program_str = ""
    program_files.append(cBN)
    program = CounterfactualProgram(program_str, program_files)
    string = "Program " + cBN + " loaded"
    print(string)


# Main execution
def query_twin_networks(observations):
    global program_files, program_str, program, cBN_file
    
    iactions = ['cruise', 'keep', 'change_to_left', 'change_to_right', 'swerve_left', 'swerve_right']
    iaction_truth = [(True,False,False,False,False,False), (False,True,False,False,False,False),(False,False,True,False,False,False), (False,False,False,True,False,False),(False,False,False,False, True,False),(False,False,False,False, False,True)]
        
    evidence = {}
    interventions = {}
    queries = []
    probabilities = {}

    # Add evidence     
    for name, value in observations.items():
       if name == 'action':
          name = 'action(' + value + ')' 
          value = True

       phase = False if value == True else True
       evidence[name] = phase
    
    # Config
    config.config["knowledge_compiler"] = "sharpsat-td"
    aspmc_logger.setLevel("ERROR")
    # Add query
    queries.append("latent_collision")    

    # Add interventions 
    for idx in range(len(iactions)):

       # Add interventions 
       iaction = iactions[idx]
       iaction_str = ""
       action_idx = iactions.index(iaction)
       for i in range(len(iactions)):
          name = 'action(' + iactions[i] + ')'
          value = iaction_truth[action_idx][i]
          phase = False if value == True else True
          interventions[name] = phase
          iaction_str = iaction_str + " -i " + 'action\(' + iactions[i] + '\)' + "," + str(value) 
          
       try:
         start_time = time.time() 
         # Do the query  
         output_query = []
         output_query = program.single_query(interventions, evidence, queries, strategy=config.config["knowledge_compiler"])
         end_time = time.time()             
         elapsed_time = end_time - start_time 
         print("Counterfactual query took: ", elapsed_time, flush=True)
       except Exception as inst:
         print(type(inst))    
         print(inst.args)     
         print(inst) 
         
       print("Evidence: ", evidence, flush=True)
       print("Intervention: ", interventions, flush=True)
       print("Query: ", queries, flush=True)
 
       prob = float(output_query[0]) 
       probabilities[iaction] = prob     
                    

    return probabilities
