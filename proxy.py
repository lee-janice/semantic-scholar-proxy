import requests
from klein import run, route

SEMANTIC_SCHOLAR_BASE_URL = "https://api.semanticscholar.org/"

PAPER_ENDPOINT    = "graph/v1/paper/"
REFERENCES_BRANCH = "references/"
CITATIONS_BRANCH  = "citations/"

def setHeader(request, content_type):
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Access-Control-Allow-Methods', 'GET')
    request.setHeader('Access-Control-Allow-Headers', 'x-prototype-version,x-requested-with')
    request.setHeader('Content-type', content_type)

@route("/")
def home(request):
    return "Hello, world!"

@route("/api/paper/DOI:<doi_prefix>/<doi_suffix>/fields=<fields>", methods = ["GET"])
def paper_by_doi(request, doi_prefix, doi_suffix, fields): 
    setHeader(request,'application/json')
    print(fields)
    response = requests.get(f"{SEMANTIC_SCHOLAR_BASE_URL}{PAPER_ENDPOINT}DOI:{doi_prefix}/{doi_suffix}/?fields={fields}")
    return response.content

@route("/api/paper/SSID:<semantic_scholar_id>/fields=<fields>", methods = ["GET"])
def paper_by_ssid(request, semantic_scholar_id, fields): 
    setHeader(request,'application/json')
    response = requests.get(f"{SEMANTIC_SCHOLAR_BASE_URL}{PAPER_ENDPOINT}{semantic_scholar_id}/?fields={fields}")
    return response.content

@route("/api/references/SSID:<semantic_scholar_id>/fields=<fields>", methods = ["GET"])
def references_by_ssid(request, semantic_scholar_id, fields):
    setHeader(request,'application/json')
    response = requests.get(f"{SEMANTIC_SCHOLAR_BASE_URL}{PAPER_ENDPOINT}{semantic_scholar_id}/{REFERENCES_BRANCH}?fields={fields}")
    return response.content

@route("/api/citations/SSID:<semantic_scholar_id>/fields=<fields>", methods = ["GET"])
def citations_by_ssid(request, semantic_scholar_id, fields):
    setHeader(request,'application/json')
    response = requests.get(f"{SEMANTIC_SCHOLAR_BASE_URL}{PAPER_ENDPOINT}{semantic_scholar_id}/{CITATIONS_BRANCH}?fields={fields}")
    return response.content

run("localhost", 8080)