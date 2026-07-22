import csv

suffix = '_RDNB'

fields = {
    'DUNSHierarchy': {
        "GlobalUltimateDUNS_RDNB__c": "*/attributes/DUNSHierarchy/*/value/GlobalUltimateDUNS/@@@ov@@@/@value",
        "GlobalUltimateOrganization_RDNB__c": "*/attributes/DUNSHierarchy/*/value/GlobalUltimateOrganization/@@@ov@@@/@value",
        "DomesticUltimateDUNS_RDNB__c": "*/attributes/DUNSHierarchy/*/value/DomesticUltimateDUNS/@@@ov@@@/@value",
        "DomesticUltimateOrganization_RDNB__c": "*/attributes/DUNSHierarchy/*/value/DomesticUltimateOrganization/@@@ov@@@/@value",
        "ParentDUNS_RDNB__c": "*/attributes/DUNSHierarchy/*/value/ParentDUNS/@@@ov@@@/@value",
        "ParentOrganization_RDNB__c": "*/attributes/DUNSHierarchy/*/value/ParentOrganization/@@@ov@@@/@value",
        "HeadquartersDUNS_RDNB__c": "*/attributes/DUNSHierarchy/*/value/HeadquartersDUNS/@@@ov@@@/@value",
        "HeadquartersOrganization_RDNB__c": "*/attributes/DUNSHierarchy/*/value/HeadquartersOrganization/@@@ov@@@/@value",
    },
    'KeyFinancialFiguresOverview': {
        "FinancialStatementToDate_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/FinancialStatementToDate/@@@ov@@@/@value",
        "FinancialPeriodDuration_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/FinancialPeriodDuration/@@@ov@@@/@value",
        "SalesRevenueCurrency_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/SalesRevenueCurrency/@@@ov@@@/@value",
        "SalesRevenueCurrencyCode_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/SalesRevenueCurrencyCode/@@@ov@@@/@value",
        "SalesRevenueReliabilityCode_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/SalesRevenueReliabilityCode/@@@ov@@@/@value",
        "SalesRevenueUnitOfSize_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/SalesRevenueUnitOfSize/@@@ov@@@/@value",
        "SalesRevenueAmount_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/SalesRevenueAmount/@@@ov@@@/@value",
        "ProfitOrLossCurrency_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/ProfitOrLossCurrency/@@@ov@@@/@value",
        "ProfitOrLossReliabilityText_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/ProfitOrLossReliabilityText/@@@ov@@@/@value",
        "ProfitOrLossUnitOfSize_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/ProfitOrLossUnitOfSize/@@@ov@@@/@value",
        "ProfitOrLossAmount_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/ProfitOrLossAmount/@@@ov@@@/@value",
        "SalesTurnoverGrowthRate_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/SalesTurnoverGrowthRate/@@@ov@@@/@value",
        "Sales3YryGrowthRate_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/Sales3YryGrowthRate/@@@ov@@@/@value",
        "Sales5YryGrowthRate_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/Sales5YryGrowthRate/@@@ov@@@/@value",
        "Employee3YryGrowthRate_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/Employee3YryGrowthRate/@@@ov@@@/@value",
        "Employee5YryGrowthRate_RDNB__c": "*/attributes/KeyFinancialFiguresOverview/*/value/Employee5YryGrowthRate/@@@ov@@@/@value", },

    'Identifiers': {
        "IdentifiersType_RDNB__c": "*/attributes/Identifiers/*/value/Type/@@@ov@@@/@value",
        "IdentifiersID_RDNB__c": "*/attributes/Identifiers/*/value/ID/@@@ov@@@/@value",
        "IdentifiersStatus_RDNB__c": "*/attributes/Identifiers/*/value/Status/@@@ov@@@/@value",
        "IdentifiersActivationDate_RDNB__c": "*/attributes/Identifiers/*/value/ActivationDate/@@@ov@@@/@value",
        "IdentifiersDeactivationDate_RDNB__c": "*/attributes/Identifiers/*/value/DeactivationDate/@@@ov@@@/@value",
        "IdentifiersDeactivationReasonCode_RDNB__c": "*/attributes/Identifiers/*/value/DeactivationReasonCode/@@@ov@@@/@value",
        "IdentifiersReactivationDate_RDNB__c": "*/attributes/Identifiers/*/value/ReactivationDate/@@@ov@@@/@value", },

    'OrganizationDetail': {
        "OrgDetailMemberRole_RDNB__c": "*/attributes/OrganizationDetail/*/value/MemberRole/@@@ov@@@/@value",
        "OrgDetailStandalone_RDNB__c": "*/attributes/OrganizationDetail/*/value/Standalone/@@@ov@@@/@value",
        "OrgDetailControlOwnershipDate_RDNB__c": "*/attributes/OrganizationDetail/*/value/ControlOwnershipDate/@@@ov@@@/@value",
        "OrgDetailOperatingStatus_RDNB__c": "*/attributes/OrganizationDetail/*/value/OperatingStatus/@@@ov@@@/@value",
        "OrgDetailStartYear_RDNB__c": "*/attributes/OrganizationDetail/*/value/StartYear/@@@ov@@@/@value",
        "OrgDetailFranchiseOperationType_RDNB__c": "*/attributes/OrganizationDetail/*/value/FranchiseOperationType/@@@ov@@@/@value",
        "OrgDetailBoneyardOrganization_RDNB__c": "*/attributes/OrganizationDetail/*/value/BoneyardOrganization/@@@ov@@@/@value",
        "OrgDetailOperatingStatusComment_RDNB__c": "*/attributes/OrganizationDetail/*/value/OperatingStatusComment/@@@ov@@@/@value", },

    'IndustryCode': {
        "IndustryCodeDNBCode_RDNB__c": "*/attributes/IndustryCode/*/value/DNBCode/@@@ov@@@/@value",
        "IndustryCode_RDNB__c": "*/attributes/IndustryCode/*/value/IndustryCode/@@@ov@@@/@value",
        "IndustryCodeDescription_RDNB__c": "*/attributes/IndustryCode/*/value/IndustryCodeDescription/@@@ov@@@/@value",
        "IndustryCodeLanguageCode_RDNB__c": "*/attributes/IndustryCode/*/value/IndustryCodeLanguageCode/@@@ov@@@/@value",
        "IndustryCodeWritingScript_RDNB__c": "*/attributes/IndustryCode/*/value/IndustryCodeWritingScript/@@@ov@@@/@value",
        "IndustryCodeDisplaySequence_RDNB__c": "*/attributes/IndustryCode/*/value/DisplaySequence/@@@ov@@@/@value",
        "IndustryCodeSalesPercentage_RDNB__c": "*/attributes/IndustryCode/*/value/SalesPercentage/@@@ov@@@/@value",
        "IndustryCodeType_RDNB__c": "*/attributes/IndustryCode/*/value/Type/@@@ov@@@/@value",
        "IndustryTypeCode_RDNB__c": "*/attributes/IndustryCode/*/value/IndustryTypeCode/@@@ov@@@/@value",
        "IndustryCodeImportExportAgent_RDNB__c": "*/attributes/IndustryCode/*/value/ImportExportAgent/@@@ov@@@/@value", },

    'ActivitiesAndOperations': {
        "ActAndOpLineOfBusinessDescription_RDNB__c": "*/attributes/ActivitiesAndOperations/*/value/LineOfBusinessDescription/@@@ov@@@/@value",
        "ActAndOpLanguageCode_RDNB__c": "*/attributes/ActivitiesAndOperations/*/value/LanguageCode/@@@ov@@@/@value",
        "ActAndOpWritingScriptCode_RDNB__c": "*/attributes/ActivitiesAndOperations/*/value/WritingScriptCode/@@@ov@@@/@value",
        "ActAndOpImportIndicator_RDNB__c": "*/attributes/ActivitiesAndOperations/*/value/ImportIndicator/@@@ov@@@/@value",
        "ActAndOpExportIndicator_RDNB__c": "*/attributes/ActivitiesAndOperations/*/value/ExportIndicator/@@@ov@@@/@value",
        "ActAndOpAgentIndicator_RDNB__c": "*/attributes/ActivitiesAndOperations/*/value/AgentIndicator/@@@ov@@@/@value", },

    'EmployeeDetails': {
        "IndividualEmployeeFiguresDate_RDNB__c": "*/attributes//EmployeeDetails/*/value/IndividualEmployeeFiguresDate/@@@ov@@@/@value",
        "IndividualTotalEmployeeQuantity_RDNB__c": "*/attributes/EmployeeDetails/*/value/IndividualTotalEmployeeQuantity/@@@ov@@@/@value",
        "IndividualReliabilityText_RDNB__c": "*/attributes/EmployeeDetails/*/value/IndividualReliabilityText/@@@ov@@@/@value",
        "TotalEmployeeQuantity_RDNB__c": "*/attributes/EmployeeDetails/*/value/TotalEmployeeQuantity/@@@ov@@@/@value",
        "TotalEmployeeReliability_RDNB__c": "*/attributes/EmployeeDetails/*/value/TotalEmployeeReliability/@@@ov@@@/@value",
        "PrincipalsIncluded_RDNB__c": "*/attributes/EmployeeDetails/*/value/PrincipalsIncluded/@@@ov@@@/@value"}
}

template = """"{name}": {{
  "name": "{reltio_name}",
  "template": "nestedarray",
  "attributes": {{
{attr_array}
  }}
}},"""

def get_attr_str(sfdc_name, uri):
    return """"{reltio_name}": "@@@{sfdc_name}@@@",""".format(reltio_name=uri.split('/')[-3], sfdc_name=sfdc_name)

with open('out_sf_mapping_r_s.txt', 'w') as out_mapping_file:
    for reltio_field in fields:
        sfdc_first_name = fields[reltio_field].keys()[0]
        attr_array = ''
        for sfdc_name in fields[reltio_field]:
            attr_array += "    " + get_attr_str(sfdc_name, fields[reltio_field][sfdc_name]) + '\n'

        print template.format(name=sfdc_first_name, reltio_name=reltio_field, attr_array=attr_array)
        # out_mapping_file.write(mapping_template.format(name=row[0], suffix=suffix, uri=convert_uri(row[2])) + '\n')
