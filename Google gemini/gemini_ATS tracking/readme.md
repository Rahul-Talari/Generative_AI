Resume Expert Streamlit Application

Project Setup
    To set up the virtual environment for building the project, run the following command:  
        conda create -p venv python=3.10 -y

    After creating the virtual environment, proceed with the creation of essential files:
        constants.py: Contains the API key.
        main.py: Main application file.
        requirements.txt: Lists project dependencies.


Running the Application
    Execute the following command to run the application:
    streamlit run main.py


Project Overview
    The job application process can be overwhelming, and a rejected application without feedback can be disheartening. The Resume Expert application aims to address this issue by utilizing Google Generative AI (GEMINI) to provide users with valuable feedback on their resumes. This includes insights into missing keywords and overall resume analysis.

Objectives
    Provide an intuitive tool for job seekers to match their resumes with job descriptions.
    Leverage advanced AI technology for analyzing and providing feedback on resumes.
    Offer a user-friendly interface that simplifies the resume review process.

Features
    Resume Upload: Users can upload their resumes in PDF format.
    Job Description Input: Users can input the job description they are targeting.
    AI-Powered Analysis: Utilizing Google Generative AI (GEMINI), the application provides detailed feedback on various aspects of the resume.
    Feedback on Different Aspects:
        Resume Review: General feedback on the resume.
        Skills Improvement: Suggestions for skills enhancement.
        Keywords Analysis: Identification of missing keywords.
        Match Percentage: A percentage score indicating how well the resume matches the job description.

Technologies Used
    Streamlit: For creating the web application interface.
    Google Generative AI (Gemini Pro Vision): For processing and analyzing the resume content.
    Python: The primary programming language for backend development.
    PDF2Image & PIL: For handling PDF file conversions and image processing.

Challenges Faced
    Integration with Gemini AI: Ensuring seamless communication between the Streamlit interface and the Gemini AI model.
    PDF Handling: Efficiently converting PDF content to a format suitable for analysis by the AI model.
    User Experience Optimization: Creating an intuitive and responsive UI.

Future Enhancements
    Support for Multiple Pages: Extend the functionality to handle multi-page resumes.
    Customizable Feedback Categories: Allow users to choose specific areas for feedback.
    Interactive Resume Editing: Integrate a feature to edit the resume directly based on the AI's suggestions.
    Enhanced Error Handling: Improve the system's robustness in handling various file formats and user inputs.


Conclusion
    The Resume Expert Streamlit application serves as a significant tool in bridging the gap between job seekers and their ideal job roles. By harnessing the power of AI, it provides valuable insights and recommendations, making it a pivotal step in enhancing the job application process.



