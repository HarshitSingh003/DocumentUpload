from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,user_id =request.user.id)
        if form.is_valid():
            document = form.save(commit=False)  # Don't save to the database yet
            document.user_id = request.user.id
            form.save()
            return redirect('document_list')  # Redirect to document list view
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})

@login_required
def document_list(request):
    print(request.user.id)
    # documents = Document.objects.all()
    documents = Document.objects.filter(user_id = request.user.id)
    return render(request, 'document_list.html', {'documents': documents})

@login_required
def download_pdf(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    # Assuming 'file' is the field name storing the uploaded PDF file
    pdf_file = document.file
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.name}.pdf"'
    return response

@login_required
def home(request):
    return render(request, 'base.html')

