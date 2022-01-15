# Analysis of Sampling Bias in COVID-19 Metadata

This project was conducted in the winter term 2021/22 at the Hasso Plattner Institute for Digital Engineering, University of Potsdam, Germany. Its goal is to perform analyses on metadata of COVID-19 sequencing data in order to identify sampling biases. Subsequently, an approach will be developed that can remove or even avoid these biases and furthermore support the removal of the found biases in the associated sequencing data.

## Materials
### EBI Metadata

The EBI metadata was retrieved from the [ENA Portal](https://www.ebi.ac.uk/ena/browser/advanced-search) by 
 - selecting data type "Nucleotide sequences" & click "next"
 - selecting "Taxonomy and related", filter for "NCBI Taxonomy", typing "Severe acute respiratory syndrome coronavirus 2", including subordinate taxa & double-click "next" to go to "Fields"
 - selecting all metadata fields & click "Search"

The definitions of the included columns can be found in [definitions_EBI_metadata.json](src/json_data/definitions_EBI_metadata.json), taken from the [API documentation of the ENA Portal](enaPortalAPI_docu.pdf) (see page 36 to 42).

### GISAID Metadata

The GISAID metadata was retrieved as a JSON file via an internal API access to the [GISAID database](https://www.epicov.org/epi3/).

### Infection Data by the John Hopkins University

The data used to integrate the number of infections (per country or per U.S. State) in our analyses is provided by the  [Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)](https://systems.jhu.edu/). It can be found in the corresponding [GitHub repository of the JHU CSSE](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data).

## Methods

The project is divided into several Juypter Notebooks. If the notebook name does not explicitly state whether it works with EBI or GISAID metadata, the former is the case:

  - [preprocess_metadata.ipynb](src/preprocess_metadata.ipynb) removes empty columns and cleans the provided metadata. It has to be executed first because it also adds several columns needed for later analysis.
  - [create_general_insights.ipynb](src/create_general_insights.ipynb) generates a profiling report as HTML about all available columns and produces general insights, e.g. regarding specific biases or columns.
  - [analyze_missing_values.ipynb](src/analyze_missing_values.ipynb) investigates if missing values are introduced by certain countries and creates PNGs disaggregating how many missing values exist in the different countries per column. 
  - [analyze_us_states.ipynb](src/analyze_us_states.ipynb) extracts the U.S. States from the "region" column and analyzes the number of samples per U.S. State in relation to the respective number of inhabitants and infections of the state. 
  - [investigate_gisaid_metadata.ipynb](src/investigate_gisaid_metadata.ipynb) converts the given JSON file to a TSV file and generates some general insights about the GISAID metadata.

All notebooks dealing with the EBI metadata read a CSV at first and execute various analyses on it afterwards, each of which is introduced with a heading in a Markdown cell. This means that before the cells of an analysis can be executed, the first cell of such a notebook that reads the mentioned CSV must be executed first. Once this first cell has been executed, it does not have to be executed again for the cells of other analyses in this notebook - meaning each analysis, if any, enriches this CSV without changing the original data.
