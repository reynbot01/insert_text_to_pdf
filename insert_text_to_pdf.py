import fitz  # PyMuPDF

def print_form_field_names(pdf_path):
    """
    Prints the names of all form fields in a PDF.

    Args:
    - pdf_path (str): Path to the PDF file.
    """
    doc = fitz.open(pdf_path)
    counter = 1 
    for page in doc:  # Iterate through each page
        for field in page.widgets(): 
            
            print(f"{counter},Field Name: {field.field_name}, Field Type: {field.field_type_string}, Field Value: {field.field_value}")
            counter += 1

def print_form_field_names(pdf_path):
    """
    Prints the names of all form fields in a PDF and attempts to modify them.

    Args:
    - pdf_path (str): Path to the PDF file.
    """
    doc = fitz.open(pdf_path)
    
    for page in doc:  # Iterate through each page
        for field in page.widgets():  # Access form fields (widgets) on the current page
            print(f"Field Name: {field.field_name}, Field Type: {field.field_type_string}, Original Field Value: {field.field_value}")
            # Example: Changing the field value
            new_value = "may laman"  # Define the new value for the field
            try:
                field.field_value = new_value
                field.update()  # Set the new value for the field
                print(f"Updated Field Value: {field.field_value}")  # Print the updated value
            except Exception as e:
                print(f"Could not update field '{field.field_name}': {e}")

    # After modifying the fields, save the document.
    # It's important to use a different file name to preserve the original PDF.
    new_pdf_path = "C:/Users/bwdgi/OneDrive/Desktop/insert_text_to_pdf/output.pdf"
    doc.save(new_pdf_path)
    print(f"Updated PDF saved to {new_pdf_path}")

# Example usage
pdf_path = "C:/Users/bwdgi/OneDrive/Desktop/insert_text_to_pdf/sample.pdf"
print_form_field_names(pdf_path)
pdf_path = "C:/Users/bwdgi/OneDrive/Desktop/insert_text_to_pdf/sample.pdf"
print_form_field_names(pdf_path)
