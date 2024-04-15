from django.test import TestCase, Client
from django.urls import reverse
from .models import Document
from .forms import DocumentForm

class DocumentUploadTestCase(TestCase):
    def test_upload_document(self):
        client = Client()
        upload_url = reverse('upload_document')
        
        # Mock a POST request with valid form data
        with open('test_document.pdf', 'rb') as pdf_file:
            response = client.post(upload_url, {'name': 'Test Document', 'file': pdf_file})
        
        self.assertEqual(response.status_code, 302)  # Check for successful redirect
        
        # Verify that the document is saved
        self.assertTrue(Document.objects.filter(name='Test Document').exists())

    def test_document_list_view(self):
        client = Client()
        document_list_url = reverse('document_list')
        response = client.get(document_list_url)
        
        self.assertEqual(response.status_code, 200)  # Check for successful response
        self.assertContains(response, 'Test Document')  # Check if document is listed

    def test_download_pdf(self):
        client = Client()
        document = Document.objects.create(name='Test Document', file='test_document.pdf')
        download_url = reverse('download_pdf', kwargs={'document_id': document.id})
        response = client.get(download_url)
        
        self.assertEqual(response.status_code, 200)  # Check for successful response
        self.assertEqual(response['Content-Type'], 'application/pdf')  # Check for PDF content type
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{document.name}.pdf"'
        )  # Check for correct filename in response

    def test_home_view(self):
        client = Client()
        home_url = reverse('home')
        response = client.get(home_url)
        
        self.assertEqual(response.status_code, 200)  # Check for successful response
        self.assertTemplateUsed(response, 'base.html')  # Check if base.html template is used

    # Add more test cases as needed, such as edge cases and security tests
