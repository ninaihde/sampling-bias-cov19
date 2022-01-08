# Analysis of Sampling Bias in COVID-19 Metadata

This project was conducted in the winter term 2021/22 at the Hasso Plattner Institute for Digital Engineering, University of Potsdam, Germany. Its goal is to perform analyses on metadata of COVID-19 sequencing data in order to identify sampling biases. Subsequently, an approach will be developed that can remove or even avoid these biases and furthermore support the removal of the found biases in the associated sequencing data.

## Materials: EBI Metadata

The EBI metadata was retrieved from the [ENA Portal](https://www.ebi.ac.uk/ena/browser/advanced-search) by 
 - selecting data type "Nucleotide sequences" & click "next"
 - selecting "Taxonomy and related", filter for "NCBI Taxonomy", typing "Severe acute respiratory syndrome coronavirus 2", including subordinate taxa & double-click "next" to go to "Fields"
 - selecting all metadata fields & click "Search"

The definitions of the included columns can be found in [definitions_EBI_metadata.json](src/json_data/definitions_EBI_metadata.json), taken from the [API documentation of the ENA Portal](enaPortalAPI_docu.pdf) (see page 36 to 42).

## Methods

The project is divided into several Juypter Notebooks:

- [preprocess_metadata.ipynb](src/preprocess_metadata.ipynb) removes empty columns and cleans the provided metadata. It has to be executed first because it also adds several columns needed for later analysis.
- [create_general_insights.ipynb](src/create_general_insights.ipynb) generates a profiling report as HTML about all available columns and produces general insights, e.g. regarding specific biases or columns.
- [investigate_missing_values.ipynb](src/investigate_missing_values.ipynb) investigates if missing values are introduced by certain countries and creates PNGs disaggregating how many missing values exist in the different countries per column. 

Each notebook first reads a corresponding CSV and then executes various analyses on it, each of which is introduced with a heading in a Markdown cell. This means that before the cells of an analysis can be executed, the first cell of a notebook that reads the mentioned CSV must be executed first. Once this first cell has been executed, it does not have to be executed again for the cells of other analyses in this notebook.
