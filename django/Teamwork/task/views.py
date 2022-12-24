from django.shortcuts import render, HttpResponse

# Create your views here.
#!SOAP (Simple Object Access Protocol), yani Basit Nesne Erişim Protokolü daha sıkı bir güvenlik yapısıyla veri transferini sağlayan API mimarisidir. Bu mimaride veri akışı XML formatı kullanılarak sağlanır. Yapılandırması Rest API’ye göre daha zor olsa da bu mimari daha güvenli bir bağlantı sağladığı söylenir.

def artist_list(request):
  return HttpResponse("welcome")