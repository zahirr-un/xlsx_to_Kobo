import json
import pandas as pd
import requests
import xml.etree.ElementTree as ET

# Load the configuration file.
def load_config(config_file):
    """
    Load the JSON configuration file and return the configuration dictionary.
    
    Args:
        config_file (str): Path to the JSON configuration file.

    Returns:
        dict: Configuration dictionary.
    """
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
            print("Config file loaded.")
    except FileNotFoundError:
        print("Config file not found.")
    except Exception as e:
        print("An error occurred:", str(e))
    return config

# Process the submission data and create an XML tree structure.
def process_submission(row, project_uuid):
    """
    Create an XML tree structure for the given row, matching_rows, and project_uuid.
    Add various elements to the XML tree based on the input data and return the root
    of the XML tree.

    Args:
        row (pd.Series): A row from the parent dataframe.
        matching_rows (pd.DataFrame): Matching rows from the child dataframe.
        project_uuid (str): The project UUID.

    Returns:
        xml.etree.ElementTree.Element: Root of the XML tree structure.
    """
    
    root = ET.Element('data')
    root.set('id', project_uuid)
    root.set('xmlns:orx', 'http://openrosa.org/xforms')
    root.set('xmlns:jr', 'http://openrosa.org/javarosa')

    #ET.SubElement(root, 'start').text = str(row['start'])
    #start=ET.SubElement(root, 'start')
    #start.text = '1'
    #print(str(row['start']))


    # Create elements for Name, Age, Sex, and Country
    

    ET.SubElement(root, 'start').text = str(row['start']) 
    ET.SubElement(root, 'end').text = str(row['end']) 
    group_Info = ET.SubElement(root, 'group_Info') 
    ET.SubElement(group_Info, 'Student_Code_Unique_identifier').text = str(row['Student Code Unique Identifier'])
    ET.SubElement(group_Info, 'PDA_Code').text = str(row['Partner (PDA) Code'])
    ET.SubElement(group_Info, 'proGres_Number').text = str(row['ProGres Number'])
    ET.SubElement(group_Info, 'First_Name').text = str(row['First Name/s _(as on official documents)'])
    ET.SubElement(group_Info, 'Surname_Name').text = str(row['Surname Name/s _(as on official documents)'])
    ET.SubElement(group_Info, 'Family_Code').text = str(row['Family Code_'])
    ET.SubElement(group_Info, 'other_document').text = str(row['Other Document Number'])
    ET.SubElement(group_Info, 'Father_s_Name').text = str(row['Father\'s Name'])
    ET.SubElement(group_Info, 'Gender').text = str(row['Gender'])
    ET.SubElement(group_Info, 'Year_of_Birth').text = str(row['Year of Birth'])
    ET.SubElement(group_Info, 'Country_of_Origin').text = str(row['Country of Origin raw'])
    ET.SubElement(group_Info, 'Region_of_Origin').text = str(row['Region of Origin'])
    ET.SubElement(group_Info, 'Location_Type_Where_from_CODES_tab').text = str(row['Location Type_(Where student lives) _(from \'CODES\' tab)'])
    
    group_Academic = ET.SubElement(root, 'group_Academic') 
    ET.SubElement(group_Academic, 'Year_Selected_for_DAFI_scholar').text = str(row['Year Selected for DAFI scholarship'])
    ET.SubElement(group_Academic, 'Year_of_entering_the_university').text = str(row['Year of entering the university'])
    ET.SubElement(group_Academic, 'Month_of_entering_the_university').text = str(row['Month of entering the university'])
    ET.SubElement(group_Academic, 'Expected_Year_of_Graduation_DAFI').text = str(row['Expected Date of Graduation from DAFI'])
    ET.SubElement(group_Academic, 'Expected_Month_of_Gr_tion_from_UNIVERSITY').text = str(row['Expected Month of Graduation from UNIVERSITY'])
    ET.SubElement(group_Academic, 'Graduation_Year_DAFI').text = str(row['Expected Year of Graduation from UNIVERSITY'])
    ET.SubElement(group_Academic, 'Academic_Status_Full_Name').text = str(row['Academic Status (Full Name)'])
    ET.SubElement(group_Academic, 'Current_Partnership_Agreement').text = str(row['Current Partnership Agreement'])
    ET.SubElement(group_Academic, 'Scholarship_Status_e_from_CODES_tab').text = str(row['Scholarship Status _(Active/ Inactive)_(from \'CODES\' tab)'])
    ET.SubElement(group_Academic, 'Field_Of_Study_Full_Name').text = str(row['Field Of Study (Full Name)'])
    ET.SubElement(group_Academic, 'Actual_Degree_Name').text = str(row['Actual Degree Name'])
    ET.SubElement(group_Academic, 'Degree_Type_University_Level_or_TVET').text = str(row['Degree Type_(University Level or TVET)'])
    ET.SubElement(group_Academic, 'Total_Number_of_Semesters').text = str(row['Total Number of Semesters'])
    ET.SubElement(group_Academic, 'Past_Degree_types_in_Dafi').text = str(row['Past Degree types in Dafi'])
    ET.SubElement(group_Academic, 'Total_GPA').text = str(row['Total GPA'])
    
    group_BA = ET.SubElement(root, 'group_BA') 
    ET.SubElement(group_BA, 'BA_Medical_Non_Medical_study').text = str(row['BA Medical or Non-medical'])
    ET.SubElement(group_BA, 'BA_Name_of_Higher_Education').text =  str(row['BA Name of Higher _Education Institution'])
    ET.SubElement(group_BA, 'BA_University_Type').text = str(row['BA University Type'])
    ET.SubElement(group_BA, 'BA_Actual_Degree_Name').text = str(row['BA Actual Degree Name'])
    ET.SubElement(group_BA, 'BA_Field_Of_Study_Full_Name').text = str(row['BA Field Of Study (Full Name)'])
    ET.SubElement(group_BA, 'BA_Year_Selected_for_DAFI').text = str(row['BA Year Selected for DAFI scholarship'])

    group_MA = ET.SubElement(root, 'group_MA') 
    ET.SubElement(group_MA, 'MA_Medical_Non_Medical_study').text = str(row['MA Medical or Non-medical'])
    ET.SubElement(group_MA, 'MA_Name_of_Higher_Education').text = str(row['MA Name of Higher _Education Institution'])
    ET.SubElement(group_MA, 'MA_University_Type').text = str(row['MA University Type'])
    ET.SubElement(group_MA, 'MA_Actual_Degree_Name').text = str(row['MA Actual Degree Name'])
    ET.SubElement(group_MA, 'MA_Field_Of_Study_Full_Name').text = str(row['MA Field Of Study (Full Name)'])
    ET.SubElement(group_MA, 'MA_Year_Selected_for_DAFI').text = str(row['MA Year Selected for DAFI scholarship'])



    group_AA = ET.SubElement(root, 'group_AA') 
    ET.SubElement(group_AA, 'AA_Medical_Non_Medical_study').text = str(row['AA Medical or Non-medical'])
    ET.SubElement(group_AA, 'AA_Name_of_Higher_Education').text = str(row['AA Name of Higher _Education Institution'])
    ET.SubElement(group_AA, 'AA_University_Type').text = str(row['AA University Type'])
    ET.SubElement(group_AA, 'AA_Actual_Degree_Name').text = str(row['AA Actual Degree Name'])
    ET.SubElement(group_AA, 'AA_Field_Of_Study_Full_Name').text = str(row['AA Field Of Study (Full Name)'])
    ET.SubElement(group_AA, 'AA_Year_Selected_for_DAFI').text = str(row['AA Year Selected for DAFI scholarship'])



    group_AS = ET.SubElement(root, 'group_AS')  
    ET.SubElement(group_AS, 'AS_Medical_Non_Medical_study').text = str(row['AS Medical or Non-medical'])
    ET.SubElement(group_AS, 'AS_Name_of_Higher_Education').text = str(row['AS Name of Higher _Education Institution'])
    ET.SubElement(group_AS, 'AS_University_Type').text = str(row['AS University Type'])
    ET.SubElement(group_AS, 'AS_Actual_Degree_Name').text = str(row['AS Actual Degree Name'])
    ET.SubElement(group_AS, 'AS_Field_Of_Study_Full_Name').text = str(row['AS Field Of Study (Full Name)'])
    ET.SubElement(group_AS, 'AS_Year_Selected_for_DAFI').text = str(row['AS Year Selected for DAFI scholarship'])

    group_contact = ET.SubElement(root, 'group_contact')  


    ET.SubElement(group_contact, 'Province').text = str(row['Province'])
    ET.SubElement(group_contact, 'Phone_Numbers').text = str(row['Phone Number'])
    ET.SubElement(group_contact, 'Email_Address').text = str(row['EMAIL'])
    ET.SubElement(group_contact, 'address').text = str(row['ADDRESS'])
    ET.SubElement(group_contact, 'Comment_Level_1').text = str(row['Comment- Level 1'])
    ET.SubElement(group_contact, 'Comment_Level_2').text = str(row['Comment- Level 2'])
    

    # Although Kobo may accept the submission without this meta element, it is highly recommended by OpenRosa
    meta = ET.SubElement(root, 'meta')
    meta_instanceID = ET.SubElement(meta, 'instanceID')
    meta_instanceID.text = project_uuid

    return root


