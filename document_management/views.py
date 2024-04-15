from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')  # Redirect to document list view
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def download_pdf(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    # Assuming 'file' is the field name storing the uploaded PDF file
    pdf_file = document.file
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.name}.pdf"'
    return response

def home(request):
    return render(request, 'base.html')

