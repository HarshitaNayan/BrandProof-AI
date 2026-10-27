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

def test_guideline_approval_permissions():
    admin=token('admin');creator=token('creator')
    payload={'rules':[{'kind':'term','key':'tutors','value':'mentors','source':'Approved brand guide','valid_until':''}]}
    assert client.post('/api/guidelines/approve',headers=creator,json=payload).status_code==403
    assert client.post('/api/guidelines/approve',headers=admin,json={'rules':[dict(payload['rules'][0],kind='bad')]}).status_code==400
    result=client.post('/api/guidelines/approve',headers=admin,json=payload)
    assert result.status_code==200 and result.json()['saved']==1
    vid=result.json()['ids'][0]
    assert any(v['id']==vid for v in client.get('/api/vault',headers=admin).json())
    assert client.delete(f'/api/vault/{vid}',headers=admin).status_code==200

def test_guideline_suggestions_require_admin():
    assert client.post('/api/guidelines/suggest',headers=token('creator'),json={'text':'Use mentors rather than tutors in marketing.'}).status_code==403


def test_round3_consistency_and_drift():
    a=token('admin'); c=token('creator')
    first=client.post('/api/drafts',headers=c,json={'title':'Campaign A','content':'Our batch starts on 2 November 2026. Course fee ₹6000.'}).json()['id']
    second=client.post('/api/drafts',headers=c,json={'title':'Campaign B','content':'Our batch starts on 4 November 2026. Course fee ₹5000.'}).json()['id']
    assert client.post('/api/consistency/compare',headers=c,json={'draft_ids':[first]}).status_code==422
    r=client.post('/api/consistency/compare',headers=c,json={'draft_ids':[first,second]})
    assert r.status_code==200,r.text
    topics={x['topic'] for x in r.json()['conflicts']}
    assert 'batch starts' in topics and 'course fee' in topics,r.json()
    assert client.post('/api/consistency/compare',headers=c,json={'draft_ids':[first,999999]}).status_code==404
    assert client.get('/api/drift').status_code==401
    assert client.post(f'/api/drafts/{first}/audit',headers=c).status_code==200
    radar=client.get('/api/drift',headers=a)
    assert radar.status_code==200 and radar.json()['summary']['total']>=1
