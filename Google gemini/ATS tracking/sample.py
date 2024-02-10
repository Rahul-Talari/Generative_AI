# import io
# import pdf2image
# import base64

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         # Convert PDF to images
#         images = pdf2image.convert_from_bytes(uploaded_file.read())

#         pdf_parts = []

#         for i, image in enumerate(images):
#             # Convert to bytes
#             img_byte_arr = io.BytesIO()
#             image.save(img_byte_arr, format='JPEG')
#             img_byte_arr = img_byte_arr.getvalue()

#             pdf_parts.append({
#                 "page_number": i + 1,  # Page numbers start from 1
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             })

#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")
