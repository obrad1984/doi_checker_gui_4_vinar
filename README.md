# DOI Checker GUI Project

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15484349.svg)](https://doi.org/10.5281/zenodo.15484349)  


This project provides a graphical user interface (GUI) for checking the existence of Digital Object Identifiers (DOIs) in the VinaR repository. Users can input a DOI and check its existence repeatedly until they decide to stop.

## Project Structure

```
doi_checker_gui_project
├── src
│   ├── doi_checker_may_2025.py  # Contains the function to check DOI existence
│   ├── gui.py                    # Implements the GUI for user interaction
├── requirements.txt              # Lists the project dependencies
└── README.md                     # Documentation for the project
```

## Requirements

To run this project, you need to install the following dependencies:

- requests
- tkinter (or PyQt, depending on the GUI framework used)

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies as mentioned above.
4. Run the GUI application:

```
python src/gui.py
```

5. Input the DOI you want to check in the provided field and click the check button. The application will inform you whether the DOI exists in the VinaR database.
6. You can continue checking DOIs until you decide to exit the application.

## Author

Obrad Vučkovac  
[ORCID](https://orcid.org/0000-0001-5616-2680)

## Zenodo release

Vučkovac, O. (2025). DOI Checker GUI (v1.1.1). Zenodo. https://doi.org/10.5281/zenodo.15484349  
