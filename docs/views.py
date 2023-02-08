from django.shortcuts import render
from django.http import StreamingHttpResponse

# Create your views here.

def index(request):
    return render(request, 'docs/index.html')
    
def _download(file, type='application/octet-stream'):
    def _chunk_manager(file):
        chunk_size = 512
        with open(file, "rb") as file:
            while True:
                chuck_stream = file.read(chunk_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break
    response = StreamingHttpResponse(_chunk_manager(file))
    response['Content-Type'] = type
    if type != 'application/octet-stream':
         response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file)
    return response

def favicon(request):
    return _download('favicon.ico', type='image/x-icon')