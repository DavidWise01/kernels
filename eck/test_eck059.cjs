/**
 * ECK-059: independent continuous-phase evidence audit.
 * Usage: node eck/test_eck059.cjs
 * Loads actual committed ECK model code, freezes nine selector outputs,
 * then scores a separate generated continuous domain. Final 145 cases sealed.
 */
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const source=fs.readFileSync(path.join(__dirname,'index.html'),'utf8').split('<script>')[1].split('</script>')[0];
new Function(source);
const bounds=[
 ['const spinorStages=','function iterateSpinorSlot()'],
 ['const neuralCarrierNames=','function renderNeuralCarriers()'],
 ['const tripleCases=','function drawTripleNet()'],
 ['const temporalState=','function renderTemporal()'],
 ['const adaptState=','function adaptRender()'],
 ['const forgeEdges=','function renderForge()'],
 ['const nState=','function nRender()'],
 ['const shiftState=','function shiftRender()'],
 ['const seedLab=','function renderSeedLab()'],
 ['const collisionState=','function collisionRender()'],
 ['const dgState=','function dgRender()'],
 ['const rankSpec=','function rankRender()'],
 ['const robustSpec=','function robustRender()'],
 ['const evidenceProtocol=','function evidenceRender()']
];
const modules=bounds.map(([a,b])=>{
 const i=source.indexOf(a),j=source.indexOf(b,i);
 assert.ok(i>=0&&j>i,'expected section '+a);
 return source.slice(i,j);
});
const context=vm.createContext({});
vm.runInContext(modules.join('\n')+'\nfunction robustRender(){}\nfunction evidenceRender(){}',context);
const report=vm.runInContext('evidenceAudit()',context);
assert.equal(report.passed,true);
assert.equal(report.models.length,9);
assert.equal(report.protocol.id,'ECK059_CONTINUOUS_PHASE_TRANSFER_V1');
assert.equal(report.protocol.count,81);
assert.equal(report.protocol.phaseCount,3);
assert.equal(report.protocol.existingFinal,'WITHHELD');
assert.equal(vm.runInContext('evidenceProbes.length',context),81);
assert.equal(vm.runInContext('evidenceProbes.every(p=>p.planes.length===3&&p.planes.every(a=>a.length===9&&a.every(v=>v>0&&v<1)))',context),true);
assert.equal(vm.runInContext('tripleTrain.length',context),438);
assert.equal(vm.runInContext('tripleValid.length',context),146);
assert.equal(vm.runInContext('tripleTest.length',context),145);
assert.equal(vm.runInContext('dgState.final',context),null);
assert.equal(vm.runInContext('robustState.result.runs.every(r=>r.test==="WITHHELD")',context),true);
const by=(seed,policy)=>report.models.find(x=>x.seed===seed&&x.policy===policy);
for(const seed of [0,1,2]){
 for(const policy of ['fixed','ranked','gradient']){
  const row=by(seed,policy);
  assert.ok(row);
  assert.equal(row.modelFrozen,true);
  assert.equal(row.finalPartition,'WITHHELD');
  assert.equal(row.candidateEvaluations,40);
  assert.ok(Number.isFinite(row.newEvaluation));
 }
}
const mean=p=>report.models.filter(x=>x.policy===p)
 .reduce((sum,x)=>sum+x.newEvaluation,0)/3;
assert.ok(Math.abs(mean('fixed')-0.0003851160254176479)<1e-12);
assert.ok(Math.abs(mean('ranked')-0.00037982287564975923)<1e-12);
assert.ok(Math.abs(mean('gradient')-0.0003864749274579595)<1e-12);
assert.ok(mean('ranked')<mean('fixed'));
assert.ok(mean('ranked')<mean('gradient'));
const trial=vm.runInContext('evidenceProbes[0]',context);
const frozen=vm.runInContext('robustState.result.runs[0].frozenModel',context);
const m=vm.runInContext('evidenceMSE(robustState.result.runs[0].frozenModel)',context);
assert.ok(Number.isFinite(m));
assert.ok(Object.isFrozen(trial));
assert.ok(Object.isFrozen(frozen));
console.log('ECK-059 PASS: 9 frozen models x 81 new continuous-phase synthetic probes; final 145 unopened.');
console.log('Means: fixed',mean('fixed'),'ranked',mean('ranked'),'gradient',mean('gradient'));
