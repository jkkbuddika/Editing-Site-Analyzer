# A-to-I Editing Site Finder
This python based pipeline is written to automate identifying A-to-I editing sites from RNA-seq datasets. A-to-I editing is a common form of RNA-editing that introduces changes to RNA sequence and thus structure. This form of post-transcriptional regulation is implicated in both normal develoment and disease, thus identifying such modification sites is a must to dissect biological roles of this process. In this pipeline I have integrated **Sailor**, an editing site prediction tool developed by [Yeo Lab](https://yeolab.github.io/) to automate A-to-I editing site identification. I ***highly recommend*** reading through the step-by-step user guide *carefully* before you start analyzing your data.

## Requirements
The A-to-I editing site analyzer requires following tools to be installed for data analysis.

- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) : Quality assessment
- [TagDust2](http://tagdust.sourceforge.net/) : Remove rRNA reads
- [STAR](https://github.com/alexdobin/STAR) : Mapping reads to a given genome
- [QualiMap](http://qualimap.bioinfo.cipf.es/) : Mapping quality assessment
- [MultiQC](https://github.com/ewels/MultiQC) : Summarize logs
- [Sailor](https://github.com/YeoLab/sailor) : A-to-I editing site identification

We thank developers of these valueble tools!

## Analysis process
All analyzed data will be saved onto the home directory where you deposited the *scripts* directory. The pipeline first use [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) to assess the quality of raw input files. Subsequently, [TagDust2](http://tagdust.sourceforge.net/) is being used to remove rRNA contaminants from individual datasets. A datamining module in the pipeline will summarize TagDust2 rRNA removal logs and deposit mined data onto a file named **TagDust_summary.csv** which will be saved onto a directory named *summary_files*. Subsequently, user defined genome and annotation files will be downloaded and a reference genome will be created. Next, rRNA-depleted sequences are mapped to the given genome using [STAR](https://github.com/alexdobin/STAR) genome aligner. The pipeline use [QualiMap](http://qualimap.bioinfo.cipf.es/) to assess the quality of sequence alignment. Furthermore, the pipeline integrates [MultiQC](https://github.com/ewels/MultiQC) to generate summary files in an interactive manner. Finally, mapped reads will be used to identify potential A-to-I editing sites using [Sailor](https://github.com/YeoLab/sailor), a tool developed by the Yeo Lab (click [here](https://www.cell.com/cell-reports/fulltext/S2211-1247(14)00028-X?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS221112471400028X%3Fshowall%3Dtrue#app3) for the reference). Now that you know the general outline of the analysis process, go through the step-by-step guide given [here](https://github.com/jkkbuddika/eCLIP-Data-Analyzer/blob/master/USERGUIDE.md) to analyze your RNA-seq data to identify A-to-I editing sites.
