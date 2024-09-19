# Mapping of Field Descriptions to Unique Concepts in the LLC-network

This section describes how to set up and use the main tools adopted for concept mapping. Specifically, we will leverage the many ready-to-use tools offered by the Observational Medical Outcomes Partnership Common Data Model ([OMOP CDM]()).

Since USAGI may require a few hours to complete the first initialization, **we suggest you follow these steps at least one day before the scheduled tutorial!**

## Prerequisites

**Java**: Several OMOP tools, including USAGI and the others described below, require Java to run, so you must have **Java 8 (1.8)** (or higher) installed on your machine.
- You can check whether you already have Java installed by running the following command in a command prompt/terminal:
     ```bash
     java -version
     ```
- If nothing shows or an error appears, you can download Java from [Oracle's website](https://www.java.com/it/download/) and install it as any other application on your PC.

## Setting up USAGI

We will use USAGI to identify coded concepts from dataset field descriptions. In particular, this tool will help us map field descriptions of each hospital into standard OMOP concepts.
This first step, made by each hospital separately, will be followed by a reviewing step. In case different concepts are selected for the same field, the one judged most appropriate will be chosen as the officially adopted for that field.

### Step-by-step installation and first-time execution

1. Download the OMOP vocabularies from Athena: [OMOP Vocabularies](https://athena.ohdsi.org/vocabulary/list)
    - You must be registered on the website and logged in to visualize this page. Once done, go to the *Vocabularies* page again.
    - Keep the default vocabularies selected. In particular, check that LOINC, SNOMED, and the ones beginning with *ICD9* are marked.
    - Click on *Download vocabularies*, choose a name for the slected set (e.g., *LLCvocabularies_downloadDate*), and continue. Preparation of the set of vocabularies will start as the previous window is closed, and you will soon receive an email with the link to download the requested set. You can also inspect progress in the preparation of the vocabularies by following the link to the [Download history](https://athena.ohdsi.org/vocabulary/download-history) of your Athena account (*PENDING* will be shown for a set being prepared).
    - After completion, download the set of vocabularies from either your [Download history page](https://athena.ohdsi.org/vocabulary/download-history) or the link received by email. A single `.zip` file will be downloaded.
2. Download the latest USAGI release (only the `.jar` file) from here: [OHDSI/Usagi Releases](https://github.com/OHDSI/Usagi/releases).
3. Create a new folder (like *OMOP_USAGI*) and move the downloaded `.jar` file there, together with the `.zip` archive containing the vocabularies. Since USAGI is a portable application and there's nothing to truly "install", this folder will be the one from which you will use USAGI. Also, the indices of the vocabularies will be compiled in the same location.
4. Right-click on the `.zip` archive of the vocabularies and *Extract all* into a subfolder. After extracting the files, double-click on `Usagi_vx.x.x.jar` to launch the tool.
5. Choose an author name (e.g., Name Surname) that will be used to mark your annotations and choices in the selection of concepts. Check the *Remember me?* box and continue.
6. USAGI will prompt you to specify the location of the Vocabulary files to create the index (needs to be done only once). Pick the subfolder where you previously extracted the vocabularies. Depending on your hardware, **it will take a few hours to complete building the index**.
7. Watch the video tutorial listed below to familiarize yourself with the tool.

## Setting up White Rabbit and Rabbit In A Hat

1. Download both tools from GitHub (they are contained in the same `.zip` archive): [White Rabbit repository](https://github.com/OHDSI/WhiteRabbit/releases).
2. Unzip the downloaded `.zip` file.
3. Open the *bin* subfolder and run either White Rabbit or Rabbit In A Hat by double-clicking on their respective `.bat` files (Windows) or on the files with no extensions (Linux/Mac).

## Additional resources

- [OMOP Book](https://ohdsi.github.io/TheBookOfOhdsi/)
    - [USAGI chapter](https://ohdsi.github.io/TheBookOfOhdsi/ExtractTransformLoad.html#usagi)
    - [White Rabbit chapter](https://ohdsi.github.io/TheBookOfOhdsi/ExtractTransformLoad.html#white-rabbit)
    - [Rabbit In A Hat chapter](https://ohdsi.github.io/TheBookOfOhdsi/ExtractTransformLoad.html#rabbit-in-a-hat)
    - ACHILLES: [Data quality in general](https://ohdsi.github.io/TheBookOfOhdsi/DataQuality.html#data-quality-in-general), [how to ACHILLES](https://ohdsi.github.io/TheBookOfOhdsi/DataQuality.html#achillesInPractice)
- Video tutorials (well made and providing helpful getting started and additional information to the previous):
    - [USAGI tutorial](https://youtu.be/O65_c3UX8Zs)
    - [ACHILLES tutorial](https://youtu.be/UyS-LAUql-A)
