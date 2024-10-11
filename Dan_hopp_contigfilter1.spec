/*
A KBase module: Dan_hopp_contigfilter1
This sample module contains one small method that filters contigs.
*/

module Dan_hopp_contigfilter1 {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_Dan_hopp_contigfilter1(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
