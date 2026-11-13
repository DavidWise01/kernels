/**
 * ECK-054 — automatic bounded neural backtracking regression.
 * Run: node eck/test_eck054.cjs
 * Evaluates training and validation only. Final 145-case test is not consulted.
 */
const fs=require('node:fs');
const vm=require('node:vm');
const path=require('node:path');
const assert=require('node:assert/strict');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const script=html.split('<script>')[1].split('</script>')[0];
assert.ok(script);
new Function(script);
const boundaries=[
 ['const spinorStages=','function iterateSpinorSlot()'],
 ['const neuralCarrierNames=','function renderNeuralCarriers()'],
 ['const tripleCases=','function drawTripleNet()'],
 ['const temporalState=','function renderTemporal()'],
 ['const adaptState=','function adaptRender()'],
 ['const forgeEdges=','function renderForge()'],
 ['const collisionState=','function collisionRender()'],
 ['const dgState=','function dgRender()']
];
const js=boundaries.map(([from,to])=>{
 const i=script.indexOf(from),j=script.indexOf(to,i);
 assert.ok(i>=0&&j>i,from);
 return script.slice(i,j);
}).join('\n')+'\nfunction dgRender(){}';
const context=vm.createContext({});
vm.runInContext(js,context);
const report=vm.runInContext('dgBacktrackingAudit()',context);
assert.equal(report.passed,true);
assert.equal(report.spec.maxTrials,9);
assert.equal(report.runs.length,3);
assert.deepEqual(Array.from(report.runs,run=>run.checkpoint),[0,20,100]);
assert.deepEqual(Array.from(report.runs,run=>run.attempts.length),[2,2,1]);
assert.deepEqual(Array.from(report.runs,run=>run.chosen.rate),[35,35,70]);
for(const run of report.runs){
 assert.equal(run.termination,'SAFE_ACCEPT');
 assert.equal(run.finalTest,'WITHHELD');
 assert.equal(run.chosen.version,run.source.version+1);
 assert.ok(run.chosen.metrics.train<run.source.metrics.train);
 assert.ok(run.chosen.metrics.validation<=run.source.metrics.validation+1e-12);
 assert.ok(run.chosen.metrics.repeated<=run.source.metrics.repeated+1e-12);
 assert.ok(run.chosen.metrics.distinct<=run.source.metrics.distinct+1e-12);
}
const failure=vm.runInContext('dgBacktrackAtCheckpoint(20,{initialRate:70,shrink:.5,maxTrials:1,minRate:.1})',context);
assert.equal(failure.termination,'BOUNDED_EXHAUSTION');
assert.equal(failure.chosen,null);
assert.equal(failure.attempts.length,1);
assert.equal(failure.attempts[0].accepted,false);
assert.equal(failure.source.version,20);
assert.equal(vm.runInContext('dgState.final',context),null);
assert.equal(vm.runInContext('tripleTest.length',context),145);
console.log('ECK-054 PASS: rates 35, 35, 70 recovered; bounded failure at checkpoint 20; final withheld.');