# Main function that drives the script.
def main():
    """
    Main function that reads Excel data into Pandas dataframes, iterates through
    the rows, creates XML entries, and posts them to the KoBoToolbox server.

    Steps:
    1. Load the configuration from the 'config.json' file.
    2. Read Excel data into Pandas dataframes for parent and child data.
    3. Construct the endpoint URL and headers for API requests to KoBoToolbox.
    4. Iterate through the rows in the parent dataframe, find the matching rows 
       in the child dataframe, and process the submissions by creating XML entries.
    5. Send the XML submission data to the KoBoToolbox server using HTTP POST requests.
    6. Print the submission status and response from the server.
    """
        
    config = load_config('config.json')
    #print (config)
    #loads excel data into pandas dataframe
    try:
        df_root = pd.read_excel(config['parent_data_path'])
    except FileNotFoundError:
        print("Excel file not found.")
    except Exception as e:
        print("An error occurred:", str(e))

    endpoint = 'https://kobocat.unhcr.org/api/v1/submissions'
    headers = {'Authorization': f"Token {config['api_token']}"}

    # Iterate, create and post xml entry to KoBo
    for i, row in df_root.iterrows():
        root = process_submission(row, config['project_uuid'])

        xml_string = ET.tostring(root, encoding='utf-8', method='xml')
        #print (xml_string)
 
        payload = {'xml_submission_file': ('data.xml', xml_string, 'text/xml')}
        try:
            response = requests.post(endpoint, headers=headers, files=payload)
            print(f'Submission {i}: {response.status_code} {response.text}')
        except requests.exceptions.RequestException as e:
            print("An error occurred during the request:", str(e))

# Entry point for the script.
if __name__ == '__main__':
    main()