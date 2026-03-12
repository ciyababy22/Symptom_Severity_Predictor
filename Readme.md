\# Symptom Severity Prediction Prototype



\## Overview

This project is a \*\*standalone prototype\*\* for predicting the severity of symptoms. It classifies user-entered symptoms into \*\*Low Risk, Moderate Risk, or High Risk\*\* using a \*\*rule-based scoring system\*\*.  



This module can be later integrated into healthcare applications like AI chatbots or symptom trackers.



---



\## Features

\- Rule-based symptom severity prediction  

\- Color-coded console output  

\- Detailed symptom scores  

\- Unit tested with pytest  



---



\## Folder Structure



Symptom\_Severity\_Prototype/

├── src/severity\_predictor.py # Core logic

├── app/demo\_app.py # Interactive demo

├── tests/test\_severity.py # Unit tests

├── requirements.txt # Dependencies

└── README.md # This file





---



\## Setup

1\. Clone the repository:

```bash

git clone <your-repo-url>

cd Symptom\_Severity\_Prototype



Create and activate a virtual environment:



python -m venv venv

.\\venv\\Scripts\\activate



Install dependencies:



pip install -r requirements.txt

Usage



Run the demo app:



python -m app.demo\_app



Enter your symptoms separated by commas, e.g.:



fever, cough, fatigue



Output shows:



Symptom scores



Predicted severity (Low / Moderate / High)



Advice based on risk level



Running Unit Tests

pytest -v -s



Tests check low, moderate, and high-risk scenarios with readable output.



Example Input/Output



Input:



headache, fatigue



Output:



Predicted Risk: Low Risk

Advice: Symptoms are mild. Monitor and rest.

Future Enhancements



Machine learning-based classification



Web interface or chatbot integration



Expanded symptom database for more accurate predictions



For detailed project documentation, see \[DOCUMENTATION](docs/DOCUMENTATION.md)

