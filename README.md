# CSV Parser Module
[![CI](https://github.com/UdarGIT829/Mistral_Completion-Base/actions/workflows/ci.yml/badge.svg)](https://github.com/UdarGIT829/Mistral_Completion-Base/actions/workflows/ci.yml)
## Overview
The is the CSV Parser module for https://github.com/UdarGIT829/Mistral_Completion-Base

## Usage
Input a CSV with headers that the LLM can assume a data type for. Examples include: Name, Temperature, Age, etc.
Also provide a user query as a string. 

The LLM will attempt to guess which column to search in then use static programming to extract the data from the LLM output and search it in the chosen CSV column using a static function.
