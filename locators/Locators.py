class Locators(object):
    # Login
    logo = '/html/body/div/div/div[1]/div/h2'
    tag_line = '/html/body/div/div/div[1]/div/h6[1]'
    version = '/html/body/div/div/div[1]/div/h6[2]'

    username = '//*[@id="UserName"]'
    password = '//*[@id="Password"]'
    login = '/html/body/div/div/div[2]/div/form/input[2]'

    # Dashboard
    advance_search_xpath = "input[id='2']"
    full_text_search = '//*[@id="fullTextSearch"]'
    search_text = '//*[@id="SearchText"]'
    is_exactly = '//*[@id="matchingCriteria"]'
    table_row = '//*[@id="SearchDataTable"]/tbody/tr[1]/td[2]'
    search_result_first_product = '//*[@id="product_0"]'
    advanced = '//*[@id="2"]'
    vendor_name = '//*[@id="select2-vendorName-container"]'
    vendor_name_input = '/html/body/span/span/span[1]/input'

    vendor_name_select = '//*[@id="select2-vendorName-results"]'
    product_category_from = '//*[@id="select2-completeFrom-container"]'
    product_category_from_input = '/html/body/span/span/span[1]/input'

    product_category_to = '//*[@id="select2-completeTo-container"]'
    product_category_to_input = '/html/body/span/span/span[1]/input'

    bulk_vendor = '//*[@id="catalogVendorProductPricing"]'



    bulk_vendor_dropdown = '//*[@id="map"]/div/div[2]/ul'
    bulk_vendor_table_row = '//*[@id="hot-bulk-vendor-product"]/div[1]/div/div/div/table/tbody/tr[3]'
    bulk_vendor_save = '//*[@id="btn-save"]'
    bulk_vendor_successful = '/html/body/div[1]/div[4]/div/div'

    bulk_item = '//*[@id="bulkItemSet"]'
    bulk_item_load_all = '//*[@id="btnCustomFieldUpdateAll"]'
    bulk_item_update_wait = '//*[@id="hot-custom-field-update"]/div[3]/div/div/div/table/tbody/tr[3]'
    bulk_item_update_made_in_usa_dropdown = '//*[@id="hot-custom-field-update"]/div[1]/div/div/div/table/tbody/tr[1]/td[2]/div'
    bulk_item_update_second_column = '//*[@id="hot-custom-field-update"]/div[1]/div/div/div/table/tbody/tr[1]/td[2]'
    bulk_item_update_right_click_table = '//div[contains(@class, "htMenu htContextMenu handsontable")]'
    choose_field = '//*[@id="select2-CustomFields-container"]'
    choose_field_input = '/html/body/span/span/span[1]/input'
    add_to_grid = '//*[@id="add-custom-field"]'
    bulk_item_update_table = '//*[@id="hot-custom-field-update"]/div[4]/div'
    hands_on_table = '//*[@id="hot-custom-field-update"]/div[1]/div/div/div/table/tbody/tr[3]'
    save_bulk_item_update = '//*[@id="btn-save"]'

    success_message = '/html/body/div[1]/div[6]/div/div'

    link = '//*[@id="product_0"]'
    product_name = '//*[@id="Name"]'
    local_part_number = '//*[@id="LocalSku"]'
    alt_spec = '//*[@id="customfieldbygroup-accordion"]/div[2]/div[1]'
    competitor_data = '//*[@id="customfieldbygroup-accordion"]/div[6]/div[1]/h3/a'
    airbus = '//*[@id="154"]'
    manufacture = '//*[@id="43"]'
    pricing_vendor = '/html/body/div[1]/div[2]/div/form/div[1]/div[2]/div[1]/ul/li[2]'
    product_cost = '//*[@id="Cost"]'

    general = '/html/body/div[1]/div[2]/div/form/div[1]/div[2]/div[1]/ul/li[1]'

    save_product_cost = '//*[@id="EditProductCatalog"]'

    loading_message = '/html/body/div[4]/div/div/div[1]/i'

    # Store
    store_data_table = '/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]'
    add_data_source = '//*[@id="btnAddDataSource"]'
    file_type = '//*[@id="connection_manager_source_type"]'
    choose_file_mapping = '//*[@id="data_source_file_upload"]'
    source_name = '//*[@id="txtImportSourceName"]'
    save = '//*[@id="btnDataSourceSave"]'

    abstract = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[1]/td[3]'
    accessories = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[2]/td[3]'
    asin = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[3]/td[3]'
    color = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[4]/td[3]'
    desc = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[5]/td[3]'
    id = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[6]/td[3]'
    name = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[7]/td[3]'
    parentsku = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[8]/td[3]'
    price = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[9]/td[3]'
    sale_price = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[10]/td[3]'
    save_mapping = '//*[@id="btnImportPlatformMappingSave"]'

    select_file = '//*[@id="cb_import_source_2081"]'

    import_file = '//*[@id="btnImport"]'
    conform_import = '//*[@id="btn_import_mode_upload_file_only"]'
    choose_file_import = '//*[@id="fileuploadInput"]'
    import_data = '//*[@id="butnImportSourcefileYes"]'

    move_mouse = '//*[@id="tableImportPlatformMapping"]/div[1]/div/div/div/table/tbody/tr[1]/td[2]'
    floating_input = '/html/body/span/span/span[1]/input'
    preview_table = '//*[@id="previewTable"]/thead'

    logout = "/html/body/div[1]/header/div[1]/div[1]/a[2]"


    #productpage
    product_name = '//*[@id="Name"]'
    expand_all_tab = '//*[@id="customfieldbygroup-accordion"]/a'
    altspec_tab = '//*[@id="customfieldbygroup-accordion"]/div[4]/div[1]/h3/a'
    altspec_airbus_pn = '//*[@id="154"]'
    altspec_manufacture_pn = '//*[@id="43"]'
    item_technical_specs_tab = '//*[@id="customfieldbygroup-accordion"]/div[8]/div[1]/h3/a'
    item_technical_materials = '//*[@id="107"]'
    save_product_warning_window ='//*[@id="SpqQplDoNotMatchModal"]/div/div'
    save_product_warning_window_yes = '//*[@id="btnYesSpqQplDoNotMatchModal"]'
    save_product_alert_success = '//div[contains(@class, "alert alert-success")]'
    save_product_loading = '/html/body/div[4]/div/div/div[2]'


