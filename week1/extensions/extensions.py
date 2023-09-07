cleaned_input = input("File name: ").lower().strip()

if cleaned_input.endswith(".gif"):
    mime_type = "image/gif"
elif cleaned_input.endswith(".jpg") or cleaned_input.endswith(".jpeg"):
    mime_type = "image/jpeg"
elif cleaned_input.endswith(".pdf"):
    mime_type = "application/pdf"
elif cleaned_input.endswith(".png"):
    mime_type = "image/png"
elif cleaned_input.endswith(".txt"):
    mime_type = "text/plain"
elif cleaned_input.endswith(".zip"):
    mime_type = "application/zip"
else:
    mime_type = "application/octet-stream"

print (mime_type)
