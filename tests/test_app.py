import os,tempfile
from pathlib import Path
os.environ['BRANDPROOF_DB']=str(Path(tempfile.gettempdir())/'brandproof_test_hynex.db')
from fastapi.testclient import TestClient
from main import app,analyze
client=TestClient(app)
def token(name):
    r=client.post('/api/login',json={'username':name,'password':'Demo123!'})
    assert r.status_code==200
    return {'Authorization':'Bearer '+r.json()['token']}
def test_workflow():
    a=token('admin');c=token('creator');r=token('reviewer')
    assert client.post('/api/vault',headers=c,json={'kind':'term','key':'foo','value':'bar','source':'guide'}).status_code==403
    draft=client.post('/api/drafts',headers=c,json={'title':'Test','content':'Our batch starts on 2 November 2026. Course fee ₹6000. Our teachers are the best in the city!'}).json()['id']
    audit=client.post(f'/api/drafts/{draft}/audit',headers=c).json()['findings']
    assert any(f['verdict']=='Contradicted' and f['source_id'] for f in audit)
    assert any(f['verdict'] in ('No source found','Needs human check') for f in audit)
    findings=client.get(f'/api/drafts/{draft}',headers=c).json()['findings']
    for f in findings:
        assert client.post(f"/api/findings/{f['id']}/decision",headers=c,json={'decision':'accept','comment':'reviewed'}).status_code==200
    assert client.post(f'/api/drafts/{draft}/submit',headers=c).status_code==200
    assert client.post(f'/api/drafts/{draft}/review',headers=r,json={'action':'approve','comment':'good'}).status_code==200
    assert client.get(f'/api/drafts/{draft}',headers=c).json()['draft']['status']=='approved'
def test_visual():
    r=client.post('/api/visual',headers=token('admin'),json={'foreground':'#000000','background':'#ffffff'}).json()
    assert r['ratio']==21.0
